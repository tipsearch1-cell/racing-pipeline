"""Phase 5 exploratory analyses on HISTORICAL, previously examined data (Phase 4 walk-forward predictions, S3 replay
Mar-Oct 2026 and H3). Nothing here touches the confirmatory forward test. Pre-specified in the Phase 5 spec section 9.
python3 explore.py -> out/early_market.csv, out/clv.csv, out/execution.csv, out/explore.json"""
import json, os
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__))
P = pd.read_pickle(os.path.join(HERE, "..", "..", "model_reconstruction", "phase4", "work", "preds.pkl"))
EPS, COMM, EV_MIN = 1e-9, 0.02, 0.04
RNG = np.random.default_rng(20261120)
P["period"] = np.select([P.month.between("2026-05", "2026-08"), P.month.isin(["2026-09", "2026-10"]), P.month.str.startswith("H3")],
                        ["dev May-Aug", "re-used Sep-Oct", "re-used H3"], "train-only Mar-Apr")
P["bsp"] = pd.to_numeric(P.bsp, errors="coerce")


def day_ci(df, col, by="date", draws=2000):
    g = df.groupby(by)[col].agg(["sum", "size"])
    s, m = g["sum"].to_numpy(), g["size"].to_numpy(); k = len(s)
    if k < 2:
        return np.nan, np.nan
    bs = [s[j].sum() / m[j].sum() for j in (RNG.integers(k, size=k) for _ in range(draws))]
    return tuple(np.percentile(bs, [2.5, 97.5]).round(4))


def band(o):
    return pd.cut(o, [1, 3, 6, 11, 21, 1000], labels=["<3", "3-6", "6-11", "11-21", "21+"])


out = {}
# ---------------- A. coverage / availability of the evening market
S = P[P.period != "re-used H3"]
cov = S.groupby("race_id").agg(e=("m_E", lambda s: s.notna().all()), bfe=("bf_E", lambda s: s.notna().all()))
r = S.assign(ratio=S.bsp / S.bf_E)
out["evening_coverage"] = dict(races=int(len(cov)), share_races_complete_E=round(float(cov.e.mean()), 3),
                               share_races_betfair_quote_all_runners_E=round(float(cov.bfe.mean()), 3),
                               median_bsp_over_betfair_quote_E=round(float(r.ratio.median()), 3),
                               median_bsp_over_betfair_quote_M=round(float((S.bsp / S.bf_M).median()), 3),
                               median_bsp_over_betfair_quote_T10=round(float((S.bsp / S.bf_T10).median()), 3))

# ---------------- B. does independent information predict overnight movement (21:00 -> 09:00)?
E = S[S.m_E.notna() & S.m_M.notna() & S.pA.notna()].copy()
E = E[E.groupby("race_id").m_E.transform(lambda s: s.notna().all()) & E.groupby("race_id").m_M.transform(lambda s: s.notna().all())]
E["move"] = np.log(E.m_M.clip(EPS)) - np.log(E.m_E.clip(EPS))
E["sigA"] = np.log(E.pA.clip(EPS)) - np.log(E.m_E.clip(EPS))     # independent improved model (A) vs evening market
E["sigF"] = np.log(E.f.clip(EPS)) - np.log(E.m_E.clip(EPS))      # production model vs evening market
rows = []
for per, g in E.groupby("period"):
    for sig in ("sigA", "sigF"):
        x = g[sig] - g.groupby("race_id")[sig].transform("mean"); y = g.move - g.groupby("race_id").move.transform("mean")
        b = (x * y).sum() / (x * x).sum()
        # day-clustered SE of the slope
        u = (x * (y - b * x)).groupby(g.date).sum()
        se = np.sqrt((u ** 2).sum()) / (x * x).sum()
        rows.append(dict(period=per, signal=sig, runners=len(g), races=g.race_id.nunique(), corr=round(float(np.corrcoef(x, y)[0, 1]), 4),
                         slope=round(float(b), 4), slope_se_day=round(float(se), 4)))
mv = pd.DataFrame(rows); out["overnight_movement"] = mv.to_dict("records")

# ---------------- C. CLV of model selections by decision checkpoint (pre-specified rule: EV >= 4% at the Betfair quote, 2% commission)
def selections(df, p, quote):
    q = df[quote]
    ev = df[p] * (1 + (q - 1) * (1 - COMM)) - 1
    return df.assign(q=q, ev=ev)[ev >= EV_MIN].copy()


