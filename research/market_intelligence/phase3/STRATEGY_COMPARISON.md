# Phase 3 - strategy comparison (win back bets, £1 fixed)

All strategies were predefined in the sealed spec. Parameters (E's drift cap k, F's disagreement cap u) were chosen on development only: k = 30%, u = 0.25.

**Prices:**
- **Exchange:** the provider's Betfair-exchange quote at the decision checkpoint, after 2% or 5% commission.
- **Bookmaker best:** the highest bookmaker price at the checkpoint. This is a best case: no Rule 4, no stake limits, no account restrictions.

**All results are conditional simulations** (EXECUTION_REVIEW.md). Intervals are 95% day-block bootstraps. The pass rule uses a Bonferroni 99.9% interval.

Full detail is in out/strategy_cells.csv (198 cells: bets, stake, returns, P/L, ROI, intervals, average and median odds, max drawdown, longest losing run, monthly P/L, CLV, ROI without the top 1%, simulated null). Pass table: out/strategy_pass.csv. Market-only controls: out/control_market_only_*.csv.

## Headline (EV ≥ 4%)
| Strategy | Decision | Price | Development ROI [95%] | Re-used ROI | H3 ROI [95%] | Avg / median odds (dev) | ROI without top 1% (dev) |
|---|---|---|---|---|---|---|---|
| A original model | 09:00 | exchange 2% | -21.3% [-26.8, -15.6] | -21.4% | -14.1% [-28.7, +6.2] | 38.5 / - | -50.9% |
| A original model | 09:00 | bookmaker | -15.9% [-21.5, -10.0] | -17.9% | -15.2% [-29.5, +3.6] | 33.4 | -49.6% |
| B calibrated | 09:00 | exchange 2% | -21.6% [-26.7, -16.2] | -21.7% | -14.3% | 38.5 | -51.2% |
| **C blend** | 09:00 | exchange 2% | **+6.0% [-4.4, +17.9]** | **+4.4%** | **+14.7% [-4.2, +32.8]** | 91.5 / 7.4 | -17.0% |
| C blend | 09:00 | bookmaker | -11.3% [-21.3, +0.1] | +14.4% | +24.5% [-2.5, +52.1] | 35.4 | -43.5% |
| F disagreement 0-0.25 (u chosen on dev) | 09:00 | exchange 2% | +39.6% [+13.1, +70.0]* | +1.8% | +30.1% [-36.5, +99.9] | 9.3 | +19.3% |
| D market confirmation | off-60m | exchange 2% | +18.0% [-11.5, +51.2] | -0.5% | not testable | 267 | -6.8% |
| D market confirmation | off-60m | bookmaker | +29.8% [+4.7, +54.6] | +24.7% | not testable | 9.0 | +9.1% |
| E drift avoidance (k = 30%) | off-60m | exchange 2% | -15.2% [-31.0, +3.0] | +13.7% | not testable | 193 | -37.6% |
| E drift avoidance | off-60m | bookmaker | +1.0% [-19.8, +31.2] | +21.9% | not testable | 31.8 | -30.8% |
| Blend at off-60m | off-60m | exchange 2% | -17.9% | -9.2% | not testable | | |
| Blend at off-10m | off-10m | bookmaker | +3.7% | +29.3% | not testable | 13.3 | |
| Blend at off-1s | off-1s | bookmaker | +7.5% | +0.4% | not testable | 8.0 | |

\* F's cap was chosen on development to maximise ROI, so its development figure is in-sample.

## Pass test (sealed rule)
Strategies evaluable on H3 are A, B, C and F at 09:00: 36 cells.

| Condition | Cells passing |
|---|---|
| H3 Bonferroni lower bound > 0 | **0 / 36** (best: C blend, bookmaker, EV ≥ 8%: -1.9%) |
| Positive in development AND re-used AND H3 | 11 / 36: all 6 **C blend at the exchange price** cells, plus 5 F cells (F's cap was tuned on development) |
| Mean CLV vs BSP > 0 on H3 | C and F only |
| **All conditions** | **0 / 36** |

D, E and the timing rules need off-60m, off-10m or off-1s prices, which H3 does not have. They can reach "preliminary" at best.

## What the controls show (market only, no model)
The same rules using only the market's own probability:

| Rule | Price | Development | Re-used | H3 |
|---|---|---|---|---|
| Market EV ≥ 4% at 09:00 | exchange 2% | -6.9% | -1.5% | -2.0% |
| Blend EV ≥ 4% at 09:00 | exchange 2% | +6.0% | +4.4% | +14.7% |
| Market EV ≥ 4% at 09:00 | bookmaker | -9.0% | +10.9% | +45.5% |
| Blend EV ≥ 4% at 09:00 | bookmaker | -11.3% | +14.4% | +24.5% |
| D market-only (shortened 09:00 -> off-60m, market EV ≥ 4% at off-60m) | bookmaker | +17.7% | +45.7% | n/a |
| D with our model | bookmaker | +29.8% | +24.7% | n/a |

What the controls show:
- **At bookmaker prices our model adds nothing.** The market-only rules do as well or better, and swing wildly between periods. Those results are about generous early or stale bookmaker prices plus a few huge winners, not about our model. They are also the prices most exposed to limits, Rule 4 and account restrictions.
- **At the exchange price, the blend does beat the market-only rule in every period** (+6 to +17 points at EV ≥ 4%), and C is the only rule positive in all three periods. This is the one **preliminary signal** in Phase 3. But:
  - every interval includes zero;
  - it fails the Bonferroni rule;
  - without the top 1% of payouts it is -9% to -19%;
  - its average odds (60-135) show it depends on long-priced morning exchange quotes whose depth is unknown.

## Risk profile (C blend, exchange 2%, EV ≥ 4%)
| Set | Bets | P/L | ROI | Max drawdown | Longest losing run | Months profitable | Raw CLV vs BSP | ROI without top 1% | Null p |
|---|---|---|---|---|---|---|---|---|---|
| Development | 2,528 | +£150 | +6.0% | £101 | 45 | 2 of 4 | +16.7% | -17.0% | 0.64 |
| Re-used | 1,110 | +£48 | +4.4% | £45 | 17 | 1 of 2 | +13.7% | -18.1% | 0.51 |
| H3 | 575 | +£84 | +14.7% | £54 | 18 | 1 of 2 | +21.6% | -13.5% | 0.43 |

Null p = the share of 1,000 simulations drawing outcomes from BSP probabilities that did at least as well.

The observed returns are **fully compatible with no edge**: null p is 0.43-0.64.
