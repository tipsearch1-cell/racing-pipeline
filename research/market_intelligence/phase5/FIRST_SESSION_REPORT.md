# First-session report (19 Nov 2026, 15:20 UTC)

**Verdict:**
- **The VPS collector is not running.** The research session cannot reach the VPS; the package is fixed and ready for McCoy.
- Connector capture and integrity are validated on today's live session.
- The first forward-test day (20 Nov) has not happened yet, so no forward prediction or settlement is claimed.

## Infrastructure
| Item | Status |
|---|---|
| Environment | Research session (cloud container, no VPS route). VPS: not reached |
| Repository commit | Phase 5 code 831c7bb; this deployment update in the commit that adds this file |
| Deployment | VPS: not deployed (blocked). Connector capture: active |
| Scheduling | 2 independent recurring tasks (evening 21:00, watchdog 10:23) + 20 Nov build + live checks (SCHEDULER_STATUS.md) |
| Collector process | No VPS process. Connector captures run inside scheduled sessions |

## Market data (today, connector)
| Item | Value |
|---|---|
| Races discovered / mapped | 33 / 33 |
| Coverage by checkpoint | SWEEP 2 (13:17, 14:00 UTC). E2100, 0900 and off-60…-01: none (not scheduled for 19 Nov / VPS not deployed) |
| Quote freshness | Newest quote 0.8 min before collection (unstarted races) |
| Missing / invalid records | 0 |

## Model predictions
| Item | Value |
|---|---|
| E and D2 hash | Verified (one artefact holds both; sha256 56179d9c…7178b52 in full in ARCHIVE_HEALTH.md) |
| Prediction timestamps / GitHub evidence / eligibility | **Pending.** First 09:00 predictions and push stamp on 20 Nov |

## Integrity
- Verification OK.
- 0 missing files, 0 duplicates, 0 timestamp violations.
- Open items are listed under next actions below.

## Production safety
- The production model, bot file, betting logic and publishing order are unchanged.
- Research steps run only after publishing.
- No production file reads research outputs.
- The only production-side activity today was the scheduled 14:00 live check: NR flags only, and a re-settle of 18 Nov now that its BSP is complete.

## Next actions
1. **McCoy:** run the commands in VPS_DEPLOYMENT_REPORT.md (`--check` first) and report the outputs.
2. **20 Nov 09:00-09:30:** first confirmatory 09:00 snapshot and E/D2 predictions; push stamp before the first off.
3. **20 Nov 10:23:** the first watchdog run confirms files and the chain.
4. **21 Nov morning:** first forward settlement and status (counts only).
5. **Optional:** Betfair API access (BETFAIR_API_STATUS.md).
