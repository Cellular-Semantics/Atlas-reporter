# Roadmap

## 0. Efficient agentic workflow architecture

**Status:** Design complete — see [`planning/efficient_workflow_design.md`](planning/efficient_workflow_design.md)

**Summary:** The April 2026 bulk generation run (~119 cell types) cost ~$597, almost entirely
from 27 Opus 4.6 subagents each independently loading full paper text into context. The core
problem is conflated phases: each agent performed name resolution + citation traversal +
synthesis in one long session, causing large cache writes per agent.

**Proposed three-phase architecture:**

1. **Name resolution** — one agent per source paper, full text permitted. Extracts
   cluster→label mappings from figure legends, supplementary tables, and lookup tables.
   May require one level of citation traversal with full text (e.g. Gopee 2024 → Reynolds
   2021 → cluster annotation table for c1/c2 identity). Full text loaded once, covers all
   cells from that paper.

2. **Evidence gathering** — snippet search only, no full text. Can be batched (one agent
   per source paper, all cells sequentially). Builds `all_summaries.json` and
   `paper_catalogue.json` with proper citation chains.

   *Optional: Haiku annotation pass.* After evidence gathering, a single Haiku call
   (cheap: ~$0.25/MTok) receives the full paper text + all collected snippets and adds
   2–3 sentences of surrounding context to each snippet. One call covers all cells from
   that paper. This enriches snippets without the synthesis agent needing the full text.
   **Note:** Haiku annotation enriches *known* snippets — it cannot substitute for name
   resolution when the identity-defining table was never surfaced by snippet search in
   the first place. The c1/c2 case (cluster label → named cell type) requires targeted
   full-text extraction at Phase 1, not annotation at Phase 2. A better fit for Haiku
   at Phase 1 is: give it the full text and ask "what do cluster labels c1–c8 correspond
   to?" — a direct extraction task that is cheap and covers all cells in one call.

3. **Synthesis** — no tool calls. Reads pre-built traversal output, weaves citation chains
   into the report. One agent per cell type, 1–2 turns, minimal cache write footprint.
   Validation and CL mapping appended to the same short session.

**Estimated cost at Sonnet rates with this architecture:** <$10 for 39 cells vs ~$45
proportional estimate for the current approach.

**Billing note:** Agentic workflow (Claude Code subagents) draws against quota rather than
per-token billing. This makes agentic preferable over programmatic (`report_graph.py`) for
bulk generation even where costs are non-trivial.

---

## 0b. Test suite grounded in high-quality reference reports

**Status:** Design ready — reference corpus available

The April 2026 agentic run produced a set of high-quality reports that serve as the
ground truth for testing. These are expensive to generate but stable — they represent
the quality bar the pipeline should meet.

**Test categories:**

### Name resolution tests

Labels that require non-trivial name resolution are the best tests of the Phase 1
pipeline. The adult keratinocyte clusters (c1–c8 from Reynolds 2021, integrated into
Gopee 2024) are ideal:

- **c1, c2** — require full text from *two* papers (Gopee → Reynolds lookup table).
  Snippet search alone returns sketchy or irrelevant results (melanoma studies, wound
  care reviews). A passing test must: (a) identify Reynolds as the source atlas,
  (b) retrieve the cluster annotation table from Reynolds full text,
  (c) map c1 → "undifferentiated KC", c2 → "proliferating KC".
- **c3–c8** — same two-paper chain, varying cluster identities.

*Could Haiku annotation have saved the c1/c2 case?* No — at least not the snippet
annotation variant. The problem is discovery, not context. The cluster mapping table
was never surfaced by snippet search, so there were no snippets to annotate. What
*would* work is using Haiku for targeted extraction: give it the Reynolds full text
and ask "list the cluster labels and their annotations". That is a different, cheaper
use of Haiku and should be tested as a Phase 1 strategy.

### Evidence chain quality tests

