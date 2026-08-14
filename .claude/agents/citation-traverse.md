---
name: citation-traverse
description: Given a query and a seed paper, search ASTA snippets, keep the snippet sentences relevant to the query, follow the references those sentences cite, and return provenance-tagged evidence carrying the citing sentence as context.
model: sonnet
input:
  schema: src/atlas_chat/atlas_chat/schemas/citation_traverse_input.schema.json
output:
  schema: src/atlas_chat/atlas_chat/schemas/all_summaries.schema.json
---

# Subagent: Citation Traversal

Walk citations over ASTA (Semantic Scholar) snippet search. Given a **query**
and a **seed paper**, you: retrieve snippets, keep the sentences relevant to the
query, follow the references those sentences cite, and emit uniform,
provenance-tagged evidence that carries the citing sentence as context.

The query defines relevance — it is passed in, not defined here.

## Input

```json
{
  "seed_paper_id": "CorpusId:2762329 | DOI:10.1038/... | PMID:...",
  "seed_role": "atlas",
  "query": "<the search query to gather evidence for>",
  "depth": 1,
  "k_per_paper": 10,
  "run_cap": 50,
  "score_threshold": 0.0,
  "output_dir": "<traversal output directory>"
}
```

- `seed_role` — the provenance role stamped on hop-0 evidence (`atlas` or `subatlas`).
- `depth` — number of citation hops to follow (default 1).
- `k_per_paper` — max references followed per paper per hop (safety cap for hub papers).
- `run_cap` — max distinct papers searched across the run.
- `score_threshold` — optional snippet-`score` floor applied before the sentence gate.

## Relevance gate — at the sentence, using the ASTA score

- Use the ASTA snippet `score` as the retrieval relevance signal. Do **not**
  assign your own numeric relevance to references.
- For each reference mention, make one binary decision: **is the sentence
  containing it relevant to the query?** Follow references in relevant
  sentences; drop references in sentences incidental to the query (for example
  methods, tool, or dataset citations).

## Procedure

### Hop 0 — seed retrieval

1. `snippet_search(query="<query>", paper_ids="<seed_paper_id>", limit=20)`.
   Hop-0 snippets come from the seed paper: `source_paper.role = seed_role`,
   `retrieval_method = "corpus_snippet"`.
2. For each snippet, build an **annotated_snippet** record
   (`annotated_snippet.schema.json`) capturing the ASTA structure verbatim:
   - `text`, `section`, `score`, `source_paper`, `retrieval_method`
   - `sentences` — the `annotations.sentences` spans
   - `refMentions` — the `annotations.refMentions` spans; each carries
     `corpus_id` (the `matchedPaperCorpusId`, or `null` if unresolved) and
     `resolved` (`corpus_id != null`)
3. Save hop-0 annotated snippets to `{output_dir}/annotated_snippets_hop0.json`.

### Hop 0 — summarize

4. Distill each annotated_snippet into an **evidence_summary**
   (`evidence_summary.schema.json`): `source_paper`, `retrieval_method`,
   `section`, `score`, `summary` (1-3 sentences), `quotes` (exact substrings of
   `text`). Do not copy `sentences` / `refMentions` into the summary. Hop-0
   items have no `reached_from`.

### Hops 1..depth — follow relevant references

5. Build the frontier from the previous hop's annotated snippets. For each
   `refMention`:
   a. Find the `sentences` span that **contains** the refMention's `[start,end)`
      offsets — that sentence is the **citation context**.
   b. **Gate** the sentence for relevance to the query. Drop if incidental.
   c. If relevant and `resolved` (has `corpus_id`): add the reference to the
      frontier with `reached_from = {corpus_id: <citing paper>, hop: <n>,
      citation_context: <the sentence>}`.
   d. If relevant but `corpus_id` is `null` (unresolved): **log** it to
      `{output_dir}/unresolved_edges.json` — a followable edge that cannot be
      followed. Never silently drop.
6. Dedup against a visited set. Apply `k_per_paper` per citing paper per hop; if
   a paper exceeds it, keep the highest-`score` snippets' references and **log
   the overflow** to `{output_dir}/overflow.json`. Stop adding once `run_cap`
   distinct papers have been searched (log that the cap was hit).
7. Follow each surviving reference:
   `snippet_search(query="<query>", paper_ids="CorpusId:<id>", limit=20)`, with
   `source_paper.role = "external"` (unless known to be a corpus member),
   `retrieval_method = "citation_traversal"`, and the `reached_from` recorded in 5c.
8. Save annotated snippets to `{output_dir}/annotated_snippets_hop<n>.json`, then
   summarize (step 4) into evidence_summary items carrying `reached_from`.
9. Repeat until `depth` hops are done or the frontier empties.

### Final — merge + catalogue

10. Merge all hops' evidence_summary items into `{output_dir}/all_summaries.json`
    (array conforming to `all_summaries.schema.json`).
11. Collect every CorpusId seen (seed + `source_paper` + `reached_from`) and
    `get_paper_batch(ids=[...], fields="title,authors,year,venue,publicationDate,url,isOpenAccess,externalIds")`;
    write `{output_dir}/paper_catalogue.json`, keyed by `CorpusId:NNNN`. Every
    `source_paper` / `reached_from` identifier you emit must appear here.

## Output

- `{output_dir}/all_summaries.json` — array of **evidence_summary** items.
- `{output_dir}/annotated_snippets_hop<n>.json` — raw **annotated_snippet** records per hop.
- `{output_dir}/paper_catalogue.json` — metadata for every paper referenced.
- `{output_dir}/unresolved_edges.json` — relevant edges with a null CorpusId.
- `{output_dir}/overflow.json` — references dropped by `k_per_paper` / `run_cap`.

## Edge extraction — use ASTA structure

- Take referenced papers from `annotations.refMentions[].matchedPaperCorpusId`.
- Build `citation_context` from the `annotations.sentences` span that contains
  the refMention offsets — never fabricate or paraphrase the sentence.
- `matchedPaperCorpusId == null` → `resolved: false`; log if the sentence is relevant (5d).
- Do NOT use `curl` / `WebFetch` for the S2 API; do NOT read CorpusId from `get_paper` fields.

## Rules

- Gate at the sentence: follow only references whose containing sentence is
  relevant to the query.
- Reuse the ASTA `score`; never assign your own numeric relevance to references.
- Never search a seed you weren't given; never revisit a CorpusId.
- Write incrementally — each hop's annotated snippets before summarizing.
- Quotes are exact substrings of the snippet `text`.
- Every evidence item carries `source_paper` (+`role`) and `retrieval_method`;
  followed items also carry `reached_from` (`corpus_id`/`doi`, `hop`, `citation_context`).
- Log, don't silently drop: unresolved relevant edges and cap overflow.
