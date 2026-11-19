"""Harville research - data assembly and inventory (research only; never imported by production code).

  python3 research/harville/data.py        -> research/harville/work/{O,F,R}.pkl + research/harville/out/inventory.md

Tracks
  O  09:00 UK market archive (raw/odds_flat + raw/odds, checkpoint M), GB+IRE Flat and Jumps, 13 Oct 2025 - 12 Oct 2026.
     Win input = 09:00 market chance (same formula as production: 0.6 x mean-exchange implied + 0.4 x bookmaker-median
     implied, normalised over the runners that ran). Genuinely timestamped pre-race.
  F  Frankie genuine pre-race archive: sealed cards 26 Oct 2026 onwards (data/card_review_tracker.csv: rev = sealed
     reviewer chance, mkt = 09:00 market) plus store/DAY/model.json (rebuilt win model, from 10 Nov).
  R  RBD GB Flat results 2020-01-01 to 2026-10-09 (raw/rbd_results). Win BSP, place BSP, 'Placed in Betfair Market',
     Forecasted Odds. Closing BSP is an OUTCOME (research rule 2): track R is a diagnostic of the win->place mapping only.
Place prices: Betfair place SP from RBD (GB Flat) and RaceData (raw/racedata, GB+IRE, 2026), joined on date+course+horse.
Exotic prices: Tote exacta / trifecta / CSF / tricast from Racing API results (store/DAY/results_all.json.gz).
"""
import glob, json, os, re, sys
import numpy as np
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "pipeline"))
from common import load_json  # noqa: E402

W = os.path.join(ROOT, "research", "harville", "work")
OUT = os.path.join(ROOT, "research", "harville", "out")
EXCH = ["Betfair Exchange", "Matchbook", "Smarkets"]


def norm(name):
    s = re.sub(r"\s*\([A-Z]{2,3}\)\s*$", "", str(name or "")).lower()
    return re.sub(r"[^a-z0-9]", "", s)


def ckey(c):
    c = re.sub(r"\(.*?\)", "", str(c or "")).lower().replace("aw", "")
    return re.sub(r"[^a-z]", "", c)


def num(x):
    try:
        v = float(str(x).replace("£", "").replace("€", "").strip())
        return v if np.isfinite(v) else np.nan
    except (TypeError, ValueError):
        return np.nan


def posnum(x):
    s = str(x).strip()
    return int(s) if s.isdigit() else np.nan


def bf_places(n, hcap):
    """Betfair 'To Be Placed' standard terms (validated against RBD 'Placed in Betfair Market' in the inventory)."""
    if n < 5:
        return 0
    if n <= 7:
        return 2
    if n <= 15:
        return 3
    return 4 if hcap else 3


# ---------------------------------------------------------------- place-price table
def place_table():
    parts = []
    # RBD (GB Flat 2020 - 9 Oct 2026)
    for f in sorted(glob.glob(os.path.join(ROOT, "raw", "rbd_results", "20*", "*.csv"))):
        d = pd.read_csv(f, low_memory=False, encoding_errors="ignore",
                        usecols=["Date of Race", "Track", "Horse", "Betfair Place SP", "Placed in Betfair Market", "Betfair SP"])
        parts.append(pd.DataFrame({"date": d["Date of Race"].astype(str).str[:10], "ck": d.Track.map(ckey), "hk": d.Horse.map(norm),
                                   "psp": d["Betfair Place SP"].map(num), "wsp": d["Betfair SP"].map(num),
                                   "placed_bf": d["Placed in Betfair Market"].astype(str).str.strip().map({"YES": 1, "NO": 0}),
                                   "src": "rbd"}))
    # RaceData archive + daily pushes
    fs = sorted(glob.glob(os.path.join(ROOT, "raw", "racedata", "files", ".openclaw", "**", "*.csv"), recursive=True))
    fs += sorted(glob.glob(os.path.join(ROOT, "raw", "racedata", "daily", "**", "*.csv"), recursive=True))
    for f in fs:
        try:
            d = pd.read_csv(f, low_memory=False, encoding_errors="ignore",
                            usecols=lambda c: c in ("Date", "Course", "Horse", "Betfair Place SP", "Betfair SP", "Finish Position"))
        except Exception:
            continue
        if "Betfair Place SP" not in d or "Horse" not in d:
            continue
        parts.append(pd.DataFrame({"date": d.Date.astype(str).str[:10], "ck": d.Course.map(ckey), "hk": d.Horse.map(norm),
                                   "psp": d["Betfair Place SP"].map(num), "wsp": d["Betfair SP"].map(num), "placed_bf": np.nan,
                                   "src": "rd"}))
    t = pd.concat(parts, ignore_index=True)
    t = t[t.psp.notna() & (t.psp > 1)]
    t = t.sort_values("src").drop_duplicates(["date", "ck", "hk"], keep="last")  # rd (later exports) over rbd on overlap
    return t


