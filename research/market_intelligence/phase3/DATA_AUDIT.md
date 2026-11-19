# Phase 3 - data audit

**Spec:** prereg/MARKET_INTEL_PHASE3_SPEC_2026-11-19.md, sealed before any win-betting, CLV or timing outcome was examined.
- sha256: e42389928f369837b12f84bc23b1079ce776ab665d91aba299593fce968feeca
- No amendments.

**One control analysis was added after the first run, labelled as such:**
- Market-only (no model) versions of the bookmaker-price strategies, out/control_market_only_bookmaker.csv. They test whether any positive result needs our model.
- Odds-band-controlled versions of the disagreement-movement correlation.

Both change interpretation only. Neither changes a strategy.

Phase 1 and Phase 2 research is untouched. One erratum is added as a separate file: research/harville/phase2/ERRATUM_2026-11-19.md.

## Categories
| Cat. | Dataset | Period | Races | Provenance |
|---|---|---|---|---|
| **A, verified forward** | Live rebuilt-model chances (store/DAY/model.json) | 10-18 Nov 2026 (19 Nov archived, not yet settled) | 221 | First git commit of each day's model.json at 08:36-08:42 UTC (10 Nov: 10:21 UTC), before the first off. models/win_model.json "history to 2026-11-09", one version only. |
| A | Sealed reviewer chance | 10-18 Nov | 221 | Sealed 08:37-08:41 UTC (git) |
| A | Live bot-file bets (Matchbook 09:00 price, BSP, result) | 11-18 Nov | 32 with BSP | data/card_review_tracker.csv, published before 09:30 |
| **B, chronological replay** | S3: the production win model refitted monthly on earlier races (Phase 2 replay) | Mar - 12 Oct 2026 | 8,196 | Out-of-time; same code as production |
| B | **H3:** the same replay for Oct and Nov (fit on races before 1 Oct / 1 Nov) | 26 Oct - 18 Nov 2026 | 776 (674 with full BSP) | Out-of-time. The 09:00 market comes from the timestamped sealed cards (fetched 08:36-09:07 UK) |
| **C, diagnostic only** | Recovered old-model chances | 14 Oct - 9 Nov | about 1,000 | First committed 10 Nov; training window unknown |
| C | RBD GB Flat closing prices | 2020-2026 | 44,761 | Closing prices only; no decision-time data |

Categories are never pooled. Every table names its set.

## Market data: what exists
| Item | Available? | Source / note |
|---|---|---|
| 21:00 previous day (E) | Yes, Oct 2025 - 12 Oct 2026 | raw/odds_flat, raw/odds (checkpoint archive by McCoy) |
| 09:00 (M) | Yes, same period; plus sealed cards 26 Oct onwards | as above; store/DAY/sealed_card.json.gz |
| 60 min before the off (H) | Yes, to 12 Oct 2026 | checkpoint archive |
| 30 / 15 / 5 min before the off | **No** | Not archived as checkpoints. The provider's full per-bookmaker price-change histories (with timestamps) are on the VPS (raw/runner_spool, raw/odds/<day>.jsonl.gz per the archive README) but not in this repo. They would allow exact reconstruction. **Not fabricated here.** |
| 10 min before the off (T10) | Yes, to 12 Oct | checkpoint archive |
| 1 second before the off (L) | Yes, to 12 Oct | checkpoint archive ("price at supplied off": actual-off provenance not established) |
| BSP (win) | Yes | Racing API results; RaceData Betfair SP fills API gaps (10-12 and 18 Nov API BSP blank) |
| Back/lay prices, spread, depth, traded volume | **No** | The provider gives one "Betfair Exchange" price (and Matchbook/Smarkets) per runner. No lay side, no volume, no market status, no suspension events |
| Actual off time | No | Scheduled/supplied off only |
| Commission | Assumption | 2% (Betfair Basic/Matchbook-like) and 5% sensitivity |
| Bookmaker each-way terms | Yes, per quote (ew_places, ew_denom) | In the sealed cards and raw provider records. Not archived in the checkpoint CSVs. Could support a future each-way study |

## What the exchange quote is
Median BSP divided by the provider's "Betfair Exchange" price, by checkpoint (Jun-Aug 2026, Flat):

| Checkpoint | E | M | H | T10 | L |
|---|---|---|---|---|---|
| BSP / exchange quote | 1.89 | 1.26 | 1.11 | 1.07 | 1.04 |

- The morning exchange quote is far shorter than where the horse eventually goes off. It behaves like the best back price in a thin early market.
- Near the off it converges to BSP: within ±4% for runners under 11.0, but still 25% short of BSP for 50+ shots.
- **Morning exchange quotes are therefore not executable "value" prices**, and raw odds-based CLV across different price sources is confounded. Phase 3 uses the **normalised market probability** (same composite at both times) as its primary CLV measure.

## Existing logic reviewed
| Item | Where | Notes |
|---|---|---|
| Bet selection | pipeline/card_review.py, pipeline/reviewer_bets_csv.py | Favourite checks (reviewer BET on 09:00 favourites, 3.0-7.0) and value flags. Price = Matchbook 09:00 or median; MinPrice limit |
| Staking | flat £1 (bot); multiples £0.50 a line | |
| Earlier movement analysis | Phase 2 DISAGREEMENT_ANALYSIS.md §4 | **Corrected in Phase 3** (MARKET_MOVEMENT.md) |
