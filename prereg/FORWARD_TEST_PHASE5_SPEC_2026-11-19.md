# PHASE 5 FORWARD SHADOW TEST - sealed spec (19 Nov 2026, before any prospective outcome exists)

Research only. No production model, bot, strategy or schedule change. No bets. Code: research/market_intelligence/phase5/ (fwd.py at the commit that adds this file).

This spec preserves the Phase 4 selection: frozen **Model E (hybrid)** and frozen **Model D2 (boosted residual)** are compared with the 09:00 market.
- Spec: prereg/MODEL_RECON_PHASE4_SPEC_2026-11-19.md + Amendment 1.
- Frozen artefact: research/model_reconstruction/phase4/models/frozen_2026-11-19.pkl, sha256 56179d9cf676d7d02a2ceb4e0cb484896057a4e0a9fbf8fcb5333bcc87178b52.
- The artefact was first pushed to GitHub at 2026-11-19T13:01:02Z (GitHub activity log, push 0d1db41).

**Seen before sealing:**
- Phase 1-4 results.
- The historical paired differences used for the power analysis (out/power.json): development and re-used data only.
- One live connector fetch of 19 Nov cards (for capture validation; 19 Nov is not a forward-test day).
- No forward-test race has been run.

## 1. What changed relative to the Phase 4 shadow plan, and why
1. **Market timing.**
   - The Phase 4 shadow script (shadow.py) uses the market in the sealed card, fetched at about 08:36 UK. The provider's own quote timestamps confirm this: 08:37 on 19 Nov.
   - The frozen models were trained on the **09:00** checkpoint (M).
   - Therefore, as the Phase 5 brief requires, the **confirmatory** predictions use a genuine 09:00 snapshot (section 3).
   - The seal-time shadow file continues unchanged as a separate, **exploratory** "early" series. Both timestamps are kept.
2. **Sample size.**
   - The original "≥ 1,000 races, 95%-interval lower bound > 0 (Bonferroni 97.5%, two models)" rule is badly under-powered.
   - At 1,000 races the power is about 9% for a true gain of 0.003 (section 6).
   - The test is therefore **extended prospectively** with the group-sequential rule in section 6.
   - The 1,000-race point is kept as look 1, and the original statistic is reported there, but it is not decisive.
   - Nothing else in the Phase 4 rule changes: paired race-level winner log-loss vs the 09:00 market, day-level blocks, Bonferroni over E and D2, and one-sided error 1.25% per model.

## 2. Daily procedure (research-only steps after the production build is published; never before it, never changing it)
| Step | Time (UK) | Command | Output (write-once, chained manifest) |
|---|---|---|---|
| R0 | 21:00 the evening before | connector `get_racecards_standard day=tomorrow` (with odds), then `fwd.py ingest E <saved file>` | phase5/snapshots/E/… |
| R1 | after publishing (about 08:45) | `shadow.py predict DAY` (Phase 4, unchanged) | shadow_phase4.json.gz (exploratory seal-time series) |
| R2 | after publishing | `fwd.py components DAY` | phase5/components.json.gz: market-independent parts g_D2(x), s_C(x), production f, frozen sha |
| R3 | 09:00-09:30 | connector `get_racecards_standard day=today` (with odds), then `fwd.py ingest M <saved file>` | phase5/snapshots/M/… |
| R4 | immediately after R3 (by 09:30 at the latest) | `fwd.py predict0900 DAY`, commit, push, `fwd.py stamp DAY`, commit, push | phase5/pred_0900.json.gz + phase5/stamps/… (GitHub server push time) |
| R5 | live checks (12/14/16/18 UTC) | `fwd.py ingest SWEEP <saved file>` | exploratory pre-off sweeps |
| R6 | next morning's settle | `fwd.py settle DAY`, `fwd.py status DAY` | results.json.gz; status/DAY.json (no outcome statistics) |

**How the 09:00 predictions are computed.** They are a deterministic function of frozen components and the 09:00 composite market m:
- D2 = softmax(log m + g_D2).
- E = softmax(1.0792·log m + 0.04381·s_C + 0.05936·log f).
- The weights are those of the frozen artefact.
- This was verified to reproduce shadow.py exactly when given the same market: max difference 5e-7, 18 Nov dry run.

**Retries.** If the 09:00 fetch fails, it is retried until 09:30. If there is no valid snapshot by 09:30, `predict0900` records "NO VALID 09:00 SNAPSHOT" and every race that day is exploratory. The file is never rewritten afterwards.

## 3. Confirmatory eligibility (race level, decided without outcomes)
A race is **confirmatory** only if all of the following hold:
1. It is on the sealed card.
2. Components exist, made with the frozen sha above.
3. The 09:00 snapshot was collected between 09:00 and 09:30 UK. The earliest valid snapshot is used.
4. The race is in that snapshot and not abandoned.
5. The newest provider quote in the race is ≤ 30 min old at collection.
6. Every remaining runner has a 09:00 price and a production chance.
7. No runner was added after the seal, and no card runner is missing from the snapshot (a mapping error).
8. At least 2 runners remain.
9. pred_0900.json.gz carries a GitHub push stamp earlier than the race's scheduled off.
10. The race settles with exactly one winner. Void races and dead heats for first are excluded, with the reason recorded.

