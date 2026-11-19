# Phase 3 - model-market disagreement (win)

**Disagreement:**
- in probability points: our model's chance minus the 09:00 market chance (bands below);
- in log terms: dlog = log(model) - log(market), split into its positive part (dpos) and negative part (dneg).

Conditional models are fitted on development (May-Aug) and scored on the re-used period and H3. Files: out/disagreement_bands.csv, out/disagreement_models.csv.

## 1. Who is better calibrated within each band?
| Band (pts) | Set | Runners | Wins | Actual | Our model | 09:00 market | BSP |
|---|---|---|---|---|---|---|---|
| < -10 | Development | 2,993 | 1,042 | 34.8% | 15.7% | 33.3% | 34.4% |
| < -10 | Re-used | 1,007 | 367 | 36.4% | 15.7% | 33.4% | 35.0% |
| < -10 | H3 | 518 | 186 | 35.9% | 15.1% | 33.8% | 35.6% |
| -10..-5 | Development | 3,705 | 708 | 19.1% | 12.1% | 19.2% | 19.5% |
| -5..-2 | Development | 5,144 | 662 | 12.9% | 9.9% | 13.3% | 13.3% |
| -2..+2 | Development | 15,474 | 1,117 | 7.2% | 7.5% | 7.3% | 7.0% |
| +2..+5 | Development | 8,827 | 554 | 6.3% | 10.0% | 6.7% | 6.5% |
| +5..+10 | Development | 5,348 | 444 | 8.3% | 15.0% | 8.1% | 8.2% |
| > +10 | Development | 1,889 | 234 | 12.4% | 25.8% | 11.6% | 12.0% |
| > +10 | Re-used | 562 | 66 | 11.7% | 25.5% | 11.0% | 10.9% |
| > +10 | H3 | 304 | 29 | 9.5% | 23.6% | 9.4% | 9.5% |
| > +10 | A verified | 49 | 6 | 12.2% | 25.3% | 11.0% | 9.9% |

**In every band and every period the market is close to the actual rate; our model is not.**
- Where the model is more than 10 points above the market, it says about 25% and the horse wins 10-12%.
- Where it is more than 10 points below, it says 15% and the horse wins 35%.
- **Large disagreements are systematically wrong in the model's direction**, but slightly *less* wrong than zero information would be: see §2.

## 2. Does disagreement add information beyond the market? (conditional logit)
win ~ log(market) + b+ · dpos + b- · dneg, fitted on development:

| Market at | Coef. on log(market) | b+ (se) | b- (se) | Log-loss gain vs market, re-used | H3 |
|---|---|---|---|---|---|
| 09:00 | 1.19 (0.03) | **+0.16 (0.075)** | +0.08 (0.051) | +0.0028 [-0.0021, +0.0074] | +0.0052 [-0.0026, +0.0112] |
| off-60m | 1.11 | +0.02 (0.074) | +0.03 (0.049) | +0.0034 [+0.0005, +0.0063] | n/a |
| off-10m | 1.07 | -0.01 (0.073) | +0.02 (0.048) | +0.0022 [+0.0001, +0.0043] | n/a |
| off-1s | 1.07 | +0.03 (0.071) | -0.00 (0.048) | +0.0010 [-0.0011, +0.0030] | n/a |

What this shows:
- **At 09:00 a small positive weight on disagreement survives** (b+ z ≈ 2.2; b- z ≈ 1.5). Agreement with our model nudges the market's chance in our direction by about a sixth of the log-gap.
- **From an hour before the off, it is zero.** The market has absorbed it, matching MARKET_MOVEMENT.md.
- Much of the log-loss gain in the table comes from the log(market) coefficient above 1: the market is too flat, and sharpening it helps. That is not our model's information.
- Interactions (dpos/dneg × top-3 in the market, field ≥ 12, Jumps, handicap) add nothing out of sample: re-used +0.0015, H3 +0.0051, both with intervals spanning 0. No coefficient is reliably non-zero except a weak positive-disagreement × handicap term (+0.23, se 0.11), which did not improve held-out loss.

## 3. Answers to the Phase 5 questions
1. **Calibration by band:** the market is calibrated; we are not.
2. **Does disagreement predict movement?** Raw: away (-0.27). Within the same odds band: towards us (+0.05 to +0.14).
3. **Does it predict winning after controlling for the market?** Slightly, at 09:00 only.
4. **Does it become more accurate closer to the off?** No. It becomes irrelevant, because the market already contains it.
5. **Does a blend improve win prediction?** By about 0.2% of log-loss (WIN_CALIBRATION.md).
6. **Beyond rank, field size and race type?** No robust condition found where our model beats the market.

**Large disagreement is not betting value.** It mainly flags the model's own ranking errors.
