"""Harville research experiments (spec prereg/HARVILLE_ICM_SPEC_2026-11-19.md).

  python3 research/harville/data.py     # once: builds work/{O,F,R}.pkl
  python3 research/harville/run.py      # fits, walk-forward tests, betting, writes research/harville/out/*

Everything is fitted on the fit period of each split only; test periods are scored once.
"""
import json, os, sys, time
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import logsumexp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from harville import clean, position_probs  # noqa: E402
from data import bf_places  # noqa: E402

W, OUT = os.path.join(HERE, "work"), os.path.join(HERE, "out")
B_BOOT = 2000
THRESH = [0.0, 0.02, 0.04, 0.06, 0.08, 0.10]
COMMS = [0.02, 0.05]
rng = np.random.default_rng(20261119)


# ------------------------------------------------------------------ races
def races_from(df, pcol):
    """List of race dicts with arrays; eligibility per spec."""
    out = []
    for rid, g in df.groupby("race_id", sort=False):
        p = g[pcol].to_numpy(float)
        if len(g) < 3 or not np.all(np.isfinite(p)) or np.any(p <= 0):
            continue
        pos = g.pos.to_numpy(float)
        fin = pos[np.isfinite(pos)]
        if len(fin) < 3:
            continue
        top = np.sort(fin)[:3]
        clean123 = list(top) == [1, 2, 3] and (fin == 1).sum() == 1 and (fin == 2).sum() == 1 and (fin == 3).sum() == 1
        if (fin == 1).sum() != 1:      # winner dead heat: skip entirely (stage 1 undefined)
            continue
        n = len(g)
        hcap = bool(g.hcap.iloc[0]) if "hcap" in g else False
        code = g.code.iloc[0] if "code" in g else "Flat"
        r = dict(race_id=rid, date=g.date.iloc[0], n=n, p=clean(p), pos=pos, clean=clean123, hcap=hcap, code=code,
                 cls=float(g.cls.iloc[0]) if "cls" in g and pd.notna(g.cls.iloc[0]) else np.nan,
                 psp=g.psp.to_numpy(float) if "psp" in g else np.full(n, np.nan),
                 placed_bf=g.placed_bf.to_numpy(float) if "placed_bf" in g else np.full(n, np.nan),
                 places=bf_places(n, hcap))
        o = np.argsort(np.where(np.isfinite(pos), pos, 99), kind="stable")
        r["first3"] = o[:3] if clean123 else None
        r["i1"] = int(np.where(pos == 1)[0][0])
        r["i2"] = int(np.where(pos == 2)[0][0]) if (pos == 2).sum() == 1 else None
        r["i3"] = int(np.where(pos == 3)[0][0]) if clean123 else None
        out.append(r)
    return out


# ------------------------------------------------------------------ features (log stage weight = X theta)
CLS_C = 4.0


def feats(r, variant):
    lp = np.log(r["p"])
    n = r["n"]
    one = np.ones(n)
    jumps = 1.0 if r["code"] == "Jumps" else 0.0
    hc = 1.0 if r["hcap"] else 0.0
    ln = np.log(n) - np.log(10)
    rank = np.argsort(np.argsort(-r["p"]))
    if variant in ("B1", "B2"):
        return lp[:, None]
    if variant == "B3":
        return np.c_[lp * (1 - jumps), lp * jumps]
    if variant == "B4":
        return np.c_[lp * hc, lp * (1 - hc)]
    if variant == "B5":
        return np.c_[lp, lp * ln]
    if variant == "C":
        cls = (r["cls"] - CLS_C) if np.isfinite(r["cls"]) else 0.0
        return np.c_[lp, lp * jumps, lp * hc, lp * ln, (rank == 0) * one, ((rank == 1) | (rank == 2)) * one, lp * cls]
    raise ValueError(variant)


def choice_sets(races, variant, stage):
    """Stacked arrays for a conditional logit: rows = runners still in, chosen flag, group id."""
    X, y, gid = [], [], []
    k = 0
    for r in races:
        if stage == 2:
            if r["i2"] is None:
                continue
            keep = np.ones(r["n"], bool); keep[r["i1"]] = False; ch = r["i2"]
        else:
            if r["i3"] is None:
                continue
            keep = np.ones(r["n"], bool); keep[[r["i1"], r["i2"]]] = False; ch = r["i3"]
        F = feats(r, variant)
        X.append(F[keep]); yy = np.zeros(r["n"]); yy[ch] = 1; y.append(yy[keep]); gid.append(np.full(keep.sum(), k)); k += 1
    return np.vstack(X), np.concatenate(y), np.concatenate(gid), k


