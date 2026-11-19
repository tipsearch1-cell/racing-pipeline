"""Phase 4 walk-forward: candidates A-E vs baseline and market.  python3 research/model_reconstruction/phase4/p4_run.py
Outputs work/preds.pkl (one row per eval runner, a probability column per model) and out/run_log.md, out/config.json.
"""
import json, os, sys, time
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "research", "harville"))
import p4_models as P  # noqa: E402
from data import ckey, norm  # noqa: E402

W, OUT = os.path.join(HERE, "work"), os.path.join(HERE, "out")
CFG = dict(seed=20261119, A_l2_grid=[0.3, 1.0, 3.0], C=dict(depth=3, lr=0.1, n_max=150, min_leaf=200), B=dict(depth=3, lr=0.1, n_max=150, min_leaf=200),
           D1_l2=3.0, D2=dict(depth=2, lr=0.05, n_max=150, min_leaf=300), max_features=0.5, patience=15,
           ind_months=["2026-03", "2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09", "2026-10", "2026-11"],
           test_months=["2026-05", "2026-06", "2026-07", "2026-08", "2026-09", "2026-10", "H3-10", "H3-11"], checkpoints=["E", "M", "H", "T10", "L"])
EPS = 1e-9
LOG = []


def log(s):
    LOG.append(s); print(s, flush=True)


def prev_month(m):
    y, mm = map(int, m.split("-"))
    return f"{y if mm > 1 else y - 1}-{mm - 1 if mm > 1 else 12:02d}"


def load():
    F = pd.read_pickle(os.path.join(W, "feat.pkl"))
    G = json.load(open(os.path.join(W, "groups.json")))
    feats = sum(G["relative"].values(), [])
    F["k"] = F.date.astype(str) + "|" + F.course.map(ckey) + "|" + F.hkey
    F[feats] = F[feats].astype(float).fillna(0.0)
    F["jumps_f"] = F.jumps.astype(float)
    F["posn"] = pd.to_numeric(F.pos, errors="coerce")
    wins = F.groupby("race_key").y.transform("sum")
    F["trainable"] = (F.n >= 4) & (wins == 1)
    # eval sets with markets
    S3 = pd.read_pickle(os.path.join(ROOT, "research", "market_intelligence", "phase3", "work", "S3.pkl"))
    H3 = pd.read_pickle(os.path.join(ROOT, "research", "market_intelligence", "phase3", "work", "H3.pkl"))
    H3["month"] = np.where(H3.date < "2026-11-01", "H3-10", "H3-11")
    ev = []
    for D in (S3, H3):
        D = D.copy()
        D["k"] = D.date + "|" + D.course.map(ckey) + "|" + D.horse.map(norm)
        D = D.merge(F[["k"] + feats + ["jumps_f"]].drop_duplicates("k"), on="k", how="left")
        full = D.groupby("race_id")[feats[0]].transform(lambda s: s.notna().all())
        D = D[full & D.m_M.notna() & D.f.notna()]
        D = D[(D.pos == 1).groupby(D.race_id).transform("sum") == 1]
        ev.append(D)
    E = pd.concat(ev, ignore_index=True).sort_values(["race_id", "horse_id"], kind="mergesort").reset_index(drop=True)
    E["y"] = (E.pos == 1).astype(float)
    return F, E, feats


def Xof(df, cols):
    return df[cols].to_numpy(np.float64)


