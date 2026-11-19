# HARVILLE / ICM finishing-position research - sealed spec (19 Nov 2026)

Research only. Nothing here changes the live bot file, the reviewer, the models or any staking. Outputs go to
research/harville/ (code, out/, work/). Written before any finishing-position outcome was compared with any model.
What was seen before sealing: data counts and coverage only (research/harville/out/inventory.md). Prior knowledge
from the literature (not from our data): Harville is reported to over-rate favourites for 2nd/3rd (Henery 1981;
Lo & Bacon-Shone 1994 suggested discount exponents near 0.8 and 0.65).

## Data (see inventory.md)
- **O (main).** 09:00 UK market archive, GB+IRE Flat and Jumps, 13 Oct 2025 - 12 Oct 2026.
  - Input = 09:00 market chance, using the production formula. Its timestamps are genuinely pre-race.
  - Places: finishing positions (Racing API).
  - Place price: Betfair place SP (RBD/RaceData), joined on date+course+horse.
- **F (Frankie, genuine forward, final holdout).** Archived pre-race Frankie chances:
  - the old model p as published on the recovered report page, 14 Oct - 9 Nov 2026 (publication time assumed, not timestamp-verified);
  - the rebuilt model p (store/DAY/model.json) and the sealed reviewer chance rev, 10 Nov onwards;
  - plus the 09:00 market.
  - Untouched until the models below are fixed. Nothing is fitted on F.
- **R (diagnostic).** RBD GB Flat 2020-01-01 to 2026-10-09.
  - Input 1 = closing win BSP. This is an outcome, so it is diagnostic only: no betting with it.
  - Input 2 = RBD "Forecasted Odds" (racecard forecast; pre-race by definition, timestamp not verified). Labelled as such.

Race eligibility:
- every runner has an input chance;
- 3+ runners with a numeric finishing position;
- no dead heat in the first three (dead-heat races are counted and excluded from the ordered metrics);
- inputs renormalised over the runners that ran.

## Models
Stage 1 (who wins) is the input win chance unchanged in every model, so the models differ only in 2nd/3rd.
- **A** Harville: sequential selection, weights = p.
- **B** Discounted Harville. Stage-2 weights p^a and stage-3 weights p^b, each normalised over the runners left. Candidates:
  - B1: a = b;
  - B2: a and b separate;
  - B3: B2 separately for Flat and Jumps;
  - B4: B2 separately for handicap and non-handicap;
  - B5: B2 with each exponent linear in log(field size).
  - The variant is picked on the fit period only, by lowest BIC on the stage-2+3 log-likelihood.
- **C** Learned ranking (Plackett-Luce style, conditional logit per stage 2 and 3). Features:
  - log p, plus log p x Jumps, log p x handicap and log p x log(n);
  - favourite dummy (rank 1 by input) and rank-2/3 dummy;
  - class (where known).
  - L2 penalty 1.0 on non-intercept terms. Fitted on the fit period only. No market features beyond the input chance, and no post-race data.
- **D** Market Harville: A applied to the 09:00 market. On O, D = A. On F, D is the benchmark for the Frankie-input models.
- **E** Existing Frankie place probabilities: none exist -> N/A.

## Splits (research rule 2)
- **S1:** fit 13 Oct 2025 - 31 Mar 2026 -> test 1 Apr - 12 Oct 2026.
- **S2:** fit 1 Apr - 12 Oct 2026 -> test 13 Oct 2025 - 31 Mar 2026.
- **Final:** fit on all of O -> apply once to F (input = each Frankie chance and the 09:00 market).
- **R:** expanding walk-forward. Fit 2020..Y-1, test year Y, for Y = 2022, 2023, 2024, 2025, 2026 (to 9 Oct). Used for parameter stability.

## Accuracy metrics (per test period)
- Top-2 Brier and top-3 Brier (per runner).
- P(2nd) and P(3rd) calibration: decile tables plus logistic calibration slope.
- Ordered exacta log-loss = -log P(actual 1st,2nd), and trifecta log-loss = -log P(1st,2nd,3rd).
- Expected vs actual counts by input rank (1-6) for 2nd and 3rd.
- Segments, with n and intervals: Flat/Jumps, handicap, field size (5-7, 8-11, 12-15, 16+), favourite rank, win-chance band and odds band.

Uncertainty: 95% date-block bootstrap (resample race days, 2000 draws) on the difference from A.

**Accuracy pass for B or C:** lower bound of the trifecta log-loss gain over A above 0 in BOTH S1 and S2 tests.

## Betting (Phase 7)
**Place market, Betfair place SP.**
- Places paid = Betfair standard terms on runners that ran: 5-7 -> 2, 8-15 -> 3, 16+ -> 4 if handicap else 3; under 5 -> no market.
  - Validated against RBD's "Placed in Betfair Market" (89% match). R uses the RBD flag itself.
- Executable as a Betfair limit-on-close back bet. Back £1 when EV = P(place) x (1 + (PSP - 1)(1 - c)) - 1 >= T. This holds only when PSP >= the limit price implied by P and T, so only pre-race information decides the limit.
- c = 2% (main) and 5%.
- T in {0, 2, 4, 6, 8, 10}%.
- Dead heats for the last place: stake split by the dead-heat rule.
- Benchmark: back every runner at place SP. Each B and C rule is also compared with the A rule at the same T.
- Inputs allowed: O = 09:00 market; F = Frankie chances and 09:00 market; R = Forecasted Odds only (never BSP).
- Report:
  - bets, stake, return, P/L, ROI;
  - 95% date-block interval;
  - max drawdown and longest losing run;
  - by month and quarter;
  - ROI without the top 1% of returns.

**Betting pass:** ROI 95% lower bound > 0 in BOTH S1 and S2 tests, AND profit in every calendar quarter of the tests.
- Multiple comparisons: 6 thresholds x 3 models x 2 commissions = 36 cells. A pass is only provisional unless it also holds at the Bonferroni level (99.86% interval).
- F is reported but is too small to pass or fail anything.

**Not testable:**
- Each-way: no archived bookmaker place terms or each-way prices.
- Forecast/exacta and tricast/trifecta: Tote and CSF dividends exist only for about 221 races (10 Nov onwards), and no pre-race executable price exists. Accuracy only; profitability = NOT TESTABLE.
- Win BSP is never used to manufacture place or exotic returns.

## Mispricing (Phase 8)
- Place-market ROI at place SP by input rank, odds band and field size, under model A and the selected B/C.
- Exploratory unless the same sign appears in both S1 and S2 tests and in at least 4 of 5 R test years (Forecasted Odds input).

## Verdicts
For each of B and C:
- **PROMOTE TO FORWARD SHADOW TEST** only if it passes accuracy AND a betting cell passes.
- **CONTINUE RESEARCH** if it passes accuracy only.
- **REJECT** otherwise.

No live implementation follows from this test, whatever the result.
