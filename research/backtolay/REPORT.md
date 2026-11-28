# Back-to-lay / lay-to-back study (28 Nov 2026), research only

**Verdict: NO-GO.** With the data we hold there is no back-to-lay (BTL) or lay-to-back (LTB) selection that shows an edge at prices with realistic liquidity. The one positive result is in 100/1+ outsiders, and it is not credible.

## Data and method
- **Data:** RBD results archive, 400,597 runners in 44,662 GB races (mostly Flat), 1 Jan 2020 to 8 Oct 2026. Fields used: BSP, in-running traded min/max, pre-off traded min/max and form fields.
- **Leakage audit:**
  - "Avg % SP drop last 5" matches a recomputation from prior runs (r 0.79 prior-only, against 0.67 including the race), so it is a pre-race field.
  - "Pace" is 0 for debutants, so it is history-based.
  - "RBD rating" adds nothing to BSP for predicting winners (log-loss 0.29733 → 0.29735), so there is no hidden result in it.
  - Our own history features (each horse/trainer/jockey/course's past halve, drift and reduction rates) use prior days only.
- **Trades:**
  - BTL: back at BSP, lay when the odds fall 30% or 50% (of BSP−1), then green up.
  - LTB: lay at BSP, back when the odds rise 50% or 100%, then green up.
- **Fill rule:** our in-running order only counts as matched if the price traded **through** it by 2 ticks. A sensitivity run used touch-only fills.
- **Costs:** commission 2% and 5% on net winnings.
- **Model:** gradient boosting, 3 outcomes (traded out / missed and won / missed and lost), giving an expected value per bet.
- **Protocol:** trained on 2020–23. The selection threshold was chosen on 2024 only (minimum 200 bets). Tested once on 2025–26 (109k runners).

## Results (test 2025–26, 2% commission)
| Trade | All runners, BSP ≤ 20 | Model selection, BSP ≤ 20 | Model selection, no price cap |
|---|---|---|---|
| BTL 30% | −41.4% | none found on 2024 | 377 bets, +6.8% (90% CI +1.8 to +12.2), **average BSP 408** |
| BTL 50% | −44.6% | none | 305 bets, −2.0% |
| LTB 50% | −34.3% | none | none |
| LTB 100% | −28.2% | none | 839 bets, −4.3% (CI −30 to +16) |

- With touch-only fills the picture is the same (BTL 50% at −42%), and so is a BSP ≤ 100 cap.
- **The positive BTL 30% result comes entirely from 100/1+ shots.** A back at BSP 400 and a lay print around 280 in-running is a thin market: one small trade can set the archive's in-running low, and nothing guarantees size. This is not treated as an edge.
- **Model lift is small.** For predicting a halve, the area under the curve (AUC; 0.5 = no skill, 1.0 = perfect) rises from 0.615 with BSP alone to 0.627 with all features. Pre-race data barely predicts in-running moves beyond the price itself.
- **The archive's in-running extremes move less than a fair market implies, in both directions and at every price band.** For example, at BSP 5–8 the odds halve 38% of the time against 58% fair, and double 86% against 92% fair. Possible causes are gaps and suspensions in-running, thin or partly recorded prints, or BSP not being the in-play starting price. Whatever the cause, these fields cannot show an edge reliably. The halve rate also falls over time (45% in 2020 → 35% in 2025–26), a regime or recording change.

## What would change the verdict
Timestamped in-running prices with traded volume (Betfair historical stream data, or a live capture). With those, fills could be simulated properly and pre-race information timed (e.g. known front-runners) could be tested. Until then, no further work is recommended.

Files: load.py, features.py, study.py (args: fill-through ticks, BSP cap), diag.py, out_*.json.