High-quality reports contain cross-paper citation chains where multiple independent
sources corroborate or extend the same claim. The c2 report is a strong example:
Reynolds (2021) defines the cluster → Cheng et al. (2018) identified the equivalent
"mitotic" cluster independently → Negri & Watt (2022) re-analysed Reynolds and
confirmed the "proliferation cluster". Each paper adds distinct evidence.

**Proposed test:** given `all_summaries.json` for c2 containing snippets from all
three papers, the synthesised report must: (a) cite all three papers, (b) use distinct
evidence from each (not just repeat the Reynolds claim three times), (c) show the
logical progression across papers (independent identification → re-analysis → confirmation).

A report that cites only Reynolds for everything, or that pads with generic keratinocyte
biology, fails this test even if it passes quote validation.

### Regression tests for known failure modes

- **Hallucinated DOIs** — validate every DOI in the report against Europe PMC, not
  just against paper_catalogue.json (which may itself be fabricated). The Szabó et al.
  (2025) incident is the reference case.
- **Generic background inflation** — reports should contain more atlas-specific claims
  than generic cell biology. Measurable heuristic: count blockquotes from the atlas
  paper vs. background-only paragraphs with no blockquote.
- **Missing CL mapping** — all reports must have a `Cell Ontology:` header line.
- **Missing blockquote attribution** — every blockquoted passage (`> "..."`) must be
  followed by a `>\n> — Author et al. (Year)` attribution line. The Neuroendocrine
  report (Apr 2026) is the reference failure case: all 15 quotes lack attribution
  despite the quote content being verifiable. The validator currently only checks
  quote content, not attribution presence. Add a check to `report_checker.py`.

**Reference corpus location:** `projects/fetal_skin_atlas/reports/` (Apr 2026 reports).
Reports from March 18/20 are explicitly *not* reference quality.

---

## 1. Report quality: atlas-specific content over generic background

| Phase | What | Branch | Tests Written During |
|-------|------|--------|----------------------|
| 0 | End-to-end acceptance spec | main | `scripts/e2e_smoke.py` — smoke checks only |
| 1 | Repository cleanup | `cleanup/flatten-package-structure` | Smoke checks must pass before merge |
| 2 | Agentic refactor (items 1+2 merged) | `feature/llm-driven-traversal` | Unit tests for stable modules + tool defs |
| 3 | Project generation | `feature/project-generation` | Schema validation, CSV parsing tests |

Phases 2 and 3 can run in parallel after Phase 1 merges.

---

## Phase 0: End-to-End Acceptance Criteria

Before any structural changes, define what "nothing broke" means. This is a specification, not a test suite — a script (`scripts/e2e_smoke.py`) that verifies all three modes without API calls.

### Programmatic mode
- `uv sync` succeeds
- `atlas-report --project fetal_skin_atlas --cell-type "Macro_1" --dry-run` exits 0
- `from atlas_chat.validation.report_checker import validate_report` imports successfully
- `from atlas_chat.services.atlas_paper import load_project_config` loads config and returns DOI
- `validate_report(report_path, traversal_dir)` passes for 3 existing reports (Macro_1, LC_1, NK)

### Agentic mode
- All `@` path references in AGENT.md resolve to real files
- All paths in `.claude/agents/*.md` resolve
- `.claude/hooks/check_report_refs.py` imports `atlas_chat.validation.report_checker`
- All 5 prompt YAMLs load via `load_prompt()`

### Chat mode
- CHAT.md path references resolve
- `/load-project-context` can locate project data

### Golden-data regression
- Pick 3 representative reports. Run `validate_report()` against their traversal data. These must pass. This catches changes to validation logic or evidence format assumptions.
- `check_quotes` and `check_references` are pure functions; their behaviour on known inputs is the regression contract.

---

## Phase 1: Repository Structure Cleanup

**Status:** Not started
**Branch:** `cleanup/flatten-package-structure`
**Prerequisite:** Phase 0 smoke script exists and passes

