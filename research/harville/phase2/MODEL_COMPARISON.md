# Phase 2 - model comparison (accuracy and calibration)

**SYNTHETIC replay (S):**
- Our rebuilt win model was refitted month by month on earlier races only.
- Second-stage parameters were fitted on earlier replayed months (expanding window).
- Development = May-Aug 2026. Holdout = 1 Sep - 12 Oct 2026, scored once.

**GENUINE (G):**
- Archived pre-race chances, 10-18 Nov 2026, 217 races.
- Parameters fitted on all of S. Nothing fitted on G.

All gains are paired on identical races (A minus model; positive = better than the market baseline), with 95% day-block bootstrap intervals (2,000 draws).

The models compared:

| Code | Win-probability input | Places step |
|---|---|---|
| H | 09:00 market | original Harville |
| A | 09:00 market | discounted Harville (field-size exponents) |
| B | our model alone | discounted Harville |
| C | log-linear blend, p ∝ market^w1 × model^w2 | discounted Harville |
| D | C | 2nd/3rd conditional logit with pre-race runner features |

## Headline
| Method | Period | Top-2 Brier | Top-3 Brier | P(3rd) calibration slope | Trifecta log-loss | Win log-loss |
|---|---|---|---|---|---|---|
| Market + discounted Harville (A) | S holdout | 0.13393 | 0.16702 | 1.02 | 5.4143 | 1.8355 |
| Our model + discounted Harville (B) | S holdout | 0.14500 | 0.18199 | 1.00 | 5.8071 | 2.0259 |
| Blend + discounted Harville (C) | S holdout | 0.13394 | 0.16709 | 1.03 | 5.4100 | 1.8321 |
| Enhanced ranking (D) | S holdout | 0.13383 | 0.16683 | 1.00 | 5.4020 | 1.8321 |
| Market + discounted Harville (A) | G | 0.13042 | 0.16310 | 1.07 | 5.3751 | 1.8421 |
| Our model + discounted Harville (B) | G | 0.14285 | 0.17752 | 1.05 | 5.7882 | 2.0406 |
| Blend + discounted Harville (C) | G | 0.13045 | 0.16305 | 1.08 | 5.3742 | 1.8448 |
| Enhanced ranking (D) | G | 0.12981 | 0.16123 | 1.10 | 5.3336 | 1.8448 |

Paired gains vs A:

| Model | Period | Top-3 Brier gain (per race) | Trifecta log-loss gain | Predictive-value pass? |
|---|---|---|---|---|
| B | S holdout | -0.145 [-0.160, -0.130] | -0.393 [-0.427, -0.359] | **No** - far worse than the market |
| C | S holdout | -0.0006 [-0.0020, +0.0008] | +0.0042 [-0.0004, +0.0088] | **No** |
| D | S holdout | +0.0019 [-0.0017, +0.0054] | +0.0123 [+0.0029, +0.0218] | **No** (Brier interval crosses 0; spec needs both) |
| B | G | -0.142 [-0.201, -0.079] | -0.413 [-0.546, -0.270] | No |
| C | G | +0.0005 [-0.0020, +0.0033] | +0.0009 [-0.0192, +0.0180] | No |
| D | G | +0.0185 [+0.0095, +0.0298] | +0.0415 [+0.0087, +0.0847] | Same sign (G too small to require significance) |

By month (point gains vs A; development months May-Aug, holdout Sep-Oct):

| Gain | Model | May | Jun | Jul | Aug | Sep | Oct |
|---|---|---|---|---|---|---|---|
| Top-3 Brier | C | -0.0009 | -0.0002 | +0.0013 | +0.0003 | -0.0002 | -0.0015 |
| Top-3 Brier | D | +0.0010 | +0.0038 | +0.0047 | +0.0032 | +0.0020 | +0.0017 |
| Trifecta LL | C | +0.0011 | +0.0061 | +0.0075 | +0.0048 | +0.0044 | +0.0038 |
| Trifecta LL | D | -0.0009 | +0.0098 | +0.0140 | +0.0108 | +0.0103 | +0.0168 |

