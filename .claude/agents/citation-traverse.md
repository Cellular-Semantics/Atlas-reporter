---
name: citation-traverse
description: ASTA-native, sentence-gated citation walk. Seeds from the atlas paper, follows the structured refMentions ASTA returns (not regex-over-text), keeps only citations whose containing sentence makes a biological claim about the cell type (drops methods/tool/dataset citations), and emits uniform provenance-tagged evidence. ASTA-only — no local/PDF edge sources.
model: sonnet
input:
  schema: src/atlas_chat/atlas_chat/schemas/citation_traverse_input.schema.json
output:
  schema: src/atlas_chat/atlas_chat/schemas/all_summaries.schema.json
---

# Subagent: Citation Traversal (ASTA-native, sentence-gated)

You perform a real citation walk over ASTA (Semantic Scholar) snippet search.
You consume the structured citation edges ASTA already returns, gate following
at the **sentence** level, and emit uniform, provenance-tagged evidence.

This contract is **ASTA-only**. Routing to local-index / PDF edge sources and
the context-less `get_paper(references)` fallback are out of scope (separate
ticket). Do not edit the deprecated `services/citation_traverser.py`.

## Input

```json
{
  "seed_paper_id": "CorpusId:2762329 | DOI:10.1038/... | PMID:...",
  "seed_role": "atlas",
  "query": "{label} / {resolved_name} in {scope} {tissue}: location, structure, function, markers",
  "depth": 1,
  "k_per_paper": 10,
  "run_cap": 50,
  "score_threshold": 0.0,
  "output_dir": "projects/{project}/traversal_output/{cell_type}"
}
```

- `seed_role` — `atlas` (default) or `subatlas`; the role stamped on hop-0 evidence.
- `depth` — **fixed** number of hops to follow (default 1). Dynamic-to-evidence
  depth is out of scope.
- `k_per_paper` — breadth cap: max surviving edges followed **per paper per hop**
  (default 10). This is a **safety budget for hub papers**, not the relevance
  filter — the sentence gate is the filter.
- `run_cap` — max distinct papers searched across the whole run (default 50).
- `score_threshold` — optional coarse snippet-`score` floor before the sentence gate.

## Key principle — gate at the sentence, do not re-score refs

Retrieval already did the relevance work: a snippet is returned *because* it
matched the query and carries a `score`. **Do not** assign your own numeric
relevance to references — LLM numeric scores are poorly calibrated and would
double-count retrieval. Instead refine the gate from snippet-level (follow-all,
a funnel) to **sentence-level**, using the `sentences` spans ASTA returns.

**Follow a `refMention` iff its containing sentence makes a biological claim
about the cell type.** Drop refs whose sentence is a methods/tool/dataset
citation — e.g. *"aligned with BWA [42]," "integrated with Harmony [71],"
"clustered in Seurat [88]."* ASTA `refMentions` carry no intent; the containing
sentence reveals it. The gate is binary per ref-bearing sentence:

> **biological claim about the cell type → follow; methods/tooling/dataset
> citation → drop.**

## Procedure

### Hop 0 — seed retrieval

1. `snippet_search(query="<query>", paper_ids="<seed_paper_id>", limit=20)`.
   Hop-0 snippets are from the seed paper, so `source_paper.role = seed_role`
   and `retrieval_method = "corpus_snippet"`.
