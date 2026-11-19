# Live capture validation (status 19 Nov 2026, 15:20 UTC)

**Summary:**
- Live capture through the Racing API connector is validated on real races today: 2 sweeps, 33/33 races mapped, quotes under a minute old.
- The VPS checkpoint capture is **not yet validated**, because it is not deployed.
- The first forward-test items (21:00 evening snapshot, 09:00 snapshot, frozen E/D2 predictions, push stamps) are **pending**. They first occur tonight and tomorrow (20 Nov).

| # | Requirement | Status | Evidence |
|---|---|---|---|
| 1 | Race cards retrieved | Done (connector) | Snapshots SWEEP/20261119T131756Z and T140055Z: 33 races each |
| 2 | Runners mapped | Done | 33/33 races; every sealed runner present; 0 mapping errors (`fwd.py verify 2026-11-19`) |
| 3 | Market snapshots collected | Partly done | 2 pre-off sweeps today. 21:00 evening: first run tonight. 09:00: first run tomorrow. VPS pre-off checkpoints: not deployed |
| 4-5 | Model E / D2 predictions generated | Pending (20 Nov 09:00-09:30) | Pipeline tested: an 18 Nov dry run reproduces the Phase 4 frozen predictions to 5e-7 |
| 6 | Files timestamped | Done | collected_utc, provider per-quote time, manifest captured_at |
| 7 | Predictions committed before race start | Pending (20 Nov) | Mechanism tested: GitHub server push stamp; races pushed after their off are excluded (test_ledger_timing) |
| 8 | Archive checksums valid | Done | `fwd.py verify`: archive_integrity_failures 0, frozen hash OK |
| 9 | Duplicate collection prevented | Done | Re-ingesting the same response archives nothing; the VPS repeat tick writes nothing (selftest) |
| 10 | Collection failures logged | Done (tests) | failures.jsonl on VPS ticks; connector failures logged by the scheduled tasks; no 09:00 snapshot means a "NO VALID 09:00 SNAPSHOT" record |
| 11 | Results and BSP after settlement | Done for 18 Nov; 20 Nov pending | 18 Nov re-fetched at 14:00: BSP now present for 325/325 runners. Forward days settle via `fwd.py settle` next morning |
| 12 | Archive verification succeeds | Done | verify ok=true (19 Nov) |

## Timestamps and daylight saving
**The provider's `updated` field is UK local time with no zone.**
- Evidence from a British Summer Time sample (raw/odds/sample_record.json, 13 Oct 2025): `updated` 14:11:07 sits beside a price history whose latest change is 14:12:00+01:00. If `updated` were UTC, it would be an hour after the last change.
- In winter, UK time equals UTC. Today's quotes were 0.8 min old at collection.

**Conversion:** fwd.py and vps_collect.py both read `updated` as Europe/London and convert it to UTC (DST-aware). Tests cover both BST and GMT. All capture times are stored in UTC.
