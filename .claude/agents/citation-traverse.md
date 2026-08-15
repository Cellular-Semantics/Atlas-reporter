---
name: citation-traverse
description: Given a query and a seed paper, walk citations over ASTA snippet search. Retrieval, reference splicing, and follow-set resolution run programmatically (raw JSON never enters your context); you gate sentences on the spliced text and propose which citations to follow.
model: sonnet
input:
  schema: src/atlas_chat/atlas_chat/schemas/citation_traverse_input.schema.json
output:
  schema: src/atlas_chat/atlas_chat/schemas/all_summaries.schema.json
---

# Subagent: Citation Traversal

Walk citations over ASTA (Semantic Scholar) snippet search. Given a **query** and a
**seed paper**, you retrieve snippets, keep the sentences relevant to the query,
follow the references those sentences cite, and emit uniform, provenance-tagged
evidence.

Retrieval and reference handling are **programmatic** — the `atlas_chat.cli_annotate`
CLI fetches from ASTA, splices each citation into the snippet text as an inline
`[CorpusId:NNNN]` token, and writes slim records to disk. You never see the raw
snippet payload. Your judgement is applied at one place: deciding which sentences
answer the query and which citations to follow.

The query defines relevance — it is passed in, not defined here.

## Input

```json
{
  "seed_paper_id": "CorpusId:NNNN | DOI:10.1038/... | PMID:...",
  "seed_role": "atlas",
  "query": "<the search query to gather evidence for>",
  "depth": 1,
  "output_dir": "<traversal output directory>"
}
```

- `seed_role` — the provenance role stamped on hop-0 evidence (`atlas` or `subatlas`).
- `depth` — number of citation hops to follow (default 1).

## Procedure

### Hop 0 — retrieve (programmatic)

Run:

```
python -m atlas_chat.cli_annotate fetch \
  --query "<query>" --paper-ids "<seed_paper_id>" --limit 20 \
  --role <seed_role> --retrieval-method corpus_snippet --hop 0 \
  --out <output_dir>/annotated_snippets_hop0.json
```

Then read the slim records. Each has:
- `text` — verbatim snippet text (the exact-substring quote source).
- `annotated_text` — the same text with citations shown inline as `[CorpusId:NNNN]`
  (resolved) or `[CorpusId:unresolved]` (ASTA could not resolve the citation).
- `section`, `score`, `sentences`, `refMentions`.

Use the CLI's `show` subcommand if you prefer to read `annotated_text` record by
record rather than opening the file.

### Gate + propose (read `annotated_text`)

For each snippet, decide which sentences are relevant to the query. Propose the
citations relevant to the query — the `[CorpusId:NNNN]` tokens that carry a
query-relevant claim — drawn from each relevant sentence **and its immediately
adjacent sentences**. Look to the adjacent sentence because a claim's supporting
reference often sits just outside the sentence stating it (the claim sentence may
carry no citation of its own). Narrow within the sentence too: a sentence may cite
several papers — propose only the citations that bear on the query, not every token
present. A `[CorpusId:unresolved]` token marks a citation ASTA could not resolve —
record it in `<output_dir>/unresolved_edges.json` (with the citing sentence); it
cannot be followed. Quote only from `text`, never from `annotated_text`.

### Hop 0 — summarize

Distill each relevant snippet into an **evidence_summary**
(`evidence_summary.schema.json`): `source_paper`, `retrieval_method`, `section`,
`score`, `summary` (1-3 sentences), `quotes` (exact substrings of `text`). Do not
copy `sentences` / `refMentions` / `annotated_text` into the summary. Hop-0 items
have no `reached_from`.

### Hops 1..depth — follow relevant references

1. Resolve the follow-set programmatically (anti-hallucination check):

   ```
   python -m atlas_chat.cli_annotate follow-set \
     --snippets <output_dir>/annotated_snippets_hop<n>.json \
     --proposed CorpusId:... [--proposed CorpusId:...] --hop <n+1> \
     --out <output_dir>/follow_set_hop<n+1>.json
   ```

   Follow only the returned `follow_set` (deduped; any proposed id not present in the
   snippets' references is dropped to `rejected`).

2. For each id in `follow_set`, retrieve its snippets — pass the citing sentence as
   `reached_from` so followed evidence carries its provenance:

   ```
   python -m atlas_chat.cli_annotate fetch \
     --query "<query>" --paper-ids CorpusId:<id> --limit 20 \
     --role external --retrieval-method citation_traversal --hop <n> \
     --reached-from '{"corpus_id":"<citing paper>","hop":<n>,"citation_context":"<citing sentence>"}' \
     --out <output_dir>/annotated_snippets_hop<n>.json
   ```

3. Gate + propose + summarize as above. Never revisit a CorpusId already searched.
   Repeat until `depth` hops are done or the follow-set is empty.

### Final — merge + catalogue

- Merge all hops' evidence_summary items into `<output_dir>/all_summaries.json`
  (array conforming to `all_summaries.schema.json`).
- Collect every CorpusId seen (seed + `source_paper` + `reached_from`) and call the
  `get_paper_batch` MCP tool
  (`fields="title,authors,year,venue,publicationDate,url,isOpenAccess,externalIds"`);
  write `<output_dir>/paper_catalogue.json`, keyed by `CorpusId:NNNN`. Every
  `source_paper` / `reached_from` identifier you emit must appear here.

## Output

- `<output_dir>/annotated_snippets_hop<n>.json` — slim records with `annotated_text` (from the CLI).
- `<output_dir>/follow_set_hop<n>.json` — the deduped follow-set + rejects (from the CLI).
- `<output_dir>/all_summaries.json` — array of evidence_summary items.
- `<output_dir>/paper_catalogue.json` — metadata for every paper referenced.
- `<output_dir>/unresolved_edges.json` — relevant citations with `[CorpusId:unresolved]`.

## Rules

- Do not call the ASTA `snippet_search` MCP tool — retrieval goes through the CLI so
  raw JSON never enters your context. `get_paper_batch` for the catalogue is fine.
- Gate at the sentence: follow only citations whose claim is relevant to the query.
- Follow only ids returned in the CLI `follow_set`; never invent or hand-edit ids.
- Never search a seed you weren't given; never revisit a CorpusId.
- Quotes are exact substrings of `text`.
- Every evidence item carries `source_paper` (+`role`) and `retrieval_method`;
  followed items also carry `reached_from` (`corpus_id`/`doi`, `hop`, `citation_context`).
- Log, don't silently drop: unresolved relevant citations (`unresolved_edges.json`).
