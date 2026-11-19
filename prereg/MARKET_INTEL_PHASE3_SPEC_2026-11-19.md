# MARKET INTELLIGENCE PHASE 3 - win calibration, CLV, movement, timing. Sealed spec (19 Nov 2026)

Research only. No production code, model, bot or staking changes. Code lives in research/market_intelligence/phase3/.

Seen before sealing:
- Phase 1/2 results. These included 09:00 vs BSP drift by disagreement decile on S, the -0.27 correlation, and blend win log-loss on S May-Oct.
- Price-source comparisons (BSP vs Betfair-exchange quote and bookmaker median, by checkpoint).
- Data counts.

No win-betting, CLV or timing outcomes have been examined.

## Data categories
- **A, verified forward:**
  - live rebuilt-model chances 10-18 Nov 2026 (store/DAY/model.json, committed before the first off; model trained to 9 Nov);
  - the live bot-file bets 11-18 Nov (data/card_review_tracker.csv: Matchbook 09:00 price, BSP, result).
- **B, chronological replay:**
  - **S:** rebuilt model refitted monthly on earlier races (Phase 2 replay), Mar - 12 Oct 2026. Market checkpoints E (21:00 previous day), M (09:00), H (off-60m), T10 (off-10m), L (off-1s) from raw/odds*, plus BSP.
  - **H3:** the same replay extended to 26 Oct - 18 Nov 2026. The market snapshot comes from the timestamped sealed cards (fetched about 08:36-09:07 UK), plus BSP and results from the Racing API.
- **C, diagnostic only:**
  - recovered old-model chances (14 Oct - 9 Nov);
  - RBD closing data;
  - anything without timestamps.

Missing checkpoints (30, 15, 5 and 1 minute before the off) are not reconstructed. The raw per-bookmaker price histories that would allow it are on the VPS, not in this repo.

## Periods
- **Fitting:** expanding, using replayed months before the test month (from Mar 2026).
- **Development (strategy and parameter choice):** May-Aug 2026.
- **Re-used, previously examined in Phase 2:** 1 Sep - 12 Oct 2026. Reported and labelled. Not an untouched holdout.
- **Untouched holdout H3:** 26 Oct - 18 Nov 2026 (09:00 + BSP only).
- **Verified forward A:** 10-18 Nov, reported separately. It overlaps H3's dates but uses the live model, not the replay.

## Probabilities
- **f:** model chance.
- **f_cal:** f^a normalised per race, with a fitted on training by conditional logit (temperature calibration; ranking unchanged).
- **m_t:** production market chance at checkpoint t (0.6 × mean exchange implied + 0.4 × bookmaker median implied, normalised).
- **close:** 1/BSP normalised.
- **blend_t:** log-linear pool m_t^w1 · f^w2, fitted on training for each t.

## Win calibration (Phase 2 of the brief)
- Metrics: log-loss, Brier, ECE (10 equal-count bins), calibration slope and intercept.
- Cuts: predicted-probability band, odds band, model rank, field size, Flat/Jumps, handicap.
- Comparisons are paired with day-block bootstrap (2,000 draws).
- **Ranking vs calibration:** if f_cal remains far behind m_M, the error is ranking, not calibration. Also reported: within-race concordance (share of correctly ordered winner-loser pairs) and top-pick win rate.

## CLV (Phase 3 of the brief)
**Selections:**
- **S-sel:** runners with f_cal EV ≥ 0 at the 09:00 best bookmaker price.
- **B-sel:** blend_M EV ≥ 0 at the same price.
- **Live:** the bot-file bets.

**Conventions:**
- raw CLV = selection odds / closing odds - 1, with closing = BSP. Also bookmaker best at L where available.
- probability CLV = m_close,norm - m_sel,norm.
- commission-adjusted CLV vs BSP = sel / (1 + (BSP - 1)(1 - c)) - 1 for bookmaker prices, and the commission-adjusted ratio for exchange prices.

**Controls:** all other runners in the same races, and runners in the same 09:00 odds band that were not selected.

**Cuts:** odds band, model confidence (f_cal), disagreement, code, field size, selection time (E/M/H/T10).

**Stability:** by month.

## Movement (Phase 4 of the brief)
- Checkpoints M, H, T10, L and BSP.
- Measures: per-interval % odds change, change in normalised probability, rank change, shorten/drift.
- Predictive tests:
  - win log-loss of m_M, m_H, m_T10, m_L and BSP;
  - conditional logit win ~ log m_M + (log m_t - log m_M).
- Verify the -0.27: correlation of (log f - log m_M) with (log close - log m_M), with a day-block interval, by month, and with H, T10 and L as alternative closers.

## Disagreement (Phase 5 of the brief)
- dlog = log f - log m_t.
- Conditional logit win ~ log m_t + b+ · max(dlog, 0) + b- · min(dlog, 0), with interactions for rank 1-3, field ≥ 12, Jumps and handicap.
- Fitted on development, scored on re-used and H3. Also fitted at each checkpoint t, to see whether the information survives to the off.
- Bands (probability points): < -10, -10..-5, -5..-2, -2..+2, +2..+5, +5..+10, > +10.

## Strategies (Phases 6-7, win back bets, £1 fixed)
Price at the decision point:
- **Primary:** Betfair-exchange quote at that checkpoint, after commission c ∈ {2%, 5%}.
- **Secondary:** best bookmaker price (best case: no Rule 4, no limits, no restrictions).
- Every result is a conditional simulation.
- T ∈ {0, 4, 8}%.

| Strategy | Decision point | Rule |
|---|---|---|
| A original | M | f EV ≥ T |
| B calibrated | M | f_cal EV ≥ T |
| C blend | M | blend_M EV ≥ T |
| D market confirmation | H | blend_M EV ≥ T at M AND m_H > m_M AND blend_H EV ≥ 0 at H; bet at the H price |
| E drift avoidance | H | blend_H EV ≥ T, excluding runners whose odds drifted > k from M to H; k ∈ {10%, 20%, 30%} chosen on development |
| F disagreement-aware | M | blend_M EV ≥ T AND 0 ≤ dlog ≤ u; u ∈ {0.25, 0.5, 1.0} chosen on development |
| Timing T_t | t ∈ {M, H, T10, L} | blend_t EV ≥ T at t |

**Pass:**
- H3 ROI 95% lower bound > 0 at the Bonferroni level over all evaluated cells (99.9% interval);
- AND positive ROI in development and in the re-used period;
- AND mean raw CLV vs BSP > 0 on H3.

Strategies needing H/T10/L checkpoints can't be evaluated on H3, so at best they reach "preliminary signal".

## Execution (Phase 8 of the brief)
No depth, spread or volume data exists, so everything is a conditional simulation. Sensitivity:
- random fill at 50% and 75%;
- adverse fill: a back order at the M quote is filled only if the H quote is at least as long (worst case for drifters).

## Verdict language
- **Proven:** passes on H3 with correction.
- **Preliminary signal:** consistent sign in development and re-used periods, but not testable or not significant on H3.
- **Unsupported:** otherwise.
