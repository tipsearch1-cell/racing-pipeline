"""Phase 3 analyses (spec prereg/MARKET_INTEL_PHASE3_SPEC_2026-11-19.md).  python3 research/market_intelligence/phase3/p3.py
Reads work/{S3,H3,A3}.pkl (p3_data.py). Writes out/*.csv and out/p3_log.md.
"""
import json, os, sys
import numpy as np
import pandas as pd
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "research", "harville"))
from run import clogit_nll, hess, se  # noqa: E402 (Phase 1 conditional logit)

W, OUT = os.path.join(HERE, "work"), os.path.join(HERE, "out")
rng = np.random.default_rng(20261119)
DEV = ["2026-05", "2026-06", "2026-07", "2026-08"]
REUSED = ["2026-09", "2026-10"]
CPS = ["M", "H", "T10", "L"]
EPS = 1e-6
LOG = []


def log(s=""):
    LOG.append(s); print(s)


# ------------------------------------------------------------------ helpers
def eligible(df, cols):
    ok = df.pos.notna().groupby(df.race_id).transform("any")
    w = (df.pos == 1).groupby(df.race_id).transform("sum") == 1
    full = np.ones(len(df), bool)
    for c in cols:
        full &= df.groupby("race_id")[c].transform(lambda s: s.notna().all() and (s > 0).all()).to_numpy()
    return df[ok & w & full].copy()


def clogit_fit(df, feats, l2=0.0, x0=None):
    d = df.sort_values("race_id")
    X = d[feats].to_numpy(float); y = (d.pos == 1).to_numpy(float)
    gid = pd.factorize(d.race_id)[0]; ng = gid.max() + 1
    x0 = np.ones(len(feats)) if x0 is None else x0
    o = minimize(clogit_nll, x0, args=(X, y, gid, ng, l2), jac=True, method="L-BFGS-B")
    return o.x, se(hess(o.x, X, y, gid, ng))


def pool(df, cols, w):
    lw = sum(wi * np.log(df[c].clip(EPS)) for c, wi in zip(cols, w))
    e = np.exp(lw - lw.groupby(df.race_id).transform("max"))
    return e / e.groupby(df.race_id).transform("sum")


def day_boot(vals_by_day, cnt_by_day, B=2000):
    d = len(vals_by_day); dr = rng.integers(0, d, (B, d))
    return vals_by_day[dr].sum(1) / cnt_by_day[dr].sum(1)


def win_metrics(df, col):
    y = (df.pos == 1).to_numpy(float); p = df[col].clip(EPS, 1 - EPS).to_numpy()
    w = df[df.pos == 1]
    ll = -np.log(w[col].clip(EPS)).mean()
    brier = np.mean((p - y) ** 2)
    q = pd.qcut(pd.Series(p).rank(method="first"), 10, labels=False)
    t = pd.DataFrame({"p": p, "y": y, "q": q}).groupby("q").agg(p=("p", "mean"), y=("y", "mean"), n=("y", "size"))
    ece = float((t.n * (t.p - t.y).abs()).sum() / t.n.sum())
    lg = np.log(p / (1 - p))
    o = minimize(lambda th: -np.sum(y * (th[0] + th[1] * lg) - np.logaddexp(0, th[0] + th[1] * lg)), [0, 1], method="BFGS")
    # concordance: share of (winner, loser) pairs in the same race where the winner has the higher probability
    conc, tot = 0.0, 0
    for _, g in df.groupby("race_id"):
        pw = g.loc[g.pos == 1, col].to_numpy()
        pl = g.loc[g.pos != 1, col].to_numpy()
        if len(pw) == 1 and len(pl):
            conc += (pl < pw[0]).sum() + 0.5 * (pl == pw[0]).sum(); tot += len(pl)
    top = df.loc[df.groupby("race_id")[col].idxmax()]
    return dict(ll=ll, brier=brier, ece=ece, slope=o.x[1], intercept=o.x[0], concordance=conc / max(tot, 1), top_win=(top.pos == 1).mean(),
                races=df.race_id.nunique(), runners=len(df))