# ---------------------------------------------------------------- track O
def market_chance(o):
    """Production formula: 0.6 x mean exchange implied + 0.4 x median implied (bookmaker median)."""
    ex = o[[c for c in EXCH if c in o]].apply(pd.to_numeric, errors="coerce")
    ex = ex.where(ex > 1)
    mean_ex = ex.mean(axis=1)
    med = pd.to_numeric(o["median"], errors="coerce")
    pe = np.where(mean_ex.notna(), 1 / mean_ex, 1 / med)
    return pd.Series(np.where(med.notna(), 0.6 * pe + 0.4 / med, np.nan), index=o.index)


def build_O(pt):
    rows = []
    for sub in ("odds_flat", "odds"):
        for f in sorted(glob.glob(os.path.join(ROOT, "raw", sub, "results_*.csv.gz"))):
            r = pd.read_csv(f, low_memory=False)
            o = pd.read_csv(f.replace("results_", "odds_"), low_memory=False)
            o = o[o.checkpoint == "M"]
            o = o.assign(raw=market_chance(o))[["race_id", "horse_id", "raw", "median", "first_price_at"]]
            d = r.merge(o, on=["race_id", "horse_id"], how="left")
            rows.append(d)
    d = pd.concat(rows, ignore_index=True).drop_duplicates(["race_id", "horse_id"])
    d["hcap"] = d.race_name.astype(str).str.contains("handicap|nursery", case=False)
    d["code"] = np.where(d.type.astype(str) == "Flat", "Flat", "Jumps")
    d["pos"] = d.position.map(posnum)
    d["n"] = d.groupby("race_id").horse_id.transform("size")
    d["date"] = d.date.astype(str).str[:10]
    d["ck"] = d.course.map(ckey)
    d["hk"] = d.horse.map(norm)
    d = d.merge(pt[["date", "ck", "hk", "psp", "wsp", "placed_bf"]], on=["date", "ck", "hk"], how="left")
    # races where every runner has a 09:00 price
    ok = d.groupby("race_id").raw.transform(lambda s: s.notna().all())
    d["priced_all"] = ok
    d["p"] = d.raw / d.groupby("race_id").raw.transform("sum")
    d["cls"] = d["class"].astype(str).str.extract(r"(\d)")[0].astype(float)
    return d[["date", "race_id", "course", "region", "off_dt", "code", "type", "hcap", "cls", "n", "horse_id", "horse", "pos",
              "p", "median", "priced_all", "bsp", "psp", "wsp", "placed_bf", "first_price_at"]]


