# Phase 2 - ranked follow-up opportunities

Scores run 1 (weak) to 5 (strong). "Evidence" means evidence from this study. Established findings are kept separate from untested hypotheses.

## Established by Phase 2
1. Betfair place SP is well calibrated in every odds band, rank, field size and code tested.
2. Our model alone is far less accurate than the 09:00 market. Blended in, it adds a small, stable amount of win information (weight about 0.1).
3. When our model and the market disagree on place chances, the outcome follows the market.
4. The market moves away from our model's disagreements between 09:00 and the off.
5. Finishing consistency and experience improve 2nd/3rd estimates beyond the win probability, mainly in fields of 12+.
6. No place-betting rule based on 09:00 information beat place SP after commission.

## Ranked opportunities
| # | Opportunity | Evidence | Incremental value | Data available | Ease | Real betting chance | Status |
|---|---|---|---|---|---|---|---|
| 1 | **Decide place bets near the off.** Use T10/L checkpoint prices instead of 09:00, so the probability already contains the late information that currently hurts us (adverse selection). Pair with a place-market limit, not BSP. | 4 (the drifter mechanism is shown) | 3 | 4: T10/L win prices archived for a year; place SP yes; place-market pre-off prices no | 3 | 2 | **Untested hypothesis**, needs archived pre-off place-market prices for a credible execution test |
| 2 | **Record our own forward data properly.** Archive every day's model chances, the enhanced 2nd/3rd probabilities, 09:00 and pre-off place-market prices (back/lay and volume), and place SP. | 5 (G is only 217 races) | 5 | 0 today, builds automatically | 4 | n/a (enabler) | Recommended; it is the precondition for everything else |
| 3 | **Use the enhanced finishing model (D) for exacta/trifecta pricing.** It gives the best trifecta log-loss (holdout +0.012, G +0.04), with gains in 12+ runner fields. | 3 | 3 | 1: Tote/CSF dividends only since 10 Nov; no pool snapshots | 3 | 2 | Accuracy established; profitability untested |
| 4 | **Timing signal from model-market disagreement**, e.g. lay early when we rate a horse above the market, or wait for BSP when we like it. Horses we rate above the market drift (holdout correlation -0.27). | 3 | 2 | 2: 09:00 exchange quotes too thin to treat as executable | 2 | 2 | Untested hypothesis |
| 5 | **Disagreement as a bet filter**, e.g. skip place bets where we are well above the market. | 2 | 1 | 4 | 5 | 1 | Weak: the bands that lost (+10..+15 holdout -12.8%) were not consistent across periods |
| 6 | **Runners whose place chance is high relative to their win chance** (consistent, experienced types; D's position-score and run-count terms). Compare against the place SP specifically. | 2 | 2 | 4 | 3 | 2 | Untested against prices: D's place probabilities did not beat place SP in betting |
| 7 | Small fields (5-7) / ranks 4-8 / non-handicaps / Jumps | 1 | 1 | 4 | 5 | 1 | **Rejected as edges.** Harville artefacts the place market does not share, or one-period noise (non-handicaps: +7.3% dev, +3.1% holdout, -14% G) |
| 8 | Each-way at bookmaker prices | 0 | ? | 0: no terms or place prices archived | 2 | ? | Not testable until EW terms and prices are archived |

## Single most promising direction
Start **#2** now; it costs nothing, because the daily build already produces most of it. Then test **#1** once a few months of pre-off place-market prices exist.

Phase 2 shows the problem is not the finishing-position maths. The place SP already knows what our 09:00-based model knows, and more. Any edge must therefore come either from better timing or from information the market doesn't have, and neither can be shown with the archive we hold today.
