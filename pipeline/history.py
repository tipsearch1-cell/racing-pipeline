"""Run history used by the rebuilt models and the page.

python3 pipeline/history.py build <api results files...>
  -> data/history_runs.csv.gz : one row per runner per past race.
     Sources: RaceData exports in raw/racedata (1 Jan - 13 Oct 2026; speed figure = Dynamic speed rating, no form
     figure) and Racing API results (14 Oct onwards; fig = performance_rating, spd = speed_rating).
     Re-running merges new API files into the existing table (dedupe on date+course+horse key).
"""
import glob, json, os, re, sys
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import p  # noqa: E402

OUT = p("data", "history")  # one gzip per month: runs_YYYY-MM.csv.gz (only changed months get rewritten)
GZ = {"method": "gzip", "mtime": 0}  # deterministic bytes: an unchanged month is not a new git version


def read_all():
    fs = sorted(glob.glob(os.path.join(OUT, "runs_*.csv.gz")))
    return pd.concat([pd.read_csv(f, low_memory=False) for f in fs], ignore_index=True) if fs else None


def write_months(d):
    os.makedirs(OUT, exist_ok=True)
    changed = 0
    for m, g in d.groupby(d.date.astype(str).str[:7]):
        f = os.path.join(OUT, f"runs_{m}.csv.gz")
        tmp = f + ".tmp"
        g.to_csv(tmp, index=False, compression=GZ)
        if os.path.exists(f) and open(f, "rb").read() == open(tmp, "rb").read():
            os.remove(tmp)
        else:
            os.replace(tmp, f)
            changed += 1
    return changed


def norm(name):
    s = re.sub(r"\s*\([A-Z]{2,3}\)\s*$", "", str(name or "")).lower()
    return re.sub(r"[^a-z0-9]", "", s)


def course_key(c):
    return re.sub(r"[^a-z]", "", re.sub(r"\(.*?\)", "", str(c or "")).lower().replace("aw", ""))


def num(x):
    try:
        v = float(str(x).strip())
        return v
    except (TypeError, ValueError):
        return None


def dist_f(s):
    s = str(s or "")
    m = re.match(r"(?:(\d+)m)?\s*(?:(\d+)f)?\s*(?:(\d+)y)?", s.replace(" ", ""))
    if not m or not any(m.groups()):
        return None
    mi, fu, yd = (int(g) if g else 0 for g in m.groups())
    return round(mi * 8 + fu + yd / 220, 1)


def code_from_type(t):
    t = str(t or "").lower()
    if "hurdle" in t:
        return "Hurdle"
    if "chase" in t:
        return "Chase"
    if "nh flat" in t or "bumper" in t:
        return "NH Flat"
    return "Flat"


def from_racedata_daily():
    """RaceData results files pushed daily by the VPS (raw/racedata/daily/, restored from the raw-data branch)."""
    fs = sorted(glob.glob(p("raw", "racedata", "daily", "**", "*.csv"), recursive=True))
    return from_racedata(fs) if fs else None


def from_racedata(fs=None):
    fs = fs or sorted(glob.glob(p("raw", "racedata", "files", ".openclaw", "**", "*.csv"), recursive=True))
    keep = {"Date": "date", "Time": "time", "Course": "course", "Race type": "rtype", "Going": "going", "Class": "cls",
            "Distance (in miles, yards, furlongs)": "dist", "Runners": "n", "Horse": "horse", "Finish Position": "pos",
            "Weight (pounds)": "lbs", "OR Rating": "or", "SP": "sp", "Betfair SP": "bsp", "Dynamic speed rating": "spd",
            "In-Running Comments": "comment", "Trainer": "trainer", "Jockey": "jockey"}
    parts = []
    for f in fs:
        try:
            d = pd.read_csv(f, usecols=lambda c: c in keep, low_memory=False, encoding_errors="ignore")
        except Exception:
            continue
        if "Finish Position" not in d or "Horse" not in d:
            continue
        parts.append(d.rename(columns=keep))
    d = pd.concat(parts, ignore_index=True)
    d = d[d.pos.notna() & d.horse.notna()]
    d["date"] = d.date.astype(str).str[:10]
    d["key"] = d.date + "|" + d.course.map(course_key) + "|" + d.horse.map(norm)
    # the latest export of a date wins (results backfills replace pre-race copies)
    d = d.drop_duplicates("key", keep="last")
    out = pd.DataFrame({
        "date": d.date, "src": "rd", "race_key": d.date + "|" + d.course.astype(str) + "|" + d.time.astype(str).str[:5],
        "race_id": None, "course": d.course, "dist_f": d.dist.map(dist_f), "going": d.going, "type": d.rtype.map(code_from_type),
        "surface": d.rtype.astype(str).str.contains("AW").map({True: "AW", False: "Turf"}), "cls": d.cls, "race_name": None,
        "n": pd.to_numeric(d.n, errors="coerce"), "horse_id": None, "horse": d.horse, "hkey": d.horse.map(norm),
        "pos": d.pos.astype(str).str.strip(), "btn": None, "ovr_btn": None, "or": pd.to_numeric(d["or"], errors="coerce"),
        "lbs": pd.to_numeric(d.lbs, errors="coerce"), "sp": None, "bsp": pd.to_numeric(d.bsp, errors="coerce"),
        "fig": None, "spd": pd.to_numeric(d.spd, errors="coerce"), "comment": d.comment})
    return out


