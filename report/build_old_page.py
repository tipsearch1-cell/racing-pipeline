"""Old-design report page: python3 report/build_old_page.py DAY -> report/race-reports.html

Uses the recovered renderer (report/old_template.html) and history (report/history_data.json: reports, tracker,
reviews, xw, guide, angles, bets, changes for 12 Oct - 9 Nov from the original pipeline) and adds DAY from the
rebuilt pipeline in the same schema. Until the models are rebuilt the "Model" column carries the reviewer's chance.
"""
import base64, json, os, re, sys
from datetime import datetime, timezone
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pipeline"))
from common import load_card, race_market, code_of, unknown_runner, p  # noqa: E402

PAT = {"fill": "solid", "halve": "halved", "quarter": "quartered", "hoop": "hoop", "hoops": "hoops", "stripe": "stripe",
       "stripes": "stripes", "check": "check", "checks": "check", "chevron": "chevron", "chevrons": "chevrons", "sash": "sash",
       "cross-belts": "cross-belts", "braces": "braces", "diamond": "diamond", "diamonds": "diamonds", "star": "star", "stars": "stars",
       "spots": "spots", "disc": "disc", "seams": "seams", "epaulettes": "epaulettes", "armlet": "armlet", "yoke": "yoke"}


def silk(url):
    if "body=" in (url or ""):
        try:
            q = dict(x.split("=", 1) for x in url.split("?", 1)[1].split("&") if "=" in x)
            def part(v):
                pat, _, cols = v.partition(":")
                cs = [c.strip() for c in cols.split(",") if c.strip()] or ["grey"]
                return [PAT.get(pat, pat), cs[0], cs[1] if len(cs) > 1 else cs[0]]
            b = part(q["body"])
            return {"b": b, "s": part(q.get("sleeves", f"solid:{b[1]}")), "k": part(q.get("cap", f"solid:{b[1]}"))}
        except Exception:
            return None
    try:
        c = url.split("c=", 1)[1]
        c += "=" * (-len(c) % 4)
        j = json.loads(base64.urlsafe_b64decode(c))
        lay = j.get("body", {}).get("layers", [])
        c1 = lay[0].get("color") if lay else "#888888"
        if len(lay) > 1:
            b = [PAT.get(lay[1].get("type"), lay[1].get("type")), c1, lay[1].get("color")]
        else:
            b = ["solid", c1, c1]
        def part(x, default):
            if not x:
                return ["solid", default, default]
            cols = x.get("colors") or [x.get("color", default)]
            return [PAT.get(x.get("pattern", "fill"), x.get("pattern", "solid")), cols[0], cols[1] if len(cols) > 1 else cols[0]]
        return {"b": b, "s": part(j.get("sleeves"), c1), "k": part(j.get("cap"), c1)}
    except Exception:
        return None


def furlongs(d):
    try:
        return f"{round(float(d))}f"
    except (TypeError, ValueError):
        return ""