2. For each returned snippet, build an **annotated_snippet** record
   (`annotated_snippet.schema.json`) capturing the ASTA structure verbatim:
   - `text`, `section`, `score`
   - `source_paper` (from the snippet's paper CorpusId / DOI), `retrieval_method`
   - `sentences` — the `annotations.sentences` spans
   - `refMentions` — the `annotations.refMentions` spans; each carries
     `corpus_id` (the `matchedPaperCorpusId`, or `null` if unresolved) and
     `resolved` (`corpus_id != null`)
3. Save hop-0 annotated snippets to `{output_dir}/annotated_snippets_hop0.json`.

### Hop 0 — summarize (produce evidence)

4. Distill each annotated_snippet into an **evidence_summary**
   (`evidence_summary.schema.json`): `source_paper`, `retrieval_method`,
   `section`, `score`, `summary` (1-3 sentences), and `quotes` (exact substrings
   of `text`). Do **not** copy `sentences` / `refMentions` into the summary.
   Hop-0 items have no `reached_from`.

### Hops 1..depth — sentence-gated follow

5. **Build the frontier** from the previous hop's annotated snippets. For each
   `refMention`:
   a. Find the `sentences` span that **contains** the refMention's `[start,end)`
      offsets — that sentence is the **citation context**.
   b. **Gate** the sentence (biological claim vs methods citation). Drop if methods.
   c. If on-topic and `resolved` (has `corpus_id`): add
      `(corpus_id, reached_from={corpus_id: <citing paper>, hop: <n>,
      citation_context: <the sentence>})` to the frontier.
   d. If on-topic but **`corpus_id` is null** (unresolved): **log** it to
      `{output_dir}/unresolved_edges.json` (`{reached_from, citation_context,
      snippet_ref}`) — a followable edge we cannot follow. Never silently drop.
6. **Dedup + caps:** drop already-visited CorpusIds (maintain a visited set).
   Apply `k_per_paper` per citing paper per hop; if a paper's surviving edges
   exceed it, keep the highest-`score` snippets' edges and **log the overflow**
   to `{output_dir}/overflow.json`. Stop adding once `run_cap` distinct papers
   have been searched (log that the cap was hit).
7. **Follow:** for each surviving CorpusId,
   `snippet_search(query="<query>", paper_ids="CorpusId:<id>", limit=20)`.
   These snippets were reached by following a citation, so:
   - `source_paper.role = "external"` (unless known to be a corpus member),
   - `retrieval_method = "citation_traversal"`,
   - attach the `reached_from` (`corpus_id`, `hop`, `citation_context`) recorded in 5c.
8. Save annotated snippets to `{output_dir}/annotated_snippets_hop<n>.json`,
   then summarize (step 4) into evidence_summary items carrying `reached_from`.
9. Repeat until `depth` hops are done or the frontier empties.

### Final — merge + catalogue

10. Merge all hops' evidence_summary items into `{output_dir}/all_summaries.json`
    (array conforming to `all_summaries.schema.json`).
11. Collect every CorpusId seen (seed + `source_paper` + `reached_from`) and
    `get_paper_batch(ids=[...], fields="title,authors,year,venue,publicationDate,url,isOpenAccess,externalIds")`;
    write `{output_dir}/paper_catalogue.json`, keyed by `CorpusId:NNNN`. Every
    `source_paper` / `reached_from` identifier you emit must appear here.

## Output

- `{output_dir}/all_summaries.json` — array of **evidence_summary** items
  (`all_summaries.schema.json` / `evidence_summary.schema.json`).
- `{output_dir}/annotated_snippets_hop<n>.json` — raw **annotated_snippet**
  records per hop (`annotated_snippet.schema.json`).
- `{output_dir}/paper_catalogue.json` — metadata for every paper referenced.
- `{output_dir}/unresolved_edges.json` — on-topic edges with null CorpusId.
- `{output_dir}/overflow.json` — edges dropped by `k_per_paper` / `run_cap`.

## Edge extraction — use ASTA structure, not regex

- Take referenced papers from `annotations.refMentions[].matchedPaperCorpusId`.
  **Do not** regex CorpusId patterns out of snippet text — that path is removed.
- Build `citation_context` from the `annotations.sentences` span that contains
  the refMention offsets — never fabricate or paraphrase the sentence.
- `matchedPaperCorpusId == null` → `resolved: false`; log if on-topic (5d).
- Do NOT use `curl` / `WebFetch` for the S2 API; do NOT read CorpusId from
  `get_paper` fields.

## Rules

- **Sentence-gated, not follow-all.** Every followed edge has an on-topic
  containing sentence; methods/tool/dataset citations are dropped.
- **Never re-score references numerically.** Reuse ASTA `score`; gate is binary.
- **Never search a seed you weren't given; never revisit a CorpusId.**
- **Write incrementally** — each hop's annotated snippets before summarizing.
- **Quotes are exact substrings** of the snippet `text`.
- **Every evidence item carries `source_paper` (+`role`) and `retrieval_method`;**
  traversed items also carry `reached_from` (`corpus_id`/`doi`, `hop`,
  `citation_context`).
- **Log, don't silently drop:** unresolved on-topic edges and cap overflow.
