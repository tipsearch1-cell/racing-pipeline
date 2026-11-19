# Phase 5 - data capture validation

**Live test: 19 Nov 2026, 13:17:56 UTC**, one connector fetch of the whole GB+IRE card.
- Archived to archive_data/2026-11-19/phase5/snapshots/SWEEP/20261119T131756Z.json.gz (76 KB).
- 19 Nov is not a forward-test day; this was a capture test.

## Results
| Check | Result |
|---|---|
| Races returned / mapped to the sealed card | 33 / 33. Every sealed runner id is present (0 mapping errors) |
| Non-runners since the seal | 18 runners show number "NR". Recorded as `non_runner`; dropped and flagged at 09:00 |
| Quotes | Median 28 per runner: 9,215 bookmaker and 1,099 exchange (Betfair Exchange, Matchbook, Smarkets back prices) |
| Price types | Stored separately: `bookmaker` and `exchange_back`. BSP is stored only from results (`results.json.gz`), never mixed with quotes |
| Each-way terms | Present per quote (ew_places, ew_denom) |
| Market id | The provider has none, so race_id is the key and `market_id` is null |
| Market status | Only `race_status` (declared/result) and `is_abandoned`. No open/suspended/in-play state. Warwick 13:02 still showed "declared" 16 minutes after its scheduled off |
| Provider timestamps | Unstarted races: newest quote 0.8 min before collection (quotes refresh about every minute). Finished races: quotes freeze at about the off, so "staleness" = time since the off. The 30-minute staleness rule therefore also rejects races already run |
| Timestamp format | The provider's `updated` field has no time zone ("2026-11-19 13:08:05"). It matched UTC = UK time to the minute today. **In British Summer Time it must be re-checked** before staleness checks rely on it (flagged in FINAL_STATUS) |
| Collection timestamp | The time the connector's saved-response file was written (within seconds of the call), stored as `collected_utc` with its source |
| Repeated collection | Re-ingesting the same response archives nothing ("identical snapshot already archived") |
| Recovery | Connector errors are retried by the session until 09:30. On the VPS, failures go to failures.jsonl and are retried next tick (selftest) |
| Integrity | `fwd.py verify` OK: chained manifest intact, frozen hash OK |
| Interference with production | One request per capture (3-6 a day). Captures run after publishing, and in separate sessions at 21:00 and at the live checks |

## Schemas
**Market snapshot** (`phase5/snapshots/{E|M|SWEEP}/<UTC>.json.gz`; sample in out/sample_snapshot_record.json):
- Top level: `day, kind="market_snapshot", checkpoint, collected_utc, collection_time_source, source, source_files_sha256, price_types`.
- `races[]`: `race_id, market_id(null), course, off_dt, race_status, is_abandoned, runners[]`.
- `runners[]`: `horse_id, horse, number, non_runner, quotes[]`.
- `quotes[]`: `bookmaker, price_type, decimal, fractional, ew_places, ew_denom, provider_updated`.

**Components** (`phase5/components.json.gz`):
- Top level: `frozen_model_sha256, E_weights, training_cutoff, history_max_date_used, sealed_card_fetched_utc, sealed_card_sha256, production_model_file_sha256, races{off_dt, n_card, type, course}`.
- `rows[]`: `race_id, horse_id, g_D2, sC, f, m_seal`.

**09:00 predictions** (`phase5/pred_0900.json.gz`; dry-run sample in out/sample_pred_0900_DRYRUN.json):
- Top level: `status, frozen_model_sha256, components_sha256, snapshot_file, snapshot_sha256, snapshot_collected_utc`.
- `races[]`: `race_id, eligible, reason, flags`.
- `rows[]`: `race_id, horse_id, m_0900, p_existing, p_D2, p_E`.

**Push stamp** (`phase5/stamps/<head>.json.gz`): `head, github_push_utc, files_at_head{name: sha256}, recorded_utc`.

**Results** (`results.json.gz`, Phase 3 format): per runner `horse_id, position, bsp, sp_dec`, plus the race's `non_runners`.

## Tests (16 in phase5/tests, plus the 12 + 5 earlier)
- Idempotent ingest and price types.
- The 09:00 window, including BST.
- The prediction formula.
- Non-runner drop and renormalisation.
- Runner added after seal; mapping error; stale quotes; race missing.
- No valid snapshot.
- Ledger timing (no stamp; pushed after the off) and confirmatory path.
- Hash mismatch and tamper detection.
- Analysis refuses before a look; paired statistic under the null.
- VPS collector selftest.

Run: `python3 -m pytest -q research/market_intelligence/phase5/tests research/market_intelligence/phase3/archive research/model_reconstruction/phase4` (33 pass).
