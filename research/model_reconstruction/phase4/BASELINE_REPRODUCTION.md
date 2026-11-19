# Phase 4 - baseline reproduction

**Reproduced.**
- Same replay predictions (Phase 2 monthly refit of the production model).
- Same race populations as Phase 3: races with a 09:00 market for every runner, exactly one winner, and every runner matched to the feature table.
- 3 more races in development (4,761 vs 4,758) because the eligibility rules differ slightly. The other figures are identical.

| Set | Source | Phase 3 log-loss | Phase 4 log-loss | Races |
|---|---|---|---|---|
| Development May-Aug | Existing model | 1.9694 | 1.9687 | 4,761 |
| Development | 09:00 market | 1.8023 | 1.8018 | 4,761 |
| Re-used Sep-Oct | Existing model | 2.0222 | 2.0222 | 1,623 |
| Re-used | 09:00 market | 1.8345 | 1.8345 | 1,623 |
| H3 26 Oct - 18 Nov | Existing model | 2.0128 | 2.0128 | 674 |
| H3 | 09:00 market | 1.7741 | 1.7741 | 674 |

Every race distribution sums to 1 (maximum error 4e-16).

**Runner lists and non-runners:**
- Replay and market are both normalised over the runners that ran.
- The live model normalises over the sealed card after non-runners are removed at seal time.
- Neither causes the gap. The remaining difference is late non-runners after 09:00, which affect the market and the model equally.

**Full metrics** (out/metrics.csv). Brier is the multiclass score per race. Favourite figures are the 09:00 favourite's predicted vs actual win rate; longshot figures are for runners under 2% at 09:00.

| Set | Model | Log-loss | Brier | Top pick wins | Winner's mean rank | Concordance | Calibration slope | Favourite predicted / actual | Longshot predicted / actual |
|---|---|---|---|---|---|---|---|---|---|
| Development | Existing model | 1.969 | 0.828 | 26.2% | 3.68 | 0.670 | 1.00 | 21.2% / 33.0% | 4.2% / 0.6% |
| Development | 09:00 market | 1.802 | 0.780 | 33.3% | 3.14 | 0.737 | 1.09 | 31.2% / 33.0% | 1.3% / 0.6% |
| Development | Market at off (diagnostic) | 1.757 | 0.770 | 34.2% | 3.03 | 0.750 | 1.05 | 32.0% / 33.0% | 1.0% / 0.6% |
| Development | BSP (diagnostic) | 1.747 | 0.768 | 34.7% | 3.01 | 0.753 | 0.98 | 33.1% / 33.0% | 0.75% / 0.6% |
| Re-used | Existing model | 2.022 | 0.835 | 25.7% | 3.85 | 0.671 | 1.00 | 20.3% / 33.0% | 4.0% / 0.9% |
| Re-used | 09:00 market | 1.835 | 0.780 | 33.0% | 3.31 | 0.734 | 1.10 | 30.8% / 33.0% | 1.3% / 0.9% |
| H3 | Existing model | 2.013 | 0.839 | 26.3% | 3.79 | 0.674 | 1.01 | 19.7% / 35.5% | 4.5% / 0.7% |
| H3 | 09:00 market | 1.774 | 0.765 | 35.5% | 3.04 | 0.761 | 1.12 | 32.5% / 35.5% | 1.2% / 0.7% |

The existing market-model blend from Phase 3 is reproduced inside candidate E. E's weights on the existing model (0.06-0.12) match Phase 3's 0.09-0.11.