def clogit_nll(theta, X, y, gid, ng, l2):
    u = X @ theta
    m = np.full(ng, -np.inf)
    np.maximum.at(m, gid, u)
    e = np.exp(u - m[gid])
    s = np.zeros(ng); np.add.at(s, gid, e)
    lse = m + np.log(s)
    nll = -(u[y == 1].sum() - lse.sum())
    pr = e / s[gid]
    g = -(X[y == 1].sum(0) - (X * pr[:, None]).sum(0))
    pen = np.r_[0.0, np.ones(len(theta) - 1)] * l2 if l2 else 0
    return nll + 0.5 * np.sum(pen * theta ** 2), g + pen * theta


def fit(races, variant):
    l2 = 1.0 if variant == "C" else 0.0
    res = {}
    nll_tot, nobs, npar = 0.0, 0, 0
    if variant == "B1":
        a2 = choice_sets(races, "B1", 2); a3 = choice_sets(races, "B1", 3)
        X = np.vstack([a2[0], a3[0]]); y = np.r_[a2[1], a3[1]]; gid = np.r_[a2[2], a3[2] + a2[3]]; ng = a2[3] + a3[3]
        o = minimize(clogit_nll, np.ones(1), args=(X, y, gid, ng, 0), jac=True, method="L-BFGS-B")
        H = hess(o.x, X, y, gid, ng)
        res = {"t2": o.x, "t3": o.x, "se2": se(H), "se3": se(H)}
        return res | {"nll": o.fun, "nobs": ng, "k": 1, "bic": 1 * np.log(ng) + 2 * o.fun}
    for st in (2, 3):
        X, y, gid, ng = choice_sets(races, variant, st)
        x0 = np.zeros(X.shape[1]); x0[:1] = 1.0
        if variant in ("B3", "B4"):
            x0[:] = 1.0
        o = minimize(clogit_nll, x0, args=(X, y, gid, ng, l2), jac=True, method="L-BFGS-B")
        res[f"t{st}"] = o.x
        res[f"se{st}"] = se(hess(o.x, X, y, gid, ng))
        nll_tot += o.fun; nobs += ng; npar += len(o.x)
    return res | {"nll": nll_tot, "nobs": nobs, "k": npar, "bic": npar * np.log(nobs) + 2 * nll_tot}


def hess(theta, X, y, gid, ng):
    u = X @ theta
    m = np.full(ng, -np.inf); np.maximum.at(m, gid, u)
    e = np.exp(u - m[gid]); s = np.zeros(ng); np.add.at(s, gid, e); pr = e / s[gid]
    k = X.shape[1]
    H = np.zeros((k, k))
    mu = np.zeros((ng, k)); np.add.at(mu, gid, X * pr[:, None])
    H = (X * pr[:, None]).T @ X - mu.T @ mu
    return H


def se(H):
    try:
        return np.sqrt(np.diag(np.linalg.inv(H)))
    except np.linalg.LinAlgError:
        return np.full(len(H), np.nan)


def weights(r, model, params):
    if model == "A":
        return r["p"], r["p"], r["p"]
    v = params["variant"] if model == "B" else "C"
    F = feats(r, v)
    lw2 = F @ params["t2"]; lw3 = F @ params["t3"]
    return r["p"], np.exp(lw2 - lw2.max()), np.exp(lw3 - lw3.max())


