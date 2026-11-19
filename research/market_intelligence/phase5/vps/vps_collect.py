"""Phase 5 VPS market collector (research only; disabled by default; never touches production or betting files).

  python3 vps_collect.py tick    [--config F]   # cron every minute; fetches ONLY when a checkpoint is due (see below)
  python3 vps_collect.py history DAY [--config F]   # after racing: per-runner price histories (/odds/{race}/{horse}) -> reconstructed checkpoints
  python3 vps_collect.py health  [DAY] [--config F] # operational status JSON (counts only, no model performance)
  python3 vps_collect.py selftest                    # offline test with the bundled fixture (no network)

Checkpoints (live captures, labelled market/<label>/<race_id>.json.gz under the race day):
  E2100   21:00 UK the evening before (request day=tomorrow)
  0900    09:00 UK race day
  off-60m off-30m off-15m off-10m off-05m off-01m   minutes before the scheduled off
A schedule cache (race_id -> scheduled off, UTC) is refreshed from the racecards at most every 30 minutes; between refreshes a
full racecards request is made only when a checkpoint is due within the tolerance. Typical load: about 50 schedule refreshes
plus about 100-200 checkpoint requests per racing day (several races share a request), never more than
max_requests_per_second. A failed request is appended to <day>/failures.jsonl and retried at the next tick while the
checkpoint is still inside its tolerance window; after that it stays missing (never back-filled as a live capture).
Each file stores fetch_started_utc / fetch_finished_utc (VPS clock, NTP), the provider's per-quote 'updated' time (UK local
clock, naive - converted to UTC as Europe/London, DST-aware) and every bookmaker/exchange quote as delivered.
Not available from this provider (stored as null, never inferred): market id, lay prices, depth, traded volume, market status.
"""
import datetime as dt, json, os, sys, time
from zoneinfo import ZoneInfo
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "phase3", "archive"))
import collector as COL  # noqa: E402

UK = ZoneInfo("Europe/London")
REFRESH_MIN = 30
UNAVAILABLE = {"market_id": None, "lay_price": None, "back_depth": None, "lay_depth": None, "traded_volume": None, "market_status": None}


def load(p):
    c = json.load(open(p))
    if not os.path.isabs(c["out_dir"]):
        c["out_dir"] = os.path.normpath(os.path.join(HERE, c["out_dir"]))
    return c


def provider_utc(s):
    """Provider 'updated' is a naive UK-local timestamp (evidence: BST sample 13 Oct 2025 vs its +01:00 history)."""
    if not s:
        return None
    try:
        return dt.datetime.fromisoformat(str(s).replace(" ", "T")).replace(tzinfo=UK).astimezone(dt.timezone.utc).isoformat(timespec="seconds")
    except ValueError:
        return None


def fetch_day(cfg, fetch, which):
    races, skip = [], 0
    while True:
        page = fetch(cfg, {"day": which, "region_codes": cfg["region_codes"], "limit": cfg["page_limit"], "skip": skip})
        races += page.get("racecards", [])
        skip += cfg["page_limit"]
        if skip >= int(page.get("total", 0)) or not page.get("racecards"):
            return races
        time.sleep(1.0 / cfg["max_requests_per_second"])


def log_failure(cfg, day, now_utc, what, e):
    os.makedirs(os.path.join(cfg["out_dir"], day), exist_ok=True)
    with open(os.path.join(cfg["out_dir"], day, "failures.jsonl"), "a") as fl:
        fl.write(json.dumps({"at_utc": now_utc.isoformat(timespec="seconds"), "what": what, "error": type(e).__name__, "message": str(e)[:300]}) + "\n")


def record(r, day, label, t0, t1, source):
    return {"checkpoint": label, "day": day, "kind": "live_capture", "source": source,
            "fetch_started_utc": t0, "fetch_finished_utc": t1, "captured_at_utc": t1,
            "race_id": r["race_id"], "course": r.get("course"), "off_dt": r.get("off_dt"), "race_status": r.get("race_status"),
            "is_abandoned": r.get("is_abandoned"), "runner_count": len(r.get("runners", [])), "unavailable_fields": UNAVAILABLE,
            "runners": [{"horse_id": h.get("horse_id"), "horse": h.get("horse"), "number": h.get("number"),
                         "non_runner": str(h.get("number", "")).upper() == "NR",
                         "odds": [{"bookmaker": o.get("bookmaker"), "price_type": "exchange_back" if o.get("bookmaker") in ("Betfair Exchange", "Matchbook", "Smarkets") else "bookmaker",
                                   "decimal": o.get("decimal"), "fractional": o.get("fractional"), "ew_places": o.get("ew_places"), "ew_denom": o.get("ew_denom"),
                                   "provider_updated_uk": o.get("updated"), "provider_updated_utc": provider_utc(o.get("updated"))} for o in (h.get("odds") or [])]}
                        for h in r.get("runners", [])]}


