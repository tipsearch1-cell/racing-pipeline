"""BTL / LTB study. Train 2020-23, choose strategy + threshold on 2024 only, test once on 2025-26.
Fill rule: our order at the target price counts as matched only if the in-running extreme traded THROUGH it by 2 ticks."""
import json, sys, numpy as np, pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
import features as F
SCR = "/tmp/claude-0/-home-claude/cd2f780b-543c-598d-8d36-a8da908aed77/scratchpad"
THROUGH = int(sys.argv[1]) if len(sys.argv) > 1 else 2
BMAX = float(sys.argv[2]) if len(sys.argv) > 2 else 1e9
FAV = len(sys.argv) > 3 and sys.argv[3] == "fav"   # train and bet on BSP favourites only   # liquidity cap on BSP (bets only; the model still trains on all runners)
d = pd.read_pickle(f"{SCR}/feat.pkl")
if FAV:
    d = d[d.fav_rank == 1].reset_index(drop=True)
B = d["Betfair SP"].values

def outcomes(kind, x):
    """class 0 = hit (traded out), 1 = miss & won, 2 = miss & lost; plus P/L per £1 stake (back stake for BTL, lay stake for LTB) by class."""
    if kind == "btl":
        L = F.tick_down(1 + (B - 1) * (1 - x), 0); hit = d["IP Min"].values <= F.tick_down(L, THROUGH)
        g = (B / L - 1, B - 1, -np.ones_like(B))
    else:
        K = F.tick_up(1 + (B - 1) * (1 + x), 0); hit = d["IP Max"].values >= F.tick_up(K, THROUGH)
        g = (1 - B / K, -(B - 1), np.ones_like(B))
    y = np.where(hit, 0, np.where(d.won.values == 1, 1, 2))
    return y, np.vstack(g).T          # gains (n,3), before commission

def pl(y, G, c):
    v = G[np.arange(len(y)), y]; return np.where(v > 0, v * (1 - c), v)

def ev(P, G, c):
    Gc = np.where(G > 0, G * (1 - c), G); return (P * Gc).sum(1)

STRATS = [("btl", .2), ("btl", .3), ("btl", .5), ("ltb", .3), ("ltb", .5), ("ltb", 1.0)] if FAV else [("btl", .3), ("btl", .5), ("ltb", .5), ("ltb", 1.0)]
tr = (d.year <= 2023).values; va = (d.year == 2024).values; te = (d.year >= 2025).values
X = d[F.FEATS].astype(float).values
res = {"through_ticks": THROUGH, "bsp_cap": BMAX, "favourites_only": FAV, "n": {"train": int(tr.sum()), "valid": int(va.sum()), "test": int(te.sum())}, "strategies": {}}
for kind, x in STRATS:
    name = f"{kind}{int(x*100)}"; y, G = outcomes(kind, x)
    m = HistGradientBoostingClassifier(max_iter=300, learning_rate=0.05, max_leaf_nodes=31, l2_regularization=1.0, random_state=0)
    m.fit(X[tr], y[tr]); P = np.zeros((len(y), 3)); P[:, m.classes_] = m.predict_proba(X)
    # fair-market baseline for hit (martingale touch prob) and model calibration on validation
    r = {"base_hit_rate": {s: round(float((y[msk] == 0).mean()), 4) for s, msk in (("train", tr), ("valid", va), ("test", te))},
         "pred_hit_valid": round(float(P[va, 0].mean()), 4)}
    liq0 = (B >= 1.5) & (B <= BMAX); r["base_hit_rate_capped"] = {s: round(float((y[msk & liq0] == 0).mean()), 4) for s, msk in (("valid", va), ("test", te))}
    for c in (0.02, 0.05):
        e = np.where((B >= 1.5) & (B <= BMAX), ev(P, G, c), -9); p_all = pl(y, G, c)
        liq = (B >= 1.5) & (B <= BMAX)
        r[f"all_c{int(c*100)}"] = {s: round(float(p_all[msk & liq].mean()), 4) for s, msk in (("valid", va), ("test", te))}
        best = None
        for tau in (0, .02, .05, .1, .15, .2, .3):
            sel = va & (e > tau)
            if sel.sum() < (100 if FAV else 200): continue
            tot = p_all[sel].sum()
            if best is None or tot > best[1]: best = (tau, tot, int(sel.sum()), float(p_all[sel].mean()))
        if best:
            tau = best[0]; st = te & (e > tau); pt = p_all[st]
            yrs = {int(yy): round(float(pl(y[st & (d.year.values == yy)], G[st & (d.year.values == yy)], c).mean()), 4) for yy in (2025, 2026) if (st & (d.year.values == yy)).sum()}
            boot = [pt[np.random.default_rng(i).integers(0, len(pt), len(pt))].mean() for i in range(500)] if len(pt) else [0]
            r[f"select_c{int(c*100)}"] = {"tau": tau, "valid_bets": best[2], "valid_roi": round(best[3], 4), "test_bets": int(st.sum()),
                                          "test_roi": round(float(pt.mean()), 4) if len(pt) else None, "test_hit": round(float((y[st] == 0).mean()), 4) if len(pt) else None,
                                          "test_roi_by_year": yrs, "test_roi_90ci": [round(float(np.percentile(boot, 5)), 4), round(float(np.percentile(boot, 95)), 4)],
                                          "test_avg_bsp": round(float(B[st].mean()), 2) if len(pt) else None}
        else:
            r[f"select_c{int(c*100)}"] = "no threshold with >=200 validation bets and positive selection"
    res["strategies"][name] = r
    print(name, json.dumps(r)[:900], flush=True)
json.dump(res, open(f"out_study_t{THROUGH}_cap{int(min(BMAX,9999))}{'_fav' if FAV else ''}.json", "w"), indent=1)
