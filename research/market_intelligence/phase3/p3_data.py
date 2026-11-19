"""Phase 3 data: runner tables with model chances and every archived market checkpoint.

  python3 research/market_intelligence/phase3/p3_data.py  -> work/{S3.pkl, H3.pkl, A3.pkl}

S3 (category B): Phase 2 replay (Mar - 12 Oct 2026) + checkpoints E/M/H/T10/L + BSP.
H3 (category B): replay extended to 26 Oct - 18 Nov 2026 + 09:00 snapshot from the timestamped sealed cards + BSP.
A3 (category A): live model chances 10-18 Nov + sealed reviewer chance + bot bets (tracker).
No checkpoint is ever filled in from BSP or interpolated.
"""
import glob, json, os, sys
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
import models as M  # noqa: E402 (production code, read-only)
from history import load as load_hist  # noqa: E402
from common import load_json  # noqa: E402

W = os.path.join(HERE, "work")
EXCH = ["Betfair Exchange", "Matchbook", "Smarkets"]
CPS = ["E", "M", "H", "T10", "L"]


def mkt_raw(ex_mean, med):
    pe = np.where(np.isfinite(ex_mean), 1 / ex_mean, 1 / med)
    return np.where(np.isfinite(med), 0.6 * pe + 0.4 / med, np.nan)


def norm_by(df, col, key="race_id"):
    s = df.groupby(key)[col].transform("sum")
    ok = df.groupby(key)[col].transform(lambda x: x.notna().all())
    return (df[col] / s).where(ok)


_PT = None


def fill_bsp(T):
    """Fill missing API BSP with the Betfair SP from RaceData result files (same race, same horse)."""
    global _PT
    sys.path.insert(0, os.path.join(ROOT, "research", "harville"))
    from data import place_table, ckey, norm
    if _PT is None:
        _PT = place_table()[["date", "ck", "hk", "wsp"]]
    T = T.assign(ck=T.course.map(ckey), hk=T.horse.map(norm)).merge(_PT, on=["date", "ck", "hk"], how="left")
    T["bsp"] = pd.to_numeric(T.bsp, errors="coerce").where(lambda x: x > 1).fillna(pd.to_numeric(T.wsp, errors="coerce").where(lambda x: x > 1)).astype(float)
    return T.drop(columns=["ck", "hk", "wsp"])


def build_S3():
    S = pd.read_pickle(os.path.join(ROOT, "research", "harville", "phase2", "work", "S.pkl"))
    S = S[S.eligible].copy()
    keep = ["date", "race_id", "course", "region", "off_dt", "code", "hcap", "cls", "n", "nnr", "horse_id", "horse", "pos", "bsp", "pm"]
    S = S[keep].rename(columns={"pm": "f"})
    parts = []
    for sub in ("odds_flat", "odds"):
        for f in sorted(glob.glob(os.path.join(ROOT, "raw", sub, "odds_*.csv.gz"))):
            o = pd.read_csv(f, usecols=lambda c: c in ["race_id", "horse_id", "checkpoint", "median", "best"] + EXCH, low_memory=False)
            parts.append(o[o.race_id.isin(set(S.race_id))])
    O = pd.concat(parts).drop_duplicates(["race_id", "horse_id", "checkpoint"])
    for c in EXCH + ["median", "best"]:
        O[c] = pd.to_numeric(O[c], errors="coerce").where(lambda x: x > 1)
    O["ex_mean"] = O[EXCH].mean(axis=1)
    O["raw"] = mkt_raw(O.ex_mean.to_numpy(), O["median"].to_numpy())
    for cp in CPS:
        x = O[O.checkpoint == cp][["race_id", "horse_id", "raw", "median", "best", "Betfair Exchange"]]
        x.columns = ["race_id", "horse_id", f"raw_{cp}", f"med_{cp}", f"best_{cp}", f"bf_{cp}"]
        S = S.merge(x, on=["race_id", "horse_id"], how="left")
        S[f"m_{cp}"] = norm_by(S, f"raw_{cp}")
    S["bsp"] = pd.to_numeric(S.bsp, errors="coerce").where(lambda x: x > 1)
    S["close"] = norm_by(S.assign(ib=1 / S.bsp), "ib")
    S["month"] = S.date.str[:7]
    S["cat"] = "B-replay"
    S.to_pickle(os.path.join(W, "S3.pkl"))
    print(f"S3: {S.race_id.nunique():,} races, {len(S):,} runners; checkpoint coverage " +
          ", ".join(f"{cp} {S[f'm_{cp}'].notna().mean():.1%}" for cp in CPS) + f"; BSP {S.close.notna().mean():.1%}")


