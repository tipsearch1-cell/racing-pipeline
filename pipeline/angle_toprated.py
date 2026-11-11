"""PAPER angle: card's own top-rated runner at a longer price (registered prereg/ANGLE_CARD_TOPRATED_2026-11-10.md).

  python3 pipeline/angle_toprated.py pick DAY     -> store/DAY/angle_toprated_DAY.csv (run right after save_card, before any off)
  python3 pipeline/angle_toprated.py settle DAY   -> fills results for DAY into data/angle_toprated_tracker.csv, prints running totals
Nothing here is ever sent to the bot.
"""
import os, re, sys
import numpy as np
import pandas as pd
from common import p, load_card, race_market, load_json

TOP = re.compile(r"(?i)one to beat|top-rated|top rated|tops (?:the|our)|our top|top of the")
RANK = re.compile(r"(?i)(?:ranks?|ranked|puts? (?:him|her)|has (?:him|her))[^.]*?\b(top|first|1st)\b[^.]*?\bof\b")
TRACKER = p("data", "angle_toprated_tracker.csv")
MIN_PRICE = 8.0


def pick(day):
    rows = []
    for r in load_card(day):
        mk = race_market(r)
        for h in r["runners"]:
            t = h.get("spotlight") or h.get("comment") or ""
            m = mk[h["horse_id"]]
            if not (TOP.search(t) or RANK.search(t)):
                continue
            rows.append(dict(day=day, race_id=r["race_id"], off_dt=r["off_dt"], course=r["course"], horse_id=h["horse_id"],
                             horse=h["horse"], mb=m["mb"], best=m["best_ex"], mkt=m["mkt"],
                             selected=bool(m["mb"] and m["mb"] >= MIN_PRICE), pos=None, won=None, bsp=None))
    d = pd.DataFrame(rows)
    d.to_csv(p("store", day, f"angle_toprated_{day}.csv"), index=False)
    s = d[d.selected] if len(d) else d
    print(f"top-rated angle {day}: {len(d)} card top-rated runners, {len(s)} selected at Matchbook >= {MIN_PRICE} (paper)")
    for x in s.itertuples():
        print(f"  {pd.Timestamp(x.off_dt).tz_convert('Europe/London'):%H:%M} {x.course} {x.horse} Matchbook {x.mb}")


def settle(day):
    d = pd.read_csv(p("store", day, f"angle_toprated_{day}.csv")).astype({"pos": object, "won": object, "bsp": object})
    res = load_json(p("store", day, "results_all.json.gz"))["results"]
    info = {(race["race_id"], hh["horse_id"]): hh for race in res for hh in race["runners"]}
    for i, x in d.iterrows():
        hh = info.get((x.race_id, x.horse_id))
        if hh is None:
            continue
        d.at[i, "pos"] = str(hh.get("position", ""))
        d.at[i, "won"] = int(str(hh.get("position", "")) == "1")
        d.at[i, "bsp"] = float(hh["bsp"]) if hh.get("bsp") not in (None, "", "-") else None
    t = pd.read_csv(TRACKER) if os.path.exists(TRACKER) else pd.DataFrame()
    t = pd.concat([t[t.day != day] if len(t) else t, d], ignore_index=True)
    t.to_csv(TRACKER, index=False)
    s = t[(t.selected == True) & t.won.notna()]  # noqa: E712
    if not len(s):
        print("no settled selections yet")
        return
    pm = np.where(s.won == 1, (s.mb - 1) * 0.98, -1)
    b = s[s.bsp.notna()]
    pb = np.where(b.won == 1, (b.bsp - 1) * 0.98, -1)
    print(f"top-rated angle (paper) to {day}: {len(s)} bets, won {int(s.won.sum())}, market expected {s.mkt.sum() / 100:.1f}, "
          f"Matchbook 09:00 {pm.sum():+.2f} ({100 * pm.mean():+.1f}%), BSP {pb.sum():+.2f} ({100 * pb.mean():+.1f}%, n {len(b)})")


if __name__ == "__main__":
    {"pick": pick, "settle": settle}[sys.argv[1]](sys.argv[2])