def from_api(files):
    rows = []
    for f in files:
        txt = open(f).read()
        try:
            j = json.loads(txt)
        except json.JSONDecodeError:
            j = json.loads(txt[txt.index("{"):])
        for r in j.get("results", []):
            n = sum(1 for h in r["runners"])
            surface = "AW" if ("(AW)" in str(r.get("course", "")) or str(r.get("going", "")).lower().startswith("standard")) else "Turf"
            for h in r["runners"]:
                rows.append({"date": r["date"], "src": "api", "race_key": r["race_id"], "race_id": r["race_id"], "course": r["course"],
                             "dist_f": num(str(r.get("dist_f", "")).rstrip("f")), "going": r.get("going"), "type": code_from_type(r.get("type")),
                             "surface": surface,
                             "cls": r.get("class"), "race_name": r.get("race_name"), "n": n, "horse_id": h.get("horse_id"),
                             "horse": re.sub(r"\s*\([A-Z]{2,3}\)\s*$", "", h.get("horse", "")), "hkey": norm(h.get("horse")),
                             "pos": str(h.get("position", "")).strip(), "btn": num(h.get("btn")), "ovr_btn": num(h.get("ovr_btn")),
                             "or": num(h.get("or")), "lbs": num(h.get("weight_lbs")), "sp": num(h.get("sp_dec")), "bsp": num(h.get("bsp")),
                             "fig": num(h.get("performance_rating")), "spd": num(h.get("speed_rating")), "comment": h.get("comment")})
    return pd.DataFrame(rows)


def build(files):
    api = from_api(files)
    old = read_all()
    if old is None:
        old = from_racedata()
    rd_new = from_racedata_daily()
    if rd_new is not None:
        old = pd.concat([old, rd_new], ignore_index=True)
    d = pd.concat([old, api], ignore_index=True)
    d["dkey"] = d.date.astype(str) + "|" + d.course.map(course_key) + "|" + d.hkey.astype(str)
    d = d.sort_values("src").drop_duplicates("dkey", keep="first").drop(columns="dkey")  # api beats rd on overlap
    d = d.sort_values(["date", "race_key", "hkey", "src"], kind="mergesort").reset_index(drop=True)
    ch = write_months(d)
    print(f"history ({ch} month file(s) changed): {len(d)} runs, {d.race_key.nunique()} races, {d.date.min()} to {d.date.max()}; "
          f"api runs {int((d.src == 'api').sum())}, racedata runs {int((d.src == 'rd').sum())}")


NR_RE = r"(?i)^(non.?runner|nr|withdrawn|w/?d|void|res.*)$"


def load():
    d = read_all()
    pos = d.pos.astype(str).str.strip()
    d = d[~pos.str.match(NR_RE) & ~pos.isin(["-", "", "nan", "Result Awaiting"])].copy()
    d["pos"] = d.pos.astype(str).str.strip().replace(LONG_POS)
    d["n"] = d.groupby("race_key").race_key.transform("size")  # runners that actually ran
    return d


LONG_POS = {"Pulled Up": "PU", "Fell": "F", "Unseated Rider": "UR", "Brought Down": "BD", "Refused To Race": "RR",
            "Slipped Up": "SU", "Ran Out": "RO", "Refused": "REF", "Carried Out": "CO", "Disqualified": "DSQ"}


if __name__ == "__main__":
    if sys.argv[1] == "build":
        build(sys.argv[2:])