# ------------------------------------------------------------------ scoring
def score(races, models):
    """Per-race metric rows and per-runner rows for each model."""
    R, U = [], []
    for r in races:
        for name, (m, prm) in models.items():
            p, w2, w3 = weights(r, m, prm)
            P = position_probs(p, w2, w3, w3, kmax=min(4, r["n"]))
            row = dict(model=name, race_id=r["race_id"], date=r["date"], n=r["n"], code=r["code"], hcap=r["hcap"])
            pos = r["pos"]
            t2 = (pos <= 2).astype(float); t3 = (pos <= 3).astype(float)
            P2 = P[:, :2].sum(1); P3 = P[:, :3].sum(1)
            row["brier2"] = np.sum((P2 - t2) ** 2); row["brier3"] = np.sum((P3 - t3) ** 2); row["nr"] = r["n"]
            if r["i2"] is not None:
                row["ll_ex"] = -np.log(p[r["i1"]] * w2[r["i2"]] / (w2.sum() - w2[r["i1"]]))
            if r["clean"]:
                row["ll_tri"] = row["ll_ex"] - np.log(w3[r["i3"]] / (w3.sum() - w3[r["i1"]] - w3[r["i2"]]))
            R.append(row)
            rank = np.argsort(np.argsort(-r["p"])) + 1
            k = r["places"]
            Pk = P[:, :k].sum(1) if k else np.full(r["n"], np.nan)
            for i in range(r["n"]):
                U.append((name, r["race_id"], r["date"], r["n"], r["code"], r["hcap"], rank[i], r["p"][i], P[i, 1] if P.shape[1] > 1 else 0,
                          P[i, 2] if P.shape[1] > 2 else 0, P2[i], P3[i], pos[i], k, Pk[i], r["psp"][i], r["placed_bf"][i]))
    R = pd.DataFrame(R)
    U = pd.DataFrame(U, columns=["model", "race_id", "date", "n", "code", "hcap", "rank", "p", "P2nd", "P3rd", "Ptop2", "Ptop3", "pos",
                                 "places", "Pplace", "psp", "placed_bf"])
    return R, U


def day_boot(df, col, base="A", models=None, B=B_BOOT, stat="mean_diff"):
    """Date-block bootstrap of mean(per-race metric of base) - mean(metric of model): positive = model better (lower loss)."""
    out = {}
    piv = df.pivot_table(index=["date", "race_id"], columns="model", values=col).dropna()
    days = piv.index.get_level_values(0)
    ud = np.unique(days)
    idx = {d: np.where(days == d)[0] for d in ud}
    for m in (models or [c for c in piv.columns if c != base]):
        diff = (piv[base] - piv[m]).to_numpy()
        sums = np.array([diff[idx[d]].sum() for d in ud]); cnt = np.array([len(idx[d]) for d in ud])
        draws = rng.integers(0, len(ud), (B, len(ud)))
        bs = sums[draws].sum(1) / cnt[draws].sum(1)
        out[m] = (diff.mean(), np.percentile(bs, 2.5), np.percentile(bs, 97.5), len(diff))
    return out


# ------------------------------------------------------------------ betting
def settle_place(U):
    """Fraction of the stake that wins (dead-heat rule at the last place)."""
    pos = U.pos.to_numpy(float); k = U.places.to_numpy(float)
    frac = np.where(pos < k, 1.0, 0.0)
    eq = pos == k
    if eq.any():
        t = U.assign(eq=eq).groupby("race_id").eq.transform("sum").to_numpy()
        frac = np.where(eq, np.where(t > 0, 1.0 / np.maximum(t, 1), 0), frac)  # k-th place dead heat: split
    if "placed_bf" in U and U.placed_bf.notna().any():   # R: Betfair's own settlement flag where known
        frac = np.where(U.placed_bf.notna() & ~eq, U.placed_bf.fillna(0).to_numpy(), frac)
    return frac


def bets(U, model, T, c):
    x = U[(U.model == model) & (U.places > 0) & U.psp.notna() & (U.psp > 1)].copy()
    x["ev"] = x.Pplace * (1 + (x.psp - 1) * (1 - c)) - 1
    x = x[x.ev >= T]
    x["ret"] = settle_place(x) * (1 + (x.psp - 1) * (1 - c))
    x["pl"] = x.ret - 1
    return x


