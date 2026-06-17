# Atlas Reporter

## Overview

Cell types in online single-cell atlases are typically annotated with short and sometimes obscure names. Understanding what these names mean — and what is known about the cell types they describe — requires looking up the atlas paper and following its citations. While this scholarly workflow remains essential, it creates a significant barrier to efficient and effective browsing of online atlases.

Atlas Chat addresses this problem by enabling researchers to explore the literature associated with online atlases directly, without leaving their browsing context.

## What It Does

Atlas Chat generates structured, evidence-grounded cell type reports via an interactive Claude Code workflow (`/run-workflow`). The workflow fetches supplementary material, resolves cell type names from the atlas paper, traverses the citation network, and synthesises a markdown report — all using MCP tools and specialised subagents. Every claim is backed by an exact quote from a source paper.


## Design Principles

- **Source transparency** — Every claim is backed by a direct quote from a source paper, so users can judge the evidence for themselves.
- **Literature navigation** — Quotes are linked to their source papers, enabling users to move quickly from a summary to the primary literature.
- **Complement, not replace** — Atlas Chat lowers the barrier to efficient browsing, not to substitute for careful scholarly reading of the original papers.

## Hallucination Detection

LLMs can fabricate quotes and identifiers. Atlas Chat treats this as a first-class problem.

- Every blockquote in a generated report is verified against the original text before the report is saved. The validator checks that each quoted passage is a verbatim substring of a source paper (normalising whitespace, dashes, and smart quotes; handling ellipsis-separated segments).
- Every DOI and CorpusId reference is checked against the paper catalogue.
- If any check fails, the report is fed back to the LLM to fix, along with details of the error (up to two retries).

**What this guarantees:** quoted text in a final report actually appears in the cited source. DOIs are correct.

**What it does not guarantee:** that the surrounding narrative accurately interprets those quotes, or that the most relevant literature was found. Users should always follow quotes back to their source papers to assess context.

## Quick Start

Running Atlas-reporter requires an ASTA API KEY. You can apply for one here: https://allenai.org/asta/resources/mcp.

### Installation

```bash
git clone <repo-url> && cd atlas-chat
uv sync
```

Create a `.env` file in the repository root with the required API keys:

```
ASTA_API_KEY=...
```

### Running a Report

Open a Claude Code session in this directory. The MCP servers defined in `.mcp.json` will be loaded automatically. Then run:

```
/run-workflow
```

Claude will ask for a project name and cell type label, then execute the full pipeline.

> **Deprecated — programmatic path.** An earlier `atlas-report` CLI (PydanticAI graph in `src/.../graphs/`) is retained for reference only. Do not use it for new work; use `/run-workflow` instead.

## Project Configuration

Each atlas project lives in `projects/{project_name}/` and is defined by a single file, `cell_type_annotations.json`:

```json
{
  "source": {
    "doi": "10.1038/s41586-024-08002-x",
    "title": "A prenatal skin atlas reveals immune regulation of human skin morphogenesis"
  },
  "annotations": [
    {
      "label": "Iron-recycling macrophage",
      "granularity": "fine",
      "scope": "fetal"
    },
    {
      "label": "DC1",
      "granularity": "fine",
      "scope": "adult"
    }
  ]
}
```

- `source.doi` is required. `pmcid` and `corpus_id` can be pre-populated to skip runtime resolution.
- Each annotation requires `label`; `granularity` (`fine`/`broad`) and `scope` (`fetal`/`adult`/`organoid`) are optional.
- The schema is defined in `src/schemas/cell_type_annotation.schema.json`.

## How It Works

### Report Generation Pipeline

The agentic workflow follows a six-step sequence:

1. **FetchSupplements** — Resolve the atlas DOI to a PMCID via Europe PMC, fetch full text and supplementary file listings.
2. **ResolveName** — LLM call to identify the author-used terminology for the cell type in the atlas paper.
3. **ScanSupplements + CitationTraverse** *(parallel)* — LLM-driven extraction of markers and findings from supplements, plus Semantic Scholar snippet search at configurable depth to build a paper catalogue with verified exact quotes.
4. **SynthesizeReport** — LLM call to generate a markdown report from all collected evidence.
5. **ValidateReport** — Check that every blockquoted passage is a substring of the evidence corpus and that all referenced papers exist in the catalogue. On failure, retry synthesis (up to 2 retries).
6. **SaveReport** — Write the final validated report to `projects/{project}/reports/{cell_type}.md`.

### Output Structure

```
projects/{project}/
├── cell_type_annotations.json           # Project configuration (user-authored)
├── traversal_output/{cell_type}/
│   ├── atlas_full_text.txt              # Fetched atlas paper text
│   ├── name_resolution.json             # Resolved cell type names
│   ├── supplementary_findings.json      # Extracted markers and findings
│   ├── raw_snippets.json                # Raw citation snippets
│   ├── all_summaries.json               # Processed summaries with verified quotes
│   └── paper_catalogue.json             # Metadata for all discovered papers
└── reports/
    └── {cell_type}.md                   # Final validated report
```

### Validation

Reports are validated before saving:

- **Quote checking** — Every `> "..."` blockquote must be a substring of the evidence corpus (with normalisation for whitespace, dashes, smart quotes, and ellipsis segments).
- **Reference checking** — Every DOI or CorpusId in the report must exist in the paper catalogue.

If validation fails, the synthesis step is retried with specific error feedback (up to 2 retries).

## Agentic Workflow (Claude Code)

Requires a Claude Code session with the project's MCP servers configured (see `.mcp.json` and `.claude/settings.local.json`).

```
/run-workflow
```

Launches the report generation pipeline interactively, using MCP tools and Claude Code subagents. The orchestrator follows `CLAUDE.md` and delegates to specialised subagents in `.claude/agents/`.

## Dependencies and Integrations

### External Services (via MCP)

| Service | Tools Used |
|---|---|
| [ARTL MCP](https://github.com/vrothenbergUSD/artl-mcp) (Europe PMC) | Full text, supplements, ID resolution, PDF-to-markdown |
| [Semantic Scholar](https://www.semanticscholar.org/) (Asta) | Snippet search, paper metadata, citation traversal |
| [OLS4](https://www.ebi.ac.uk/ols4/) | Cell Ontology term lookup |
| Playwright | Browser automation (available but not central to current workflow) |

### Python Utilities

The Python package (`src/atlas_chat/`) provides supporting utilities used by the agentic workflow:

| Module | Role |
|---|---|
| `services/local_snippet_index.py` | Local vector index for preprints not yet in ASTA |
| `services/fetch_preprint.py` | JATS XML fetch for bioRxiv preprints |
| `validation/report_checker.py` | Shared quote and reference validation logic |
| `schemas/*.schema.json` | JSON schemas — source of truth for all output shapes |

### Environment Variables

| Variable | Required | Purpose |
|---|---|---|
| `ASTA_API_KEY` | Yes | Semantic Scholar API access |

## Development

This project uses Claude Code for agentic development. Load [`CLAUDE_dev.md`](CLAUDE_dev.md) as context when working on the codebase:

```
/load CLAUDE_dev.md
```

It covers schema-first design, testing conventions, the curation-mode write guard, and the deprecated programmatic path.

```bash
# Run tests
uv run pytest -m unit
uv run pytest -m integration   # requires API keys; skipped in CI

# Lint and type check
uv run ruff check src/ tests/
uv run mypy src/
```
