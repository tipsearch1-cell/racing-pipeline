"""Forward market-intelligence archive (Phase 3). DISABLED BY DEFAULT - see ../FORWARD_ARCHIVE.md.

Commands
  python3 collector.py tick [--config config.json]        # run every minute (cron); takes due market snapshots
  python3 collector.py predictions DAY [--config ...]     # archive our model's chances for DAY (from store/DAY/model.json)
  python3 collector.py settle DAY RESULTS_JSON [--config]  # archive BSP + positions after racing (Racing API results JSON)
  python3 collector.py verify [--config ...]              # re-hash every archived file against the manifest

Design
  * Snapshots: one /racecards/standard request (paged) per due checkpoint, never per runner -> 1-2 requests per tick.
    Checkpoints: 09:00 UK, and off-60/-30/-15/-5/-1 minutes for each race. A checkpoint is "due" inside +-tolerance
    of its time and only if its file does not exist yet (idempotent, resumable: state = files on disk).
  * Files: <out>/<day>/market/<checkpoint>/<race_id>.json.gz (deterministic gzip), each with captured_at_utc,
    request params (never credentials), and the race's runners with every bookmaker/exchange price as delivered.
  * manifest.jsonl per day: one line per file with sha256, size, captured_at_utc -> auditable; `verify` re-checks.
  * Never touches production files; reads store/DAY/model.json read-only for predictions.
  * Credentials: RACING_API_USERNAME / RACING_API_PASSWORD from the environment only. Missing -> exits with the
    blocker message; values are never printed, logged or written.
"""
import argparse, datetime as dt, gzip, hashlib, io, json, os, subprocess, sys, time
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))


class Blocker(Exception):
    pass


def load_config(path):
    cfg = json.load(open(path))
    cfg["out_dir"] = cfg["out_dir"] if os.path.isabs(cfg["out_dir"]) else os.path.join(HERE, cfg["out_dir"])
    return cfg


def credentials():
    u, p = os.environ.get("RACING_API_USERNAME"), os.environ.get("RACING_API_PASSWORD")
    if not u or not p:
        raise Blocker("RACING_API_USERNAME / RACING_API_PASSWORD are not set in this environment (values never logged).")
    return u, p


def http_fetch(cfg, params):  # pragma: no cover - network; replaced by a fixture fetcher in tests
    import base64, urllib.parse, urllib.request
    u, p = credentials()
    url = cfg["base_url"] + cfg["racecards_endpoint"] + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": "Basic " + base64.b64encode(f"{u}:{p}".encode()).decode()})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def gz_bytes(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", mtime=0) as g:
        g.write(raw)
    return buf.getvalue()


def write_once(cfg, day, rel, obj, captured_at):
    """Write <out>/<day>/<rel> only if absent; append to manifest. Returns True if written."""
    path = os.path.join(cfg["out_dir"], day, rel)
    if os.path.exists(path):
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = gz_bytes(obj)
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)
    with open(os.path.join(cfg["out_dir"], day, "manifest.jsonl"), "a") as m:
        m.write(json.dumps({"file": rel, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "captured_at_utc": captured_at}) + "\n")
    return True


def off_utc(race, day, tz):
    """Racecard off_dt if present, else off_time (UK clock, 12h with afternoon racing) on DAY."""
    if race.get("off_dt"):
        return dt.datetime.fromisoformat(race["off_dt"]).astimezone(dt.timezone.utc)
    hh, mm = map(int, str(race["off_time"]).split(":"))
    if hh < 10:
        hh += 12
    return dt.datetime.fromisoformat(f"{day}T{hh:02d}:{mm:02d}").replace(tzinfo=tz).astimezone(dt.timezone.utc)


def due_checkpoints(cfg, races, day, now_utc):
    """[(checkpoint_label, race)] that are due now and not yet archived."""
    tz = ZoneInfo(cfg["timezone"])
    tol = dt.timedelta(minutes=cfg["tolerance_minutes"])
    h, m = map(int, cfg["morning_checkpoint_uk"].split(":"))
    morning = dt.datetime.fromisoformat(f"{day}T{h:02d}:{m:02d}").replace(tzinfo=tz).astimezone(dt.timezone.utc)
    out = []
    for r in races:
        off = off_utc(r, day, tz)
        targets = [("0900", morning)] + [(f"off-{k:02d}m", off - dt.timedelta(minutes=k)) for k in cfg["pre_off_minutes"]]
        for lab, t in targets:
            if abs(now_utc - t) <= tol and now_utc < off and not os.path.exists(os.path.join(cfg["out_dir"], day, "market", lab, f"{r['race_id']}.json.gz")):
                out.append((lab, r))
    return out


def fetch_all(cfg, fetch):
    races, skip = [], 0
    while True:
        page = fetch(cfg, {"day": "today", "region_codes": cfg["region_codes"], "limit": cfg["page_limit"], "skip": skip})
        races += page.get("racecards", [])
        skip += cfg["page_limit"]
        if skip >= int(page.get("total", 0)) or not page.get("racecards"):
            return races
        time.sleep(1.0 / cfg["max_requests_per_second"])


