"""Phase 2 analysis: accuracy, disagreement, segments, betting, outliers, movement.  python3 research/harville/phase2/analyze2.py
Reads phase2/work/{S,G,G_rev}_{races,runners}.csv.gz written by run2.py. Writes phase2/out/*.csv and tables.md.
"""
import json, os, sys
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
W, OUT = os.path.join(HERE, "work"), os.path.join(HERE, "out")
B = 2000
rng = np.random.default_rng(20261119)
DEV = ["2026-05", "2026-06", "2026-07", "2026-08"]
HOLD = ["2026-09", "2026-10"]
THRESH = [0.0, 0.02, 0.04, 0.06, 0.08, 0.10]
COMMS = [0.02, 0.05]
NAMES = {"H": "Original Harville (market)", "A": "Market + discounted Harville", "B": "Our model + discounted Harville",
         "C": "Blend + discounted Harville", "D": "Enhanced ranking"}


def period(df, which):
    if which == "dev":
        return df[df.month.isin(DEV)]
    if which == "hold":
        return df[df.month.isin(HOLD)]
    return df


def boot_days(values_by_day, counts_by_day, B=B):
    d = len(values_by_day)
    draws = rng.integers(0, d, (B, d))
    return values_by_day[draws].sum(1) / counts_by_day[draws].sum(1)


def paired(R, col, base="A", models=("H", "B", "C", "D")):
    piv = R.pivot_table(index=["date", "race_id"], columns="model", values=col).dropna()
    days = piv.index.get_level_values(0).to_numpy()
    ud, inv = np.unique(days, return_inverse=True)
    cnt = np.bincount(inv)
    out = {}
    for m in models:
        if m not in piv:
            continue
        diff = (piv[base] - piv[m]).to_numpy()
        sums = np.bincount(inv, weights=diff)
        bs = boot_days(sums, cnt)
        out[m] = (diff.mean(), np.percentile(bs, 2.5), np.percentile(bs, 97.5), len(diff))
    return out


def ci(t, k=4):
    return f"{t[0]:+.{k}f} [{t[1]:+.{k}f}, {t[2]:+.{k}f}]"


def calib_slope(p, y):
    from scipy.optimize import minimize
    p = np.clip(p, 1e-6, 1 - 1e-6); lg = np.log(p / (1 - p))
    o = minimize(lambda th: -np.sum(y * (th[0] + th[1] * lg) - np.logaddexp(0, th[0] + th[1] * lg)), [0, 1], method="BFGS")
    return o.x[1]


