"""Phase 3 charts.  python3 research/market_intelligence/phase3/charts3.py (after p3.py)"""
import json, os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p3  # noqa: E402

OUT = os.path.join(HERE, "out")
E = 1e-6
S = p3.eligible(pd.read_pickle(os.path.join(HERE, "work", "S3.pkl")), ["m_M", "f"])
H3 = pd.read_pickle(os.path.join(HERE, "work", "H3.pkl")); H3 = H3[H3.close.notna()]

# 1. disagreement vs movement: raw vs within 09:00-odds band
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.3), dpi=130)
rows = []
for lab, d, c in (("Development May-Aug (replay)", S[S.date.str[:7].isin(p3.DEV)], "#2f6db3"), ("Sep-Oct, re-used (replay)", S[S.date >= "2026-09-01"], "#c0632b"),
                  ("H3 26 Oct-18 Nov (replay, untouched)", H3, "#2a9d4b")):
    dis = np.log(d.f.clip(E)) - np.log(d.m_M.clip(E)); mv = np.log(d.close.clip(E)) - np.log(d.m_M.clip(E))
    x = pd.DataFrame({"d": dis, "m": mv, "b": pd.qcut(d.m_M.rank(method="first"), 20, labels=False)}).replace([np.inf, -np.inf], np.nan).dropna()
    q = pd.qcut(x.d, 10, labels=False)
    raw = x.groupby(q).agg(d=("d", "mean"), m=("m", "mean"))
    x["dr"] = x.d - x.groupby("b").d.transform("mean"); x["mr"] = x.m - x.groupby("b").m.transform("mean")
    q2 = pd.qcut(x.dr, 10, labels=False)
    wb = x.groupby(q2).agg(d=("dr", "mean"), m=("mr", "mean"))
    axs[0].plot(raw.d, raw.m, "o-", color=c, label=lab, ms=4)
    axs[1].plot(wb.d, wb.m, "o-", color=c, label=lab, ms=4)
    rows.append(dict(set=lab, raw_corr=np.corrcoef(x.d, x.m)[0, 1], within_band_corr=np.corrcoef(x.dr, x.mr)[0, 1], within_band_slope=np.polyfit(x.dr, x.mr, 1)[0], n=len(x)))
axs[0].set_title("Raw: looks like the market moves away (corr -0.17 to -0.34)", fontsize=9.5)
axs[1].set_title("Same 09:00 odds band: market moves towards us (corr +0.05 to +0.14)", fontsize=9.5)
for a in axs:
    a.axhline(0, color="#444", lw=0.8, ls=":"); a.grid(alpha=0.25)
    a.set_xlabel("log(model / 09:00 market) - decile means"); a.set_ylabel("log(BSP-implied / 09:00 market)")
axs[0].legend(fontsize=7, frameon=False)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "disagreement_vs_movement.png")); plt.close(fig)
pd.DataFrame(rows).to_csv(os.path.join(OUT, "disagreement_movement_within_band.csv"), index=False)

# 2. win calibration by 09:00 odds band (re-used + H3 pooled)
s = pd.read_csv(os.path.join(OUT, "win_segments.csv"))
x = s[(s.cut == "oddsband") & s.set.isin(["reused", "H3"])]
g = x.assign(**{k + "w": x[k] * x.n for k in ("f", "m_M", "b_M", "close")}).groupby("value").sum(numeric_only=True)
order = ["<2.5", "2.5-5", "5-10", "10-20", "20-50", "50+"]
g = g.loc[order]
fig, ax = plt.subplots(figsize=(8, 4.2), dpi=130)
xx = np.arange(len(g))
for k, lab, c, mk in (("wins", "Actual win rate", "#111", "o"), ("fw", "Our model", "#c0632b", "v"), ("m_Mw", "09:00 market", "#7a7a7a", "^"), ("b_Mw", "Blend (market + 10% model)", "#2f6db3", "D"), ("closew", "BSP", "#2a9d4b", "s")):
    ax.plot(xx, g[k] / g.n, marker=mk, color=c, label=lab, lw=2.4 if k == "wins" else 1.4, ms=5)
ax.set_yscale("log"); ax.set_xticks(xx, order); ax.set_xlabel("09:00 market odds band"); ax.set_ylabel("Win probability (log)")
ax.set_title("Our model is too flat: favourites under-rated, outsiders over-rated", fontsize=10.5)
ax.legend(fontsize=8, frameon=False); ax.grid(alpha=0.25, which="both")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "win_calibration_by_odds.png")); plt.close(fig)

# 3. blend weight on our model by decision time
prm = json.load(open(os.path.join(OUT, "params.json")))
fig, ax = plt.subplots(figsize=(6.5, 3.6), dpi=130)
for mth in ["2026-07", "2026-08", "2026-09", "2026-10", "final"]:
    ws = [prm[mth][f"w_{cp}"][1] for cp in p3.CPS]
    ax.plot(range(4), ws, "o-", label=mth, lw=2.2 if mth == "final" else 1, color="#111" if mth == "final" else None)
ax.set_xticks(range(4), ["09:00", "off-60m", "off-10m", "off-1s"]); ax.axhline(0, color="#444", lw=0.8, ls=":")
ax.set_ylabel("Weight on our model in the blend"); ax.set_title("The market absorbs our model's information by the off", fontsize=10)
ax.legend(fontsize=7, frameon=False, title="fit window", title_fontsize=7); ax.grid(alpha=0.25)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "model_weight_by_time.png")); plt.close(fig)
print(pd.DataFrame(rows).round(3).to_string())
