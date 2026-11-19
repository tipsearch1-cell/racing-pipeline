# Harville Phase 2 - final report (19 Nov 2026)

**Result: no place-betting edge.** On its own, our model knows less than the 09:00 market. Blended in, it adds a small but real amount of win information. A finishing model using finishing consistency improves 2nd/3rd estimates, mainly in big fields.

None of this beats Betfair place SP, which is accurately calibrated. Every apparent place profit is explained by a few huge payouts plus a selection effect that favours drifters.

This is a credible negative result. Nothing should be promoted to a forward shadow test of betting.

- **Spec:** prereg/HARVILLE_PHASE2_SPEC_2026-11-19.md, sealed before any outcome comparison (sha256 dc20868c…74). No amendments.
- **Code:** research/harville/phase2/
  - replay.py, run2.py, analyze2.py, charts2.py, test_phase2.py;
  - outputs in out/.
- Phase 1 files are untouched. No production code, model or bot changed.

## What was fixed from Phase 1
| Phase 1 weakness | Phase 2 fix |
|---|---|
| Mostly market input, not our model | Our model's chances on 8,132 races (strict month-by-month SYNTHETIC replay, Mar - Oct 2026) plus 217 races of genuine archived pre-race chances (G, 10-18 Nov, verified by git commit times and a model trained to 9 Nov) |
| Reverse-chronological S2 split | Dropped as evidence. Expanding walk-forward only; untouched holdout 1 Sep - 12 Oct; G scored once |
| 89% place-terms agreement | Places now come from declared runners (ran + non-runners): **99.2%** agreement with Betfair's own settlement (5+ runners) |
| Outlier-dependent profits | Outlier decomposition, null simulations, and the drifter mechanism identified (ROBUSTNESS.md) |
| Execution assumptions | LOC-at-BSP modelled from pre-race limits only. Partial fills can't be reconstructed (no BSP volumes), so results are labelled conditional simulations |

## Strategy comparison (identical races and prices; paired intervals vs the market model)
| Method | Period | Top-2 Brier | Top-3 Brier | P(place) calibration slope | Bets (EV ≥ 0, 2%) | ROI | 95% CI |
|---|---|---|---|---|---|---|---|
| Market + discounted Harville | S holdout | 0.13393 | 0.16702 | 1.03 | 7,482 | +0.8% | [-6.9, +8.5] |
| Our model + discounted Harville | S holdout | 0.14500 | 0.18199 | 1.04 | 7,738 | +1.1% | [-6.3, +8.6] |
| Blend + discounted Harville | S holdout | 0.13394 | 0.16709 | 0.99 | 7,432 | +1.0% | [-6.4, +9.6] |
| Enhanced ranking | S holdout | 0.13383 | 0.16683 | 0.99 | 7,444 | +0.9% | [-6.3, +9.0] |
| Market + discounted Harville | G | 0.13042 | 0.16310 | 1.00 | 463 | -23.2% | [-37.5, +4.1] |
| Our model + discounted Harville | G | 0.14285 | 0.17752 | 1.13 | 532 | -21.0% | [-36.0, +8.9] |
| Blend + discounted Harville | G | 0.13045 | 0.16305 | 0.98 | 454 | -19.7% | [-34.4, +8.3] |
| Enhanced ranking | G | 0.12981 | 0.16123 | 1.00 | 471 | -23.8% | [-35.7, -3.7] |

Benchmark, back every runner at place SP (2%): holdout -1.0% [-4.5, +2.9]; G -10.6%.

Results by period, threshold, odds band, field size, code, handicap and rank are in:
- BETTING_RESULTS.md and out/betting_tables.md;
- SEGMENT_ANALYSIS.md, out/segments.csv and out/field_accuracy.csv.

