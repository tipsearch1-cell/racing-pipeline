"""Tests for Phase 4 algorithms.  python3 -m pytest -q research/model_reconstruction/phase4/test_p4.py"""
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p4_models as P  # noqa: E402

rng = np.random.default_rng(1)


def synth(nr=600, n=8, k=4):
    race = np.repeat(np.arange(nr), n)
    X = rng.normal(size=(nr * n, k))
    beta = np.array([1.0, -0.5, 0.0, 0.3])
    s = X @ beta
    st, gid = P.groups(race)
    p = P.softmax_g(s, st, gid)
    y = np.zeros(nr * n); pos = np.full(nr * n, np.nan)
    for r in range(nr):
        idx = np.arange(r * n, r * n + n)
        order = rng.choice(idx, n, replace=False, p=p[idx])
        y[order[0]] = 1; pos[order] = np.arange(1, n + 1)
    return X, y, pos, race, beta, p


def test_softmax_sums_to_one():
    X, y, pos, race, beta, p = synth(50)
    st, gid = P.groups(race)
    assert np.allclose(np.add.reduceat(p, st), 1)


def test_clogit_recovers_coefficients():
    X, y, pos, race, beta, p = synth(3000)
    w = P.clogit_fit(X, y, race, l2=0.0)
    assert np.allclose(w, beta, atol=0.12)


def test_offset_with_zero_correction_recovers_market():
    X, y, pos, race, beta, p = synth(200)
    st, gid = P.groups(race)
    off = np.log(p)
    m = P.ListwiseGBM(n_max=0).fit(X, y, race, offset=off)
    assert np.allclose(P.softmax_g(m.score(X, offset=off), st, gid), p)


def test_listwise_and_pairwise_learn_signal():
    X, y, pos, race, beta, p = synth(1500)
    st, gid = P.groups(race)
    base = P.race_ll(np.full(len(y), 1 / 8), y, st)
    lw = P.ListwiseGBM(depth=2, lr=0.1, n_max=60, min_leaf=50).fit(X, y, race)
    assert P.race_ll(P.softmax_g(lw.score(X), st, gid), y, st) < base - 0.1
    pw = P.PairwiseGBM(depth=2, lr=0.1, n_max=40, min_leaf=50).fit(X, pos, race)
    s = pw.score(X); a = P.temperature_fit(s, y, race)
    assert P.race_ll(P.softmax_g(a * s, st, gid), y, st) < base - 0.1


def test_pairs_put_better_runner_first():
    X, y, pos, race, beta, p = synth(100)
    A, B = P.make_pairs(pos, race, np.random.default_rng(0))
    assert (pos[A] < pos[B]).all() and (race[A] == race[B]).all()
