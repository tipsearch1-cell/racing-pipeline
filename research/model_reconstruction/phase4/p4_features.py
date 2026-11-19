"""Phase 4 feature table. Every feature uses strictly EARLIER races only.
  python3 research/model_reconstruction/phase4/p4_features.py -> work/feat.pkl, work/groups.json
"""
import glob, json, os, sys, time
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
sys.path.insert(0, os.path.join(ROOT, "research", "harville"))
sys.path.insert(0, os.path.join(ROOT, "research", "harville", "phase2"))
import models as M  # noqa: E402 (production, read-only)
from history import load as load_hist  # noqa: E402
from data import ckey, norm  # noqa: E402
from replay import runner_features  # noqa: E402

W = os.path.join(HERE, "work")
JFAM = ("Hurdle", "Chase", "NH Flat")


def connections():
    fs = sorted(glob.glob(os.path.join(ROOT, "raw", "racedata", "files", ".openclaw", "**", "*.csv"), recursive=True))
    fs += sorted(glob.glob(os.path.join(ROOT, "raw", "racedata", "daily", "**", "*.csv"), recursive=True))
    parts = []
    for f in fs:
        try:
            d = pd.read_csv(f, usecols=lambda c: c in ("Date", "Course", "Horse", "Trainer", "Jockey"), encoding_errors="ignore", low_memory=False)
        except Exception:
            continue
        if not {"Date", "Course", "Horse", "Trainer"} <= set(d.columns):
            continue
        parts.append(d)
    d = pd.concat(parts, ignore_index=True)
    d["k"] = d.Date.astype(str).str[:10] + "|" + d.Course.map(ckey) + "|" + d.Horse.map(norm)
    return d.drop_duplicates("k", keep="last").set_index("k")[["Trainer", "Jockey"]]


def rolling_rate(df, who, days):
    """Prior win rate of `who` over the previous `days` days (strictly earlier dates), with counts."""
    d = df[[who, "dt", "won"]].dropna(subset=[who])
    daily = d.groupby([who, "dt"]).agg(r=("won", "size"), w=("won", "sum")).reset_index().sort_values([who, "dt"])
    out_r, out_w = {}, {}
    for name, g in daily.groupby(who, sort=False):
        t = g.dt.values.astype("datetime64[D]").astype(np.int64)
        cr = np.r_[0, np.cumsum(g.r.values)]; cw = np.r_[0, np.cumsum(g.w.values)]
        lo = np.searchsorted(t, t - days, side="left")       # first day inside window
        hi = np.arange(len(t))                               # exclude same day
        for i, tt in enumerate(t):
            out_r[(name, tt)] = cr[hi[i]] - cr[lo[i]]
            out_w[(name, tt)] = cw[hi[i]] - cw[lo[i]]
    key = list(zip(df[who], df.dt.values.astype("datetime64[D]").astype(np.int64)))
    r = np.array([out_r.get(k, np.nan) for k in key], float); w = np.array([out_w.get(k, np.nan) for k in key], float)
    return r, w


