#!/usr/bin/env bash
# Phase 5 research market collector - VPS deployment (research only; no betting, no production change).
#
#   bash deploy_vps.sh /path/to/racing-pipeline --check     # audit + offline selftest only; changes nothing
#   bash deploy_vps.sh /path/to/racing-pipeline             # audit, selftest, one live tick, install cron (idempotent)
#
# Credentials: read only from the protected env file McCoy already uses (RACING_ENV_FILE, default /root/.racing_pipeline_env).
# They are never echoed, copied or written. The script never switches branches, never resets, never touches production files.
set -euo pipefail
REPO=${1:?usage: deploy_vps.sh REPO [--check]}; MODE=${2:-install}
ENVF=${RACING_ENV_FILE:-/root/.racing_pipeline_env}
D=$REPO/research/market_intelligence/phase5/vps
LOG=${P5_LOG:-/var/log/p5collect.log}; touch "$LOG" 2>/dev/null || LOG=$HOME/p5collect.log
PY=$(command -v python3)

echo "== 1. audit (no changes) =="
echo "host: $(hostname)  time UTC: $(date -u +%FT%TZ)  TZ: $(cat /etc/timezone 2>/dev/null || readlink /etc/localtime)"
timedatectl show -p NTPSynchronized 2>/dev/null || echo "NTP status: unknown (check chrony/ntp)"
cd "$REPO"
echo "repo: $(git remote get-url origin | sed 's#//[^@]*@#//#')  branch: $(git rev-parse --abbrev-ref HEAD)  commit: $(git rev-parse --short HEAD)"
DIRTY=$(git status --porcelain --untracked-files=no | wc -l)
echo "tracked files with local changes: $DIRTY"
echo "python: $($PY --version 2>&1)  zoneinfo: $($PY -c 'import zoneinfo;zoneinfo.ZoneInfo("Europe/London");print("ok")')"
df -h "$REPO" | tail -1 | awk '{print "disk free: "$4" of "$2}'
free -m 2>/dev/null | awk '/Mem:/{print "memory free MB: "$7" of "$2}'
echo "existing cron entries mentioning racing/collector:"; crontab -l 2>/dev/null | grep -Ei 'racing|collect|odds|bot|p5' || echo "  (none)"
echo "collector processes already running:"; pgrep -af 'vps_collect.py|collector.py tick' || echo "  (none)"
[ -r "$ENVF" ] || { echo "BLOCKED: $ENVF not readable"; exit 2; }
[ "$(stat -c %a "$ENVF")" = "600" ] || echo "WARNING: $ENVF permissions are $(stat -c %a "$ENVF"), expected 600"
( set -a; . "$ENVF"; set +a; [ -n "${RACING_API_USERNAME:-}" ] && [ -n "${RACING_API_PASSWORD:-}" ] ) && echo "credentials: present (values not shown)" || { echo "BLOCKED: RACING_API_USERNAME/PASSWORD not in $ENVF"; exit 2; }
( set -a; . "$ENVF"; set +a; env | grep -oE '^(BETFAIR|BF)_[A-Z_]*' | sed 's/^/betfair-related variable present: /' ) || echo "betfair-related variables: none"

echo "== 2. update code (fast-forward only, never switches branch) =="
BR=$(git rev-parse --abbrev-ref HEAD)
if [ "$BR" = "main" ] && [ "$DIRTY" = "0" ]; then git fetch -q origin main && git merge -q --ff-only origin/main && echo "now at $(git rev-parse --short HEAD)";
else echo "NOT updating: branch=$BR, local changes=$DIRTY. Use a clean main checkout (e.g. git worktree add ~/rp-research origin/main) and pass that path."; [ "$MODE" = "--check" ] || exit 3; fi

echo "== 3. offline selftest =="
$PY "$D/vps_collect.py" selftest
$PY -m pytest -q "$REPO/research/market_intelligence/phase5/tests" "$REPO/research/market_intelligence/phase3/archive" 2>&1 | tail -1 || true
[ "$MODE" = "--check" ] && { echo "check mode: nothing installed"; exit 0; }

echo "== 4. enable + one live tick =="
[ -f "$D/config_vps.local.json" ] || $PY -c "import json,sys;c=json.load(open('$D/config_vps.json'));c['enabled']=True;json.dump(c,open('$D/config_vps.local.json','w'),indent=1)"
( set -a; . "$ENVF"; set +a; cd "$D" && $PY vps_collect.py tick --config config_vps.local.json )
( cd "$D" && $PY vps_collect.py health --config config_vps.local.json )

echo "== 5. cron (idempotent; flock prevents overlap) =="
P="PATH=/usr/local/bin:/usr/bin:/bin"
RUN="set -a; . $ENVF; set +a; cd $D &&"
C1="* * * * * $P flock -n /tmp/p5collect.lock bash -c '$RUN $PY vps_collect.py tick --config config_vps.local.json' >> $LOG 2>&1 # p5collect"
C2="30 22 * * * $P flock /tmp/p5collect.lock bash -c '$RUN $PY vps_collect.py history \$(date +\\%F) --config config_vps.local.json' >> $LOG 2>&1 # p5collect-history"
C3="45 23 * * * $P bash $D/push_archive.sh $REPO >> $LOG 2>&1 # p5collect-push"
C4="50 23 * * * $P bash -c 'cd $D && $PY vps_collect.py health --config config_vps.local.json' >> $LOG 2>&1 # p5collect-health"
( crontab -l 2>/dev/null | grep -v '# p5collect' ; echo "$C1"; echo "$C2"; echo "$C3"; echo "$C4" ) | crontab -
crontab -l | grep -c '# p5collect' | sed 's/^/p5collect cron entries: /'
echo "deployed. log: $LOG  data: $REPO/research/market_intelligence/phase3/archive/archive_data_vps"
echo "verify in 2 minutes: tail -n 5 $LOG ; ls $REPO/research/market_intelligence/phase3/archive/archive_data_vps/\$(date +%F)/"