def paired_ll(df, a, b, B=2000):
    """mean per-race log-loss of a minus b (positive = b better), day-block CI."""
    w = df[df.pos == 1]
    diff = (-np.log(w[a].clip(EPS))) - (-np.log(w[b].clip(EPS)))
    d = pd.DataFrame({"date": w.date, "x": diff}).groupby("date").x.agg(["sum", "size"])
    bs = day_boot(d["sum"].to_numpy(), d["size"].to_numpy(), B)
    return diff.mean(), np.percentile(bs, 2.5), np.percentile(bs, 97.5), len(diff)


def ci(t, k=4):
    return f"{t[0]:+.{k}f} [{t[1]:+.{k}f}, {t[2]:+.{k}f}] (n={t[3]:,})"


# ------------------------------------------------------------------ fit second-stage params walk-forward on S3
def fit_params(train):
    prm = {}
    tr = train.assign(lf=np.log(train.f.clip(EPS)))
    prm["a"], prm["a_se"] = clogit_fit(tr, ["lf"])
    for cp in CPS:
        t = eligible(train, [f"m_{cp}", "f"]).assign(lm=lambda d: np.log(d[f"m_{cp}"].clip(EPS)), lf=lambda d: np.log(d.f.clip(EPS)))
        prm[f"w_{cp}"], prm[f"w_{cp}_se"] = clogit_fit(t, ["lm", "lf"], x0=np.array([1.0, 0.0]))
    return prm


def apply_params(df, prm, cps=CPS):
    df = df.copy()
    lf = prm["a"][0] * np.log(df.f.clip(EPS))
    e = np.exp(lf - lf.groupby(df.race_id).transform("max")); df["f_cal"] = e / e.groupby(df.race_id).transform("sum")
    for cp in cps:
        if f"m_{cp}" in df:
            df[f"b_{cp}"] = pool(df, [f"m_{cp}", "f"], prm[f"w_{cp}"])
    return df


def walk_forward(S):
    outs, params = [], {}
    for mth in DEV + REUSED:
        tr = eligible(S[(S.month < mth) & (S.month >= "2026-03")], ["m_M", "f"])
        te = S[S.month == mth]
        prm = fit_params(tr)
        params[mth] = {k: np.asarray(v).tolist() for k, v in prm.items()}
        outs.append(apply_params(te, prm))
    return pd.concat(outs), params


# ------------------------------------------------------------------ betting
def strat_bets(df, prob, price_col, T, c, exchange=True, extra=None):
    x = df[np.isfinite(df[price_col]) & (df[price_col] > 1) & df[prob].notna()].copy()
    if extra is not None:
        x = x[extra(x)]
    net = 1 + (x[price_col] - 1) * (1 - c) if exchange else x[price_col]
    x["ev"] = x[prob] * net - 1
    x = x[x.ev >= T].copy()
    netx = 1 + (x[price_col] - 1) * (1 - c) if exchange else x[price_col]
    x["ret"] = np.where(x.pos == 1, netx, 0.0)
    x["pl"] = x.ret - 1
    x["clv_bsp"] = x[price_col] / x.bsp - 1
    x["price"] = x[price_col]
    return x


