# Phase 5 - daily monitoring

**What it is:** `python3 fwd.py status DAY` writes status/DAY.json and status/DAY.md. It runs every morning after the previous day is settled (build step R6).
- It reports counts and integrity only.
- It computes **no outcome statistic** (no log-loss, no returns, no significance), so collection cannot be steered by interim results.

| Field | Meaning |
|---|---|
| races_on_card / eligible_races_processed | Sealed-card races / races eligible at 09:00 |
| model_E_predictions / model_D2_predictions | Races with frozen E / D2 09:00 probabilities (always equal by construction) |
| capture_0900 | A snapshot was collected inside 09:00-09:30 UK |
| capture_evening_races | Races in the previous evening's 21:00 snapshot |
| sweep_snapshots | Pre-off sweeps archived |
| archive_verification | Hash chain and file hashes (`collector.verify`) |
| model_hash_ok | Frozen artefact and every record carry the sealed sha256 |
| timestamp_violations | Races whose 09:00 prediction was not pushed to GitHub before the off |
| mapping_errors | Card runners missing from the snapshot, or runners added after the seal |
| exclusion_reasons | Count of ledger reasons that made races exploratory |
| valid_prospective_races_to_date | Confirmatory settled races so far |
| next_look | Race count at which the next pre-registered look happens |

**Supporting commands:**
- `fwd.py verify` writes out/verify.json across all forward days: totals, unreadable files, missing E/M snapshots, duplicate snapshot races.
- Any failure is visible in the status file and reported in the build summary.

**Rules:**
- `shadow.py score` and `fwd.py analyze` are **not** run between looks.
- `fwd.py analyze --look K` refuses to compute anything until look K's race count is reached.
- Collection continues whatever happens.

The sample for 19 Nov is in status/2026-11-19.md. It was a capture test only, not a forward day, so most fields are zero.
