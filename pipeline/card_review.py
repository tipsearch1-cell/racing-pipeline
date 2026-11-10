"""Card reviewer (rebuilt 10 Nov 2026).

  python3 pipeline/card_review.py prep DAY      -> store/DAY/review/in_<meeting>.md + meetings.json
  python3 pipeline/card_review.py seal DAY      -> validates out_<meeting>.json, writes tracker rows + SEAL.txt
  python3 pipeline/card_review.py settle DAY    -> fills results (pos, SP, BSP) for DAY and prints running summaries

Amendments 10 Nov 2026 (prereg/REBUILD_RULES_2026-11-10.md, from 11 Nov): price tests use the Matchbook 09:00 price;
races with an unraced runner are excluded; the card's own rating/ranking sentences are removed from the packet comments.
CHECK runners (rebuilt rule): the market favourite of each race with 5+ runners whose 09:00 median price is 3.0-6.0.
Value flag: the reviewer actively raised the runner, final chance >= 1.25 x market chance and >= 3%,
and best exchange price >= 100 / reviewer chance. Changed runners keep the reviewer's figure; unchanged runners share the rest.
"""
import csv, glob, hashlib, json, math, os, re, sys
import numpy as np, pandas as pd
from common import load_card, race_market, code_of, is_aw, unknown_runner, meeting_key, now_utc, p, load_json

TRACKER = p("data", "card_review_tracker.csv")
COLS = ["day", "race_id", "off", "off_dt", "course", "code", "aw", "hcap", "runners", "horse_id", "horse", "mkt", "rev",
        "median", "best", "mb", "check", "verdict", "bet", "reason", "excluded", "pos", "won", "sp", "bsp"]

OWN_RATING = re.compile(r"(?i)our rating|our top|top-rated|top rated|one to beat|leading danger|main danger|ranks? (him|her|it)|"
                        r"ranked|tops? (the|our)|by our|on our|our figures|our ratings")


def strip_own_ratings(txt):
    """Drop sentences that quote the card provider's own rating or ranking (amended rule 10 Nov 2026)."""
    sents = re.split(r"(?<=[.!?])\s+", txt.strip())
    return " ".join(s for s in sents if not OWN_RATING.search(s)).strip()


HEADER = """# Card review packet: {course}, {day}

You are a racing form reviewer. Use ONLY this packet. For every race:

1. Start from each runner's MARKET chance (the sharp-weighted 09:00 price, in %).
2. Change a runner's chance ONLY where the card below gives a specific reason: recent form figures, a comment
   or spotlight line, official rating (OR) vs today's weight, days since last run, trainer's 14-day record,
   headgear or wind surgery first time, draw, trip/going/course clues in the comment. Give a one-line reason
   that names the card fact. No reason on the card = no change. Do not use outside knowledge of the horses.
3. Keep changes moderate: normally within 0.67x to 1.5x of the market chance; never beyond 0.33x to 3x.
   Totals do not need to add to 100; they are rescaled afterwards.
4. Runners marked CHECK need a verdict, BET or SKIP:
   BET only if (a) your chance x Matchbook price >= 1.05 AND (b) Matchbook price >= the skip line
   shown (0.95 x 09:00 median), and the card supports your chance. "Matchbook" is the price the bet would get. Otherwise SKIP. Give a one-line reason.

Write valid JSON to the out path you were given, exactly this shape (use the exact race_id and horse_id values):
{{"meeting": "{key}", "races": [
  {{"race_id": "rac_...", "changes": [{{"horse_id": "hrs_...", "horse": "Name", "chance_pct": 12.5, "reason": "..."}}],
    "checks": [{{"horse_id": "hrs_...", "horse": "Name", "verdict": "BET", "reason": "..."}}]}}
]}}
Include every race (empty lists are fine). chance_pct is the new win chance in percent.
"""


def fmt(x, nd=2):
    return "-" if x is None else f"{x:.{nd}f}"


