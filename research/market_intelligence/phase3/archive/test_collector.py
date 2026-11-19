"""Tests for the forward archive (fixtures only; no network).  python3 -m pytest -q research/market_intelligence/phase3/archive"""
import copy, datetime as dt, json, os, sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import collector as C  # noqa: E402

FIX = json.load(open(os.path.join(HERE, "fixtures", "racecards_standard_sample.json")))


def cfg(tmp_path, enabled=True):
    c = json.load(open(os.path.join(HERE, "config.json")))
    c["enabled"] = enabled
    c["out_dir"] = str(tmp_path / "arch")
    return c


def fake_fetch(calls):
    def f(cfg, params):
        calls.append(params)
        return copy.deepcopy(FIX)
    return f


def utc(s):
    return dt.datetime.fromisoformat(s).astimezone(dt.timezone.utc)


def test_disabled_by_default_and_does_nothing(tmp_path):
    assert json.load(open(os.path.join(HERE, "config.json")))["enabled"] is False
    calls = []
    assert C.tick(cfg(tmp_path, enabled=False), fetch=fake_fetch(calls), log=lambda s: None) == 0
    assert calls == [] and not os.path.exists(tmp_path / "arch")


def test_morning_snapshot_written_once(tmp_path):
    c, calls = cfg(tmp_path), []
    now = utc("2026-11-19T09:01:00+00:00")
    assert C.tick(c, fetch=fake_fetch(calls), now_utc=now, log=lambda s: None) == 3
    assert C.tick(c, fetch=fake_fetch(calls), now_utc=now, log=lambda s: None) == 0       # idempotent
    man = [json.loads(l) for l in open(tmp_path / "arch" / "2026-11-19" / "manifest.jsonl")]
    assert len(man) == 3 and len({m["file"] for m in man}) == 3
    rec = C.json.loads(C.gzip.decompress(open(tmp_path / "arch" / "2026-11-19" / man[0]["file"], "rb").read()))
    assert rec["checkpoint"] == "0900" and rec["captured_at_utc"].startswith("2026-11-19T09:01")
    assert all("odds" in r for r in rec["runners"])


def test_pre_off_checkpoints(tmp_path):
    c = cfg(tmp_path)
    r = FIX["racecards"][0]
    off = dt.datetime.fromisoformat(r["off_dt"]).astimezone(dt.timezone.utc)
    for k in (60, 30, 15, 5, 1):
        due = C.due_checkpoints(c, [r], "2026-11-19", off - dt.timedelta(minutes=k))
        assert (f"off-{k:02d}m", r) in due
    assert C.due_checkpoints(c, [r], "2026-11-19", off - dt.timedelta(minutes=45)) == []   # between checkpoints
    assert C.due_checkpoints(c, [r], "2026-11-19", off + dt.timedelta(minutes=1)) == []    # never after the off


def test_resumable_after_partial_failure(tmp_path):
    c = cfg(tmp_path)
    now = utc("2026-11-19T09:00:30+00:00")
    races = FIX["racecards"]
    lab, r0 = C.due_checkpoints(c, races, "2026-11-19", now)[0]
    C.write_once(c, "2026-11-19", os.path.join("market", lab, f"{r0['race_id']}.json.gz"), {"x": 1}, "t")   # simulate a crash after 1 file
    assert C.tick(c, fetch=fake_fetch([]), now_utc=now, log=lambda s: None) == 2


def test_credentials_never_exposed(monkeypatch, capsys):
    monkeypatch.setenv("RACING_API_USERNAME", "SECRET_USER_X")
    monkeypatch.delenv("RACING_API_PASSWORD", raising=False)
    with pytest.raises(C.Blocker) as e:
        C.credentials()
    assert "SECRET_USER_X" not in str(e.value)
    assert "SECRET_USER_X" not in json.dumps(json.load(open(os.path.join(HERE, "config.json"))))


def test_verify_detects_tampering(tmp_path):
    c = cfg(tmp_path)
    C.tick(c, fetch=fake_fetch([]), now_utc=utc("2026-11-19T09:00:00+00:00"), log=lambda s: None)
    assert C.verify(c) == 0
    f = next((tmp_path / "arch" / "2026-11-19" / "market" / "0900").iterdir())
    f.write_bytes(f.read_bytes() + b"x")
    assert C.verify(c) == 1


def test_paging(tmp_path):
    c = cfg(tmp_path); c["page_limit"] = 2; c["max_requests_per_second"] = 1000
    pages = []
    def f(cfg, params):
        pages.append(params["skip"])
        rc = FIX["racecards"][params["skip"]:params["skip"] + 2]
        return {"racecards": rc, "total": 3}
    assert len(C.fetch_all(c, f)) == 3 and pages == [0, 2]


@pytest.mark.skipif(not os.path.exists(os.path.join(C.ROOT, "store", "2026-11-18", "model.json")), reason="store not restored")
def test_predictions_archive_real_day(tmp_path):
    c = cfg(tmp_path)
    assert C.predictions(c, "2026-11-18") is True
    assert C.predictions(c, "2026-11-18") is False
    rec = json.loads(C.gzip.decompress(open(tmp_path / "arch" / "2026-11-18" / "predictions.json.gz", "rb").read()))
    assert rec["model_training_cutoff"] == "history to 2026-11-09"
    by = {}
    for r in rec["rows"]:
        by.setdefault(r["race_id"], []).append(r["p_model"])
    assert all(abs(sum(v) - 1) < 1e-3 for v in by.values())
