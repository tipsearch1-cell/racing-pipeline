"""Rebuilt models (10 Nov 2026), all built from data/history_runs.csv.gz only.

  python3 pipeline/models.py train            -> models/win_model.json (+ validation print)
  python3 pipeline/models.py run DAY           -> store/DAY/model.json (p, style, lead, shape, hist, pros, cons, h2h)

Win model: conditional logit (softmax within a race), separate Flat / Jumps coefficients. Features come only from a
horse's earlier runs in the history table plus today's official rating and weight, all relative to the race:
earlier Betfair SP (market rating), finishing positions, run count, days off, last-time win, non-completions,
official rating and weight. It does NOT use today's market, so it can disagree with it.
Early-position model: each past in-running comment is classed Leader / Prominent / Midfield / Held up; a runner's
style is the average of its last 4 classed runs; lead = smoothed share of runs it led. Race shape from the number of
likely leaders (same labels as the old page).
"""
import json, math, os, re, sys
import numpy as np
import pandas as pd
from scipy.optimize import minimize

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import p, load_card, code_of, load_json  # noqa: E402
from history import load as load_hist, norm  # noqa: E402

MODEL = p("models", "win_model.json")
FEATS = ["mkt_rel", "mkt_na", "pos_rel", "pos_na", "or_rel", "or_na", "lbs_rel", "log_runs", "days_long", "days_short",
         "first", "won_last", "nonfin"]

LEAD_RE = re.compile(r"^(made all|made virtually all|made most|led|made the running|set the pace|front from|took (the )?lead|"
                     r"went on|in front|disputed (the )?lead|vied for (the )?(front|lead|top)|sent to the front|took charge|"
                     r"jumped (off|out) in front|bounced out in front)")
PROM_RE = re.compile(r"(prominent|up with the pace|with the pace|chased (the )?leaders?|tracked|close up|handy|pressed|"
                     r"in touch|chased|with leaders?|up with|upsides|near the front|front rank|disputed|vied)")
MID_RE = re.compile(r"(mid|in the pack|middle|centre of|center of|among the pack|in touch with the pack)")
HOLD_RE = re.compile(r"(held up|rear|at the back|towards the back|behind|dropped out|in last|settled last|detached|"
                     r"slowly away|missed the break|outpaced early|backmarker|tailed)")
STYLE_SCORE = {"Leader": 4, "Prominent": 3, "Midfield": 2, "Held up": 1}


def early_class(c):
    if not isinstance(c, str) or not c.strip():
        return None
    s = c.strip().lower()
    first = re.split(r" - |, |; ", s)[0]
    if "made all" in s[:40] or LEAD_RE.search(first):
        return "Leader"
    for rx, lab in ((HOLD_RE, "Held up"), (PROM_RE, "Prominent"), (MID_RE, "Midfield")):
        if rx.search(first):
            return lab
    return None


def pos_num(x):
    try:
        return int(float(x))
    except (TypeError, ValueError):
        return None


def prior_features(H):
    """H: rows sorted by hkey, date. Adds per-row features from that horse's EARLIER rows only."""
    H = H.sort_values(["hkey", "date", "race_key"]).reset_index(drop=True)
    for c in ("n", "bsp", "or", "lbs", "fig", "spd", "dist_f", "ovr_btn", "btn"):
        H[c] = pd.to_numeric(H[c], errors="coerce")
    H["is_target"] = H.is_target.astype(bool)
    H["dt"] = pd.to_datetime(H.date)
    pn = H.pos.map(pos_num)
    H["posscore"] = np.where(pn.notna() & (H.n > 1), 1 - (pn.fillna(1) - 1) / (H.n.clip(lower=2) - 1), np.where(pn.isna() & H.pos.notna(), 0.0, np.nan))
    H.loc[H.is_target, "posscore"] = np.nan
    H["imp"] = np.log((H.n.clip(lower=2)) / H.bsp.where(H.bsp > 1))
    H.loc[H.is_target, "imp"] = np.nan
    H["won"] = (pn == 1).astype(float).where(~H.is_target)
    H["nf"] = (pn.isna() & H.pos.notna() & ~H.pos.astype(str).isin(["", "nan"])).astype(float).where(~H.is_target)
    g = H.groupby("hkey", sort=False)
    H["runs_before"] = g.cumcount()
    H["prev_dt"] = g.dt.shift(1)
    sh = lambda col, k: g[col].shift(k)  # noqa: E731
    imp1, imp2 = sh("imp", 1), sh("imp", 2)
    H["mkt_prev"] = pd.concat([imp1, imp2], axis=1).mean(axis=1)
    H["pos_prev"] = pd.concat([sh("posscore", 1), sh("posscore", 2), sh("posscore", 3)], axis=1).mean(axis=1)
    H["won_last"] = sh("won", 1).fillna(0)
    H["nonfin"] = pd.concat([sh("nf", 1), sh("nf", 2), sh("nf", 3)], axis=1).sum(axis=1)
    H["days"] = (H.dt - H.prev_dt).dt.days
    return H


