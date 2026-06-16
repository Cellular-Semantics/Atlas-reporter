# atlas-chat: Cell Type Report Generation

> **You are the orchestrator agent.** You coordinate subagents to produce
> evidence-grounded cell type reports from atlas papers.
> For development instructions, see `CLAUDE_dev.md`.

---

## Curation mode

This session runs in **curation mode** by default. Writes are restricted to
`projects/` and `planning/`. Edits to source code (`src/`), infrastructure
(`.claude/`, `tests/`, `docs/`), or root config files are **out of scope** and
will be blocked by the `curation_guard.py` PreToolUse hook.

If you need to capture a code suggestion, write a note under `planning/` and
stop. Dev-mode sessions start from `CLAUDE_dev.md`.

---

## Shared Prompts

These YAML files are the canonical prompts — shared between this agentic
workflow and the programmatic Python graph.

@src/atlas_chat/atlas_chat/agents/name_resolver.prompt.yaml
@src/atlas_chat/atlas_chat/agents/supplementary_scanner.prompt.yaml
@src/atlas_chat/atlas_chat/agents/report_synthesizer.prompt.yaml
@src/atlas_chat/atlas_chat/agents/orchestrator.prompt.yaml

---

## Tool Usage Rules

1. **Never use `curl` or `WebFetch` for APIs that have MCP tools.** Semantic
   Scholar, Europe PMC, and PubMed Central all have MCP tools. If an MCP tool
   has a gap (e.g. missing field), use a different MCP query pattern — do not
   bypass MCP.

2. **Prefer `snippet_search` over `get_europepmc_full_text`** for evidence
   gathering. Full text is fragile (silent failures, huge output). Snippet
   search returns pre-chunked, relevance-ranked text with reference annotations.

3. **CorpusId retrieval**: `snippet_search` is the canonical way to get
   CorpusIds via MCP. The response includes `paper.corpusId` in snippet
   metadata. For referenced papers within snippets, check
   `matchedPaperCorpusId`. Do not attempt to get CorpusId from `get_paper`
   fields — it is not available there.

4. **Batch paper lookups**: Use `get_paper_batch` early to pre-fetch metadata
   for all papers that will appear in the catalogue.

5. **Limit supplement fetch attempts**: Max 2 attempts for full text or
   supplement retrieval per paper. If both fail, move on to snippet search.

6. **Pre-extract JSON before grepping MCP output**: When MCP tools save
   large results as single-line JSON, use `python3 -c "import json..."` to
   extract and search — do not grep raw JSON files.

---

## Workflow Sequence

Given a **project name** and **cell type label**:

### 1. Load Project Config

Read `projects/{project}/cell_type_annotations.json`:
- Extract atlas DOI, title
- Validate the cell type label exists in annotations
- Get scope and granularity for the cell type
- **If scope indicates integrated external annotations** (e.g. adult annotations
  from Reynolds integrated into Gopee), identify the source atlas early and
  pivot supplementary fetching to that paper.

### 2. Fetch Supplementary Material

Use MCP tools directly (single call, no subagent needed):
1. `get_all_identifiers_from_europepmc(doi)` → get PMCID
2. `get_pmc_supplemental_material(pmcid)` → list available supplements
3. Fetch relevant supplement files (tables, figures with legends)

If supplements are unavailable (max 2 attempts), fall back to snippet search
with marker-focused queries. Try `get_europepmc_pdf_as_markdown` for
supplement PDFs as an alternative.

Store supplementary text for downstream steps.

### 3. Resolve Name → subagent: `resolve-name`

**Primary method**: Use `snippet_search` with `paper_ids` parameter scoped to
the atlas paper. This avoids fragile full text download → grep → parse cycles
and returns relevance-ranked text.

**Input:**
- `cell_type_label`, `atlas_doi`, `scope`
- `supplementary_text` from step 2
- `traversal_dir`: `projects/{project}/traversal_output/{cell_type}`

**Output:** `projects/{project}/traversal_output/{cell_type}/name_resolution.json`

**Contract:**
```json
{
  "label": "Iron-recycling macrophage",
  "resolved_names": ["Iron-recycling macrophage", "HRG+ macrophage"],
  "scope": "fetal",
  "tissue_context": "fetal skin",
  "confidence": "high",
  "evidence": "Found in cluster annotations table"
}
```

### 4. Parallel: Scan Supplements + Citation Traverse

These two steps are independent after name resolution. Run them in parallel.

#### 4a. Scan Supplements → subagent: `scan-supplements`

**Input:**
- `pmcid`, `cell_type_label`, `resolved_names`
- `supplementary_text` from step 2
- `traversal_dir`: `projects/{project}/traversal_output/{cell_type}`

