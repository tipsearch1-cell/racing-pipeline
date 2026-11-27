"""Phase 5 forward shadow test: market capture via the Racing API connector, 09:00 frozen-model predictions,
audit ledger, verification, daily status and the sealed analysis. Research only: never touches production files.

  python3 fwd.py components DAY            # after the 08:35 build: market-independent parts of frozen D2/E for DAY's sealed card
  python3 fwd.py ingest CP FILE [--day D]  # archive a saved racecards response as a market snapshot (CP = E | M | SWEEP)
  python3 fwd.py predict0900 DAY           # frozen D2/E probabilities from the components + the 09:00 (M) snapshot
  python3 fwd.py stamp DAY                 # record GitHub's server-side push time for the current HEAD (provenance)
  python3 fwd.py settle DAY                # archive results/BSP from store/DAY/results_all.json.gz
  python3 fwd.py verify [DAY ...]          # integrity, timing, mapping, model-hash checks -> out/verify.json (exit 1 on failure)
  python3 fwd.py status DAY                # daily monitoring report (no outcome statistics) -> status/DAY.json + .md
  python3 fwd.py analyze --look K          # the sealed confirmatory analysis; refuses until look K's race count is reached

Spec: prereg/FORWARD_TEST_PHASE5_SPEC_2026-11-19.md. Files are written once into the Phase 3 archive layout
(research/market_intelligence/phase3/archive/archive_data/DAY/...) with the chained manifest.
"""
import argparse, datetime as dt, glob, gzip, hashlib, json, os, subprocess, sys, time
from zoneinfo import ZoneInfo
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
P4 = os.path.join(ROOT, "research", "model_reconstruction", "phase4")
ARCH = os.path.join(ROOT, "research", "market_intelligence", "phase3", "archive")
for p in (ARCH, P4, os.path.join(ROOT, "pipeline"), os.path.join(ROOT, "research", "harville")):
    sys.path.insert(0, p)
import collector as COL  # noqa: E402

UK = ZoneInfo("Europe/London")
EPS = 1e-9
FROZEN = os.path.join(P4, "models", "frozen_2026-11-19.pkl")
FROZEN_SHA = "56179d9cf676d7d02a2ceb4e0cb484896057a4e0a9fbf8fcb5333bcc87178b52"   # full hash, as recorded in frozen_2026-11-19.json
EXCHANGES = {"Betfair Exchange", "Matchbook", "Smarkets"}
M_WINDOW = ("09:00", "09:30")      # UK clock window for a valid 09:00 snapshot (spec)
STALE_MIN = 30                      # newest provider quote older than this at collection -> stale (spec)
LOOKS = [1000, 3200, 6400, 9600, 12800]
REPO = "tipsearch1-cell/racing-pipeline"


def cfg(out_dir=None):
    c = COL.load_config(os.path.join(ARCH, "config.json"))
    if out_dir:
        c["out_dir"] = out_dir
    return c


def now():
    return dt.datetime.now(dt.timezone.utc)


def iso(t):
    return t.astimezone(dt.timezone.utc).isoformat(timespec="seconds")


def read_gz(path):
    return json.loads(gzip.decompress(open(path, "rb").read()))


