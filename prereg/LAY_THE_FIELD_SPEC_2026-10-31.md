# Lay the field (LTF): can we pick the races where it pays? (sealed 2026-10-31, before any LTF result is looked at)

Question (user, 31 Oct): can we predict close races for a lay-the-field strategy?

## Data
RBD GB Flat files, raw/rbd/2023-2026 (2023-03 to 2026-10-09). Race key = date + track + off time.
Per runner: Betfair SP (B), IP Min (lowest price traded in running), Place.
Races kept: every runner has B > 1 and IP Min > 1, exactly one winner (Place == "1"), 4+ runners.

## Strategy (per race, at the off, before any in-running information)
Lay every runner with B > L at price L for a £1 lay stake (liability L-1 each).
Primary L = 4.0. Secondary (reported, not used for the verdict): L = 3.0 and L = 6.0.
Fill rule (PRIMARY, strict): a lay is matched only if the price traded THROUGH L: IP Min <= L minus one Betfair tick
(4.0 -> 3.95; 3.0 -> 2.98; 6.0 -> 5.9). Optimistic rule (IP Min <= L) reported as a sensitivity only.
The winner always trades to ~1.01, so a laid winner is always matched.
Race P/L = (matched losers x 1) - (L-1 if the winner was laid). 2% commission on a positive race P/L.
Turnover for ROI = sum of liability of all lays placed (n laid x (L-1)).

## Prediction (pre-off only; nothing from in running or the result)
Features per race: number of runners; number laid (B > L); favourite's BSP; 2nd favourite's BSP;
market overround at BSP; book entropy of 1/B (normalised); number of runners with B in (L, 2L];
share of 1/B held by runners with B > L; handicap flag (Type contains Handicap or Nursery); AW flag (Going code SD/ST/STD or track in the AW list);
distance in furlongs; class; month.
Model: ridge regression (alpha 10, standardised features) of race P/L (strict rule, before commission),
fit on 2023-03..2024-12, tuned on nothing. Selection rule fixed now: bet races with predicted P/L > 0.

## Periods
Train 2023-03..2024-12. Validation 2025-01..2025-12. Test 2026-01..2026-10.

## Pass rule (pre-registered)
PASS only if, under the STRICT fill rule at L = 4.0, the selected races have
(a) mean P/L per race > 0 with day-block bootstrap 95% CI (3,000 draws) above 0 in validation AND in test, and
(b) more than 300 selected races in each of validation and test.
Also reported: all races (no selection) per period; ROI on liability; secondary L; optimistic fill.

## Caveats written now
IP Min is the lowest traded price, not proof our lay at L would have been filled (queue position; brief touches);
the strict rule needs a full tick through, but fills can still be overstated. Earlier test (INPLAY_AND_RA_SPEC) found
in-running prices unreliable for back-to-lay. A PASS would justify a small paper forward test, not real stakes.
