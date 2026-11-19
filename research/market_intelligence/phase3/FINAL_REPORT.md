# Market intelligence Phase 3 - final report (19 Nov 2026)

**Bottom line:**
- Our model has a small amount of genuine early information. The market absorbs all of it by the off.
- That information is far too small to make up for the model's much weaker ranking (log-loss 0.17-0.24 worse than the 09:00 market).
- No betting strategy passed. The one strategy positive in every period (market + 10% model blend, backed at the 09:00 exchange quote) is not significant, depends on a few long-priced winners, and disappears under a realistic adverse-fill assumption.

The recommendation is to **change the modelling approach** rather than search for more thresholds.

| | |
|---|---|
| Spec | prereg/MARKET_INTEL_PHASE3_SPEC_2026-11-19.md, sealed before outcomes (sha256 e4238992…feeca), no amendments. Two control analyses were added and labelled. |
| Code | research/market_intelligence/phase3/: p3_data.py, p3.py, charts3.py, archive/ (collector + tests). Outputs in out/. |
| Data categories | **A** verified forward (221 races 10-18 Nov plus 32 live bot bets with BSP) · **B** chronological replay (S3: 8,196 races Mar - 12 Oct, with 09:00, off-60m, off-10m and off-1s prices; H3: 674 untouched races 26 Oct - 18 Nov, 09:00 and BSP only) · **C** diagnostic (not used for conclusions) |
| Holdout honesty | Sep - 12 Oct was examined in Phase 2, so it is labelled "re-used". H3 is the only untouched replay period. A is too small to decide anything on its own. Repeated research on the same 2026 replay limits how strong any conclusion can be. |
| Production | Nothing changed. Phase 1 and 2 files untouched. One erratum file added to phase2/. |

## Answers
| # | Question | Answer | Evidence | Status |
|---|---|---|---|---|
| 1 | Is our model's win calibration competitive with the market? | **Calibration yes, accuracy no.** Slope about 1.0, ECE ≤ 0.006, but log-loss 2.01 vs the market's 1.77 (H3). Concordance 0.67 vs 0.76; top pick wins 26% vs 36%. Favourites under 2.5 get 31% from us vs 56% actual. | WIN_CALIBRATION.md | Proven |
| 2 | Does our model have independent predictive information? | **A little, early only.** Blend weight about 0.10 at 09:00 (z 2-3.6), 0.03 at off-60m, about 0 at the off. Within the same odds band the market moves towards our view (+0.05 to +0.14 correlation in all three periods). | MARKET_MOVEMENT.md, DISAGREEMENT_ANALYSIS.md | Proven but small |
| 3 | Does combining with the market improve win prediction? | **Marginally:** +0.003 to +0.005 log-loss (0.2%). Significant in development only; negative in the 221 verified races. Operationally negligible: about ±0.3 points on a 10% chance. | WIN_CALIBRATION.md | Preliminary |
| 4 | Do selections beat the closing line? | **No in absolute terms.** Model selections mostly drift, because they are outsiders. **Yes slightly against odds-matched controls:** +0.02 to +0.06 log in all three periods. Live favourite checks: Matchbook 09:00 beat BSP by +6% on average (30 bets), but returned -43%. | CLV_ANALYSIS.md | Preliminary signal |
| 5 | Are large disagreements systematically wrong? | **Yes.** Model 25% vs actual 10-12% when we are more than 10 points above the market; 15% vs 35% when more than 10 below. | DISAGREEMENT_ANALYSIS.md | Proven |
| 6 | Can market movement identify bets to avoid? | Movement is highly informative (coefficient 1.06 beyond the 09:00 price) and makes our model redundant. Drift-avoidance rule E: -15% / +14% (exchange), no consistent benefit. | MARKET_MOVEMENT.md, STRATEGY_COMPARISON.md | Unsupported as a betting filter |
| 7 | Does waiting until nearer the off help? | **No consistent ROI benefit.** Later markets are more accurate, but they replace our model's information. Morning exchange quotes are short (BSP 26% longer), so there is no early-price advantage on the exchange. | TIMING_ANALYSIS.md | Unsupported |
| 8 | Are positive-CLV selections profitable? | **Not demonstrably.** C blend has +14% to +22% raw CLV vs BSP and +4% to +15% ROI, but every interval includes 0, null p is 0.43-0.64, and it is -13% to -18% without the top 1%. Live favourite checks had positive CLV and lost. | CLV_ANALYSIS.md, STRATEGY_COMPARISON.md | Unsupported |
| 9 | Does any edge survive commission and execution? | **No.** 0 of 36 cells pass on H3. At 5% commission or with adverse fills (-24% to -29% for C), nothing is positive. Bookmaker-price "edges" do not need our model (market-only controls do as well) and face limits and Rule 4. | STRATEGY_COMPARISON.md, EXECUTION_REVIEW.md | Proven negative |
| 10 | What should change in our model? | **Ranking, not calibration.** It is too flat: it ignores how strongly the market separates favourites from outsiders. Use it as a **small adjustment to the market** (market-anchored residual model), not as a standalone probability. Re-target training on market-relative errors with features the market may under-use (consistency, stable form, recent class moves). Drop standalone value flags based on our model's price. | WIN_CALIBRATION.md, Phase 2 D-model | Recommendation |
| 11 | Which avenues should be abandoned? | Standalone-model value betting (A/B); place betting at place SP (Phase 2); disagreement-band and drift filters; bookmaker-best-price backtests without account and limit data; threshold tuning on the replay period. | all | Recommendation |
| 12 | Highest-value next experiment? | **A forward shadow test of "market + 10% model at 09:00", with executable price and depth capture.** Enable the forward archive on the VPS (09:00 and 60/30/15/5/1-minute snapshots), add Betfair order-book data if an API key can be obtained, and paper-log blend-C selections with their actual best-back price and size. Decide after a pre-set sample (e.g. 1,000 selections). In parallel: push the VPS raw price histories to rebuild exact 30/15/5-minute replays. | FORWARD_ARCHIVE.md | Recommendation |