def tick(cfg, fetch=http_fetch, now_utc=None, log=print):
    if not cfg.get("enabled"):
        log("archive disabled (config enabled=false): nothing done")
        return 0
    now_utc = now_utc or dt.datetime.now(dt.timezone.utc)
    day = now_utc.astimezone(ZoneInfo(cfg["timezone"])).date().isoformat()
    races = fetch_all(cfg, fetch)
    captured = now_utc.isoformat(timespec="seconds")
    n = 0
    for lab, r in due_checkpoints(cfg, races, day, now_utc):
        rec = {"captured_at_utc": captured, "checkpoint": lab, "day": day, "source": cfg["racecards_endpoint"],
               "race_id": r["race_id"], "course": r.get("course"), "off_time": r.get("off_time"), "off_dt": r.get("off_dt"),
               "runners": [{"horse_id": h.get("horse_id"), "horse": h.get("horse"), "number": h.get("number"),
                            "odds": [{k: o.get(k) for k in ("bookmaker", "decimal", "fractional", "ew_places", "ew_denom", "updated")} for o in (h.get("odds") or [])]}
                           for h in r.get("runners", [])]}
        n += write_once(cfg, day, os.path.join("market", lab, f"{r['race_id']}.json.gz"), rec, captured)
    log(f"{captured}: {len(races)} races fetched, {n} snapshot files written")
    return n


def git_info(path, first=False):
    """(commit, commit time) of the latest commit touching path, or of the commit that first added it (first=True)."""
    try:
        args = ["git", "-C", ROOT, "log", "--format=%H %cI"] + (["--diff-filter=A"] if first else ["-1"]) + ["--", path]
        lines = subprocess.run(args, capture_output=True, text=True, timeout=20).stdout.strip().splitlines()
        return lines[-1].split(" ") if lines else (None, None)
    except Exception:
        return None, None


def predictions(cfg, day, params_path=None, store=None):
    """Archive our model's chances for DAY with provenance. Calibrated / blended chances use the Phase 3 final params."""
    import numpy as np
    store = store or os.path.join(ROOT, "store")
    mp = os.path.join(store, day, "model.json")
    model = json.load(open(mp))
    wm = json.load(open(os.path.join(ROOT, "models", "win_model.json")))
    prm = json.load(open(params_path or os.path.join(HERE, "..", "out", "params.json")))["final"]
    commit, commit_time = git_info(os.path.relpath(mp, ROOT), first=True)   # first commit = when the prediction became fixed
    mcommit, _ = git_info("models/win_model.json")
    mkt = {}
    sc = os.path.join(store, day, "sealed_card.json.gz")
    if os.path.exists(sc):
        sys.path.insert(0, os.path.join(ROOT, "pipeline"))
        from common import load_json, race_market
        card = load_json(sc)
        for r in (card["racecards"] if isinstance(card, dict) else card):
            for hid, x in race_market(r).items():
                mkt[(r["race_id"], hid)] = (x.get("mkt") or np.nan) / 100
    rows = []
    for rid, r in model["races"].items():
        ids = list(r["runners"])
        f = np.array([r["runners"][h]["p"] for h in ids], float); f = f / f.sum()
        a = prm["a"][0]; fc = f ** a; fc /= fc.sum()
        m = np.array([mkt.get((rid, h), np.nan) for h in ids], float)
        if np.isfinite(m).all() and m.sum() > 0:
            m = m / m.sum(); w = prm["w_M"]; b = np.exp(w[0] * np.log(np.clip(m, 1e-6, 1)) + w[1] * np.log(np.clip(f, 1e-6, 1))); b /= b.sum()
        else:
            b = np.full(len(ids), np.nan)
        for i, h in enumerate(ids):
            rows.append({"race_id": rid, "horse_id": h, "p_model": round(float(f[i]), 6), "p_calibrated": round(float(fc[i]), 6),
                         "p_blend_0900": None if not np.isfinite(b[i]) else round(float(b[i]), 6), "m_0900": None if not np.isfinite(m[i]) else round(float(m[i]), 6)})
    rec = {"day": day, "model_version": mcommit, "model_training_cutoff": wm.get("trained"), "prediction_file": os.path.relpath(mp, ROOT),
           "prediction_commit": commit, "prediction_timestamp_utc": commit_time, "calibration_params": "phase3 out/params.json final",
           "category": "A-verified" if commit_time else "C-unverified (no git timestamp)", "rows": rows}
    return write_once(cfg, day, "predictions.json.gz", rec, dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))


def settle(cfg, day, results):
    rows = [{"race_id": r["race_id"], "off_dt": r.get("off_dt"), "non_runners": r.get("non_runners"),
             "runners": [{k: h.get(k) for k in ("horse_id", "position", "bsp", "sp_dec")} for h in r.get("runners", [])]} for r in results.get("results", [])]
    return write_once(cfg, day, "results.json.gz", {"day": day, "results": rows}, dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"))


def verify(cfg):
    bad = 0
    for day in sorted(os.listdir(cfg["out_dir"])) if os.path.isdir(cfg["out_dir"]) else []:
        mf = os.path.join(cfg["out_dir"], day, "manifest.jsonl")
        for line in open(mf) if os.path.exists(mf) else []:
            e = json.loads(line)
            data = open(os.path.join(cfg["out_dir"], day, e["file"]), "rb").read()
            if hashlib.sha256(data).hexdigest() != e["sha256"]:
                bad += 1; print("HASH MISMATCH", day, e["file"])
    print("verify:", "OK" if not bad else f"{bad} mismatches")
    return bad


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["tick", "predictions", "settle", "verify"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--config", default=os.path.join(HERE, "config.json"))
    a = ap.parse_args(argv)
    cfg = load_config(a.config)
    try:
        if a.cmd == "tick":
            tick(cfg)
        elif a.cmd == "predictions":
            print("written" if predictions(cfg, a.args[0]) else "already archived")
        elif a.cmd == "settle":
            print("written" if settle(cfg, a.args[0], json.load(open(a.args[1]))) else "already archived")
        else:
            sys.exit(1 if verify(cfg) else 0)
    except Blocker as e:
        print("BLOCKED:", e)
        sys.exit(2)


if __name__ == "__main__":
    main()
