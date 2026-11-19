# Phase 5 - daily shadow pipeline audit

The research steps run in the scheduled daily-build session, after the bot file is published. Production code (pipeline/) never reads research/ or the archive: a search found no reference.

Three gaps were found in the Phase 4 arrangement and fixed:
1. The seal-time market was labelled as 09:00.
2. Provenance relied on self-reported commit times.
3. A daily score command printed interim outcomes.

## The ten requirements
| # | Requirement | Phase 4 state | Phase 5 state | Test |
|---|---|---|---|---|
| 1 | Production published normally | Research steps after the bot file; skipped if they would delay it | Unchanged. The 09:00 wait happens after publishing (the bot matches around 09:30 from the already-published file) | Build prompt order |
| 2 | Research predictions generated separately | Separate archive file | Separate files under archive_data/DAY/phase5/ | n/a |
| 3 | E/D2 cannot influence the bot | No production file reads research outputs | Same | grep of pipeline/ |
| 4 | Model version recorded | Frozen sha in the shadow file | Frozen sha in components and in pred_0900, checked against the constant | test_hash_mismatch_detected |
| 5 | Generation timestamp | created_utc | created_utc, snapshot collected_utc, provider quote times, plus a GitHub server-side push stamp | test_ledger_* |
| 6 | Committed before the race | **Gap:** the git commit time is set by the committer | `fwd.py stamp` records GitHub's server push time (activity API) with the file hashes. The ledger marks every race whose prediction was pushed after its off (or never stamped) as not confirmatory | test_ledger_timing |
| 7 | Write-once | write_once refuses an existing path | Same; a re-run computes but cannot overwrite | test_predict_matches_formula |
| 8 | No silent modification | Chained manifest + verify | Same, plus stamps hold file hashes at push time. Rewriting files and manifest together would also need a force-push, which shows in the GitHub activity log | test_tamper_detected |
| 9 | Failures logged | **Gap:** shadow.py logged nothing on failure | Missing components or prediction, no valid 09:00 snapshot, stale quotes and mapping errors are written into the record or the ledger with reasons, and shown in the status file | test_ineligible_reasons, test_no_valid_snapshot |
| 10 | Recovery never alters sealed data | Write-once | Same. A failed 09:00 fetch may be retried until 09:30; after that the day is recorded as exploratory and never rewritten | test_no_valid_snapshot |

## Timing (the brief's "important timing check")
- The 08:35 build fetches and seals the card at about 08:36 UK. The Phase 4 shadow output therefore uses a pre-09:00 market and is **not** a valid 09:00 prediction.
- Phase 5 keeps it as the **early (seal-time) exploratory series**, with its own timestamps.
- The confirmatory predictions are computed from:
  - market-independent components fixed after publishing (`fwd.py components`), and
  - a 09:00-09:30 UK snapshot (`fwd.py ingest M`, then `fwd.py predict0900`).
- Both timestamps are kept, and the production publishing sequence is unchanged.

## Interim peeking removed
The Phase 4 daily step R3 (`shadow.py score`) printed the running mean gain every day. It was removed from the scheduled build. The daily status now carries counts only (DAILY_MONITORING.md).

## Scheduled steps now in force
- **20 Nov build:** R1-R6 as in the spec.
- **Live checks** (14/16/18 UTC today; 12-18 UTC daily from tomorrow): sweep capture added.
- **Evening:** a 21:00 UK snapshot each evening, starting tonight.
- **Chaining:** each build schedules the next day's checks, the evening snapshot and the next build.