**Output:** `projects/{project}/traversal_output/{cell_type}/supplementary_findings.json`

**Contract:**
```json
{
  "markers": [{"gene": "HRG", "evidence_type": "DE analysis", "source_table": "..."}],
  "other_findings": [{"finding": "...", "category": "function", "source_table": "..."}],
  "evidence_quotes": [{"quote": "exact text", "source_file": "...", "context": "..."}]
}
```

#### 4b. Citation Traverse → subagent: `citation-traverse`

**Input:**
- `seed_paper_id`: CorpusId from snippet metadata, or `DOI:{doi}`
- `query`: `"{label} / {resolved_name} in {scope} {tissue}: location, structure, function, markers"`
- `depth`: 1 (default), configurable up to 3
- `traversal_dir`: `projects/{project}/traversal_output/{cell_type}`

**Local snippet index (fresh preprints):** if
`projects/{project}/local_index/manifest.json` exists, the graph also calls
`services.citation_traverser.traverse_local` in parallel with the ASTA path
and merges results. Snippets carry `source_method: "local_snippet"`. See the
`local-paper-index` skill (`.claude/skills/local-paper-index/SKILL.md`) for
how to build the index when ASTA is blind to the atlas paper.

**Output:**
- `projects/{project}/traversal_output/{cell_type}/all_summaries.json`
- `projects/{project}/traversal_output/{cell_type}/paper_catalogue.json`

### 5. Synthesize Report → subagent: `synthesize-report`

**Input:**
- `traversal_dir`: `projects/{project}/traversal_output/{cell_type}`
- `reports_dir`: `projects/{project}/reports`
- `cell_type`: the cell type label

**Output:** `projects/{project}/reports/{cell_type}.md`

### 6. Validate Report (explicit step — not hook-dependent)

After the report is written, **always run validation explicitly**:

1. Read the report file and the evidence files (`all_summaries.json`,
   `paper_catalogue.json`, `supplementary_findings.json`).
2. Check that every blockquoted text (`> "..."`) is a substring of the
   evidence corpus.
3. Check that every DOI in the report exists in the paper catalogue.
4. If validation fails, pass the error list back to `synthesize-report` and
   retry (max 2 retries).

The validation logic lives in `src/atlas_chat/atlas_chat/validation/report_checker.py`.
You can invoke it directly:

```python
from atlas_chat.validation.report_checker import validate_report
passed, errors = validate_report(report_path, traversal_dir)
```

**Note:** The Claude Code write hook (`.claude/hooks/check_report_refs.py`) is
an *optional extra guard* for interactive sessions — it is NOT the primary
validation mechanism. The correction loop must work without it.

### 7. Map to Cell Ontology → subagent: `ontology-term-lookup`

After the report passes validation, map the cell type to the Cell Ontology.

**Input:**
- Report path from step 5
- Cell type label
- Output path: `projects/{project}/traversal_output/{cell_type}/cl_mapping.json`

**Output:** `projects/{project}/traversal_output/{cell_type}/cl_mapping.json`

The subagent searches OLS4 for CL terms, compares definitions against the
report content, and classifies the match as exact, broad, narrow, or none
using SKOS vocabulary. Output conforms to the JSON Schema at
`src/atlas_chat/atlas_chat/schemas/cl_mapping.schema.json` and is validated
by a PostToolUse hook.

### 8. Insert CL Mapping into Report Header

After the CL mapping JSON is written, insert the mapping metadata into the
report header block (between the title line and `## Summary`). Read
`cl_mapping.json` and add a `Cell Ontology` line:

- **Exact match:**
  `Cell Ontology: [basal cell of epidermis](http://purl.obolibrary.org/obo/CL_0002187) (CL:0002187, exact match)`
- **Broad match:**
  `Cell Ontology: [keratinocyte](http://purl.obolibrary.org/obo/CL_0000312) (CL:0000312, broad match — no exact CL term)`
- **No match:**
  `Cell Ontology: No CL term (new term needed)`

The PURL format is `http://purl.obolibrary.org/obo/CL_NNNNNNN` (underscore,
not colon).

### 9. Draft CL Term Request (conditional) → subagent: `cl-term-request`

**Only run this step if** `cl_mapping.json` has `"new_term_needed": true`.

**Input:**
- Report path from step 5
- CL mapping path from step 7
- Output path: `projects/{project}/traversal_output/{cell_type}/cl_term_request.json`

**Output:** `projects/{project}/traversal_output/{cell_type}/cl_term_request.json`

The subagent generates a draft new term request following:
- CL definition guidelines (`docs/LLM_prompt_guidelines_for_CL_definitions.md`)
- CL relations guide (`docs/relations_guide.md`)
- CL NTR issue template (`docs/cl_new_term_request_template.md`)