### Problem

Oddly nested `src/atlas_chat/atlas_chat/` structure from early scaffolding. Schemas duplicated between `src/schemas/` and the inner package. Empty shadow directories at the outer level.

### Target layout

```
src/atlas_chat/
  __init__.py
  cli.py
  agents/        ← prompt YAMLs
  graphs/
  llm/
  schemas/       ← consolidated (merge both locations)
  services/
  utils/
  validation/
  pyproject.toml
```

### Sequence

1. Audit and document what lives where
2. Flatten: move `src/atlas_chat/atlas_chat/*` up one level, delete inner directory
3. Update internal imports (package name `atlas_chat` stays the same)
4. Update all `@` path references in AGENT.md, CHAT.md, `.claude/agents/*.md`
5. Consolidate schemas into `src/atlas_chat/schemas/`
6. Fix `prompt_loader.py` `_AGENTS_DIR` path calculation (one fewer nesting level)
7. Update `pyproject.toml` paths (setuptools find, coverage source, mypy packages)
8. Decide on `atlas_chat_validation_tools` — keep or remove empty stubs
9. Run Phase 0 smoke checks — all must pass before merge

**Rules:** Structure changes only. No feature work. No logic changes.

**Highest-risk breakage points:**
- `prompt_loader.py` `_AGENTS_DIR` — navigates `parent.parent`; after flattening this is wrong
- AGENT.md `@` imports — if not updated, agentic workflow silently can't find prompts

---

## Phase 2: Agentic Refactor — LLM-Driven Traversal with Cost Tracking

**Status:** Not started — needs design
**Branch:** `feature/llm-driven-traversal`
**Merges ROADMAP items 1 (unified queries) and 2 (LLM-driven traversal)**

### Why merge items 1 and 2

The whole point of `query_unified()` is to support tool-calling loops with usage tracking — exactly what LLM-driven traversal needs. Doing cost tracking first without the traversal refactor means touching the same code twice.

### Design philosophy: priorities, not procedures

The current programmatic traverser is rigid: fixed snippet search, broaden at depth 1, return everything. The agentic path lets the LLM decide. The refactored programmatic path should adopt the agentic philosophy with budget constraints:

**Give the LLM priorities, not steps:**
1. First: find direct evidence about this cell type in the seed paper
2. Second: if the seed paper references other studies of this cell type, follow those
3. Third: broaden to the cell type in other tissue contexts if direct evidence is thin
4. Stop when evidence covers markers, function, and location — or after N tool calls

**Constrain cost, not behaviour.** Set `max_turns` on `query_unified()` to cap total tool calls. Track usage via `track_usage=True`. This is a budget guardrail, not a behaviour script.

**Do not overfit to the fetal_skin_atlas reports.** The 34 existing reports are a validation baseline, not a training set. The refactored pipeline should produce reports of comparable quality but not identical content (different traversal paths, different quotes). The regression test is: `validate_report()` passes on newly generated reports.

### Atlas paper full text

AGENT.md currently says "Prefer `snippet_search` over `get_europepmc_full_text`." This is correct for agentic sessions (huge output, fragile download). But the programmatic path already fetches full text (FetchSupplements node).

**Resolution:** Keep the snippet-first guidance for the agentic workflow. For the programmatic path, make full text available as a tool the LLM can query on demand — a `search_atlas_full_text(query)` tool that does local text search against the already-fetched document. The traversal prompt should mention it as a fallback: "If snippet search does not cover methodology or supplementary table references, search the atlas paper full text."

This matters because subtle decisions (e.g. which annotations are integrated from external sources, tissue-specific terminology) often require reading the methods or figure legends — information that snippet search may not surface.

### Sequence

