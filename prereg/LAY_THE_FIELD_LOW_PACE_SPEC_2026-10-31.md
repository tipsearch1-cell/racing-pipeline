# Lay the field at 2.0 or lower, using pace (sealed 2026-10-31, before any result at these prices is looked at)

Follows LAY_THE_FIELD_SPEC_2026-10-31 (L = 3/4/6 FAIL). User asks: L = 2.0 or lower, and can pace pick races where
several horses trade low in running? Only L = 3.0/4.0/6.0 results have been seen; nothing at L <= 2.0 and no pace feature has been tried.

## Data, strategy, fill rule, P/L, periods: as LAY_THE_FIELD_SPEC_2026-10-31
(RBD GB Flat 2023-03..2026-10; train 2023-03..2024-12, valid 2025, test 2026.)
Primary L = 2.0 (strict fill: IP Min <= 1.99). Secondary L = 1.5 (strict: IP Min <= 1.49). Lay only runners with BSP > L.
A laid winner costs L-1; each matched loser pays 1. 2% commission on a positive race P/L.

## Pace features (RBD pre-race "Pace", 0-10, higher = races nearer the front, 0 = no history; checked not to leak in
PACE_FORECAST_RBD_BACKTEST_SPEC_2026-10-22)
n_front = runners with Pace >= 8; n_known = runners with Pace > 0; mean Pace of known; top Pace; 2nd top Pace; gap top1-top2;
sd of known Pace; share unknown.

## Tests
M (PRIMARY): ridge (alpha 10, standardised) on the LAY_THE_FIELD features plus the pace features, target race P/L
(strict, before commission), fit on train. Bet races with predicted P/L > 0.
R1 (secondary): no front-runner, n_front == 0 and n_known >= 4 (expected slow, bunched finish).
R2 (secondary): contested, n_front >= 3.
Also reported: all races; M without pace features (to see what pace adds); L = 1.5 for everything.

## Pass rule
M PASSES only if at L = 2.0, strict fill, selected races have mean P/L per race > 0 with day-block 95% CI above 0
in validation AND test, with more than 300 races in each. R1/R2 are informational (only noteworthy if both periods' CIs exceed 0).
A pass would justify a paper forward test only.