def prep(day):
    card = load_card(day)
    outdir = p("store", day, "review")
    os.makedirs(outdir, exist_ok=True)
    meetings = {}
    by_course = {}
    for r in card:
        by_course.setdefault(r["course"], []).append(r)
    for course, races in by_course.items():
        key = meeting_key(course)
        lines = [HEADER.format(course=course, day=day, key=key)]
        nchk = 0
        for r in races:
            mk = race_market(r)
            fav = max((h for h in r["runners"] if mk[h["horse_id"]]["mkt"]), key=lambda h: mk[h["horse_id"]]["mkt"], default=None)
            lines.append(f"\n## {r['off_time']} {course} | race_id {r['race_id']} | {r['race_name']}")
            lines.append(f"{r.get('type')} | {r.get('race_class')} | {r.get('distance')} | going {r.get('going')} | "
                         f"{r.get('surface')} | {len(r['runners'])} runners | rating band {r.get('rating_band') or '-'} | age {r.get('age_band')}")
            for h in sorted(r["runners"], key=lambda h: -(mk[h["horse_id"]]["mkt"] or 0)):
                m = mk[h["horse_id"]]
                is_chk = (fav is h and len(r["runners"]) >= 5 and m["median"] and 3.0 <= m["median"] <= 6.0)
                nchk += bool(is_chk)
                t14 = h.get("trainer_14_days") or {}
                tag = f" | CHECK (skip line {0.95 * m['median']:.2f})" if is_chk else ""
                lines.append(
                    f"- {h['horse']} ({h['horse_id']}) | {h.get('age')}yo {h.get('sex_code')} | {h.get('lbs')}lb | OR {h.get('ofr') or '-'} | "
                    f"draw {h.get('draw') or '-'} | jockey {h.get('jockey')} | trainer {h.get('trainer')} (14d {t14.get('wins', '?')}/{t14.get('runs', '?')}) | "
                    f"headgear {h.get('headgear') or '-'}{' (1st time)' if h.get('headgear_run') == '1' else ''}"
                    f"{' | wind surgery' if h.get('wind_surgery') else ''} | last run {h.get('last_run') or '-'} days | form {h.get('form') or '-'} | "
                    f"MARKET {fmt(m['mkt'], 1)}% | 09:00 median {fmt(m['median'])} | Matchbook {fmt(m['mb'])}{tag}")
                txt = strip_own_ratings(h.get("spotlight") or h.get("comment") or "")
                if txt:
                    lines.append(f"    comment: {txt}")
        inp, out = os.path.join(outdir, f"in_{key}.md"), os.path.join(outdir, f"out_{key}.json")
        with open(inp, "w") as f:
            f.write("\n".join(lines) + "\n")
        meetings[key] = {"course": course, "in": inp, "out": out, "races": len(races), "checks": nchk}
        print(f"  {course}: {inp} -> {out} ({len(races)} races, {nchk} CHECK)")
    json.dump(meetings, open(os.path.join(outdir, "meetings.json"), "w"), indent=1)


