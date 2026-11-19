"""Phase 5 VPS market collector: the Phase 3 collector with the Phase 5 checkpoint set. Research only, disabled by default.

  python3 vps_collect.py tick [--config config_vps.local.json]   # cron every minute
  python3 vps_collect.py selftest                                  # offline test with the bundled fixture

Checkpoints: 21:00 UK the evening before (day=tomorrow request, stored under the race day as market/E2100/),
09:00 UK (market/0900/), and off-60/-30/-15/-10/-5/-1 minutes (market/off-NNm/). One paged /racecards/standard request per
tick that has something due (about 1-3 requests per minute at most while racing, 0 otherwise). Same write-once files and
chained manifest as Phase 3; a failed fetch is logged to failures.jsonl and retried on the next tick (state = files on disk).
Each file stores captured_at_utc (VPS clock, NTP), the provider's per-quote 'updated' time, request parameters (never
credentials), and every bookmaker/exchange quote as delivered. No lay side, depth or volume exists in this API.
"""
import datetime as dt, json, os, sys
from zoneinfo import ZoneInfo
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "phase3", "archive"))
import collector as COL  # noqa: E402


def evening_due(cfg, now_utc):
    tz = ZoneInfo(cfg["timezone"]); local = now_utc.astimezone(tz)
    h, m = map(int, cfg["evening_checkpoint_uk"].split(":"))
    t = local.replace(hour=h, minute=m, second=0, microsecond=0)
    return abs(local - t) <= dt.timedelta(minutes=cfg["tolerance_minutes"]), (local.date() + dt.timedelta(days=1)).isoformat()


def tick(cfg, fetch=COL.http_fetch, now_utc=None, log=print):
    if not cfg.get("enabled"):
        log("vps collector disabled (enabled=false): nothing done"); return 0
    now_utc = now_utc or dt.datetime.now(dt.timezone.utc)
    n = COL.tick(cfg, fetch=fetch, now_utc=now_utc, log=log)        # 09:00 + pre-off checkpoints (today)
    due, tomorrow = evening_due(cfg, now_utc)
    if due:
        mark = os.path.join(cfg["out_dir"], tomorrow, "market", "E2100")
        if not os.path.isdir(mark) or not os.listdir(mark):
            try:
                races, skip = [], 0
                while True:
                    page = fetch(cfg, {"day": "tomorrow", "region_codes": cfg["region_codes"], "limit": cfg["page_limit"], "skip": skip})
                    races += page.get("racecards", []); skip += cfg["page_limit"]
                    if skip >= int(page.get("total", 0)) or not page.get("racecards"):
                        break
            except COL.Blocker:
                raise
            except Exception as e:
                os.makedirs(os.path.join(cfg["out_dir"], tomorrow), exist_ok=True)
                with open(os.path.join(cfg["out_dir"], tomorrow, "failures.jsonl"), "a") as fl:
                    fl.write(json.dumps({"at_utc": now_utc.isoformat(timespec="seconds"), "checkpoint": "E2100", "error": type(e).__name__, "message": str(e)[:300]}) + "\n")
                log(f"evening fetch failed ({type(e).__name__}); logged, retried next tick"); return -1
            cap = now_utc.isoformat(timespec="seconds")
            for r in races:
                rec = {"captured_at_utc": cap, "checkpoint": "E2100", "day": tomorrow, "source": cfg["racecards_endpoint"] + "?day=tomorrow",
                       "race_id": r["race_id"], "course": r.get("course"), "off_dt": r.get("off_dt"), "runner_count": len(r.get("runners", [])),
                       "runners": [{"horse_id": h.get("horse_id"), "horse": h.get("horse"), "number": h.get("number"),
                                    "odds": [{k: o.get(k) for k in ("bookmaker", "decimal", "fractional", "ew_places", "ew_denom", "updated")} for o in (h.get("odds") or [])]}
                                   for h in r.get("runners", [])]}
                n += COL.write_once(cfg, tomorrow, os.path.join("market", "E2100", f"{r['race_id']}.json.gz"), rec, cap)
            log(f"{cap}: evening snapshot for {tomorrow}: {len(races)} races")
    return n


def selftest():
    import tempfile
    fx = json.load(open(os.path.join(HERE, "..", "..", "phase3", "archive", "fixtures", "racecards_standard_sample.json")))
    cfg = json.load(open(os.path.join(HERE, "config_vps.json"))); cfg["enabled"] = True
    with tempfile.TemporaryDirectory() as d:
        cfg["out_dir"] = d
        race = fx["racecards"][0]; off = dt.datetime.fromisoformat(race["off_dt"]).astimezone(dt.timezone.utc)
        fetch = lambda c, p: fx                                          # noqa: E731
        for k in (60, 30, 15, 10, 5, 1):
            tick(cfg, fetch, off - dt.timedelta(minutes=k), log=lambda *_: None)
        tick(cfg, fetch, off - dt.timedelta(minutes=10), log=lambda *_: None)   # repeat: no duplicate
        day = off.astimezone(ZoneInfo("Europe/London")).date().isoformat()
        labs = sorted(os.listdir(os.path.join(d, day, "market")))
        assert labs == ["off-01m", "off-05m", "off-10m", "off-15m", "off-30m", "off-60m"], labs
        ev = dt.datetime.fromisoformat(f"{(off - dt.timedelta(days=1)).date()}T21:00").replace(tzinfo=ZoneInfo("Europe/London"))
        tick(cfg, fetch, ev.astimezone(dt.timezone.utc), log=lambda *_: None)
        assert os.listdir(os.path.join(d, (ev.date() + dt.timedelta(days=1)).isoformat(), "market", "E2100"))
        def bad(c, p): raise TimeoutError("simulated outage")
        assert tick(cfg, bad, off - dt.timedelta(minutes=10), log=lambda *_: None) == -1
        cfg2 = dict(cfg); 
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            assert COL.verify(cfg2) == 0
    print("selftest OK: 6 pre-off checkpoints, evening snapshot, idempotent repeat, logged outage, manifest verified")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "tick"
    if cmd == "selftest":
        selftest()
    else:
        p = sys.argv[sys.argv.index("--config") + 1] if "--config" in sys.argv else os.path.join(HERE, "config_vps.local.json")
        c = json.load(open(p))
        c["out_dir"] = c["out_dir"] if os.path.isabs(c["out_dir"]) else os.path.normpath(os.path.join(HERE, c["out_dir"]))
        try:
            tick(c)
        except COL.Blocker as e:
            print("BLOCKED:", e); sys.exit(2)
