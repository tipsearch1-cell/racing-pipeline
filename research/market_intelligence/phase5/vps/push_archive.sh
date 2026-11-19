#!/usr/bin/env bash
# Nightly: push the VPS-captured archive to the research-archive branch (separate from main, so the VPS never edits main).
# Data files are copied only if absent (never overwritten). A manifest.jsonl is replaced only when the pushed copy is an exact
# prefix of the new one (append-only); anything else stops the push. The copy is hash-verified before pushing.
set -euo pipefail
REPO=${1:?repo path}; SRC=$REPO/research/market_intelligence/phase3/archive/archive_data_vps; W=${P5_ARCHIVE_WT:-$HOME/research-archive-wt}
[ -d "$SRC" ] || { echo "nothing captured yet"; exit 0; }
URL=$(git -C "$REPO" remote get-url origin)
if [ ! -d "$W/.git" ]; then
  git clone -q --depth 1 --branch research-archive "$URL" "$W" 2>/dev/null || {
    git clone -q --depth 1 "$URL" "$W"; git -C "$W" checkout -q --orphan research-archive; git -C "$W" rm -rqf . >/dev/null 2>&1 || true; }
fi
cd "$W"; git pull -q --ff-only origin research-archive 2>/dev/null || true
python3 - "$SRC" "$W/archive_data_vps" <<'P'
import os, shutil, sys
src, dst = sys.argv[1], sys.argv[2]
for root, _, files in os.walk(src):
    for f in files:
        if f.endswith(".tmp") or f == "schedule_cache.json":
            continue
        s = os.path.join(root, f); d = os.path.join(dst, os.path.relpath(s, src))
        os.makedirs(os.path.dirname(d), exist_ok=True)
        if f in ("manifest.jsonl", "failures.jsonl"):
            if os.path.exists(d) and not open(s, "rb").read().startswith(open(d, "rb").read()):
                sys.exit(f"STOP: {d} is not a prefix of the VPS copy (append-only violated)")
            shutil.copyfile(s, d)
        elif not os.path.exists(d):
            shutil.copyfile(s, d)
P
CFG=$(mktemp); echo "{\"out_dir\": \"$W/archive_data_vps\", \"enabled\": false}" > "$CFG"
python3 "$REPO/research/market_intelligence/phase3/archive/collector.py" verify --config "$CFG" || { echo "VERIFY FAILED - not pushing"; rm -f "$CFG"; exit 1; }
rm -f "$CFG"
git add -A archive_data_vps
git diff --cached --quiet && echo "nothing new" || { git commit -qm "VPS market archive $(date -u +%F)"; git push -q origin research-archive; echo "pushed $(git rev-parse --short HEAD)"; }
