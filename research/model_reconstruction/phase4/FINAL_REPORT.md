# Model reconstruction Phase 4 - final report (19 Nov 2026)

**Bottom line:**
- The ranking weakness is caused by **missing information**. The objective, normalisation, field size, training population and compression are not the cause.
- Better features (mainly trainer and jockey current form) and better learners improve the existing model by 0.02-0.07 log-loss. They still leave every **independent** model 0.14-0.19 behind the 09:00 market.
- Only **market-anchored** models reach or beat the market. The best, E (market + 10% existing model + listwise score), gains about +0.003 log-loss per race (0.2%).
- That gain is consistent in sign but tiny. It rests on development and re-used data only.
- **No historical period is untouched any more.** The decisive test is the prospective shadow test, which starts tomorrow.

| | |
|---|---|
| Spec | prereg/MODEL_RECON_PHASE4_SPEC_2026-11-19.md. Sealed before scoring (sha256 826756d1…7e) plus Amendment 1, written before any shadow data |
| Code | research/model_reconstruction/phase4/: p4_features.py, p4_models.py, p4_run.py, p4_eval.py, p4_diag.py, shadow.py, test_p4.py |
| Outputs | out/: metrics.csv, paired_gains.csv, selection.json, ablation.csv, diagnostics.json, checkpoint_experiment.csv, betting.csv, calibration_by_odds.csv, config.json, charts |
| Production | Unchanged. The bot is unaffected. The 20 Nov build only gained research steps that run after publishing. |

## Final comparison (paired log-loss gain per race vs the 09:00 market, 95% day-block)
| Model | Win log-loss (development) | Brier (development) | Top pick wins (development) | Concordance (development) | vs market, development | vs market, re-used Sep-Oct | vs market, H3 (re-used) | Status |
|---|---|---|---|---|---|---|---|---|
| Existing model | 1.969 | 0.828 | 26.2% | 0.670 | -0.167 [-0.183, -0.150] | -0.188 | -0.239 | REJECT as a standalone model |
| 09:00 market | 1.802 | 0.780 | 33.3% | 0.737 | (baseline) | | | benchmark |
| A Improved current | 1.944 | 0.823 | 27.6% | 0.682 | -0.142 [-0.156, -0.127] | -0.151 | -0.190 | CONTINUE RESEARCH (replaces existing as the independent model) |
| B Pairwise | 1.944 | 0.822 | 27.3% | 0.681 | -0.142 [-0.158, -0.125] | -0.142 | -0.168 | REJECT (no better than the simpler A) |
| C Listwise | 1.950 | 0.823 | 27.2% | 0.676 | -0.148 [-0.164, -0.134] | -0.145 | -0.178 | REJECT as a standalone model (kept only as an input to E) |
| D1 Market residual (linear) | 1.801 | 0.781 | 32.8% | 0.737 | +0.0007 [-0.0043, +0.0056] | -0.0031 | +0.0013 | REJECT (unstable) |
| D2 Market residual (boosted) | 1.800 | 0.780 | 33.0% | 0.737 | +0.0022 [-0.0001, +0.0043] | +0.0003 | +0.0018 | **PROMOTE TO FORWARD SHADOW TEST** (rule-selected; Amendment 1) |
| E Hybrid | 1.798 | 0.780 | 33.2% | 0.736 | **+0.0034 [+0.0008, +0.0060]** | +0.0033 [-0.0016, +0.0082] | +0.0043 [-0.0033, +0.0108] | **PROMOTE TO FORWARD SHADOW TEST** |
| BSP (diagnostic) | 1.747 | 0.768 | 34.7% | 0.753 | +0.056 | +0.070 | +0.050 | not available at 09:00 |

Periods and sizes:
- **Development:** May-Aug 2026, 4,761 races.
- **Re-used:** Sep - 12 Oct, 1,623 races.
- **H3:** 26 Oct - 18 Nov, 674 races.
- **Training:** expanding, from Jan 2026 (independent models) or Mar 2026 (market-anchored).
- **Verified forward results for the candidates:** none yet.

E meets the sealed promote criterion: development lower bound above 0, and the same sign in both re-used periods. D2 was picked by the selection tie-break rule, so both are being shadow-tested.

