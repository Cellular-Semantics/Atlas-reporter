# Shared setup for the corpus build scripts.
#
# Everything is resolved from this file's own location, so the scripts run
# from any worktree and any working directory. The originals hardcoded a
# `pdf-text-extract` worktree that no longer exists.
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT="$(cd "$HERE/../.." && pwd)"          # projects/HCA_reproductive_atlas_v1
REPO="$(cd "$PROJECT/../.." && pwd)"          # worktree root
STORE="$PROJECT/supplements"
LOGS="$HERE/logs"
mkdir -p "$LOGS" "$STORE"

# Serial, because retrieval is the bottleneck and the CLI is serial
# (planning/supplement_corpus_findings_2026-08.md §10.6).
dois() {
  python3 -c "
import json
for r in json.load(open('$PROJECT/paper_corpus.json')): print(r['doi'])
"
}
