# Roadmap

## 1. Report quality: atlas-specific content over generic background

**Status:** Not started — highest priority

**Priority: HIGH.** This is the most impactful quality issue across generated reports.

Reports currently read like generic cell biology reviews with atlas citations bolted on. The pipeline treats every cell type the same: resolve name, gather evidence, synthesize. It doesn't ask "what does *this atlas* claim about this cell type that is novel or specific?" before assembling background.

**Observed problems:**

- **Too much generic content.** Reports fill sections with textbook-level information about well-known cell types rather than focusing on what the atlas paper contributes.
- **Name resolution fails on opaque labels.** Labels like `c1`, `c2`, ..., `c8` (adult keratinocyte clusters from Reynolds et al., integrated into Gopee) produce empty name resolutions. The programmatic pipeline has no recovery path — it proceeds with the opaque label and pulls irrelevant papers (melanoma studies, wound care reviews).
- **The agentic workflow handles this significantly better.** In a Claude Code session on `c1`, the agent: (1) read the config and noticed "adult scope", (2) inferred this meant integrated external annotations, (3) identified Reynolds et al. as the source atlas, (4) checked an existing successful adult-scope report for the pattern, (5) pivoted its entire strategy accordingly. The programmatic pipeline cannot do any of this — it runs a fixed sequence regardless of context.

**Root cause:** The programmatic pipeline lacks adaptive reasoning. It can't inspect its own intermediate results and change strategy. A thinking model with tool access (as in the agentic workflow) can.

**Proposed approach:**

1. **Add a "novel claims" extraction step** early in the pipeline — before general citation traversal, search the atlas paper (via `snippet_search`) for what it specifically claims about this cell type. This becomes the backbone of the report; background literature supports it rather than replacing it.
2. **Improve name resolution recovery** — when the label is opaque (short alphanumeric like `c1`, `F2`), the pipeline should search for cluster-to-name mapping tables in supplements and in the atlas text before giving up. The agentic workflow does this naturally by reasoning about context.
3. **Consider replacing the fixed pipeline with a thin wrapper around an agentic loop** — use `query_unified()` with tools and a thinking model to let the LLM drive the entire workflow, not just individual steps. This is the logical endpoint of item 2 below (LLM-driven traversal) extended to the full pipeline. The programmatic workflow would become an orchestration layer that launches a tool-equipped LLM conversation rather than a rigid graph.

**Relationship to other items:** This subsumes item 2 (LLM-driven traversal) if taken to its logical conclusion. Item 1 (cost tracking via `query_unified`) is a prerequisite for understanding the cost implications.

**Open question:** The agentic workflow may partly benefit from Claude Code session memory (e.g. knowing about Reynolds et al. from a prior run). A standalone programmatic run won't have this. The "novel claims" step and better name resolution would need to compensate.

## 2. Switch to unified queries with cost tracking (prerequisite for 1)

**Status:** Not started

The `cellsem_llm_client` library provides `query_unified()` — a single method that combines schema enforcement, tool calling, and usage tracking. The graph currently uses the older `query()` and `query_with_schema()` methods, which discard token counts and cost data.

**Goal:** Replace all LLM calls in `report_graph.py` with `query_unified(..., track_usage=True)`. Accumulate `UsageMetrics` on `ReportState` across all nodes (ResolveName, SnippetSummarizer batches, ScanSupplements, SynthesizeReport + retries). Print a cost summary at the end of each run, and in batch mode, a cumulative total.

**What this enables:**
- Per-run cost reporting (input/output/cached/thinking tokens + USD estimate)
- Batch cost forecasting (run one, extrapolate)
- Provider comparison (same report, Anthropic vs OpenAI cost)

**Effort:** Small. The calls already return structured output; the change is mechanical — swap method, collect `result.usage`, sum at the end.

## 3. LLM-driven citation traversal via tool calling

**Status:** Not started — needs design

The current citation traverser (`citation_traverser.py`) calls `AstaProvider` directly: it runs a fixed snippet search, broadens the query at depth 1, and returns everything. The LLM has no say in which papers are followed or which results are irrelevant.

The agentic workflow (Claude Code) does this differently — the LLM decides which snippets matter, which CorpusIds to follow, and when to stop. This produces more focused evidence and avoids noise from irrelevant citations.

**Goal:** Give the programmatic pipeline the same capability by wiring Semantic Scholar as LLM tools via `query_unified()` with tool calling.

