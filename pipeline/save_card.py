"""Seal the day's card: python3 pipeline/save_card.py DAY saved_racecards_file [more files]

Keeps the raw morning card (card_morning.json.gz), drops abandoned races and runners already declared
non-runners (runner number == "NR"), and writes store/DAY/sealed_card.json.gz plus out/for_vps copies.
"""
import os, sys
from common import load_json, save_json, day_dir, now_utc, p


def main(day, files):
    cards = []
    for f in files:
        cards += load_json(f)["racecards"]
    seen, uniq = set(), []
    for r in cards:
        if r["race_id"] not in seen:
            seen.add(r["race_id"])
            uniq.append(r)
    d = day_dir(day)
    save_json(os.path.join(d, "card_morning.json.gz"), {"fetched_at_uk": now_utc(), "racecards": uniq})
    sealed, abandoned, n_nr = [], [], 0
    for r in uniq:
        if r.get("date") and r["date"] != day:
            continue
        if r.get("is_abandoned"):
            abandoned.append(f'{r["off_time"]} {r["course"]}')
            continue
        nr = [h["horse"] for h in r["runners"] if str(h.get("number", "")).upper() == "NR"]
        n_nr += len(nr)
        r = dict(r)
        r["runners"] = [h for h in r["runners"] if str(h.get("number", "")).upper() != "NR"]
        r["nr_at_seal"] = nr
        r["field_size"] = str(len(r["runners"]))
        sealed.append(r)
    sealed.sort(key=lambda r: r["off_dt"])
    out = {"fetched_at_uk": now_utc(), "racecards": sealed}
    save_json(os.path.join(d, "sealed_card.json.gz"), out)
    os.makedirs(p("out", "for_vps"), exist_ok=True)
    for name in (f"sealed_card_{day}.json", "sealed_card_latest.json"):
        save_json(p("out", "for_vps", name), out)
    courses = sorted({r["course"] for r in sealed})
    print(f"{day}: {len(sealed)} races sealed at {now_utc()} ({len(abandoned)} abandoned left out: {', '.join(abandoned) or 'none'}); "
          f"{n_nr} declared non-runners removed")
    if sealed:
        print(f"meetings: {', '.join(courses)} | first off {sealed[0]['off_dt']} | last off {sealed[-1]['off_dt']} | "
              f"Flat races {sum(1 for r in sealed if (r.get('type') or '').lower() == 'flat')}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
