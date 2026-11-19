# Phase 5 - forward test specification (summary)

**The sealed text is prereg/FORWARD_TEST_PHASE5_SPEC_2026-11-19.md.**
- sha256 50a1dc8ee0adca943a224b14ff34f32b2e474a0fee85e7a92e073cb7f189134a, also listed in prereg/SHA256SUMS.txt.
- Pushed in commit 24befa8. GitHub server push time 2026-11-19T13:21:34Z, before any forward-test race (the first is on 20 Nov).
- Any change is made only as a dated amendment.

| Element | Sealed choice |
|---|---|
| Models | Frozen E (hybrid) and frozen D2 (boosted residual), sha256 56179d9c…7178b52, as selected in Phase 4 (Amendment 1) |
| Baseline | 09:00 composite market (0.6 exchange mean + 0.4 / bookmaker median, normalised), from a snapshot collected 09:00-09:30 UK |
| Population | Races meeting all ten rules in spec section 3, judged without outcomes. All others go to the audit ledger as exploratory, with reasons |
| Runner list | Runners that ran; model and market renormalised over exactly the same runners |
| Primary metric | Race-level winner log-loss; paired d = log p_model(winner) − log m(winner) |
| Statistic | Race-weighted mean of d; z with a day-clustered standard error; the 97.5% day-block bootstrap interval reported alongside |
| Multiplicity | Bonferroni over E and D2: one-sided α = 0.0125 per model (the Phase 4 convention: lower bound of a two-sided 97.5% interval) |
| Looks | 1,000 / 3,200 / 6,400 / 9,600 / 12,800 confirmatory settled races. O'Brien-Fleming spending; critical z ∞ / 4.926 / 3.351 / 2.670 / 2.279 |
| Early stopping | For success only. **No futility stop.** Collection continues regardless |
| Secondary | Brier, top pick %, winner rank, concordance, calibration by band, gain by odds band / code / field size, early seal-time series, production model |
| Classification | PASS (boundary crossed) / CONTINUE FORWARD RESEARCH (not crossed, before the final look) / FAIL (not crossed at 12,800, qualified by power) |
| Exploratory, never decisive | X1 evening model, sweeps, CLV, execution scenarios, seal-time series |

**Why the extension from 1,000 races?** See POWER_ANALYSIS.md. At 1,000 races the test has about 9% power for the gain E showed historically. The 1,000-race point is kept as the first look, and the original Phase 4 statistic is reported there, but it is not decisive.

## Code changes after sealing (logged)
On 19 Nov, after commit 24befa8 and before any forward race, fwd.py gained:
- the exploratory `clv` command;
- a display fix for reason labels in the status counts (split on ": " so "09:00" is not cut).

The primary-analysis code (`race_ledger`, `load_confirmatory`, `paired_stats`, `analyze`, `predict0900`, `components`) is unchanged; see `git diff 24befa8 -- research/market_intelligence/phase5/fwd.py`.
