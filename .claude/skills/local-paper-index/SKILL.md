---
name: local-paper-index
description: Build and query a local ASTA-shape snippet index for a fresh preprint atlas paper not yet indexed in EuropePMC or Semantic Scholar. Use when ASTA snippet_search returns nothing for the atlas DOI and you need quoted evidence from the paper text. Installs the [local-index] extra (~500 MB of MiniLM via sentence-transformers).
---

# local-paper-index

When the atlas paper is a fresh bioRxiv preprint, ASTA `snippet_search` scoped
to the paper returns nothing. This skill builds a project-wide local index
that emits ASTA-shape snippet objects so the existing
`_summarize_snippets` / `validate_report` machinery works unchanged.

## When to invoke

- `mcp__Asta_semanticscholar__snippet_search` returns no hits for the atlas DOI.
- The project's `cell_type_annotations.json` has a recent (≤ 6 months) bioRxiv DOI.
- `atlas_chat.services.local_snippet_index.has_local_index(project_dir)` is False.

## Build

```bash
uv run python scripts/setup_local_index.py --project <name> [--doi DOI] [--force]
```

If `--doi` is omitted, the DOI is read from
`projects/<name>/cell_type_annotations.json`. Output lives under
`projects/<name>/local_index/`:

```
local_index/
  source/paper.jats.xml         # fetched via EuropePMC → curl_cffi → Playwright
  chunks/{chunks.jsonl, embeddings.npy, chunks.fulltext.txt}
  citations/{sentences.jsonl, ref_resolution.json}
  snippet_index/snippets.json   # ASTA-shape snippet objects
  manifest.json
```

Build is idempotent — a re-run short-circuits unless `--force` or the JATS
SHA256 changed.

## Query

```bash
uv run python -m atlas_chat.services.local_snippet_index search \
  --project projects/<name> --query "ILC3 CCL1 PTGDS skin inflammation" -k 10
```

Returns JSON of ASTA-shape dicts (`snippet`, `paper_id`, `title`, `authors`,
`year`, `corpus_id`, `score`, `annotations.refMentions`).

## Integration

Once built, the report graph picks the local index up automatically via
`FanOut._citation_traverse` — runs in parallel with ASTA and merges results.
No flag or env var needed; existence of `manifest.json` is the gate.

## Limitations

- bioRxiv JATS ref-list quality varies; many references lack DOIs and are
  therefore unresolvable to CorpusIds. Cited-paper traversal via ASTA covers
  the gap for indexed references.
- Image-based supplementary PDFs aren't OCR'd; supplementary text only enters
  the index if the JATS includes structured tables.
- Heavy ML stack: pulls in `sentence-transformers` + torch. Behind the
  `[local-index]` optional extra to keep default installs lean.
- The JATS parser is vendored at `src/atlas_chat/atlas_chat/services/_jats_parser.py`
  (source: Cellular-Semantics/paperqa2_cyberian@4d5d153). Re-sync periodically
  by `cp` if upstream picks up additional JATS dialect support.