## Proven vs preliminary vs unsupported
**Proven** (holds in development, re-used and untouched H3, with intervals):
- The model is calibrated but low-resolution, and much worse than the market.
- Large disagreements are the model's errors.
- Later market prices are more informative, and movement makes the model redundant.
- No strategy passes the sealed betting rule.
- The Phase 2 "-0.27 drift" was an odds-level artefact. It is corrected: within the same odds band the market drifts **towards** us.

**Preliminary signals** (consistent sign, not significant, or not testable on untouched data):
- The model's early information (blend weight about 0.1; within-band movement towards us).
- Selections beat odds-matched controls on CLV.
- Blend C at the exchange quote is positive in all periods.
- D market confirmation at bookmaker prices: development +29.8%, re-used +24.7%. Its market-only control does comparably (+17.7% / +45.7%), and it can't be tested on H3.

**Unsupported:**
- Any profitable, executable strategy.
- Timing advantages.
- Drift-avoidance filters.
- Disagreement conditions where our model beats the market.

## Is the blend's improvement operationally meaningful?
- The log-loss gain is about 0.004 per race, 5-9% of the gap between the 09:00 market and BSP.
- On a typical 10% runner it moves the probability by about 0.3 points. Against a 2% commission and a 3-6% bid-ask cost in morning markets, that is not enough to create value on its own.
- It is useful only as a small correction inside a better model.

## Deliverables
DATA_AUDIT.md · WIN_CALIBRATION.md · CLV_ANALYSIS.md · MARKET_MOVEMENT.md · DISAGREEMENT_ANALYSIS.md · STRATEGY_COMPARISON.md · TIMING_ANALYSIS.md · EXECUTION_REVIEW.md · FORWARD_ARCHIVE.md · this report.

Charts: out/win_calibration_by_odds.png, out/disagreement_vs_movement.png, out/model_weight_by_time.png.

## Reproduce
```
bash tools/restore_raw.sh
python3 research/harville/data.py && python3 research/harville/phase2/replay.py      # Phase 1/2 inputs
python3 research/market_intelligence/phase3/p3_data.py     # S3 / H3 / A3 tables
python3 research/market_intelligence/phase3/p3.py          # all analyses -> out/
python3 research/market_intelligence/phase3/charts3.py
python3 -m pytest -q research/market_intelligence/phase3   # archive + phase 3 tests
```
Random seed 20261119.
