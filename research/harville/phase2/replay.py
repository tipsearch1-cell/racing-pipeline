"""Phase 2 data: synthetic chronological replay of the rebuilt win model + pre-race runner features + genuine archive.

  python3 research/harville/phase2/replay.py   -> research/harville/phase2/work/{S.pkl, G.pkl, G0.pkl}

S  : for each month M in Mar..Oct 2026 the production win model (pipeline/models.py code, unchanged) is refitted on
     history races dated before the 1st of M and predicts every race in M. SYNTHETIC - never pooled with G.
G  : genuine archived rebuilt-model chances 10-18 Nov 2026 (store/DAY/model.json) + sealed reviewer chance.
G0 : recovered old-model chances 14 Oct - 9 Nov 2026 (provenance unverified; reported only).
"""
import glob, json, os, re, sys
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
sys.path.insert(0, os.path.join(ROOT, "research", "harville"))
import models as M  # noqa: E402  (production code, imported read-only)
from history import load as load_hist  # noqa: E402
from data import ckey, norm, posnum, bf_places  # noqa: E402
from common import load_json  # noqa: E402

W = os.path.join(HERE, "work")
MONTHS = ["2026-03", "2026-04", "2026-05", "2026-06", "2026-07", "2026-08", "2026-09", "2026-10"]


def going_group(g):
    g = str(g or "").lower()
    if "standard" in g or "slow" in g or "fast" in g and "firm" not in g:
        return "AW"
    if "heavy" in g:
        return "Heavy"
    if "soft" in g or "yield" in g:
        return "Soft"
    if "firm" in g:
        return "Firm"
    if "good" in g:
        return "Good"
    return "Other"


def cls_num(c):
    m = re.search(r"(\d)", str(c or ""))
    return float(m.group(1)) if m else np.nan


def runner_features(H):
    """Pre-race features for every history row from that horse's EARLIER rows only."""
    H = H.sort_values(["hkey", "date", "race_key"]).reset_index(drop=True)
    pn = H.pos.map(M.pos_num)
    n = pd.to_numeric(H.n, errors="coerce")
    H["ps"] = np.where(pn.notna() & (n > 1), 1 - (pn.fillna(1) - 1) / (n.clip(lower=2) - 1), np.where(pn.isna(), 0.0, np.nan))
    H["top3"] = ((pn <= 3) & pn.notna()).astype(float)
    sty = H.comment.map(M.early_class)
    H["sty"] = sty.map(M.STYLE_SCORE)
    H["led"] = (sty == "Leader").astype(float).where(sty.notna())
    H["ob"] = pd.to_numeric(H.ovr_btn, errors="coerce")
    H["gg"] = H.going.map(going_group)
    H["clsn"] = H.cls.map(cls_num)
    H["dist_f"] = pd.to_numeric(H.dist_f, errors="coerce")
    g = H.groupby("hkey", sort=False)
    sh = lambda c: g[c].shift(1)  # noqa: E731
    H["f_runs"] = g.cumcount()
    H["f_top3"] = g.top3.transform(lambda s: s.shift(1).expanding().mean())
    H["f_ps"] = g.ps.transform(lambda s: s.shift(1).expanding().mean())
    H["f_style"] = g.sty.transform(lambda s: s.shift(1).rolling(4, min_periods=1).mean())
    H["f_lead"] = g.led.transform(lambda s: s.shift(1).expanding().mean())
    H["f_ob"] = g.ob.transform(lambda s: s.shift(1).rolling(3, min_periods=1).median())
    H["f_clschg"] = H.clsn - sh("clsn")
    # distance and going suitability: per horse loop over earlier rows
    ds, gs = np.full(len(H), np.nan), np.full(len(H), np.nan)
    for _, idx in g.indices.items():
        d = H.dist_f.values[idx]; p = H.ps.values[idx]; gg = H.gg.values[idx]
        for j in range(1, len(idx)):
            pd_, pp, pg = d[:j], p[:j], gg[:j]
            ok = np.isfinite(pp)
            m1 = ok & np.isfinite(pd_) & (np.abs(pd_ - d[j]) <= 1)
            if m1.any():
                ds[idx[j]] = pp[m1].max()
            m2 = ok & (pg == gg[j])
            if m2.any():
                gs[idx[j]] = pp[m2].mean()
    H["f_dist"] = ds
    H["f_going"] = gs
    return H


