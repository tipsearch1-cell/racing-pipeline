# Phase 3 - bet timing: early price vs late information

**Decision points with real archived prices (replay set S3 only, May - 12 Oct 2026):**
- 09:00;
- 60 minutes before the off;
- 10 minutes before the off;
- 1 second before the off.

**Not available:** 30, 15 and 5 minutes before the off (DATA_AUDIT.md). These are not interpolated. They are planned in the forward archive (FORWARD_ARCHIVE.md). H3 has only 09:00, so no timing comparison is possible on untouched data.

## 1. Information: how much does our model add at each time?
Blend weight on our model, fitted on training months (out/params.json, chart out/model_weight_by_time.png):

| Fit window | 09:00 | off-60m | off-10m | off-1s |
|---|---|---|---|---|
| to Jul | 0.100 | 0.036 | 0.022 | 0.013 |
| to Sep | 0.108 | 0.038 | 0.020 | 0.011 |
| all (Mar - 12 Oct) | 0.094 (se 0.026) | 0.027 | 0.011 | 0.002 |

Market accuracy improves through the day (win log-loss, development):

| 09:00 | off-60m | off-10m | off-1s | BSP |
|---|---|---|---|---|
| 1.802 | 1.770 | 1.762 | 1.757 | 1.747 |

**Late information is real, and it replaces our model.** By an hour before the off, about 70% of our model's weight is gone. By the off, essentially all of it is.

## 2. Price: what do you get at each time?
- Median BSP divided by the exchange quote: 1.26 at 09:00, 1.11 at off-60m, 1.07 at off-10m, 1.04 at the off.
- The morning exchange quote is **shorter** than the eventual BSP. In thin morning markets the back price on offer is poor, so there is no general "early price advantage" on the exchange.
- Bookmaker prices are a different matter. The best bookmaker price can exceed fair value early, but that is a bookmaker-margin and limits question (STRATEGY_COMPARISON.md controls).

## 3. Results by decision time
Blend EV ≥ 4%, 2% commission at the exchange price, or bookmaker best:

| Decided at | Exchange: development / re-used ROI | Bookmaker best: development / re-used ROI | Bets (development, bookmaker) | Probability CLV, development / re-used (EV ≥ 0) |
|---|---|---|---|---|
| 09:00 | +6.0% / +4.4% | -11.3% / +14.4% | 6,451 | -0.487 / -0.217 |
| off-60m | -17.9% / -9.2% | -19.0% / +19.9% | 1,681 | -0.359 / -0.013 |
| off-10m | -11.4% / -16.7% | +3.7% / +29.3% | 830 | -0.047 / +0.025 |
| off-1s | +7.1% / +2.6% | +7.5% / +0.4% | 1,036 | -0.017 / +0.033 |

No timing is consistently better.
- Every interval includes zero.
- Signs change between periods.
- The late bookmaker figures depend on a few hundred bets at stale bookmaker prices.

CLV improves mechanically the later you decide: there is less time left for the price to move.

## Conclusion
- **Early price advantage:** not shown for the exchange, where morning quotes are short.
- **Late information advantage:** real for the market, but it removes our model's contribution rather than adding to it.
- **Waiting does not improve our decisions in a way that shows up in ROI.**
- A proper test needs executable back prices **with depth** at 09:00, 60, 30, 15 and 5 minutes before the off. That data does not exist here; the forward archive is designed to collect it.