1. Define Semantic Scholar tools as `cellsem_llm_client.tools.Tool` objects (or bridge via `load_mcp_tools()` if ASTA MCP server is already running)
2. Replace `citation_traverser.py` with `services/llm_traverser.py` — same interface, LLM-driven internals
3. Replace `_llm_call()` in `report_graph.py` with `query_unified(..., track_usage=True)`
4. Accumulate `UsageMetrics` on `ReportState`, print cost summary per run and per batch
5. Simplify or remove `_summarize_snippets` if the LLM extracts quotes during traversal
6. Add `search_atlas_full_text` tool for the programmatic traversal

### Tests written during this phase
- Unit tests for `report_checker.py` (stable pure logic — the validation contract)
- Unit tests for `atlas_paper.py` (config loading, path helpers)
- Unit tests for `prompt_loader.py` (YAML loading, template rendering)
- Unit tests for new tool definitions (serialization, handler dispatch)
- Integration test (marked, skipped without API keys): single cell type end-to-end

### Trade-offs
- More LLM calls = higher cost per run, but fewer wasted tokens on irrelevant evidence
- Non-determinism — different paths on re-runs; the validation contract is deterministic even if content is not
- Tool bridge vs direct handlers: MCP bridging is simpler but adds a process dependency

---

## Phase 3: Project Generation Workflow

**Status:** Not started — needs design
**Branch:** `feature/project-generation`
**Independent of Phase 2 — can develop in parallel after Phase 1**

### Problem

Setting up a new atlas project requires manually authoring `cell_type_annotations.json` — tedious for large atlases and error-prone for unfamiliar users.

### Goal

An `atlas-generate-project` command (or `/generate-project` in Claude Code) that creates project config from an atlas source.

**Effort:** Medium. Requires refactoring the agentic workflow to separate catalogue writes from report synthesis, and adding an external DOI check to `report_checker.py`.

## 6. Distinguish citation-traversed from free-search evidence in reports

**Status:** Not started

The paper catalogue already tags each entry with `"source": "citation_traverse"` or
`"source": "snippet_search"` (free search). This distinction matters: citation-traversed
papers are linked to the atlas via its own reference list; free-search papers are
background literature that the atlas may not cite at all.

Reports should make this visible to readers. Two complementary approaches:

**In the report text:** Mark free-search citations with a subtle indicator, e.g.
`(Woo et al., 2014†)` with a footnote/legend explaining `†` = general background
literature not directly cited by the atlas. This flags to readers when the agent
has gone beyond the atlas evidence chain.

**In the report header:** Add a `Sources:` line summarising counts, e.g.
`Sources: 6 atlas-cited papers, 2 background (free search)`. A high free-search
fraction is a quality signal that name resolution may have been incomplete (the
Neuroendocrine/Merkel cell case is the reference example: 6 of 7 papers came from
free search because the opaque "Neuroendocrine" label prevented effective
citation-scoped traversal).

Free-search fallback is sometimes necessary and legitimate — for well-studied cell
types the atlas may have few direct citations. The goal is transparency, not
elimination. The validator should warn (not fail) when all evidence is free-search.

**Effort:** Small for the header summary (read catalogue, count sources, insert line).
Medium for inline citation markers (synthesizer prompt change + validator check).

## 7. Project generation workflow

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
- Validate against `cell_type_annotation.schema.json`
- Resolve DOI → PMCID via Europe PMC
- Optionally deduplicate annotations at multiple granularity levels
- Interactive review before saving

### Tests written during this phase
- Unit tests for schema validation
- Unit tests for CSV/TSV column mapping
- Integration test for DOI → PMCID resolution

---

## Coverage Ratchet (ongoing, not a discrete phase)

Tests are written during Phases 1–3, not as a standalone effort. The 60% coverage threshold should be adjusted:

- After Phase 1: lower to 0% or write `report_checker` + `atlas_paper` unit tests to reach ~30%
- After Phase 2: should reach 40–60% from tests written during the refactor
- Ratchet up as new code is added

The pre-commit hook should enforce whatever the current floor is, not an aspirational target that forces bypass.