def build(extra=None, upto=None):
    """extra: optional target rows (today's card) appended to history; upto: use history strictly before this date."""
    t0 = time.time()
    H = load_hist()
    if upto:
        H = H[H.date < upto]
    H["is_target"] = False
    if extra is not None:
        H = pd.concat([H, extra.assign(is_target=True)], ignore_index=True)
    H = M.prior_features(H)              # production per-horse prior features
    H = M.race_relative(H)               # production G0 relative features
    H["y"] = (H.pos.map(M.pos_num) == 1).astype(float)
    H["jumps"] = H.type.isin(JFAM)
    H["dt"] = pd.to_datetime(H.date)
    F = runner_features(H.copy())        # phase 2 suitability / consistency / style (earlier rows only)
    for c in ("f_top3", "f_ps", "f_style", "f_lead", "f_dist", "f_going", "f_clschg", "clsn"):
        H[c] = F.set_index(["hkey", "date", "race_key"])[c].reindex(pd.MultiIndex.from_frame(H[["hkey", "date", "race_key"]])).values
    # G1 speed: earlier SAME-CODE runs only
    H = H.sort_values(["hkey", "date", "race_key"]).reset_index(drop=True)
    H["spd"] = pd.to_numeric(H.spd, errors="coerce")
    g = H.groupby(["hkey", "jumps"], sort=False).spd
    H["spd_last"] = g.shift(1)
    H["spd_best3"] = g.transform(lambda s: s.shift(1).rolling(3, min_periods=1).max())
    H["spd_mean3"] = g.transform(lambda s: s.shift(1).rolling(3, min_periods=1).mean())
    # G2 class change vs mean of last 3
    H["cls_prev3"] = H.groupby("hkey").clsn.transform(lambda s: s.shift(1).rolling(3, min_periods=1).mean())
    H["cls_chg3"] = H.clsn - H.cls_prev3
    # G3 course experience
    H["ck"] = H.course.map(ckey)
    gc = H.groupby(["hkey", "ck"], sort=False)
    H["course_runs"] = gc.cumcount()
    H["course_wins"] = gc.y.transform(lambda s: s.shift(1).fillna(0).cumsum())
    # G4 connections
    con = connections()
    k = H.date.astype(str) + "|" + H.ck + "|" + H.hkey
    tj = H[["trainer", "jockey"]].copy() if "trainer" in H else None
    H["trainer"] = con.Trainer.reindex(k).values; H["jockey"] = con.Jockey.reindex(k).values
    if tj is not None:   # target rows carry their own connections from the card
        H["trainer"] = H.trainer.where(H.trainer.notna(), tj.trainer.values); H["jockey"] = H.jockey.where(H.jockey.notna(), tj.jockey.values)
    H["won"] = H.y
    for who in ("trainer", "jockey"):
        for days in (30, 365):
            r, w = rolling_rate(H, who, days)
            prior = 0.10
            H[f"{who}_sr{days}"] = (w + prior * 10) / (r + 10)      # shrunk towards 10%
            H[f"{who}_n{days}"] = np.log1p(np.nan_to_num(r))
    # G5 career runs
    H["career"] = np.log1p(H.runs_before)
    # G6 pace: race-level likely leaders
    H["likely_leader"] = (H.f_lead.fillna(0) >= 0.3).astype(float)
    # G7 field
    gr = H.groupby("race_key")
    H["n_field"] = H.n
    H["or_field_mean"] = gr["or"].transform("mean")
    H["or_gap12"] = gr["or"].transform(lambda s: (s.nlargest(2).iloc[0] - s.nlargest(2).iloc[-1]) if s.notna().sum() >= 2 else np.nan)
    H["leaders_in_race"] = gr.likely_leader.transform("sum")
    # relative forms
    cont = ["spd_last", "spd_best3", "spd_mean3", "or", "cls_chg3", "f_dist", "f_going", "f_top3", "f_ps", "f_style", "f_lead",
            "trainer_sr30", "trainer_sr365", "jockey_sr30", "jockey_sr365", "course_runs", "course_wins", "career", "mkt_prev", "pos_prev"]
    gr = H.groupby("race_key")
    for c in cont:
        x = H[c].astype(float)
        mean = gr[c].transform("mean"); mx = gr[c].transform("max")
        H[f"{c}_rm"] = (x - mean).fillna(0)
        H[f"{c}_rx"] = (x - mx).fillna(0)
        H[f"{c}_rk"] = gr[c].rank(pct=True, ascending=False).fillna(0.5)
        H[f"{c}_na"] = x.isna().astype(float)
        H[f"{c}_abs"] = x.fillna(x.median())
    # scale a few
    for c in [c for c in H.columns if c.startswith(("spd_", "or_")) and c.endswith(("_rm", "_rx", "_abs")) and c not in ("or_field_mean", "or_gap12")]:
        H[c] = H[c] / 10.0
    groups = {
        "G0": M.FEATS,
        "G1": [f"spd_{a}_{b}" for a in ("last", "best3", "mean3") for b in ("rm", "rx", "rk", "na")],
        "G2": ["or_rx", "or_rk", "cls_chg3_rm", "cls_chg3_na"],
        "G3": [f"{c}_{b}" for c in ("f_dist", "f_going", "course_runs", "course_wins") for b in ("rm", "rx", "na")],
        "G4": [f"{w}_sr{d}_{b}" for w in ("trainer", "jockey") for d in (30, 365) for b in ("rm", "rx")],
        "G5": ["f_top3_rm", "f_top3_na", "f_ps_rm", "career_rm", "career_rx"],
        "G6": ["f_style_rm", "f_style_na", "f_lead_rm", "leaders_in_race"],
        "G7": ["n_field", "or_field_mean", "or_gap12"],
    }
    absolute = {
        "G1": [f"spd_{a}_abs" for a in ("last", "best3", "mean3")] + [f"spd_{a}_na" for a in ("last", "best3", "mean3")],
        "G2": ["or_abs", "cls_chg3_abs"], "G3": ["f_dist_abs", "f_going_abs", "course_runs_abs", "course_wins_abs"],
        "G4": [f"{w}_sr{d}_abs" for w in ("trainer", "jockey") for d in (30, 365)], "G5": ["f_top3_abs", "f_ps_abs", "career_abs"],
        "G6": ["f_style_abs", "f_lead_abs", "leaders_in_race"], "G7": ["n_field", "or_field_mean", "or_gap12"],
    }
    for c in ("or_field_mean", "or_gap12"):
        H[c] = (H[c].fillna(H[c].median()) - H[c].median()) / 10.0
    H["n_field"] = np.log(H.n_field.clip(lower=2))
    keep = ["date", "race_key", "race_id", "course", "type", "jumps", "n", "horse", "hkey", "horse_id", "pos", "y", "bsp", "src", "trainer", "jockey"] + \
        sorted(set(sum(groups.values(), []) + sum(absolute.values(), [])))
    H = H[keep + (["is_target"] if extra is not None else [])].copy()
    assert H.filter(like="_na").isin([0, 1]).all().all()
    if extra is not None:
        return H[H.is_target], groups
    H.to_pickle(os.path.join(W, "feat.pkl"))
    json.dump({"relative": groups, "absolute": absolute}, open(os.path.join(W, "groups.json"), "w"), indent=1)
    cov = {c: float(H[c.replace("_rm", "_na")].eq(0).mean()) if c.endswith("_rm") and c.replace("_rm", "_na") in H else None for c in sum(groups.values(), [])}
    tj = {"trainer": float(H.trainer.notna().mean()), "jockey": float(H.jockey.notna().mean()), "spd_last": float(1 - H.spd_last_na.mean())}
    json.dump({"coverage": tj, "rows": len(H), "races": int(H.race_key.nunique())}, open(os.path.join(W, "coverage.json"), "w"))
    print(f"features: {len(H):,} rows, {H.race_key.nunique():,} races, {time.time() - t0:.0f}s; coverage {tj}")


if __name__ == "__main__":
    os.makedirs(W, exist_ok=True)
    build()
