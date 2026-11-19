# Phase 3 - win-probability calibration: our model vs the market

**Data:**
- Replay (B): development May-Aug, re-used Sep - 12 Oct, untouched H3 26 Oct - 18 Nov.
- Verified (A): 10-18 Nov.

Calibration exponent and blend weights are fitted on earlier months only (expanding). H3 and A use the final fit on Mar - 12 Oct. Full table: out/win_calibration.csv. Segments: out/win_segments.csv.

## Headline
| Set | Source | Log-loss | Brier | ECE | Slope | Intercept | Concordance | Top pick wins |
|---|---|---|---|---|---|---|---|---|
| Development (4,758 races) | our model | 1.969 | 0.0909 | 0.0039 | 1.00 | -0.01 | 0.670 | 26.6% |
| | calibrated model | 1.970 | 0.0909 | 0.0040 | 1.03 | 0.05 | 0.670 | 26.6% |
| | 09:00 market | 1.802 | 0.0856 | 0.0060 | 1.09 | 0.16 | 0.737 | 33.4% |
| | blend (market + model) | 1.799 | 0.0855 | 0.0045 | 0.99 | -0.02 | 0.736 | 33.2% |
| | BSP (closing) | 1.747 | 0.0843 | 0.0029 | 0.98 | -0.04 | 0.753 | 34.8% |
| Re-used (1,623) | our model | 2.022 | 0.0862 | 0.0032 | 1.00 | 0.01 | 0.671 | 25.8% |
| | 09:00 market | 1.835 | 0.0806 | 0.0071 | 1.10 | 0.17 | 0.734 | 33.1% |
| | blend | 1.832 | 0.0804 | 0.0038 | 0.99 | -0.01 | 0.734 | 32.9% |
| | BSP | 1.765 | 0.0787 | 0.0070 | 1.01 | 0.01 | 0.759 | 35.3% |
| **H3 untouched (674)** | our model | 2.013 | 0.0879 | 0.0063 | 1.01 | 0.02 | 0.674 | 26.3% |
| | 09:00 market | 1.774 | 0.0802 | 0.0103 | 1.12 | 0.20 | 0.761 | 35.5% |
| | blend | 1.769 | 0.0801 | 0.0080 | 1.02 | 0.03 | 0.763 | 35.8% |
| | BSP | 1.724 | 0.0788 | 0.0044 | 1.01 | 0.02 | 0.771 | 36.4% |
| **A verified (221)** | our model (live) | 2.032 | 0.0868 | 0.0140 | 0.98 | -0.04 | 0.683 | 24.0% |
| | 09:00 market | 1.838 | 0.0811 | 0.0171 | 1.00 | -0.01 | 0.750 | 30.8% |
| | blend | 1.842 | 0.0814 | 0.0169 | 0.90 | -0.17 | 0.754 | 31.7% |

Paired log-loss gain against the 09:00 market (positive = better than the market), 95% day-block interval:

| Set | Our model | Calibrated model | Blend | BSP |
|---|---|---|---|---|
| Development | -0.167 [-0.184, -0.150] | -0.168 | **+0.0038 [+0.0012, +0.0065]** | +0.056 |
| Re-used | -0.188 [-0.213, -0.163] | -0.188 | +0.0030 [-0.0022, +0.0076] | +0.070 |
| H3 | -0.239 [-0.285, -0.191] | -0.239 | +0.0047 [-0.0025, +0.0106] | +0.050 |
| A | -0.194 [-0.264, -0.118] | -0.194 | -0.0035 [-0.0217, +0.0148] | n/a |

## Findings
1. **Our model is well calibrated but has low resolution.**
   - Slope about 1.0, intercept about 0, ECE ≤ 0.006 on the replay. The fitted temperature a was 0.92-0.99, so calibration changes nothing.
   - Within bands of its own probability it is right: in the 10-20% band it says 13.9% and 14.0% win.
   - **The problem is ranking.** Concordance is 0.67 vs the market's 0.73-0.76, and top picks win 26% vs 33-36%.
   - Its log-loss is 0.17-0.24 worse than the 09:00 market. That is 3-4 times the whole gap between the 09:00 market and BSP (0.05-0.07).
2. **The model is too flat compared with the market.** Pooled re-used + H3, by 09:00 odds band:

   | 09:00 odds | Runners | Actual | Our model | 09:00 market | Blend | BSP |
   |---|---|---|---|---|---|---|
   | < 2.5 | 536 | 56.2% | 30.7% | 51.3% | 55.3% | 54.4% |
   | 2.5-5 | 2,359 | 28.3% | 19.8% | 26.9% | 28.4% | 27.9% |
   | 5-10 | 5,352 | 14.1% | 13.0% | 14.0% | 14.1% | 14.3% |
   | 10-20 | 5,848 | 6.8% | 9.0% | 7.3% | 6.9% | 7.0% |
   | 20-50 | 5,202 | 2.9% | 6.2% | 3.4% | 2.9% | 2.9% |
   | 50+ | 2,851 | 0.84% | 4.1% | 1.2% | 0.9% | 0.7% |

   Short-priced favourites get about half their real chance from our model, and 50+ outsiders about five times theirs. The 09:00 market itself is slightly too flat (slope 1.09-1.12). The blend fixes that, and that is most of its gain.
3. **By model rank, field size, Flat/Jumps and handicap**, the same story holds. Mean probabilities match by construction; ranking is the weakness everywhere. No segment where the model beats the market was found.
4. **Blend:**
   - weight on our model about 0.10 (z 2.0-3.6) at 09:00;
   - log-loss gain +0.003 to +0.005: about 0.2% of log-loss, or 5-9% of the gap between the 09:00 market and BSP;
   - significant in development only; not significant in re-used or H3; negative in the 221-race verified set.
   - **Operationally that is negligible.** It moves a typical 10% chance by about ±0.3 percentage points.
5. **The errors are ranking, not calibration.** Recalibrating the model cannot close the gap. It reproduces neither market information nor results better than the market. The model is fairly independent of the market (correlation of chances 0.73), but where it differs it is mostly wrong.

Charts: out/win_calibration_by_odds.png.
