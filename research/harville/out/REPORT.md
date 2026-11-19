# Harville / ICM finishing-position research: final report (19 Nov 2026)

- **Spec:** prereg/HARVILLE_ICM_SPEC_2026-11-19.md
  - sealed sha256 db8f9110…a375982;
  - after Amendment 1 (implementation details, written before outcomes) 33b7b6f1…c9e8a.
- **Deviation disclosed in out/deviations.md:** during the code smoke test, 200 races from inside the S2 test period were scored. Nothing was changed afterwards.
- **Production untouched:** no file the live pipeline uses was modified.

## Bottom line
- **Accuracy:** Discounted Harville and the learned ranking model both predict 2nd and 3rd places better than plain Harville. This held in both test periods, on six years of GB Flat, and on Frankie's own genuine forward chances.
- **Betting:** none of the 36 betting rules made a reliable profit at Betfair place SP. The best results are well inside noise and depend on a handful of big-priced placers.
- **Exacta/trifecta and each-way:** profitability cannot be tested with the prices we hold.
- **Verdict:**
  - Discounted Harville: **CONTINUE RESEARCH**.
  - Learned ranking: **CONTINUE RESEARCH**.
  - Plain Harville stays only as a reference.
  - Nothing goes near the bot.

## 1. Data used (full inventory: out/inventory.md)
| Track | What | Period | Races | Use |
|---|---|---|---|---|
| O | 09:00 UK market chances (timestamped pre-race), GB+IRE Flat and Jumps; positions; Betfair place SP | 13 Oct 2025 - 12 Oct 2026 | 12,449 eligible | main test, two splits |
| F | Frankie's archived chances: old model (14 Oct - 9 Nov), rebuilt model and sealed reviewer chance (10-18 Nov) | 14 Oct - 18 Nov 2026 | 1,213 (reviewer: 217) | final holdout, nothing fitted |
| R | RBD GB Flat: closing win BSP (diagnostic only), Forecasted Odds (pre-race by definition, timestamp not verified), place SP and Betfair place flag | 2020 - 9 Oct 2026 | 44,761 | parameter stability, long-run betting check |

Notes on provenance and coverage:
- **Old-model chances** come from the recovered report page. Their publication time is assumed, not timestamp-verified.
- **No Frankie chances exist before 14 Oct 2026.** The rebuilt model was trained on Jan - 25 Oct 2026, so replaying it over that period would be in-sample. That replay was not done.
- **Place SP coverage on O:** 86% of runners. It's missing for Jumps in Oct-Dec 2025.
- **Places rule check:** the Betfair place-terms rule matches Betfair's own settlement in 89% of RBD races.
- **Place-market overround:** sum of 1/place SP divided by places has a median of 1.004, so the joins are sound.

## 2. Final comparison (track O tests; 09:00 market input, so "Market baseline" = Harville on the market)
| Model | Test | Races | Top-2 Brier | Top-3 Brier | Exacta log-loss | Trifecta log-loss | Place ROI (2% comm, EV ≥ 0) | Exacta ROI | Trifecta ROI |
|---|---|---|---|---|---|---|---|---|---|
| Harville = market baseline | S1 (Apr-Oct 26) | 7,447 | 0.13875 | 0.17157 | 3.6299 | 5.3524 | +1.5% [-3.4, +7.3], 31,501 bets | NOT TESTABLE | NOT TESTABLE |
| Discounted Harville (B5) | S1 | 7,447 | 0.13869 | 0.17109 | 3.6269 | 5.3339 | +1.4% [-3.6, +7.0] | NOT TESTABLE | NOT TESTABLE |
| Learned ranking (C) | S1 | 7,447 | 0.13867 | 0.17101 | 3.6256 | 5.3315 | +1.5% [-4.0, +7.2] | NOT TESTABLE | NOT TESTABLE |
| Harville = market baseline | S2 (Oct 25-Mar 26) | 5,002 | 0.13810 | 0.16860 | 3.5253 | 5.1931 | -4.4% [-9.8, +1.9], 14,337 bets | NOT TESTABLE | NOT TESTABLE |
| Discounted Harville (B5) | S2 | 5,002 | 0.13811 | 0.16846 | 3.5231 | 5.1817 | -5.6% [-11.1, +0.4] | NOT TESTABLE | NOT TESTABLE |
| Learned ranking (C) | S2 | 5,002 | 0.13805 | 0.16831 | 3.5212 | 5.1758 | -5.6% [-11.0, +0.6] | NOT TESTABLE | NOT TESTABLE |
| Frankie place probabilities (E) | - | - | N/A (never produced) | | | | | | |

