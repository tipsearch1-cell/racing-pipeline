"""Calibration charts for the Harville research.  python3 research/harville/charts.py  (after run.py)"""
import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
COL = {"A": "#7a7a7a", "B": "#2f6db3", "C": "#c0632b"}
NAME = {"A": "Harville", "B": "Discounted Harville", "C": "Learned ranking"}

for split in ("S1", "S2"):
    c = pd.read_csv(os.path.join(OUT, f"calibration_{split}.csv"))
    fig, axs = plt.subplots(1, 2, figsize=(10, 4.6), dpi=130)
    for ax, what, title in zip(axs, ("P2nd", "P3rd"), ("Probability of finishing 2nd", "Probability of finishing 3rd")):
        mx = 0
        for _, r in c[c.what == what].iterrows():
            t = pd.DataFrame(json.loads(r.table))
            ax.plot(t.pred, t.obs, "o-", color=COL[r.model], ms=4, lw=1.4, label=f"{NAME[r.model]} (slope {r.slope:.2f})")
            mx = max(mx, t.pred.max(), t.obs.max())
        ax.plot([0, mx], [0, mx], ls=":", color="#444", lw=1)
        ax.set_title(title, fontsize=10)
        ax.set_xlabel("Predicted (decile mean)")
        ax.set_ylabel("Observed frequency")
        ax.legend(fontsize=7, frameon=False)
        ax.grid(alpha=0.25)
    fig.suptitle(f"Calibration, {split} test period (09:00 market input, GB+IRE)", fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, f"calibration_{split}.png"))
    plt.close(fig)

# expected vs actual by rank, both splits pooled
rows = []
for split in ("S1", "S2"):
    U = pd.read_csv(os.path.join(HERE, "work", f"O_{split}_runners.csv.gz"))
    for m, g in U.groupby("model"):
        g = g[g["rank"] <= 8]
        rows.append(g.groupby("rank").agg(e2=("P2nd", "sum"), e3=("P3rd", "sum"), a2=("pos", lambda s: (s == 2).sum()), a3=("pos", lambda s: (s == 3).sum())).assign(model=m, split=split).reset_index())
d = pd.concat(rows).groupby(["model", "rank"]).sum(numeric_only=True).reset_index()
fig, axs = plt.subplots(1, 2, figsize=(10, 4.2), dpi=130)
for ax, (e, a, t) in zip(axs, (("e2", "a2", "2nd place"), ("e3", "a3", "3rd place"))):
    for m in ("A", "B", "C"):
        x = d[d.model == m]
        ax.plot(x["rank"], 100 * (x[a] / x[e] - 1), "o-", color=COL[m], label=NAME[m], ms=4)
    ax.axhline(0, color="#444", lw=1, ls=":")
    ax.set_title(f"Actual vs expected {t}, by 09:00 market rank", fontsize=10)
    ax.set_xlabel("Market rank (1 = favourite)")
    ax.set_ylabel("Actual / expected - 1 (%)")
    ax.legend(fontsize=7, frameon=False); ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "actual_vs_expected_by_rank.png"))
d.to_csv(os.path.join(OUT, "actual_vs_expected_by_rank.csv"), index=False)
print("charts written")
