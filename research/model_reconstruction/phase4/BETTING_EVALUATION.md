# Phase 4 - limited betting evaluation (secondary)

**Pre-specified rule:** one rule, no threshold search. Back at 09:00 when EV ≥ 4% at:
- (i) the Betfair-exchange quote after 2% commission (5% shown too); or
- (ii) the best bookmaker price (best case: no Rule 4, no limits).

Results are **conditional simulations**: no depth data, no verified fills. The periods are development or re-used, **not independent**. Full table: out/betting.csv.

| Model | Price | Development ROI [95%] | Re-used ROI | H3 ROI | Bets (development) | Average odds | Probability CLV (development) | 5% commission (development) |
|---|---|---|---|---|---|---|---|---|
| Existing model | exchange | -21.3% [-26.7, -15.8] | -21.4% | -14.1% | 17,927 | 38 | -0.31 | -23.5% |
| Market only (control) | exchange | -6.9% [-19.7, +7.3] | -1.5% | -2.0% | 3,630 | 93 | -0.29 | -9.4% |
| A Improved | exchange | -18.1% [-23.9, -12.3] | -19.9% | -13.0% | 17,137 | 39 | -0.29 | -20.4% |
| C Listwise | exchange | -20.5% | -20.8% | -16.6% | 17,638 | 39 | -0.29 | -22.7% |
| D1 Residual | exchange | -3.1% [-11.0, +4.9] | -6.5% | +1.5% | 5,516 | 53 | -0.12 | -5.6% |
| D2 Residual | exchange | 0.0% [-9.8, +10.4] | +11.0% | +3.4% | 4,095 | 76 | -0.20 | -2.7% |
| E Hybrid | exchange | +7.4% [-2.6, +18.8] | +7.6% | +14.9% | 2,572 | 91 | -0.16 | +4.7% |
| E Hybrid | bookmaker best | -10.6% [-20.8, +0.1] | +15.3% | +23.5% | 6,472 | 35 | -0.60 | n/a |
| Market only | bookmaker best | -9.0% | +10.9% | +45.5% | 9,268 | 41 | -0.65 | n/a |

**Reading:**
- **Better accuracy shows up as smaller losses.** The independent models lose less than the existing model (-18% vs -21%), but still lose heavily.
- **E repeats Phase 3's "blend at the exchange price" pattern:** positive in all three periods, but every interval includes zero. It depends on long-priced morning quotes (average odds about 90) whose depth is unknown. Phase 3 showed that adverse fills turn this kind of result negative (-24% to -29%).
- **Bookmaker-price results are driven by the market control** as much as by any model, and are the least executable.
- **No model is chosen on ROI.** The shadow test is about prediction (log-loss), not betting.
- Drawdowns (development): existing model about £4,000 on £17,900 staked; E about £70 on £2,600.