# ---------------------------------------------------------------- track F
def build_F(pt):
    t = pd.read_csv(os.path.join(ROOT, "data", "card_review_tracker.csv"), low_memory=False)
    t = t[t.day >= "2026-10-26"].copy()
    mp = {}
    for f in glob.glob(os.path.join(ROOT, "store", "*", "model.json")):
        day = f.split(os.sep)[-2]
        j = json.load(open(f))
        for rid, r in j["races"].items():
            for hid, x in r["runners"].items():
                mp[(day, rid, hid)] = x.get("p")
    t["p_model"] = [mp.get((a, b, c)) for a, b, c in zip(t.day, t.race_id, t.horse_id)]
    tote = {}
    for f in glob.glob(os.path.join(ROOT, "store", "*", "results_all.json.gz")):
        for r in load_json(f)["results"]:
            tote[r["race_id"]] = {k: r.get(k) for k in ("tote_win", "tote_pl", "tote_ex", "tote_csf", "tote_tricast", "tote_trifecta")}
    t["date"] = t.day
    t["ck"] = t.course.map(ckey)
    t["hk"] = t.horse.map(norm)
    t = t.merge(pt[["date", "ck", "hk", "psp", "wsp"]], on=["date", "ck", "hk"], how="left")
    t["pos"] = t.pos.map(posnum)
    t["tote"] = t.race_id.map(lambda r: json.dumps(tote.get(r)) if r in tote else None)
    t["src"] = "rebuilt"
    # old pipeline: model chances as published on the recovered report page (12 Oct - 9 Nov 2026)
    old = json.load(open(os.path.join(ROOT, "report", "history_data.json")))
    rows = []
    for rep in old["reports"]:
        if rep["day"] >= "2026-11-10":
            continue
        for r in rep["races"]:
            for h in r["runners"]:
                rows.append(dict(day=rep["day"], date=rep["day"], race_id=r["race_id"], course=r["course"], hcap=r.get("hcap"),
                                 horse=h["horse"], p_model=h.get("p"), mkt=h.get("mkt"), runners=r.get("field")))
    o = pd.DataFrame(rows)
    sys.path.insert(0, os.path.join(ROOT, "pipeline"))
    from history import load as load_hist  # noqa: E402
    H = load_hist()
    H = H[H.src == "api"]
    pos = {(a, b): c for a, b, c in zip(H.race_id, H.hkey, H.pos)}
    typ = {a: b for a, b in zip(H.race_id, H.type)}
    o["hk"] = o.horse.map(norm)
    o["ck"] = o.course.map(ckey)
    o["pos"] = [posnum(pos.get((a, b))) if (a, b) in pos else np.nan for a, b in zip(o.race_id, o.hk)]
    o["code"] = o.race_id.map(lambda r: "Flat" if typ.get(r) == "Flat" else ("Jumps" if r in typ else None))
    o = o[o.race_id.isin(typ)]
    o = o.merge(pt[["date", "ck", "hk", "psp", "wsp"]], on=["date", "ck", "hk"], how="left")
    o["src"] = "old"
    o["mkt"] = 100 * o.mkt  # old page stored fractions
    return pd.concat([t, o], ignore_index=True)


# ---------------------------------------------------------------- track R
def build_R():
    fs = sorted(glob.glob(os.path.join(ROOT, "raw", "rbd_results", "20*", "*.csv")))
    d = pd.concat([pd.read_csv(f, low_memory=False, encoding_errors="ignore") for f in fs], ignore_index=True)
    d = pd.DataFrame({"date": d["Date of Race"].astype(str).str[:10], "course": d.Track, "time": d.Time.astype(str),
                      "type": d.Type, "cls": pd.to_numeric(d.Class, errors="coerce"), "dist": d.Distance, "going": d.Going,
                      "horse": d.Horse, "pos": d.Place.map(posnum), "runners": pd.to_numeric(d.Runners, errors="coerce"),
                      "bsp": d["Betfair SP"].map(num), "psp": d["Betfair Place SP"].map(num),
                      "placed_bf": d["Placed in Betfair Market"].astype(str).str.strip().map({"YES": 1, "NO": 0}),
                      "fc": d["Forecasted Odds"].map(num), "isp": d["Industry SP"].map(num)})
    d["race_id"] = d.date + "|" + d.course.astype(str) + "|" + d.time
    d = d.drop_duplicates(["race_id", "horse"])
    d["hcap"] = d.type.astype(str).str.contains("Handicap|Nursery", case=False)
    d["code"] = "Flat"
    d["n"] = d.groupby("race_id").horse.transform("size")
    return d