def fit_independent(F, feats, month_start):
    tr = F[F.trainable & (F.date < month_start)].sort_values("race_key", kind="mergesort")
    vstart = prev_month(month_start[:7]) + "-01"
    fit_part, val = tr[tr.date < vstart], tr[tr.date >= vstart]
    out = {}
    # A: linear race-softmax per code, L2 chosen on the last training month
    out["A"] = {}
    for jm in (False, True):
        a, v, full = fit_part[fit_part.jumps == jm], val[val.jumps == jm], tr[tr.jumps == jm]
        best = None
        for l2 in CFG["A_l2_grid"]:
            w = P.clogit_fit(Xof(a, feats), a.y.values, a.race_key.values, l2=l2)
            st, g = P.groups(v.race_key.values)
            ll = P.race_ll(P.softmax_g(Xof(v, feats) @ w, st, g), v.y.values, st)
            if best is None or ll < best[1]:
                best = (l2, ll)
        out["A"][jm] = (best[0], P.clogit_fit(Xof(full, feats), full.y.values, full.race_key.values, l2=best[0]))
    cols = feats + ["jumps_f"]
    c = P.ListwiseGBM(**CFG["C"], seed=CFG["seed"], max_features=CFG["max_features"])
    out["C"] = fit_gbm(c, fit_part, val, cols)
    b = P.PairwiseGBM(**CFG["B"], seed=CFG["seed"], max_features=CFG["max_features"])
    b.fit(Xof(fit_part, cols), fit_part.posn.values, fit_part.race_key.values, Xv=Xof(val, cols), yv=val.y.values, racev=val.race_key.values, patience=CFG["patience"])
    sb = b.score(Xof(tr, cols))
    out["B"] = (b, P.temperature_fit(sb, tr.y.values, tr.race_key.values))
    return out


def fit_gbm(model, fit_part, val, cols, offset=None, offv=None):
    model.fit(Xof(fit_part, cols), fit_part.y.values, fit_part.race_key.values if "race_key" in fit_part else fit_part.race_id.values, offset=offset,
              Xv=Xof(val, cols), yv=val.y.values, racev=val.race_key.values if "race_key" in val else val.race_id.values, offv=offv, patience=CFG["patience"])
    return model


def predict_independent(mods, D, feats):
    st, g = P.groups(D.race_id.values)
    s = np.zeros(len(D))
    for jm in (False, True):
        sel = (D.jumps_f.values == float(jm))
        s[sel] = Xof(D[sel], feats) @ mods["A"][jm][1]
    pa = P.softmax_g(s, st, g)
    cols = feats + ["jumps_f"]
    sc = mods["C"].score(Xof(D, cols)); pc = P.softmax_g(sc, st, g)
    b, a = mods["B"]; sbv = b.score(Xof(D, cols)); pb = P.softmax_g(a * sbv, st, g)
    return pa, pb, pc, sc


