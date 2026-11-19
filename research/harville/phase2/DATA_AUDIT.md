# Phase 2 - data audit (19 Nov 2026)

Phase 1 files are untouched: research/harville/*.py, research/harville/out/* and prereg/HARVILLE_ICM_SPEC_2026-11-19.md.

The Phase 2 spec was sealed before any comparison of our model's chances with outcomes or with the market:
- file: prereg/HARVILLE_PHASE2_SPEC_2026-11-19.md;
- sha256: dc20868ceb7970173ff05fa54bde7f0b7f3f981edf93ef81406de5a939ffb874.

## 1. What was audited in Phase 1
| Item | Where | Finding |
|---|---|---|
| Discounted Harville parameters | research/harville/out/final_params.json | B5 (field-size exponents), fitted on all of track O, so it includes Phase 1's test periods. **Not reused as-is in Phase 2**: refitted inside every walk-forward window instead. |
| Learned ranking model | research/harville/run.py (model C) | Market input only. Phase 2's enhanced model D replaces it with our model's information and runner features. |
| Betting simulation | research/harville/run.py | Place SP, limit-on-close, day-block bootstrap. Places used the ran-count rule (see §3). |
| Confidence intervals | day-block bootstrap, 2,000 draws | Kept. Phase 2 adds **paired** differences on identical races. |
| Phase 1 split S2 (fit later, test earlier) | Phase 1 | Reverse-chronological. **Not used as forward evidence** in Phase 2. |

## 2. Our model's archived chances: provenance
| Set | Dates | Races | Provenance check | Status |
|---|---|---|---|---|
| **G** rebuilt model (store/DAY/model.json) | 10-18 Nov 2026 | 217 eligible | (1) models/win_model.json says "history to 2026-11-09"; its only git version is commit 8e02309, 10 Nov, so it was never retrained. (2) Each day's model.json was committed at 08:36-08:41 UTC, before the first off (10 Nov at 10:21 UTC, also before the first off). | **Genuine pre-race; used** |
| G reviewer chance (sealed) | 10-18 Nov 2026 | 217 | Sealed at 08:37-08:41 UTC (git); the reviewer saw the card and the 09:00 market only | Genuine; reported as a variant |
| **G0** old-model chances (report/history_data.json) | 14 Oct - 9 Nov 2026 | ~1,000 | File first committed 10 Nov (recovered). The old model's code and training window are lost, so it cannot be shown that predictions were made pre-race or by a model blind to later results. | **Unverified; not used for any conclusion** |
| **S** chronological replay of the rebuilt model | Mar - 12 Oct 2026 | 8,132 | Same production feature code (pipeline/models.py, imported unchanged). Refitted monthly on races before the 1st of each month. Features use only a horse's earlier runs plus that day's official rating and weight. | **Synthetic**, out-of-time, labelled throughout and never pooled with G |

Replay caveats:
- History starts on 1 Jan 2026, so features are thin in Mar-Apr.
- Field size counts runners that ran, as in production.
- Beaten distances are missing for the RaceData-sourced history, so that feature is empty in S (see §6).

## 3. Place terms: the 89% agreement, resolved
Phase 1's rule counted runners that **ran**. Betfair sets place terms when it creates the market, from **declared** runners, and does not change them when non-runners are withdrawn.

On the 1,490 track-O races with Betfair's own placed flag (RBD):

| Rule | Agreement | 5+ ran only |
|---|---|---|
| Ran count (Phase 1) | 90.8% | 94.5% |
| **Declared = ran + listed non-runners (Phase 2)** | **97.2%** | **99.2%** |

- The remaining 5+ runner mismatches: 11 races (0.8%). Seven of them are 7 ran + 1 non-runner where Betfair still paid 2 places; the other four are isolated (e.g. 3 places in a 6-runner handicap).
- Most residual mismatches overall are races with fewer than 5 runners, which are excluded from betting.
- Across all 44k RBD races, mismatches concentrate where the ran count crosses a boundary: 7 runners paying 3 places (8 declared), 14-15 runners paying 4 (16+ declared).
- Under-5 races are never bet.
- **Phase 2 uses the declared rule everywhere.**

Further settlement notes:
- **Non-runners and reduction factors:** a limit-on-close bet is matched at BSP after non-runners are removed, so no reduction factor applies.
- **Dead heat for the last place:** the stake is split equally among the tied horses.

## 4. Market prices available
| Source | Content | Coverage (S races) | Use |
|---|---|---|---|
| raw/odds_flat, raw/odds (checkpoints E 21:00 day before, **M 09:00**, H off-60m, T10 off-10m, L off-1s) | Bookmaker median and best, Betfair/Matchbook/Smarkets win prices | Median 98-99.5% at every checkpoint | 09:00 market chance (production formula). Later checkpoints only for the movement check |
| Results (Racing API) | Win BSP, positions, non-runners | 100% | Settlement; closing win market (diagnostic) |
| Betfair place SP (RBD + RaceData) | Place BSP | 86% of track O; 96.8% of eligible S runners May-Oct | Place bets (limit-on-close) |
| Tote/CSF dividends | Racing API results | 221 races, 10 Nov onwards | Not enough for exotics betting |
| Bookmaker each-way terms and place prices | none | 0 | Each-way NOT TESTABLE |
| BSP pool volumes / reconciliation detail | none | 0 | LOC partial matching NOT reconstructable -> conditional simulation |

The 09:00 "Betfair Exchange" win quotes are thin. On average BSP is 40-130% (log 0.3-1.3) above them, so they are **not treated as executable 09:00 prices**.

## 5. Leakage checks
- Replay fits use only races dated before the test month. Second-stage fits (blend weights, discount exponents, D coefficients) use only replayed months before the test month (expanding window).
- Final holdout S Sep-Oct and the genuine set G were not looked at until all choices were fixed.
- G parameters were fitted on S (Mar - 12 Oct), before G's dates.
- One small leak shared with production: field size (n) counts runners that ran. Late non-runners after 09:00 are therefore known to the model. The effect is small and identical for every model compared.

## 6. Coverage of the enhanced-model features (S)
| Feature | Present |
|---|---|
| Run style (from in-running comments) | 78% |
| Prior top-3 rate, position score | 87% |
| Distance suitability (±1f) | 71% |
| Going suitability | 57% |
| Class change | 63% |
| Median beaten distance | 0% (RaceData history has no beaten distances; empty feature, coefficient 0) |

Place SP is present for 96.8% of eligible S runners in May - 12 Oct.