def inventory(O, F, R, pt):
    L = ["# Harville research - data inventory and provenance", "",
         f"Built {pd.Timestamp.now("UTC"):%Y-%m-%d %H:%M} UTC by research/harville/data.py. Counts only; no outcome comparisons.", ""]

    def block(name, d, rid="race_id"):
        g = d.groupby(rid)
        L.append(f"## {name}")
        L.append(f"- races {d[rid].nunique():,}; runners {len(d):,}; dates {d.date.min()} to {d.date.max()} ({d.date.nunique()} days)")
        if "code" in d:
            L.append(f"- by code: {d.groupby('code')[rid].nunique().to_dict()}")
        if "region" in d:
            L.append(f"- by region: {d.groupby('region')[rid].nunique().to_dict()}")
        for c in ("p", "rev", "mkt", "p_model", "psp", "bsp", "wsp", "fc", "placed_bf"):
            if c in d:
                L.append(f"- {c} present: {d[c].notna().mean():.1%} of runners")
        L.append(f"- runners with a numeric finishing position: {d.pos.notna().mean():.1%}")
        top3 = g.pos.apply(lambda s: sorted(s.dropna().tolist())[:3] == [1, 2, 3])
        L.append(f"- races with a clean 1-2-3 (no dead heat in the first three, 3+ finishers): {top3.mean():.1%}")
        L.append("")

    block("Track O - 09:00 market archive (genuine pre-race timestamps)", O)
    L.append(f"- races with a 09:00 price for every runner: {O.groupby('race_id').priced_all.first().mean():.1%}")
    L.append("- non-runners: odds rows without a result row are dropped and the 09:00 chances renormalised over runners")
    L.append("")
    block("Track F - Frankie sealed cards (genuine pre-race, 26 Oct 2026 onwards)", F.rename(columns={"day": "date"}) if "date" not in F else F)
    nt = F.drop_duplicates("race_id").tote.notna().sum()
    L.append(f"- races with Tote dividends (exacta/trifecta/CSF/tricast): {nt}")
    L.append("")
    block("Track R - RBD GB Flat 2020-2026 (closing prices: diagnostic only)", R)
    # validate Betfair place-terms rule
    g = R[R.placed_bf.notna()].groupby("race_id").agg(n=("horse", "size"), runners=("runners", "first"), hcap=("hcap", "first"),
                                                      yes=("placed_bf", "sum"), fin=("pos", lambda s: s.notna().sum()))
    g["rule"] = [bf_places(n, h) for n, h in zip(g.n, g.hcap)]
    ok = (g.yes == np.minimum(g.rule, g.fin))
    L.append(f"- Betfair place-terms rule (5-7: 2, 8-15: 3, 16+ hcap: 4 else 3; by runners that ran) matches RBD 'Placed in Betfair Market' count in {ok.mean():.1%} of {len(g):,} races "
             f"(mismatches mostly declared-runner vs ran differences or dead heats)")
    L.append("")
    L.append("## Place-price table")
    L.append(f"- Betfair place SP rows {len(pt):,}: {pt.groupby('src').size().to_dict()}; dates {pt.date.min()} to {pt.date.max()}")
    L.append("")
    L.append("## Not available")
    L.append("- Historical bookmaker place / each-way prices with terms: none archived (09:00 win prices only, no EW terms, no Rule 4) -> each-way NOT TESTABLE as an executable price.")
    L.append("- Exchange forecast / exacta prices: none. Tote exacta/trifecta and bookmaker CSF/tricast dividends only in Racing API results saved since 10 Nov 2026 (track F).")
    L.append("- Frankie win probabilities before 26 Oct 2026: none archived; the rebuilt model was trained on Jan-25 Oct 2026 so a replay over that period is in-sample -> Frankie evidence is the genuine forward window only.")
    L.append("- Existing Frankie place probabilities (comparator E): none - Frankie has never produced place probabilities.")
    open(os.path.join(OUT, "inventory.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    os.makedirs(W, exist_ok=True)
    os.makedirs(OUT, exist_ok=True)
    pt = place_table()
    O = build_O(pt)
    F = build_F(pt)
    R = build_R()
    for k, v in (("O", O), ("F", F), ("R", R)):
        v.to_pickle(os.path.join(W, f"{k}.pkl"))
    inventory(O, F, R, pt)
