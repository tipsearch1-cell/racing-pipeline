# Phase 5 - final status (19 Nov 2026)

**Bottom line:**
- A working, auditable forward test is in place and starts tomorrow (20 Nov).
- Frozen E and D2 are verified unchanged.
- Their 09:00 predictions will be computed from a genuine 09:00 snapshot, stamped by GitHub's server before each race, and judged under a spec sealed at 13:21 UTC today.
- **The original 1,000-race test is badly under-powered** (about 9% power for E's historical gain). The sealed rule therefore extends it to at most 12,800 races (about 14 months), with group-sequential looks.
- **No forward result exists yet. None is claimed.**

Machine-readable status: out/phase5_status.json. Code: fwd.py, power.py, explore.py, freeze_x1.py, vps/. Tests: 16 Phase 5 tests (33 including the earlier Phase 3 and 4 suites), all passing.

## Done
| Area | Result |
|---|---|
| Frozen models | Hash 56179d9c…7178b52 matches the record; first pushed 13:01:02Z on 19 Nov. Reproducible, same population. Not retrained (FROZEN_MODEL_AUDIT.md) |
| Shadow pipeline | 10 requirements met. Three gaps fixed: seal-time market treated as 09:00; self-reported commit times; daily interim scoring (SHADOW_PIPELINE_AUDIT.md) |
| Market capture | Active through the Racing API connector: 21:00 evening (first run tonight), 09:00 (from tomorrow), pre-off sweeps at the live checks. Live test on 19 Nov: 33/33 races mapped, quotes 0.8 min fresh, idempotent (DATA_CAPTURE_VALIDATION.md) |
| Integrity | Write-once files, chained manifest, GitHub push stamps, model-hash checks, mapping, staleness, missing and duplicate detection. `fwd.py verify` reports all of them |
| Pre-registration | prereg/FORWARD_TEST_PHASE5_SPEC_2026-11-19.md (sha 50a1dc8e…), pushed 13:21:34Z, before any forward race |
| Power | 1,000 races: 5% / 9% / 22% power for 0.002 / 0.003 / 0.005. Needed: 27,909 / 12,404 / 4,466 races (POWER_ANALYSIS.md) |
| Monitoring | Daily status with counts only; interim outcome statistics are disabled (DAILY_MONITORING.md) |
| Exploratory (historical) | Overnight movement, evening CLV, execution scenarios (EARLY_MARKET_RESEARCH.md, CLV_FRAMEWORK.md, EXECUTION_FRAMEWORK.md). X1 evening model frozen for a forward exploratory series |

## Unresolved blockers
1. **VPS capture of exact pre-off checkpoints** (−60/−30/−15/−10/−5/−1 minutes). This environment cannot reach the VPS. The tested package and exact commands are in ARCHIVE_DEPLOYMENT.md (for McCoy). Until it runs, near-off data are the sweeps (variable lead) and BSP.
2. **Betfair Exchange depth, lay prices and volume:** no Betfair API key. All execution results remain conditional simulations.
3. **Provider timestamp time zone:** the field has no zone. It matched UTC/UK in winter; it must be re-checked when British Summer Time starts (29 Mar 2027).
4. **Scheduling is a chain:** each build schedules the next day. One failed session would stop collection until noticed. The status file shows gaps, but they cannot be back-filled.
5. **Racing API BSP gaps** on some days (for example 10-12 and 18 Nov). These affect CLV and execution diagnostics only, not the primary metric.

## Timeline (estimates; depend on racing volume and eligibility)
| Milestone | Races | Approx. date |
|---|---|---|
| First forward day | n/a | 20 Nov 2026 |
| Look 1 (original Phase 4 point; cannot pass) | 1,000 | late Dec 2026 / early Jan 2027 |
| Look 2 | 3,200 | about Mar 2027 |
| Look 3 | 6,400 | about Jun 2027 |
| Look 4 | 9,600 | about Oct 2027 |
| Final look | 12,800 | about Jan-Feb 2028 |

## Decision framework: status of the 12 questions today
| # | Question | Status today |
|---|---|---|
| 1 | Does E beat the 09:00 market forward? | **Not yet answerable** (0 forward races). Historical, previously examined data: +0.003 |
| 2 | Does D2? | Not yet answerable. Historical: +0.002 development, about 0 to +0.002 re-used |
| 3 | Statistically credible after correction? | Decided only at the sealed looks |
| 4 | Practically meaningful? | A 0.003 gain is about 0.2% of log-loss. Even if real, it is small |
| 5 | Calibration acceptable? | Reported at each look. Historically fine (slope about 1.0) |
| 6 | Limited to segments? | Reported at each look (odds band, code, field size) |
| 7 | Does the signal fade towards the off? | Historically yes (Phase 4). Forward evidence needs the VPS checkpoints or sweeps |
| 8 | Useful overnight information? | Historically: independent signals predict overnight movement (slope 0.17 development, 0.08 re-used). Not shown to be tradable (evening quotes ≈ ½ BSP) |
| 9 | Positive absolute CLV? | Historically: 09:00 E selections beat BSP (+0.05 to +0.08) via long morning quotes; selections from 21:00 and from off−60 onwards lose to BSP |
| 10 | Executable? | Not demonstrated. Every rule loses under adverse fills; depth is unknown |
| 11 | Continue market-anchored modelling? | Yes, as research: the forward test is the deciding evidence. No further model development during the test |
| 12 | Advance beyond research? | **No.** Nothing advances before the confirmatory test passes. A pass would still need a separate execution study |

Current classification for both models: **CONTINUE FORWARD RESEARCH** (no forward data yet).