Further rules:
- Non-runners declared between seal and 09:00 are dropped, and the race stays eligible (flagged).
- At evaluation, model and market are renormalised over the **same** runners that ran.
- Every race appears in the audit ledger (`fwd.py verify`, `race_ledger`) with its reasons. Ineligible races are **exploratory** and are never re-admitted after the results are known.

## 4. Primary metric and comparison
- Per confirmatory race, d = log p_model(winner) − log m_0900(winner). Positive means the model has lower winner log-loss.
- Statistic: mean of d over races, with z = mean / (day-clustered standard error, races grouped by race day).
- Models: E and D2, each against the 09:00 market. Bonferroni over 2: one-sided α = 0.0125 per model.
- Reported with each look: the day-block bootstrap percentile interval at 97.5% (10,000 draws, seed 20261120), which is the Phase 4 convention.

## 5. Secondary metrics (descriptive, every look)
- Multiclass Brier, top-pick win %, winner's mean rank, concordance.
- Calibration by probability band.
- Gain by 09:00 odds band, by code (Flat/Jumps) and by field size.
- The seal-time (early) series and the existing production model as further descriptive comparators.

## 6. Sample size and looks (out/power.json, sha256 b10626e5…cda067)
**Planning inputs** (historical, previously examined):
- Per-race standard deviation of d: 0.094 (worst of E/D2, pooled).
- Design effect for day clustering: 1.33.
- About 30-39 races per day.

**Fixed-sample sizes** for 80% power at one-sided α = 0.0125:

| True gain | Races needed | Power at 1,000 races |
|---|---|---|
| 0.002 | 27,909 | 5% |
| 0.003 | 12,404 | 9% |
| 0.005 | 4,466 | 22% |

**Rule.**
- Looks at **1,000 / 3,200 / 6,400 / 9,600 / 12,800** confirmatory settled races.
- Each look is taken at the end of the race day on which the count is reached.
- Alpha is spent with Lan-DeMets O'Brien-Fleming, one-sided 0.0125 per model.
- Critical z by look: **∞ / 4.926 / 3.351 / 2.670 / 2.279** (cumulative α 0 / 5.9e-7 / 4.1e-4 / 3.9e-3 / 0.0125).
- A model **PASSES** at the first look where z exceeds the critical value.
- Simulated power with day-block resampling: E 87% at 0.003 and 55% at 0.002; D2 82% at 0.002. Simulated type-I error is 1.3% for E and 0.7% for D2.
- **No futility stop.** Collection continues whatever interim results show. No other significance test of the primary metric is run between looks. The daily status report carries counts only.
- At 12,800 races (about 14-16 months), a model that has not passed is classed **FAIL FORWARD ACCURACY TEST**, qualified by the power figures above. Before then, the status is **CONTINUE FORWARD RESEARCH**.

**Stop / invalidation.**
- If the frozen artefact's hash ever differs, the confirmatory test stops and is reported. Models are never refitted or substituted.
- Failed integrity checks are reported in the status file and are not repaired by rewriting archived files.

## 7. Classification at a look
| Classification | When |
|---|---|
| PASS FORWARD ACCURACY TEST | z > boundary at a look, with valid confirmatory data |
| CONTINUE FORWARD RESEARCH | No boundary crossed and the final look is not yet reached |
| FAIL FORWARD ACCURACY TEST | No crossing by the 12,800-race look (qualified by power; not proof of zero value) |

Passing does not authorise live betting.

## 8. Exploratory candidate X1 (evening), frozen now, not confirmatory
- X1 = softmax(1.0781·log m_E + 0.2625·s_C + 0.0898·log f), fitted on 1 Mar - 12 Oct 2026 replay data (8,136 races, previously examined).
- File: models/x1_evening_2026-11-19.json, sha256 8b1c18c2…fb54cc.
- It is evaluated forward against the 21:00 market and the 09:00 market, using the R0 snapshot and the next morning's components. The 08:35 card is a decision-time approximation, and that is labelled.
- X1 is not the frozen 09:00 E and is never reported as such.

## 9. Exploratory CLV and execution rules (pre-specified; no threshold search)
**Selection:** EV ≥ 4% at the provider's Betfair Exchange back quote after 2% commission, using E at 09:00 (forward) and X1 at 21:00 (forward).

**Measures:**
- Absolute CLV = log(quote / BSP).
- Share beating BSP.
- CLV relative to odds-band-matched runners. This is reported separately and never presented as profit.
- Change in closing implied probability, by odds band and by snapshot time.

**Conditional fill scenarios:**
1. Full fill at the quote.
2. Fill at BSP.
3. Adverse fills: matched only if BSP ≥ quote.
4. Quote less a 5% haircut.

Commission is 2% and stakes are level. Depth is unknown (no Betfair key), so every return is a **conditional simulation**.