def sha_file(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def softmax_by(score, race):
    out = np.empty_like(score)
    for r in np.unique(race):
        i = race == r
        e = np.exp(score[i] - score[i].max()); out[i] = e / e.sum()
    return out


# ------------------------------------------------------------------ components (market-independent parts)
def components(day, out_dir=None):
    import pickle, shadow
    from p4_features import build
    sha = sha_file(FROZEN)
    if sha != FROZEN_SHA:
        raise SystemExit(f"FROZEN MODEL HASH MISMATCH: {sha} != {FROZEN_SHA}. Confirmatory test stopped; investigate, never refit.")
    fz = pickle.load(open(FROZEN, "rb"))
    extra, mkt = shadow.card_rows(day)
    T, _ = build(extra=extra, upto=day)
    feats = fz["meta"]["features"]
    T[feats] = T[feats].astype(float).fillna(0.0)
    T["jumps_f"] = T.type.isin(["Hurdle", "Chase", "NH Flat"]).astype(float)
    mp = json.load(open(os.path.join(ROOT, "store", day, "model.json")))
    T["f"] = [mp["races"].get(r, {}).get("runners", {}).get(h, {}).get("p", np.nan) for r, h in zip(T.race_id, T.horse_id)]
    T["m_seal"] = [mkt.get((r, h), np.nan) for r, h in zip(T.race_id, T.horse_id)]
    T = T.sort_values(["race_id", "horse_id"], kind="mergesort").reset_index(drop=True)
    X = T[feats + ["jumps_f"]].to_numpy(float)
    T["g_D2"] = fz["D2"].score(X)          # D2 score = log m + g(x); g does not depend on the market
    T["sC"] = fz["C"].score(X)
    from common import load_json
    sc = load_json(os.path.join(ROOT, "store", day, "sealed_card.json.gz"))
    hist_max = None
    try:
        from p4_features import load_hist
        H = load_hist(); hist_max = str(H[H.date < day].date.max())
    except Exception as e:  # pragma: no cover
        hist_max = f"unknown ({type(e).__name__})"
    rows = [dict(race_id=r, horse_id=h, g_D2=round(float(a), 8), sC=round(float(b), 8),
                 f=None if not np.isfinite(c) else round(float(c), 8), m_seal=None if not np.isfinite(d) else round(float(d), 8))
            for r, h, a, b, c, d in zip(T.race_id, T.horse_id, T.g_D2, T.sC, T.f, T.m_seal)]
    rec = dict(day=day, kind="components", created_utc=iso(now()), frozen_model_sha256=sha, E_weights=list(map(float, fz["wE"])),
               training_cutoff=fz["meta"]["training_cutoff"], history_max_date_used=hist_max,
               sealed_card_fetched_utc=sc.get("fetched_at_utc"), sealed_card_sha256=sha_file(os.path.join(ROOT, "store", day, "sealed_card.json.gz")),
               production_model_file_sha256=sha_file(os.path.join(ROOT, "store", day, "model.json")),
               races={r: dict(off_dt=x["off_dt"], n_card=len(x["runners"]), type=x.get("type"), course=x.get("course")) for x in sc["racecards"] for r in [x["race_id"]]},
               rows=rows, spec="prereg/FORWARD_TEST_PHASE5_SPEC_2026-11-19.md")
    ok = COL.write_once(cfg(out_dir), day, "phase5/components.json.gz", rec, rec["created_utc"])
    print(f"components {day}: {T.race_id.nunique()} races, {len(T)} runners, history to {hist_max}; written={ok}")
    return rec


# ------------------------------------------------------------------ snapshots
def normalise_snapshot(payload, checkpoint, collected):
    races = payload["racecards"] if isinstance(payload, dict) else payload
    out = []
    for r in races:
        runners = []
        for h in r.get("runners") or []:
            q = []
            for o in h.get("odds") or []:
                try:
                    dec = float(o.get("decimal"))
                except (TypeError, ValueError):
                    dec = None
                q.append(dict(bookmaker=o.get("bookmaker"), price_type="exchange_back" if o.get("bookmaker") in EXCHANGES else "bookmaker",
                              decimal=dec, fractional=o.get("fractional"), ew_places=o.get("ew_places"), ew_denom=o.get("ew_denom"),
                              provider_updated=o.get("updated")))
            runners.append(dict(horse_id=h.get("horse_id"), horse=h.get("horse"), number=h.get("number"),
                                non_runner=str(h.get("number", "")).upper() == "NR", quotes=q))
        out.append(dict(race_id=r.get("race_id"), market_id=None, course=r.get("course"), off_dt=r.get("off_dt"),
                        race_status=r.get("race_status"), is_abandoned=r.get("is_abandoned"), runners=runners))
    return out


def ingest(checkpoint, files, day=None, out_dir=None, collected_utc=None):
    """Archive saved racecards responses (the connector's saved tool results). Collection time = the file's save time
    (mtime) unless given. One snapshot file per (checkpoint, day, collection time); identical content is skipped."""
    assert checkpoint in ("E", "M", "SWEEP"), checkpoint
    c = cfg(out_dir); written = 0
    payload = {"racecards": []}
    for f in files:
        d = json.load(open(f))
        payload["racecards"] += d["racecards"] if isinstance(d, dict) else d
    collected = collected_utc or dt.datetime.fromtimestamp(max(os.path.getmtime(f) for f in files), dt.timezone.utc)
    races = normalise_snapshot(payload, checkpoint, collected)
    seen, uniq = set(), []
    for r in races:
        if r["race_id"] not in seen:
            seen.add(r["race_id"]); uniq.append(r)
    by_day = {}
    for r in uniq:
        d0 = dt.datetime.fromisoformat(r["off_dt"]).astimezone(UK).date().isoformat() if r.get("off_dt") else (day or "unknown")
        by_day.setdefault(day or d0, []).append(r)
    for d0, rs in by_day.items():
        rec = dict(day=d0, kind="market_snapshot", checkpoint=checkpoint, collected_utc=iso(collected),
                   collection_time_source="saved-response file time" if not collected_utc else "given",
                   source="The Racing API /racecards/standard via the Racing API connector (no market id, no lay side, no depth, no volume)",
                   source_files_sha256=sorted(sha_file(f) for f in files), price_types={"bookmaker": "bookmaker fixed odds",
                   "exchange_back": "best back price shown by the provider for Betfair Exchange / Matchbook / Smarkets (no lay, no depth)"},
                   races=rs)
        data = COL.gz_bytes(rec); h = hashlib.sha256(data).hexdigest()
        mf = os.path.join(c["out_dir"], d0, "manifest.jsonl")
        if os.path.exists(mf) and h in open(mf).read():
            print(f"ingest {checkpoint} {d0}: identical snapshot already archived (skipped)"); continue
        rel = f"phase5/snapshots/{checkpoint}/{collected.strftime('%Y%m%dT%H%M%SZ')}.json.gz"
        ok = COL.write_once(c, d0, rel, rec, rec["collected_utc"])
        written += ok
        print(f"ingest {checkpoint} {d0}: {len(rs)} races at {rec['collected_utc']} -> {rel} written={ok}")
    return written


def snapshots(day, checkpoint, out_dir=None):
    c = cfg(out_dir)
    return [(p, read_gz(p)) for p in sorted(glob.glob(os.path.join(c["out_dir"], day, "phase5", "snapshots", checkpoint, "*.json.gz")))]


def in_m_window(collected_iso, day):
    t = dt.datetime.fromisoformat(collected_iso).astimezone(UK)
    lo = dt.datetime.fromisoformat(f"{day}T{M_WINDOW[0]}").replace(tzinfo=UK)
    hi = dt.datetime.fromisoformat(f"{day}T{M_WINDOW[1]}").replace(tzinfo=UK)
    return lo <= t <= hi


def staleness_min(race, collected_iso):
    ts = [q["provider_updated"] for h in race["runners"] for q in h["quotes"] if q.get("provider_updated")]
    if not ts:
        return None
    newest = max(dt.datetime.fromisoformat(t.replace(" ", "T")).replace(tzinfo=UK) for t in ts)
    return round((dt.datetime.fromisoformat(collected_iso) - newest).total_seconds() / 60, 1)


def market_from_snapshot(race):
    """Production composite (0.6 exchange-mean + 0.4 / bookmaker median), normalised; NRs dropped. {horse_id: m} or None if any runner unpriced."""
    from common import race_market
    r = dict(runners=[dict(horse_id=h["horse_id"], odds=[dict(bookmaker=q["bookmaker"], decimal=q["decimal"]) for q in h["quotes"]])
                      for h in race["runners"] if not h["non_runner"]])
    mk = race_market(r)
    if not mk or any(v.get("mkt") is None for v in mk.values()):
        return None
    tot = sum(v["mkt"] for v in mk.values())
    return {k: v["mkt"] / tot for k, v in mk.items()}


# ------------------------------------------------------------------ 09:00 predictions
def predict0900(day, out_dir=None):
    c = cfg(out_dir)
    cp = os.path.join(c["out_dir"], day, "phase5", "components.json.gz")
    if not os.path.exists(cp):
        raise SystemExit(f"no components for {day}: run `fwd.py components {day}` first")
    comp = read_gz(cp)
    snaps = [(p, s) for p, s in snapshots(day, "M", out_dir) if in_m_window(s["collected_utc"], day)]
    ledger, rows = [], []
    if not snaps:
        rec = dict(day=day, kind="pred_0900", created_utc=iso(now()), status="NO VALID 09:00 SNAPSHOT",
                   note=f"no M snapshot collected inside {M_WINDOW[0]}-{M_WINDOW[1]} UK; every race is exploratory (seal-time shadow only)",
                   races=[dict(race_id=r, eligible=False, reason="no 09:00 snapshot in window") for r in comp["races"]], rows=[])
        COL.write_once(c, day, "phase5/pred_0900.json.gz", rec, rec["created_utc"])
        print(rec["note"]); return rec
    sp, snap = snaps[0]                                           # the earliest valid snapshot (spec)
    S = {r["race_id"]: r for r in snap["races"]}
    wE = np.array(comp["E_weights"])
    by_race = {}
    for x in comp["rows"]:
        by_race.setdefault(x["race_id"], []).append(x)
    for rid, rr in sorted(by_race.items()):
        reason, flags = None, []
        s = S.get(rid)
        if s is None:
            reason = "race missing from 09:00 snapshot"
        elif s.get("is_abandoned"):
            reason = "abandoned"
        else:
            st = staleness_min(s, snap["collected_utc"])
            if st is None or st > STALE_MIN:
                reason = f"stale or missing provider quotes ({st} min)"
            snap_ids = {h["horse_id"]: h for h in s["runners"]}
            comp_ids = {x["horse_id"] for x in rr}
            added = [h for h, v in snap_ids.items() if h not in comp_ids and not v["non_runner"]]
            missing = [h for h in comp_ids if h not in snap_ids]
            if added:
                reason = reason or f"runner(s) added after seal: {added}"
            if missing:
                reason = reason or f"mapping error: card runners absent from snapshot {missing}"
            nr = [x["horse_id"] for x in rr if x["horse_id"] in snap_ids and snap_ids[x["horse_id"]]["non_runner"]]
            if nr:
                flags.append(f"non-runner(s) since seal: {len(nr)}")
            m = None if reason else market_from_snapshot(s)
            if not reason and m is None:
                reason = "a runner has no 09:00 price"
            if not reason and any(x["f"] is None for x in rr):
                reason = "production model chance missing"
            if not reason:
                keep = [x for x in rr if x["horse_id"] not in nr]
                if len(keep) < 2:
                    reason = "fewer than 2 runners"
        if reason:
            ledger.append(dict(race_id=rid, eligible=False, reason=reason, flags=flags)); continue
        ids = [x["horse_id"] for x in keep]
        mm = np.array([m[h] for h in ids]); mm = mm / mm.sum()
        f = np.array([x["f"] for x in keep]); f = f / f.sum()
        lm, lf = np.log(np.clip(mm, EPS, 1)), np.log(np.clip(f, EPS, 1))
        g = np.array([x["g_D2"] for x in keep]); sC = np.array([x["sC"] for x in keep])
        pD2 = np.exp(lm + g - (lm + g).max()); pD2 /= pD2.sum()
        zE = np.c_[lm, sC, lf] @ wE; pE = np.exp(zE - zE.max()); pE /= pE.sum()
        for h, a, b, d2, e in zip(ids, mm, f, pD2, pE):
            rows.append(dict(race_id=rid, horse_id=h, m_0900=round(float(a), 8), p_existing=round(float(b), 8), p_D2=round(float(d2), 8), p_E=round(float(e), 8)))
        ledger.append(dict(race_id=rid, eligible=True, reason=None, flags=flags))
    rec = dict(day=day, kind="pred_0900", created_utc=iso(now()), status="OK", frozen_model_sha256=comp["frozen_model_sha256"],
               components_sha256=sha_file(cp), snapshot_file=os.path.relpath(sp, c["out_dir"]), snapshot_sha256=sha_file(sp),
               snapshot_collected_utc=snap["collected_utc"], races=ledger, rows=rows,
               spec="prereg/FORWARD_TEST_PHASE5_SPEC_2026-11-19.md")
    ok = COL.write_once(c, day, "phase5/pred_0900.json.gz", rec, rec["created_utc"])
    ne = sum(x["eligible"] for x in ledger)
    print(f"pred_0900 {day}: {ne}/{len(ledger)} races eligible, snapshot {snap['collected_utc']}; written={ok}")
    return rec


# ------------------------------------------------------------------ exploratory X1 (evening) - never confirmatory
def x1(day, out_dir=None):
    c = cfg(out_dir)
    comp = read_gz(os.path.join(c["out_dir"], day, "phase5", "components.json.gz"))
    w = np.array(json.load(open(os.path.join(HERE, "models", "x1_evening_2026-11-19.json")))["weights"])
    ev = snapshots(day, "E", out_dir)
    if not ev:
        print(f"x1 {day}: no evening snapshot"); return None
    sp, snap = ev[0]
    S = {r["race_id"]: r for r in snap["races"]}
    by = {}
    for x in comp["rows"]:
        by.setdefault(x["race_id"], []).append(x)
    rows, led = [], []
    for rid, rr in sorted(by.items()):
        s = S.get(rid)
        m = market_from_snapshot(s) if s else None
        keep = [x for x in rr if m and x["horse_id"] in m and x["f"] is not None]
        if not m or len(keep) != len([h for h in s["runners"] if not h["non_runner"]]) or len(keep) < 2:
            led.append(dict(race_id=rid, ok=False)); continue
        mm = np.array([m[x["horse_id"]] for x in keep]); mm /= mm.sum()
        f = np.array([x["f"] for x in keep]); f /= f.sum()
        z = np.c_[np.log(np.clip(mm, EPS, 1)), [x["sC"] for x in keep], np.log(np.clip(f, EPS, 1))] @ w
        p = np.exp(z - z.max()); p /= p.sum()
        rows += [dict(race_id=rid, horse_id=x["horse_id"], m_E=round(float(a), 8), p_X1=round(float(b), 8)) for x, a, b in zip(keep, mm, p)]
        led.append(dict(race_id=rid, ok=True))
    rec = dict(day=day, kind="x1_evening", status="EXPLORATORY", created_utc=iso(now()), snapshot_file=os.path.relpath(sp, c["out_dir"]),
               snapshot_collected_utc=snap["collected_utc"], note="components come from the 08:35 card (decision-time approximation)", races=led, rows=rows)
    ok = COL.write_once(c, day, "phase5/x1_evening.json.gz", rec, rec["created_utc"])
    print(f"x1 {day}: {sum(x['ok'] for x in led)}/{len(led)} races; written={ok}")
    return rec


# ------------------------------------------------------------------ exploratory CLV / execution (spec section 9)
def clv(out_dir=None, comm=0.02, ev_min=0.04):
    """Selections: E at 09:00 with EV >= 4% at the 09:00 Betfair Exchange back quote (2% commission). Closing = BSP, plus the
    last pre-off sweep quote when one exists. Conditional fill scenarios only; no depth data. Writes out/clv_forward.csv."""
    import pandas as pd
    c = cfg(out_dir); rows = []
    for day in sorted(d for d in os.listdir(c["out_dir"]) if d[:2] == "20" and d >= "2026-11-20"):
        dd = os.path.join(c["out_dir"], day)
        pp, rp = os.path.join(dd, "phase5", "pred_0900.json.gz"), os.path.join(dd, "results.json.gz")
        if not (os.path.exists(pp) and os.path.exists(rp)):
            continue
        pred = read_gz(pp)
        if pred.get("status") != "OK":
            continue
        snap = read_gz(os.path.join(dd, pred["snapshot_file"]))
        bf = {(r["race_id"], h["horse_id"]): q["decimal"] for r in snap["races"] for h in r["runners"] for q in h["quotes"] if q["bookmaker"] == "Betfair Exchange"}
        sweeps = snapshots(day, "SWEEP", out_dir)
        res = {(r["race_id"], h["horse_id"]): h for r in read_gz(rp)["results"] for h in r["runners"]}
        bp = os.path.join(dd, "phase5", "results_bsp.json.gz")
        sup = read_gz(bp)["bsp"] if os.path.exists(bp) else {}
        offs = {r["race_id"]: x["off_dt"] for x in [read_gz(os.path.join(dd, "phase5", "components.json.gz"))] for r in [dict(race_id=k, **v) for k, v in x["races"].items()]}
        for x in pred["rows"]:
            k = (x["race_id"], x["horse_id"]); q = bf.get(k); h = res.get(k)
            if not q or not h or str(h.get("position", "")).upper() in ("NR", ""):
                continue
            last = None
            for _, s in sweeps:
                if s["collected_utc"] < offs.get(x["race_id"], ""):
                    for r in s["races"]:
                        if r["race_id"] == x["race_id"]:
                            for hh in r["runners"]:
                                if hh["horse_id"] == x["horse_id"]:
                                    last = next((qq["decimal"] for qq in hh["quotes"] if qq["bookmaker"] == "Betfair Exchange"), last)
            raw = h.get("bsp") or sup.get(x["race_id"], {}).get(x["horse_id"])
            bsp = float(raw) if str(raw or "").replace(".", "", 1).isdigit() else None
            rows.append(dict(day=day, race_id=x["race_id"], horse_id=x["horse_id"], p_E=x["p_E"], m_0900=x["m_0900"], quote_0900=q,
                             price_type="exchange_back (provider, no depth)", last_sweep_quote=last, bsp=bsp, won=int(str(h.get("position")) == "1"),
                             ev=x["p_E"] * (1 + (q - 1) * (1 - comm)) - 1))
    D = pd.DataFrame(rows)
    if not len(D):
        print("no settled forward days with 09:00 predictions yet"); return D
    S = D[D.ev >= ev_min].copy()
    S["clv_abs"] = np.log(S.quote_0900 / S.bsp); S["beat_bsp"] = S.clv_abs > 0
    S["ret_quote"] = np.where(S.won == 1, (S.quote_0900 - 1) * (1 - comm), -1.0)
    S["ret_bsp"] = np.where(S.won == 1, (S.bsp - 1) * (1 - comm), -1.0)
    S["adverse_fill"] = S.bsp >= S.quote_0900
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    S.to_csv(os.path.join(HERE, "out", "clv_forward.csv"), index=False)
    print(S[["clv_abs", "beat_bsp", "ret_quote", "ret_bsp", "adverse_fill"]].mean().round(4).to_dict(), len(S), "selections (EXPLORATORY, conditional)")
    return S


# ------------------------------------------------------------------ provenance
def gh_pushes(pages=3):
    out = []
    for pg in range(1, pages + 1):
        try:
            r = subprocess.run(["gh", "api", f"repos/{REPO}/activity?per_page=100&page={pg}"], capture_output=True, text=True, timeout=40)
            items = json.loads(r.stdout or "[]")
        except Exception:
            return out
        if not isinstance(items, list) or not items:
            break
        out += [dict(at=i["timestamp"], before=i.get("before"), after=i.get("after"), ref=i.get("ref")) for i in items if i.get("activity_type") == "push"]
    return out


def stamp(day, out_dir=None):
    head = subprocess.run(["git", "-C", ROOT, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    hit = []
    for _ in range(12):  # the activity API can lag a push by a few seconds (27 Nov: stamp ran 1 s after the push and saw none)
        hit = [p for p in gh_pushes(1) if p["after"] == head]
        if hit:
            break
        time.sleep(10)
    files = {os.path.basename(p): sha_file(p) for p in glob.glob(os.path.join(cfg(out_dir)["out_dir"], day, "phase5", "*.json.gz"))}
    rec = dict(day=day, kind="push_stamp", head=head, github_push_utc=hit[0]["at"] if hit else None, files_at_head=files,
               recorded_utc=iso(now()), note="GitHub server-side push time from the repository activity API" if hit else "push not found in GitHub activity (not pushed yet?)")
    rel = f"phase5/stamps/{head[:12]}.json.gz"
    ok = COL.write_once(cfg(out_dir), day, rel, rec, rec["recorded_utc"])
    print(f"stamp {day}: HEAD {head[:12]} pushed {rec['github_push_utc']}; written={ok}")
    return rec


def settle(day, out_dir=None):
    from common import load_json
    p = os.path.join(ROOT, "store", day, "results_all.json.gz")
    if not os.path.exists(p):
        raise SystemExit(f"no results for {day} yet")
    ok = COL.settle(cfg(out_dir), day, load_json(p))
    print(f"settle {day}: written={ok}")


def bsp_supplement(day, out_dir=None):
    """BSP published after the write-once settle: archive it once as phase5/results_bsp.json.gz (never rewrites results.json.gz).
    Used only by exploratory CLV/execution; the primary metric needs winners only."""
    from common import load_json
    c = cfg(out_dir); p = os.path.join(ROOT, "store", day, "results_all.json.gz")
    res = load_json(p)["results"]
    b = {r["race_id"]: {h["horse_id"]: h.get("bsp") for h in r["runners"] if h.get("bsp") not in (None, "", "-")} for r in res}
    n = sum(len(v) for v in b.values())
    rec = dict(day=day, kind="bsp_supplement", created_utc=iso(now()), source="store/DAY/results_all.json.gz (Racing API results)",
               runners_with_bsp=n, runners=sum(len(r["runners"]) for r in res), bsp=b)
    ok = COL.write_once(c, day, "phase5/results_bsp.json.gz", rec, rec["created_utc"])
    print(f"bsp {day}: {n}/{rec['runners']} runners with BSP; written={ok}")


# ------------------------------------------------------------------ ledger / verify / status
def race_ledger(day, out_dir=None, pushes=None):
    """One row per sealed-card race: confirmatory eligibility and reasons. Uses no outcome except 'settled' (one winner)."""
    c = cfg(out_dir); dd = os.path.join(c["out_dir"], day, "phase5")
    rows = []
    comp = read_gz(os.path.join(dd, "components.json.gz")) if os.path.exists(os.path.join(dd, "components.json.gz")) else None
    pred = read_gz(os.path.join(dd, "pred_0900.json.gz")) if os.path.exists(os.path.join(dd, "pred_0900.json.gz")) else None
    stamps = [read_gz(p) for p in sorted(glob.glob(os.path.join(dd, "stamps", "*.json.gz")))]
    pred_sha = sha_file(os.path.join(dd, "pred_0900.json.gz")) if pred else None
    pushed = sorted(s["github_push_utc"] for s in stamps if s.get("github_push_utc") and pred_sha in s.get("files_at_head", {}).values())
    first_push = pushed[0] if pushed else None
    res_p = os.path.join(c["out_dir"], day, "results.json.gz")
    res = {r["race_id"]: r for r in read_gz(res_p)["results"]} if os.path.exists(res_p) else {}
    sealed = os.path.join(ROOT, "store", day, "sealed_card.json.gz")
    races = comp["races"] if comp else {}
    if not races and os.path.exists(sealed):
        from common import load_json
        races = {r["race_id"]: dict(off_dt=r["off_dt"]) for r in load_json(sealed)["racecards"]}
    pl = {x["race_id"]: x for x in (pred or {}).get("races", [])}
    for rid, info in sorted(races.items()):
        reasons = []
        if comp is None:
            reasons.append("no components")
        elif comp["frozen_model_sha256"] != FROZEN_SHA:
            reasons.append("model hash mismatch")
        if pred is None:
            reasons.append("no 09:00 prediction file")
        elif not pl.get(rid, {}).get("eligible"):
            reasons.append(pl.get(rid, {}).get("reason") or "not in 09:00 prediction file")
        if pred and pred.get("status") == "OK":
            if first_push is None:
                reasons.append("no GitHub push stamp for the prediction file")
            elif first_push > dt.datetime.fromisoformat(info["off_dt"]).astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z"):
                reasons.append("prediction pushed after the off")
        r = res.get(rid)
        settled = None
        if r is None:
            settled = "no result yet"
        else:
            nw = sum(1 for h in r["runners"] if str(h.get("position")) == "1")
            settled = "ok" if nw == 1 else f"{nw} winners (void/dead-heat)"
        rows.append(dict(day=day, race_id=rid, off_dt=info["off_dt"], confirmatory=not reasons and settled == "ok",
                         reasons=reasons, settled=settled, flags=pl.get(rid, {}).get("flags", []), pushed_utc=first_push))
    return rows


def verify(days=None, out_dir=None):
    c = cfg(out_dir)
    base = c["out_dir"]
    days = days or sorted(d for d in os.listdir(base) if d[:2] == "20" and d >= "2026-11-20")
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        chain_bad = COL.verify(c)
    rep = dict(checked_utc=iso(now()), archive_integrity_failures=chain_bad, archive_integrity_detail=[l for l in buf.getvalue().splitlines() if "verify:" not in l],
               frozen_model_sha256_ok=sha_file(FROZEN) == FROZEN_SHA, days={})
    tot = dict(races=0, eligible_0900=0, confirmatory_settled=0, timestamp_violations=0, mapping_errors=0, model_hash_discrepancies=0,
               missing_E=0, missing_M=0, duplicate_snapshots=0)
    for day in days:
        try:
            led = race_ledger(day, out_dir)
        except Exception as e:   # an unreadable / corrupted file is an integrity failure, reported, never skipped silently
            rep["days"][day] = dict(error=f"{type(e).__name__}: {e}"); rep.setdefault("unreadable_days", []).append(day)
            continue
        dd = os.path.join(base, day, "phase5")
        comp_ok = os.path.exists(os.path.join(dd, "components.json.gz"))
        snapsM = snapshots(day, "M", out_dir); snapsE = snapshots(day, "E", out_dir); sw = snapshots(day, "SWEEP", out_dir)
        validM = [s for _, s in snapsM if in_m_window(s["collected_utc"], day)]
        dup = 0
        for lab, ss in (("M", snapsM), ("E", snapsE)):
            seen = set()
            for _, s in ss:
                for r in s["races"]:
                    dup += r["race_id"] in seen; seen.add(r["race_id"])
        pred = read_gz(os.path.join(dd, "pred_0900.json.gz")) if os.path.exists(os.path.join(dd, "pred_0900.json.gz")) else None
        hashbad = int(bool(pred and pred.get("frozen_model_sha256") not in (None, FROZEN_SHA)))
        if comp_ok and read_gz(os.path.join(dd, "components.json.gz"))["frozen_model_sha256"] != FROZEN_SHA:
            hashbad += 1
        tv = sum(1 for x in led if "prediction pushed after the off" in x["reasons"] or "no GitHub push stamp for the prediction file" in x["reasons"])
        mapping = sum(1 for x in led if any("mapping error" in r or "added after seal" in r for r in x["reasons"]))
        n_e = len({r["race_id"] for _, s in snapsE for r in s["races"]})
        d = dict(races=len(led), components=comp_ok, snapshots_M=len(snapsM), snapshots_M_in_window=len(validM),
                 snapshots_E=len(snapsE), races_in_E=n_e, snapshots_SWEEP=len(sw), eligible_0900=sum(1 for x in led if not x["reasons"]),
                 confirmatory_settled=sum(x["confirmatory"] for x in led), timestamp_violations=tv, mapping_errors=mapping,
                 model_hash_discrepancies=hashbad, duplicate_snapshot_races=dup,
                 reasons={}, )
        for x in led:
            for r in x["reasons"]:
                k = r.split(": ")[0]; d["reasons"][k] = d["reasons"].get(k, 0) + 1
        rep["days"][day] = d
        tot["races"] += d["races"]; tot["eligible_0900"] += d["eligible_0900"]; tot["confirmatory_settled"] += d["confirmatory_settled"]
        tot["timestamp_violations"] += tv; tot["mapping_errors"] += mapping; tot["model_hash_discrepancies"] += hashbad
        tot["missing_E"] += int(n_e == 0); tot["missing_M"] += int(not validM); tot["duplicate_snapshots"] += dup
    rep["totals"] = tot
    rep["ok"] = not rep.get("unreadable_days") and chain_bad == 0 and rep["frozen_model_sha256_ok"] and tot["model_hash_discrepancies"] == 0
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    if out_dir is None:
        json.dump(rep, open(os.path.join(HERE, "out", "verify.json"), "w"), indent=1)
    print(json.dumps(dict(ok=rep["ok"], archive_integrity_failures=chain_bad, frozen_model_sha256_ok=rep["frozen_model_sha256_ok"], **tot), indent=1))
    return rep


def status(day, out_dir=None):
    rep = verify([day], out_dir)
    allrep = verify(None, out_dir) if out_dir is None else rep
    d = rep["days"].get(day, {})
    pred = os.path.join(cfg(out_dir)["out_dir"], day, "phase5", "pred_0900.json.gz")
    pr = read_gz(pred) if os.path.exists(pred) else {"rows": []}
    s = dict(day=day, generated_utc=iso(now()), eligible_races_processed=d.get("eligible_0900", 0), races_on_card=d.get("races", 0),
             model_E_predictions=len({x["race_id"] for x in pr["rows"]}), model_D2_predictions=len({x["race_id"] for x in pr["rows"]}),
             capture_0900=d.get("snapshots_M_in_window", 0) > 0, capture_evening_races=d.get("races_in_E", 0), sweep_snapshots=d.get("snapshots_SWEEP", 0),
             archive_verification="OK" if rep["archive_integrity_failures"] == 0 else f"{rep['archive_integrity_failures']} FAILURES",
             model_hash_ok=rep["frozen_model_sha256_ok"] and d.get("model_hash_discrepancies", 0) == 0,
             timestamp_violations=d.get("timestamp_violations", 0), mapping_errors=d.get("mapping_errors", 0),
             exclusion_reasons=d.get("reasons", {}), valid_prospective_races_to_date=allrep["totals"]["confirmatory_settled"],
             next_look=next((L for L in LOOKS if L > allrep["totals"]["confirmatory_settled"]), None),
             note="No outcome statistics are computed before a pre-registered look (spec).")
    os.makedirs(os.path.join(HERE, "status"), exist_ok=True)
    if out_dir is None:
        json.dump(s, open(os.path.join(HERE, "status", f"{day}.json"), "w"), indent=1)
        md = [f"# Forward-test status {day}", "", "| Item | Value |", "|---|---|"] + [f"| {k} | {v} |" for k, v in s.items() if k not in ("day",)]
        open(os.path.join(HERE, "status", f"{day}.md"), "w").write("\n".join(md) + "\n")
    print(json.dumps(s, indent=1))
    return s


# ------------------------------------------------------------------ sealed analysis
def load_confirmatory(out_dir=None):
    import pandas as pd
    c = cfg(out_dir); out = []
    for day in sorted(d for d in os.listdir(c["out_dir"]) if d[:2] == "20" and d >= "2026-11-20"):
        led = {x["race_id"]: x for x in race_ledger(day, out_dir) if x["confirmatory"]}
        if not led:
            continue
        pred = read_gz(os.path.join(c["out_dir"], day, "phase5", "pred_0900.json.gz"))
        res = {r["race_id"]: r for r in read_gz(os.path.join(c["out_dir"], day, "results.json.gz"))["results"]}
        for rid in led:
            ran = {h["horse_id"]: h for h in res[rid]["runners"] if str(h.get("position", "")).upper() not in ("NR", "")}
            rows = [x for x in pred["rows"] if x["race_id"] == rid and x["horse_id"] in ran]
            for x in rows:
                out.append(dict(x, day=day, type=(read_gz(os.path.join(c["out_dir"], day, "phase5", "components.json.gz"))["races"].get(rid, {}).get("type")), y=int(str(ran[x["horse_id"]].get("position")) == "1"), bsp=ran[x["horse_id"]].get("bsp")))
    D = pd.DataFrame(out)
    if len(D):
        D = D[D.groupby("race_id").y.transform("sum") == 1]
        for col in ("m_0900", "p_E", "p_D2", "p_existing"):     # same runner list for every model: renormalise over runners that ran
            D[col] = D[col] / D.groupby("race_id")[col].transform("sum")
    return D


def paired_stats(D, col, draws=10000, seed=20261120):
    w = D[D.y == 1]
    x = (np.log(w[col].clip(EPS)) - np.log(w.m_0900.clip(EPS))).to_numpy()
    days = w.day.to_numpy(); ud = np.unique(days)
    sums = np.array([x[days == d].sum() for d in ud]); m = np.array([(days == d).sum() for d in ud])
    mu = sums.sum() / m.sum(); k = len(ud)
    se = np.sqrt(k / (k - 1) * ((sums - mu * m) ** 2).sum()) / m.sum()
    rng = np.random.default_rng(seed); bs = []
    for _ in range(draws):
        j = rng.integers(k, size=k); bs.append(sums[j].sum() / m[j].sum())
    lo, hi = np.percentile(bs, [1.25, 98.75])
    return dict(races=len(x), days=k, mean_gain=float(mu), se=float(se), z=float(mu / se) if se > 0 else 0.0, ci97_5=[float(lo), float(hi)])


def analyze(look, out_dir=None, D=None, force_n=None):
    D = load_confirmatory(out_dir) if D is None else D
    n = D.race_id.nunique() if len(D) else 0
    need = force_n or LOOKS[look - 1]
    if n < need:
        print(f"look {look} not reached: {n} confirmatory settled races < {need}. No outcome statistics computed.")
        return None
    crit = json.load(open(os.path.join(HERE, "out", "power.json")))["obf_critical_z"][look - 1]
    out = dict(look=look, races=n, critical_z=crit, models={})
    for col in ("p_E", "p_D2"):
        s = paired_stats(D, col)
        s["crosses_boundary"] = bool(crit is not None and s["z"] > crit)
        out["models"][col] = s
    out["secondary"] = secondary(D)
    json.dump(out, open(os.path.join(HERE, "out", f"analysis_look{look}.json"), "w"), indent=1, default=float)
    print(json.dumps(out["models"], indent=1))
    return out


def secondary(D):
    import pandas as pd
    res = {}
    for col in ("m_0900", "p_E", "p_D2", "p_existing"):
        g = D.groupby("race_id")
        ll = -np.log(D[D.y == 1][col].clip(EPS)).mean()
        brier = ((D[col] - D.y) ** 2).groupby(D.race_id).sum().mean()
        top = D.loc[g[col].idxmax()].y.mean()
        rank = D.assign(r=g[col].rank(ascending=False))[D.y == 1].r.mean()
        conc = []
        for _, r in D.groupby("race_id"):
            pw = r.loc[r.y == 1, col].iloc[0]; pl = r.loc[r.y == 0, col]
            conc.append(((pw > pl).sum() + 0.5 * (pw == pl).sum()) / max(len(pl), 1))
        bands = pd.cut(D[col], [0, .05, .1, .2, .35, .6, 1])
        cal = D.groupby(bands, observed=True).agg(pred=(col, "mean"), obs=("y", "mean"), n=("y", "size"))
        res[col] = dict(log_loss=float(ll), brier=float(brier), top_pick_win=float(top), winner_mean_rank=float(rank),
                        concordance=float(np.mean(conc)), calibration={str(k): v for k, v in cal.round(4).to_dict("index").items()})
    w = D[D.y == 1].copy()
    w["fs"] = D.groupby("race_id").race_id.transform("size")[D.y == 1]
    w["ob"] = pd.cut(1 / w.m_0900, [1, 3, 6, 11, 21, 1e9]).astype(str)
    w["fsb"] = pd.cut(w.fs, [0, 7, 11, 15, 99]).astype(str)
    for col in ("p_E", "p_D2"):
        w["g"] = np.log(w[col].clip(EPS)) - np.log(w.m_0900.clip(EPS))
        res[f"{col}_gain_by_winner_odds_band"] = w.groupby("ob").g.agg(["mean", "size"]).round(5).to_dict("index")
        res[f"{col}_gain_by_field_size"] = w.groupby("fsb").g.agg(["mean", "size"]).round(5).to_dict("index")
        if "type" in w:
            res[f"{col}_gain_by_type"] = w.groupby("type").g.agg(["mean", "size"]).round(5).to_dict("index")
    return res


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["components", "x1", "clv", "bsp", "ingest", "predict0900", "stamp", "settle", "verify", "status", "analyze"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--day"); ap.add_argument("--look", type=int)
    a = ap.parse_args(argv)
    if a.cmd == "components":
        components(a.args[0])
    elif a.cmd == "bsp":
        bsp_supplement(a.args[0])
    elif a.cmd == "clv":
        clv()
    elif a.cmd == "x1":
        x1(a.args[0])
    elif a.cmd == "ingest":
        ingest(a.args[0], a.args[1:], day=a.day)
    elif a.cmd == "predict0900":
        predict0900(a.args[0])
    elif a.cmd == "stamp":
        stamp(a.args[0])
    elif a.cmd == "settle":
        settle(a.args[0])
    elif a.cmd == "verify":
        sys.exit(0 if verify(a.args or None)["ok"] else 1)
    elif a.cmd == "status":
        status(a.args[0])
    elif a.cmd == "analyze":
        analyze(a.look)


if __name__ == "__main__":
    main()
