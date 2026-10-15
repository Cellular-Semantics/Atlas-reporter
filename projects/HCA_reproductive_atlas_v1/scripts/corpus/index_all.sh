#!/bin/bash
# Unpack archives and triage each paper's fetched files.
source "$(dirname "${BASH_SOURCE[0]}")/common.sh"
cd "$REPO" || exit 1
: > "$LOGS/index.log"
while IFS= read -r doi; do
  echo "=== $doi" >> "$LOGS/index.log"
  uv run python -m atlas_chat.cli_supplements unpack --store "$STORE" --doi "$doi" >> "$LOGS/index.log" 2>&1
  uv run python -m atlas_chat.cli_supplements triage --store "$STORE" --doi "$doi" >> "$LOGS/index.log" 2>&1
done < <(dois)
echo "DONE" >> "$LOGS/index.log"
