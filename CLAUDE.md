# atlas-chat: Cell Type Report Generation

> **You are the orchestrator agent.** You coordinate subagents to produce
> evidence-grounded cell type reports from atlas papers.
> For development instructions, see `CLAUDE_dev.md`.

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

### 1. Load Project Config (CAS+)

The project config is a **CAS+** document at `projects/{project}/cas.json`
(schema: `src/atlas_chat/atlas_chat/schemas/cas_annotation.schema.json`). CAS+
supersedes the legacy flat `cell_type_annotations.json`.

- **If `projects/{project}/cas.json` exists and validates**, load it and move on.
- **Otherwise**, invoke the `generate-cas` skill
  (`.claude/skills/generate-cas/SKILL.md`) to build it from the project's
  source(s), asking the user for anything not derivable (DOI, organism, which
  column is the cell-type label). The `check_cas_annotation` PostToolUse hook
  enforces schema compliance on write.

From the loaded CAS+ document:
- Extract atlas DOI + title from `source`.
- Validate the requested cell type label exists as an annotation `cell_label`.
- Read its `labelset` (granularity) and context from `composition`
  (e.g. developmental stage / organism / tissue).
- **If any annotation carries `transferred_annotations`**, the project has
  integration provenance and step 3b applies: the label may have been inherited
  from a contributing study, in which case that study — not the atlas — is where
  the cell type was characterised, and supplementary fetching and traversal should
  both pivot to it.

> Migration note: downstream steps below still reference the legacy `label` /
> `scope` fields; their input contracts move to CAS+ `cell_label` / `composition`
> as part of the query-decomposer work.

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
- Cell type label, atlas DOI, scope
- Supplementary text from step 2

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

### 3b. Subatlas Contributors + Consistency (when the project has integration provenance)

Skip this step entirely if no annotation in `cas.json` carries
`transferred_annotations` — most single-study atlases won't.

Otherwise: an integrated atlas's cell sets are built from cells other studies
already annotated, and where a label was inherited, the biology was characterised
**upstream**. This step finds out which paper that is, and it runs before traversal
because it decides where traversal starts.

**3b(i). Apply the cutoff (deterministic, no subagent):**

```bash
uv run python -m atlas_chat.cli_contributors \
  --cas projects/{project}/cas.json \
  --cell-type "{cell_type}" [--labelset {labelset}] \
  --out projects/{project}/traversal_output/{cell_type}/subatlas_contributors.json
```

Defaults keep a contributor at ≥5% of the cell set and ≥50 cells, tier it
`primary` at ≥20%, and list its labels down to 2% of what it contributed. Override
per project if the numbers look wrong for it; the thresholds are recorded on the
output either way.

**3b(ii). Judge consistency → subagent: `subatlas-consistency`**

**Input:** per `subatlas_consistency_input.schema.json` — cell label, atlas DOI,
`contributors_path`, `cas_path`, `project_dir`, `output_path` (and
`name_resolution_path` from step 3, which sharpens the comparison).

**Output:** `projects/{project}/traversal_output/{cell_type}/subatlas_consistency.json`
— a SKOS verdict per contributor with its explanation, plus the `primacy` call
that step 4b consumes.

### 4. Parallel: Scan Supplements + Citation Traverse

These two steps are independent after name resolution. Run them in parallel.

#### 4a. Scan Supplements → subagent: `scan-supplements`

**Input:**
- PMCID, cell type label + resolved names
- Supplementary text from step 2

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

**Input:** per `citation_traverse_input.schema.json`.
- `seeds` — the papers to search at hop 0, **in priority order**. Take the order
  from step 3b's `primacy`:
  - `subatlas_primary` → that paper is seed priority 0, the atlas paper priority 1.
    It is where the cell type was characterised; searching the atlas first spends
    the run cap on a paper that only inherited the label.
  - `co_equal` → the atlas paper plus every paper in `co_equal_papers`.
  - `atlas_primary`, or no step 3b at all → the atlas paper alone.
  Set each seed's `retrieval` from its registry entry in `source.subatlas_papers`:
  `local` for `status: local` (ASTA holds too little of it to quote — that is why
  it was built locally), `asta` otherwise.
- Query: `"{label} / {resolved_name} in {scope} {tissue}: location, structure, function, markers"`
- Depth: 1 (default), configurable up to 3

**Local snippet index:** the agentic route reaches it through
`cli_annotate fetch --local --project-dir ... --papers <DOI>`, which produces the
same records as the ASTA path. Use it for any seed whose registry `status` is
`local`. See the `local-paper-index` skill
(`.claude/skills/local-paper-index/SKILL.md`) for building the corpus. (The
deprecated graph does the same merge via
`services.citation_traverser.traverse_local`.)

**Output:**
- `projects/{project}/traversal_output/{cell_type}/all_summaries.json`
- `projects/{project}/traversal_output/{cell_type}/paper_catalogue.json`

### 5. Synthesize Report → subagent: `synthesize-report`

**Input:** Reads all output files from steps 3-4, including
`subatlas_contributors.json` and `subatlas_consistency.json` where step 3b ran.
Those drive an "Annotation provenance and subatlas consistency" section and, where
`primacy` is `subatlas_primary`, which paper is cited as the primary source.

**Output:** `projects/{project}/reports/{cell_type}.md`

### 6. Validate Report (explicit step — not hook-dependent)

After the report is written, **always run validation explicitly**:

1. Read the report file and the evidence files (`all_summaries.json`,
   `paper_catalogue.json`, `supplementary_findings.json`).
2. Check that every blockquoted text (`> "..."`) is a substring of the
   evidence corpus.
3. Check that every DOI in the report exists in the paper catalogue.
3b. Where `subatlas_consistency.json` gives `primacy: subatlas_primary`, check
   that paper's DOI is both in the catalogue and in the report
   (`check_defining_paper`). A report that omits the paper its cell type comes
   from is the failure this catches.
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
│   ├── subatlas_contributors.json   # if the project has integration provenance
│   ├── subatlas_consistency.json    #   "
│   ├── supplementary_findings.json
│   ├── all_summaries.json
│   └── paper_catalogue.json
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
3. **Defining-paper check**: where `subatlas_consistency.json` names a
   `subatlas_primary` paper, its DOI must be in the catalogue *and* in the report.
   Reaching the paper and actually citing it are different failures, so both are
   checked.

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
