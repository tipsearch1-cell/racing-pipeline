# VPS deployment report (19 Nov 2026, 15:20 UTC)

**Status: NOT DEPLOYED. Blocked.**
- This brief is written for McCoy, but it was run in the research session, which has no route to the VPS: `ssh` is not installed, there are no keys or host, and the shell's outbound allowlist refuses api.theracingapi.com.
- Nothing has been run on the VPS, and nothing here claims it has.
- What *was* done: the package McCoy will run was reviewed line by line. Five defects were fixed, and the fixes were tested offline. The commands below are ready to run.

## Package review (before anyone runs it)
| # | Finding | Risk | Fix (tested) |
|---|---|---|---|
| 1 | The collector tick (Phase 3 `collector.tick`) fetched the **full GB+IRE racecards every minute** (about 1,440 requests a day, about 1.8 MB each) | API load on the shared production account; possible rate limiting of production fetches | New `vps_collect.tick`: a schedule cache refreshed every 30 min, and a fetch only when a checkpoint is due. Selftest: **11 requests over 76 one-minute ticks** (6 checkpoints) instead of 76 |
| 2 | `deploy_vps.sh` ran `git checkout main && git pull` in McCoy's working repo | Could switch McCoy's branch or disturb local work | No checkout. It updates only on a clean `main` with `--ff-only`, and otherwise stops and suggests a separate worktree |
| 3 | No pre-deployment audit | Duplicate collectors, wrong repo or clock problems would go unnoticed | `--check` mode: host, UTC time, NTP, repo/branch/commit, local changes, Python + zoneinfo, disk, memory, existing racing cron entries, running collectors, credential presence (never values), Betfair variable names. Changes nothing |
| 4 | Cron lines had no PATH and logged to /var/log without a fallback | Silent cron failure for a non-root user | Explicit PATH and an absolute python3 path; the log falls back to ~/p5collect.log |
| 5 | `push_archive.sh` copied with `cp -n`, so a manifest that grows during the day could never update; it also failed on the first run (empty orphan branch) | Pushed archive would fail verification; first push would break | Data files copy only if absent; a manifest is replaced only if the pushed copy is an exact prefix (append-only), otherwise it stops; verified before push. Tested end-to-end against a local bare origin: first and repeat runs OK |

**Also added:**
- `history DAY`: per-runner provider price histories after racing, archived raw, so any checkpoint can be **reconstructed** (labelled as such, never mixed with live captures) if the VPS misses one.
- `health`: operational status (see ARCHIVE_HEALTH.md).

## Collector configuration (config_vps.json; enabled=false in git)
| Setting | Value |
|---|---|
| Endpoint | /racecards/standard, gb,ire, pages of 50, ≤ 2 requests/s |
| Checkpoints | E2100 (21:00 UK the evening before), 0900, off-60/-30/-15/-10/-05/-01 min; tolerance ±2 min |
| Output | research/market_intelligence/phase3/archive/archive_data_vps/<day>/market/<label>/<race_id>.json.gz (write-once, chained manifest), failures.jsonl, schedule_cache.json |
| Credentials | Environment only (RACING_API_USERNAME/PASSWORD from McCoy's protected env file); never written or logged |
| Schedule | cron every minute with `flock -n` (no overlap); history 22:30; nightly push 23:45 to the `research-archive` branch; health 23:50 |
| Times | VPS clock in UTC. Provider times are UK local and converted to UTC with Europe/London (DST-aware; see LIVE_CAPTURE_VALIDATION.md) |

## Exact commands for McCoy
```
cd ~/racing-pipeline && git status --short && git rev-parse --abbrev-ref HEAD      # must be clean main; otherwise use a worktree:
#   git worktree add ~/rp-research origin/main && REPO=~/rp-research
RACING_ENV_FILE=<your protected Racing API env file> bash research/market_intelligence/phase5/vps/deploy_vps.sh ~/racing-pipeline --check
# read the audit; if it shows no conflicting collector and no BLOCKED line:
RACING_ENV_FILE=<same file> bash research/market_intelligence/phase5/vps/deploy_vps.sh ~/racing-pipeline
sleep 180; tail -n 10 /var/log/p5collect.log; crontab -l | grep p5collect
python3 research/market_intelligence/phase5/vps/vps_collect.py health --config research/market_intelligence/phase5/vps/config_vps.local.json
```
**Report back:**
- the `--check` audit output;
- the log tail;
- the cron lines;
- the health JSON;
- after 23:45, the `research-archive` commit id.

No credentials or other secrets go in the report.
