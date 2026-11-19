"""Phase 4 evaluation: metrics, paired intervals, calibration, checkpoint experiment, limited betting, charts.
  python3 research/model_reconstruction/phase4/p4_eval.py  (after p4_run.py) -> out/*.csv, out/*.png, out/selection.json
"""
import json, os, sys, warnings
warnings.filterwarnings('ignore')
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p4_models as P  # noqa: E402

W, OUT = os.path.join(HERE, "work"), os.path.join(HERE, "out")
EPS = 1e-9
rng = np.random.default_rng(20261119)
DEV = ["2026-05", "2026-06", "2026-07", "2026-08"]; RE = ["2026-09", "2026-10"]; H3 = ["H3-10", "H3-11"]
MODELS = {"f": "Existing model (replay)", "m_M": "09:00 market", "pA": "A Improved current (linear, new features)", "pB": "B Pairwise boosted",
          "pC": "C Listwise boosted", "pD1": "D1 Market residual (linear)", "pD2": "D2 Market residual (boosted)", "pE": "E Hybrid (market + C + existing)",
          "m_L": "Market 1 s before off (diagnostic)", "close": "BSP (diagnostic)"}


def metrics(d, col):
    d = d[d[col].notna()]
    y = d.y.values; p = d[col].clip(EPS, 1).values
    st, g = P.groups(d.race_id.values)
    p = p / np.add.reduceat(p, st)[g]
    ll = -np.log(p[y == 1]).mean()
    brier = np.add.reduceat((p - y) ** 2, st).mean()
    rank = d.assign(p=p).groupby("race_id").p.rank(ascending=False, method="average")
    win_rank = rank[y == 1].mean()
    top = d.assign(p=p).loc[lambda x: x.groupby("race_id").p.transform("max") == x.p].drop_duplicates("race_id")
    conc = 0.0; tot = 0
    for rid, gg in d.assign(p=p).groupby("race_id"):
        pw = gg.p[gg.y == 1].to_numpy(); pl = gg.p[gg.y == 0].to_numpy()
        conc += (pl < pw[0]).sum() + 0.5 * (pl == pw[0]).sum(); tot += len(pl)
    lg = np.log(p / (1 - p + EPS))
    from scipy.optimize import minimize
    o = minimize(lambda th: -np.sum(y * (th[0] + th[1] * lg) - np.logaddexp(0, th[0] + th[1] * lg)), [0, 1], method="BFGS")
    fav = d.assign(p=p)[d.groupby("race_id").m_M.transform("max") == d.m_M]
    out = dict(races=int(d.race_id.nunique()), ll=ll, brier=brier, top_win=float((top.y == 1).mean()), winner_rank=float(win_rank), concordance=conc / tot,
               cal_slope=o.x[1], cal_int=o.x[0], fav_pred=float(fav.p.mean()), fav_actual=float(fav.y.mean()))
    long = d.assign(p=p)[d.m_M < 0.02]
    out.update(longshot_pred=float(long.p.mean()), longshot_actual=float(long.y.mean()))
    return out


def paired(d, a, b, B=2000):
    """mean per-race LL(a) - LL(b): positive = b better than a. Day-block bootstrap."""
    w = d[d.y == 1]
    x = -np.log(w[a].clip(EPS)) + np.log(w[b].clip(EPS))
    t = pd.DataFrame({"date": w.date.values, "x": x.values}).groupby("date").x.agg(["sum", "size"])
    dr = rng.integers(0, len(t), (B, len(t)))
    bs = t["sum"].values[dr].sum(1) / t["size"].values[dr].sum(1)
    return float(x.mean()), float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5)), int(len(x))


