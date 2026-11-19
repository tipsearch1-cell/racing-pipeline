# Phase 2 - our model vs the market: disagreement analysis

**Disagreement (Δ)** = our place probability (our model + discounted Harville, B) minus a market place probability, in percentage points. Places use the declared-runner rule.

Bands follow the brief. Every band holds at least 6% of development runners, so no band needed merging. Full numbers: out/disagreement.csv. Chart: out/disagreement_holdout.png.

## 1. Against market-derived (09:00 + discounted Harville) place probabilities
**SYNTHETIC holdout, 1 Sep - 12 Oct 2026:**

| Δ band (pp) | Runners | Our P | Market-Harville P | Place SP implied | Actual | Mean place SP | ROI at place SP (2%) [95%] |
|---|---|---|---|---|---|---|---|
| < -15 | 1,769 | 32.2% | 56.7% | 55.0% | **55.8%** | 2.10 | -0.3% [-4.7, +4.0] |
| -15..-10 | 1,080 | 31.1% | 43.5% | 43.7% | **41.3%** | 3.00 | -7.0% [-14.2, +0.3] |
| -10..-5 | 1,583 | 29.7% | 37.0% | 37.4% | **37.4%** | 3.71 | -0.4% [-9.2, +10.0] |
| -5..+5 | 5,504 | 24.9% | 24.3% | 24.7% | **24.8%** | 13.79 | +0.5% [-7.6, +9.0] |
| +5..+10 | 2,629 | 26.2% | 18.8% | 19.1% | **19.2%** | 19.04 | +9.0% [-6.4, +26.2] |
| +10..+15 | 1,587 | 30.2% | 17.9% | 18.2% | **18.1%** | 14.71 | -12.8% [-24.0, -1.6] |
| > +15 | 1,326 | 38.3% | 18.2% | 18.2% | **18.3%** | 15.83 | -9.5% [-22.9, +3.8] |

Development (May-Aug) shows the same pattern:
- **> +15 band:** we say 39.4%, market Harville 19.2%, actual 19.6%.
- **< -15 band:** we say 32.5%, market Harville 57.3%, actual 56.0%.

**Finding: when we disagree with the market, the market is right.** In every band the actual place rate sits on the market line, often within a percentage point. Our model's line is flat and wrong by up to 20 points either way.

Large disagreements identify places where **our model** is miscalibrated, not where the market is. On its own the model has no place information beyond the market.

## 2. Against actual Betfair place SP (the betting comparison)
Δ here = our place probability minus place-SP implied probability (1/PSP, normalised to the places paid).

| Δ band | Development: actual vs SP-implied | Dev ROI [95%] | Holdout: actual vs SP-implied | Holdout ROI [95%] |
|---|---|---|---|---|
| < -15 | 57.5% vs 57.8% | -1.0% [-3.2, +1.2] | 57.5% vs 57.1% | -0.4% [-3.8, +3.3] |
| -15..-10 | 44.5% vs 44.9% | -2.1% [-5.9, +1.8] | 45.8% vs 44.0% | +4.2% [-1.8, +11.0] |
| -10..-5 | 39.2% vs 39.0% | +0.5% [-3.8, +4.8] | 35.8% vs 37.1% | -5.2% [-12.3, +2.1] |
| -5..+5 | 26.9% vs 27.1% | -1.3% [-5.8, +3.7] | 25.3% vs 25.6% | -6.7% [-13.2, +0.2] |
| +5..+10 | 19.4% vs 18.2% | +3.5% [-4.6, +12.5] | 17.1% vs 16.7% | +14.7% [-2.8, +33.4] |
| +10..+15 | 15.8% vs 16.0% | +15.5% [-5.6, +42.1] | 15.6% vs 15.1% | +2.2% [-15.0, +20.2] |
| > +15 | 13.8% vs 14.0% | -1.9% [-11.1, +8.0] | 13.1% vs 13.8% | -11.8% [-24.1, +2.0] |

**Finding:**
- Place SP is almost perfectly calibrated in every band: actual is within about 1-2 points of SP-implied.
- None of the bands where we are more positive than place SP has a 95% interval above zero. Their point ROIs swap sign between periods (+10..+15: +15.5% then +2.2%; > +15: -1.9% then -11.8%).
- The "value" bands are dominated by long prices (mean place SP 19-22), so their intervals are very wide.

The blended model (C) against place SP shows the same picture: holdout bands run from -16% to +4%, and no interval is above zero.

## 3. Genuine archive (G, 10-18 Nov, 217 races)
- Same shape: against market Harville, actual follows the market line.
- Bands where we are 5-15 points above place SP lost:
  - +5..+10: -20% on 106 bets;
  - +10..+15: -69% on 49 bets.
- The sample is far too small for a conclusion, but there is no sign of the opposite.

## 4. Does disagreement predict market movement? (Phase 12 check, exploratory)
Disagreement = log(our win chance) - log(09:00 market chance). Movement = log(BSP-implied chance) - log(09:00 market chance).

| Period | Runners | Slope | Correlation |
|---|---|---|---|
| Development | 43,297 | -0.17 | -0.17 |
| Holdout | 15,701 | -0.26 | -0.27 |

**The market moves away from our model.** Horses we rate above the 09:00 market drift towards the off, and horses we rate below it shorten.

By disagreement decile (holdout), the mean log(BSP / 09:00 Betfair price) rises from 0.26-0.31 in the bottom four deciles to 1.28 in the top decile.

The model's disagreements are therefore partly stale information the market corrects. That is the opposite of an edge for backing. It could be a timing signal: lay early, or wait for BSP. But the 09:00 exchange quotes are too thin to treat as executable, so that is a hypothesis, not a result (OPPORTUNITIES.md).