# ------------------------------------------------------------------ accuracy
def accuracy(R, U, label, models):
    L = [f"\n### {label}", "", "| Model | Races | Win log-loss | Top-2 Brier | Top-3 Brier | Exacta LL | Trifecta LL | P(2nd) slope | P(3rd) slope | Place-prob slope |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    rows = []
    for m in models:
        g = R[R.model == m]
        if not len(g):
            continue
        y2 = (U.pos == 2).astype(float).to_numpy(); y3 = (U.pos == 3).astype(float).to_numpy()
        ok = U.places > 0
        s2 = calib_slope(U[f"P2_{m}"].to_numpy(), y2); s3 = calib_slope(U[f"P3_{m}"].to_numpy(), y3)
        sk = calib_slope(U.loc[ok, f"Pk_{m}"].to_numpy(), (U.loc[ok, "frac"] > 0).astype(float).to_numpy())
        r = dict(period=label, model=m, races=g.race_id.nunique(), ll_win=g.ll_win.mean(), brier2=g.brier2.sum() / g.nr.sum(),
                 brier3=g.brier3.sum() / g.nr.sum(), ll_ex=g.ll_ex.mean(), ll_tri=g.ll_tri.mean(), slope2=s2, slope3=s3, slopek=sk)
        rows.append(r)
        L.append(f"| {NAMES[m]} | {r['races']:,} | {r['ll_win']:.4f} | {r['brier2']:.5f} | {r['brier3']:.5f} | {r['ll_ex']:.4f} | {r['ll_tri']:.4f} | {s2:.2f} | {s3:.2f} | {sk:.2f} |")
    L.append("")
    L.append("Paired gains vs market + discounted Harville (A minus model; positive = model better), 95% day-block interval:")
    for col, lab in (("ll_win", "win log-loss"), ("brier2", "top-2 Brier (per race)"), ("brier3", "top-3 Brier (per race)"), ("ll_ex", "exacta LL"), ("ll_tri", "trifecta LL")):
        p = paired(R, col, models=[m for m in models if m != "A"])
        L.append(f"- {lab}: " + "; ".join(f"{m} {ci(v)}" for m, v in p.items()))
        for m, v in p.items():
            rows.append(dict(period=label, model=m, metric=f"gain_{col}", est=v[0], lo=v[1], hi=v[2], n=v[3]))
    return L, rows


# ------------------------------------------------------------------ betting
def bets(U, m, T, c):
    x = U[(U.places > 0) & np.isfinite(U.psp) & (U.psp > 1)].copy()
    x["P"] = x[f"Pk_{m}"]
    x["ev"] = x.P * (1 + (x.psp - 1) * (1 - c)) - 1
    x = x[x.ev >= T].copy()
    x["ret"] = x.frac * (1 + (x.psp - 1) * (1 - c))
    x["pl"] = x.ret - 1
    return x


def bet_stats(x, c, sims=True):
    if not len(x):
        return dict(bets=0)
    d = x.groupby("date").agg(pl=("pl", "sum"), n=("pl", "size"))
    bs = boot_days(d.pl.to_numpy(), d.n.to_numpy())
    xs = x.sort_values(["date", "race_id"])
    cum = xs.pl.cumsum().to_numpy()
    dd = float(np.max(np.maximum.accumulate(np.r_[0, cum])[1:] - cum))
    run = mx = 0
    for v in (xs.pl < 0).to_numpy():
        run = run + 1 if v else 0; mx = max(mx, run)
    mon = x.groupby("month").pl.sum()
    q = x.assign(q=pd.PeriodIndex(pd.to_datetime(x.date), freq="Q").astype(str)).groupby("q").pl.sum()
    srt = np.sort(x.ret.to_numpy())[::-1]
    n1 = max(1, int(round(0.01 * len(x)))); n5 = max(1, int(round(0.05 * len(x))))
    out = dict(bets=len(x), stake=float(len(x)), ret=float(x.ret.sum()), pl=float(x.pl.sum()), roi=float(x.pl.mean()),
               lo=float(np.percentile(bs, 2.5)), hi=float(np.percentile(bs, 97.5)), lo_bonf=float(np.percentile(bs, 0.07)), hi_bonf=float(np.percentile(bs, 99.93)),
               median_psp=float(x.psp.median()), mean_psp=float(x.psp.mean()), max_payout=float(x.ret.max()),
               pl_ex_top1=float(x.pl.sum() - (srt[:n1] - 1).sum()), pl_ex_top5=float(x.pl.sum() - (srt[:n5] - 1).sum()),
               months_profit=int((mon > 0).sum()), months=int(len(mon)), quarters_profit=int((q > 0).sum()), quarters=int(len(q)),
               longest_losing=mx, maxdd=dd, month_pl=json.dumps({k: round(v, 2) for k, v in mon.items()}))
    if sims:
        # outcome simulation under (i) the model's own probabilities, (ii) place-SP implied probabilities (no-edge null)
        win_ret = 1 + (x.psp.to_numpy() - 1) * (1 - c)
        for lab, p in (("model", x.P.to_numpy()), ("market", np.clip(x.imp_psp.to_numpy(), 0, 1))):
            ok = np.isfinite(p)
            draws = rng.random((1000, ok.sum())) < p[ok]
            roi = (draws * win_ret[ok]).sum(1) / ok.sum() - 1
            out[f"sim_{lab}_mean"] = float(roi.mean()); out[f"sim_{lab}_p95"] = float(np.percentile(roi, 95))
            out[f"p_obs_ge_{lab}"] = float((roi >= out["roi"]).mean())
    return out


def betting(U, label, models=("A", "B", "C", "D")):
    rows = []
    for c in COMMS:
        for T in THRESH:
            for m in models:
                s = bet_stats(bets(U, m, T, c), c)
                rows.append(dict(period=label, model=m, comm=c, T=T, **s))
    allb = U[(U.places > 0) & np.isfinite(U.psp) & (U.psp > 1)].copy()
    for c in COMMS:
        allb["ret"] = allb.frac * (1 + (allb.psp - 1) * (1 - c)); allb["pl"] = allb.ret - 1
        rows.append(dict(period=label, model="ALL", comm=c, T=np.nan, **bet_stats(allb, c, sims=False)))
    return rows


# ------------------------------------------------------------------ disagreement
BANDS = [-1, -0.15, -0.10, -0.05, 0.05, 0.10, 0.15, 1]
BLAB = ["< -15", "-15..-10", "-10..-5", "-5..+5", "+5..+10", "+10..+15", "> +15"]


def disagreement(U, label, a="B", base="A", against="harville"):
    x = U[(U.places > 0)].copy()
    x["d"] = x[f"Pk_{a}"] - (x[f"Pk_{base}"] if against == "harville" else x.imp_psp)
    x = x[np.isfinite(x.d)]
    x["band"] = pd.cut(x.d, BANDS, labels=BLAB)
    x["placed"] = (x.frac > 0).astype(float)
    x["ret"] = x.frac * (1 + (x.psp - 1) * 0.98); x["pl"] = x.ret - 1
    x["ev"] = x[f"Pk_{a}"] * (1 + (x.psp - 1) * 0.98) - 1
    rows = []
    for b, g in x.groupby("band", observed=True):
        gp = g[np.isfinite(g.psp) & (g.psp > 1)]
        lo = hi = np.nan
        if len(gp) > 20:
            d = gp.groupby("date").agg(pl=("pl", "sum"), n=("pl", "size"))
            bs = boot_days(d.pl.to_numpy(), d.n.to_numpy())
            lo, hi = np.percentile(bs, [2.5, 97.5])
        rows.append(dict(period=label, against=against, band=b, n=len(g), share=len(g) / len(x), P_model=g[f"Pk_{a}"].mean(), P_mkt_harville=g[f"Pk_{base}"].mean(),
                         P_psp=g.imp_psp.mean(), actual=g.placed.mean(), err_model=g.placed.mean() - g[f"Pk_{a}"].mean(),
                         err_mkt=g.placed.mean() - g[f"Pk_{base}"].mean(), err_psp=g.placed.mean() - g.imp_psp.mean(),
                         n_priced=len(gp), mean_psp=gp.psp.mean(), median_psp=gp.psp.median(), ev_model=gp.ev.mean(), roi=gp.pl.mean(), lo=lo, hi=hi))
    return rows


# ------------------------------------------------------------------ segments
def segments(U, R, label):
    x = U[(U.places > 0)].copy()
    x["placed"] = (x.frac > 0).astype(float)
    x["ret"] = x.frac * (1 + (x.psp - 1) * 0.98); x["pl"] = x.ret - 1
    x["field"] = pd.cut(x.n, [0, 7, 11, 15, 99], labels=["5-7", "8-11", "12-15", "16+"])
    x["oddsband"] = pd.cut(1 / x.m, [1, 3, 5, 8, 13, 21, 41, 1e9], labels=["<3", "3-5", "5-8", "8-13", "13-21", "21-41", "41+"])
    x["pband"] = pd.cut(x.m, [0, 0.02, 0.05, 0.1, 0.2, 1], labels=["<2%", "2-5%", "5-10%", "10-20%", "20%+"])
    x["rankg"] = np.where(x["rank"] <= 3, "1-3", np.where(x["rank"] <= 8, "4-8", "9+"))
    rows = []
    for seg in ("field", "code", "hcap", "oddsband", "pband", "rank", "rankg"):
        for k, g in x.groupby(seg, observed=True):
            if seg == "rank" and k > 10:
                continue
            gp = g[np.isfinite(g.psp) & (g.psp > 1)]
            rows.append(dict(period=label, subset="all", seg=seg, value=str(k), n=len(g), actual=g.placed.mean(),
                             **{f"P_{m}": g[f"Pk_{m}"].mean() for m in ("H", "A", "B", "C", "D")},
                             P_psp=g.imp_psp.mean(), n_priced=len(gp), roi_all=gp.pl.mean() if len(gp) else np.nan))
    m48 = x[(x["rank"] >= 4) & (x["rank"] <= 8)]
    for seg in ("field", "code", "hcap", "oddsband", "pband", "rank"):
        for k, g in m48.groupby(seg, observed=True):
            gp = g[np.isfinite(g.psp) & (g.psp > 1)]
            lo = hi = np.nan
            if len(gp) > 50:
                d = gp.groupby("date").agg(pl=("pl", "sum"), n=("pl", "size"))
                bs = boot_days(d.pl.to_numpy(), d.n.to_numpy()); lo, hi = np.percentile(bs, [2.5, 97.5])
            rows.append(dict(period=label, subset="rank4-8", seg=seg, value=str(k), n=len(g), actual=g.placed.mean(),
                             **{f"P_{m}": g[f"Pk_{m}"].mean() for m in ("H", "A", "B", "C", "D")},
                             P_psp=g.imp_psp.mean(), n_priced=len(gp), roi_all=gp.pl.mean() if len(gp) else np.nan, lo=lo, hi=hi))
    # accuracy by field size
    R = R.copy(); R["field"] = pd.cut(R.n, [0, 7, 11, 15, 99], labels=["5-7", "8-11", "12-15", "16+"])
    acc = []
    for k, g in R.groupby("field", observed=True):
        for col in ("brier3", "ll_tri"):
            p = paired(g, col, models=("H", "B", "C", "D"))
            for m, v in p.items():
                acc.append(dict(period=label, field=k, metric=col, model=m, est=v[0], lo=v[1], hi=v[2], races=v[3]))
    return rows, acc


# ------------------------------------------------------------------ movement (Phase 12)
def movement(U):
    x = U.copy()
    S = pd.read_pickle(os.path.join(W, "S.pkl"))[["race_id", "horse", "bsp"]]
    x = x.merge(S, on=["race_id", "horse"], how="left")
    x["pb"] = (1 / x.bsp).where(x.bsp > 1)
    x["pb"] = x.pb / x.groupby("race_id").pb.transform("sum")
    x = x[np.isfinite(x.pb) & (x.pb > 0)]
    x["dis"] = np.log(x.f) - np.log(x.m)
    x["move"] = np.log(x.pb) - np.log(x.m)
    out = []
    for lab, g in (("dev", period(x, "dev")), ("hold", period(x, "hold"))):
        b = np.polyfit(g.dis, g.move, 1)
        out.append(dict(period=lab, n=len(g), slope=b[0], corr=np.corrcoef(g.dis, g.move)[0, 1]))
    return out


def main():
    RS = pd.read_csv(os.path.join(W, "S_races.csv.gz")); US = pd.read_csv(os.path.join(W, "S_runners.csv.gz"))
    RG = pd.read_csv(os.path.join(W, "G_races.csv.gz")); UG = pd.read_csv(os.path.join(W, "G_runners.csv.gz"))
    RV = pd.read_csv(os.path.join(W, "G_rev_races.csv.gz")); UV = pd.read_csv(os.path.join(W, "G_rev_runners.csv.gz"))
    L, acc_rows = [], []
    for lab, R, U, ms in (("S development May-Aug 2026 (SYNTHETIC replay)", period(RS, "dev"), period(US, "dev"), "HABCD"),
                          ("S holdout 1 Sep-12 Oct 2026 (SYNTHETIC replay)", period(RS, "hold"), period(US, "hold"), "HABCD"),
                          ("G genuine archive 10-18 Nov 2026 (model input)", RG, UG, "HABCD"),
                          ("G genuine archive 10-18 Nov 2026 (reviewer input as B)", RV, UV, "ABC")):
        l, r = accuracy(R, U, lab, ms); L += l; acc_rows += r
    for m in ("2026-05", "2026-06", "2026-07", "2026-08", "2026-09", "2026-10"):
        p = paired(RS[RS.month == m], "brier3", models=("B", "C", "D")); p2 = paired(RS[RS.month == m], "ll_tri", models=("B", "C", "D"))
        for k in p:
            acc_rows.append(dict(period=m, model=k, metric="gain_brier3", est=p[k][0], lo=p[k][1], hi=p[k][2], n=p[k][3]))
            acc_rows.append(dict(period=m, model=k, metric="gain_ll_tri", est=p2[k][0], lo=p2[k][1], hi=p2[k][2], n=p2[k][3]))
    pd.DataFrame(acc_rows).to_csv(os.path.join(OUT, "accuracy.csv"), index=False)
    bet_rows = betting(period(US, "dev"), "dev") + betting(period(US, "hold"), "hold") + betting(UG, "G") + betting(UV, "G_rev", models=("A", "B", "C"))
    for m in DEV + HOLD:
        for r in betting(US[US.month == m], m):
            bet_rows.append({k: v for k, v in r.items() if not k.startswith(("sim_", "p_obs"))})
    pd.DataFrame(bet_rows).to_csv(os.path.join(OUT, "betting_cells.csv"), index=False)
    dis = []
    for lab, U in (("dev", period(US, "dev")), ("hold", period(US, "hold")), ("G", UG)):
        dis += disagreement(U, lab, against="harville") + disagreement(U, lab, against="psp")
        dis += [dict(r, model="C") for r in disagreement(U, lab, a="C", against="psp")]
    pd.DataFrame(dis).to_csv(os.path.join(OUT, "disagreement.csv"), index=False)
    seg, sacc = [], []
    for lab, R, U in (("dev", period(RS, "dev"), period(US, "dev")), ("hold", period(RS, "hold"), period(US, "hold")), ("G", RG, UG)):
        a, b = segments(U, R, lab); seg += a; sacc += b
    pd.DataFrame(seg).to_csv(os.path.join(OUT, "segments.csv"), index=False)
    pd.DataFrame(sacc).to_csv(os.path.join(OUT, "field_accuracy.csv"), index=False)
    pd.DataFrame(movement(US)).to_csv(os.path.join(OUT, "movement.csv"), index=False)
    open(os.path.join(OUT, "accuracy_tables.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
