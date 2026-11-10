# raw-data branch (archives only - no code)
Large source archives behind the racing pipeline. The main branch's raw/ folder is rebuilt from these.
Restore (from /home/claude/racing-pipeline): `bash tools/restore_raw.sh`
- rbd/: RBD Flat results 2020 - 9 Oct 2026; RBD jumps daily/historical/pre-race Jan 2023 - Jun 2026
- raceiq/: RaceIQ exports Jan - 9 Nov 2026 (4 Nov missing at source)
- racedata/: RaceData exports 1 Jan - 13 Oct 2026; race_advisor/: pre-race files 19 Jul - 12 Oct
- odds/: odds history Flat + Jumps 13 Oct 2025 - 12 Oct 2026
- research/: earlier model documents and RTR sample
New batches: add files under the same folders in a new commit (never rewrite history).