def race_relative(X):
    X = X.copy()
    grp = X.groupby("race_key")
    for c, out in (("mkt_prev", "mkt_rel"), ("pos_prev", "pos_rel"), ("or", "or_rel"), ("lbs", "lbs_rel")):
        m = grp[c].transform("mean")
        X[out] = (X[c] - m).fillna(0)
        if out in ("mkt_rel", "pos_rel", "or_rel"):
            X[out.replace("_rel", "_na")] = X[c].isna().astype(float)
    X["or_rel"] = X.or_rel / 10
    X["lbs_rel"] = X.lbs_rel / 10
    X["log_runs"] = np.log1p(X.runs_before)
    X["days_long"] = (X.days >= 90).astype(float)
    X["days_short"] = (X.days <= 10).astype(float)
    X["first"] = X.days.isna().astype(float)
    return X


def fit(X, y, rk, l2=1.0):
    Xv = X[FEATS].values.astype(float)
    codes, idx = np.unique(rk, return_inverse=True)

    def nll(w):
        s = Xv @ w
        mx = pd.Series(s).groupby(idx).transform("max").values
        e = np.exp(s - mx)
        den = np.bincount(idx, weights=e)
        lp = s - mx - np.log(den[idx])
        g_p = e / den[idx]
        grad = -(Xv.T @ (y - g_p)) + l2 * w
        return -(lp * y).sum() + 0.5 * l2 * (w @ w), grad

    r = minimize(nll, np.zeros(len(FEATS)), jac=True, method="L-BFGS-B")
    return r.x


def predict(X, w):
    s = X[FEATS].values.astype(float) @ np.array(w)
    s = pd.Series(s, index=X.index)
    e = np.exp(s - s.groupby(X.race_key).transform("max"))
    return e / e.groupby(X.race_key).transform("sum")


def training_frame():
    H = load_hist()
    H["is_target"] = False
    H = prior_features(H)
    H = H[H.n >= 4]
    wins = H.assign(w=(H.pos.map(pos_num) == 1)).groupby("race_key").w.sum()
    H = H[H.race_key.isin(wins[wins == 1].index)]
    H = race_relative(H)
    H["y"] = (H.pos.map(pos_num) == 1).astype(float)
    H["jumps"] = H.type.isin(["Hurdle", "Chase", "NH Flat"])
    return H