How to read the table:
- Brackets are 95% date-block bootstrap intervals (whole race days resampled, 2,000 draws).
- Benchmark (back every runner at place SP, 2%): S1 -2.5% [-4.9, +0.2]; S2 -5.1% [-7.7, -2.2].
- **NOT TESTABLE** means no historical executable price exists. It is not a zero return.

**Accuracy gains over Harville** (trifecta log-loss per race; pass rule = lower bound > 0 in both splits):

| Model | S1 | S2 | Verdict |
|---|---|---|---|
| Discounted Harville | +0.0185 [+0.0146, +0.0225] | +0.0115 [+0.0054, +0.0177] | **PASS** |
| Learned ranking | +0.0210 [+0.0164, +0.0255] | +0.0173 [+0.0100, +0.0247] | **PASS** |

- Learned ranking vs Discounted Harville:
  - S1: +0.0024 [-0.0003, +0.0053];
  - S2: +0.0059 [+0.0036, +0.0083].
  - The edge is small and only clearly real in one split.
- Top-2 Brier gains are not significant in either split.
- Top-3 Brier gains are significant for C in both splits, and for B in S1 only.
- So the improvement is mainly in **3rd place**, then 2nd.

## 3. What the models learned
**Discounted Harville** (selected variant B5, picked by BIC on the fit period in both splits): each exponent depends on field size. Fitted on all of O:
- 2nd-place exponent = 0.931 + 0.222·ln(n/10);
- 3rd-place exponent = 0.787 + 0.243·ln(n/10).

So:
- a 6-runner race gets about 0.82 / 0.66;
- a 10-runner race gets 0.93 / 0.79;
- a 20-runner race gets about 1.08 / 0.96.

Harville's error is largest in small fields and close to zero in big handicaps.

**Stability:**
- Split fits: B2 exponents were 0.94/0.80 on S1 and 0.88/0.74 on S2.
- **R with closing BSP:** the B2 exponents were the same every year 2022-2026: 0.79-0.80 for 2nd, 0.65-0.66 for 3rd (out/r_stability.csv). This matches the published Lo & Bacon-Shone values (0.81 / 0.65) almost exactly.
- **R with Forecasted Odds:** about 0.92 / 0.76 in every year.

The discount is weaker on 09:00 chances than on closing chances, because morning prices are already flatter.

**Learned ranking:**
- Its main extra signal is a negative favourite term: the favourite is over-rated for 2nd and 3rd even after the exponent.
- It also has slightly stronger discounting in handicaps.
- Class and code add little. Separate Flat/Jumps parameters (B3) were never selected by BIC.

## 4. Where Harville goes wrong (out/actual_vs_expected_by_rank.png, both tests pooled)
**Favourite:**
- Finishes 2nd 13% less often than Harville predicts.
- Finishes 3rd 19% less often.
- Discounted Harville halves this error. The learned model nearly removes it (-4% / -1%).

**Ranks 4-8:**
- Harville under-predicts their 3rd places by 7-20%.
- Both corrected models bring this within about ±5%.

**Calibration slope for P(3rd):**
- Harville 0.86-0.89;
- Discounted 1.00 (S1) / 1.08 (S2);
- Learned 0.98 / 1.08.

**Segments (trifecta gain):**
- Strongest in 5-7 runner races (+0.02 to +0.04) and in Jumps.
- In 12-15 and 16+ runner races Discounted Harville is no better than Harville, and in S1's 16+ races it is slightly worse (-0.011).
- The learned model holds up there.

**Frankie inputs (genuine forward, F):** the same correction helps when the input is Frankie's own chances.
- Rebuilt/old model input: trifecta gain B +0.015 [+0.008, +0.022], C +0.020 [+0.009, +0.029].
- Reviewer input (217 races): B +0.048 [+0.023, +0.078].

