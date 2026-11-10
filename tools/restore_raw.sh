#!/usr/bin/env bash
# Rebuild raw/ from the raw-data branch (archives + daily files pushed by the VPS). Safe to re-run every morning:
# fetches only the newest snapshot of the branch and never overwrites files already unpacked.
set -euo pipefail
ROOT=/home/claude/racing-pipeline; B=/home/claude/raw-data-branch; R=$ROOT/raw
URL=https://github.com/tipsearch1-cell/racing-pipeline
if [ -d "$B/.git" ]; then git -C "$B" fetch -q --depth 1 origin raw-data && git -C "$B" reset -q --hard FETCH_HEAD
else git clone -q --depth 1 --branch raw-data --single-branch "$URL" "$B"; fi
mkdir -p "$R"/{rbd_results,rbd_hh,raceiq,racedata,race_advisor,odds,odds_flat,rtr}
u() { unzip -qn "$1" -d "$2"; }
[ -d "$R/rbd_results/2026" ] || u "$B/rbd/RBD-results-CSV-2020-to-2026-10-09.zip" "$R/rbd_results"
for z in "$B"/rbd/*_GB_IRE_HH_HC_*.zip; do u "$z" "$R/rbd_hh"; done
for z in "$B"/raceiq/*.zip; do n=$(basename "$z" .zip); [ -d "$R/raceiq/$n" ] || u "$z" "$R/raceiq/$n"; done
[ -d "$R/racedata/files" ] || u "$B"/racedata/*racedata-all-*.zip "$R/racedata"
[ -d "$R/race_advisor/CSV" ] || u "$B"/race_advisor/*.zip "$R/race_advisor"
[ -f "$R/odds/README.txt" ] || u "$B"/odds/*odds_hist_jumps*.zip "$R/odds"
[ -f "$R/odds_flat/README.txt" ] || u "$B"/odds/*odds_history_compact*.zip "$R/odds_flat"
cp -n "$B"/research/*RatingTheRaces* "$R/rtr/" 2>/dev/null || true
# daily files pushed by the VPS: daily/raceiq/YYYY-MM-DD/..., daily/racedata/YYYY-MM-DD/...
if [ -d "$B/daily/raceiq" ]; then
  mkdir -p "$R/raceiq/daily"; cp -rn "$B"/daily/raceiq/* "$R/raceiq/daily/" 2>/dev/null || true
  find "$R/raceiq/daily" -name '*.zip' | while read -r z; do d="${z%.zip}"; [ -d "$d" ] || unzip -qn "$z" -d "$d"; done
  find "$R/raceiq/daily" -name '*.gz' ! -name '*.csv.gz' -o -name '*.csv.gz' | while read -r g; do [ -f "${g%.gz}" ] || gunzip -kf "$g"; done
fi
if [ -d "$B/daily/racedata" ]; then
  mkdir -p "$R/racedata/daily"; cp -rn "$B"/daily/racedata/* "$R/racedata/daily/" 2>/dev/null || true
  find "$R/racedata/daily" -name '*.csv.gz' | while read -r g; do [ -f "${g%.gz}" ] || gunzip -kf "$g"; done
fi
last() { ls -d "$B/daily/$1"/20* 2>/dev/null | sort | tail -1 | xargs -r basename; }
echo "raw restored. Latest daily push: RaceIQ $(last raceiq || true) | RaceData $(last racedata || true)"