D is positive in every month but May on both measures. Its holdout Brier gain is too small to clear the interval.

## Our model's independent information (blend weights)
Each window's weights are fitted by win-only conditional logit on earlier months:

| Test month | Train races | w market | w model (se) | z for model |
|---|---|---|---|---|
| May | 1,784 | 1.094 | 0.108 (0.055) | 2.0 |
| Jun | 3,105 | 1.104 | 0.051 (0.042) | 1.2 |
| Jul | 4,261 | 1.085 | 0.098 (0.036) | 2.7 |
| Aug | 5,452 | 1.087 | 0.099 (0.032) | 3.1 |
| Sep | 6,516 | 1.082 | 0.106 (0.029) | 3.6 |
| Oct | 7,626 | 1.085 | 0.096 (0.027) | 3.5 |
| G (all S) | 8,132 | 1.088 | 0.091 (0.026) | 3.5 |

**Interpretation:**
- Our model carries a small amount of win information the 09:00 market lacks. The weight is stable at about 0.1 and significant once there is enough training data.
- The market weight is above 1: the 09:00 market is slightly too flat and the blend sharpens it.
- The independent-information pass fails on the spec's strict rule, because the June window has z = 1.2.
- A linear mixture λ·model + (1-λ)·market chose λ = 0 in every window. Only the log-linear blend finds any value.

In win log-loss the blend gains:
- +0.0039 [+0.0013, +0.0065] in development;
- +0.0034 [-0.0015, +0.0082] in the holdout;
- -0.0027 [-0.022, +0.017] in G.

That is about 0.2% of the log-loss: real but tiny.

## Where D's gain comes from (Phase 6)
Coefficients are fitted on all S months (se in brackets):

| Feature | Stage 2 (2nd place) | Stage 3 (3rd place) |
|---|---|---|
| prior position score (finishing consistency) | +0.26 (0.12) | +0.56 (0.12) |
| prior top-3 rate | -0.05 (0.06) | -0.32 (0.07) |
| log run count | +0.08 (0.04) | +0.21 (0.04) |
| favourite dummy | -0.21 (0.05) | -0.19 (0.06) |
| lead share (front-runner) | -0.18 (0.07) | -0.07 (0.08) |
| run-style score | +0.05 (0.02) | +0.01 (0.02) |
| distance suitability | -0.12 (0.08) | +0.08 (0.08) |
| going suitability | -0.03 | -0.06 |
| class change | +0.03 | -0.01 |

What the coefficients say:
- **Consistent, experienced horses place more often than their win chance implies.** This supports the "consistent runner" hypothesis.
- Front-runners are slightly less likely to finish 2nd ("win or fade"), but only marginally (z ≈ 2.4 at stage 2, not significant at stage 3).
- Distance, going and class add nothing measurable.

Paired D vs C (the features' own contribution):

| Measure | Development | Holdout | G |
|---|---|---|---|
| Top-3 Brier | +0.0030 [+0.0014, +0.0045] | +0.0025 [-0.0004, +0.0052] | +0.0180 [+0.0087, +0.0304] |
| Trifecta LL | +0.0033 [-0.0011, +0.0075] | +0.0081 [+0.0005, +0.0155] | +0.0406 [+0.0053, +0.0807] |

## Calibration
- Original Harville's P(3rd) slope is 0.83 (holdout) and 0.86 (G). That is the known bias.
- All discounted models sit at about 1.00-1.10 for P(2nd), P(3rd) and P(place).
- Our model alone (B) is reasonably calibrated in slope but much less sharp: its Brier and log-loss are far worse.

## Reviewer as the input (G only, 217 races)
The sealed reviewer chance is no better than the 09:00 market:
- win log-loss +0.004 [-0.014, +0.021];
- trifecta log-loss -0.011 [-0.047, +0.023].

Full tables: out/accuracy_tables.md and out/accuracy.csv. Field-size breakdown: SEGMENT_ANALYSIS.md.