## Verdicts
| Candidate | Predictive value | Independent information | Betting value | Robustness | Operational | Verdict |
|---|---|---|---|---|---|---|
| Market + discounted Harville | Baseline (beats original Harville) | none (it is the market) | none | n/a | yes | Reference |
| Our model + discounted Harville | **Fails**: far worse than the market | n/a | none | n/a | yes | **REJECT** as a standalone place model |
| Blend + discounted Harville | Fails: win LL +0.003, top-3 Brier ≈ 0 | Small but real (w ≈ 0.1, z 2.0-3.6 in 5 of 6 windows; the June window z = 1.2 fails the strict rule) | none | stable weight | yes | **CONTINUE RESEARCH** (as a win-probability input only) |
| Enhanced ranking (D) | Borderline: trifecta LL passes (+0.012 [+0.003, +0.022]); top-3 Brier misses (+0.0019 [-0.0017, +0.0054]); positive in 5 of 6 months and in G | comes from runner features, not from beating the market | none | gains concentrated in 12+ fields | yes | **CONTINUE RESEARCH** (as a probability tool, e.g. for exotics) |
| Any place-betting rule (36 cells) | | | **0 of 36 pass** | September up and October down in every cell; development profit all from June; G -20% to -35% | conditional simulation only | **REJECT** |

**PROMOTE TO FORWARD SHADOW TEST: none.**

## Answers
1. **Is our model more accurate than the market at 2nd and 3rd?** No. It is much worse on its own. Holdout top-3 Brier per race is 0.145 worse, trifecta log-loss 0.39 worse; G is the same.
2. **Does combining it with the market help?** A little, for the win: the log-linear blend gains about 0.2% of win log-loss with a stable weight of about 0.1. It does not improve 2nd/3rd on its own; the runner features (D) do that.
3. **Do large disagreements predict outcomes?** Yes, in the market's favour. In every band the actual place rate sits on the market line, while ours is out by up to 20 points. The market also moves away from our view by the off (correlation -0.27).
4. **Are ranks 4-8 mispriced in place markets?** No. Harville's under-rating of them is real, but Betfair place SP is calibrated for every rank. ROI at place SP has no interval above zero and swaps sign between periods.
5. **Are 5-7 runner races promising?** No. The Phase 1 small-field gain was Harville's bias, and the field-size exponents already fix it. Nothing beyond that baseline works there; back-all ROI was +0.5%, then -6.8%.
6. **Can pace, consistency and setup improve place probabilities?** Consistency and experience do (position-score and run-count terms, mostly at 3rd, mostly in 12+ fields). Front-running is a weak negative for 2nd. Distance, going and class add nothing. Beaten distances weren't available for the replay period.
7. **Is any betting profit statistically convincing?** No. 0 of 36 cells pass. No holdout cell's ordinary 95% interval is above zero.
8. **Could the strategies be executed?** Only as conditional simulations. LOC-at-BSP fills can't be verified without BSP pool data. The rules select drifters, where thin place pools make full fills least likely.
9. **Extreme payouts or consistent mispricing?** Extreme payouts plus model miscalibration on drifters. The top 1% of payouts turn every cell from about break-even to about -25%. All development profit came in June 2026. Place SP itself is calibrated.
10. **Single most promising next step?** Start archiving our own forward data properly: daily model chances, the enhanced 2nd/3rd probabilities, and 09:00 and pre-off place-market prices with volume. Then test place decisions made near the off (OPPORTUNITIES.md #1-#2). The 217-race genuine archive is far too short today.

## Limitations
- **Genuine archive is small:** 217 races of verified pre-race chances (9 days). The large-sample evidence is a SYNTHETIC replay. It is strictly out-of-time, but it is not what was actually published.
- **Thin early history:** history starts 1 Jan 2026, so replay features are thin early in the year. That is why development starts in May.
- **No beaten distances** in the RaceData-sourced history.
- **No BSP volume data** (fills), **no bookmaker each-way data**, and **no exotic pool data**.
- **The 09:00 exchange quotes are too thin** to test anything executed at 09:00 itself.

## Reproduce
```
bash tools/restore_raw.sh
python3 research/harville/data.py                 # Phase 1 track O (unchanged)
python3 research/harville/phase2/replay.py        # synthetic replay + genuine archive  (~45 s)
python3 research/harville/phase2/run2.py          # walk-forward fits and scoring       (~45 s)
python3 research/harville/phase2/analyze2.py      # tables, betting, disagreement        (~45 s)
python3 research/harville/phase2/charts2.py
python3 -m pytest -q research/harville/phase2/test_phase2.py
```
Random seed 20261119.
