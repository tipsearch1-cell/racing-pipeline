# Phase 2 - robustness: walk-forward, multiple comparisons, outliers

## 1. Walk-forward design
| Layer | What is fitted | Training data | Scored on |
|---|---|---|---|
| Our win model (SYNTHETIC replay) | production conditional logit, Flat and Jumps | history races before the 1st of the month | that month (Mar - Oct 2026) |
| Second stage | discounted-Harville exponents per input; blend weights; D coefficients | replayed months before the test month (expanding, Mar..M-1) | test month (May - Oct) |
| Development | May, Jun, Jul, Aug | | model choices were fixed in advance by the sealed spec; nothing was tuned on them |
| **Final S holdout** | | | **1 Sep - 12 Oct 2026, scored once** |
| **Genuine G** | everything fitted on Mar - 12 Oct replay | | **10-18 Nov 2026 archived pre-race chances** |

- Phase 1's reverse split (S2) is not used as forward evidence.
- The recovered old-model chances (G0, 14 Oct - 9 Nov) are not used: provenance unverified.
- **Archive length: G has 217 races (9 days). That is too short to confirm or rule out a place-betting edge on its own.** It is used only as a sign check.

## 2. Multiple comparisons
- **Accuracy:** 3 candidate models (B, C, D) × 2 primary measures on the holdout, against one pre-registered pass rule. None of B or C would pass even without correction. D passes the trifecta measure but not top-3 Brier.
- **Betting:** 36 cells. The pass rule uses the Bonferroni 99.86% interval. Nothing passes even the uncorrected 95% interval.
- **Disagreement bands, segments and odds bands:** exploratory. 7 bands × 2 comparisons × 3 periods, plus about 60 segments. A few nominal "significant" cells appear in one period. None repeats with the same sign in both S periods and G, which is what chance alone produces.

## 3. Outliers and longshots (Phase 8)
Explanations ranked by the evidence:

| Explanation | Evidence | Verdict |
|---|---|---|
| Genuine longshot edge | Place SP is calibrated at long prices: 20-50 band actual 3.2% vs SP-implied 3.4%; 50+ band 1.4% vs 1.0%. No interval for long-priced segments is above zero in the holdout. | **Not supported** |
| Ordinary high variance | The top 1% of payouts (place SP 50-500) turn every cell's P/L from about break-even to about -25% ROI. Development profit is all from one month (June: +£1,040 to +£1,170; the other three months together about -£100). | **Main driver** |
| **Model miscalibration** | Against place SP the 09:00-based models over-rate long-priced runners: 20-50 band market+Harville 9.0%, ours 16.5%, actual 3.2%; 50+ band 6.3% / 12.9% vs 1.4%. Their claimed EVs are +64% to +229% against an observed +1%. | **Main driver** |
| Small-sample artefact | June 2026 alone; G (one week) goes the other way at -20% to -35% | Contributes |
| Wrong execution assumptions | LOC with full fill at BSP is optimistic for drifters (thin place pools, and our own order would lower BSP). Partial fills can't be modelled. | Would make results worse, not better |

### Why the EV signal points at drifters
An EV rule with a limit-on-close order bets only when the final place SP is long relative to our 09:00-based probability. Such horses are mostly ones the market moved against between 09:00 and the off. The movement check confirms that horses we rate above the market drift: correlation -0.27 in the holdout.

So the rule systematically selects horses with negative late information. That is adverse selection, and it is why the model's stated EV is wildly above what is realised. Any future place strategy must condition on, or be decided at, prices close to the off.

See out/calibration_by_psp_band.png: the place SP line overlaps the actual line in every band, while the market+Harville and our-model lines rise above it from place SP 5 upwards.

## 4. Sensitivity
- **Commission 5%:** every holdout cell is between -2.3% and -0.5%, and every interval includes zero.
- **EV threshold:** holdout ROI is flat across 0-10% (+0.2% to +1.9% at 2% commission). There is no dose-response, which is what an edge would show.
- **Model parameters:** blend weight on our model 0.05-0.11 across windows; discount exponents stable (market 0.90-0.93 / 0.75-0.77; ours 0.79-0.81 / 0.67-0.71 at 10 runners). The results do not hinge on any single fit.
- **Excluding extreme payouts:** without the top 1% every cell is about -25%. Without the top 5% about -50%. As the brief says, this alone does not reject a strategy. Combined with the calibrated place SP it shows the profit isn't systematic.
