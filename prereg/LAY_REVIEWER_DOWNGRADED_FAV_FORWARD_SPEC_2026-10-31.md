# Forward paper test: lay the favourite when the LIVE reviewer marks it down (sealed 2026-10-31)

Why: exploratory look on 31 Oct at the live reviewer tracker (21-28 Oct, BSP available), a cut that was NOT pre-registered:
favourites (highest 09:00 market chance) that the live reviewer moved DOWN: 141 runners, 34 won, A/E vs BSP 0.81,
lay at BSP +4.6% per GBP liability (8 days, so the CI is not trustworthy). Shadow reviewer similar (56, A/E 0.77).
Earlier history: LAY_FAV_SPEC (price-blind model doubts the favourite) FAILED. So this is a hypothesis, not a finding.
21-30 Oct is the discovery sample and is EXCLUDED from the verdict.

## Rule (from races on 1 Nov 2026)
Favourite = runner with the highest 09:00 market chance (mkt) in data/card_review_tracker.csv (ties: skip race).
Lay at BSP when the LIVE reviewer's chance (rev) < mkt (moved DOWN). Non-runners and races voided: excluded.
P/L per lay: fav loses +0.98 x stake; fav wins -(BSP-1) x stake. Reported per GBP of liability (BSP-1).
Paper only. Nothing is staked.

## Verdict
After 300 settled lays or 30 Apr 2027, whichever first. PASS = return per GBP liability > 0 with day-block bootstrap
95% CI (3,000 draws) above 0, AND A/E vs BSP < 1 with CI below 1. Also reported: by size of the downgrade
(rev/mkt < 0.85 vs 0.85-1), Flat vs Jumps, and the shadow reviewer's downgraded favourites (Flat only, informational).
No change to the rule after this seal.
