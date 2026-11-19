"""Phase 2 charts.  python3 research/harville/phase2/charts2.py"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
W, OUT = os.path.join(HERE, "work"), os.path.join(HERE, "out")
U = pd.read_csv(os.path.join(W, "S_runners.csv.gz"))
U = U[U.month.isin(["2026-05", "2026-06", "2026-07", "2026-08", "2026-09", "2026-10"]) & (U.places > 0) & (U.psp > 1)].copy()
U["placed"] = (U.frac > 0).astype(float)

# 1. place probability by place-SP band: place SP vs market Harville vs our model vs actual
U["b"] = pd.cut(U.psp, [1, 1.5, 2, 3, 5, 10, 20, 50, 1e9], labels=["1-1.5", "1.5-2", "2-3", "3-5", "5-10", "10-20", "20-50", "50+"])
t = U.groupby("b", observed=True).agg(act=("placed", "mean"), psp=("imp_psp", "mean"), A=("Pk_A", "mean"), B=("Pk_B", "mean"), D=("Pk_D", "mean"), n=("placed", "size"))
fig, ax = plt.subplots(figsize=(8.5, 4.6), dpi=130)
x = np.arange(len(t))
for col, lab, c, mk in (("act", "Actual place rate", "#111", "o"), ("psp", "Place SP implied", "#2a9d4b", "s"), ("A", "Market + discounted Harville", "#7a7a7a", "^"),
                        ("B", "Our model + discounted Harville", "#c0632b", "v"), ("D", "Enhanced ranking", "#2f6db3", "D")):
    ax.plot(x, t[col], marker=mk, color=c, label=lab, lw=1.5 if col != "act" else 2.4, ms=5)
ax.set_xticks(x, t.index.astype(str)); ax.set_yscale("log")
ax.set_xlabel("Betfair place SP band"); ax.set_ylabel("Place probability (log scale)")
ax.set_title("Place SP is calibrated; 09:00-based models over-rate the drifters", fontsize=11)
ax.legend(fontsize=8, frameon=False); ax.grid(alpha=0.25, which="both")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "calibration_by_psp_band.png")); plt.close(fig)
t.to_csv(os.path.join(OUT, "calibration_by_psp_band.csv"))

# 2. disagreement bands (holdout): actual vs model vs market Harville vs place SP
d = pd.read_csv(os.path.join(OUT, "disagreement.csv"))
d = d[(d.period == "hold") & (d.against == "harville") & d.get("model", pd.Series(index=d.index, dtype=object)).isna()]
fig, ax = plt.subplots(figsize=(8.5, 4.4), dpi=130)
x = np.arange(len(d))
ax.plot(x, d.P_model, "v-", color="#c0632b", label="Our model + discounted Harville")
ax.plot(x, d.P_mkt_harville, "^-", color="#7a7a7a", label="Market + discounted Harville")
ax.plot(x, d.P_psp, "s-", color="#2a9d4b", label="Place SP implied")
ax.plot(x, d.actual, "o-", color="#111", lw=2.4, label="Actual place rate")
ax.set_xticks(x, d.band); ax.set_xlabel("Disagreement: our place probability minus market's (percentage points)")
ax.set_ylabel("Place probability"); ax.set_title("Holdout Sep-Oct 2026: outcomes follow the market, not our model", fontsize=11)
ax.legend(fontsize=8, frameon=False); ax.grid(alpha=0.25)
fig.tight_layout(); fig.savefig(os.path.join(OUT, "disagreement_holdout.png")); plt.close(fig)
print("charts written")