def build_H3():
    H = load_hist()
    H["is_target"] = False
    H = M.prior_features(H)
    H = M.race_relative(H)
    H["jumps"] = H.type.isin(["Hurdle", "Chase", "NH Flat"])
    H["y"] = (H.pos.map(M.pos_num) == 1).astype(float)
    wins = H.groupby("race_key").y.transform("sum")
    trainable = (H.n >= 4) & (wins == 1)
    H["f"] = np.nan
    for mth, start, end in (("2026-10", "2026-10-26", "2026-10-31"), ("2026-11", "2026-11-01", "2026-11-18")):
        tr = H[trainable & (H.date < f"{mth}-01")]
        sel_all = (H.date >= start) & (H.date <= end) & (H.src == "api")
        for name, jm in (("jumps", True), ("flat", False)):
            a = tr[tr.jumps == jm]
            w = M.fit(a, a.y.values, a.race_key.values)
            sel = sel_all & (H.jumps == jm)
            if sel.any():
                H.loc[sel, "f"] = M.predict(H[sel], w).values
    T = H[H.f.notna()][["date", "race_id", "course", "type", "n", "horse_id", "horse", "pos", "bsp", "f", "cls"]].copy()
    T["hn"] = T.groupby("race_id").horse_id.transform("size")
    rows = []
    for day in sorted(T.date.unique()):
        fp = os.path.join(ROOT, "store", day, "sealed_card.json.gz")
        if not os.path.exists(fp):
            continue
        card = load_json(fp)
        cards = card["racecards"] if isinstance(card, dict) else card
        for r in cards:
            hc = "handicap" in str(r.get("race_name", "")).lower() or "nursery" in str(r.get("race_name", "")).lower()
            for h in r["runners"]:
                px = {o["bookmaker"]: pd.to_numeric(o.get("decimal"), errors="coerce") for o in h.get("odds", []) or []}
                px = {k: v for k, v in px.items() if pd.notna(v) and v > 1}
                books = [v for k, v in px.items() if k not in EXCH]
                med = float(np.median(books)) if books else np.nan
                exs = [px[k] for k in EXCH if k in px]
                best = max([v for v in books if v <= 1 + 1.3 * (med - 1)], default=np.nan) if books else np.nan
                rows.append(dict(race_id=r["race_id"], horse_id=h["horse_id"], hcap=hc, raw_M=float(mkt_raw(np.array([np.mean(exs) if exs else np.nan]), np.array([med]))[0]),
                                 med_M=med, best_M=best, bf_M=px.get("Betfair Exchange", np.nan), mb_M=px.get("Matchbook", np.nan)))
    C = pd.DataFrame(rows)
    T = T.merge(C, on=["race_id", "horse_id"], how="inner")
    T = T[T.groupby("race_id").horse_id.transform("size") == T.hn]   # every runner matched to the 09:00 card
    T = fill_bsp(T)
    T["code"] = np.where(T.type == "Flat", "Flat", "Jumps")
    T["pos"] = pd.to_numeric(T.pos, errors="coerce")
    T["bsp"] = pd.to_numeric(T.bsp, errors="coerce").where(lambda x: x > 1)
    T["n"] = T.groupby("race_id").horse_id.transform("size")
    T["f"] = T.f / T.groupby("race_id").f.transform("sum")
    T["m_M"] = norm_by(T, "raw_M")
    T["close"] = norm_by(T.assign(ib=1 / T.bsp), "ib")
    T["month"] = T.date.str[:7]
    T["cat"] = "B-replay-H3"
    T.to_pickle(os.path.join(W, "H3.pkl"))
    print(f"H3: {T.race_id.nunique():,} races, {len(T):,} runners, {T.date.min()}..{T.date.max()}; m_M {T.m_M.notna().mean():.1%}, BSP {T.close.notna().mean():.1%}, positions {T.pos.notna().mean():.1%}")


def build_A3():
    G = pd.read_pickle(os.path.join(ROOT, "research", "harville", "phase2", "work", "G.pkl"))
    G = G[["date", "race_id", "course", "code", "hcap", "runners", "horse_id", "horse", "pos", "bsp", "mkt", "rev", "p_model", "mb", "best", "median", "check", "verdict", "bet", "excluded"]].copy()
    G["code"] = np.where(G.code == "Flat", "Flat", "Jumps")
    G["f"] = G.p_model / G.groupby("race_id").p_model.transform("sum")
    G["m_M"] = G.mkt / G.groupby("race_id").mkt.transform("sum")
    G["bsp"] = pd.to_numeric(G.bsp, errors="coerce").where(lambda x: x > 1)
    G = fill_bsp(G)
    G["close"] = norm_by(G.assign(ib=1 / G.bsp), "ib")
    G["n"] = G.groupby("race_id").horse_id.transform("size")
    G["month"] = G.date.str[:7]
    G["cat"] = "A-verified"
    G.to_pickle(os.path.join(W, "A3.pkl"))
    print(f"A3: {G.race_id.nunique()} races, {len(G)} runners; BSP {G.close.notna().mean():.0%}")


if __name__ == "__main__":
    os.makedirs(W, exist_ok=True)
    build_S3(); build_H3(); build_A3()
