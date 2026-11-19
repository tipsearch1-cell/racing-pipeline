# Phase 4 - candidate models

Configuration: out/config.json. Code:
- p4_models.py: race-softmax conditional logit, listwise Newton-boosting, pairwise RankNet-boosting, temperature;
- p4_run.py: walk-forward;
- p4_eval.py: metrics.

Tests: test_p4.py, 5 tests (softmax normalisation, coefficient recovery, recovering the market when there is no correction, learning a signal, pair ordering).

**Tooling note:** lightgbm and xgboost are not installable in this workspace (no wheel in the package registry). The boosted models use scikit-learn regression trees inside a custom Newton-boosting loop. That is the same idea as LightGBM's ranking objectives at this scale. Training times are under 2 minutes per monthly fit (out/config.json `timing_s`).

| Candidate | Inputs | Objective | Probability step | Notes |
|---|---|---|---|---|
| Baseline | 13 production features | race softmax | softmax | Phase 2 replay, unchanged |
| **A** Improved current | 61 race-relative features (groups G0-G7), per code | race softmax, L2 ∈ {0.3, 1, 3} chosen on the last training month | softmax | Same architecture, more information |
| **B** Pairwise | 61 features + code flag | pairwise logistic (winner vs all, plus sampled finisher pairs), depth 3, learning rate 0.1, early stopping | race softmax with a temperature fitted on training (1.23-1.43) | RankNet-style |
| **C** Listwise | same | race softmax via Newton boosting, depth 3, learning rate 0.1, early stopping (22-142 trees) | softmax | |
| **D1** Market residual, linear | log 09:00 market (offset) + 61 features | race softmax, L2 = 3 | softmax | Equals the market when the correction is zero |
| **D2** Market residual, boosted | log 09:00 market (offset) + features | Newton boosting from the market, depth 2, learning rate 0.05, early stopping (8-83 trees) | softmax | Equals the market when there are no trees |
| **E** Hybrid | log market, C's score, log existing model | race softmax (3 weights) on earlier months' out-of-time scores | softmax | E weights ≈ (1.07-1.11 market, -0.03 to +0.07 C, 0.06-0.12 existing) |

## Results (paired log-loss gain per race; positive = better than the comparator; 95% day-block intervals)
| Candidate | vs existing model, development | vs 09:00 market, development | vs market, re-used | vs market, H3 | Top pick wins (development) | Concordance (development) |
|---|---|---|---|---|---|---|
| A Improved | +0.025 [+0.017, +0.033] | -0.142 [-0.156, -0.127] | -0.151 | -0.190 | 27.6% | 0.682 |
| B Pairwise | +0.025 [+0.015, +0.036] | -0.142 [-0.158, -0.125] | -0.142 | -0.168 | 27.3% | 0.681 |
| C Listwise | +0.019 [+0.009, +0.029] | -0.148 [-0.164, -0.134] | -0.145 | -0.178 | 27.2% | 0.676 |
| D1 Residual (linear) | +0.168 | +0.0007 [-0.0043, +0.0056] | -0.0031 [-0.0095, +0.0031] | +0.0013 [-0.0085, +0.0113] | 32.8% | 0.737 |
| D2 Residual (boosted) | +0.169 | +0.0022 [-0.0001, +0.0043] | +0.0003 [-0.0026, +0.0028] | +0.0018 [-0.0004, +0.0039] | 33.0% | 0.737 |
| **E Hybrid** | +0.170 | **+0.0034 [+0.0008, +0.0060]** | +0.0033 [-0.0016, +0.0082] | +0.0043 [-0.0033, +0.0108] | 33.2% | 0.736 |

Re-used period, existing model vs each candidate: A +0.037, B +0.046, C +0.043. H3: A +0.049, B +0.071, C +0.061.

**By month, gain vs the 09:00 market** (chart: out/gain_vs_market_by_month.png):

| Candidate | May | Jun | Jul | Aug | Sep | Oct | H3 Oct | H3 Nov |
|---|---|---|---|---|---|---|---|---|
| D2 | -0.0016 | +0.0044 | +0.0035 | +0.0030 | +0.0004 | +0.0001 | +0.0053 | -0.0001 |
| E | -0.0006 | +0.0056 | +0.0047 | +0.0047 | +0.0029 | +0.0040 | +0.0148 | -0.0013 |

## Reading it
- **Independent models (A, B, C) beat the existing model in every period** (+0.02 to +0.07 log-loss), with top pick wins up from 26% to 27-29%.
- **They remain far behind the market** (-0.14 to -0.19). Pairwise (B) is the best independent model, but it is statistically indistinguishable from the linear A in development. The simpler A is enough.
- **Market-anchored models are the only ones at or above the market.** Their gains are tiny: about 0.2% of log-loss, against about 2.5-3.5% for the move from 09:00 to BSP. E is positive in 6 of 8 months.
- **Calibration by odds band** (out/calibration_by_odds.png): A and C still give odds-on favourites about 35% (actual 56%). D1, D2 and E sit on the market line. E matches the actual rate closely in every band (under 2.5: 55.4% vs 56.2%; 50+: 0.91% vs 0.84%).
