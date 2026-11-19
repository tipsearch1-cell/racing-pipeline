"""Tests for research/harville/harville.py.   python3 -m pytest -q research/harville/test_harville.py"""
import itertools
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harville import clean, discount_weights, exacta_matrix, ordered_prob, position_probs, top_k  # noqa: E402

rng = np.random.default_rng(7)


def brute(p, w2, w3, w4, kmax):
    """Enumerate every ordered sequence of the first kmax finishers."""
    n = len(p)
    out = np.zeros((n, kmax))
    ws = [p, w2, w3, w4]
    for seq in itertools.permutations(range(n), kmax):
        pr, left = 1.0, set(range(n))
        for k, i in enumerate(seq):
            w = ws[k]
            pr *= w[i] / sum(w[j] for j in left)
            left.discard(i)
        for k, i in enumerate(seq):
            out[i, k] += pr
    return out


@pytest.mark.parametrize("n", [4, 5, 6, 7])
@pytest.mark.parametrize("ab", [(1, 1), (0.8, 0.65), (1.2, 0.5)])
def test_matches_enumeration(n, ab):
    p = rng.dirichlet(np.ones(n) * 0.7)
    p, w2, w3 = discount_weights(p, *ab)
    P = position_probs(p, w2, w3, kmax=4)
    B = brute(p, w2, w3, w3, 4)
    assert np.allclose(P, B, atol=1e-12)


@pytest.mark.parametrize("n", [3, 8, 16, 30])
def test_conservation(n):
    p = rng.dirichlet(np.ones(n))
    p, w2, w3 = discount_weights(p, 0.85, 0.7)
    P = position_probs(p, w2, w3, kmax=min(4, n))
    assert np.allclose(P.sum(axis=0), 1.0)          # exactly one horse in each position
    assert np.all(P.sum(axis=1) <= 1 + 1e-12)       # a horse occupies at most one position
    assert np.all(P >= 0)
    assert np.isclose(exacta_matrix(p, w2).sum(), 1.0)  # all ordered pairs sum to one
    tri = sum(ordered_prob(p, (i, j, k), w2, w3) for i, j, k in itertools.permutations(range(n), 3)) if n <= 16 else 1.0
    assert np.isclose(tri, 1.0)
    assert np.isclose(top_k(P, 2).sum(), 2.0) and (n < 3 or np.isclose(top_k(P, 3).sum(), 3.0))


def test_alpha_beta_one_is_harville():
    p = clean([0.5, 0.3, 0.15, 0.05])
    _, w2, w3 = discount_weights(p, 1, 1)
    assert np.isclose(ordered_prob(p, (0, 1), w2), 0.5 * 0.3 / 0.5)
    assert np.isclose(ordered_prob(p, (0, 1, 2), w2, w3), 0.5 * 0.3 / 0.5 * 0.15 / 0.2)
    assert np.allclose(position_probs(p, w2, w3), position_probs(p))


def test_discount_moves_mass_to_outsiders():
    p = clean([0.6, 0.2, 0.1, 0.06, 0.04])
    H = position_probs(p, kmax=3)
    _, w2, w3 = discount_weights(p, 0.7, 0.5)
    D = position_probs(p, w2, w3, kmax=3)
    assert D[0, 1] < H[0, 1] and D[-1, 1] > H[-1, 1]
    assert np.allclose(D[:, 0], H[:, 0])            # stage 1 untouched


def test_edge_cases():
    P = position_probs([1.0, 0.0, 0.0], kmax=3)    # certain winner; zero chances clipped, not divided by zero
    assert np.all(np.isfinite(P)) and np.allclose(P.sum(axis=0), 1)
    assert np.isclose(P[0, 0], 1, atol=1e-5)
    P2 = position_probs([0.7, 0.3], kmax=4)         # two runners: only two positions
    assert P2.shape == (2, 2) and np.allclose(P2.sum(axis=0), 1)
    P1 = position_probs([1.0], kmax=3)
    assert P1.shape == (1, 1)
    tiny = clean(np.r_[0.999, np.full(20, 1e-12)])
    assert np.all(np.isfinite(position_probs(tiny, kmax=4)))
    with pytest.raises(ValueError):
        clean([0.5, -0.1])
    with pytest.raises(ValueError):
        clean([np.nan, 1])
    with pytest.raises(ValueError):
        clean([0, 0])


def test_unnormalised_input_and_nonrunner_removal():
    raw = np.array([40.0, 30.0, 20.0, 10.0, 5.0])
    P = position_probs(raw[:4], kmax=3)              # non-runner removed, the rest renormalised
    assert np.allclose(P[:, 0], raw[:4] / raw[:4].sum())
