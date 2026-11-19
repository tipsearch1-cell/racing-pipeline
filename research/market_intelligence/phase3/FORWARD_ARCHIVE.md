# Phase 3 - forward market-intelligence archive

**Status:**
- **Implemented, tested and disabled by default** for market snapshots.
- **Running** for prediction archiving: 10-19 Nov 2026 are archived, all category A with commit timestamps.
- **No historical market snapshots are claimed.** Market capture starts only when the archive is enabled.

Code: research/market_intelligence/phase3/archive/
- collector.py;
- config.json (`"enabled": false`);
- test_collector.py (8 tests, all fixture-based, no network);
- fixtures/.

## What it collects
**Predictions** (`collector.py predictions DAY`), from the daily build's own files, read-only. Per runner:
- race ID, runner ID;
- model version (git commit of models/win_model.json) and training cutoff ("history to 2026-11-09");
- prediction timestamp = the first git commit of store/DAY/model.json;
- our model's chance;
- calibrated chance;
- 09:00 market chance;
- blended chance (Phase 3 parameters).

**Market snapshots** (`collector.py tick`, once a minute):
- **Checkpoints:** 09:00 UK, and 60 / 30 / 15 / 5 / 1 minutes before each race's scheduled off.
- **Per race:** the capture time, scheduled off, and every runner's prices exactly as the Racing API delivers them (every bookmaker, Betfair Exchange, Matchbook, Smarkets, with each-way terms and last-update time).

**Results** (`collector.py settle DAY results.json`): positions, BSP, SP and non-runners.

## Design properties
| Property | How |
|---|---|
| Incremental, idempotent | A file is written only if absent. Re-running a tick writes nothing new. |
| Resumable | State = files on disk. After a crash the next tick fills only the missing checkpoint files, if still inside the window (tested). |
| Timestamped, auditable | Every file carries captured_at_utc. manifest.jsonl records sha256 and size. `collector.py verify` re-hashes everything (tamper test included). |
| Storage-efficient | One gzip per race per checkpoint (deterministic bytes). About 2-4 MB a day for 6 checkpoints × about 40 races. |
| API-efficient | One paged /racecards/standard request (1-2 calls) per tick when something is due. No per-runner calls. Rate limit setting 2/s (the provider allows 5/s). |
| Safe for production | Only reads store/, models/ and the git log. Writes only to its own archive_data/. Never imports the bot or changes any pipeline file. |
| Credentials | Only from RACING_API_USERNAME / RACING_API_PASSWORD in the environment. Never printed, logged or written (tested). |

## Blockers (exact)
1. **This workspace cannot reach api.theracingapi.com from the shell.** Its network allowlist blocks it, and the Racing API is only reachable here through the chat connector. Market snapshots must run on the VPS (McCoy), which already has REST access and the credentials in protected environment variables.
2. **Order-book data (back/lay, spread, depth, traded volume, suspensions) needs the Betfair Exchange API.** That means a Betfair account, an application key and a login certificate, none of which exist in this project. The Racing API gives one exchange price per runner, with no volume.
3. **Historic 30/15/5-minute prices could be rebuilt exactly, but not here.** The provider's full price-change histories (per bookmaker, timestamped) are on the VPS: raw/runner_spool and raw/odds/<day>.jsonl.gz per the odds archive README. They are not in this repo.

## How to activate (VPS)
1. `git pull` the racing-pipeline repo on the VPS.
2. Edit research/market_intelligence/phase3/archive/config.json: set `"enabled": true` (and optionally `out_dir`).
3. Add a cron line (UK time zone):
   `* 8-21 * * * cd <repo>/research/market_intelligence/phase3/archive && python3 collector.py tick >> tick.log 2>&1`
4. After racing: `python3 collector.py predictions <DAY>` and `python3 collector.py settle <DAY> <results.json>` (the API results JSON McCoy already fetches).
5. Push archive_data/ daily to the raw-data branch, like the RaceIQ/RaceData pushes. Run `python3 collector.py verify` before each push.
6. Optional, high value: push the existing raw/runner_spool price histories so the replay can be given exact 30/15/5-minute checkpoints.

A 30-day dry run with `enabled: true` is recommended before any analysis. The archive is research data only and must never feed the live bot.