def bet_stats(x, B=2000):
    if not len(x):
        return dict(bets=0)
    d = x.groupby("date").agg(pl=("pl", "sum"), n=("pl", "size"))
    bs = day_boot(d.pl.to_numpy(), d.n.to_numpy(), B)
    xs = x.sort_values(["date", "race_id"]); cum = xs.pl.cumsum().to_numpy()
    dd = float(np.max(np.maximum.accumulate(np.r_[0, cum])[1:] - cum))
    run = mx = 0
    for v in (xs.pl < 0).to_numpy():
        run = run + 1 if v else 0; mx = max(mx, run)
    mon = x.groupby("month").pl.sum()
    srt = np.sort(x.ret.to_numpy())[::-1]; n1 = max(1, int(round(0.01 * len(x))))
    # null: outcomes drawn from closing (BSP-normalised) probabilities
    pc = x.close.to_numpy(); ok = np.isfinite(pc)
    sims = (rng.random((1000, ok.sum())) < pc[ok]) * x.ret.where(x.pos == 1, np.nan).fillna(1 + (x.price - 1)).to_numpy()[ok]
    null_roi = sims.sum(1) / ok.sum() - 1
    clv = x.clv_bsp[np.isfinite(x.clv_bsp)]
    return dict(bets=len(x), stake=float(len(x)), ret=float(x.ret.sum()), pl=float(x.pl.sum()), roi=float(x.pl.mean()),
                lo=float(np.percentile(bs, 2.5)), hi=float(np.percentile(bs, 97.5)), lo_bonf=float(np.percentile(bs, 0.05)),
                avg_odds=float(x.price.mean()), med_odds=float(x.price.median()), maxdd=dd, longest_losing=mx,
                months_profit=int((mon > 0).sum()), months=int(len(mon)), roi_ex_top1=float((x.pl.sum() - (srt[:n1] - 1).sum()) / len(x)),
                clv_mean=float(clv.mean()) if len(clv) else np.nan, clv_median=float(clv.median()) if len(clv) else np.nan,
                beat_close=float((clv > 0).mean()) if len(clv) else np.nan, null_mean=float(null_roi.mean()), p_null=float((null_roi >= x.pl.mean()).mean()),
                month_pl=json.dumps({k: round(v, 2) for k, v in mon.items()}))


