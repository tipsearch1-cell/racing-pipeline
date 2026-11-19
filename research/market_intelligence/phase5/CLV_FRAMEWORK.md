# Phase 5 - closing-line value framework

**Status:**
- The forward CLV code is in place (`fwd.py clv`) and runs once forward days are settled. There is nothing to report yet.
- On historical data, selections at 09:00 beat BSP on average, but only through long-priced morning quotes whose fills are doubtful.
- Selections from an hour before the off onwards lose to BSP.

## Definitions (pre-specified, spec section 9)
| Field | Definition |
|---|---|
| Decision price | Provider "Betfair Exchange" back quote in the decision snapshot (09:00 for E; 21:00 for X1). Price type `exchange_back`, no depth |
| Liquidity | **Not available** (no Betfair key). Recorded as unknown, never inferred |
| Closing price | BSP from results. Also the last pre-off sweep quote, when a sweep exists before the off |
| Absolute CLV | log(decision quote / BSP). Above 0 means the bet was struck at a bigger price than BSP |
| Relative CLV | Absolute CLV minus the mean absolute CLV of all runners in the same period and decision-odds band (<3, 3-6, 6-11, 11-21, 21+) |
| Implied-probability change | 1/BSP − 1/quote |
| Share beating the close | Share of selections with absolute CLV > 0 |
| Breakdowns | By odds band and by decision snapshot time (21:00 / 09:00 / off−60 / off−10) |

**Rule:** relative CLV is reported but never presented as profit. A selection set with negative absolute CLV is called *losing to the close*, however it compares with similar-priced runners. CLV is not proof of ROI.

## Historical illustration (exploratory; previously examined data)
Selections are runners with EV ≥ 4% at the decision quote after 2% commission. Each model is walk-forward at its checkpoint.

| Decision time / model | Period | Selections | Median quote | Absolute CLV [95%] | Beat BSP | Relative CLV |
|---|---|---|---|---|---|---|
| 21:00, market-anchored D1 | Development | 2,209 | 5.3 | −0.027 [−0.049, −0.006] | 49.7% | +0.91 |
| 21:00, market-anchored D1 | Re-used Sep-Oct | 841 | 4.8 | −0.029 [−0.057, −0.003] | 48.6% | +0.87 |
| 09:00, hybrid E | Development | 2,571 | 7.2 | +0.077 [+0.057, +0.095] | 55.6% | +0.47 |
| 09:00, hybrid E | Re-used Sep-Oct | 1,118 | 6.4 | +0.052 [+0.026, +0.078] | 53.4% | +0.44 |
| 09:00, hybrid E | Re-used H3 | 590 | 9.2 | +0.082 [+0.017, +0.139] | 57.6% | +0.45 |
| off−60, D1 | Development | 9,501 | 16.0 | −0.107 | 39.4% | +0.14 |
| off−60, D1 | Re-used Sep-Oct | 3,337 | 18.5 | −0.166 | 35.2% | +0.10 |
| off−10, D1 | Development | 13,032 | 23.0 | −0.124 | 36.7% | +0.03 |
| off−10, D1 | Re-used Sep-Oct | 4,407 | 28.0 | −0.118 | 36.3% | +0.05 |

**Reading:**
- **09:00 E selections** show positive absolute CLV in all three periods.
  - The mean quote is about 90 (median 6-9). The gain comes largely from long morning quotes that are bigger than BSP.
  - Adverse fills are where execution is likely to fail (EXECUTION_FRAMEWORK.md).
- **Off−60 and off−10:** selections lose to BSP. This is consistent with Phase 3-4: no model value close to the off.

## Forward procedure
`fwd.py clv` builds the selection table (out/clv_forward.csv) from:
- the 09:00 predictions;
- the 09:00 snapshot's Betfair quote;
- the last pre-off sweep quote;
- the archived results.

It is run at the pre-registered looks, alongside the primary analysis and never instead of it.
