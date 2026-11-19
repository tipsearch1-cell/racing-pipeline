# Phase 4 - forward archive: validation and deployment status

**Code:**
- research/market_intelligence/phase3/archive/: collector.py, config.json (`"enabled": false`), test_collector.py;
- this phase's shadow.py writes into the same archive.

## Validation (12 automated tests, all passing; fixtures only, no network)
| Requirement | How it is met | Test |
|---|---|---|
| 1. Implementation sound | Paged single-endpoint fetch; checkpoints 09:00 and off-60/30/15/5/1 minutes | `test_morning_snapshot_written_once`, `test_pre_off_checkpoints`, `test_paging` |
| 2. Prediction timestamp and model version | `predictions` records the git commit of models/win_model.json, its training cutoff ("history to 2026-11-09"), and the **first** git commit time of store/DAY/model.json. Archived for 10-19 Nov: all category A, committed 08:36-08:42 UTC (10 Nov: 10:21 UTC), before the first off. | `test_predictions_archive_real_day` |
| 3. No silent alteration | Files are written once and never overwritten. sha256 per file in manifest.jsonl. **Each manifest line now carries the hash of the previous line**, so editing or deleting a line breaks the chain. `collector.py verify` re-hashes everything. Daily git commits add an external timestamp. | `test_verify_detects_tampering`, `test_manifest_chain_detects_deleted_line` |
| 4. Accurate collection timestamp | Every snapshot carries captured_at_utc (time of the API response), the off time used, and the runner count | `test_morning_snapshot_written_once` |
| 5. Failures logged and recoverable | A fetch error is appended to <day>/failures.jsonl (error class and message, never credentials) and returns -1. The next tick retries anything still due, because state = files on disk. | `test_fetch_failure_logged_and_recovered`, `test_resumable_after_partial_failure` |
| 6. Efficient and idempotent | 1-2 API calls per tick, only when something is due. A re-run writes nothing. | `test_morning_snapshot_written_once` |
| 7. Postponed races, non-runners | Checkpoints are recomputed from the race's **current** off time on every tick. A postponed race gets its pre-off snapshots at the new time, never after the off. Runner lists are stored exactly as delivered, so a withdrawn non-runner simply disappears from later snapshots and earlier ones are never rewritten. | `test_postponed_race_uses_current_off_time`, `test_non_runner_removed_between_snapshots` |
| 8. No interference with production | Reads only store/, models/ and the git log. Writes only to its own archive_data/. Imports no bot or pipeline module except read-only helpers. Disabled by default. | `test_disabled_by_default_and_does_nothing`, `test_credentials_never_exposed` |

`python3 collector.py verify` on the current archive: **OK**.

## What the archive will and will not contain
| Item | Status |
|---|---|
| Model probabilities, calibrated and blended | Yes: `predictions` (10-19 Nov archived) |
| Phase 4 shadow probabilities (D2, E) | Yes, from 20 Nov (`shadow.py predict`) |
| Market-implied probabilities, every bookmaker and exchange price, each-way terms | Yes, once market capture is enabled |
| Race/runner IDs, timestamps, BSP, finishing position | Yes (`settle`) |
| **Best back/lay, depth, traded volume** | **No.** The Racing API does not supply them. This needs the Betfair Exchange API (account + app key + certificate). Not claimed. |

## Deployment status: market capture NOT yet running (blocked here)
- **Blocker 1:** this workspace's shell cannot reach api.theracingapi.com (network allowlist). The connector works only through chat tool calls, not cron.
- **Blocker 2:** there is no direct access from this session to the VPS. Only McCoy can run commands there.

**No credentials were used, printed or stored.**

**Exact deployment (for McCoy, on the VPS, in the racing-pipeline checkout that already has RACING_API_USERNAME / RACING_API_PASSWORD in its protected environment):**
```
cd ~/racing-pipeline && git pull
cd research/market_intelligence/phase3/archive
python3 -m pytest -q .                                   # expect 12 passed
python3 - <<'PY'
import json; p='config.json'; c=json.load(open(p)); c['enabled']=True; json.dump(c, open(p,'w'), indent=2)
PY
( crontab -l; echo 'CRON_TZ=Europe/London'; echo '* 8-21 * * * cd ~/racing-pipeline/research/market_intelligence/phase3/archive && <load the same protected env McCoy uses for the odds fetches> && python3 collector.py tick >> tick.log 2>&1' ) | crontab -
# daily after racing (append to the existing daily push job):
#   python3 collector.py verify && git add archive_data && git commit -m "market archive <DAY>" && git push   (to the raw-data branch, like RaceIQ/RaceData)
```
Do not commit the `enabled: true` change to main. It is a VPS-local setting.

**Optional, high value:** push the existing raw/runner_spool price histories. They would let the replay be rebuilt with exact 30/15/5-minute checkpoints.