def seal(day):
    card = load_card(day)
    rd = p("store", day, "review")
    meetings = json.load(open(os.path.join(rd, "meetings.json")))
    outs, missing = {}, []
    for key, m in meetings.items():
        try:
            outs[key] = {x["race_id"]: x for x in json.load(open(m["out"]))["races"]}
        except Exception as e:
            missing.append(f"{key}: {e}")
    if missing:
        sys.exit("NOT SEALED - missing/invalid: " + "; ".join(missing))
    rows, nchg, nbet, nchk, nskip = [], 0, 0, 0, 0
    warn = []
    stamp_dt = pd.Timestamp(now_utc())
    if stamp_dt.tzinfo is None:
        stamp_dt = stamp_dt.tz_localize("UTC")
    for r in card:
        key = meeting_key(r["course"])
        if r["race_id"] not in outs.get(key, {}):
            warn.append(f"{r['off_time']} {r['course']}: race missing from reviewer output (treated as no changes, no verdicts)")
        ro = outs.get(key, {}).get(r["race_id"], {"changes": [], "checks": []})
        mk = race_market(r)
        ids = {h["horse_id"] for h in r["runners"]}
        fav = max((h for h in r["runners"] if mk[h["horse_id"]]["mkt"]), key=lambda h: mk[h["horse_id"]]["mkt"], default=None)
        chk_ids = {fav["horse_id"]} if (fav and len(r["runners"]) >= 5 and mk[fav["horse_id"]]["median"]
                                        and 3.0 <= mk[fav["horse_id"]]["median"] <= 6.0) else set()
        for c in ro.get("changes", []) + ro.get("checks", []):
            if c.get("horse_id") and c["horse_id"] not in ids:
                warn.append(f"{r['off_time']} {r['course']}: unknown horse_id {c['horse_id']} ({c.get('horse')}) ignored")
        off_before_seal = pd.Timestamp(r["off_dt"]) <= stamp_dt
        ch = {c["horse_id"]: c for c in ro.get("changes", []) if c.get("horse_id")}
        ck = {c["horse_id"]: c for c in ro.get("checks", []) if c.get("horse_id") in chk_ids}
        for c in ro.get("checks", []):
            if c.get("horse_id") in ids and c["horse_id"] not in chk_ids:
                warn.append(f"{r['off_time']} {r['course']}: verdict for non-CHECK runner {c.get('horse')} ignored")
        for hid in chk_ids - set(ck):
            warn.append(f"{r['off_time']} {r['course']}: CHECK runner without a verdict -> SKIP")
            ck[hid] = {"verdict": "SKIP", "reason": "no verdict given (auto SKIP)"}
        raw = {}
        for h in r["runners"]:
            m = mk[h["horse_id"]]["mkt"]
            if m is None:
                continue
            v = ch.get(h["horse_id"], {}).get("chance_pct", m)
            try:
                v = float(v)
            except (TypeError, ValueError):
                v = m
            raw[h["horse_id"]] = min(max(v, m / 3), m * 3)
        # changed runners keep the reviewer's figure; unchanged runners share what is left, in market proportion
        chg_tot = sum(v for k, v in raw.items() if k in ch)
        unch_mkt = sum(mk[k]["mkt"] for k in raw if k not in ch)
        left = 100 - chg_tot
        if ch and unch_mkt and left > 0.5 * unch_mkt:
            for k in raw:
                if k not in ch:
                    raw[k] = mk[k]["mkt"] * left / unch_mkt
        tot = max(sum(raw.values()), 100.0)  # scale down only: an under-100 book never inflates the reviewer's figures
        excluded = any(unknown_runner(h) for h in r["runners"]) or off_before_seal
        if off_before_seal:
            warn.append(f"{r['off_time']} {r['course']}: already off at seal time -> excluded")
        hcap = "handicap" in (r.get("race_name") or "").lower() or "nursery" in (r.get("race_name") or "").lower()
        for h in r["runners"]:
            hid = h["horse_id"]
            m = mk[hid]
            if m["mkt"] is None:
                continue
            rev = round(100 * raw[hid] / tot, 2)
            verdict = (ck.get(hid, {}).get("verdict") or "").upper() or None
            if verdict == "BET":  # re-check the packet's own BET test instead of trusting the reviewer's arithmetic
                yours = raw[hid] * 100 / tot
                if not (m["mb"] and m["median"] and yours * m["mb"] / 100 >= 1.05 and m["mb"] >= 0.95 * m["median"]):
                    warn.append(f"{r['off_time']} {r['course']}: {h['horse']} BET fails the packet test "
                                f"(chance {yours:.1f}% x Matchbook {m['mb']}) -> SKIP")
                    verdict = "SKIP"
            if verdict not in (None, "BET", "SKIP"):
                warn.append(f"{r['off_time']} {r['course']}: {h['horse']} verdict {verdict!r} not BET/SKIP -> SKIP")
                verdict = "SKIP"
            reason = ck.get(hid, {}).get("reason") or ch.get(hid, {}).get("reason") or ""
            raised = hid in ch and float(ch[hid].get("chance_pct") or 0) > m["mkt"]
            bet = bool(raised and rev >= 1.25 * m["mkt"] and rev >= 3 and m["mb"] and m["mb"] >= 100 / rev)
            nchg += hid in ch
            nbet += bet
            nchk += verdict is not None
            nskip += verdict == "SKIP"
            rows.append(dict(day=day, race_id=r["race_id"], off=r["off_time"], off_dt=r["off_dt"], course=r["course"], code=code_of(r),
                             aw=is_aw(r), hcap=hcap, runners=len(r["runners"]), horse_id=hid, horse=h["horse"], mkt=m["mkt"], rev=rev,
                             median=m["median"], best=m["best_ex"], mb=m["mb"], check=verdict is not None, verdict=verdict, bet=bet,
                             reason=reason, excluded=excluded, pos=None, won=None, sp=None, bsp=None))
    df = pd.DataFrame(rows, columns=COLS)
    if os.path.exists(TRACKER):
        old = pd.read_csv(TRACKER)
        if (old.day == day).any():
            sys.exit(f"{day} already sealed in the tracker - not overwriting")
        df = pd.concat([old, df], ignore_index=True)
    os.makedirs(os.path.dirname(TRACKER), exist_ok=True)
    df.to_csv(TRACKER, index=False)
    h = hashlib.sha256()
    for key in sorted(meetings):
        h.update(open(meetings[key]["out"], "rb").read())
    first_off = min(r["off_dt"] for r in card)
    stamp = now_utc()
    with open(os.path.join(rd, "SEAL.txt"), "w") as f:
        f.write(f"sealed {stamp}; first off {first_off}; sha256 of outputs {h.hexdigest()}\n")
    for w in warn:
        print("  WARNING:", w)
    if pd.Timestamp(first_off) <= stamp_dt:
        print(f"  WARNING: sealed AFTER the first off ({first_off}); races already off are excluded from the bot file")
    print(f"sealed {day} at {stamp} (first off {first_off}): {len(card)} races, {len(rows)} runners, {nchg} changed, "
          f"{nbet} value flags, {nchk} CHECK verdicts ({nskip} SKIP)")