def build_S():
    H = load_hist()
    H["is_target"] = False
    H = M.prior_features(H)
    H = M.race_relative(H)
    H["jumps"] = H.type.isin(["Hurdle", "Chase", "NH Flat"])
    H["y"] = (H.pos.map(M.pos_num) == 1).astype(float)
    wins = H.groupby("race_key").y.transform("sum")
    trainable = (H.n >= 4) & (wins == 1)
    H["month"] = H.date.astype(str).str[:7]
    H["p_model"] = np.nan
    coefs = {}
    for mth in MONTHS:
        tr = H[trainable & (H.date < f"{mth}-01")]
        te = H.month == mth
        for name, jm in (("jumps", True), ("flat", False)):
            a = tr[tr.jumps == jm]
            w = M.fit(a, a.y.values, a.race_key.values)
            coefs[f"{mth}-{name}"] = dict(zip(M.FEATS, map(float, w)))
            sel = te & (H.jumps == jm)
            if sel.any():
                H.loc[sel, "p_model"] = M.predict(H[sel], w).values
    json.dump(coefs, open(os.path.join(W, "replay_coefs.json"), "w"), indent=1)
    F = runner_features(H.copy())
    F = F[F.month.isin(MONTHS)]
    F["k"] = F.date.astype(str) + "|" + F.course.map(ckey) + "|" + F.hkey
    keep = ["k", "p_model", "f_runs", "f_top3", "f_ps", "f_style", "f_lead", "f_ob", "f_clschg", "f_dist", "f_going", "clsn", "dist_f"]
    F = F.drop_duplicates("k")[keep]
    O = pd.read_pickle(os.path.join(ROOT, "research", "harville", "work", "O.pkl"))
    O["k"] = O.date + "|" + O.course.map(ckey) + "|" + O.horse.map(norm)
    S = O.merge(F, on="k", how="left")
    S = S[S.date >= "2026-03-01"]
    # declared runners for place terms
    r = pd.concat([pd.read_csv(f, usecols=["race_id", "non_runners"]) for f in glob.glob(os.path.join(ROOT, "raw", "odds*", "results_*.csv.gz"))]).drop_duplicates("race_id")
    r["nnr"] = r.non_runners.fillna("").astype(str).map(lambda s: 0 if not s.strip().strip('"') else max(1, s.count("(")))
    S = S.merge(r[["race_id", "nnr"]], on="race_id", how="left")
    S["nnr"] = S.nnr.fillna(0)
    ok = S.groupby("race_id").p_model.transform(lambda s: s.notna().all()) & S.priced_all & S.p.notna()
    S["eligible"] = ok
    S["pm"] = S.p_model / S.groupby("race_id").p_model.transform("sum")
    S.to_pickle(os.path.join(W, "S.pkl"))
    e = S[S.eligible]
    print(f"S: {S.race_id.nunique():,} O races Mar-Oct 2026; eligible (model + market for every runner) {e.race_id.nunique():,} races, {len(e):,} runners")
    print(e.groupby(e.date.str[:7]).race_id.nunique().to_dict())
    return S


def build_G():
    t = pd.read_csv(os.path.join(ROOT, "data", "card_review_tracker.csv"), low_memory=False)
    t = t[(t.day >= "2026-11-10") & (t.day <= "2026-11-18")].copy()
    mp, feats = {}, {}
    for f in glob.glob(os.path.join(ROOT, "store", "2026-11-1*", "model.json")):
        day = f.split(os.sep)[-2]
        for rid, r in json.load(open(f))["races"].items():
            for hid, x in r["runners"].items():
                mp[(day, rid, hid)] = x.get("p")
    t["p_model"] = [mp.get((a, b, c)) for a, b, c in zip(t.day, t.race_id, t.horse_id)]
    res = {}
    for f in glob.glob(os.path.join(ROOT, "store", "2026-11-1*", "results_all.json.gz")):
        for r in load_json(f)["results"]:
            nr = str(r.get("non_runners") or "")
            res[r["race_id"]] = dict(nnr=0 if not nr.strip() else max(1, nr.count("(")), tote=json.dumps({k: r.get(k) for k in ("tote_ex", "tote_trifecta", "tote_csf", "tote_tricast")}))
    t["nnr"] = t.race_id.map(lambda r: res.get(r, {}).get("nnr", 0))
    t["date"] = t.day
    t["pos"] = t.pos.map(posnum)
    t["hcap"] = t.hcap.astype(str).isin(["True", "true", "1"])
    F = pd.read_pickle(os.path.join(ROOT, "research", "harville", "work", "F.pkl"))
    F = F[F.src == "rebuilt"][["race_id", "horse_id", "psp"]]
    t = t.merge(F, on=["race_id", "horse_id"], how="left")
    # runner features for G from the full history (rows before each day only)
    H = load_hist()
    H = H[H.date <= "2026-11-18"].copy()
    Hf = runner_features(H.copy())
    Hf["k"] = Hf.race_id.astype(str) + "|" + Hf.hkey
    t["k"] = t.race_id + "|" + t.horse.map(norm)
    t = t.merge(Hf.drop_duplicates("k")[["k", "f_runs", "f_top3", "f_ps", "f_style", "f_lead", "f_ob", "f_clschg", "f_dist", "f_going", "clsn", "dist_f"]], on="k", how="left")
    t["n"] = t.groupby("race_id").horse_id.transform("size")
    t.to_pickle(os.path.join(W, "G.pkl"))
    print(f"G: {t.race_id.nunique()} races, model p {t.p_model.notna().mean():.0%}, features matched {t.f_runs.notna().mean():.0%}, psp {t.psp.notna().mean():.0%}")
    return t


if __name__ == "__main__":
    os.makedirs(W, exist_ok=True)
    build_S()
    build_G()
