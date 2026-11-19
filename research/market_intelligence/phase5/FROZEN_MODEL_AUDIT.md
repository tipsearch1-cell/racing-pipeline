# Phase 5 - frozen model audit (19 Nov 2026)

**Verdict:** frozen Models E and D2 are intact.
- The full hash matches the repository record.
- Predictions reproduce exactly.
- E and D2 use the same race population.
- Nothing was retrained or replaced.

**One timing problem was found:** the Phase 4 shadow script uses the ~08:36 seal-time market, not 09:00. The confirmatory test now uses a genuine 09:00 snapshot (see SHADOW_PIPELINE_AUDIT.md).

## Artefacts
| Item | Value |
|---|---|
| Artefact | research/model_reconstruction/phase4/models/frozen_2026-11-19.pkl (238,262 bytes) |
| SHA-256 (full, recomputed) | `56179d9cf676d7d02a2ceb4e0cb484896057a4e0a9fbf8fcb5333bcc87178b52` |
| Recorded in frozen_2026-11-19.json | identical |
| Frozen at | 2026-11-19T12:52:48Z (record) |
| First committed | 0d1db41, committed 2026-11-19T13:01:00Z |
| First on GitHub (server-side push time, repository activity API) | 2026-11-19T13:01:02Z |
| Contents | C listwise booster (142 trees), D2 market-residual booster (83 trees), E weights [1.0792, 0.04381, 0.05936] on [log m, s_C, log f], 61 features + jumps flag, configuration (seed 20261119) |
| Training cutoff | all history before 2026-11-19. C and D2 fitted to 18 Oct with early stopping on 19 Oct - 18 Nov. E weights on Mar - 18 Nov. Market-anchored parts use the 09:00 checkpoint (M) |
| Feature pipeline | p4_features.build (history strictly before the race day) + shadow.card_rows (card weight minus the jockey's claim, to match training) |
| Calibration transformation | None beyond the per-race softmax. E is a conditional logit; D2 has no temperature |
| Exploratory X1 (new, not confirmatory) | phase5/models/x1_evening_2026-11-19.json, sha256 8b1c18c2…fb54cc |

## Checks
| Check | Result |
|---|---|
| Hash vs record | Match. `fwd.py` refuses to run (and stops the confirmatory test) on any mismatch |
| Unchanged since freezing | Same bytes as the first commit. GitHub records the push at 13:01:02Z on 19 Nov, before any forward race |
| Reproducible predictions | `shadow.predict` run twice for 18 Nov (31 races, 344 runners): byte-identical rows. About 90 s per run |
| New 09:00 decomposition | `fwd.py components` + `predict0900` given the same market reproduces shadow.py to 5e-7 (rounding) on every runner, for both E and D2 |
| Same race population | E and D2 are computed from the same table. A race is kept only if every runner has a market price and a production chance. The 09:00 eligibility (spec section 3) applies to both at once |
| Sums to 1 | Maximum per-race error 3e-6 (6-decimal rounding) |
| Market input available at prediction time | **No for "09:00" in Phase 4.** The sealed card is fetched at 08:36-08:37 UK (15-19 Nov), and provider quote times say 08:37 (19 Nov). The model was trained on the 09:00 checkpoint. Phase 5 records the seal-time series as exploratory and computes confirmatory predictions from a snapshot taken 09:00-09:30 UK |
| History used | Depends on whether yesterday was settled before the research step. It is now recorded per day (`history_max_date_used`). Any history date gives a valid pre-race prediction, but it is logged |

**Nothing was retrained, recalibrated or substituted.**
