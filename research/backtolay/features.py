"""Pre-race features + in-running outcome targets for back-to-lay (BTL) / lay-to-back (LTB) research.
Every history feature uses PRIOR DAYS only. Targets use IP Min / IP Max (in-running traded extremes)."""
import numpy as np, pandas as pd

# Betfair price ladder
_LAD = np.concatenate([np.arange(1.01, 2, .01), np.arange(2, 3, .02), np.arange(3, 4, .05), np.arange(4, 6, .1), np.arange(6, 10, .2),
                       np.arange(10, 20, .5), np.arange(20, 30, 1), np.arange(30, 50, 2), np.arange(50, 100, 5), np.arange(100, 1000.01, 10)]).round(2)
def tick_down(p, n):  # n ticks below the highest ladder price <= p
    i = np.searchsorted(_LAD, np.asarray(p) + 1e-9, side="right") - 1
    return _LAD[np.clip(i - n, 0, len(_LAD) - 1)]
def tick_up(p, n):    # n ticks above the lowest ladder price >= p
    i = np.searchsorted(_LAD, np.asarray(p) - 1e-9, side="left")
    return _LAD[np.clip(i + n, 0, len(_LAD) - 1)]

def targets(d, drop, rise, through=2):
    B = d["Betfair SP"].values
    L = 1 + (B - 1) * (1 - drop)                    # lay price for BTL
    K = 1 + (B - 1) * (1 + rise)                    # back price for LTB
    d[f"btl{int(drop*100)}"] = (d["IP Min"].values <= tick_down(L, through)).astype(int)
    d[f"ltb{int(rise*100)}"] = (d["IP Max"].values >= tick_up(K, through)).astype(int)
    return L, K

def _prior_rate(d, key, col, name, min_n=1):
    """Rate of `col` for `key` over prior days only (expanding), plus count."""
    g = d.groupby([key, "date"])[col].agg(["sum", "count"]).reset_index().sort_values([key, "date"])
    g["cs"] = g.groupby(key)["sum"].cumsum() - g["sum"]; g["cn"] = g.groupby(key)["count"].cumsum() - g["count"]
    g[name] = np.where(g.cn >= min_n, g.cs / g.cn.replace(0, np.nan), np.nan); g[name + "_n"] = g.cn
    return d.merge(g[[key, "date", name, name + "_n"]], on=[key, "date"], how="left")

def _dist_y(s):
    import re
    s = str(s); m = re.findall(r"(\d+)\s*([mfy])", s)
    return sum(int(v) * {"m": 1760, "f": 220, "y": 1}[u] for v, u in m) or np.nan
def _wt_lb(s):
    import re
    m = re.match(r"\s*(\d+)\s*-\s*(\d+)", str(s))
    return int(m.group(1)) * 14 + int(m.group(2)) if m else pd.to_numeric(s, errors="coerce")

def build(d):
    d = d.copy()
    d["lb"] = np.log(d["Betfair SP"]); d["imp"] = 1 / d["Betfair SP"]
    d["race_overround"] = d.groupby("race").imp.transform("sum"); d["imp_n"] = d.imp / d.race_overround
    d["fav_rank"] = d.groupby("race")["Betfair SP"].rank(method="min")
    d["pre_rng"] = np.log(d["Pre Max"] / d["Pre Min"]); d["pre_vs_bsp_min"] = np.log(d["Betfair SP"] / d["Pre Min"])
    d["pre_vs_bsp_max"] = np.log(d["Pre Max"] / d["Betfair SP"]); d["fc_vs_bsp"] = np.log(d["Forecasted Odds"] / d["Betfair SP"])
    d["isp_vs_bsp"] = np.log(d["Industry SP"] / d["Betfair SP"])
    d["red"] = pd.to_numeric(d["% BSP reduction"], errors="coerce")
    # in-running behaviour history (prior days only): halve rate, drift rate, mean reduction
    d["_h50"] = (d["IP Min"] <= 1 + (d["Betfair SP"] - 1) * 0.5).astype(float)
    d["_d100"] = (d["IP Max"] >= 1 + (d["Betfair SP"] - 1) * 2).astype(float)
    d["_lead"] = d["_h50"] * (1 - d.won)            # traded at half price but lost: "travels well, doesn't finish"
    for key, pre in (("Horse", "h"), ("Trainer", "t"), ("Jockey", "j"), ("Track", "c")):
        for col, nm in (("_h50", "h50"), ("_d100", "d100"), ("_lead", "lead"), ("red", "red")):
            d = _prior_rate(d, key, col, f"{pre}_{nm}")
    d["dist_y"] = d["Distance_raw"].map(_dist_y) if "Distance_raw" in d else np.nan
    d["wt_lb"] = d["Weight_raw"].map(_wt_lb) if "Weight_raw" in d else np.nan; d["going"] = d.Going.astype("category").cat.codes; d["type"] = d.Type.astype("category").cat.codes
    d["track"] = d.Track.astype("category").cat.codes
    d["year"] = d.date.dt.year
    return d

FEATS = ["lb", "imp_n", "race_overround", "fav_rank", "Runners", "pre_rng", "pre_vs_bsp_min", "pre_vs_bsp_max", "fc_vs_bsp", "isp_vs_bsp",
         "dist_y", "wt_lb", "going", "type", "track", "Class", "Stall", "Official Rating", "Age", "Pace", "Runs last 18 months", "Wins Last 5 races",
         "Avg % SP Drop Last 5 races", "Avg % SP Drop last 18 mths", "RBD Rating", "RBD Rank", "Total Prev Races", "Days Since Last time out",
         "Last time out Position"] + [f"{p}_{n}{s}" for p in "htjc" for n in ("h50", "d100", "lead", "red") for s in ("", "_n")]
