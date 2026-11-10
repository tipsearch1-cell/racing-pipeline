"""RaceIQ finishing speed -> data/raceiq_runs.csv.gz.  python3 pipeline/raceiq.py build
Reads every normalized runner CSV under raw/raceiq (all export formats). One row per runner: date, race, horse key,
finishing_speed_percentage and its difference from that race's average (fsp_rel, percentage points)."""
import glob, os, sys
import pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import p  # noqa: E402
from history import norm  # noqa: E402

OUT = p("data", "raceiq_runs.csv.gz")


def build():
    fs = sorted(set(glob.glob(p("raw", "raceiq", "**", "raceiq_2026_normalized.csv"), recursive=True)
                    + glob.glob(p("raw", "raceiq", "**", "RaceIQ_runner_data.csv"), recursive=True)))
    parts = []
    for f in fs:
        try:
            d = pd.read_csv(f, usecols=lambda c: c in ("date", "race_id", "track", "horse_name", "finish_position",
                                                         "finishing_speed_percentage", "time_index_score"), low_memory=False)
        except Exception:
            continue
        parts.append(d)
    d = pd.concat(parts, ignore_index=True)
    d["hkey"] = d.horse_name.map(norm)
    d = d.drop_duplicates(["date", "race_id", "hkey"], keep="last")
    d["fsp"] = pd.to_numeric(d.finishing_speed_percentage, errors="coerce")
    d["fsp_rel"] = d.fsp - d.groupby(["date", "race_id"]).fsp.transform("mean")
    d = d[["date", "race_id", "track", "hkey", "finish_position", "fsp", "fsp_rel", "time_index_score"]]
    d.to_csv(OUT, index=False, compression="gzip")
    print(f"raceiq: {len(d)} runners, {d.date.min()} to {d.date.max()}, finishing speed for {d.fsp.notna().mean():.0%}")


def load():
    return pd.read_csv(OUT) if os.path.exists(OUT) else pd.DataFrame(columns=["date", "hkey", "fsp", "fsp_rel"])


if __name__ == "__main__":
    build()