def clv_block(df, p, quote, label):
    base = df[df[p].notna() & df[quote].notna() & df.bsp.notna() & (df[quote] > 1)].copy()
    base["clv_abs"] = np.log(base[quote] / base.bsp)                      # > 0: price taken was bigger than BSP
    base["ob"] = band(base[quote])
    ctl = base.groupby(["period", "ob"], observed=True).clv_abs.mean().rename("ctl")
    sel = selections(base, p, quote).join(ctl, on=["period", "ob"])
    sel["clv_rel"] = sel.clv_abs - sel.ctl
    res = []
    for per, g in sel.groupby("period"):
        lo, hi = day_ci(g, "clv_abs")
        rlo, rhi = day_ci(g, "clv_rel")
        y = (g.y == 1).astype(float)
        ret_q = (y * (g.q - 1) * (1 - COMM) - (1 - y))                         # level stake 1, filled at the quote
        ret_b = (y * (g.bsp - 1) * (1 - COMM) - (1 - y))                       # taken at BSP instead
        fill_adv = g.bsp >= g.q                                                # adverse: matched only when the market drifted
        ret_adv = ret_q[fill_adv]
        res.append(dict(checkpoint=label, period=per, selections=len(g), mean_quote=round(float(g.q.mean()), 1), median_quote=round(float(g.q.median()), 1),
                        clv_abs_mean=round(float(g.clv_abs.mean()), 4), clv_abs_ci=[lo, hi], share_beat_bsp=round(float((g.clv_abs > 0).mean()), 3),
                        clv_rel_mean=round(float(g.clv_rel.mean()), 4), clv_rel_ci=[rlo, rhi], winners=int(y.sum()),
                        roi_fill_at_quote=round(float(ret_q.mean()), 3), roi_at_bsp=round(float(ret_b.mean()), 3),
                        adverse_fill_rate=round(float(fill_adv.mean()), 3), roi_adverse_fills=round(float(ret_adv.mean()), 3) if len(ret_adv) else None,
                        roi_haircut_5pct=round(float((y * ((g.q * 0.95) - 1).clip(lower=0) * (1 - COMM) - (1 - y)).mean()), 3)))
    return res


clv = []
clv += clv_block(S, "pD1_E", "bf_E", "21:00 market-anchored (D1 at E, walk-forward)")
clv += clv_block(P, "pE", "bf_M", "09:00 hybrid E (walk-forward)")
clv += clv_block(S, "pD1_H", "bf_H", "off-60 market-anchored (D1 at H)")
clv += clv_block(S, "pD1_T10", "bf_T10", "off-10 market-anchored (D1 at T10)")
clv += clv_block(S.assign(pAx=S.pA), "pAx", "bf_E", "21:00 independent model A (no market)")
C = pd.DataFrame(clv); out["clv_and_execution"] = C.to_dict("records")

# ---------------- D. where is the evening advantage? log-loss gain vs the evening market by odds band / code (re-used data)
L = S[S.y == 1 & S.m_E.notna()]
w = S[(S.y == 1) & S.pD1_E.notna() & S.m_E.notna()].copy()
w["gain"] = np.log(w.pD1_E.clip(EPS)) - np.log(w.m_E.clip(EPS)); w["ob"] = band(1 / w.m_E)
seg = w.groupby(["period", "code"]).gain.agg(["mean", "size"]).round(4).reset_index()
seg2 = w.groupby(["period", "ob"], observed=True).gain.agg(["mean", "size"]).round(4).reset_index()
out["evening_gain_by_code"] = seg.to_dict("records"); out["evening_gain_by_band"] = seg2.astype({"ob": str}).to_dict("records")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
mv.to_csv(os.path.join(HERE, "out", "early_market_movement.csv"), index=False)
C.to_csv(os.path.join(HERE, "out", "clv_execution.csv"), index=False)
json.dump(out, open(os.path.join(HERE, "out", "explore.json"), "w"), indent=1, default=str)
pd.set_option("display.width", 250); pd.set_option("display.max_columns", 30)
print(json.dumps(out["evening_coverage"], indent=1)); print(mv)
print(C.drop(columns=["clv_abs_ci", "clv_rel_ci"])); print(C[["checkpoint", "period", "clv_abs_ci", "clv_rel_ci"]])
print(seg); print(seg2)
