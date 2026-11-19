# HARVILLE PHASE 2 - does our model know something the market does not? Sealed spec (19 Nov 2026)

Research only. No production code, model, bot file or staking changes.
- Code lives in research/harville/phase2/ and reuses Phase 1 (research/harville/harville.py, data.py), which is not modified.
- Written before any comparison of our model's chances with outcomes or with the market.
- Already seen before sealing: Phase 1 results (market-input models only), data counts, and the place-terms reconciliation counts (below).

## Data
1. **G - genuine archive (verified).** Rebuilt-model chances from store/DAY/model.json for 10-18 Nov 2026, plus the sealed reviewer chance.
   - Git commit times are before the first off each day.
   - models/win_model.json was trained on history to 9 Nov 2026 and never retrained.
   - 09:00 market = the production `mkt` in data/card_review_tracker.csv.
2. **G0 - recovered old-model chances (14 Oct - 9 Nov).** From report/history_data.json.
   - Provenance is unverified: first committed 10 Nov, and the old model's training window is unknown.
   - Reported separately. Never used for any decision or pass.
3. **S - synthetic chronological replay of the rebuilt win model.**
   - Same feature code (pipeline/models.py functions, imported unchanged) and the same Flat/Jumps split.
   - For each month M from Mar to Oct 2026, it is refitted on history races before the 1st of M (history starts 1 Jan 2026) and predicts M.
   - Joined to Phase 1 track O (09:00 market, results, place SP) on date+course+horse.
   - A race is used only if every runner has both a model chance and a 09:00 chance.
   - Labelled SYNTHETIC throughout and never pooled with G.

## Place terms (reconciliation, done before sealing)
- Places paid = Betfair standard terms on DECLARED runners. Declared = ran + non-runners listed in the result:
  - 5-7 -> 2;
  - 8-15 -> 3;
  - 16+ -> 4 if handicap, else 3;
  - under 5 -> no bets.
- On the 1,490 track-O races with Betfair's own placed flag (RBD), this matches 99.2% of 5+ runner races. The Phase 1 ran-count rule matched 94.5%.
- LOC/BSP bets are matched after non-runners are removed, so no reduction factors apply.
- Dead heat for the last place: stake split.

## Models (stage 1 = the input's win chance; stages 2-3 = field-size discounted Harville, variant B5, refitted on each training window for that input)
- **A Market:** 09:00 market chance.
- **B Ours:** model chance.
- **C Blend (main form):** log-linear pool, p ∝ m^w1 · f^w2, with w1 and w2 fitted by win-only conditional logit on the training window.
  - Secondary form (reported, not used for decisions): linear mixture λf + (1-λ)m.
- **D Enhanced:** C's stage 1, plus stage-2/3 conditional logit on:
  - log pC and log pC × ln(n/10);
  - run-style score and lead share;
  - prior top-3 rate (with a count);
  - mean finishing-position score;
  - median overall beaten distance of the last 3 runs;
  - distance suitability (best position score within ±1f of today's distance);
  - going suitability (mean position score on today's going group);
  - class change from the last run (where class is known);
  - handicap × log p, favourite dummy, rank 2-3 dummy.
  - All features come from earlier runs only. Missing values are set to 0 with an indicator. L2 penalty 1.0.

## Walk-forward (all chronological)
**S second-stage fits** (blend weights, discounted-Harville exponents, D coefficients):
- expanding;
- for each test month M from May to Oct 2026, fit on replayed months Mar..M-1;
- development months: May-Aug 2026;
- **final S holdout: 1 Sep - 12 Oct 2026**, scored once after every choice is fixed.

**G:**
- parameters fitted on all S months (Mar - 12 Oct 2026, input = replayed model or market as each model needs);
- B, C and D are applied with the live model's chances;
- nothing is fitted on G.

The Phase 1 reverse split (S2) is not used as forward evidence.

## Metrics
- Top-2 and top-3 Brier.
- Win log-loss.
- Exacta and trifecta log-loss.
- P(2nd) and P(3rd) calibration slope plus decile tables.
- **Paired** date-block bootstrap differences against A (whole race days, 2,000 draws).

**Predictive-value pass (B, C, D vs A):** top-3 Brier AND trifecta log-loss improvement with 95% lower bound > 0 on the S holdout, AND the same sign in G (G too small to require significance).

**Independent-information pass:** w2 > 0 with z > 2 in every S training window, AND C passes predictive value.

## Disagreement (Phase 3)
- Δ = P_place(B) - P_place(A), in percentage points, places by the declared rule.
- Bands: < -15, -15..-10, -10..-5, -5..+5, +5..+10, +10..+15, > +15.
  - A band with fewer than 1% of development-month runners is merged with its neighbour. That rule is applied on May-Aug only.
- Per band: n, mean model P, mean market-Harville P, actual place rate, place-SP implied P (1/PSP, normalised per race so it sums to the places paid), calibration errors, mean PSP, model EV, and realised ROI at PSP (2%) with a 95% day-block interval.
- Both comparisons are reported: against market Harville, and against actual place SP.

## Betting (Phase 7)
- Back at Betfair place SP as a limit-on-close order. Limit = the price at which EV = T for the model's place probability.
- No BSP pool or volume data is archived, so partial matching cannot be reconstructed. All returns are **CONDITIONAL SIMULATIONS** (filled iff BSP >= limit).
- Models B, C, D. T ∈ {0, 2, 4, 6, 8, 10}%. Commission 2% and 5%. That is 36 cells. A is reported as a benchmark.

**Pass:**
- S-holdout ROI lower bound > 0 at the Bonferroni level (99.86% interval);
- AND profit in both holdout months;
- AND profit in at least 3 of 4 development months;
- AND a positive point estimate in G.

**Outliers (Phase 8):** for every cell:
- median and mean PSP, max payout, share of profit from the top 1% and 5% of payouts;
- profitable months, longest losing run, max drawdown;
- simulated ROI distribution (2,000 draws) under (i) the model's probabilities and (ii) place-SP implied probabilities, compared with the observed ROI.

**Not testable:**
- Each-way: no bookmaker EW terms or place prices.
- Exacta/trifecta profitability: no pre-race executable prices; Tote dividends exist for only about 221 races. Accuracy only.

## Segments (Phases 4-5)
- Ranks 4-8 and field sizes 5-7 / 8-11 / 12-15 / 16+.
- Also Flat/Jumps, handicap, odds band and win-chance band.
- Each segment reports predicted vs actual vs place-SP implied, and ROI at PSP, with intervals.
- Exploratory unless the same sign appears in all development months and the holdout.

## Phase 12 checks (exploratory, labelled)
- Does (log f - log m) at 09:00 predict the move from the 09:00 to the last-checkpoint (L) market log-odds? Measured on the S holdout.
- Is model-market disagreement useful as a filter on A-model place bets?

## Verdicts
- **PROMOTE TO FORWARD SHADOW TEST:** passes predictive value AND betting.
- **CONTINUE RESEARCH:** passes predictive value only, OR its point estimates are positive but the sample is too small.
- **REJECT:** fails predictive value on the S holdout.

Nothing goes live.
