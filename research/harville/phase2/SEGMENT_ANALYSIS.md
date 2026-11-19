# Phase 2 - segment analysis (ranks 4-8, field sizes, odds bands, race types)

Full numbers: out/segments.csv (every segment, every period) and out/field_accuracy.csv.

"Place SP implied" = 1/PSP normalised so it sums to the places paid. "ROI" = backing every runner in the segment at place SP with 2% commission. Data = SYNTHETIC replay: development May-Aug, holdout 1 Sep - 12 Oct 2026.

## Phase 4 - runners ranked 4-8 (09:00 market rank)
| Rank | Period | Runners | Actual placed | Original Harville | Market + discounted Harville | Our model + discounted Harville | Enhanced | Place SP implied | ROI [95%] |
|---|---|---|---|---|---|---|---|---|---|
| 4 | Development | 4,536 | 34.7% | 31.9% | 32.1% | 32.7% | 32.5% | 33.5% | +3.2% [-1.6, +7.7] |
| 5 | Development | 4,438 | 26.8% | 25.3% | 26.1% | 29.5% | 26.2% | 26.7% | -0.3% [-8.1, +7.7] |
| 6 | Development | 4,030 | 21.8% | 20.9% | 22.1% | 27.2% | 21.9% | 22.3% | -5.5% [-12.0, +1.6] |
| 7 | Development | 3,506 | 18.8% | 17.9% | 19.2% | 25.5% | 19.0% | 18.8% | +6.2% [-6.6, +19.9] |
| 8 | Development | 2,972 | 16.9% | 15.3% | 16.8% | 23.5% | 16.4% | 15.9% | +5.0% [-7.1, +17.5] |
| 4 | Holdout | 1,554 | 34.0% | 32.1% | 32.3% | 32.1% | 33.0% | 33.6% | -0.7% [-8.2, +7.6] |
| 5 | Holdout | 1,530 | 25.6% | 25.6% | 26.4% | 29.2% | 26.7% | 27.2% | -8.5% [-17.7, -0.0] |
| 6 | Holdout | 1,426 | 22.2% | 21.0% | 22.1% | 26.7% | 22.1% | 22.4% | -2.5% [-17.4, +15.8] |
| 7 | Holdout | 1,293 | 21.3% | 17.5% | 18.9% | 24.8% | 18.7% | 18.7% | +11.0% [-7.1, +34.0] |
| 8 | Holdout | 1,136 | 15.1% | 14.7% | 16.0% | 22.6% | 15.7% | 15.7% | -1.9% [-20.2, +17.8] |

**Findings:**
- **The ranks 4-8 bias is a Harville artefact.**
  - Original Harville under-rates these runners by 1-4 points.
  - Discounted Harville and the place SP both remove almost all of it.
  - The place SP is the closest of all to the actual rate.
- **Our model over-rates ranks 5-8 by 3-7 points.** That is miscalibration, not independent information.
- **ROI at place SP is noise.** No rank has an interval above zero in either period, and signs swap between periods (rank 7: +6.2% then +11.0%; rank 8: +5.0% then -1.9%).

Other cuts of ranks 4-8:
- By odds band: no interval above zero in the holdout.
- 21-41 shots in development were +13.7% [-1.3, +31.9], but -1.8% in the holdout.
- Under-2% win chances lost in both periods: -31.8% development, -31.2% holdout.
- By field size and handicap: no repeatable sign.

**Answer: ranks 4-8 are not mispriced in place markets.** The Harville bias is real, but Betfair's place market does not share it.

## Phase 5 - field size
| Field | Period | Races | Top-3 Brier gain, blend vs market | Top-3 Brier gain, enhanced vs market | Trifecta LL gain, enhanced vs market | Back-all ROI at place SP |
|---|---|---|---|---|---|---|
| 5-7 | Development | 1,760 | -0.0009 [-0.0020, +0.0002] | +0.0012 [-0.0015, +0.0037] | -0.0015 [-0.0106, +0.0067] | +0.5% |
| 8-11 | Development | 1,901 | +0.0002 [-0.0011, +0.0016] | +0.0029 [-0.0001, +0.0060] | +0.0048 [-0.0048, +0.0143] | -3.1% |
| 12-15 | Development | 792 | +0.0012 [-0.0014, +0.0038] | +0.0061 [+0.0017, +0.0101] | +0.0245 [+0.0115, +0.0373] | +12.4% |
| 16+ | Development | 279 | +0.0022 [-0.0012, +0.0057] | +0.0082 [+0.0023, +0.0137] | +0.0443 [+0.0173, +0.0706] | -3.3% |
| 5-7 | Holdout | 480 | -0.0013 [-0.0033, +0.0009] | +0.0005 [-0.0055, +0.0062] | +0.0076 [-0.0084, +0.0253] | -6.8% |
| 8-11 | Holdout | 682 | +0.0001 [-0.0017, +0.0021] | -0.0000 [-0.0045, +0.0045] | +0.0067 [-0.0062, +0.0193] | +1.9% |
| 12-15 | Holdout | 346 | -0.0023 [-0.0056, +0.0011] | +0.0028 [-0.0039, +0.0099] | +0.0172 [-0.0032, +0.0387] | +0.5% |
| 16+ | Holdout | 108 | +0.0032 [-0.0048, +0.0117] | +0.0175 [+0.0060, +0.0304] | +0.0529 [+0.0168, +0.0908] | -7.3% |

**Findings:**
- **Small fields (5-7) are not an opportunity.**
  - Phase 1's large small-field gain was Harville's bias, and the field-size-dependent exponents in the market baseline already capture it.
  - Beyond that baseline, neither our model nor the runner features add anything in 5-7 runner races, in either period.
  - Back-all place ROI there was +0.5%, then -6.8%.
- **The enhanced model's gains are in big fields (12+).** These are races where finishing consistency and experience matter more. The 16+ gain survives the holdout.
- Even there, place-SP ROI does not follow:
  - back-all 12-15 was +12.4% in development but +0.5% in the holdout;
  - 16+ was negative in both.
- No field size needs a separate model beyond the existing field-size exponents.

## Odds bands, race type, handicap (all runners)
Place SP implied vs actual (holdout):

| Odds band | Actual | Place SP implied |
|---|---|---|
| < 3 | 78.2% | 76.2% |
| 3-5 | 58.0% | 58.0% |
| 5-8 | 43.4% | 44.6% |
| 8-13 | 33.1% | 32.8% |
| 13-21 | 23.3% | 23.1% |
| 21-41 | 14.0% | 14.4% |
| 41+ | 6.1% | 5.8% |

- The place market is calibrated in every band.
- Our model on its own is badly compressed: 54% for the < 3 band and 15.5% for the 41+ band.
- Flat vs Jumps:
  - development: -2.0% vs +12.2%;
  - holdout: -1.1% vs -0.7%.
  - The development Jumps figure did not repeat.
- Handicap vs non-handicap:
  - development: -1.5% vs +7.3% [-1.9, +18.9];
  - holdout: -2.8% vs +3.1% [-5.6, +13.1];
  - G (genuine): -8.5% vs -14.4%.
  - Without the top 1% of payouts, non-handicaps go to -25% (development) and -29% (holdout).
  - This was the only S segment with the same sign in both periods, and it failed G. Classed as noise (OPPORTUNITIES.md).
