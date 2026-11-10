"""Shared helpers for the rebuilt racing pipeline (rebuilt 10 Nov 2026 after the workspace was reclaimed).

Market definitions (new in the rebuild, documented in prereg/REBUILD_RULES_2026-11-10.md):
  median   = median decimal price across all bookmakers quoting the runner at the 09:00 fetch
  best_ex  = best (highest) exchange price among Betfair Exchange, Matchbook, Smarkets
  mkt      = sharp-weighted market chance: 0.6 * (1/mean exchange price) + 0.4 * (1/median), normalised to 100% per race
"""
import gzip, json, os, re, statistics
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCHANGES = {"Betfair Exchange", "Matchbook", "Smarkets"}


def p(*parts):
    return os.path.join(ROOT, *parts)


def day_dir(day):
    d = p("store", day)
    os.makedirs(d, exist_ok=True)
    return d


def load_json(path):
    op = gzip.open if path.endswith(".gz") else open
    with op(path, "rt") as f:
        return json.load(f)


def save_json(path, obj):
    op = gzip.open if path.endswith(".gz") else open
    with op(path, "wt") as f:
        json.dump(obj, f)


def load_card(day):
    return load_json(p("store", day, "sealed_card.json.gz"))["racecards"]


def num(x):
    try:
        v = float(x)
        return v if v > 1 else None
    except (TypeError, ValueError):
        return None


def runner_prices(h):
    """Return (median, best_ex, mean_ex, n_books) for one runner."""
    allp, ex = [], []
    for o in h.get("odds", []) or []:
        v = num(o.get("decimal"))
        if v is None:
            continue
        allp.append(v)
        if o.get("bookmaker") in EXCHANGES:
            ex.append(v)
    if not allp:
        return None, None, None, 0
    med = statistics.median(allp)
    return med, (max(ex) if ex else None), (sum(ex) / len(ex) if ex else None), len(allp)


def race_market(race):
    """Per runner dict horse_id -> {median, best_ex, mkt (0-100)}; runners without prices get mkt None."""
    rows, raw = {}, {}
    for h in race["runners"]:
        med, best_ex, mean_ex, n = runner_prices(h)
        rows[h["horse_id"]] = dict(median=med, best_ex=best_ex, n_books=n)
        if med:
            pe = 1 / mean_ex if mean_ex else 1 / med
            raw[h["horse_id"]] = 0.6 * pe + 0.4 / med
    tot = sum(raw.values())
    for hid, r in rows.items():
        r["mkt"] = round(100 * raw[hid] / tot, 2) if hid in raw and tot else None
    return rows


def code_of(race):
    t = (race.get("type") or "").lower()
    return "Flat" if t == "flat" else "Jumps"


def is_aw(race):
    return "(AW)" in race.get("course", "") or (race.get("surface") or "").lower() not in ("turf", "")


def unknown_runner(h):
    """A runner the card says nothing about: no form string and no comment/spotlight."""
    return not (h.get("form") or "").strip() and not (h.get("comment") or "").strip() and not (h.get("spotlight") or "").strip()


def base_name(s):
    return re.sub(r"\s*\([A-Z]{2,4}\)\s*$", "", s or "").strip().lower()


def now_utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def meeting_key(course):
    return re.sub(r"[^a-z0-9]+", "_", course.lower().replace("(aw)", "aw")).strip("_")