def settle(day):
    rf = p("store", day, "results_all.json.gz")
    res = load_json(rf)["results"]
    info = {}
    for race in res:
        for hh in race["runners"]:
            info[(race["race_id"], hh["horse_id"])] = hh
    df = pd.read_csv(TRACKER)
    for c in ("pos", "sp", "bsp", "won"):
        df[c] = df[c].astype(object)
    m = df.day == day
    for i in df[m].index:
        hh = info.get((df.at[i, "race_id"], df.at[i, "horse_id"]))
        if hh is None:
            continue
        pos = str(hh.get("position", ""))
        df.at[i, "pos"] = pos
        df.at[i, "won"] = int(pos == "1")
        df.at[i, "sp"] = float(hh["sp_dec"]) if hh.get("sp_dec") not in (None, "", "-") else None
        df.at[i, "bsp"] = float(hh["bsp"]) if hh.get("bsp") not in (None, "", "-") else None
    df.to_csv(TRACKER, index=False)
    summary(df)


def summary(df):
    s = df[df.pos.notna() & (df.pos.astype(str) != "NR")].copy()
    s["won"] = s.won.astype(float)
    live = set()
    if os.path.exists(p("data", "live_days.csv")):
        ld = pd.read_csv(p("data", "live_days.csv"))
        live = set(ld[ld.status == "LIVE"].day)
    s["status"] = np.where(s.day.isin(live), "LIVE", "PAPER")
    ll = []
    for _, g in s.groupby(["day", "race_id"]):
        if g.won.sum() != 1:
            continue
        w = g[g.won == 1].iloc[0]
        ll.append(math.log(w.rev / 100) - math.log(w.mkt / 100))
    print(f"  reviewer log-loss gain vs market (+ = reviewer better): {np.mean(ll):+.4f} per race (n {len(ll)})" if ll else "  no settled races")
    s = s[s.excluded.astype(str) != "True"]  # P/L only for rows that could reach the bot file
    groups = []
    for st in ("LIVE", "PAPER"):
        g = s[s.status == st]
        groups += [(f"{st} CHECK BET", g[g.verdict == "BET"]), (f"{st} value flags", g[g.bet == True])]  # noqa: E712
    for lab, x in groups:
        if not len(x):
            continue
        px = x.mb.where(x.mb.notna(), x.best) if "mb" in x else x.best  # Matchbook 09:00 from 11 Nov; best exchange before
        p9 = np.where(x.won == 1, (px - 1) * 0.98, -1)
        b = x[x.bsp.notna()]
        pb = np.where(b.won == 1, (b.bsp - 1) * 0.98, -1)
        print(f"  {lab}: {len(x)} bets, won {int(x.won.sum())}, 09:00 Matchbook/best {p9.sum():+.2f} ({100 * p9.mean():+.1f}%)"
              + (f", BSP {pb.sum():+.2f} ({100 * pb.mean():+.1f}%, n {len(b)})" if len(b) else ""))


if __name__ == "__main__":
    {"prep": prep, "seal": seal, "settle": settle}[sys.argv[1]](sys.argv[2])
