# Efficient Agentic Research Workflow — Design Notes

*Derived from conversation, April 2026*

---

## Context: What We Learned from the April 2026 Run

Generating ~119 cell type reports in one session cost approximately **$597**, almost entirely
from 27 Opus 4.6 subagents. The dominant cost driver was **cache writes** ($69.75 at Opus rates
= $18.75/MTok): each subagent independently wrote the full atlas paper text, system prompt, and
accumulated conversation context to the prompt cache.

The 6 Sonnet 4.6 subagents cost $23 combined for comparable work volume — a ~13× per-cell
cost reduction. Switching fully to Sonnet is the minimum viable improvement.

**Billing note:** Agentic workflow (Claude Code subagents) draws against quota rather than
per-token billing. Programmatic API calls (`report_graph.py`) are billed per token with no
quota coverage. This makes the agentic approach preferable for bulk generation even if quota
costs are non-zero.

---

## Root Cause: Conflated Phases

Each subagent performed all steps in a single long session:
fetch paper → name resolution → citation traversal → synthesis → validation → CL mapping

This means:
- Full paper text was loaded into context for every agent, independently
- Context grew with each step (compounding cache writes)
- Citation traversal happened mid-synthesis, pulling in additional papers

The traversal_output directory structure already reflects a better design: research outputs
(name_resolution, supplementary_findings, all_summaries, paper_catalogue) are separate from
the report. The problem is agents were generating both in one pass.

---

## Proposed Architecture: Three Phases

### Phase 1 — Name Resolution (per source paper, full text permitted)

**When full text is needed:** Name resolution cannot always be completed from snippets alone.
Cluster labels (c1, c2, LC_1, Macro_1) are often defined in figure legends, supplementary
tables, or inline annotation tables that snippet search may not surface reliably. The c1
example: snippet search returns sketchy results; reading the Reynolds full text reveals a
explicit cluster→label lookup table.

**Cascading name resolution:** Some labels require one level of citation traversal even for
name resolution. For example, c1/c2 in the prenatal skin atlas context requires:
  Gopee (2024) → integrated Reynolds (2021) → Reynolds cluster annotation table

In such cases, the name resolution agent may need to fetch the referenced paper's full text,
not just the seed paper. This is bounded: it is one level of traversal, for one paper, done
once.

**Efficiency:** One name resolution agent per source paper. Reynolds (2021) covers all 32
adult-scope annotations. Full text loaded once, cluster mapping extracted for all cells,
name_resolution.json written for each. Agent terminates.

**Output:** `traversal_output/{cell}/name_resolution.json` for all cells from that paper.

---

### Phase 2 — Evidence Gathering (snippet search only, no full text)

Once identity is confirmed, a chain of snippets across papers is sufficient for synthesis.
The full paper text is not needed at this stage.

**Per-cell or per-batch:** Evidence gathering can be batched within one agent (one agent
handles all cells from one source paper sequentially), keeping the source paper's citation
graph warm in context. Each cell type gets:
- Snippet search scoped to the atlas paper (depth-1)
- Snippet search on matched corpus IDs from depth-1 results (depth-2)
- Results written to all_summaries.json + paper_catalogue.json

Context grows across cells but only from snippet JSON responses — much smaller than full text.

**Output:** `traversal_output/{cell}/all_summaries.json` + `paper_catalogue.json`

---

### Phase 2b — Haiku Snippet Annotation (optional enrichment step)

**Problem:** Raw snippets from `snippet_search` sometimes lack context — the surrounding
paragraph, the section heading, whether the snippet comes from a methods note vs. a key
result. Synthesis agents working from thin snippets produce thinner reports.

**Solution:** After evidence gathering, run a single Haiku call per source paper:

```
Input:  full paper text + all snippets collected across all cells from that paper
Task:   for each snippet, add 2-3 sentences of context — section heading, 
        what precedes/follows, any relevant table or figure reference
Output: annotated snippets saved back to all_summaries.json
```

**Why Haiku:** At ~$0.25/MTok input, a 150K-token paper costs ~$0.04 to process. Annotating
all snippets for all 32 Reynolds cells in one pass would cost under $1. The synthesis agent
then never needs the full text.

**Key property:** Multiple cells' snippets can be annotated in a single Haiku call — Haiku
reads the paper once, annotates all N snippets regardless of which cell type they belong to.
This amortises the full-text read cost across all cells from that paper.

**Output:** Enriched `all_summaries.json` entries with an added `context` field per snippet.

---

### Phase 3 — Synthesis (no tool calls)

With rich traversal_output in place, synthesis is a pure read-and-write operation:

```
Input:  traversal_output/{cell}/*.json  (name_resolution, supplementary_findings,
                                         all_summaries with context, paper_catalogue)
Output: reports/{cell}.md
Tools:  none needed
```

The synthesis agent reads the pre-built evidence corpus and weaves it into a report. Citation
chains (e.g. Reynolds → Cheng 2018 → Negri & Watt 2022) are already present in
all_summaries.json — the agent's job is to recognise the connections and build the narrative,
which requires no tool calls.

Each synthesis agent handles one cell type in ~1-2 turns. Cache write cost is minimal:
system prompt + input files (tens of KB). No compounding context growth.

After synthesis: validation (quote check against corpus) and CL mapping (OLS lookup only)
can be appended to the same short session without significant cost impact.

**Output:** `reports/{cell}.md` with validated quotes and CL mapping header.

---

## Cost Model Comparison

| Approach | Full text loads | Cache writes | Model | Relative cost |
|----------|----------------|--------------|-------|---------------|
| April 2026 (actual) | 1 per agent × 27 agents | ~564K tokens/agent | Opus | ~$597 |
| Single-agent per paper (Sonnet) | 1 per paper | ~1 per paper + context growth | Sonnet | ~$45 (est.) |
| Three-phase (Sonnet + Haiku annot.) | 1 per paper (Phase 1 + Haiku) | Minimal per phase | Sonnet/Haiku | <$10 (est.) |

---

## Implementation Notes

- The programmatic graph (`report_graph.py`) produces lower quality output because it makes
  single-shot LLM calls without tool access. Nodes cannot follow unexpected citation threads
  or recover from ambiguous name resolution. The solution is not to abandon the graph but to
  make graph nodes invoke agents (with tool access) rather than bare LLM calls — preserving
  the quality of iterative research within a structured pipeline.

- The existing traversal_output structure already supports the three-phase design. No schema
  changes are needed; the phases just need to be separated into distinct agent sessions.

- For the current task (39 Reynolds/fetal cells needing regeneration): all traversal_output
  is from March 18/20 (old workflow) and should be treated as stale. Full re-research needed.
  Recommended: one Reynolds research agent (Phases 1+2) → Haiku annotation pass →
  per-cell synthesis agents.
