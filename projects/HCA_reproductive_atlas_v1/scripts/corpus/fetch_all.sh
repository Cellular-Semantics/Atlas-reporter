#!/bin/bash
# Fetch every paper's supplements into the store, one at a time.
source "$(dirname "${BASH_SOURCE[0]}")/common.sh"
cd "$REPO" || exit 1
: > "$LOGS/fetch.log"
n=0
while IFS= read -r doi; do
  n=$((n+1))
  echo "=== [$n] $doi" >> "$LOGS/fetch.log"
  uv run python -m atlas_chat.cli_supplements fetch \
      --store "$STORE" --doi "$doi" >> "$LOGS/fetch.log" 2>&1
  echo "--- exit $?" >> "$LOGS/fetch.log"
done < <(dois)
echo "DONE" >> "$LOGS/fetch.log"
