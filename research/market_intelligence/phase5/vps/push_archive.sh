#!/usr/bin/env bash
# Push the VPS-captured archive to the research-archive branch (separate from main, so the VPS never edits main's manifests).
set -euo pipefail
REPO=${1:?repo path}; SRC=$REPO/research/market_intelligence/phase3/archive/archive_data_vps; W=/root/research-archive-wt
[ -d "$SRC" ] || { echo "nothing captured yet"; exit 0; }
if [ ! -d "$W/.git" ]; then
  git clone -q --depth 1 --branch research-archive "$(git -C "$REPO" remote get-url origin)" "$W" 2>/dev/null || {
    git clone -q --depth 1 "$(git -C "$REPO" remote get-url origin)" "$W"; git -C "$W" checkout -q --orphan research-archive; git -C "$W" rm -rqf . ; }
fi
cd "$W" && git pull -q --ff-only origin research-archive 2>/dev/null || true
mkdir -p archive_data_vps && cp -rn "$SRC"/. archive_data_vps/     # -n: never overwrite an already-pushed file
python3 "$REPO/research/market_intelligence/phase3/archive/collector.py" verify --config <(python3 -c "import json;print(json.dumps({'out_dir':'$W/archive_data_vps','enabled':False}))") || { echo "VERIFY FAILED - not pushing"; exit 1; }
git add -A archive_data_vps && git commit -qm "VPS market archive $(date -u +%F)" && git push -q origin research-archive || echo "nothing new"
