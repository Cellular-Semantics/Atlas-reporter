# [schema] Agentic workflow has no item-level contract for `all_summaries.json`, so #12's provenance tags are never emitted

Follow-up to #12 (evidence source tagging: `source_paper.role` + `retrieval_method`).

Scope: the **agentic** workflow (`.claude/agents/`, `CLAUDE.md`). The LangGraph
path is out of scope — see the note at the bottom.

## Problem

#12 landed `all_summaries.schema.json` (requiring `source_paper`,
`retrieval_method`, `summary`, `quotes`, with `additionalProperties: false`) and
schema-derived validation in `report_checker.check_source_tags`. But nothing on
the agentic side tells the `citation-traverse` subagent what an item should
contain:

- `.claude/agents/citation-traverse.md` §Output names only the two output
  *files* — no per-item field contract.
- `CLAUDE.md` §4b likewise gives only filenames (contrast §3 and §4a, which do
  give explicit JSON contracts).
- `retrieval_method` / `source_paper` appear nowhere in `.claude/` or
  `src/atlas_chat/atlas_chat/agents/*.prompt.yaml`.

So the subagent invents a shape. Real output from a completed run
(`projects/HCA_reproductive_atlas_v1/traversal_output/`):

```json
{"title": "...", "authors": [...], "year": 2026,
 "doi": "10.64898/2026.06.10.731198", "corpusId": "289267967", "quotes": [...]}
```

Item keys are `[authors, corpusId, doi, quotes, title, year]`. Validated against
the schema: **76 errors** across 19 items in one file, **48** across 12 in the
other. Missing `source_paper`, `retrieval_method` and `summary` (despite the
agent's own rule "Summarize each snippet as it is returned"); `authors`/`title`/
`year` now forbidden by `additionalProperties: false`.

## Fix

1. Add an explicit item contract to `.claude/agents/citation-traverse.md` and
   `CLAUDE.md` §4b, matching `all_summaries.schema.json` field-for-field, and
   name the schema file as the source of truth rather than restating it loosely.
2. Make step 6 of `CLAUDE.md` (explicit validation) call `check_source_tags`,
   not just `validate_report` — otherwise the orchestrator cannot see these
   errors.

## Decision needed: how to tag local-index hits

The schema's `retrieval_method` enum is `corpus_snippet | supplement |
citation_traversal | free_search`. It has no member for evidence served by the
**local snippet index** — but the local index is a distinct retrieval backend
(`local_snippet_index.py:1154` tags its snippets `source_method:
"local_snippet"`, and `CLAUDE.md` §4b documents that tag), and it is the *only*
route to papers ASTA cannot reach.

Losing that distinction would break the reasoning in this project's
`notes/EVIDENCE_COVERAGE_AUDIT.md`, which turns on "ASTA served this" vs "we read
this in a PDF/JATS we hold locally". Options:

1. Add `local_snippet` to the `retrieval_method` enum.
2. Keep `retrieval_method` as the mechanism and add an optional
   `retrieval_backend` (`asta` | `local_snippet`).
3. Map `local_snippet` → `corpus_snippet` and accept the loss.

(2) preserves #12's stated orthogonality — `role` = what the paper *is*,
`retrieval_method` = how it was *reached* — while adding backend as its own axis.

## Note on the LangGraph path

`graphs/report_graph.py` emits `source_method` (not `retrieval_method`) plus a
`snippet` field at lines 314/339/444, which the schema forbids, so its output
also cannot validate. If that runtime is deprecated it should be marked as such —
there is currently **no deprecation marker in `report_graph.py` on `main`,
`dev`, or this branch**, so a reader has no way to tell it is not the supported
path.
