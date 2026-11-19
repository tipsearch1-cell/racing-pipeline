# MODEL RECONSTRUCTION PHASE 4 - sealed spec (19 Nov 2026)

Research only. No production model, bot, strategy or schedule changes. Code is in research/model_reconstruction/phase4/.

**Evidence grading:**
- **No untouched historical period remains.** Mar - 12 Oct 2026 (S3) and 26 Oct - 18 Nov 2026 (H3) were examined in Phases 2-3. All historical results here are **development / diagnostic evidence**.
- **Genuinely untouched evidence is prospective only.** Frozen predictions start on 20 Nov 2026 (shadow log, below).

**Seen before sealing:** Phase 1-3 results (production-model replay vs market on S3/H3), data columns and package availability. No candidate model has been scored.

**Tooling:** lightgbm and xgboost cannot be installed here (the package registry has no wheel for Python 3.13). Pairwise and listwise boosted models are therefore implemented directly with scikit-learn regression trees (Newton boosting on the race-level softmax / pairwise logistic loss). This is functionally equivalent for this purpose, and is documented in the reports.

## Data
**Runner features:** built from the history table (pipeline/history.py load, read-only) plus trainer and jockey names from RaceData exports, joined on date+course+horse. Every feature is computed from a horse's, trainer's or jockey's **earlier** races only (strictly earlier dates). Groups:
- **G0 production:** the 13 production features (mkt_prev, pos, OR, weight, runs, days, first-time, won last, non-finishes).
- **G1 speed:** Dynamic speed rating / API speed of earlier same-code runs: best of last 3, mean of last 3, last.
- **G2 rating and class:** OR minus field max, OR rank, class change vs the mean of the last 3.
- **G3 suitability:** best position score within ±1f; mean on the same going group; runs and wins at the course.
- **G4 connections:** trainer and jockey win rate over the previous 30 and 365 days (shrunk, minimum counts).
- **G5 consistency:** top-3 rate, career runs.
- **G6 pace:** run-style score, lead share, likely leaders in the race.
- **G7 field:** field size, field mean OR, gap between the top two ORs.
- **Relative forms:** each continuous feature minus the race mean, minus the race max, and rank within the race.

**Market:** production composite at checkpoints E/M/H/T10/L (S3), and 09:00 from sealed cards (H3).
- **Diagnostic only:** BSP, which is never an input.

## Candidates
- **Baseline:** production replay (Phase 2/3 monthly refit, unchanged code).
- **A Improved current:** the same conditional-logit (race softmax) objective with G0-G7 relative features; L2 chosen from {0.3, 1, 3} on the last training month.
- **B Pairwise:** boosted trees on within-race pairwise feature differences (logistic loss on "i beat j" pairs, all pairs involving the winner plus a sample of others). Scores are turned into probabilities by a race-softmax temperature fitted on training.
- **C Listwise:** boosted trees on the race-softmax loss (Newton steps), depth 3, learning rate 0.05, number of trees chosen by early stopping on the last training month.
- **D Market residual:** score = log m_t + g(x). Two forms:
  - D1 linear: offset conditional logit, L2 = 3;
  - D2 boosted listwise: init score = log m_t, depth 2, learning rate 0.03, early stopping.
  - Recovers the market exactly when g = 0.
  - Trained only on races with that checkpoint's market data, before the test month.
- **E Hybrid:** race-softmax of w1·log m_t + w2·s_C (+ w3·log baseline), weights fitted on training.

## Walk-forward
**Monthly expanding.**
- Independent models (A, B, C): train on all history races before the 1st of the test month, from 1 Jan 2026.
- Market-dependent models (D, E): train on S3-joined races from Mar 2026 up to the test month.
- **Test months:** May - Oct 2026 (S3), plus H3 (fitted on races before 1 Oct and 1 Nov respectively).

**Model selection (frozen before the shadow test):**
- Choose by mean paired log-loss gain vs the 09:00 market over May - Aug.
- Sep - Oct and H3 are reported as re-used diagnostics.
- Ties within 0.002 go to the simpler model.

## Metrics
Race-level multiclass log-loss, multiclass Brier, top-pick win %, winner's mean rank, concordance, calibration (slope, intercept, ECE, by odds band), favourite and outsider bias, and results by field size, code and handicap.

Comparisons are paired day-block bootstrap (2,000 draws) against the 09:00 market and against the baseline.

## Ranking diagnostics (hypotheses A-F)
- **A relative ranking:** concordance within 09:00 odds bands; absolute vs relative feature versions of A.
- **B objective:** the same features under runner-level logistic (then normalised), race-softmax, and pairwise.
- **C features:** ablation, adding G1-G7 one at a time to G0, and leaving each out from the full set.
- **D field size:** entropy vs the market by field size; a separate temperature per field-size band.
- **E population:** training on the last 3 months only vs expanding; Flat/Jumps pooled vs separate.
- **F compression:** production L2 (1.0) vs L2 = 0; post-hoc temperature; normalisation check (sums to 1, non-runner handling).

## Market information
D and E are fitted at E, M, H, T10 and L (S3). Reported: the gain over the market at each checkpoint.

## Limited betting (pre-specified, no threshold search)
- Bet at 09:00 if EV ≥ 4% at (i) the exchange quote after 2% commission, or (ii) the bookmaker best price.
- Compared: baseline, market-only control, best independent candidate, best residual, hybrid.
- Reported on development periods only, labelled as conditional simulations.

## Prospective shadow test (the only untouched evidence)
**From 20 Nov 2026:** after each 08:35 build has been published, research/model_reconstruction/phase4/shadow.py writes the frozen chosen model's probabilities for every race:
- hashed into the forward-archive layout;
- committed to git before the first off.

The bot is never affected.

**Pass:** after ≥ 1,000 races, the paired log-loss gain vs the 09:00 market has a 95% day-block lower bound > 0.

## Verdicts
| Verdict | Criteria |
|---|---|
| PROMOTE TO FORWARD SHADOW TEST | Positive mean dev gain vs the 09:00 market with lower bound > 0 in May-Aug, **and** the same sign in Sep-Oct and H3 |
| CONTINUE RESEARCH | Beats the baseline but not the market, or beats the market without a consistent sign |
| REJECT | Neither |

## Amendment 1 (19 Nov 2026, after the development scoring, before ANY shadow prediction exists)
**What happened at selection:**
- The sealed selection rule (best development gain; ties within 0.002 go to the simpler model) picked **D2** (boosted market residual), because it was within 0.0012 of **E** (hybrid).
- D2's development lower bound is -0.0001, so it does not meet the sealed PROMOTE criterion.
- E meets the PROMOTE criterion: development gain +0.0034 [+0.0008, +0.0060], with the same sign in Sep-Oct and H3.

**Decision, so that neither result is suppressed and no swap is made after the fact:**
- The prospective shadow test logs **both D2 (rule-selected) and E (criterion-promoted)**, frozen as fitted on 19 Nov.
- Each is tested against the 09:00 market with a Bonferroni-adjusted interval (97.5%, two models). The pass rule is otherwise unchanged.
- No shadow outcome exists yet.
