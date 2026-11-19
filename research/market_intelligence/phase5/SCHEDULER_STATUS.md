# Scheduler status (19 Nov 2026, 15:20 UTC)

**Summary:**
- The fragile single chain has been reduced.
- The evening snapshot and a daily watchdog are now **independent recurring scheduled tasks**.
- The watchdog re-creates the next day's build if the chain breaks.
- The VPS cron (exact checkpoints) is pending McCoy.

| Job | Type | When | Status |
|---|---|---|---|
| 20 Nov 08:35 build (+ research steps R1-R6, 09:00 snapshot) | One-shot, chained into this conversation | 20 Nov 08:35 UK | Enabled. Prompt now uses the template ops/DAILY_BUILD_PROMPT.md and no longer schedules the evening task |
| Live checks with sweep capture | Chained one-shots | 16:00, 18:00 UTC today; 12-18 UTC daily | Enabled (14:00 ran: sweep archived) |
| **Racing research: 21:00 evening market snapshot** | **Recurring**, fresh session | 21:00 Europe/London daily (DST-aware; the server may start it a few minutes late; the actual time is recorded) | Enabled. First run tonight. Approval: automatic |
| **Racing research: daily forward-test watchdog** | **Recurring**, fresh session | 10:23 Europe/London daily | Enabled. First run 20 Nov. Push notification on completion. Approval: automatic |
| Old chained 21:00 snapshot (tonight) | One-shot | n/a | **Disabled** to avoid a duplicate collector (deleting it was refused by a permission check, so it is kept disabled) |
| VPS collector (every minute, flock), history 22:30, push 23:45, health 23:50 | cron on the VPS | n/a | **Not deployed** (VPS_DEPLOYMENT_REPORT.md) |

## Resilience
| Failure | Effect now |
|---|---|
| Evening session fails | Next evening's task still runs (recurring). The gap is logged (evening_failures.log) and shown as missing_E |
| Build session fails, or the next build is not scheduled | The 10:23 watchdog finds no next-day build task and creates it from the template. The day's own 09:00 window cannot be recovered (by design: never back-filled) |
| 09:00 fetch fails | Retried until 09:30; then "NO VALID 09:00 SNAPSHOT" and the day is exploratory |
| VPS tick fails | failures.jsonl; retried next minute while the checkpoint is inside its ±2 min window |
| Overlap | VPS: `flock -n`. Scheduled tasks: one recurring task per job; the watchdog never creates a second build |
| Rate limits | VPS ≤ 2 requests/s with about 150-250 requests a day. Connector: one fetch per capture |
| Restart | State is the files on disk; restarts are safe and write-once prevents overwrites |

**Remaining single point:**
- Live checks and the build still chain inside this conversation.
- If this conversation's session became unusable, builds would continue only through the watchdog's re-created (fresh-session) tasks.