def train():
    H = training_frame()
    tr = H[(H.date >= "2026-04-01") & (H.date < "2026-10-26")]
    va = H[H.date >= "2026-10-26"]
    out = {}
    for name, m in (("jumps", True), ("flat", False)):
        a, b = tr[tr.jumps == m], va[va.jumps == m]
        w = fit(a, a.y.values, a.race_key.values)
        pv = predict(b, w)
        bm = (1 / b.bsp).where(b.bsp > 1)
        bm = bm / bm.groupby(b.race_key).transform("sum")
        ok = bm.notna()
        ll_m = -np.log(pv[b.y == 1].clip(1e-6)).mean()
        ll_b = -np.log(bm[(b.y == 1) & ok].clip(1e-6)).mean()
        top = b.assign(pv=pv).sort_values("pv").groupby("race_key").tail(1)
        print(f"{name}: train {a.race_key.nunique()} races, validation {b.race_key.nunique()} races (26 Oct - 9 Nov)")
        print(f"   log-loss model {ll_m:.3f} vs BSP {ll_b:.3f}; top pick wins {top.y.mean():.1%}, "
              f"top-pick BSP ROI {((top.y * (top.bsp - 1) * 0.98) - (1 - top.y)).mean():+.1%}")
        wf = fit(H[H.jumps == m], H[H.jumps == m].y.values, H[H.jumps == m].race_key.values)
        out[name] = dict(zip(FEATS, map(float, wf)))
        out[name + "_to25oct"] = dict(zip(FEATS, map(float, w)))  # out-of-sample version for back-checks
        print("   coef", {k: round(v, 2) for k, v in out[name].items()})
    os.makedirs(p("models"), exist_ok=True)
    out["trained"] = f"history to {H.date.max()}"
    json.dump(out, open(MODEL, "w"), indent=1)


# ---------------------------------------------------------------- daily run
def fmt_date(d):
    return pd.Timestamp(d).strftime("%-d %b")


