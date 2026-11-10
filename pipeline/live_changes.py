"""Live card check: python3 pipeline/live_changes.py DAY saved_racecards_file [more files]
Compares the current card with the sealed card and with earlier checks (store/DAY/changes.json) and prints NEW events:
late non-runners (flagging bot-file bets and multiple legs), going changes and abandoned races, for races not yet off.
"""
import json, os, sys
from datetime import datetime, timezone
import pandas as pd
from common import load_json, load_card, race_market, p


def main(day, files):
    now = datetime.now(timezone.utc)
    cur = {}
    for f in files:
        for r in load_json(f)["racecards"]:
            cur[r["race_id"]] = r
    sealed = load_card(day)
    cf = p("store", day, "changes.json")
    seen = json.load(open(cf)) if os.path.exists(cf) else {"events": []}
    known = {e["key"] for e in seen["events"]}
    bets = set()
    bf = p("store", day, f"reviewer_bets_detail_{day}.csv")
    if os.path.exists(bf):
        b = pd.read_csv(bf)
        bets = set(b[b.Status == "BOT FILE"].SelectionName)
    legs = set()
    mf = p("store", day, f"multiples_{day}.csv")
    if os.path.exists(mf) and os.path.getsize(mf) > 5:
        legs = set(pd.read_csv(mf).horse)
    new = []
    for r in sealed:
        c = cur.get(r["race_id"])
        off = datetime.fromisoformat(r["off_dt"])
        future = off > now
        tag = f"{r['off_time']} {r['course']}"
        if c is None:
            continue
        if c.get("is_abandoned"):
            new.append(dict(key=f"ab|{r['race_id']}", text=f"{tag}: race ABANDONED", future=future, important=True))
        if (c.get("going") or "") != (r.get("going") or ""):
            new.append(dict(key=f"go|{r['race_id']}|{c.get('going')}", text=f"{tag}: going changed from {r.get('going')} to {c.get('going')}",
                            future=future, important=True))
        nrs = [h for h in c["runners"] if str(h.get("number", "")).upper() == "NR" and h["horse"] not in r.get("nr_at_seal", [])]
        if nrs:
            left = dict(c, runners=[h for h in c["runners"] if str(h.get("number", "")).upper() != "NR"])
            mk = race_market(left)
            top = sorted(left["runners"], key=lambda h: -(mk[h["horse_id"]]["mkt"] or 0))[:4]
            line = ", ".join(f"{h['horse']} {mk[h['horse_id']]['mkt']:.0f}%" for h in top if mk[h["horse_id"]]["mkt"])
            for h in nrs:
                flag = " [BOT-FILE BET - void]" if h["horse"] in bets else (" [MULTIPLE LEG - void leg]" if h["horse"] in legs else "")
                new.append(dict(key=f"nr|{r['race_id']}|{h['horse_id']}", text=f"{tag}: {h['horse']} now a non-runner{flag}. Re-worked market: {line}",
                                future=future, important=bool(flag)))
            others = [x for x in left["runners"] if x["horse"] in bets or x["horse"] in legs]
            for x in others:
                new.append(dict(key=f"aff|{r['race_id']}|{x['horse_id']}|{len(nrs)}", text=f"{tag}: bet/leg {x['horse']} runs on in a race with a new non-runner",
                                future=future, important=True))
    fresh = [e for e in new if e["key"] not in known]
    seen["events"] += [dict(e, at=now.strftime("%H:%M")) for e in fresh]
    json.dump(seen, open(cf, "w"), indent=1)
    print(f"{day} {now:%H:%M}: checked {len(sealed)} races; new events {len(fresh)} "
          f"(still to run {sum(e['future'] for e in fresh)}, important & still to run {sum(e['future'] and e['important'] for e in fresh)})")
    for e in fresh:
        print(("  ! " if e["future"] and e["important"] else "  ") + e["text"] + ("" if e["future"] else " (race already off)"))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
