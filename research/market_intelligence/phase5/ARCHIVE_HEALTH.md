# Archive health (19 Nov 2026, 15:20 UTC)

`python3 fwd.py verify 2026-11-19` (connector archive, main branch):
```
ok: true; archive_integrity_failures: 0; frozen_model_sha256_ok: true; races: 33; eligible_0900: 0; confirmatory_settled: 0
timestamp_violations: 0; mapping_errors: 0; model_hash_discrepancies: 0; missing_E: 1; missing_M: 1; duplicate_snapshots: 0
```
19 Nov is a capture-test day, not a forward day. The missing E and M snapshots are expected, because neither was scheduled for 19 Nov.

| Check | Result |
|---|---|
| Frozen model sha256 | 56179d9cf676d7d02a2ceb4e0cb484896057a4e0a9fbf8fcb5333bcc87178b52, recomputed = record |
| Spec sha256 | 50a1dc8ee0adca943a224b14ff34f32b2e474a0fee85e7a92e073cb7f189134a, matches prereg/SHA256SUMS.txt (`sha256sum -c` OK) |
| Manifest chain | Intact (all days) |
| Missing files | None (every manifest entry present and hash-matching) |
| Duplicate records | 0 duplicate race snapshots per checkpoint |
| Timestamp violations | 0 (no forward predictions yet) |
| Tests | 33 passed (phase5 16, phase3 archive 12, phase4 5) |

**Operational health on the VPS** (`vps_collect.py health`, after deployment):
- races scheduled;
- captures per checkpoint;
- checkpoints already passed and missing;
- failed requests;
- stale snapshots (newest quote > 30 min old);
- integrity failures;
- free disk.

It reports no model performance. The daily forward-test status (`fwd.py status`) gives eligible races, E/D2 prediction counts, the 09:00 capture, timestamp violations and integrity, also with counts only.

**Alerts:** no Telegram or other channel is configured in this repository, and none was created. The watchdog's push notification to the account owner is the only alert, and it is operational only.