def run_day(day, card=None, oos=False):
    card = card or load_card(day)
    coefs = json.load(open(MODEL))
    if oos:
        coefs = {k: coefs[k + "_to25oct"] for k in ("jumps", "flat")}
    H = load_hist()
    H = H[H.date < day]
    guide = json.load(open(p("report", "history_data.json"))).get("guide", {})
    rows = []
    for r in card:
        for h in r["runners"]:
            rows.append({"date": day, "src": "card", "race_key": r["race_id"], "race_id": r["race_id"], "course": r["course"],
                         "dist_f": float(r.get("distance_f") or 0), "going": r.get("going"), "type": "Flat" if code_of(r) == "Flat" else (r.get("type") or "Hurdle"),
                         "n": len(r["runners"]), "horse_id": h["horse_id"], "horse": h["horse"], "hkey": norm(h["horse"]), "pos": None,
                         "or": pd.to_numeric(h.get("ofr"), errors="coerce"), "lbs": pd.to_numeric(h.get("lbs"), errors="coerce"),
                         "bsp": None, "fig": None, "spd": None, "comment": None})
    T = pd.DataFrame(rows)
    H = H.copy()
    H["is_target"] = False
    T["is_target"] = True
    A = prior_features(pd.concat([H, T], ignore_index=True))
    X = race_relative(A[A.is_target].copy())
    X["jumps"] = X.type.isin(["Hurdle", "Chase", "NH Flat"])
    X["p"] = 0.0
    for name, m in (("jumps", True), ("flat", False)):
        sel = X.jumps == m
        if sel.any():
            X.loc[sel, "p"] = predict(X[sel], [coefs[name][f] for f in FEATS])
    Hh = H.sort_values("date")
    byh = {k: g for k, g in Hh.groupby("hkey")}
    out = {"day": day, "races": {}}
    for r in card:
        rid = r["race_id"]
        xr = X[X.race_id == rid].set_index("horse_id")
        jumps = code_of(r) != "Flat"
        rr = {}
        for h in r["runners"]:
            past = byh.get(norm(h["horse"]), pd.DataFrame(columns=Hh.columns))
            if len(past) and h["horse_id"] and past.horse_id.notna().any():
                # same-name clash guard: if any API row has a different horse_id, keep only matching ids + rd rows
                past = past[(past.horse_id.isna()) | (past.horse_id == h["horse_id"])]
            cls = [early_class(c) for c in past.comment.tail(4)]
            cls = [c for c in cls if c]
            style = "Unknown"
            lead = None
            sc = None
            if cls:
                sc = np.mean([STYLE_SCORE[c] for c in cls])
                style = "Leader" if sc >= 3.2 else "Prominent" if sc >= 2.4 else "Midfield" if sc >= 1.6 else "Held up"  # tuned to old labels 26 Oct-9 Nov
                lead = round((sum(c == "Leader" for c in cls) + 0.15) / (len(cls) + 1), 3)
            last3 = past.tail(3)
            hist = [{"date": fmt_date(x.date), "course": x.course, "dist": f"{x.dist_f:g}f" if pd.notna(x.dist_f) else "",
                     "going": x.going if isinstance(x.going, str) else "", "pos": str(x.pos), "n": int(x.n) if pd.notna(x.n) else None,
                     "tfig": None, "spd": None if (pd.isna(x.spd) or x.src != "api") else int(x.spd), "fig": None if pd.isna(x.fig) else int(x.fig)}
                    for x in last3.itertuples()]
            rr[h["horse_id"]] = {"p": float(xr.p.get(h["horse_id"], 0)), "style": style, "lead": lead, "sc": None if sc is None else round(float(sc), 3), "nled": sum(c == "Leader" for c in cls), "ncls": len(cls), "runs": int(len(past)),
                                 "hist": hist, "_past": past}
        # race-level figure context
        figs = {k: v["_past"].tail(3).fig.max() for k, v in rr.items()}
        figs = {k: v for k, v in figs.items() if pd.notna(v)}
        favg = np.mean(list(figs.values())) if len(figs) >= 3 else None
        ors = [pd.to_numeric(h.get("ofr"), errors="coerce") for h in r["runners"]]
        ors = [o for o in ors if pd.notna(o)]
        oavg = np.mean(ors) if len(ors) >= 3 else None
        lbs = [pd.to_numeric(h.get("lbs"), errors="coerce") for h in r["runners"]]
        lavg = np.nanmean(lbs) if lbs else None
        ages = [pd.to_numeric(h.get("age"), errors="coerce") for h in r["runners"]]
        leaders = [h["horse"] for h in r["runners"] if rr[h["horse_id"]]["style"] == "Leader" or (rr[h["horse_id"]]["lead"] or 0) >= 0.4]
        known = sum(rr[h["horse_id"]]["style"] != "Unknown" for h in r["runners"])
        nrun = len(r["runners"])
        if known < max(2, nrun / 2):
            shape = {"label": "Unclear", "note": f"Running styles known for only {known} of {nrun} runners."}
        elif len(leaders) == 0:
            shape = {"label": "Slow / tactical", "note": "No established front-runner. Expect a steady early pace; prominent racers favoured, hold-up horses may find it hard to close."}
        elif len(leaders) == 1:
            shape = {"label": "Lone leader", "note": f"{leaders[0]} is the only habitual front-runner and may be allowed an easy lead."}
        elif len(leaders) == 2:
            shape = {"label": "Even", "note": f"Two likely leaders ({', '.join(leaders)}). A fair, even gallop is most likely."}
        else:
            shape = {"label": "Strong pace", "note": f"{len(leaders)} habitual front-runners ({', '.join(leaders)}). A contested lead should set things up for horses coming from behind."}
        bkey = f"{r['course']} {round(float(r.get('distance_f') or 0))}f"
        gd = guide.get(bkey)
        for h in r["runners"]:
            x = rr[h["horse_id"]]
            past = x.pop("_past")
            pros, cons = [], []
            if favg is not None and h["horse_id"] in figs:
                d = figs[h["horse_id"]] - favg
                if d >= 4:
                    pros.append(f"Best recent form figure {figs[h['horse_id']]:.0f}, {d:.0f} lb above field average")
                elif d <= -4:
                    cons.append(f"Best recent form figure {figs[h['horse_id']]:.0f}, {-d:.0f} lb below field average")
            o = pd.to_numeric(h.get("ofr"), errors="coerce")
            if pd.notna(o) and h["horse_id"] in figs and "andicap" in (r.get("race_name") or ""):
                d = figs[h["horse_id"]] - o
                if d >= 4:
                    pros.append(f"Recent figures {d:.0f} lb above its current mark (looks well handicapped)")
                elif d <= -6:
                    cons.append(f"Recent figures {-d:.0f} lb below its current mark (looks high in the weights)")
            if oavg is not None and pd.notna(o):
                d = o - oavg
                if d >= 5:
                    pros.append(f"Official rating {o:.0f}, {d:.0f} lb above field average")
                elif d <= -5:
                    cons.append(f"Official rating {o:.0f}, {-d:.0f} lb below field average")
            tc = h.get("trainer_14_days") or {}
            try:
                tw, tn = int(tc.get("wins")), int(tc.get("runs"))
                if tn >= 5 and tw / tn >= 0.2:
                    pros.append(f"Trainer {tw / tn:.0%} wins ({tw}/{tn}), last 14 days")
                elif tn >= 8 and tw == 0:
                    cons.append(f"Trainer 0 wins from {tn} runs, last 14 days")
            except (TypeError, ValueError):
                pass
            pn = past.pos.map(pos_num)
            same = past[past.type.isin(["Hurdle", "Chase", "NH Flat"]) == jumps]
            if ((same.pos.map(pos_num) == 1) & (same.dist_f >= float(r.get("distance_f") or 0) - 0.5)).any():
                pros.append("Has won at this trip or further")
            l3 = past.tail(3)
            sc = l3.pos.map(pos_num)
            if len(l3) >= 2 and sc.notna().all() and (sc <= 3).sum() >= 2:
                pros.append("Good recent finishing positions")
            elif len(l3) >= 3 and ((sc.isna()) | (sc >= 6)).all():
                cons.append("Poor recent finishing positions")
            lb = pd.to_numeric(h.get("lbs"), errors="coerce")
            if lavg and pd.notna(lb) and "andicap" in (r.get("race_name") or ""):
                if lb - lavg <= -5:
                    pros.append(f"Carries {lavg - lb:.0f} lb less than average")
                elif lb - lavg >= 5:
                    cons.append(f"Carries {lb - lavg:.0f} lb more than average")
            if str(h.get("headgear_run", "")).strip() == "1" and h.get("headgear"):
                pros.append("First-time headgear")
            try:
                lr = int(h.get("last_run"))
                if lr >= 90:
                    cons.append(f"Returns from a {lr}-day break")
            except (TypeError, ValueError):
                pass
            if x["runs"] <= 2:
                cons.append(f"Lightly raced: {x['runs']} run{'s' if x['runs'] != 1 else ''} in our data, so the model has little to go on")
            if jumps:
                jr = past[past.type.isin(["Hurdle", "Chase"])].tail(5)
                if len(jr):
                    k = jr.comment.fillna("").str.lower().str.contains(r"blunder|error|mistake|jumped (?:poorly|awkwardly|badly)|clumsy|untidy|sluggish (?:jump|leap)|scrappy|hit the").sum()
                    if k >= 2:
                        cons.append(f"Race comments mention jumping mistakes in {k} of its last {len(jr)} runs")
                    fu = jr.pos.astype(str).isin(["F", "UR", "U", "BD", "RO", "SU"]).sum()
                    if fu:
                        cons.append(f"Fell or unseated in {fu} of its last {len(jr)} jumps runs")
                    pu = jr.pos.astype(str).isin(["PU", "P"]).sum()
                    if pu:
                        cons.append(f"Pulled up in {pu} of its last {len(jr)} jumps runs")
                rtype = (r.get("type") or "")
                if rtype in ("Hurdle", "Chase") and x["runs"] >= 2 and not (past.type == rtype).any():
                    cons.append(f"First run over {'hurdles' if rtype == 'Hurdle' else 'fences'} in our data")
            a = pd.to_numeric(h.get("age"), errors="coerce")
            if pd.notna(a) and len([z for z in ages if pd.notna(z)]) >= 5 and a >= np.nanmax(ages) and a - np.nanmedian(ages) >= 3:
                cons.append(f"Aged {a:.0f}, older than most of this field")
            st = x["style"]
            if st == "Leader" and shape["label"] == "Lone leader":
                pros.append("Pace: may get an uncontested lead")
            elif st == "Leader" and shape["label"] == "Strong pace":
                cons.append("Pace: likely to be taken on for the lead")
            elif st == "Held up" and shape["label"] == "Strong pace":
                pros.append("Pace: a contested lead should suit its hold-up style")
            elif st == "Held up" and shape["label"] == "Slow / tactical":
                cons.append("Pace: steady gallop likely, hard to come from off the pace")
            if gd and st in (gd.get("st") or {}):
                v = gd["st"][st]
                lab = {"Leader": "front-runners", "Prominent": "prominent racers", "Midfield": "midfield runners", "Held up": "hold-up horses"}[st]
                if v[0] and v[3] and v[3] >= 50 and v[0] >= 1.25:
                    pros.append(f"Course: {lab} have won {v[0]:.1f}× their fair share at {bkey.split()[-1]} here")
                elif v[0] is not None and v[3] and v[3] >= 50 and v[0] <= 0.75:
                    cons.append(f"Course: {lab} have won {v[0]:.1f}× their fair share at {bkey.split()[-1]} here")
            x["pros"], x["cons"] = pros, cons
        # head-to-heads between today's rivals
        ids = {h["horse_id"]: h for h in r["runners"]}
        pasts = {hid: byh.get(norm(h["horse"])) for hid, h in ids.items()}
        for hid in ids:
            rr[hid]["h2h"] = []
        hs = list(ids)
        for i, a in enumerate(hs):
            for b in hs[i + 1:]:
                pa, pb = pasts[a], pasts[b]
                if pa is None or pb is None:
                    continue
                common = set(pa.race_key) & set(pb.race_key)
                for rk in sorted(common, key=lambda k: pa[pa.race_key == k].date.iloc[0])[-2:]:
                    ra, rb = pa[pa.race_key == rk].iloc[0], pb[pb.race_key == rk].iloc[0]
                    na, nb = pos_num(ra.pos), pos_num(rb.pos)
                    if na is None or nb is None:
                        continue
                    lens = None
                    if pd.notna(ra.ovr_btn) and pd.notna(rb.ovr_btn):
                        lens = round(float(rb.ovr_btn) - float(ra.ovr_btn), 1)
                    la, lb_ = pd.to_numeric(ids[a].get("lbs"), errors="coerce"), pd.to_numeric(ids[b].get("lbs"), errors="coerce")
                    bo = None
                    if pd.notna(ra.lbs) and pd.notna(rb.lbs) and pd.notna(la) and pd.notna(lb_):
                        bo = int((ra.lbs - rb.lbs) - (la - lb_))
                    where = f"{ra.course}, {fmt_date(ra.date)}, {ra.dist_f:g}f" if pd.notna(ra.dist_f) else f"{ra.course}, {fmt_date(ra.date)}"
                    for me, other, sgn in ((a, b, 1), (b, a, -1)):
                        ahead = (na < nb) if sgn == 1 else (nb < na)
                        L = None if lens is None else abs(lens)
                        txt = (f"finished {L:.1f}L {'ahead of' if ahead else 'behind'} " if L is not None else f"finished {'ahead of' if ahead else 'behind'} ") + ids[other]["horse"]
                        b_o = None if bo is None else bo * sgn
                        txt += f" ({where}" + ("" if b_o is None else f"; {abs(b_o)} lb {'better' if b_o >= 0 else 'worse'} off today") + ")"
                        rr[me]["h2h"].append({"date": fmt_date(ra.date), "text": txt, "lens": None if L is None else (L if ahead else -L), "better_off": b_o})
        out["races"][rid] = {"shape": shape, "runners": rr, "bias_key": bkey if gd else None}
    if oos:
        return out
    os.makedirs(p("store", day), exist_ok=True)
    json.dump(out, open(p("store", day, "model.json"), "w"), default=lambda o: None if (isinstance(o, float) and math.isnan(o)) else str(o))
    n = sum(len(v["runners"]) for v in out["races"].values())
    print(f"model run {day}: {len(out['races'])} races, {n} runners, styles known for "
          f"{sum(x['style'] != 'Unknown' for v in out['races'].values() for x in v['runners'].values())}")
    return out


if __name__ == "__main__":
    if sys.argv[1] == "train":
        train()
    elif sys.argv[1] == "run":
        run_day(sys.argv[2])
