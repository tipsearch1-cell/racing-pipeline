"""Tests for Phase 3 helpers.  python3 -m pytest -q research/market_intelligence/phase3/test_p3.py"""
import os, sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p3  # noqa: E402


def toy():
    return pd.DataFrame(dict(race_id=["r1"] * 3 + ["r2"] * 3, date=["2026-06-01"] * 6, month=["2026-06"] * 6,
                             pos=[1, 2, 3, 2, 1, 3], m_M=[.5, .3, .2, .6, .3, .1], f=[.4, .4, .2, .2, .5, .3],
                             bf_M=[2.2, 3.5, 6.0, 1.8, 4.0, 12.0], bsp=[2.0, 3.6, 6.5, 1.7, 4.2, 15.0], close=[.5, .3, .2, .6, .3, .1]))


def test_pool_identity_and_normalisation():
    d = toy()
    assert np.allclose(p3.pool(d, ["m_M", "f"], [1, 0]), d.m_M)
    b = p3.pool(d, ["m_M", "f"], [0.7, 0.4])
    assert np.allclose(b.groupby(d.race_id).sum(), 1)


def test_eligible_requires_one_winner_and_complete_prices():
    d = toy()
    assert len(p3.eligible(d, ["m_M"])) == 6
    d.loc[0, "m_M"] = np.nan
    assert set(p3.eligible(d, ["m_M"]).race_id) == {"r2"}
    d2 = toy(); d2.loc[1, "pos"] = 1                     # dead-heat winner -> excluded
    assert set(p3.eligible(d2, ["m_M"]).race_id) == {"r2"}


def test_strategy_commission_and_settlement():
    d = toy()
    x = p3.strat_bets(d, "f", "bf_M", 0.0, 0.02)
    # r1 runner 1: EV = 0.4*(1+1.2*0.98)-1 = -0.13 -> no bet; r2 winner f=.5 * (1+3*0.98)=1.97 -> bet and wins
    w = x[(x.race_id == "r2") & (x.pos == 1)]
    assert len(w) == 1 and np.isclose(w.ret.iloc[0], 1 + 3.0 * 0.98)
    assert np.isclose(w.clv_bsp.iloc[0], 4.0 / 4.2 - 1)
    assert (x.ev >= 0).all()


def test_win_metrics_ranges():
    d = toy()
    m = p3.win_metrics(d, "m_M")
    assert 0 <= m["ece"] <= 1 and 0 <= m["concordance"] <= 1 and m["races"] == 2
    assert np.isclose(m["ll"], -np.mean(np.log([.5, .3])))
