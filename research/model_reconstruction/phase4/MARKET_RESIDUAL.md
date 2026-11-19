# Phase 4 - market-anchored residual learning

**Form:** score = log(market chance at the decision time) + g(pre-race features); probabilities = race softmax.
- With g = 0 this is exactly the market (unit test `test_offset_with_zero_correction_recovers_market`).
- g is fitted only on earlier months.
- BSP and later prices are never inputs.
- Variants: D1 (linear g, L2 = 3), D2 (boosted g, depth 2, early stopping), and E (stack of log market, the independent listwise score and the existing model).

## Results at 09:00 (paired log-loss gain vs the 09:00 market, 95% day-block)
| | Development | Re-used Sep-Oct | H3 | Months positive |
|---|---|---|---|---|
| D1 linear | +0.0007 [-0.0043, +0.0056] | -0.0031 | +0.0013 | 4 / 8 |
| D2 boosted | +0.0022 [-0.0001, +0.0043] | +0.0003 | +0.0018 | 6 / 8 |
| E hybrid | **+0.0034 [+0.0008, +0.0060]** | +0.0033 [-0.0016, +0.0082] | +0.0043 [-0.0033, +0.0108] | 6 / 8 |

What drives the gains:
- **Sharpening the market.** The 09:00 market is slightly too flat (calibration slope 1.09-1.12). All three models learn a market coefficient around 1.07-1.10. That alone accounts for most of the gain (see the checkpoint table).
- **The existing model's information** (E weight 0.06-0.12, as in Phase 3).
- **The independent listwise score** adds almost nothing beyond them (E weight -0.03 to +0.07, sign unstable).

**Stability of the corrections:**
- D1's feature coefficients are not stable month to month. It loses to the market in 4 of 8 months.
- D2's correction shrinks over time: 77 trees when trained to Jul, 8-13 trees by Oct/Nov. Early stopping finds less and less to correct.
- Weights for E: see MODEL_EXPERIMENTS.md.

## Does the residual keep value closer to the off? (Phase 6 experiment, D1 at each checkpoint)
| Decision time | Market log-loss (development) | Residual gain, development | Of which market sharpening alone | **Features beyond sharpening** | Residual gain, re-used | Features beyond, re-used |
|---|---|---|---|---|---|---|
| 21:00 previous evening | 1.877 | **+0.024 [+0.016, +0.033]** | +0.014 | **+0.0105** | +0.011 [-0.001, +0.023] | -0.0007 |
| 09:00 | 1.802 | +0.0007 | +0.0033 | -0.0026 | -0.0031 | -0.0064 |
| off-60m | 1.770 | -0.0035 | +0.0019 | -0.0053 | -0.0049 | -0.0085 |
| off-10m | 1.762 | -0.0041 | +0.0011 | -0.0052 | -0.0054 | -0.0075 |
| 1 second before the off | 1.757 | -0.0043 | +0.0008 | -0.0052 | -0.0054 | -0.0066 |

**Reading:**
- Our pre-race features add real information **only against the previous evening's market**: +0.0105 in development, about 0 in the re-used period.
- By 09:00 the market has already absorbed it. From an hour before the off, adding features makes things **worse** (overfitting noise the market has already priced).
- **There is no period close to the off when our information helps.**
- The only window is the overnight market (21:00 previous evening). That is a thin market where prices are least executable (Phase 3: morning exchange quotes are short).