## Answers
1. **What causes the ranking weakness?** The model does not know what the market knows. It cannot tell which outsiders are hopeless: concordance in the outsider quintile is 0.52 vs the market's 0.71. So it spreads probability onto them and away from favourites.
2. **Objective, features, transformation or data?** **Features and information.**
   - The objective is already race-level softmax; switching to pairwise or runner-level changes almost nothing.
   - Calibration and normalisation are correct: the oracle temperature is 1.006.
   - A data issue was found: card weights are before the jockey's claim, but training weights are after it.
3. **Does pairwise ranking improve winner identification?** Slightly over the existing model (top pick 27-29% vs 26%), but no better than the linear model A.
4. **Does listwise ranking improve race-level probabilities?** Over the existing model, yes (+0.02 to +0.06). Over the market, no.
5. **Does market-anchored learning beat independent modelling?** Yes, by about 0.15 log-loss. Market anchoring is the only route that reaches the market, and its corrections are small.
6. **Largest incremental features?** Trainer and jockey form (+0.023), then OR and class (+0.007). Speed figures, consistency, pace and field strength add nothing.
7. **Are corrections stable?** D2 and E are positive in 6 of 8 months. D1's coefficients are unstable. D2's corrections shrink over time. E's independent component flips sign.
8. **Does any candidate beat the 09:00 market?** E, by +0.003 (development, significant). It is the same sign but not significant in the re-used periods. That counts as **development evidence only**.
9. **Value close to the off?** **No.** Features beat the market only at the previous evening's checkpoint (+0.0105 development). From 09:00 they add nothing. From an hour before the off they hurt.
10. **Does accuracy translate into betting value?** Not demonstrably. E at the 09:00 exchange quote: +7% / +8% / +15% across the three periods, every interval including zero, dependent on long morning quotes whose depth is unknown, and a pattern that turned negative under adverse fills in Phase 3.
11. **Keep, redesign or replace the architecture?** **Redesign.**
    - Keep the race-softmax objective.
    - Replace the 13-feature model with model A (adds trainer/jockey form and OR/class; +0.025 to +0.049 better).
    - Use it only as an input to a **market-anchored** model, never as a standalone price.
    - Fix the claim mismatch in the weight feature.
12. **Single best candidate for shadow testing?** **E (hybrid).** D2 runs alongside as the rule-selected comparator. Both are frozen as of today. The test needs at least 1,000 races (about 4-5 weeks). Pass = paired lower bound > 0, Bonferroni over 2 models.

## Proven vs preliminary vs unsupported
- **Proven** (all periods, with intervals):
  - the information gap is the cause;
  - the objective, field-size temperature, population and compression are not causes;
  - independent models stay about 0.14 behind the market;
  - trainer and jockey form is the most valuable missing feature group;
  - features lose their value by 09:00.
- **Preliminary:** E's +0.003 over the 09:00 market. D2's +0.002.
- **Unsupported:** any betting edge. Any value close to the off.

## Forward archive
- 12 tests pass.
- Tamper-evident chained manifest, failure logging and recovery, postponed-race and non-runner handling were added and tested.
- Predictions for 10-19 Nov are archived, all verified.
- **Market capture is still blocked here.** It can't reach the Racing API from this shell or reach the VPS. Exact McCoy deployment commands are in ARCHIVE_STATUS.md.
- **Exchange depth and volume need a Betfair API key.** Not claimed.

## Reproduce
```
bash tools/restore_raw.sh
python3 research/harville/data.py && python3 research/harville/phase2/replay.py && python3 research/market_intelligence/phase3/p3_data.py
python3 research/model_reconstruction/phase4/p4_features.py      # ~90 s
python3 research/model_reconstruction/phase4/p4_run.py           # ~8 min
python3 research/model_reconstruction/phase4/p4_eval.py
python3 research/model_reconstruction/phase4/p4_diag.py
python3 -m pytest -q research/model_reconstruction/phase4 research/market_intelligence/phase3
python3 research/model_reconstruction/phase4/shadow.py predict <DAY>   # daily, after publishing
```
Seed 20261119. Configuration: out/config.json.
