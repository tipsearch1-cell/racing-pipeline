"""Save results: python3 pipeline/save_res.py DAY saved_results_file [more files]
Writes store/DAY/results_all.json.gz (races of DAY only) and prints race / BSP coverage vs the sealed card.
"""
import os, sys
from common import load_json, save_json, p


def main(day, files):
    res = []
    for f in files:
        res += load_json(f)["results"]
    res = [r for r in res if str(r.get("date", day))[:10] == day]
    seen, uniq = set(), []
    for r in res:
        if r["race_id"] not in seen:
            seen.add(r["race_id"])
            uniq.append(r)
    save_json(p("store", day, "results_all.json.gz"), {"results": uniq})
    n = sum(len(r["runners"]) for r in uniq)
    nb = sum(1 for r in uniq for h in r["runners"] if h.get("bsp") not in (None, "", "-"))
    miss = sum(1 for r in uniq if any(h.get("bsp") in (None, "", "-") and str(h.get("position", "")) not in ("", "NR") for h in r["runners"]))
    sealed = p("store", day, "sealed_card.json.gz")
    card_ids = {r["race_id"] for r in load_json(sealed)["racecards"]} if os.path.exists(sealed) else set()
    print(f"{day}: {len(uniq)} races saved ({len(card_ids - seen)} sealed races missing from results), runners {n}, with BSP {nb}, "
          f"races still missing BSP {miss}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