def summarise_bets(x, B=B_BOOT):
    if not len(x):
        return dict(bets=0)
    x = x.sort_values(["date", "race_id"])
    d = x.groupby("date").agg(pl=("pl", "sum"), st=("pl", "size"))
    draws = rng.integers(0, len(d), (B, len(d)))
    roi_bs = d.pl.to_numpy()[draws].sum(1) / d.st.to_numpy()[draws].sum(1)
    cum = x.pl.cumsum().to_numpy()
    dd = float(np.max(np.maximum.accumulate(np.r_[0, cum]) [1:] - cum)) if len(cum) else 0
    lose = (x.pl < 0).astype(int).to_numpy()
    run = mx = 0
    for v in lose:
        run = run + 1 if v else 0; mx = max(mx, run)
    q = x.assign(q=pd.PeriodIndex(pd.to_datetime(x.date), freq="Q").astype(str)).groupby("q").pl.agg(["size", "sum"])
    cut = x.ret.quantile(0.99)
    trim = x[x.ret <= cut] if (x.ret > cut).any() else x
    return dict(bets=len(x), stake=len(x), ret=round(x.ret.sum(), 2), pl=round(x.pl.sum(), 2), roi=x.pl.mean(),
                lo=np.percentile(roi_bs, 2.5), hi=np.percentile(roi_bs, 97.5), lo_bonf=np.percentile(roi_bs, 0.07), hi_bonf=np.percentile(roi_bs, 99.93),
                maxdd=round(dd, 2), longest_losing=mx, quarters={k: (int(v["size"]), round(v["sum"], 2)) for k, v in q.iterrows()},
                all_q_profit=bool((q["sum"] > 0).all()), roi_trim=trim.pl.mean())


# ------------------------------------------------------------------ calibration
def calib(U, col, outcome):
    rows = []
    for m, g in U.groupby("model"):
        g = g[np.isfinite(g[col])]
        y = outcome(g)
        b = pd.qcut(g[col].rank(method="first"), 10, labels=False)
        t = pd.DataFrame({"pred": g[col].values, "obs": y, "b": b.values}).groupby("b").agg(pred=("pred", "mean"), obs=("obs", "mean"), n=("obs", "size"))
        lg = np.log(np.clip(g[col].values, 1e-6, 1 - 1e-6) / (1 - np.clip(g[col].values, 1e-6, 1 - 1e-6)))
        o = minimize(lambda th: -np.sum(y * (th[0] + th[1] * lg) - np.logaddexp(0, th[0] + th[1] * lg)), [0, 1], method="BFGS")
        rows.append((m, t, o.x))
    return rows


def fmt_ci(t, k=4):
    return f"{t[0]:+.{k}f} [{t[1]:+.{k}f}, {t[2]:+.{k}f}] (n={t[3]:,})"


# ------------------------------------------------------------------ main
def fit_all(train):
    fits = {v: fit(train, v) for v in ("B1", "B2", "B3", "B4", "B5")}
    best = min(fits, key=lambda v: fits[v]["bic"])
    cf = fit(train, "C")
    return fits, best, cf


def models_for(fits, best, cf):
    return {"A": ("A", None), "B": ("B", fits[best] | {"variant": best}), "C": ("C", cf)}


def run_split(name, train_df, test_df, pcol, log, store):
    t0 = time.time()
    tr = races_from(train_df, pcol); te = races_from(test_df, pcol)
    fits, best, cf = fit_all(tr)
    log.append(f"\n### {name}: fit {train_df.date.min()}..{train_df.date.max()} ({len(tr):,} races) -> test {test_df.date.min()}..{test_df.date.max()} ({len(te):,} races)")
    for v, f in fits.items():
        log.append(f"- {v}: BIC {f['bic']:.1f}; stage-2 coef {np.round(f['t2'], 3).tolist()} (se {np.round(f['se2'], 3).tolist()}); stage-3 coef {np.round(f['t3'], 3).tolist()} (se {np.round(f['se3'], 3).tolist()})")
    log.append(f"- selected B variant (lowest BIC on fit): **{best}**")
    log.append(f"- C coefficients [lp, lp*jumps, lp*hcap, lp*log(n/10), fav, rank2-3, lp*(class-4)]: stage 2 {np.round(cf['t2'], 3).tolist()}; stage 3 {np.round(cf['t3'], 3).tolist()}")
    M = models_for(fits, best, cf)
    R, U = score(te, M)
    store[name] = dict(R=R, U=U, best=best, fits={k: {kk: (vv.tolist() if hasattr(vv, "tolist") else vv) for kk, vv in f.items()} for k, f in fits.items()},
                       C={k: (v.tolist() if hasattr(v, "tolist") else v) for k, v in cf.items()}, M=M)
    log.append(f"- ({time.time() - t0:.0f}s)")
    return R, U