Output includes structured JSON (definition, parent, axioms, synonyms,
references) and a pre-rendered `ntr_markdown` field ready to paste into a
GitHub issue on `obophenotype/cell-ontology`. The JSON is validated by a
PostToolUse hook against the schema at
`src/atlas_chat/atlas_chat/schemas/cl_term_request.schema.json`.

### 10. Post CL Term Request to GitHub (conditional, requires confirmation)

**Only run this step if:**
- Step 9 produced a `cl_term_request.json`
- A GitHub token with `public_repo` scope is available
- The user explicitly confirms they want to post

**This step modifies an external shared repository. Always ask the user
before posting.** Show them the `ntr_markdown` content and the target repo
first.

**Authentication:** Pass the token via `GH_TOKEN` so the user's default `gh`
credentials are unaffected. The token must have `public_repo` scope.

**Procedure:**

1. Read `cl_term_request.json` and extract `suggested_label` and `ntr_markdown`.
2. Show the user the draft issue title and body for review.
3. On confirmation, post:

```bash
GH_TOKEN=$(grep ATLAS_CHAT_GH_TOKEN .env | cut -d= -f2) gh issue create \
  --repo obophenotype/cell-ontology \
  --title "[NTR] {suggested_label}" \
  --label "new term request" \
  --body "$ntr_markdown"
```

4. Record the returned issue URL in the report header, appending it to the
   Cell Ontology line:
   `Cell Ontology: ... (broad match — NTR: obophenotype/cell-ontology#NNN)`

**Never post without user confirmation.** This creates a public issue on an
external repository.

**Note:** A GitHub App-based alternative (`gh-app-post` CLI) is implemented
at `src/github_app_posting/` for future use — posts as a bot identity without
a personal token.

---

## Output Layout

```
projects/{project}/
├── cell_type_annotations.json
├── traversal_output/{cell_type}/
│   ├── name_resolution.json
│   ├── supplementary_findings.json
│   ├── all_summaries.json
│   ├── paper_catalogue.json
│   ├── cl_mapping.json
│   └── cl_term_request.json    (conditional — only if new_term_needed: true)
└── reports/
    └── {cell_type}.md
```

---

## Report Format

Reports use standard academic citation style. See the shared prompt at
`src/atlas_chat/atlas_chat/agents/report_synthesizer.prompt.yaml` for full
instructions. Key conventions:

- **Inline citations**: `(Author et al., Year)`
- **Blockquote evidence**: `> "exact quote"\n>\n> — Author et al. (Year)`
- **References**: standard academic format with DOI links

```markdown
# Iron-Recycling Macrophages in Prenatal Human Skin

## Summary
Iron-recycling macrophages are one of four macrophage subsets identified in
prenatal human skin by Gopee et al. (2024)...

## Markers
> "Iron-recycling macrophages: CD5L, APOE, VCAM, TIMD4, SLC40A1"
>
> — Gopee et al. (2024), Supplementary Materials

These markers reflect the subset's functional specialisation:
- **SLC40A1** (ferroportin) — the sole known cellular iron exporter...

## Location
### In prenatal skin
...

## Function
### 1. Endothelial cell chemotaxis
...

## References
- Gopee NH et al. (2024). "A prenatal skin atlas..." *Nature*. DOI: [10.1038/s41586-024-08002-x](https://doi.org/10.1038/s41586-024-08002-x)
- Suo C et al. (2022). "Mapping the developing human immune system..." *Science*. DOI: ...
```

---

## Validation Rules

Shared validation logic in `src/atlas_chat/atlas_chat/validation/report_checker.py`:

1. **Quote check**: Every blockquoted text (`> "..."`) must be a substring of
   the evidence corpus (all_summaries.json snippets + supplementary evidence +
   atlas full text).
2. **DOI check**: Every DOI in the report must appear in `paper_catalogue.json`.

The canonical correction loop is in Python (`report_graph.py` nodes
`SynthesizeReport` → `ValidateReport` → retry). Both runtimes use it:
- **Programmatic**: Graph validation node → routes back to synthesis with error list
- **Agentic**: Orchestrator calls validation explicitly after synthesis, feeds
  errors back to synthesize-report subagent for retry

The Claude Code write hook (`.claude/hooks/check_report_refs.py`) is an
**optional extra guard** — it catches problems in interactive sessions but is
not part of the required correction loop.

---

## Rules

- Do **not** write or modify source code unless the user explicitly asks.
- Do **not** run the test suite.
- Do **not** commit changes.
- All quotes in the final report must be traceable to traversal evidence files.
- Use the test cell type "Iron-recycling macrophage" (fetal scope) from the
  fetal_skin_atlas project for verification runs.
