---
name: local-paper-index
description: Build and query a local ASTA-shape snippet index for an atlas project's papers — the primary atlas paper plus its subatlas references (upstream studies that contributed cell types). Supports JATS XML (preprints + EuropePMC) and PDF (closed-access journals via pymupdf4llm). Installs the [local-index] extra (~500 MB of MiniLM via sentence-transformers, ~25 MB PyMuPDF).
---

# local-paper-index

A project's `local_index/` is a **corpus** of one or more papers:

- Exactly one `role: atlas` paper — the DOI in `cell_type_annotations.json.source.doi`.
- Zero or more `role: subatlas` papers — upstream studies whose cell types were folded into the atlas (sourced from `label_provenance.json` study labels).

Snippets emitted by the corpus are ASTA-shape, so `_summarize_snippets` / `validate_report` consume them unchanged.

## When to invoke

- Atlas setup: after `anndata-zarr-summary` has produced `cell_type_annotations.json` + `label_provenance.json`, run the discover → review → ingest flow to build the corpus.
- Adding a new subatlas paper: when fan-out logs a `needs_pdf` warning, download the publisher PDF and run `add --pdf …`.

## Flow

```bash
# 1. Propose subatlas papers from label_provenance.json (S2 title-match + author/year hints).
uv run python scripts/setup_local_index.py discover-subatlas --project <name>

# 2. Review projects/<name>/cell_type_annotations.json:
#    For each entry under source.subatlas_papers, copy `proposed_doi` → `doi`
#    (or replace with the correct DOI). Delete entries that aren't useful.

# 3. Run the waterfall: ASTA probe → JATS fetch → mark needs_pdf if neither.
#    Also builds the atlas paper's local index.
uv run python scripts/setup_local_index.py init-corpus --project <name>

# 4. Inspect:
uv run python scripts/setup_local_index.py list --project <name>
cat projects/<name>/subatlas_todo.md   # papers awaiting PDF, with publisher links

# 5. After downloading any needs_pdf paper:
uv run python scripts/setup_local_index.py add \
  --project <name> --doi <DOI> --pdf path/to/paper.pdf --role subatlas

# 6. Query:
uv run python scripts/setup_local_index.py search \
  --project <name> --query "ILC3 CCL1 PTGDS skin inflammation" -k 10
uv run python scripts/setup_local_index.py search \
  --project <name> --query "..." --role subatlas   # restrict to subatlas papers
```

## Output layout

```
projects/<name>/local_index/
  corpus.json                # version, atlas_doi, use_in_fanout flag, papers list
  papers/<paper_slug>/
    manifest.json            # role, source_type, hash, n_chunks, paper metadata
    source/{paper.jats.xml | paper.pdf}
    chunks/{chunks.jsonl, embeddings.npy, chunks.fulltext.txt}
    citations/{sentences.jsonl, ref_resolution.json}   # JATS papers only
    snippet_index/snippets.json
```

`paper_slug` = DOI lowercased with `/` → `_` (e.g. `10.1126_science.adf1226`), sha1 fallback for pathological DOIs.

Builds are idempotent — per-paper hash short-circuits a rebuild unless `--force` or the source changed. Adding or removing one paper never re-embeds the others.

## Integration with fan-out

**Default: local index is NOT queried during `FanOut._citation_traverse`.** Subatlas papers are surfaced as a curated corpus; fan-out relies on ASTA for citation traversal.

To opt in to parallel local-index search during fan-out, edit `corpus.json` and set `"use_in_fanout": true`. Hits from the local index are merged with ASTA results, with local taking precedence on `(corpus_id, chunk_id)` dedupe.

Even with the default (off), fan-out **does** emit a non-blocking warning row whenever the corpus has subatlas entries at `status: needs_pdf`, listing them in `traversal_output/<cell_type>/subatlas_missing.json`. Useful for spotting papers worth grabbing.

## Source-type behavior

| Source | Parser | Citation graph | Metadata |
|---|---|---|---|
| JATS XML | `_jats_parser` (vendored) | yes — `xref → ref_id → CorpusId` | bioRxiv API |
| PDF | `pymupdf4llm` via `_pdf_parser` | no (PDFs lack xref markers) | Crossref REST API |

PDF parser notes:
- Reading order at the *document* level may be shuffled across columns on multi-column layouts (Science, etc.). Each *paragraph* is internally coherent — fine for embedding-based retrieval.
- Figure-internal text (axis labels, panel tags, gene-name strips) is tagged `section: IN_FIGURE` so consumers can filter it from quoted evidence while still indexing it for recall.
- Front-matter paragraphs that near-duplicate the abstract (e.g. Science "Research Article Summary") are deduped by prefix.

## Migration from the old single-paper layout

Projects built with the previous version of this skill have `local_index/manifest.json` at the corpus root. On first read, `local_snippet_index` automatically moves the existing files under `papers/<atlas_slug>/` and synthesises `corpus.json` with that paper as `role: atlas`. One-shot, no flag needed.

## Limitations

- bioRxiv JATS ref-list quality varies; references without DOIs can't be auto-resolved to CorpusIds. Cited-paper traversal via ASTA covers the gap for indexed references.
- Image-only PDFs aren't OCR'd. If `pymupdf4llm` returns an empty markdown for a PDF, the paper falls back to `needs_pdf` (manual re-OCR + re-add).
- Heavy ML stack: pulls in `sentence-transformers` + torch + PyMuPDF. Behind the `[local-index]` optional extra to keep default installs lean.
- The vendored JATS parser is at `src/atlas_chat/atlas_chat/services/_jats_parser.py` (source: Cellular-Semantics/paperqa2_cyberian@4d5d153). Re-sync periodically by `cp` if upstream picks up additional JATS dialect support.