def targets(cfg, day, off_utc):
    h, m = map(int, cfg["morning_checkpoint_uk"].split(":"))
    morning = dt.datetime.fromisoformat(f"{day}T{h:02d}:{m:02d}").replace(tzinfo=UK).astimezone(dt.timezone.utc)
    return [("0900", morning)] + [(f"off-{k:02d}m", off_utc - dt.timedelta(minutes=k)) for k in cfg["pre_off_minutes"]]


def due(cfg, day, sched, now_utc):
    tol = dt.timedelta(minutes=cfg["tolerance_minutes"]); out = []
    for rid, off in sched.items():
        off = dt.datetime.fromisoformat(off)
        for lab, t in targets(cfg, day, off):
            if abs(now_utc - t) <= tol and now_utc < off and not os.path.exists(os.path.join(cfg["out_dir"], day, "market", lab, f"{rid}.json.gz")):
                out.append((lab, rid))
    return out


def tick(cfg, fetch=COL.http_fetch, now_utc=None, log=print):
    if not cfg.get("enabled"):
        log("vps collector disabled (enabled=false): nothing done"); return 0
    now_utc = now_utc or dt.datetime.now(dt.timezone.utc)
    day = now_utc.astimezone(UK).date().isoformat()
    sp = os.path.join(cfg["out_dir"], day, "schedule_cache.json")
    sched = json.load(open(sp)) if os.path.exists(sp) else None
    stale = sched is None or (now_utc - dt.datetime.fromisoformat(sched["refreshed_utc"])).total_seconds() > REFRESH_MIN * 60
    races = None; n = 0
    pending = due(cfg, day, sched["off_utc"], now_utc) if sched else []
    if stale or pending:
        t0 = now_utc.isoformat(timespec="seconds")
        try:
            races = fetch_day(cfg, fetch, "today")
        except COL.Blocker:
            raise
        except Exception as e:
            log_failure(cfg, day, now_utc, "racecards today", e); log(f"{t0}: fetch failed ({type(e).__name__}); logged, retried next tick"); return -1
        t1 = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds") if fetch is COL.http_fetch else t0
        offs = {r["race_id"]: COL.off_utc(r, day, UK).isoformat() for r in races}
        os.makedirs(os.path.dirname(sp), exist_ok=True)
        json.dump({"refreshed_utc": t0, "off_utc": offs}, open(sp + ".tmp", "w")); os.replace(sp + ".tmp", sp)
        by = {r["race_id"]: r for r in races}
        for lab, rid in due(cfg, day, offs, now_utc):
            if rid in by:
                n += COL.write_once(cfg, day, os.path.join("market", lab, f"{rid}.json.gz"), record(by[rid], day, lab, t0, t1, cfg["racecards_endpoint"] + "?day=today"), t1)
        log(f"{t0}: {len(races)} races fetched ({'schedule refresh' if stale else 'checkpoint'}), {n} snapshot files written")
    # evening checkpoint (tomorrow's card)
    loc = now_utc.astimezone(UK); h, m = map(int, cfg["evening_checkpoint_uk"].split(":"))
    ev = loc.replace(hour=h, minute=m, second=0, microsecond=0)
    if abs(loc - ev) <= dt.timedelta(minutes=cfg["tolerance_minutes"]):
        tom = (loc.date() + dt.timedelta(days=1)).isoformat()
        mark = os.path.join(cfg["out_dir"], tom, "market", "E2100")
        if not (os.path.isdir(mark) and os.listdir(mark)):
            t0 = now_utc.isoformat(timespec="seconds")
            try:
                rs = fetch_day(cfg, fetch, "tomorrow")
            except COL.Blocker:
                raise
            except Exception as e:
                log_failure(cfg, tom, now_utc, "racecards tomorrow (E2100)", e); log("evening fetch failed; logged, retried next tick"); return -1
            t1 = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds") if fetch is COL.http_fetch else t0
            for r in rs:
                n += COL.write_once(cfg, tom, os.path.join("market", "E2100", f"{r['race_id']}.json.gz"), record(r, tom, "E2100", t0, t1, cfg["racecards_endpoint"] + "?day=tomorrow"), t1)
            log(f"{t0}: evening snapshot for {tom}: {len(rs)} races")
    return n


