#!/usr/bin/env bash
# Phase 5 research market collector - VPS deployment (run by McCoy on the VPS; research only, no betting).
# Usage: bash deploy_vps.sh /path/to/racing-pipeline      (idempotent; re-run safe)
# Needs: the same protected env file that holds RACING_API_USERNAME / RACING_API_PASSWORD for McCoy's odds fetches.
# Never echoes, copies or writes the credentials.
set -euo pipefail
REPO=${1:?repo path}; ENVF=${RACING_ENV_FILE:-/root/.racing_pipeline_env}
D=$REPO/research/market_intelligence/phase5/vps
cd "$REPO" && git fetch -q origin main && git checkout -q main && git pull -q --ff-only origin main
[ -r "$ENVF" ] || { echo "BLOCKED: $ENVF not readable"; exit 2; }
[ "$(stat -c %a "$ENVF")" = "600" ] || echo "WARNING: $ENVF permissions are not 600"
( set -a; . "$ENVF"; set +a; [ -n "${RACING_API_USERNAME:-}" ] && [ -n "${RACING_API_PASSWORD:-}" ] ) || { echo "BLOCKED: credentials not in $ENVF"; exit 2; }
python3 "$D/vps_collect.py" selftest
[ -f "$D/config_vps.local.json" ] || python3 - "$D" <<'P'
import json, sys; d = sys.argv[1]; c = json.load(open(f"{d}/config_vps.json")); c["enabled"] = True
json.dump(c, open(f"{d}/config_vps.local.json", "w"), indent=1)
P
# one live tick now (prints counts only)
( set -a; . "$ENVF"; set +a; cd "$D" && python3 vps_collect.py tick --config config_vps.local.json )
# cron: every minute (flock prevents overlap); nightly push of the archive to the research-archive branch
CRON1="* * * * * flock -n /tmp/p5collect.lock bash -c 'set -a; . $ENVF; set +a; cd $D && python3 vps_collect.py tick --config config_vps.local.json' >> /var/log/p5collect.log 2>&1"
CRON2="45 23 * * * bash $D/push_archive.sh $REPO >> /var/log/p5collect.log 2>&1"
( crontab -l 2>/dev/null | grep -v 'p5collect' ; echo "$CRON1 # p5collect"; echo "$CRON2 # p5collect-push" ) | crontab -
echo "deployed: cron installed; log /var/log/p5collect.log; data $REPO/research/market_intelligence/phase3/archive/archive_data_vps"
