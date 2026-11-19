# Phase 4 - architecture audit of the current win model

Source: pipeline/models.py (functions `prior_features`, `race_relative`, `fit`, `predict`, `train`, `run_day`) and pipeline/history.py. Read-only; nothing changed.

| Aspect | Current design | Assessment |
|---|---|---|
| Training data | History table: RaceData exports (1 Jan - 13 Oct 2026) plus Racing API results (14 Oct onwards). GB+IRE, Flat and Jumps. Races with ≥ 4 runners and exactly one winner. | Only about 10 months deep. No pre-2026 history, so early-2026 horses look "first-time". |
| Target | Winner indicator per runner | Appropriate |
| Objective | **Conditional logit = race-level softmax, multiclass winner log-loss** (`fit`: per-race softmax NLL plus L2) | **Already listwise.** There is no objective mismatch: the model is optimised for race-level winner probability, which is the right target. |
| Algorithm | Linear score (13 weights), separate Flat and Jumps coefficient sets | Linear and additive, no interactions |
| Features (13) | mkt_rel (mean log(n/BSP) of the last 2 runs, relative to the field), pos_rel (mean position score of the last 3 runs), or_rel, lbs_rel (today's official rating and weight relative to the field), log runs, days ≥ 90, days ≤ 10, first run, won last time, non-finishes in the last 3, plus 3 missing flags | Thin. **No trainer/jockey information, no speed or performance figures, no class change, no course/distance/going suitability, no pedigree, no market signal from today.** The strongest feature is earlier BSP (an old market opinion). |
| Relative features | Field-mean centring for 4 features; ranks not used | Partly relative. Phase 4 tested fuller relative forms (§ RANKING_DIAGNOSTICS) |
| Training period | `train()` fits on 1 Apr - 25 Oct (for validation) and on all history for the live coefficients ("history to 2026-11-09") | One fit, never refreshed since 10 Nov |
| Hyperparameters | L2 = 1.0, L-BFGS-B | Negligible effect (L2 = 0 vs 1: log-loss 1.9417 vs 1.9415) |
| Feature selection | None (fixed list) | n/a |
| Probability transformation | Softmax of the linear score; no post-hoc calibration | Calibration is fine (slope 1.00-1.01). The best temperature on test is 1.006: **no compression from post-processing** |
| Race normalisation | Softmax per race over the card's runners | Sums to 1 (max error 4e-16) |
| Non-runners | Removed from the card at seal; the model runs on the remaining runners. Field size n = runners on the card. In history, n = runners that ran. | Consistent between training and prediction. A small leak in training (late non-runners are known) applies equally to the market comparison. |
| Market information | Today's market is **excluded** by design. Earlier BSPs are used as a horse-quality feature. | Independence is intended, but it means discarding the strongest available signal. |
| Missing data | Race-mean fill (0 after centring) plus 3 NA flags | Adequate |
| Flat vs Jumps | Separate coefficient sets | Fine (pooling made no difference) |
| Handicap vs non-handicap | Not distinguished | The handicap mark is partly captured by OR and weight |
| Field size | Implicit (softmax over n) | Entropy is higher than the market's in every field band. That comes from weak information, not scaling (a temperature per band changes nothing) |
| Leakage / timestamps | `prior_features` uses only strictly earlier rows of the same horse; `run_day` filters history to date < day. Today's OR and weight are pre-race. | **No leakage found** |
| Training vs prediction mismatch | Training n = ran; prediction n = card after non-runners removed (equivalent at 09:00). Field-relative features are computed the same way. | None material |

## Likely cause of the gap (tested in RANKING_DIAGNOSTICS.md)
The model ranks horses using a handful of crude form signals. The market also prices trainer and jockey intent, connections' form, ratings quality, stable information, pedigree and late news.

The ranking failure is mainly a **missing-information problem**, not an objective, normalisation, field-size, compression or population problem.
- Adding trainer and jockey form closes the biggest single part.
- All the extra feature groups together close only about 17% of the gap to the 09:00 market.