def main():
    E = pd.read_pickle(os.path.join(W, "preds.pkl"))
    sets = {"development May-Aug": E[E.month.isin(DEV)], "re-used Sep-Oct": E[E.month.isin(RE)], "H3 26 Oct-18 Nov (re-used)": E[E.month.isin(H3) & E.close.notna()]}
    rows, prs = [], []
    for nm, d in sets.items():
        for col, lab in MODELS.items():
            if col not in d or d[col].isna().all():
                continue
            if col == "m_L" and nm.startswith("H3"):
                continue
            rows.append(dict(set=nm, model=lab, col=col, **metrics(d, col)))
            if col not in ("m_M",):
                t = paired(d[d[col].notna()], "m_M", col); prs.append(dict(set=nm, model=lab, vs="09:00 market", gain=t[0], lo=t[1], hi=t[2], races=t[3]))
            if col not in ("f", "m_M", "m_L", "close"):
                t = paired(d[d[col].notna()], "f", col); prs.append(dict(set=nm, model=lab, vs="existing model", gain=t[0], lo=t[1], hi=t[2], races=t[3]))
        for mth in sorted(d.month.unique()):
            dm = d[d.month == mth]
            for col in ("pA", "pB", "pC", "pD1", "pD2", "pE"):
                t = paired(dm, "m_M", col, B=500); prs.append(dict(set=f"month {mth}", model=MODELS[col], vs="09:00 market", gain=t[0], lo=t[1], hi=t[2], races=t[3]))
    R = pd.DataFrame(rows); PR = pd.DataFrame(prs)
    R.to_csv(os.path.join(OUT, "metrics.csv"), index=False); PR.to_csv(os.path.join(OUT, "paired_gains.csv"), index=False)
    print(R.round(4).to_string()); print(PR[~PR.set.str.startswith("month")].round(4).to_string())
    # model selection rule (sealed): mean dev gain vs market, lower bound > 0; ties within 0.002 -> simpler
    dev = PR[(PR.set == "development May-Aug") & (PR.vs == "09:00 market") & PR.model.isin(["A Improved current (linear, new features)", "B Pairwise boosted", "C Listwise boosted", "D1 Market residual (linear)", "D2 Market residual (boosted)", "E Hybrid (market + C + existing)"])].sort_values("gain", ascending=False)
    order = ["D1 Market residual (linear)", "A Improved current (linear, new features)", "D2 Market residual (boosted)", "E Hybrid (market + C + existing)", "C Listwise boosted", "B Pairwise boosted"]
    best = dev.iloc[0]
    tied = dev[dev.gain >= best.gain - 0.002]
    chosen = sorted(tied.model, key=order.index)[0]
    sel = dict(rule="max mean development gain vs 09:00 market; ties within 0.002 -> simpler", ranking=dev[["model", "gain", "lo", "hi"]].to_dict("records"), chosen=chosen)
    for nm in ("re-used Sep-Oct", "H3 26 Oct-18 Nov (re-used)"):
        r = PR[(PR.set == nm) & (PR.vs == "09:00 market") & (PR.model == chosen)]
        sel[nm] = r[["gain", "lo", "hi", "races"]].to_dict("records")
    json.dump(sel, open(os.path.join(OUT, "selection.json"), "w"), indent=1, default=float)
    print(json.dumps(sel, indent=1, default=float))
    # calibration by 09:00 odds band (re-used + H3 pooled)
    d = pd.concat([sets["re-used Sep-Oct"], sets["H3 26 Oct-18 Nov (re-used)"]])
    d["band"] = pd.cut(1 / d.m_M, [1, 2.5, 5, 10, 20, 50, 1e9], labels=["<2.5", "2.5-5", "5-10", "10-20", "20-50", "50+"])
    cal = d.groupby("band", observed=True).agg(n=("y", "size"), actual=("y", "mean"), **{c: (c, "mean") for c in ("f", "m_M", "pA", "pC", "pD1", "pD2", "pE", "close")})
    cal.to_csv(os.path.join(OUT, "calibration_by_odds.csv")); print(cal.round(4).to_string())
    fig, ax = plt.subplots(figsize=(8.5, 4.4), dpi=130); xx = np.arange(len(cal))
    for c, lab, col, mk in (("actual", "Actual", "#111", "o"), ("f", "Existing model", "#c0632b", "v"), ("pA", "A improved", "#e0a03a", "<"), ("pC", "C listwise", "#8e5bb5", ">"),
                            ("m_M", "09:00 market", "#7a7a7a", "^"), ("pD1", "D1 market residual", "#2f6db3", "D"), ("close", "BSP", "#2a9d4b", "s")):
        ax.plot(xx, cal[c], marker=mk, color=col, label=lab, lw=2.4 if c == "actual" else 1.3, ms=5)
    ax.set_yscale("log"); ax.set_xticks(xx, cal.index.astype(str)); ax.set_xlabel("09:00 odds band"); ax.set_ylabel("Win probability (log)")
    ax.set_title("Calibration by odds band (Sep-Oct + H3, re-used periods)", fontsize=10.5); ax.legend(fontsize=7.5, frameon=False); ax.grid(alpha=0.25, which="both")
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "calibration_by_odds.png")); plt.close(fig)
    # ranking chart: log-loss gap to market by month
    pm = PR[PR.set.str.startswith("month")].copy(); pm["month"] = pm.set.str.replace("month ", "")
    fig, ax = plt.subplots(figsize=(8.5, 4.2), dpi=130)
    for lab in ["A Improved current (linear, new features)", "B Pairwise boosted", "C Listwise boosted", "D1 Market residual (linear)", "D2 Market residual (boosted)", "E Hybrid (market + C + existing)"]:
        x = pm[pm.model == lab]; ax.plot(x.month, x.gain, "o-", label=lab, ms=4)
    base = pd.DataFrame([dict(month=m, g=paired(E[E.month == m], "m_M", "f", B=200)[0]) for m in DEV + RE + H3])
    ax.plot(base.month, base.g, "k--", label="Existing model", lw=1)
    ax.axhline(0, color="#444", lw=0.8); ax.set_ylabel("Log-loss gain vs 09:00 market (per race)"); ax.set_title("Gain vs the 09:00 market by test month", fontsize=10.5)
    ax.legend(fontsize=7, frameon=False); ax.grid(alpha=0.25); plt.xticks(rotation=30)
    fig.tight_layout(); fig.savefig(os.path.join(OUT, "gain_vs_market_by_month.png")); plt.close(fig)
    # checkpoint experiment (S3 months)
    ck = []
    for nm, d in (("development May-Aug", sets["development May-Aug"]), ("re-used Sep-Oct", sets["re-used Sep-Oct"])):
        for cp in ("E", "M", "H", "T10", "L"):
            if f"pD1_{cp}" not in d:
                continue
            dd = d[d[f"pD1_{cp}"].notna()]
            t = paired(dd, f"pM_{cp}", f"pD1_{cp}"); t2 = paired(dd, f"pM_{cp}", f"pMs_{cp}")
            ck.append(dict(set=nm, checkpoint=cp, market_ll=float(-np.log(dd[dd.y == 1][f"pM_{cp}"].clip(EPS)).mean()), residual_gain=t[0], lo=t[1], hi=t[2],
                           sharpening_only_gain=t2[0], features_beyond_sharpening=t[0] - t2[0], races=t[3]))
    CK = pd.DataFrame(ck); CK.to_csv(os.path.join(OUT, "checkpoint_experiment.csv"), index=False); print(CK.round(4).to_string())
    # limited betting: EV >= 4% at 09:00, exchange quote (2%) and bookmaker best; development + re-used + H3 (all re-used / dev)
    bet = []
    for nm, d in sets.items():
        for col in ("f", "m_M", "pA", "pC", "pD1", "pE", chosen_col(chosen)):
            for price, c in (("bf_M", 0.02), ("best_M", 0.0)):
                if price not in d:
                    continue
                x = d[d[price] > 1].copy()
                net = 1 + (x[price] - 1) * (1 - c)
                x = x[x[col] * net - 1 >= 0.04]
                if not len(x):
                    continue
                pl = np.where(x.y == 1, 1 + (x[price] - 1) * (1 - c), 0) - 1
                t = pd.DataFrame({"date": x.date.values, "pl": pl}).groupby("date").pl.agg(["sum", "size"])
                dr = rng.integers(0, len(t), (2000, len(t))); bs = t["sum"].values[dr].sum(1) / t["size"].values[dr].sum(1)
                clv = np.log(x.close.clip(EPS)) - np.log(x.m_M.clip(EPS))
                cum = np.cumsum(pl); dd_ = float(np.max(np.maximum.accumulate(np.r_[0, cum])[1:] - cum))
                bet.append(dict(set=nm, model=MODELS.get(col, col), price="exchange 2%" if price == "bf_M" else "bookmaker best", bets=len(x), roi=pl.mean(),
                                lo=np.percentile(bs, 2.5), hi=np.percentile(bs, 97.5), avg_odds=x[price].mean(), prob_clv=clv.mean(), max_dd=dd_,
                                roi_5pct_comm=float((np.where(x.y == 1, 1 + (x[price] - 1) * 0.95, 0) - 1).mean()) if price == "bf_M" else np.nan))
    BT = pd.DataFrame(bet).drop_duplicates(["set", "model", "price"]); BT.to_csv(os.path.join(OUT, "betting.csv"), index=False); print(BT.round(3).to_string())


def chosen_col(lab):
    return {v: k for k, v in MODELS.items()}[lab]


if __name__ == "__main__":
    main()