def main():
    os.makedirs(OUT, exist_ok=True)
    np.random.seed(CFG["seed"])
    F, E, feats = load()
    log(f"features {len(feats)}; eval runners {len(E):,} in {E.race_id.nunique():,} races; months {E.month.value_counts().sort_index().to_dict()}")
    for c in ("pA", "pB", "pC", "sC", "pD1", "pD2", "pE"):
        E[c] = np.nan
    timing = {}
    # independent candidates: Mar..Nov (Mar/Apr produce out-of-time C scores used to train E)
    for m in CFG["ind_months"]:
        t0 = time.time()
        mods = fit_independent(F, feats, f"{m}-01")
        sel = (E.month == m) if m != "2026-11" else (E.month == "H3-11")
        if m == "2026-10":
            sel = (E.month == "2026-10") | (E.month == "H3-10")
        D = E[sel]
        if len(D):
            pa, pb, pc, sc = predict_independent(mods, D, feats)
            E.loc[sel, "pA"], E.loc[sel, "pB"], E.loc[sel, "pC"], E.loc[sel, "sC"] = pa, pb, pc, sc
        timing[m] = round(time.time() - t0, 1)
        log(f"- independent fit < {m}-01: A l2 flat/jumps {mods['A'][False][0]}/{mods['A'][True][0]}; C trees {len(mods['C'].trees)}; "
            f"B trees {len(mods['B'][0].trees)} temp {mods['B'][1]:.2f}; {timing[m]}s")
    # market-dependent: D1, D2, E, trained on earlier eval months (S3 from Mar), tested May.. and H3
    E["lm"] = np.log(E.m_M.clip(EPS)); E["lf"] = np.log(E.f.clip(EPS))
    for tm in CFG["test_months"]:
        t0 = time.time()
        cut = {"H3-10": "2026-10", "H3-11": "2026-11"}.get(tm, tm)
        tr = E[(E.month >= "2026-03") & (E.month < cut) & ~E.month.str.startswith("H3")].sort_values("race_id", kind="mergesort")
        te = E[E.month == tm]
        if not len(te):
            continue
        st, g = P.groups(te.race_id.values)
        w = P.clogit_fit(Xof(tr, feats), tr.y.values, tr.race_id.values, l2=CFG["D1_l2"], offset=tr.lm.values)
        E.loc[te.index, "pD1"] = P.softmax_g(te.lm.values + Xof(te, feats) @ w, st, g)
        vstart = prev_month(cut)
        fp, va = tr[tr.month < vstart], tr[tr.month >= vstart]
        d2 = P.ListwiseGBM(**CFG["D2"], seed=CFG["seed"], max_features=CFG["max_features"])
        d2.fit(Xof(fp, feats + ["jumps_f"]), fp.y.values, fp.race_id.values, offset=fp.lm.values, Xv=Xof(va, feats + ["jumps_f"]), yv=va.y.values,
               racev=va.race_id.values, offv=va.lm.values, patience=CFG["patience"])
        E.loc[te.index, "pD2"] = P.softmax_g(d2.score(Xof(te, feats + ["jumps_f"]), offset=te.lm.values), st, g)
        trE = tr[tr.sC.notna()]
        we = P.clogit_fit(trE[["lm", "sC", "lf"]].to_numpy(), trE.y.values, trE.race_id.values, l2=0.0, w0=np.array([1.0, 0.0, 0.0]))
        E.loc[te.index, "pE"] = P.softmax_g(te[["lm", "sC", "lf"]].to_numpy() @ we, st, g)
        # market-information experiment: D1 at each checkpoint (S3 months only)
        if not tm.startswith("H3"):
            for cp in CFG["checkpoints"]:
                ok_tr = tr[f"m_{cp}"].notna().groupby(tr.race_id).transform("all"); ok_te = te[f"m_{cp}"].notna().groupby(te.race_id).transform("all")
                a, b = tr[ok_tr], te[ok_te]
                if not len(b):
                    continue
                lma, lmb = np.log(a[f"m_{cp}"].clip(EPS)).values, np.log(b[f"m_{cp}"].clip(EPS)).values
                wc = P.clogit_fit(Xof(a, feats), a.y.values, a.race_id.values, l2=CFG["D1_l2"], offset=lma)
                stb, gb = P.groups(b.race_id.values)
                E.loc[b.index, f"pD1_{cp}"] = P.softmax_g(lmb + Xof(b, feats) @ wc, stb, gb)
                E.loc[b.index, f"pM_{cp}"] = P.softmax_g(lmb, stb, gb)
                wci = P.clogit_fit(a[["lm"]].assign(lm=lma).to_numpy(), a.y.values, a.race_id.values, l2=0.0, w0=np.array([1.0]))
                E.loc[b.index, f"pMs_{cp}"] = P.softmax_g(wci[0] * lmb, stb, gb)  # market with fitted sharpening only (control)
        log(f"- market-dependent test {tm}: train {tr.race_id.nunique():,} races; D2 trees {len(d2.trees)}; E weights (log m, s_C, log f) {np.round(we, 3).tolist()}; {time.time() - t0:.0f}s")
    E.to_pickle(os.path.join(W, "preds.pkl"))
    json.dump(dict(CFG, timing_s=timing), open(os.path.join(OUT, "config.json"), "w"), indent=1)
    open(os.path.join(OUT, "run_log.md"), "w").write("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
