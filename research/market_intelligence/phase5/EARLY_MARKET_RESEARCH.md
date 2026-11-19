# Phase 5 - early (21:00 → 09:00) market opportunity (exploratory)

**Bottom line:**
- The independent information predicts which way prices move overnight, and market-anchored chances beat the 21:00 market on log-loss. That information is real.
- But the 21:00 exchange quotes the provider shows are about **half of BSP** (median BSP / quote = 2.0). Model selections at those quotes **do not beat BSP** (absolute CLV −0.03).
- Positive "relative CLV" against similar-priced runners exists, but it is an artefact of every evening quote being short. It is **not** evidence of profit.
- An overnight edge is plausible but unproven. Testing it needs real evening liquidity data. A forward evening series (exploratory model X1) starts tonight.

All results are from historical data examined in Phases 2-4: development May-Aug and re-used Sep-Oct 2026. They are exploratory and have no bearing on the confirmatory test.
- Script: explore.py.
- Outputs: out/explore.json, out/early_market_movement.csv, out/clv_execution.csv.

## 1. Are previous-evening prices realistically available?
| Measure | Value |
|---|---|
| Races with a complete 21:00 composite | 99.4% of 8,187 |
| Races with a Betfair quote for every runner at 21:00 | 98.6% |
| Median BSP / provider "Betfair Exchange" quote at 21:00 | **2.00** |
| Same at 09:00 | 1.29 |
| Same at off−10 | 1.08 |

**What this means:**
- The evening "exchange" figure is far shorter than where the market settles. It behaves like a thin early book or a lay-side figure, not a price you could back at in size.
- The quotes exist, but their tradability is unknown. Without Betfair depth data (blocked) every evening return is a conditional simulation.

## 2. Does independent information predict overnight movement?
Regression of the within-race change in log market chance (21:00 → 09:00) on the model's disagreement with the 21:00 market. Day-clustered standard errors.

| Period | Signal | Races | Correlation | Slope (SE) |
|---|---|---|---|---|
| Development | Improved independent model A | 4,753 | 0.20 | 0.170 (0.012) |
| Re-used Sep-Oct | A | 1,623 | 0.10 | 0.078 (0.017) |
| Development | Production model | 4,753 | 0.12 | 0.100 (0.012) |
| Re-used Sep-Oct | Production model | 1,623 | −0.01 | −0.007 (0.015) |

**Findings:**
- Yes, for model A. Horses that A rates above the evening market tend to shorten by 09:00.
- The effect halves from development to the re-used period.
- The production model's signal disappears in the re-used period.

## 3. Do evening selections beat the line?
Rule: market-anchored model at 21:00 (D1 at E, walk-forward). Select at EV ≥ 4% at the Betfair quote, 2% commission.

| Period | Selections | Median quote | Absolute CLV vs BSP [95%] | Share beating BSP | CLV vs odds-matched runners |
|---|---|---|---|---|---|
| Development | 2,209 | 5.3 | −0.027 [−0.049, −0.006] | 49.7% | +0.91 |
| Re-used Sep-Oct | 841 | 4.8 | −0.029 [−0.057, −0.003] | 48.6% | +0.87 |

**Findings:**
- The selections do better than other runners at similar evening odds (relative CLV +0.9). That is because evening quotes for longer-priced runners are even further below BSP.
- In absolute terms they **lose** to BSP. Under the brief's rule this is not profitable CLV.
- The independent model A on its own at 21:00 is much worse: absolute CLV −0.49 to −0.54, with 26-29% beating BSP.

## 4. Where is the evening gain?
Log-loss gain of the market-anchored evening model over the 21:00 market, by the winner's 21:00 odds band:

| Winner's odds band | Development | Re-used |
|---|---|---|
| < 3 | +0.11 | +0.11 |
| 3-6 | +0.08 | +0.09 |
| 6-11 | +0.02 | 0.00 |
| 11-21 | −0.08 | −0.08 |
| 21+ | −0.22 | −0.30 |

**Findings:**
- The evening model moves probability towards the front of the market. That helps in races won by fancied horses and hurts in races won by outsiders.
- By code the gain is similar: Flat +0.025 / +0.012, Jumps +0.023 / +0.010.
- Part of this is the evening market being under-confident. Phase 4 found only +0.0105 beyond simple sharpening in development, and about 0 in the re-used period.

## 5. Forward exploratory candidate X1 (frozen 19 Nov)
- X1 = softmax(1.078·log m_E + 0.263·s_C + 0.090·log f), fitted on Mar - 12 Oct replay data.
- The weight on the independent score is 6× its 09:00 counterpart (0.044 in frozen E), consistent with the evening market leaving more room.
- It is computed each morning from the 21:00 snapshot (`fwd.py x1 DAY`).
- **Decision-time caveat:** the components come from the 08:35 card, not the 21:00 card, and this is labelled.
- It is a separate exploratory candidate, never the frozen 09:00 E.

## 6. What would make this testable
1. Real evening liquidity: Betfair Exchange API (depth, matched volume), or the VPS price histories.
2. The forward X1 series against the 09:00 market and BSP, with absolute CLV per spec section 9.
3. Execution evidence: whether an evening back order at the displayed quote is matched, and at what size.
