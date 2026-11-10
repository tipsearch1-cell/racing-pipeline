# Forward paper test: model top pick in Flat all-weather races (sealed 2026-11-02, ~22:00 local)

Why: exploratory look on 2 Nov at data/tracker.csv, 12 Oct - 2 Nov (NOT pre-registered): Flat all-weather top picks
215, won 59, A/E vs BSP 1.08, ROI +10.0% at the 09:00 best price, +9.6% at BSP (CI about [-25%, +47%]).
Flat turf 0.92, jumps ~1.00. Earlier back-tests found no model edge beyond BSP. So this is a hypothesis only.
12 Oct - 2 Nov is the discovery sample and is EXCLUDED from the verdict.

## Rule (races from 3 Nov 2026)
Every model top pick in data/tracker.csv with code == Flat in an all-weather race (race segment "Flat all-weather",
i.e. sealed card surface AW) - handicaps and non-handicaps. Nothing changes in the daily build: race_report.py
already writes the pick and its 09:00 best price ("price") before racing, and settle_tracker.py checks picks are unchanged.
Paper only. Nothing is staked.

## Settlement
(1) PRIMARY: level stakes at the 09:00 best price recorded on the card (pl_price).
(2) Level stakes at BSP with 2% commission on winnings (from store/<day>/results_all.json.gz).
(3) A/E vs BSP (winners / sum of 1/BSP). Non-runners excluded.

## Verdict
After 300 settled picks or 30 Apr 2027, whichever first. PASS = (1) ROI > 0 with day-block bootstrap 95% CI
(3,000 draws) above 0, AND (2) ROI at BSP > 0. Also reported: handicap vs non-handicap, and by course.
No change to the rule after this seal.
