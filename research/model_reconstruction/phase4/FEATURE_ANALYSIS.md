# Phase 4 - feature analysis

All features are built in p4_features.py from **strictly earlier** races of the horse, trainer or jockey. Today's official rating and weight are known before the race.

| Group | Features | Available since | Knowable pre-race | Coverage | Development gain added alone | Lost when removed from full set | Stable? |
|---|---|---|---|---|---|---|---|
| G0 production | earlier BSP, positions, OR, weight, runs, days off, last-time win, non-finishes | Jan 2026 | yes | 100% (flags for missing) | baseline | -0.0019 (removing all of G0) | yes |
| G1 speed | RaceData dynamic speed rating / API speed, earlier same-code runs: last, best and mean of 3 (relative to field mean, max and rank) | Jan 2026 | yes | 69% | **-0.0027** | -0.0020 | no gain |
| G2 OR & class | OR vs field max, OR rank, class change vs the last 3 | Jan 2026 | yes | OR about 85%, class about 63% | **+0.0072** | +0.0056 | yes |
| G3 suitability | best position score within ±1f, going-group mean, course runs and wins | Jan 2026 | yes | 57-71% | +0.0006 | +0.0006 | marginal |
| G4 connections | trainer and jockey win rate over the previous 30 and 365 days (shrunk), relative to field | Jan 2026 (RaceData names; API dates matched through RaceData daily files) | yes | 99.9% | **+0.0232** | **+0.0230** | yes: the largest single group |
| G5 consistency | earlier top-3 rate, position score, career runs | Jan 2026 | yes | 87% | -0.0014 | -0.0016 | no |
| G6 pace | run-style score, lead share, likely leaders in race | Jan 2026 | yes | 78% | -0.0005 | -0.0004 | no |
| G7 field | field size, field mean OR, top-two OR gap | Jan 2026 | yes | 100% | 0.0000 | 0.0000 | no (constant within a race, so it only works through interactions) |
| All G0-G7 | 61 features | | | | +0.0258 | | |

**Relative vs absolute:**
- All-relative 1.9157 vs absolute 1.9111. Relative transformation did not help; the race softmax already makes everything relative.
- Field-relative features (vs mean, vs max, rank) are kept because they help the boosted models with field context.

**Computational cost:** building the feature table takes about 90 s for 106k runners. Trainer/jockey rolling windows are the most expensive part (about 40 s).

**Not available, or not used, and why:**

| Data | Reason |
|---|---|
| Beaten distances | Not in RaceData history |
| RPR / Topspeed for earlier runs | API performance ratings only exist from 14 Oct 2026 |
| Pedigree | Not in the history table |
| Market rank | Used only in market-anchored candidates |
| Provider predictions in RaceData exports ("Race Predictor Win %", "PR Score", "VDW") | Present in result files of unverified pre-race provenance. Excluded to avoid leakage; a candidate for a separately sealed test using the true pre-race exports archived since 11 Nov |

Chart: out/feature_ablation.png. Data: out/ablation.csv.
