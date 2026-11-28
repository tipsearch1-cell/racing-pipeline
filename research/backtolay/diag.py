"""Diagnostics: observed vs fair-market touch rates by BSP band; model lift over a BSP-only model (AUC, test 2025-26)."""
import json, numpy as np, pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score
import features as F
d = pd.read_pickle("/tmp/claude-0/-home-claude/cd2f780b-543c-598d-8d36-a8da908aed77/scratchpad/feat.pkl")
B = d["Betfair SP"].values; out = {}
L = F.tick_down(1 + (B - 1) * .5, 0); K = F.tick_up(1 + (B - 1) * 2, 0)
d["h"] = (d["IP Min"].values <= F.tick_down(L, 2)).astype(int); d["fair_h"] = np.minimum(1, L / B)  # P(touch L) for a fair martingale = (1/B)/(1/L)
d["k"] = (d["IP Max"].values >= F.tick_up(K, 2)).astype(int); d["fair_k"] = (1 - 1 / B) / (1 - 1 / K)
d["band"] = pd.cut(d["Betfair SP"], [1.01, 2, 3, 5, 8, 13, 21, 51, 1001])
t = d.groupby("band", observed=True).agg(n=("h", "size"), btl50_obs=("h", "mean"), btl50_fair=("fair_h", "mean"), ltb100_obs=("k", "mean"), ltb100_fair=("fair_k", "mean")).round(3)
print(t); out["by_band"] = t.reset_index().astype({"band": str}).to_dict("records")
out["by_year_btl50"] = d.groupby("year").agg(obs=("h", "mean"), fair=("fair_h", "mean")).round(3).reset_index().to_dict("records")
tr = (d.year <= 2023).values; te = (d.year >= 2025).values & (B <= 20)
for tgt in ("h", "k"):
    y = d[tgt].values; aucs = {}
    for nm, cols in (("bsp_only", ["lb"]), ("full", F.FEATS)):
        m = HistGradientBoostingClassifier(max_iter=300, learning_rate=.05, random_state=0).fit(d.loc[tr, cols].astype(float), y[tr])
        aucs[nm] = round(roc_auc_score(y[te], m.predict_proba(d.loc[te, cols].astype(float))[:, 1]), 4)
        if nm == "full":
            from sklearn.inspection import permutation_importance
    out[f"auc_{tgt}"] = aucs; print(tgt, aucs)
json.dump(out, open("out_diag.json", "w"), indent=1, default=str)
