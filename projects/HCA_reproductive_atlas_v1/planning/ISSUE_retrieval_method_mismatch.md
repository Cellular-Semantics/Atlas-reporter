# [schema] `source_method` vs `retrieval_method`: runtime output cannot satisfy `all_summaries.schema.json`

Follow-up to #12 (evidence source tagging: `source_paper.role` + `retrieval_method`).

## Summary

The schema introduced in #12 and the field the graph actually emits are different
fields with different vocabularies. Any `all_summaries.json` the graph writes today
fails `report_checker.check_source_tags`.

## The mismatch

Three names for provenance are live at once:

| Where | Field | Values |
|---|---|---|
| `services/local_snippet_index.py:1154` | `source_method` | `"local_snippet"` |
| `graphs/report_graph.py:314,339,444` | `source_method` | `"asta"` (default) |
| `services/citation_traverser.py:198` (docstring) | `source_method` | `"local_snippet"` |
| `schemas/all_summaries.schema.json` (#12) | **`retrieval_method`** | `corpus_snippet`, `supplement`, `citation_traversal`, `free_search` |

`report_graph.py:444` sets `ev["source_method"]` (and `ev["snippet"]`) on every
evidence item that becomes `all_summaries.json`. The schema declares
`additionalProperties: false` and requires `source_paper` + `retrieval_method`, so
each item fails twice over: unexpected `source_method`/`snippet`, missing
`retrieval_method`/`source_paper`.

## Why this isn't just a rename

`retrieval_method` models *how the evidence was reached* and `source_paper.role`
models *what the paper is* — orthogonal, per #12's own field descriptions.
`source_method` encodes a **third** axis the schema does not model: which retrieval
*backend* served the snippet (ASTA API vs the local snippet index). Collapsing
`local_snippet` into `corpus_snippet` would lose exactly the distinction the
HCA reproductive atlas coverage audit depends on — "ASTA served this" vs "we read
this in a PDF/JATS we hold locally", for papers ASTA cannot reach at all.

## Decision needed

1. Add `local_snippet` to the `retrieval_method` enum; **or**
2. Keep `retrieval_method` as the mechanism and add a separate optional
   `retrieval_backend` (`asta` | `local_snippet`); **or**
3. Declare backend identity out of scope and map `local_snippet` →
   `corpus_snippet`, accepting the loss.

(2) preserves both axes cleanly and keeps #12's orthogonality intact.

## Then wire the graph

No new information is needed — the graph already holds everything:

- `source_paper.role` — `corpus.json` records `role: atlas|subatlas` per paper;
  anything not a corpus member is `external`.
- `retrieval_method` / backend — `report_graph.py:309` already has `asta_snips`
  and `local_snips` as separate lists before merging, so the tag is known at the
  point the two are combined.
- Drop `snippet` from the emitted item, or add it to the schema (it is currently
  carried "for validation" and then written out).

## Also

`tests/unit/test_evidence_provenance_schema.py` and
`test_report_checker_source_tags.py` validate fixtures, not graph output. A test
that runs the graph's evidence-assembly path through `check_source_tags` would
have caught this.