def main(day):
    hist = json.load(open(p("report", "history_data.json")))
    card = load_card(day)
    t = pd.read_csv(p("data", "card_review_tracker.csv"))
    t = t[t.day == day].set_index(["race_id", "horse_id"])
    det_f = p("store", day, f"reviewer_bets_detail_{day}.csv")
    det = pd.read_csv(det_f) if os.path.exists(det_f) else pd.DataFrame()
    status = "PAPER"
    if os.path.exists(p("data", "live_days.csv")):
        s = pd.read_csv(p("data", "live_days.csv"))
        if (s.day == day).any():
            status = s[s.day == day].status.iloc[-1]
    mf = p("store", day, "model.json")
    model = json.load(open(mf))["races"] if os.path.exists(mf) else {}
    races, bets = [], {}
    for r in card:
        mr = model.get(r["race_id"], {})
        mk = race_market(r)
        name = r.get("race_name") or ""
        hcap = "handicap" in name.lower() or "nursery" in name.lower()
        runners = []
        for h in r["runners"]:
            m = mk[h["horse_id"]]
            md = (mr.get("runners") or {}).get(h["horse_id"])
            row = t.loc[(r["race_id"], h["horse_id"])] if (r["race_id"], h["horse_id"]) in t.index else None
            rev = None if row is None else float(row.rev) / 100
            pros, cons = [], []
            if row is not None and isinstance(row.reason, str) and row.reason:
                (pros if row.rev > row.mkt else cons).append("Reviewer: " + row.reason)
            tc = h.get("trainer_14_days") or {}
            note = f"Form {h.get('form') or '-'} · last run {h.get('last_run') or '-'} days · trainer 14d {tc.get('wins', '?')}/{tc.get('runs', '?')}"
            if unknown_runner(h):
                cons.append("Unknown runner: no form and no card comment (race excluded from the bot file)")
            txt = (h.get("spotlight") or h.get("comment") or "").strip()
            if md:
                pros = md["pros"] + pros
                cons = md["cons"] + cons
                if rev is not None:
                    (pros if rev > (m["mkt"] or 0) / 100 else cons).append(f"Sealed reviewer chance {rev:.0%} (market {(m['mkt'] or 0):.0f}%)")
            runners.append({"horse": h["horse"], "age": h.get("age"), "OR": None if h.get("ofr") in ("", "-", None) else h.get("ofr"),
                            "lbs": h.get("lbs"), "draw": None if str(h.get("draw")) in ("", "0") else h.get("draw"),
                            "style": md["style"] if md else "Unknown", "lead": md["lead"] if md else None,
                            "p": md["p"] if md else rev, "best": m["best_ex"], "bf": None, "mkt": (m["mkt"] or 0) / 100 or None,
                            "runs": md["runs"] if md else None, "days": h.get("last_run"), "hist": md["hist"] if md else [],
                            "pros": pros + ([note] if note and not md else []),
                            "cons": cons + ([f"Card comment: {txt}"] if txt else []), "h2h": md["h2h"] if md else [],
                            "silk": silk(h.get("silk_url", ""))})
        runners.sort(key=lambda x: -(x["p"] or x["mkt"] or 0))
        off = pd.Timestamp(r["off_dt"]).tz_convert("Europe/London").strftime("%H:%M")
        rtype = None if code_of(r) == "Flat" else r.get("type")
        races.append({"race_id": r["race_id"], "course": r["course"], "off": off, "off_dt": r["off_dt"], "name": name[:80],
                      "dist": r.get("distance_round") or r.get("distance"), "going": r.get("going"), "cls": r.get("race_class"),
                      "region": r.get("region"), "hcap": hcap, "field": len(r["runners"]), "code": code_of(r), "rtype": rtype,
                      "shape": mr.get("shape") or {"label": "Unclear", "note": "No model output for this race."},
                      "bias": [], "bias_key": mr.get("bias_key"), "runners": runners,
                      "top": runners[0]["horse"] if runners else None})
        if len(det):
            b = det[(det.Status == "BOT FILE") & (det.Course == r["course"]) & (det.OffUK == off)]
            if len(b):
                bets[r["race_id"]] = [f"{x.SelectionName} ({'CHECK BET' if 'CHECK' in x.Source else 'value flag'}; best price {x.BestPrice9am}; "
                                      f"min {x.MinPrice}; reviewer {x.ReviewerChancePct:.0f}% vs market {x.MarketChancePct:.0f}%) - {x.Reason}"
                                      for x in b.itertuples()]
    note = (f"{status}. Rebuilt pipeline from 10 Nov: Model = rebuilt win model (form, earlier Betfair prices, ratings; no market), "
            "run styles from in-running comments; best price = best 09:00 exchange price; market = sharp-weighted 09:00 market"
            if model else f"{status}. Rebuilt pipeline: Model column shows the sealed reviewer's chance (no model output for this day)")
    rep = {"day": day, "generated": datetime.now(timezone.utc).astimezone().strftime("%H:%M"), "price_note": note, "races": races}
    hist["reports"] = [x for x in hist["reports"] if x["day"] != day] + [rep]
    hist["reports"].sort(key=lambda x: x["day"])
    hist.setdefault("bets", {})[day] = bets
    cf = p("store", day, "changes.json")
    if os.path.exists(cf):
        ev = json.load(open(cf)).get("events", [])
        byr = {}
        for e in ev:
            rid = e["key"].split("|")[1]
            byr.setdefault(rid, []).append(f"{e.get('at', '')}: {e['text']}")
        hist.setdefault("changes", {})[day] = {"updated": ev[-1].get("at", "") if ev else "", "races": byr}
    tpl = open(p("report", "old_template.html")).read()
    data = json.dumps(hist, separators=(",", ":")).replace("</", "<\\/")
    out = tpl.replace("__DATA__", data, 1)
    with open(p("report", "race-reports.html"), "w") as f:
        f.write(out)
    print(f"old-design page: {day} added ({len(races)} races, {sum(len(v) for v in bets.values())} bet lines), {len(hist['reports'])} days, {len(out)/1e6:.1f} MB")


if __name__ == "__main__":
    main(sys.argv[1])
