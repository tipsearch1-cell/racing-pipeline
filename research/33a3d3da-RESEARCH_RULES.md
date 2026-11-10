# Research rules for the racing model

These rules apply to anyone building or changing a model in this project, whether a person or an agent.
They exist because almost every idea looks profitable on the data it was built from. Read FINDINGS.md
before starting: about 20 ideas have already been tested, and most failed.

## 1. Seal the test before looking at outcomes
- Before comparing any new feature, rule or model with results, write a spec in `prereg/NAME_SPEC_<date>.md`:
  the data, the date periods, the exact rule or features, the comparison baseline, and the pass rule.
- Record its fingerprint: `sha256sum prereg/NAME_SPEC_<date>.md`, and put that line in the report.
- After the spec is sealed, changes go in a dated **Amendment** at the bottom, written before the affected
  outcome is seen, saying what changed and why. Never edit the original text.
- If an outcome was looked at before sealing, say so in the spec. That test counts only as exploratory.

## 2. Test only on data the model has not seen
- Fit on earlier dates, score on later dates (walk-forward). Never score on the period used for fitting or tuning.
- Any threshold, weight or setting must be chosen on the fit period only.
- Use two splits where the data allows (for example fit Jan-May -> test Jun-Oct, and fit Jan-Oct -> test the
  earlier Oct-Dec). A real improvement should hold in both.
- Use only information available before the decision time (10:00 UK on race day). Final BSP, in-running
  prices, results and post-race comments are outcomes, not inputs.

## 3. Measure the right thing
- **Accuracy:** win log-loss gain over the current live model, with a 95% date-block bootstrap interval
  (resample whole race days, 2000 draws). Pass = lower bound above 0.
- **Betting:** ROI at prices you could really get, with a 95% date-block interval. The benchmark is Betfair SP
  after 2% commission (also report 5%). Backing everything at BSP loses about 3%; that is the bar to beat.
- Bookmaker prices: allow for Rule 4, treat Best Odds Guaranteed as a best case, and remember a winning
  account gets restricted.
- A betting rule passes only if the interval is above 0 **and** it is profitable in each sub-period
  (for example each year). One good period is not enough.
- Always report failures with the same detail as passes.

## 4. Changing the live model
- The live report model changes only after a sealed test passes. Note the spec name in the code comment.
- Keep logging the previous model's probabilities alongside (data/v1v2_forward.csv) so the change can be checked
  on live races.
- Review live performance at the agreed checkpoint (end of December 2026 or 300 Flat handicap picks).

## 5. Published picks are never changed
- Once a day's report is published, its picks are fixed. Never re-run `race_report.py` for a published day.
  12-13 Oct 2026 were published with `race_report_v1.py`.
- Settle results with `pipeline/settle_tracker.py`, which refuses to run if any pick would change.
- Back up `data/tracker.csv` and `data/ew_tracker.csv` before any run that writes to them.

## 6. Safety
- Racing API credentials only in environment variables `RACING_API_USERNAME` / `RACING_API_PASSWORD`.
  Never print them, write them to files, or send them in messages.
- Read-only use of data sources. No bets, no account changes.

## 7. Checking two installations agree
- `python3 pipeline/fingerprint.py <day>` prints hashes of the input card, picks, model % and tracker.
  Same card + same code must give the same picks hashes. 14 Oct 2026 matched between the cloud build and the VPS.