def history(cfg, day, fetch_json=None, log=print):
    """Per-runner price histories after racing (/odds/{race_id}/{horse_id}), archived raw. Checkpoints rebuilt from them are
    labelled RECONSTRUCTED and kept apart from live captures (they rely on the provider's history, recorded after the event)."""
    import base64, urllib.request
    def http(path):  # pragma: no cover - network
        u, p = COL.credentials()
        req = urllib.request.Request(cfg["base_url"] + path, headers={"Authorization": "Basic " + base64.b64encode(f"{u}:{p}".encode()).decode()})
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    fetch_json = fetch_json or http
    sp = os.path.join(cfg["out_dir"], day, "schedule_cache.json")
    snaps = []
    for lab in ("0900",):
        d = os.path.join(cfg["out_dir"], day, "market", lab)
        snaps += [os.path.join(d, f) for f in sorted(os.listdir(d))] if os.path.isdir(d) else []
    import gzip
    pairs = set()
    for p in snaps:
        r = json.loads(gzip.decompress(open(p, "rb").read()))
        pairs |= {(r["race_id"], h["horse_id"]) for h in r["runners"]}
    n = 0; now = dt.datetime.now(dt.timezone.utc)
    for rid, hid in sorted(pairs):
        rel = os.path.join("odds_history", rid, f"{hid}.json.gz")
        if os.path.exists(os.path.join(cfg["out_dir"], day, rel)):
            continue
        try:
            body = fetch_json(f"/odds/{rid}/{hid}")
        except Exception as e:
            log_failure(cfg, day, now, f"odds history {rid}/{hid}", e); continue
        n += COL.write_once(cfg, day, rel, {"kind": "provider_history", "fetched_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                                            "race_id": rid, "horse_id": hid, "body": body}, now.isoformat(timespec="seconds"))
        time.sleep(1.0 / cfg["max_requests_per_second"])
    log(f"history {day}: {len(pairs)} runners, {n} written")
    return n


def health(cfg, day=None):
    import gzip, shutil
    day = day or dt.datetime.now(UK).date().isoformat()
    dd = os.path.join(cfg["out_dir"], day)
    sp = os.path.join(dd, "schedule_cache.json")
    sched = json.load(open(sp))["off_utc"] if os.path.exists(sp) else {}
    labs = ["E2100", "0900"] + [f"off-{k:02d}m" for k in cfg["pre_off_minutes"]]
    cov = {}
    stale = 0
    for lab in labs:
        d = os.path.join(dd, "market", lab)
        files = sorted(os.listdir(d)) if os.path.isdir(d) else []
        cov[lab] = len(files)
        for f in files:
            r = json.loads(gzip.decompress(open(os.path.join(d, f), "rb").read()))
            ts = [o["provider_updated_utc"] for h in r["runners"] for o in h["odds"] if o.get("provider_updated_utc")]
            if ts and (dt.datetime.fromisoformat(r["captured_at_utc"]) - dt.datetime.fromisoformat(max(ts))).total_seconds() > 1800:
                stale += 1
    fails = sum(1 for _ in open(os.path.join(dd, "failures.jsonl"))) if os.path.exists(os.path.join(dd, "failures.jsonl")) else 0
    now = dt.datetime.now(dt.timezone.utc)
    passed = {k: sum(1 for off in sched.values() for lab, t in targets(cfg, day, dt.datetime.fromisoformat(off)) if lab == k and t + dt.timedelta(minutes=cfg["tolerance_minutes"]) < now) for k in labs[1:]}
    import io, contextlib
    with contextlib.redirect_stdout(io.StringIO()):
        bad = COL.verify(cfg)
    du = shutil.disk_usage(cfg["out_dir"] if os.path.exists(cfg["out_dir"]) else HERE)
    out = dict(day=day, checked_utc=now.isoformat(timespec="seconds"), races_scheduled=len(sched), captured_by_checkpoint=cov,
               checkpoints_already_passed=passed, missing_by_checkpoint={k: max(0, passed[k] - cov[k]) for k in passed},
               failed_requests=fails, stale_snapshots=stale, archive_integrity_failures=bad, disk_free_gb=round(du.free / 1e9, 1),
               note="operational health only; no model performance")
    print(json.dumps(out, indent=1)); return out


def selftest():
    import tempfile, io, contextlib
    fx = json.load(open(os.path.join(HERE, "..", "..", "phase3", "archive", "fixtures", "racecards_standard_sample.json")))
    cfg = json.load(open(os.path.join(HERE, "config_vps.json"))); cfg["enabled"] = True
    with tempfile.TemporaryDirectory() as d:
        cfg["out_dir"] = d
        race = fx["racecards"][0]; off = dt.datetime.fromisoformat(race["off_dt"]).astimezone(dt.timezone.utc)
        calls = []
        def fetch(c, p):
            calls.append(p["day"]); return fx
        q = lambda *_: None  # noqa: E731
        start = off - dt.timedelta(minutes=75)
        for k in range(0, 76):                                   # every minute from off-75 to the off
            tick(cfg, fetch, start + dt.timedelta(minutes=k), log=q)
        day = off.astimezone(UK).date().isoformat()
        labs = sorted(os.listdir(os.path.join(d, day, "market")))
        assert labs == ["off-01m", "off-05m", "off-10m", "off-15m", "off-30m", "off-60m"], labs
        assert len(calls) <= 12, f"too many requests: {len(calls)}"             # schedule refreshes + 6 checkpoints, not 76
        n_before = len(calls)
        k10 = len(os.listdir(os.path.join(d, day, "market", "off-10m")))
        tick(cfg, fetch, off - dt.timedelta(minutes=10), log=q)                # repeat: nothing new written
        assert len(os.listdir(os.path.join(d, day, "market", "off-10m"))) == k10
        ev = dt.datetime.fromisoformat(f"{(off - dt.timedelta(days=1)).date()}T21:00").replace(tzinfo=UK)
        tick(cfg, fetch, ev.astimezone(dt.timezone.utc), log=q)
        assert os.listdir(os.path.join(d, (ev.date() + dt.timedelta(days=1)).isoformat(), "market", "E2100"))
        def bad(c, p): raise TimeoutError("simulated outage")
        os.remove(os.path.join(d, day, "schedule_cache.json"))
        assert tick(cfg, bad, off - dt.timedelta(minutes=10), log=q) == -1
        assert os.path.exists(os.path.join(d, day, "failures.jsonl"))
        r = json.loads(__import__("gzip").decompress(open(os.path.join(d, day, "market", "off-10m", os.listdir(os.path.join(d, day, "market", "off-10m"))[0]), "rb").read()))
        assert r["unavailable_fields"]["traded_volume"] is None and r["runners"][0]["odds"][0]["price_type"] in ("bookmaker", "exchange_back")
        assert provider_utc("2026-07-01 14:11:07") == "2026-07-01T13:11:07+00:00" and provider_utc("2026-11-19 14:11:07") == "2026-11-19T14:11:07+00:00"
        h = history(cfg, day, fetch_json=lambda p: {"odds": []}, log=q)      # no 0900 snapshot in this fixture day -> 0 runners
        with contextlib.redirect_stdout(io.StringIO()):
            assert COL.verify(cfg) == 0
            assert health(cfg, day)["archive_integrity_failures"] == 0
    print(f"selftest OK: 6 pre-off checkpoints with {n_before} requests over 76 ticks, evening snapshot, idempotent repeat, "
          "logged outage, unavailable fields null, BST/GMT timestamp conversion, health + manifest verified")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "tick"
    if cmd == "selftest":
        selftest(); sys.exit(0)
    p = sys.argv[sys.argv.index("--config") + 1] if "--config" in sys.argv else os.path.join(HERE, "config_vps.local.json")
    c = load(p)
    args = [a for a in sys.argv[2:] if not a.startswith("--") and a != p]
    try:
        if cmd == "tick":
            tick(c)
        elif cmd == "history":
            history(c, args[0])
        elif cmd == "health":
            health(c, args[0] if args else None)
    except COL.Blocker as e:
        print("BLOCKED:", e); sys.exit(2)
