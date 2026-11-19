# Phase 3 - execution and liquidity

## What exists
| Item | Status |
|---|---|
| Back prices | One "Betfair Exchange" price per runner per checkpoint (plus Matchbook and Smarkets, about 15% coverage), as delivered by the Racing API. It is not known whether it is best-back, last-traded or indicative. |
| Lay prices / spread | **None** |
| Available depth / traded volume | **None** |
| Market suspensions, actual off | **None** (scheduled off only) |
| Commission | Assumed 2% and 5% |
| Matched-bet records | Only the live bot's own bets (MB Bot Manager, Matchbook). Their fill records are on the VPS/bot side, not in this repo. |

## Classification
| Result | Class |
|---|---|
| Every Phase 3 strategy ROI | **Conditional simulation**: a price exists, fills cannot be reconstructed |
| Live bot bets (CLV vs BSP) | Price at publication (Matchbook 09:00) vs BSP. **Not verified execution**: actual matched prices were not available here |
| Verified execution | **None available** |

## Sensitivity (development / re-used, exchange 2%, EV ≥ 4%; out/strategy_cells.csv rows marked "|")
| Strategy | Full fill | Random 75% fill | Random 50% fill | Adverse fill: filled only if the off-60m quote ≥ the 09:00 quote |
|---|---|---|---|---|
| A original | -21.3% / -21.4% | -22.7% / -20.1% | -21.6% / -20.2% | **-39.7% / -45.1%** |
| B calibrated | -21.6% / -21.7% | -23.4% / -22.6% | -15.3% / -21.6% | **-39.7% / -45.4%** |
| C blend | +6.0% / +4.4% | +5.4% / +10.6% | -1.1% / +11.7% | **-23.9% / -29.4%** |
| F disagreement | +39.6% / +1.8% | +36.4% / +8.5% | +35.9% / -23.6% | +32.7% / -26.7% |

- Random partial fills change only the variance, not the expected return.
- **Adverse selection is the real risk.** A morning back order that only gets matched when the horse later drifts is exactly what a thin early exchange market produces. Under that rule, C's apparent +4% to +6% becomes -24% to -29%.
- C's selections average odds of 60-135 at 09:00, in markets with unknown depth. A one-pound stake might be fillable; anything larger very likely is not.

**Conclusion:** no apparent edge survives a plausible adverse-fill assumption. Without order-book data, none can be verified.
