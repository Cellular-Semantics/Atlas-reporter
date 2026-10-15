#!/bin/bash
# Extract prose evidence units from each paper's triaged supplements.
source "$(dirname "${BASH_SOURCE[0]}")/common.sh"
cd "$REPO" || exit 1
: > "$LOGS/prose.log"; mkdir -p "$PROJECT/units"
while IFS= read -r doi; do
  slug=$(echo "$doi" | tr '/' '_')
  echo "=== $doi" >> "$LOGS/prose.log"
  uv run python -m atlas_chat.cli_supplement_prose units \
    --store "$STORE" --doi "$doi" \
    --out "$PROJECT/units/$slug.json" >> "$LOGS/prose.log" 2>&1
done < <(dois)
echo "DONE" >> "$LOGS/prose.log"
