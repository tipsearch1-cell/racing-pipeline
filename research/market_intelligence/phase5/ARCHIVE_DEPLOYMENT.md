# Phase 5 - archive deployment

**Status:**
- **Active from tonight:** capture of the 21:00 (evening), 09:00 and pre-off sweep markets through the Racing API connector, in the scheduled daily session.
- **Not active (blocked here):** fixed pre-off checkpoints at -60/-30/-15/-10/-5/-1 minutes. These need the VPS, and this environment cannot reach it. A tested deployment package for McCoy is below.
- **Still blocked:** exchange depth, lay prices and traded volume (no Betfair Exchange API key; the Racing API supplies none).

## Access found (19 Nov, 13:15 UTC)
| Route | Result |
|---|---|
| VPS (SSH / any host access) | **None.** No keys, no host, and no VPS env file in this environment |
| Racing API from the shell | **Blocked.** The outbound allowlist refuses api.theracingapi.com (HTTP 000) |
| Credentials in env (RACING_API_USERNAME/PASSWORD, any Betfair key) | Not set here. Checked by presence only; no values read or printed |
| Racing API connector (account plan: Standard) | **Works.** `get_racecards_standard` for today and tomorrow, with every bookmaker and exchange quote and the provider's update time. Large responses are saved by the connector to a file, which `fwd.py ingest` archives |
| GitHub (git + gh) | Works, including the repository activity API used for server-side push times |

## What runs where
| Checkpoint | Where | When | Command |
|---|---|---|---|
| 21:00 the evening before (E) | Scheduled session (send_later chain) | 21:00 UK daily; first run tonight for 20 Nov | connector fetch (day=tomorrow), then `fwd.py ingest E` |
| 09:00 (M), confirmatory | Daily build session, after publishing | 09:00-09:30 UK | connector fetch, then `fwd.py ingest M`, `predict0900`, `stamp` |
| Pre-off sweeps (SWEEP) | Live-check sessions | 12/14/16/18 UTC | `fwd.py ingest SWEEP` (lead time varies by race; exploratory) |
| BSP + results | Daily build settle | Next morning | `fwd.py settle` (API BSP, gaps flagged) |
| Off-60/-30/-15/-10/-5/-1 and 21:00/09:00 at exact times | **VPS: not deployed** | every minute (cron) | `vps/vps_collect.py tick` |

## McCoy deployment package (research/market_intelligence/phase5/vps/)
| File | Purpose |
|---|---|
| vps_collect.py | The Phase 3 collector with the Phase 5 checkpoint set, disabled by default. `selftest` runs offline: all 6 pre-off checkpoints, the evening snapshot, an idempotent repeat, a logged outage and manifest verification |
| config_vps.json | Template (enabled=false). It writes to archive_data_vps/, so the VPS never edits the main branch's manifests |
| deploy_vps.sh | Idempotent installer. It checks that the env file is readable and chmod 600, and that the credentials are present (never echoed). It runs the selftest, one live tick, then installs the cron entries (every minute with flock; nightly push) |
| push_archive.sh | Nightly. Verifies the VPS archive (hash chain), then pushes it to a separate `research-archive` branch. `cp -n` never overwrites a pushed file |

**Exact commands for McCoy (on the VPS, as the user that runs the odds fetches):**
```
cd ~/racing-pipeline && git pull --ff-only origin main
RACING_ENV_FILE=<the protected env file McCoy already uses for the Racing API> bash research/market_intelligence/phase5/vps/deploy_vps.sh ~/racing-pipeline
tail -n 20 /var/log/p5collect.log          # expect "N races fetched, M snapshot files written" lines, no BLOCKED
```

**Also requested from McCoy (would remove the need to reconstruct checkpoints):**
- If the VPS still keeps the provider's per-bookmaker price-change histories (raw/odds/<day>.jsonl.gz, raw/runner_spool per the archive README), push them daily to the raw-data branch under daily/odds_hist/<day>/.
- With them, every checkpoint (including -30/-15/-5) can be rebuilt exactly from timestamped quotes.

**Prompt for McCoy (copy as is):**
> Research-only deployment, no betting change: on the VPS run `cd ~/racing-pipeline && git pull --ff-only origin main` then `RACING_ENV_FILE=<your Racing API env file> bash research/market_intelligence/phase5/vps/deploy_vps.sh ~/racing-pipeline`. Do not print the env file. Reply with the last 20 lines of /var/log/p5collect.log and the output of `crontab -l | grep p5collect`. If the VPS still stores raw/odds/<day>.jsonl.gz price histories, please also push the last 30 days and then each new day to the raw-data branch under daily/odds_hist/<day>/.

## Betfair Exchange data
- **Still a blocker.** There is no Betfair API key (app key + session).
- The Racing API supplies one "Betfair Exchange" back price per runner (plus Matchbook and Smarkets). It gives no lay side, no depth, no traded volume and no market status.
- These fields are recorded as unavailable and never inferred.
- BSP comes from Racing API results. On some days it is blank (for example 10-12 and 18 Nov), and those gaps are flagged, not filled.