**How it would work:**
1. Define Semantic Scholar tools (`snippet_search`, `get_paper`, `get_paper_batch`, `get_citations`) as `cellsem_llm_client.tools.Tool` objects with handlers that call the ASTA API.
2. Replace the fixed traversal loop with a `query_unified()` call that gives the LLM access to these tools plus a system prompt describing the traversal strategy.
3. The LLM decides: which snippets are relevant, which papers to follow up on, when the evidence is sufficient to stop.
4. The library's `_run_tool_loop` handles the multi-turn conversation automatically.

The library already supports this pattern — `query_unified` accepts `tools` and `tool_handlers`, runs a tool-call loop (up to `max_turns`), and optionally tracks usage across all turns.

Alternatively, `cellsem_llm_client.tools.mcp_source.load_mcp_tools()` can bridge MCP servers directly into LiteLLM tool format, which would let the programmatic pipeline use the same ASTA MCP server as the agentic workflow without duplicating tool definitions.

**What this enables:**
- Selective citation following — the LLM skips irrelevant papers instead of fetching everything
- Deeper traversal without proportional noise — depth 2+ becomes practical
- Convergence between programmatic and agentic workflows — same decision-making, different execution mode
- Cost tracking across the full traversal (via `track_usage=True`)

**Trade-offs to consider:**
- More LLM calls = higher cost per run (but potentially fewer wasted tokens on irrelevant evidence)
- Non-determinism — the LLM may follow different paths on re-runs
- Need to decide: use Tool objects with direct ASTA API handlers, or bridge the MCP server? MCP bridging is simpler (no duplicate code) but adds a process dependency.

**Relationship to item 1:** Item 1 proposes extending this approach to the full pipeline — not just traversal but the entire workflow driven by a thinking model with tools. If item 1 goes that direction, this item becomes a subset of it.

**Effort:** Medium. Needs a new traversal prompt, tool definitions, and changes to the FanOut node. The snippet summarizer step may become unnecessary if the LLM extracts quotes during traversal.

## 4. Repository structure cleanup

**Status:** Not started — requires careful planning

The project has an oddly nested structure from early development, with some duplication between levels (e.g. `src/atlas_chat/atlas_chat/`, schemas in multiple locations). This makes navigation confusing and risks divergence between duplicated files.

**Goal:** Flatten to a conventional Python package layout. Eliminate duplicated files and consolidate schemas, prompts, and config into canonical locations.

**Approach — must be done carefully:**
- Work on a dedicated branch, not main
- Audit every file to identify duplicates, dead code, and misplaced assets before moving anything
- Update all internal imports, entry points, pyproject.toml paths, and tool references
- End-to-end test all three modes (programmatic single + batch, agentic workflow, chat) before merging
- Verify: `uv sync`, `atlas-report --dry-run`, a real single-cell run, the agentic `/run-workflow`, and `/chat` all still work
- Keep the PR atomic — structure changes only, no feature work mixed in

**Risk:** High if done carelessly — broken imports, missing prompt files, or stale paths in AGENT.md/CHAT.md could silently break workflows. The careful branch + full test pass mitigates this.

## 5. Project generation workflow

**Status:** Not started — needs design

Currently, setting up a new atlas project requires manually authoring `cell_type_annotations.json` with the atlas DOI, title, and a list of cell type annotations with labels, scope, and granularity. This is tedious for large atlases and error-prone for users unfamiliar with the schema.

**Goal:** An `atlas-generate-project` command (or `/generate-project` in Claude Code) that creates a project config from an atlas source, with two input paths:

### Path A: From an online atlas (Playwright)
1. User provides a URL to an online atlas (e.g. CellxGene, HCA, or similar)
2. Playwright navigates to the atlas and extracts cell type annotations from the UI — labels, hierarchy, metadata
3. The LLM resolves the atlas DOI from the page content or linked publications
4. Generates `cell_type_annotations.json` with all discovered annotations

### Path B: From user-provided tabular data
1. User provides a CSV/TSV/spreadsheet with cell type annotations (at minimum a label column)
2. The LLM infers or asks for: atlas DOI, scope, granularity, and any missing metadata
3. Generates `cell_type_annotations.json`, mapping columns to schema fields

### Shared post-processing
- Validate the generated config against `cell_type_annotation.schema.json`
- Resolve DOI → PMCID via Europe PMC to confirm the atlas paper is accessible
- Optionally deduplicate annotations that appear at multiple granularity levels
- Interactive review: show the user the proposed config and let them edit before saving

**What this enables:**
- Lower barrier to entry — users don't need to understand the JSON schema
- Faster onboarding of new atlases
- Consistent annotation metadata (scope/granularity inferred rather than guessed)

**Effort:** Medium-large. Playwright extraction is atlas-specific and will need per-platform adapters (or a generic strategy that works across common atlas UIs). The CSV path is simpler and should come first.
