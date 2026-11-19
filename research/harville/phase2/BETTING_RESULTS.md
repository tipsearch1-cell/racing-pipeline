# Phase 2 - betting results (place market)

## Execution assumptions
**Order type:** a Betfair place-market back bet at BSP with a limit (limit-on-close).
- Limit price L = the price at which EV = T for our place probability: L = 1 + ((1 + T)/P - 1)/(1 - c).
- Only pre-race information (09:00 market, our model, earlier runs) sets P. The closing price never decides.
- The order is treated as filled at place SP if and only if place SP ≥ L.

**Not reconstructable:**
- BSP pool volume and reconciliation, so partial or unmatched LOC orders can't be modelled. A large LOC back order also pushes the BSP down.
- **All returns below are CONDITIONAL SIMULATIONS (assumes full fill at the final place SP), not verified executable returns.**

**Settlement:**
- Places paid = Betfair terms on declared runners (99.2% agreement with Betfair's own settlement on 5+ runner races).
- Dead heat at the last place splits the stake.
- Non-runners need no reduction factor (BSP).
- Races with fewer than 5 runners are never bet.

**Strategies:** models B, C, D × EV threshold T ∈ {0, 2, 4, 6, 8, 10}% × commission 2% / 5% = 36 cells. Model A is a benchmark.

**Pass rule (sealed), all four needed:**
1. Holdout ROI lower bound > 0 at the Bonferroni level (99.86%);
2. profit in both holdout months;
3. profit in at least 3 of 4 development months;
4. positive ROI in G.

**Not testable:**
- **Each-way:** no archived bookmaker each-way terms or place prices; exchange win BSP was not used to make them up.
- **Exacta/trifecta:** no pre-race executable prices. Tote/CSF dividends exist for only 221 races (10 Nov onwards), and none for the replay period. Probability accuracy is in MODEL_COMPARISON.md.

## Result: 0 of 36 cells pass
| Condition | Cells meeting it |
|---|---|
| Holdout Bonferroni lower bound > 0 | 0 / 36 (best: -9.9%) |
| Holdout ordinary 95% lower bound > 0 | 0 / 36 |
| Profit in both holdout months | 0 / 36 (every cell: September up, October down) |
| Profit in ≥ 3 of 4 development months | 0 / 36 (27 cells profitable in 1 month, 9 in 2) |
| Positive in G | 0 / 36 (G ROI -20% to -35%) |

Selected cells at 2% commission:

| Method | Development ROI [95%] | Holdout ROI [95%] | Holdout bets | G ROI [95%] |
|---|---|---|---|---|
| Benchmark: back everything | +1.4% [-2.0, +5.7] | -1.0% [-4.5, +2.9] | 14,362 | -10.6% [-18.0, +3.3] |
| A market + discounted Harville, EV ≥ 0 | +4.1% [-2.6, +12.6] | +0.8% [-6.9, +8.5] | 7,482 | -23.2% [-37.5, +4.1] |
| B our model, EV ≥ 0 | +4.6% [-2.5, +12.6] | +1.1% [-6.3, +8.6] | 7,738 | -21.0% [-36.0, +8.9] |
| C blend, EV ≥ 0 | +3.8% [-3.1, +12.0] | +1.0% [-6.4, +9.6] | 7,432 | -19.7% [-34.4, +8.3] |
| D enhanced, EV ≥ 0 | +4.6% [-2.1, +12.7] | +0.9% [-6.3, +9.0] | 7,444 | -23.8% [-35.7, -3.7] |
| D enhanced, EV ≥ 4% | +4.3% [-3.2, +12.7] | +1.9% [-6.8, +11.0] | 6,653 | -24.7% [-37.5, -2.3] |
| C blend, EV ≥ 10% | +5.8% [-3.1, +16.3] | +1.3% [-9.0, +12.0] | 5,631 | -35.2% [-58.7, -4.1] |

**Our information adds nothing to the betting result.** At every threshold, B, C and D are within about a point of the pure-market rule A on the same races. Whatever ROI there is comes from the place-SP lottery, not from our probabilities.

## Where the development "profit" came from
- **The development period is positive only because of June.** Every cell made +£1,040 to +£1,170 in June and was flat or negative in May, July and August. For example, B at EV ≥ 0 went -£138, +£1,126, +£95, -£32.
- June contains the biggest payouts in the data (place SP 500.85 and 310 placers, 14-15 June).

At 5% commission every holdout cell is negative (-2.3% to -0.5%).

## Uncertainty and outlier profile (full detail: out/betting_tables.md, out/betting_cells.csv)
Holdout cells at 2% commission:
- median place SP 5.8-8.0, mean 19-24;
- largest single return 98;
- without the top 1% of payouts, P/L falls from about +£30 to +£128 to between -£1,770 and -£2,100 on 5,600-7,700 bets (about -25% to -30% ROI).

**Simulated ROI under two probability sets** (1,000 draws, the same bets):

| | Development | Holdout |
|---|---|---|
| Model's own probabilities (what it claims) | +84% to +229% | +64% to +229% |
| Place-SP implied (no-edge null), mean | about -1% | about -1% |
| Share of null draws at least as good as observed | 2-5% | 25-35% |

- The model's claimed ROI is absurd against the observed +1%: its EV is badly over-stated (see ROBUSTNESS.md §3).
- The development share of 2-5% looks interesting, but these draws assume independent outcomes and no day clustering, so they are overconfident. The day-block intervals above all include zero.
- The holdout is fully consistent with no edge.

## Genuine archive (G)
- 217 races, 10-18 Nov; 1,107 runners with a place SP.
- Every strategy lost 20-35%. Backing everything lost 10.6%. This is a small, unlucky week for longer-priced runners.
- With the reviewer's chance as the input, B and C lost 19-25% (out/betting_cells.csv, period G_rev).
- G cannot pass anything on its own, but it gives no support to a hidden edge.
