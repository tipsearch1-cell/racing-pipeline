"""Tests for Phase 2 helpers.  python3 -m pytest -q research/harville/phase2/test_phase2.py"""
import os, sys
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run2  # noqa: E402
from replay import runner_features  # noqa: E402
from data import bf_places  # noqa: E402


def race(m, f, pos, n_nr=0, hcap=False):
    n = len(m)
    df = pd.DataFrame(dict(race_id="r1", date="2026-06-01", m=m, f=f, pos=pos, hcap=hcap, nnr=n_nr, code="Flat",
                           psp=np.full(n, 3.0), placed_bf=np.nan, horse=[f"h{i}" for i in range(n)]))
    return run2.build_races(df, "m", "f")[0]


def test_blend_identity_and_normalisation():
    r = race([0.5, 0.3, 0.2], [0.2, 0.3, 0.5], [1, 2, 3])
    assert np.allclose(run2.blend(r, np.array([1.0, 0.0])), r["m"])
    assert np.allclose(run2.blend(r, np.array([0.0, 1.0])), r["f"])
    b = run2.blend(r, np.array([0.7, 0.4]))
    assert np.isclose(b.sum(), 1) and np.all(b > 0)


def test_declared_places():
    r = race([0.2] * 7, [0.2] * 7, [1, 2, 3, 4, 5, 6, 7], n_nr=1)   # 7 ran + 1 NR = 8 declared -> 3 places
    assert r["places"] == 3
    r = race([0.1] * 15, [0.1] * 15, list(range(1, 16)), n_nr=1, hcap=True)  # 16 declared handicap -> 4
    assert r["places"] == 4
    assert bf_places(4, False) == 0


def test_dead_heat_split():
    frac = run2.settle_frac(np.array([1, 2, 3, 3, 5.0]), 3)
    assert np.allclose(frac, [1, 1, 0.5, 0.5, 0])
    assert np.isclose(frac.sum(), 3)


def test_runner_features_use_only_earlier_runs():
    H = pd.DataFrame(dict(hkey="x", date=["2026-01-01", "2026-02-01", "2026-03-01"], race_key=["a", "b", "c"], pos=["1", "5", "2"], n=[5, 5, 5],
                          comment=["made all", "held up", "led"], ovr_btn=[None, None, None], going=["Good"] * 3, cls=["Class 4"] * 3, dist_f=[8, 8, 12]))
    F = runner_features(H)
    assert np.isnan(F.f_top3.iloc[0])                 # first run: nothing earlier
    assert F.f_top3.iloc[1] == 1.0                    # only the win before it
    assert F.f_top3.iloc[2] == 0.5                    # win + 5th, not its own 2nd
    assert F.f_dist.iloc[1] == 1.0 and np.isnan(F.f_dist.iloc[2])   # 12f today: no earlier run within 1f


def test_probs_are_valid_distributions():
    r = race([0.4, 0.25, 0.15, 0.1, 0.06, 0.04], [0.3, 0.3, 0.1, 0.1, 0.1, 0.1], [1, 2, 3, 4, 5, 6])
    prm = {"w": np.array([1.0, 0.1])}
    for m in ("A", "B", "C"):
        prm[f"{m}2"] = np.array([0.9, 0.1]); prm[f"{m}3"] = np.array([0.75, 0.2])
    prm["D2"] = np.r_[0.9, 0.1, np.zeros(len(run2.D_NAMES) - 2)]; prm["D3"] = np.r_[0.75, 0.2, np.zeros(len(run2.D_NAMES) - 2)]
    R, U = run2.score([r], prm)
    for m in ("H", "A", "B", "C", "D"):
        assert np.isclose(U[f"Pk_{m}"].sum(), r["places"])
        assert np.isclose(U[f"P2_{m}"].sum(), 1) and np.isclose(U[f"P3_{m}"].sum(), 1)