def accuracy_table(R, label):
    L = [f"\n**{label}** - mean per race (lower is better); gain = A minus model, 95% date-block interval"]
    L.append("| Model | Top-2 Brier | Top-3 Brier | Exacta log-loss | Trifecta log-loss |")
    L.append("|---|---|---|---|---|")
    for m, g in R.groupby("model"):
        L.append(f"| {m} | {g.brier2.sum() / g.nr.sum():.5f} | {g.brier3.sum() / g.nr.sum():.5f} | {g.ll_ex.mean():.4f} | {g.ll_tri.mean():.4f} |")
    for col in ("ll_tri", "ll_ex", "brier3", "brier2"):
        b = day_boot(R, col)
        L.append(f"- gain in {col}: " + "; ".join(f"{m} {fmt_ci(v)}" for m, v in b.items()))
    return L


def segment_table(R, U, label):
    L = [f"\n**Segments - {label}** (trifecta log-loss gain vs A per race, 95% day-block interval)"]
    R = R.copy()
    R["field"] = pd.cut(R.n, [0, 7, 11, 15, 99], labels=["5-7", "8-11", "12-15", "16+"])
    for seg in ("code", "hcap", "field"):
        for k, g in R.groupby(seg, observed=True):
            b = day_boot(g, "ll_tri", B=500)
            L.append(f"- {seg}={k}: " + "; ".join(f"{m} {fmt_ci(v)}" for m, v in b.items()))
    L.append("\nExpected vs actual 2nd and 3rd places by input rank (test period, all models share actuals):")
    L.append("| Rank | n | actual 2nd | A exp 2nd | B exp 2nd | C exp 2nd | actual 3rd | A exp 3rd | B exp 3rd | C exp 3rd |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    piv2 = U.pivot_table(index=["race_id", "rank"], columns="model", values="P2nd").reset_index()
    piv3 = U.pivot_table(index=["race_id", "rank"], columns="model", values="P3rd").reset_index()
    act = U[U.model == "A"].set_index(["race_id", "rank"]).pos
    piv2["a"] = (act.reindex(pd.MultiIndex.from_frame(piv2[["race_id", "rank"]])).to_numpy() == 2)
    piv3["a"] = (act.reindex(pd.MultiIndex.from_frame(piv3[["race_id", "rank"]])).to_numpy() == 3)
    for rk in range(1, 9):
        a2 = piv2[piv2["rank"] == rk]; a3 = piv3[piv3["rank"] == rk]
        if not len(a2):
            continue
        L.append(f"| {rk} | {len(a2):,} | {a2.a.sum():,} | {a2.A.sum():.0f} | {a2.B.sum():.0f} | {a2.C.sum():.0f} | {a3.a.sum():,} | {a3.A.sum():.0f} | {a3.B.sum():.0f} | {a3.C.sum():.0f} |")
    return L


def betting_tables(U, label, cells):
    L = [f"\n**Place betting at Betfair place SP - {label}** (£1 limit-on-close back bets; ROI after commission; 95% day-block interval; Bonferroni 99.86%)"]
    allb = U[(U.model == "A") & (U.places > 0) & U.psp.notna() & (U.psp > 1)].copy()
    for c in COMMS:
        allb["ret"] = settle_place(allb) * (1 + (allb.psp - 1) * (1 - c)); allb["pl"] = allb.ret - 1
        s = summarise_bets(allb)
        L.append(f"- Benchmark, back every runner at place SP, commission {c:.0%}: {s['bets']:,} bets, ROI {s['roi']:+.2%} [{s['lo']:+.2%}, {s['hi']:+.2%}]")
    L.append("| Model | Comm | T | Bets | P/L | ROI | 95% | Bonferroni | Max DD | Longest losing | Every quarter +? | ROI w/o top 1% |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for c in COMMS:
        for T in THRESH:
            for m in ("A", "B", "C"):
                s = summarise_bets(bets(U, m, T, c))
                cells[(label, m, c, T)] = s
                if not s["bets"]:
                    L.append(f"| {m} | {c:.0%} | {T:.0%} | 0 | | | | | | | | |"); continue
                L.append(f"| {m} | {c:.0%} | {T:.0%} | {s['bets']:,} | {s['pl']:+.1f} | {s['roi']:+.2%} | [{s['lo']:+.2%}, {s['hi']:+.2%}] | [{s['lo_bonf']:+.2%}, {s['hi_bonf']:+.2%}] | {s['maxdd']:.1f} | {s['longest_losing']} | {'yes' if s['all_q_profit'] else 'no'} | {s['roi_trim']:+.2%} |")
    return L


def mispricing(U, label):
    L = [f"\n**Mispricing scan - {label}**: back every runner at place SP (2% commission), ROI by segment"]
    x = U[(U.model == "A") & (U.places > 0) & U.psp.notna() & (U.psp > 1)].copy()
    x["ret"] = settle_place(x) * (1 + (x.psp - 1) * 0.98); x["pl"] = x.ret - 1
    x["band"] = pd.cut(1 / x.p, [1, 2, 3, 5, 8, 13, 21, 41, 1e9], labels=["<2", "2-3", "3-5", "5-8", "8-13", "13-21", "21-41", "41+"])
    x["field"] = pd.cut(x.n, [0, 7, 11, 15, 99], labels=["5-7", "8-11", "12-15", "16+"])
    x["edgeA"] = x.Pplace * (1 + (x.psp - 1) * 0.98) - 1
    res = {}
    for seg in ("rank", "band", "field", "hcap"):
        g = x[x["rank"] <= 8] if seg == "rank" else x
        t = g.groupby(seg, observed=True).agg(n=("pl", "size"), roi=("pl", "mean"), harville_ev=("edgeA", "mean"))
        L.append(f"- by {seg}: " + "; ".join(f"{k}: n={int(v.n):,} ROI {v.roi:+.1%} (A-model EV {v.harville_ev:+.1%})" for k, v in t.iterrows()))
        res[seg] = t.roi.to_dict()
    return L, res


def main():
    os.makedirs(OUT, exist_ok=True)
    O = pd.read_pickle(os.path.join(W, "O.pkl"))
    O = O[O.priced_all & O.p.notna()]
    F = pd.read_pickle(os.path.join(W, "F.pkl"))
    Rr = pd.read_pickle(os.path.join(W, "R.pkl"))
    log = ["# Harville research - results", "", "Spec: prereg/HARVILLE_ICM_SPEC_2026-11-19.md (sha256 in prereg/SHA256SUMS.txt). Generated by research/harville/run.py.", ""]
    store, cells = {}, {}

    # ---------------- track O, two splits
    s1f, s1t = O[O.date <= "2026-03-31"], O[O.date >= "2026-04-01"]
    log.append("## Track O (09:00 market input, GB+IRE Flat and Jumps)")
    for nm, tr, te in (("S1", s1f, s1t), ("S2", s1t, s1f)):
        R, U = run_split(nm, tr, te, "p", log, store)
        log += accuracy_table(R, f"{nm} test")
        log += segment_table(R, U, f"{nm} test")
        log += betting_tables(U, f"{nm} test", cells)
        L, _ = mispricing(U, f"{nm} test"); log += L
        R.to_csv(os.path.join(W, f"O_{nm}_races.csv.gz"), index=False); U.to_csv(os.path.join(W, f"O_{nm}_runners.csv.gz"), index=False)

    # ---------------- track R diagnostics (walk-forward by year)
    log.append("\n## Track R (RBD GB Flat 2020-2026): expanding walk-forward by year")
    Rr = Rr.assign(p_bsp=1 / Rr.bsp, p_fc=1 / Rr.fc)
    for inp in ("p_fc", "p_bsp"):
        Rr[inp] = Rr[inp] / Rr.groupby("race_id")[inp].transform("sum")
    rstab = []
    for inp, lab in (("p_bsp", "closing BSP input (DIAGNOSTIC - outcome price)"), ("p_fc", "Forecasted Odds input (pre-race by definition; timestamp not verified)")):
        log.append(f"\n### R - {lab}")
        for Y in ("2022", "2023", "2024", "2025", "2026"):
            tr = Rr[Rr.date < f"{Y}-01-01"]; te = Rr[Rr.date.str[:4] == Y]
            R, U = run_split(f"R-{inp}-{Y}", tr, te, inp, log, store)
            st = store[f"R-{inp}-{Y}"]
            b = day_boot(R, "ll_tri", B=1000)
            rstab.append(dict(input=inp, year=Y, best=st["best"], a=st["fits"]["B2"]["t2"][0], b=st["fits"]["B2"]["t3"][0],
                              gainB=b["B"][0], loB=b["B"][1], gainC=b["C"][0], loC=b["C"][1], races=b["B"][3]))
            log.append(f"- {Y}: trifecta log-loss gain vs A: B {fmt_ci(b['B'])}; C {fmt_ci(b['C'])}")
            if inp == "p_fc":
                log += betting_tables(U, f"R {Y} (Forecasted Odds)", cells)
                L, mp = mispricing(U, f"R {Y}"); log += L
                rstab[-1]["mispricing"] = mp
            if Y == "2025":
                log += accuracy_table(R, f"R {Y} {inp}")
    pd.DataFrame([{k: v for k, v in r.items() if k != "mispricing"} for r in rstab]).to_csv(os.path.join(OUT, "r_stability.csv"), index=False)
    json.dump({f"{r['input']}-{r['year']}": r.get("mispricing") for r in rstab if r.get("mispricing")}, open(os.path.join(W, "r_mispricing.json"), "w"), default=str)

    # ---------------- final: fit on all O, apply to F
    log.append("\n## Track F (Frankie genuine pre-race chances) - final holdout, parameters fitted on all of O")
    allO = races_from(O, "p")
    fits, best, cf = fit_all(allO)
    log.append(f"- fitted on {len(allO):,} O races; selected B variant {best}; B2 a={fits['B2']['t2'][0]:.3f} b={fits['B2']['t3'][0]:.3f}")
    M = models_for(fits, best, cf)
    json.dump({"best": best, "fits": {k: {kk: (vv.tolist() if hasattr(vv, "tolist") else vv) for kk, vv in f.items()} for k, f in fits.items()},
               "C": {k: (v.tolist() if hasattr(v, "tolist") else v) for k, v in cf.items()}}, open(os.path.join(OUT, "final_params.json"), "w"), indent=1)
    F = F[F.date <= "2026-11-18"].copy()
    F["hcap"] = F.hcap.astype(str).isin(["True", "true", "1"])
    F["cls"] = np.nan
    for inp, lab in (("mkt", "09:00 market (D)"), ("p_model", "Frankie model p"), ("rev", "Frankie sealed reviewer chance")):
        g = F[F[inp].notna()].copy()
        g = g[g.groupby("race_id")[inp].transform(lambda s: s.notna().all())]
        if not len(g):
            continue
        g["pin"] = g[inp] / g.groupby("race_id")[inp].transform("sum")
        te = races_from(g, "pin")
        R, U = score(te, M)
        log += accuracy_table(R, f"F - input {lab}, {g.date.min()}..{g.date.max()}")
        log += betting_tables(U, f"F {lab}", cells)
        R.to_csv(os.path.join(W, f"F_{inp}_races.csv.gz"), index=False); U.to_csv(os.path.join(W, f"F_{inp}_runners.csv.gz"), index=False)

    open(os.path.join(OUT, "results.md"), "w").write("\n".join(log) + "\n")
    pd.DataFrame([dict(track=k[0], model=k[1], comm=k[2], T=k[3], **{kk: vv for kk, vv in v.items() if kk != "quarters"}, quarters=json.dumps(v.get("quarters")))
                  for k, v in cells.items()]).to_csv(os.path.join(OUT, "betting_cells.csv"), index=False)
    # calibration data for charts
    for nm in ("S1", "S2"):
        U = store[nm]["U"]
        rows = []
        for col, k in (("P2nd", 2), ("P3rd", 3)):
            for m, t, th in calib(U, col, lambda g, k=k: (g.pos == k).astype(float).to_numpy()):
                rows.append(dict(split=nm, what=col, model=m, slope=th[1], intercept=th[0], table=t.to_json()))
        pd.DataFrame(rows).to_csv(os.path.join(OUT, f"calibration_{nm}.csv"), index=False)
    print("\n".join(log))


if __name__ == "__main__":
    main()
