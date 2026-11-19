"""Phase 5 forward-test tests (synthetic archives in a temp dir; no network, no production files touched)."""
import datetime as dt, gzip, json, os, sys
import numpy as np, pandas as pd, pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fwd  # noqa: E402

DAY = "2026-12-01"
UTC = dt.timezone.utc


def quotes(dec, upd="2026-12-01 09:04:00"):
    return [{"bookmaker": b, "decimal": str(dec), "fractional": "x", "ew_places": "3", "ew_denom": "5", "updated": upd}
            for b in ("Bet365", "William Hill", "Betfair Exchange")]


def card(runners=("h1", "h2", "h3"), prices=(2.0, 3.0, 6.0), nr=(), upd="2026-12-01 09:04:00", race="r1", off="2026-12-01T13:00:00+00:00"):
    return {"racecards": [{"race_id": race, "course": "X", "off_dt": off, "race_status": "declared", "is_abandoned": False,
                           "runners": [{"horse_id": h, "horse": h, "number": "NR" if h in nr else str(i + 1), "odds": quotes(p, upd)}
                                       for i, (h, p) in enumerate(zip(runners, prices))]}]}


def comp(tmp, runners=("h1", "h2", "h3"), race="r1", sha=fwd.FROZEN_SHA, off="2026-12-01T13:00:00+00:00"):
    rows = [dict(race_id=race, horse_id=h, g_D2=0.1 * i, sC=0.2 * i, f=1 / len(runners), m_seal=1 / len(runners)) for i, h in enumerate(runners)]
    rec = dict(day=DAY, kind="components", created_utc="2026-12-01T08:45:00+00:00", frozen_model_sha256=sha, E_weights=[1.0, 0.05, 0.05],
               races={race: dict(off_dt=off, n_card=len(runners))}, rows=rows)
    fwd.COL.write_once(fwd.cfg(str(tmp)), DAY, "phase5/components.json.gz", rec, rec["created_utc"])


def snap(tmp, c, at, cp="M"):
    p = tmp / f"c{at.strftime('%H%M%S')}.json"; p.write_text(json.dumps(c))
    return fwd.ingest(cp, [str(p)], out_dir=str(tmp), collected_utc=at)


def test_ingest_idempotent_and_price_types(tmp_path):
    t = dt.datetime(2026, 12, 1, 9, 5, tzinfo=UTC)
    assert snap(tmp_path, card(), t) == 1
    assert snap(tmp_path, card(), t) == 0                      # identical content -> no duplicate record
    (_, s), = fwd.snapshots(DAY, "M", str(tmp_path))
    q = s["races"][0]["runners"][0]["quotes"]
    assert {x["price_type"] for x in q} == {"bookmaker", "exchange_back"}
    assert s["collected_utc"] == "2026-12-01T09:05:00+00:00"


def test_window():
    assert fwd.in_m_window("2026-12-01T09:05:00+00:00", DAY)
    assert not fwd.in_m_window("2026-12-01T08:59:00+00:00", DAY)
    assert not fwd.in_m_window("2026-12-01T09:31:00+00:00", DAY)
    assert fwd.in_m_window("2026-07-01T08:10:00+00:00", "2026-07-01")   # BST: 09:10 UK


def test_predict_matches_formula(tmp_path):
    comp(tmp_path); snap(tmp_path, card(), dt.datetime(2026, 12, 1, 9, 5, tzinfo=UTC))
    r = fwd.predict0900(DAY, out_dir=str(tmp_path))
    assert all(x["eligible"] for x in r["races"])
    m = np.array([x["m_0900"] for x in r["rows"]]); pD2 = np.array([x["p_D2"] for x in r["rows"]])
    exp = m * np.exp([0.0, 0.1, 0.2]); exp /= exp.sum()
    assert np.allclose(pD2, exp, atol=1e-7)
    assert abs(sum(x["p_E"] for x in r["rows"]) - 1) < 1e-6
    assert fwd.predict0900(DAY, out_dir=str(tmp_path))["created_utc"]   # second run computes but cannot overwrite
    assert len(open(tmp_path / DAY / "manifest.jsonl").read().splitlines()) == 3


def test_non_runner_dropped_and_flagged(tmp_path):
    comp(tmp_path); snap(tmp_path, card(nr=("h2",)), dt.datetime(2026, 12, 1, 9, 5, tzinfo=UTC))
    r = fwd.predict0900(DAY, out_dir=str(tmp_path))
    assert r["races"][0]["eligible"] and r["races"][0]["flags"]
    assert {x["horse_id"] for x in r["rows"]} == {"h1", "h3"}
    assert abs(sum(x["p_E"] for x in r["rows"]) - 1) < 1e-6


