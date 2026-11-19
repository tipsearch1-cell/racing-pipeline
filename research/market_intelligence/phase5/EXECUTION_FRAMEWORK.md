# Phase 5 - executable betting evidence (framework + historical conditional simulations)

**Bottom line:**
- No historical rule survives conservative fill assumptions.
- The 09:00 E rule shows +7% to +15% at the quoted price. It turns to **−25% to −37%** if bets are matched only when the market drifts against them. That adverse-fill case is what an unseen order book makes likely.
- No bets are placed and no execution is enabled. Betting analysis is secondary to the probability test.

## Pre-specified scenarios (spec section 9; no threshold search)
| Scenario | Assumption |
|---|---|
| S1 Full fill at quote | Every selection matched at the decision quote (optimistic upper bound) |
| S2 BSP | Every selection taken at BSP |
| S3 Adverse fills | Matched at the quote **only if BSP ≥ quote** (the market drifted, so a counterparty was willing). Selections that shortened are missed |
| S4 Haircut | Quote less 5% |

**Common settings:**
- 2% commission and level stakes of 1 unit.
- Stake size is unknown because depth is unavailable, so every result is a **conditional simulation**.
- Matching probability is approximated only by S3's fill rate.

## Historical results (exploratory; ROI per unit staked)
| Rule | Period | Bets | S1 quote | S2 BSP | S3 fill rate | S3 adverse | S4 haircut |
|---|---|---|---|---|---|---|---|
| 09:00 hybrid E | Development | 2,571 | +7.4% | −9.0% | 44% | −37.4% | +2.0% |
| 09:00 hybrid E | Re-used Sep-Oct | 1,118 | +7.6% | −9.5% | 47% | −35.1% | +2.2% |
| 09:00 hybrid E | Re-used H3 | 590 | +14.9% | +4.2% | 42% | −25.5% | +9.2% |
| 21:00 market-anchored D1 | Development | 2,209 | +3.9% | −2.5% | 50% | −28.1% | −1.3% |
| 21:00 market-anchored D1 | Re-used Sep-Oct | 841 | +9.5% | +5.9% | 51% | −18.3% | +4.1% |
| off−60 D1 | Development | 9,501 | −8.6% | −4.4% | 61% | −30.1% | −13.2% |
| off−10 D1 | Development | 13,032 | −9.4% | +0.9% | 63% | −22.4% | −14.0% |

**Reading:**
- The positive S1 numbers depend on long quotes (mean about 90 at 09:00) with few winners. As Phase 4 found, their intervals include zero.
- At BSP the 09:00 rule loses in two of three periods.
- Under adverse fills every rule loses heavily.
- The evening rule is less extreme, but it also loses under adverse fills. Its quotes are about half of BSP, so "fill at quote" is especially doubtful there.

## Forward procedure
- `fwd.py clv` computes S1-S3 for the forward 09:00 E selections (out/clv_forward.csv), using archived quotes, sweeps and results.
- It is run at the pre-registered looks only.
- Until Betfair depth and matched-volume data exist, forward returns stay labelled as conditional simulations.
- **Passing the accuracy test would not authorise betting.** That would need a separate execution study with real order-book data and a sealed profitability test.