# ------------------------------------------------------------------ main
def main():
    os.makedirs(OUT, exist_ok=True)
    S = pd.read_pickle(os.path.join(W, "S3.pkl")); H3 = pd.read_pickle(os.path.join(W, "H3.pkl")); A3 = pd.read_pickle(os.path.join(W, "A3.pkl"))
    S = eligible(S, ["m_M", "f"])
    log("# Phase 3 run log\n")
    SW, params = walk_forward(S)
    prmF = fit_params(eligible(S, ["m_M", "f"]))
    params["final"] = {k: np.asarray(v).tolist() for k, v in prmF.items()}
    json.dump(params, open(os.path.join(OUT, "params.json"), "w"), indent=1)
    for k, v in params.items():
        log(f"- params {k}: a={np.round(v['a'], 3)} w_M={np.round(v['w_M'], 3)} (se {np.round(v['w_M_se'], 3)}) w_H={np.round(v['w_H'], 3)} w_T10={np.round(v['w_T10'], 3)} w_L={np.round(v['w_L'], 3)}")
    H3e = apply_params(eligible(H3, ["m_M", "f"]), prmF, cps=["M"])
    A3e = apply_params(eligible(A3, ["m_M", "f"]), prmF, cps=["M"])
    sets = {"dev": SW[SW.month.isin(DEV)], "reused": SW[SW.month.isin(REUSED)], "H3": H3e, "A": A3e}

    # ---------------- win calibration
    rows = []
    for nm, d in sets.items():
        cols = ["f", "f_cal", "m_M", "b_M"] + (["m_H", "m_T10", "m_L"] if nm in ("dev", "reused") else [])
        dd = d[d.close.notna()] if nm != "A" else d
        for c in cols + (["close"] if d.close.notna().any() else []):
            g = dd if c != "close" else dd[dd.close.notna()]
            rows.append(dict(set=nm, prob=c, **win_metrics(g, c)))
        for c in ("f", "f_cal", "b_M", "close"):
            if c in dd and dd[c].notna().all():
                t = paired_ll(dd, "m_M", c)
                rows.append(dict(set=nm, prob=f"gain_vs_m_M:{c}", ll=t[0], lo=t[1], hi=t[2], races=t[3]))
    cal = pd.DataFrame(rows); cal.to_csv(os.path.join(OUT, "win_calibration.csv"), index=False)
    log("\n## Win calibration\n" + cal.round(4).to_string())
    # segments: predicted vs actual and LL by cut (reused + H3 pooled as 'later'; dev separately)
    seg = []
    for nm in ("dev", "reused", "H3"):
        d = sets[nm].copy(); d = d[d.close.notna()] if nm == "H3" else d
        d["rank_f"] = d.groupby("race_id").f.rank(ascending=False, method="first")
        d["oddsband"] = pd.cut(1 / d.m_M, [1, 2.5, 5, 10, 20, 50, 1e9], labels=["<2.5", "2.5-5", "5-10", "10-20", "20-50", "50+"])
        d["pband"] = pd.cut(d.f_cal, [0, .02, .05, .1, .2, .35, 1], labels=["<2%", "2-5%", "5-10%", "10-20%", "20-35%", "35%+"])
        d["field"] = pd.cut(d.n, [0, 7, 11, 15, 99], labels=["<=7", "8-11", "12-15", "16+"])
        d["won"] = (d.pos == 1).astype(float)
        for cut in ("oddsband", "pband", "rank_f", "field", "code", "hcap"):
            for k, g in d.groupby(cut, observed=True):
                if cut == "rank_f" and k > 8:
                    continue
                w = g[g.pos == 1]
                seg.append(dict(set=nm, cut=cut, value=str(k), n=len(g), wins=int(g.won.sum()), actual=g.won.mean(), f=g.f.mean(), f_cal=g.f_cal.mean(),
                                m_M=g.m_M.mean(), b_M=g.b_M.mean(), close=g.close.mean()))
    pd.DataFrame(seg).to_csv(os.path.join(OUT, "win_segments.csv"), index=False)

    # ---------------- movement (S3 dev + reused)
    mv = []
    Sx = SW.copy()
    for a, b in (("M", "H"), ("H", "T10"), ("T10", "L")):
        ch = Sx[f"bf_{b}"] / Sx[f"bf_{a}"] - 1
        dp = Sx[f"m_{b}"] - Sx[f"m_{a}"]
        mv.append(dict(interval=f"{a}->{b}", n=int(ch.notna().sum()), med_abs_pct=float(ch.abs().median()), share_shorten=float((dp > 0.002).mean()),
                       share_drift=float((dp < -0.002).mean()), mean_abs_dprob=float(dp.abs().mean()),
                       rank_change_share=float((Sx.groupby("race_id")[f"m_{a}"].rank(ascending=False) != Sx.groupby("race_id")[f"m_{b}"].rank(ascending=False)).mean())))
    ch = Sx.close - Sx.m_L
    mv.append(dict(interval="L->BSP", n=int(ch.notna().sum()), mean_abs_dprob=float(ch.abs().mean()), share_shorten=float((ch > 0.002).mean()), share_drift=float((ch < -0.002).mean())))
    pd.DataFrame(mv).to_csv(os.path.join(OUT, "movement_intervals.csv"), index=False)
    # predictive value of later checkpoints and of movement beyond m_M
    pv = []
    for nm in ("dev", "reused"):
        d = sets[nm]
        for c in ("m_M", "m_H", "m_T10", "m_L", "close"):
            pv.append(dict(set=nm, prob=c, ll=-np.log(d[d.pos == 1][c].clip(EPS)).mean()))
    tr = sets["dev"].assign(lm=lambda d: np.log(d.m_M.clip(EPS)), mvL=lambda d: np.log(d.m_L.clip(EPS)) - np.log(d.m_M.clip(EPS)),
                            mvB=lambda d: np.log(d.close.clip(EPS)) - np.log(d.m_M.clip(EPS)), lf=lambda d: np.log(d.f.clip(EPS)) - np.log(d.m_M.clip(EPS)))
    cf, cse = clogit_fit(tr, ["lm", "mvL"], x0=np.array([1.0, 0.0]))
    pv.append(dict(set="dev", prob="clogit win ~ log m_M + move(M->L)", coef=json.dumps(np.round(cf, 3).tolist()), se=json.dumps(np.round(cse, 3).tolist())))
    cf2, cse2 = clogit_fit(tr, ["lm", "mvL", "lf"], x0=np.array([1.0, 0.0, 0.0]))
    pv.append(dict(set="dev", prob="clogit win ~ log m_M + move(M->L) + (log f - log m_M)", coef=json.dumps(np.round(cf2, 3).tolist()), se=json.dumps(np.round(cse2, 3).tolist())))
    pd.DataFrame(pv).to_csv(os.path.join(OUT, "movement_predictive.csv"), index=False)
    log("\n## Movement\n" + pd.DataFrame(mv).round(4).to_string() + "\n" + pd.DataFrame(pv).round(4).to_string())
    # correlation of disagreement with subsequent movement (verification of -0.27)
    cr = []
    for nm in ("dev", "reused", "H3"):
        d = sets[nm]
        dis = np.log(d.f.clip(EPS)) - np.log(d.m_M.clip(EPS))
        closers = (("H", "m_H"), ("T10", "m_T10"), ("L", "m_L"), ("BSP", "close")) if nm != "H3" else (("BSP", "close"),)
        for lab, col in closers:
            mvv = np.log(d[col].clip(EPS)) - np.log(d.m_M.clip(EPS))
            ok = np.isfinite(dis) & np.isfinite(mvv)
            dd = pd.DataFrame({"date": d.date[ok], "x": dis[ok], "y": mvv[ok]})
            r = np.corrcoef(dd.x, dd.y)[0, 1]
            days = dd.date.unique(); idx = {k: v for k, v in dd.groupby("date").indices.items()}
            bs = []
            for _ in range(500):
                ii = np.concatenate([idx[k] for k in rng.choice(days, len(days))])
                bs.append(np.corrcoef(dd.x.to_numpy()[ii], dd.y.to_numpy()[ii])[0, 1])
            cr.append(dict(set=nm, closer=lab, n=int(ok.sum()), corr=r, lo=np.percentile(bs, 2.5), hi=np.percentile(bs, 97.5)))
        if nm in ("dev", "reused"):
            for mth, g in d.groupby("month"):
                dis = np.log(g.f.clip(EPS)) - np.log(g.m_M.clip(EPS)); mvv = np.log(g.close.clip(EPS)) - np.log(g.m_M.clip(EPS))
                ok = np.isfinite(dis) & np.isfinite(mvv)
                cr.append(dict(set=mth, closer="BSP", n=int(ok.sum()), corr=np.corrcoef(dis[ok], mvv[ok])[0, 1]))
    pd.DataFrame(cr).to_csv(os.path.join(OUT, "disagreement_movement_corr.csv"), index=False)
    log("\n## Disagreement vs movement\n" + pd.DataFrame(cr).round(3).to_string())

    # ---------------- disagreement conditional models (fit on dev, score later sets)
    def dfeat(d, mcol):
        d = d.assign(lm=np.log(d[mcol].clip(EPS)), dl=np.log(d.f.clip(EPS)) - np.log(d[mcol].clip(EPS)))
        r = d.groupby("race_id")[mcol].rank(ascending=False, method="first")
        d["dpos"] = d.dl.clip(lower=0); d["dneg"] = d.dl.clip(upper=0)
        d["dpos_top3"] = d.dpos * (r <= 3); d["dneg_top3"] = d.dneg * (r <= 3)
        d["dpos_big"] = d.dpos * (d.n >= 12); d["dpos_jumps"] = d.dpos * (d.code == "Jumps"); d["dpos_hcap"] = d.dpos * d.hcap.astype(bool)
        return d
    F1 = ["lm", "dpos", "dneg"]; F2 = F1 + ["dpos_top3", "dneg_top3", "dpos_big", "dpos_jumps", "dpos_hcap"]
    dis_rows = []
    for mcol in ("m_M", "m_H", "m_T10", "m_L"):
        tr = dfeat(sets["dev"], mcol)
        for nmF, F in (("simple", F1), ("interactions", F2)):
            x0 = np.zeros(len(F)); x0[0] = 1
            cfx, sex = clogit_fit(tr, F, x0=x0)
            row = dict(market=mcol, form=nmF, coefs=json.dumps(dict(zip(F, np.round(cfx, 3).tolist()))), ses=json.dumps(dict(zip(F, np.round(sex, 3).tolist()))))
            for nm in ("reused", "H3") if mcol == "m_M" else ("reused",):
                te = dfeat(sets[nm][sets[nm].close.notna()] if nm == "H3" else sets[nm], mcol)
                s = te[F].to_numpy(float) @ cfx
                te = te.assign(s=s); e = np.exp(te.s - te.groupby("race_id").s.transform("max")); te["pd"] = e / e.groupby(te.race_id).transform("sum")
                t = paired_ll(te.assign(mm=te[mcol] / te.groupby("race_id")[mcol].transform("sum")), "mm", "pd")
                row[f"gain_{nm}"] = ci(t)
            dis_rows.append(row)
    pd.DataFrame(dis_rows).to_csv(os.path.join(OUT, "disagreement_models.csv"), index=False)
    log("\n## Disagreement models\n" + pd.DataFrame(dis_rows).to_string())
    band_rows = []
    for nm in ("dev", "reused", "H3", "A"):
        d = sets[nm]; d = d[d.close.notna()] if nm in ("H3", "A") else d
        dp = d.f - d.m_M
        b = pd.cut(dp, [-1, -.10, -.05, -.02, .02, .05, .10, 1], labels=["< -10", "-10..-5", "-5..-2", "-2..+2", "+2..+5", "+5..+10", "> +10"])
        for k, g in d.groupby(b, observed=True):
            band_rows.append(dict(set=nm, band=k, n=len(g), wins=int((g.pos == 1).sum()), actual=(g.pos == 1).mean(), f=g.f.mean(), f_cal=g.f_cal.mean(), m_M=g.m_M.mean(),
                                  close=g.close.mean(), drift=float((np.log(g.close.clip(EPS)) - np.log(g.m_M.clip(EPS))).mean())))
    pd.DataFrame(band_rows).to_csv(os.path.join(OUT, "disagreement_bands.csv"), index=False)

    # ---------------- CLV of selections
    clv_rows = []
    for nm in ("dev", "reused", "H3"):
        d = sets[nm][sets[nm].bsp.notna() & (sets[nm].best_M > 1)].copy()
        d["clv"] = d.best_M / d.bsp - 1
        d["clv_c2"] = d.best_M / (1 + (d.bsp - 1) * 0.98) - 1
        d["pclv"] = d.close - d.m_M
        d["lclv"] = np.log(d.close.clip(EPS)) - np.log(d.m_M.clip(EPS))
        d["bfclv"] = d.bf_M / d.bsp - 1
        d["band"] = pd.cut(d.best_M, [1, 3, 5, 8, 13, 21, 51, 1e9])
        for selname, sel in (("f_cal EV>=0", d.f_cal * d.best_M >= 1), ("blend EV>=0", d.b_M * d.best_M >= 1), ("f EV>=0", d.f * d.best_M >= 1),
                             ("all runners (control)", pd.Series(True, index=d.index))):
            g = d[sel]
            ctrl = d[~sel & d.band.isin(g.band.unique())]
            # odds-band matched control: reweight control to the selection's band mix
            wts = g.band.value_counts(normalize=True)
            cm = sum(wts.get(b, 0) * ctrl[ctrl.band == b].clv.mean() for b in wts.index if (ctrl.band == b).any())
            dd = g.groupby("date").clv.agg(["sum", "size"]); bs = day_boot(dd["sum"].to_numpy(), dd["size"].to_numpy())
            gl = g[np.isfinite(g.lclv)]; dl = gl.groupby("date").lclv.agg(["sum", "size"]); bl = day_boot(dl["sum"].to_numpy(), dl["size"].to_numpy())
            cl = ctrl[np.isfinite(ctrl.lclv)]
            lctrl = sum(wts.get(b, 0) * cl[cl.band == b].lclv.mean() for b in wts.index if (cl.band == b).any())
            clv_rows.append(dict(set=nm, selection=selname, n=len(g), lclv_mean=gl.lclv.mean(), lclv_lo=np.percentile(bl, 2.5), lclv_hi=np.percentile(bl, 97.5),
                                 lclv_matched_control=lctrl, share_shortened=(gl.lclv > 0).mean(), beat_close=(g.clv > 0).mean(), clv_mean=g.clv.mean(), clv_lo=np.percentile(bs, 2.5), clv_hi=np.percentile(bs, 97.5),
                                 clv_median=g.clv.median(), clv_comm2_mean=g.clv_c2.mean(), pclv_mean=g.pclv.mean(), bf_clv_median=g.bfclv.median(),
                                 matched_control_clv=cm, roi_at_best=float(np.where(g.pos == 1, g.best_M - 1, -1).mean()),
                                 roi_at_bsp_c2=float(np.where(g.pos == 1, (g.bsp - 1) * 0.98, -1).mean())))
            if selname == "f_cal EV>=0":
                for cut, vals in (("band", g.band.astype(str)), ("conf", pd.cut(g.f_cal, [0, .05, .1, .2, .35, 1]).astype(str)),
                                  ("dis", pd.cut(g.f - g.m_M, [-1, 0, .02, .05, .1, 1]).astype(str)), ("code", g.code), ("field", pd.cut(g.n, [0, 7, 11, 15, 99]).astype(str))):
                    for k, gg in g.groupby(vals):
                        clv_rows.append(dict(set=nm, selection=f"f_cal EV>=0 by {cut}", value=k, n=len(gg), lclv_mean=gg.lclv.mean(), share_shortened=(gg.lclv > 0).mean(), beat_close=(gg.clv > 0).mean(), clv_mean=gg.clv.mean(),
                                             clv_median=gg.clv.median(), pclv_mean=gg.pclv.mean()))
                for mth, gg in g.groupby("month"):
                    clv_rows.append(dict(set=nm, selection="f_cal EV>=0 by month", value=mth, n=len(gg), lclv_mean=gg.lclv.mean(), share_shortened=(gg.lclv > 0).mean(), beat_close=(gg.clv > 0).mean(), clv_mean=gg.clv.mean(),
                                         clv_median=gg.clv.median(), pclv_mean=gg.pclv.mean()))
    # selection time (S3 only): blend_t EV>=0 at best_t, CLV vs BSP
    for nm in ("dev", "reused"):
        d = sets[nm]
        for cp in ("M", "H", "T10", "L"):
            g = d[(d[f"b_{cp}"] * d[f"best_{cp}"] >= 1) & d.bsp.notna() & (d[f"best_{cp}"] > 1)]
            c = g[f"best_{cp}"] / g.bsp - 1
            lc = np.log(g.close.clip(EPS)) - np.log(g[f"m_{cp}"].clip(EPS))
            clv_rows.append(dict(set=nm, selection=f"blend EV>=0 decided at {cp}", n=len(g), lclv_mean=lc.mean(), share_shortened=(lc > 0).mean(), beat_close=(c > 0).mean(), clv_mean=c.mean(), clv_median=c.median(),
                                 pclv_mean=(g.close - g[f"m_{cp}"]).mean(), roi_at_best=float(np.where(g.pos == 1, g[f"best_{cp}"] - 1, -1).mean())))
    # live bot bets (category A)
    t = pd.read_csv(os.path.join(ROOT, "data", "card_review_tracker.csv"), low_memory=False)
    t = t[(t.day >= "2026-11-11") & (t.excluded.astype(str) != "True")]
    chk = t.check.astype(str) == "True"
    lb = t[(chk & (t.verdict == "BET")) | (~chk & (t.bet.astype(str) == "True"))].copy()
    lb["px"] = lb.mb.fillna(lb.best); lb["bsp"] = pd.to_numeric(lb.bsp, errors="coerce")
    lb = lb[lb.bsp > 1]
    lb["clv"] = lb.px / lb.bsp - 1
    lb["typ"] = np.where(lb.check.astype(str) == "True", "favourite check", "value flag")
    for k, g in [("all live bot bets", lb)] + list(lb.groupby("typ")):
        clv_rows.append(dict(set="A-live-bot", selection=k, n=len(g), beat_close=(g.clv > 0).mean(), clv_mean=g.clv.mean(), clv_median=g.clv.median(),
                             roi_at_best=float(np.where(g.won.astype(float) == 1, (g.px - 1) * 0.98, -1).mean()),
                             roi_at_bsp_c2=float(np.where(g.won.astype(float) == 1, (g.bsp - 1) * 0.98, -1).mean())))
    clvdf = pd.DataFrame(clv_rows); clvdf.to_csv(os.path.join(OUT, "clv.csv"), index=False)
    log("\n## CLV\n" + clvdf[~clvdf.selection.str.contains(" by ")].round(4).to_string())

    # ---------------- strategies
    cells = []
    # choose k (E) and u (F) on dev at T=4%, 2% commission, primary price
    def E_rule(k):
        return lambda x: (x.bf_H / x.bf_M - 1) <= k
    def F_rule(u):
        return lambda x: ((np.log(x.f.clip(EPS)) - np.log(x.m_M.clip(EPS))) >= 0) & ((np.log(x.f.clip(EPS)) - np.log(x.m_M.clip(EPS))) <= u)
    dev = sets["dev"]
    kbest = max((0.1, 0.2, 0.3), key=lambda k: strat_bets(dev, "b_H", "bf_H", 0.04, 0.02, extra=E_rule(k)).pl.mean())
    ubest = max((0.25, 0.5, 1.0), key=lambda u: strat_bets(dev, "b_M", "bf_M", 0.04, 0.02, extra=F_rule(u)).pl.mean())
    log(f"\nChosen on development: E drift cap k={kbest}, F disagreement cap u={ubest}")
    D_rule = lambda x: (x.b_M * (1 + (x.bf_M - 1) * 0.98) - 1 >= 0) & (x.m_H > x.m_M)  # noqa: E731
    strategies = [("A original @M", "f", "M", None), ("B calibrated @M", "f_cal", "M", None), ("C blend @M", "b_M", "M", None),
                  (f"F disagreement 0..{ubest} @M", "b_M", "M", F_rule(ubest)), ("D market confirmation @H", "b_H", "H", D_rule),
                  (f"E drift avoidance k={kbest} @H", "b_H", "H", E_rule(kbest)), ("Timing blend @H", "b_H", "H", None),
                  ("Timing blend @T10", "b_T10", "T10", None), ("Timing blend @L", "b_L", "L", None)]
    for nm in ("dev", "reused", "H3"):
        d = sets[nm]
        if nm == "H3":
            d = d[d.close.notna()]
        for sname, prob, cp, extra in strategies:
            if nm == "H3" and cp != "M":
                continue
            for pricekind in ("exchange", "bookmaker best"):
                col = f"bf_{cp}" if pricekind == "exchange" else f"best_{cp}"
                for c in (0.02, 0.05) if pricekind == "exchange" else (0.0,):
                    for T in (0.0, 0.04, 0.08):
                        x = strat_bets(d, prob, col, T, c, exchange=pricekind == "exchange", extra=extra)
                        st = bet_stats(x)
                        cells.append(dict(set=nm, strategy=sname, price=pricekind, comm=c, T=T, **st))
                        # execution sensitivity on the primary cell
                        if pricekind == "exchange" and c == 0.02 and T == 0.04 and cp == "M" and nm != "H3" and len(x):
                            adv = x[x.bf_H >= x.bf_M]
                            cells.append(dict(set=nm, strategy=sname + " | adverse fill (filled only if H quote >= M quote)", price=pricekind, comm=c, T=T, **bet_stats(adv)))
                            for fr in (0.5, 0.75):
                                sub = x[rng.random(len(x)) < fr]
                                cells.append(dict(set=nm, strategy=sname + f" | random fill {int(fr * 100)}%", price=pricekind, comm=c, T=T, **bet_stats(sub)))
    C = pd.DataFrame(cells); C.to_csv(os.path.join(OUT, "strategy_cells.csv"), index=False)
    log("\n## Strategy cells (2% exchange, T=4%)\n" + C[(C.comm.isin([0.02, 0.0])) & (C["T"] == 0.04)][["set", "strategy", "price", "bets", "roi", "lo", "hi", "clv_mean", "beat_close", "p_null"]].round(4).to_string())
    open(os.path.join(OUT, "p3_log.md"), "w").write("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
