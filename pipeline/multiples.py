"""Bookmaker multiples (rebuilt 12 Nov 2026; registered prereg/MULTIPLES_REBUILD_2026-11-12.md).

  python3 pipeline/multiples.py build DAY    (after card_review seal) -> store/DAY/multiples_DAY.csv + out/for_vps copies
  python3 pipeline/multiples.py settle DAY   (after save_res)         -> data/multiples_tracker.csv, prints P/L

Legs: sealed CHECK BETs (not excluded) in Flat handicaps with 6+ runners and 09:00 median 3.0-7.0.
Bookmaker choice (William Hill / Betfred / Bet Victor, 09:00 prices): a bookmaker "covers" a leg if its price is at least
the leg's 09:00 median and at least 0.95 x the best of the three. Greedily, the bookmaker covering the most remaining legs
takes all of them (tie: higher total price, then alphabetical); repeat. Legs no bookmaker covers are dropped. Per bookmaker, legs in off-time order are cut into groups of 4:
4 -> Lucky 15 (15 lines), 3 -> Trixie (4 lines), 2 -> Double (1 line), 1 -> Single. Stake 0.50 a line.
"""
import os, shutil, sys
from itertools import combinations
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import p, load_card, num, load_json  # noqa: E402

BOOKS = ["Bet Victor", "Betfred", "William Hill"]
STAKE = 0.5
TYPES = {4: ("Lucky 15", 15), 3: ("Trixie (3 doubles + treble)", 4), 2: ("Double", 1), 1: ("Single only (no partner leg)", 1)}
COLS = ["day", "off_uk", "course", "race_id", "horse", "horse_id", "best_price", "median", "bookmaker", "price", "also_ok_at",
        "bet_id", "bet_type", "n_lines", "stake_per_line", "total_stake"]
TRACKER = p("data", "multiples_tracker.csv")


def build(day):
    t = pd.read_csv(p("data", "card_review_tracker.csv"))
    t = t[(t.day == day) & (t.verdict == "BET") & (t.excluded.astype(str) != "True")]
    t = t[(t.code == "Flat") & (t.hcap.astype(str) == "True") & (t.runners >= 6) & t["median"].between(3.0, 7.0)]
    card = {r["race_id"]: r for r in load_card(day)}
    legs = []
    for x in t.itertuples():
        h = next(h for h in card[x.race_id]["runners"] if h["horse_id"] == x.horse_id)
        px = {o["bookmaker"]: num(o.get("decimal")) for o in h.get("odds", []) or [] if o.get("bookmaker") in BOOKS}
        px = {k: v for k, v in px.items() if v}
        if not px:
            continue
        legs.append(dict(day=day, off_uk=x.off, off_dt=x.off_dt, course=x.course, race_id=x.race_id, horse=x.horse,
                         horse_id=x.horse_id, best_price=max(px.values()), median=x.median, px=px))
    legs.sort(key=lambda l: l["off_dt"])
    left = list(legs)
    while left:
        def cover(bk):
            return [l for l in left if l["px"].get(bk) and l["px"][bk] >= l["median"] and l["px"][bk] >= 0.95 * max(l["px"].values())]
        bk = sorted(BOOKS, key=lambda bk: (-len(cover(bk)), -sum(l["px"][bk] for l in cover(bk)), bk))[0]
        got = cover(bk)
        if not got:
            break
        for l in got:
            l["bookmaker"], l["price"] = bk, l["px"][bk]
            l["also_ok_at"] = ", ".join(f"{k} {v:g}" for k, v in sorted(l["px"].items()) if k != bk and v >= l["median"])
        left = [l for l in left if l not in got]
    legs = [l for l in legs if "bookmaker" in l]
    rows = []
    for b in BOOKS:
        mine = [l for l in legs if l["bookmaker"] == b]
        for i in range(0, len(mine), 4):
            grp = mine[i:i + 4]
            bt, nl = TYPES[len(grp)]
            bid = f"{day}-{b}-{i // 4 + 1}" if len(grp) > 1 else f"{day}-{b}-single"
            for l in grp:
                rows.append({**{k: l[k] for k in COLS if k in l}, "bet_id": bid, "bet_type": bt, "n_lines": nl,
                             "stake_per_line": STAKE, "total_stake": nl * STAKE})
    d = pd.DataFrame(rows, columns=COLS)
    out = p("store", day, f"multiples_{day}.csv")
    d.to_csv(out, index=False)
    os.makedirs(p("out", "for_vps"), exist_ok=True)
    for name in (f"multiples_{day}.csv", "multiples_latest.csv"):
        shutil.copy(out, p("out", "for_vps", name))
    stake = d.drop_duplicates("bet_id").total_stake.sum() if len(d) else 0
    print(f"multiples {day}: {len(legs)} legs, {d.bet_id.nunique() if len(d) else 0} bets, total stake {stake:.2f}")
    for bid, g in d.groupby("bet_id", sort=False):
        print(f"  {g.bookmaker.iloc[0]}: {g.bet_type.iloc[0]} ({g.n_lines.iloc[0]} x {STAKE:.2f}) - "
              + "; ".join(f"{r.off_uk} {r.course} {r.horse} {r.price:g}" for r in g.itertuples()))


def settle(day):
    f = p("store", day, f"multiples_{day}.csv")
    d = pd.read_csv(f) if os.path.exists(f) else pd.DataFrame(columns=COLS)
    res = load_json(p("store", day, "results_all.json.gz"))["results"]
    pos = {(r["race_id"], h["horse_id"]): str(h.get("position", "")) for r in res for h in r["runners"]}
    nr = {(r["race_id"]) : str(r.get("non_runners") or "") for r in res}
    rows = []
    for bid, g in d.groupby("bet_id"):
        legs = g.drop_duplicates("race_id")
        st = float(g.stake_per_line.iloc[0])
        outcome = []
        for l in legs.itertuples():
            ps = pos.get((l.race_id, l.horse_id))
            if ps is None:
                outcome.append("void" if l.horse.split(" (")[0].lower() in nr.get(l.race_id, "").lower() else None)
            else:
                outcome.append("win" if ps == "1" else "lose")
        if any(o is None for o in outcome):
            continue
        k0 = 1 if len(legs) in (1, 4) else 2
        ret = 0.0
        lines = [c for k in range(k0, len(legs) + 1) for c in combinations(range(len(legs)), k)]
        for c in lines:
            if all(outcome[i] in ("win", "void") for i in c):
                ret += st * np.prod([legs.iloc[i].price if outcome[i] == "win" else 1.0 for i in c])
        stake = st * len(lines)
        rows.append(dict(day=day, bet_id=bid, bookmaker=g.bookmaker.iloc[0], bet_type=g.bet_type.iloc[0], legs=len(legs),
                         winners=outcome.count("win"), stake=stake, returns=round(ret, 2), pl=round(ret - stake, 2)))
    t = pd.read_csv(TRACKER) if os.path.exists(TRACKER) else pd.DataFrame()
    t = pd.concat([t[t.day != day] if len(t) else t, pd.DataFrame(rows)], ignore_index=True)
    t.to_csv(TRACKER, index=False)
    day_pl = sum(r["pl"] for r in rows)
    print(f"multiples {day}: {len(rows)} bets settled, P/L {day_pl:+.2f}; since rebuild: {len(t)} bets, stake {t.stake.sum() if len(t) else 0:.2f}, "
          f"P/L {t.pl.sum() if len(t) else 0:+.2f}")


if __name__ == "__main__":
    {"build": build, "settle": settle}[sys.argv[1]](sys.argv[2])
