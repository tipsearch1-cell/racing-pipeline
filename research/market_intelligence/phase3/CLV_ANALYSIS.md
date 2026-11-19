# Phase 3 - closing-line value (CLV)

**Conventions:**

| Measure | Formula | Notes |
|---|---|---|
| **Probability CLV (primary)** | log(closing chance / chance at selection), both normalised over the race (no overround) | Closing chance = 1/BSP normalised; selection chance = 09:00 composite. Positive = the horse shortened |
| Raw CLV | selection odds / BSP - 1 | Selection odds = best bookmaker price at 09:00 (best case, see below) |
| Commission-adjusted CLV | bookmaker odds / (1 + (BSP - 1) × 0.98) - 1 | Compares a fixed-odds price with BSP after 2% commission |
| Realised profit | at the selection price and at BSP | Not the same thing as CLV |

**Why the primary is probability CLV:**
- Raw CLV compares two different price sources, bookmaker best and BSP. Bookmaker prices carry their own margin and are much shorter than BSP for outsiders.
- Raw CLV is also biased in favour of whatever a rule selects, because the rule selects on that same price.
- Every comparison is against **odds-band-matched controls**: runners in the same 09:00 price bands, not selected, reweighted to the selection's band mix.

**Selections:**
- calibrated model with EV ≥ 0 at the 09:00 best bookmaker price;
- blend with EV ≥ 0 at the same price;
- the live bot-file bets (A).

Full detail, including every cut: out/clv.csv.

## Results
| Set | Selection | n | Probability CLV, mean log [95%] | Matched control | Selection minus control | Share that shortened | Raw CLV vs BSP | ROI at bookmaker best | ROI at BSP (2%) |
|---|---|---|---|---|---|---|---|---|---|
| Development | calibrated model | 23,197 | -0.392 [-0.409, -0.373] | -0.446 | **+0.054** | 33.7% | -15.6% | -16.4% | -3.6% |
| Development | blend | 8,660 | -0.487 [-0.525, -0.447] | -0.276 | **-0.211** | 34.4% | -1.2% | -8.4% | -19.0% |
| Development | all runners | 43,372 | -0.260 | n/a | n/a | 39.3% | -14.1% | -15.1% | -3.0% |
| Re-used | calibrated model | 8,238 | -0.377 [-0.406, -0.349] | -0.439 | **+0.062** | 33.5% | -20.1% | -18.3% | -5.1% |
| Re-used | blend | 2,001 | -0.217 [-0.274, -0.157] | -0.174 | **-0.043** | 46.1% | +5.3% | +8.0% | -4.1% |
| **H3 untouched** | calibrated model | 3,506 | -0.363 [-0.401, -0.324] | -0.387 | **+0.024** | 30.7% | -20.6% | -16.1% | +22.1%* |
| **H3 untouched** | blend | 765 | -0.152 [-0.196, -0.105] | -0.180 | **+0.029** | 46.7% | +16.6% | +32.6%* | +24.0%* |
| H3 | all runners | 6,432 | -0.248 | n/a | n/a | 36.7% | -17.3% | -16.4% | +8.3%* |

\* H3 returns are dominated by two winners at BSP 670 and 480. Backing every runner at BSP returned +15.7% in H3's complete-BSP races, and -11.0% without its five biggest winners. This is variance, not edge.

How to read it:
- The negative mean probability CLV for *all* runners is the favourite-longshot pattern: outsiders' 09:00 composite chances shrink by BSP. That is why matched controls are essential.
- **Calibrated-model selections beat their odds-matched controls by +0.02 to +0.06 log points in all three periods.** This matches the within-band movement finding (MARKET_MOVEMENT.md): the market drifts towards the model.
- The effect is small next to the price gap. Selections still lose 15-21% at bookmaker best prices and 4-5% at BSP in the replay periods.
- Blend selections do not beat their controls consistently: -0.21, -0.04, +0.03.

### Probability CLV of calibrated-model selections by cut
Mean log; share shortened in brackets.

| Cut | Development | Re-used | H3 |
|---|---|---|---|
| 09:00 odds ≤ 3 | +0.027 (58%) | -0.003 (54%) | +0.035 (54%) |
| 3-5 | -0.006 (52%) | -0.008 (53%) | -0.024 (46%) |
| 5-8 | -0.017 (53%) | -0.018 (50%) | -0.064 (44%) |
| 8-13 | -0.094 (44%) | -0.131 (41%) | -0.108 (41%) |
| 13-21 | -0.189 (37%) | -0.197 (36%) | -0.163 (35%) |
| 21-51 | -0.503 (27%) | -0.456 (29%) | -0.394 (27%) |
| 51+ | -1.361 (8%) | -1.163 (10%) | -1.100 (9%) |
| Model chance ≥ 35% | -0.003 (52%) | -0.019 (52%) | +0.026 (52%) |
| Model chance < 5% | -0.940 (16%) | -0.798 (19%) | -0.775 (17%) |
| Disagreement > +10 pts | -0.142 (44%) | -0.230 (38%) | -0.143 (41%) |
| Field ≤ 7 | -0.245 | -0.287 | -0.201 |
| Field 16+ | -0.547 | -0.586 | -0.511 |

Monthly stability (calibrated selections): -0.397, -0.385, -0.394, -0.391 (May-Aug), -0.375, -0.382 (Sep-Oct), -0.371, -0.358 (Oct-Nov H3). Very stable, because it is dominated by the longshot mix.

**By selection time** (blend EV ≥ 0 at that checkpoint's best bookmaker price; probability CLV from that checkpoint to BSP):

| Decided at | Development n / mean log / shortened | Re-used n / mean log / shortened |
|---|---|---|
| 09:00 | 8,660 / -0.487 / 34% | 2,001 / -0.217 / 46% |
| off-60m | 3,160 / -0.359 / 40% | 700 / -0.013 / 53% |
| off-10m | 2,153 / -0.047 / 50% | 691 / +0.025 / 58% |
| off-1s | 2,640 / -0.017 / 53% | 1,641 / +0.033 / 64% |

Later decisions show better CLV almost mechanically, because there is less time left for the price to move.

## Live bot bets (category A, 11-18 Nov, 32 with BSP)
| Group | n | Beat BSP (Matchbook 09:00 > BSP) | Mean raw CLV | Median | ROI at Matchbook | ROI at BSP |
|---|---|---|---|---|---|---|
| All | 32 | 53% | +4.2% | +2.2% | -46.6% | -42.3% |
| Favourite checks | 30 | 53% | +6.0% | +2.2% | -43.1% | -38.5% |
| Value flags | 2 | 50% | -22.7% | | -100% | -100% |

- The live favourite checks were taken at slightly better than BSP on average (Matchbook 09:00 vs BSP).
- Realised returns were very poor over these 32 bets (5 winners), which is far too few to judge.
- Positive CLV did not equal profit here, as the brief warns.

## Conclusion
- **Proven:** none.
- **Preliminary signal:** model-selected runners shorten slightly more than odds-matched non-selected runners (+0.02 to +0.06 log), consistent across three periods.
- **Not supported:** that model selections beat the closing line in absolute terms. They do not: most selections drift, because the model selects outsiders.