@pytest.mark.parametrize("kw,reason", [
    (dict(runners=("h1", "h2", "h3", "h4"), prices=(2, 3, 6, 9)), "added after seal"),
    (dict(runners=("h1", "h2"), prices=(2, 3)), "mapping error"),
    (dict(upd="2026-12-01 08:00:00"), "stale"),
    (dict(race="r9"), "missing from 09:00 snapshot"),
])
def test_ineligible_reasons(tmp_path, kw, reason):
    comp(tmp_path); snap(tmp_path, card(**kw), dt.datetime(2026, 12, 1, 9, 5, tzinfo=UTC))
    r = fwd.predict0900(DAY, out_dir=str(tmp_path))
    x = [x for x in r["races"] if x["race_id"] == "r1"][0]
    assert not x["eligible"] and reason in x["reason"]


def test_no_valid_snapshot(tmp_path):
    comp(tmp_path); snap(tmp_path, card(), dt.datetime(2026, 12, 1, 9, 45, tzinfo=UTC))
    r = fwd.predict0900(DAY, out_dir=str(tmp_path))
    assert r["status"] == "NO VALID 09:00 SNAPSHOT" and not r["rows"]


def stamp_rec(tmp, at):
    sha = fwd.sha_file(tmp / DAY / "phase5" / "pred_0900.json.gz")
    rec = dict(day=DAY, kind="push_stamp", head="abc", github_push_utc=at, files_at_head={"pred_0900.json.gz": sha}, recorded_utc=at)
    fwd.COL.write_once(fwd.cfg(str(tmp)), DAY, f"phase5/stamps/{at[11:19].replace(':', '')}.json.gz", rec, at)


def settle(tmp, winner="h1"):
    res = {"results": [{"race_id": "r1", "runners": [{"horse_id": h, "position": "1" if h == winner else "2"} for h in ("h1", "h2", "h3")]}]}
    fwd.COL.settle(fwd.cfg(str(tmp)), DAY, res)


def test_ledger_timing(tmp_path):
    comp(tmp_path); snap(tmp_path, card(), dt.datetime(2026, 12, 1, 9, 5, tzinfo=UTC)); fwd.predict0900(DAY, out_dir=str(tmp_path))
    led = fwd.race_ledger(DAY, str(tmp_path))
    assert "no GitHub push stamp for the prediction file" in led[0]["reasons"]
    stamp_rec(tmp_path, "2026-12-01T13:30:00Z")
    assert "prediction pushed after the off" in fwd.race_ledger(DAY, str(tmp_path))[0]["reasons"]


def test_ledger_confirmatory(tmp_path):
    comp(tmp_path); snap(tmp_path, card(), dt.datetime(2026, 12, 1, 9, 5, tzinfo=UTC)); fwd.predict0900(DAY, out_dir=str(tmp_path))
    stamp_rec(tmp_path, "2026-12-01T09:20:00Z")
    assert fwd.race_ledger(DAY, str(tmp_path))[0]["settled"] == "no result yet"
    settle(tmp_path)
    x = fwd.race_ledger(DAY, str(tmp_path))[0]
    assert x["confirmatory"] and not x["reasons"]


def test_hash_mismatch_detected(tmp_path):
    comp(tmp_path, sha="0" * 64)
    assert "model hash mismatch" in fwd.race_ledger(DAY, str(tmp_path))[0]["reasons"]
    rep = fwd.verify([DAY], out_dir=str(tmp_path))
    assert rep["totals"]["model_hash_discrepancies"] >= 1 and not rep["ok"]


def test_tamper_detected(tmp_path):
    comp(tmp_path); snap(tmp_path, card(), dt.datetime(2026, 12, 1, 9, 5, tzinfo=UTC))
    f = tmp_path / DAY / "phase5" / "components.json.gz"
    data = bytearray(f.read_bytes()); data[-5] ^= 1; f.write_bytes(bytes(data))
    assert fwd.verify([DAY], out_dir=str(tmp_path))["archive_integrity_failures"] >= 1


def test_analyze_refuses_before_look(tmp_path):
    D = pd.DataFrame(dict(race_id=["a", "a"], day=[DAY] * 2, y=[1, 0], m_0900=[.5, .5], p_E=[.6, .4], p_D2=[.5, .5], p_existing=[.5, .5]))
    assert fwd.analyze(1, out_dir=str(tmp_path), D=D) is None


def test_paired_stats_null_and_shift():
    rng = np.random.default_rng(1); rows = []
    for d in range(60):
        for r in range(30):
            m = rng.dirichlet(np.ones(8)); w = rng.choice(8, p=m)
            for i in range(8):
                rows.append(dict(day=f"d{d}", race_id=f"{d}-{r}", y=int(i == w), m_0900=m[i], p_E=m[i], p_D2=m[i]))
    D = pd.DataFrame(rows)
    s = fwd.paired_stats(D, "p_E", draws=200)
    assert abs(s["mean_gain"]) < 1e-12 and s["races"] == 1800