## 5. Betting
**Place bets at Betfair place SP.** Executable as limit-on-close BSP bets, with the limit set from the pre-race probability.
- In 36 cells per test (3 models × 6 EV thresholds × 2 commission rates), no cell has a 95% lower bound above 0.
- No cell is profitable in every quarter.
- S1 shows +1-2% for every model and S2 shows -4 to -7%. The models do not separate from each other at the same threshold.
- R (Forecasted Odds input) loses in all 5 years (-1% to -7%).
- F with Frankie-model input shows +1-2%, but its intervals span ±12%.
- F with reviewer input loses heavily on 9 days.

**Outlier dependence:**
- Removing the top 1% of returns turns every place strategy to about -27% to -35%.
- Any apparent profit comes from a few big-priced runners placing, not from repeatable edge.

**Not testable:**
- **Each-way:** no archived bookmaker place terms or each-way prices; no Rule 4.
- **Forecast/exacta and tricast/trifecta:** Tote/CSF dividends exist for only 221 races since 10 Nov, and there is no pre-race executable price.
- Win BSP was never used to make up place or exotic returns.

## 6. Mispricing scan (Phase 8, exploratory)
Backing every runner at place SP lost in every market-rank group in at least one split.

Odd-looking segments that did not repeat:
- 21-41 shots: +4.1% in S1, -10.0% in S2.
- 12-15 runner fields: +2.0% in S1, -8.9% in S2.
- Non-handicaps: +3.7% in S1, -8.5% in S2.

No effect kept the same sign across both splits and at least 4 of 5 R years. **No systematic place-market mispricing was found.**

## 7. Answers
1. **Is plain Harville accurate enough?** No for 2nd/3rd. It over-rates favourites and under-rates mid-priced runners, by 10-20% at rank 1 and ranks 4-8.
2. **Does Discounted Harville give a repeatable improvement?**
   - In accuracy, yes: both splits, every R year and the Frankie forward data.
   - In betting, no.
3. **Separate Flat/Jumps parameters?** Not justified; never selected by BIC. Field size matters; code does not.
4. **Does the learned model beat the simpler methods?**
   - Slightly better than Discounted Harville: significant in S2, borderline in S1.
   - Better in big fields.
   - Not enough to justify the extra complexity on its own.
5. **Largest errors?** 3rd place, then 2nd, and for the favourite and ranks 4-8.
6. **Where are the gains concentrated?** Small fields (5-7 runners), the favourite, and mid-ranked runners (4-8).
7. **Positive EV at historical prices?** Not shown. No place cell passes. Exotics and each-way are NOT TESTABLE.
8. **Are profitable results driven by outliers?** Yes. Every positive place result goes to about -27% or worse without the top 1% of returns.
9. **More data needed?**
   - For exotics: archived pre-race exchange forecast prices or Tote pool snapshots, plus a longer run of dividends.
   - For each-way: bookmaker EW terms and prices.
   - More Frankie forward days.
10. **Production candidate?** No. Both corrections are worth keeping as research tools, for example to give Frankie's chances a proper 2nd/3rd estimate. Neither has shown a betting edge.

## 8. Verdicts
| Model | Verdict | Why |
|---|---|---|
| Harville | Reference only | Systematically miscalibrated for 2nd/3rd |
| Discounted Harville (field-size exponents) | **CONTINUE RESEARCH** | Passes accuracy in both splits; no betting cell passes |
| Learned ranking | **CONTINUE RESEARCH** | Passes accuracy, slightly better than B; no betting cell passes |
| Market Harville on Frankie (D) | Reference | Same pattern as above |

No model reaches PROMOTE TO FORWARD SHADOW TEST, because that needs a betting pass.

## 9. Reproduce
```
bash tools/restore_raw.sh                          # raw data from the raw-data branch
python3 research/harville/data.py                  # -> work/{O,F,R}.pkl, out/inventory.md
python3 -m pytest -q research/harville/test_harville.py   # 20 tests: conservation, enumeration, edge cases
python3 research/harville/run.py                   # -> out/results.md, betting_cells.csv, r_stability.csv, final_params.json, calibration_*.csv
python3 research/harville/charts.py                # -> out/calibration_S1.png, calibration_S2.png, actual_vs_expected_by_rank.png
```
- Random seed 20261119. Runtime about 5 minutes.
- Full per-split detail is in out/results.md: every betting cell with drawdown, losing run, quarters and trimmed ROI, plus fitted coefficients with standard errors.
