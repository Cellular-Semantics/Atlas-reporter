# Plan: Project Initialization, Multi-Source Ingestion & First-Run Guidance

Date: 2026-06-23 · Author: do12 (dev-mode planning)
Supersedes/extends: `planning/plan_project_initialization_2026-06-22.md`

## Context

Today the only real on-ramp to a runnable project is: hand-author
`projects/{name}/cell_type_annotations.json`, then `/run-workflow`. The
`anndata-zarr-summary` skill can pull annotations from a published AnnData-zarr,
but its output is **not schema-conformant** (no `doi`/`scope`/`granularity`) and
is undiscoverable. There is no documented path from "I have an atlas / dataset /
spreadsheet / DOI" → "I have a project", no first-run orientation, and no naming
or git-branch handling at init time.

We are adding a single **`/init-project`** front door that names the project,
auto-branches off `main`, and routes several input sources through deterministic
loaders that all converge on one schema-valid `cell_type_annotations.json`. We
also reconcile the schema with what `local-paper-index`/`subatlas_resolver`
already expect (`source.subatlas_papers`), and ship the docs + SessionStart
orientation from the prior plan.

**Decisions (user, 2026-06-23):**
- **Scope:** framework + priority sources now (local h5ad/zarr, CELLxGENE,
  spreadsheet, DOI/paper-only). **CAP = documented stub**, follow-up.
- **Architecture:** hybrid — deterministic loaders as tested
  `src/atlas_chat/atlas_chat/services/` modules + a thin `/init-project`
  orchestration command/skill.
- **APIs:** research CELLxGENE Discover + CAP public APIs during implementation;
  pick example datasets for integration tests.
- **Init UX:** new `/init-project` command; prompt for name; if on `main`,
  `git checkout -b project/{name}`; create `projects/{name}/`; route by source;
  emit `cell_type_annotations.json`; point to `/run-workflow`.

**Execution constraint:** all targets (`src/`, `.claude/`, `docs/`, root
`README.md`, `pyproject.toml`) are blocked by `curation_guard.py` in curation
mode. **Must run in a genuine dev-mode session** (trusted git identity +
curation hook not active). Do not commit unless asked.

---

## Architecture: one convergence point

Every source produces the same artifact via a single shared writer:

```
source → loader (intermediate) → annotations_writer → cell_type_annotations.json (schema-valid)
                                                     → co_annotations.json (sibling, full covariate detail)
                                                     → label_provenance.json (when obs gives study columns)
```

- **Intermediate** (in-process dict, not persisted): `{labels: [{label, n_cells,
  covariates}], source_meta: {...}}`.
- **`annotations_writer`** is the ONLY thing that writes the canonical file. It
  fills `source` (doi/title/provenance), maps covariates → optional
  `scope`/`granularity` where inferable, parks full covariate distributions in
  `co_annotations.json`, and validates against the schema before writing.

This keeps loaders simple and guarantees schema conformance in one place.

---

## Part 0: Schema reconciliation (source of truth first)

Edit `src/atlas_chat/atlas_chat/schemas/cell_type_annotation.schema.json`:

1. **`source.subatlas_papers`** (new, optional array). Pin the shape already
   written by `subatlas_resolver.discover()` (`subatlas_resolver.py:209-222`):
   `{label, first_author, year, venue, total_cells, doi, status, proposed_doi?,
   proposed: [{doi,title,year,corpus_id,venue}]}`. This removes existing
   schema↔code drift (`local_snippet_index.py:1196`, `subatlas_resolver.py:346`
   already read this field).
2. **`source.local_text_path`** (new, optional string) — path to a local
   full-text file for the primary atlas paper (the "primary atlas paper: local
   text + DOI" case).
3. **`source.data_provenance`** (new, optional object) — where annotations came
   from: `{source_type: enum[manual, published_zarr, local_h5ad, local_zarr,
   cellxgene, cap, spreadsheet], dataset_id?, source_url?, file_path?,
   obs_column?, n_cells_total?, extracted_at?}`.
4. **`CellTypeAnnotation`**: add optional `n_cells` (integer). Keep
   `granularity`/`scope` optional. Do **not** set `additionalProperties:false`
   on the annotation object yet (covariate keys vary); full detail lives in
   `co_annotations.json`.
5. Keep `source.doi` **required** — the report workflow depends on it. Loaders
   that can't auto-resolve a DOI must prompt for one (init flow handles this).

No PostToolUse validator hook exists for this schema today; add a small
regression test instead (below) rather than a new hook, to match the existing
`test_cl_mapping_schema.py` pattern.

---

## Part 1: `/init-project` flow

**New files:**
- `.claude/commands/init-project.md` — entry command.
- `.claude/skills/init-project/SKILL.md` — orchestration contract (declare
  input/output front-matter per `CLAUDE_dev.md` modular-orchestration rules).

**Behaviour:**
1. Prompt for **project name** (validate: slug-safe; error if
   `projects/{name}/` already exists).
2. **Git branch:** detect current branch via `git rev-parse --abbrev-ref HEAD`.
   If `main`, run `git checkout -b project/{name}`. If already on a non-main
   branch, stay and note it. (Read-only check + one mutating git command,
   gated behind the name prompt.)
3. `mkdir -p projects/{name}/`.
4. Ask **source type** and gather the needed input:
   - **local h5ad / zarr** → path
   - **published AnnData-zarr URL** → existing `anndata-zarr-summary` skill
   - **CELLxGENE** → dataset id / URL
   - **CAP** → (stub: explain not-yet-supported, fall back to manual/DOI)
   - **spreadsheet** → csv/xlsx path (+ column mapping)
   - **DOI / paper-only** → DOI(s) + optional local text path
5. Invoke the matching loader (Bash → `uv run python -m
   atlas_chat.services.<loader>` or the zarr skill), producing
   `cell_type_annotations.json` via `annotations_writer`.
6. Validate the result; if a DOI is missing, prompt and patch `source.doi`.
7. If subatlas papers are wanted → point to `local-paper-index`
   (`discover-subatlas` → review → `init-corpus`).
8. Print next steps: `/run-workflow` (or `/load-project-context {name}`).

---

## Part 2: Loaders (hybrid: tested services + thin orchestration)

All new modules under `src/atlas_chat/atlas_chat/services/`, each returning the
**intermediate** and delegating the write to `annotations_writer`.

- **`annotations_writer.py`** (shared, build first) — intermediate → schema-valid
  `cell_type_annotations.json` + `co_annotations.json` + optional
  `label_provenance.json`. Validates via `from atlas_chat.schemas import
  load_schema` + `jsonschema`. Unit-tested with good/bad fixtures.
- **`anndata_loader.py`** — local `.h5ad` (anndata/h5py) and local `.zarr`
  (zarr/anndata): read `obs/` only, auto-pick cell-type column + covariates
  (reuse the candidate-column heuristics documented in the `anndata-zarr-summary`
  SKILL, §3–4). Mirrors the zarr skill's logic for the local case.
- **`cellxgene_loader.py`** — CELLxGENE Discover **curation API** (base
  `https://api.cellxgene.cziscience.com/curation/v1/`; collections carry `doi`,
  datasets expose H5AD download `assets`). Flow: dataset/collection id →
  resolve `doi` + H5AD asset URL → download → `anndata_loader` → intermediate
  with `source.doi` + `data_provenance.source_type="cellxgene"`. Uses `httpx`
  (already an inline dep in `subatlas_resolver.py`). Confirm exact endpoint
  paths against the live Swagger during impl.
- **`spreadsheet_loader.py`** — csv/xlsx (pandas + openpyxl). Column mapping:
  `label` (required), optional `granularity`, `scope`, `n_cells`. Auto-detect
  header; surface detected columns for confirmation. Unit-tested (no network).
- **`cap_loader.py`** — **stub** module + docstring documenting the CAP / CAS
  (cellannotation.org) approach and that it's deferred; raises a clear
  `NotImplementedError` with guidance to use manual/DOI for now. Add a
  follow-up note (below).
- **paper-only / DOI** — no new loader; init flow writes a minimal
  `cell_type_annotations.json` (`source.doi` + optional `local_text_path` +
  empty/seed `annotations`) from the template, then user adds annotations or
  runs `local-paper-index`.

**Dependencies** — add optional extra to `src/atlas_chat/pyproject.toml`:
```toml
[project.optional-dependencies]
data-sources = ["anndata>=0.10", "zarr>=2.18", "h5py>=3", "pandas>=2", "openpyxl>=3.1", "httpx>=0.27"]
```
Keep heavy readers behind the extra (lazy import inside loaders, like the
`local-index` extra). Document `uv sync --extra data-sources`.

---

## Part 3: Docs, README & first-run orientation

(From the 2026-06-22 plan, expanded for the new sources.)

- **`docs/getting-started.md`** (new) — canonical "from nothing → runnable
  project" doc. Decision tree across all on-ramps (local h5ad/zarr · published
  zarr URL · CELLxGENE · spreadsheet · DOI/paper-only · CAP=later), the
  `/init-project` flow, the minimal template, the subatlas-papers step, and the
  manual-edit caveats. Single source of truth.
- **`README.md`** — rewrite Quick Start: Install (incl. `--extra
  data-sources`) → **Initialize a project** (`/init-project`, link to
  getting-started, inline decision tree + template) → `/run-workflow`. Add a
  short "Setup tooling" subsection listing `init-project`,
  `anndata-zarr-summary`, `local-paper-index` so they're discoverable. Update
  the Project Configuration section to show `subatlas_papers` /
  `data_provenance`.
- **`.claude/hooks/session_orientation.py`** (new, SessionStart) — scan
  `projects/` for a parseable `cell_type_annotations.json` with non-empty
  `annotations` + `source.doi`. None → print short orientation (pointer to
  `docs/getting-started.md` + `/init-project` + template path). Some → terse
  one-line "N projects: ...". Read-only, fast, no network. Register under
  `SessionStart` in `.claude/settings.json`.
- **Cross-link skills:** `run-workflow.md` pre-flight line ("no project yet? →
  `/init-project` / getting-started"); `anndata-zarr-summary` SKILL "Next step"
  pointer; ensure its output path is schema-conformant or routes through
  `annotations_writer`.

---

## Testing

Per `CLAUDE_dev.md` (unit + real integration, markers required, CI = unit only):
- **Unit:** `annotations_writer` (good/bad fixtures → schema accept/reject),
  `spreadsheet_loader` (csv + xlsx fixtures), schema regression for the new
  `subatlas_papers`/`data_provenance` shapes (extend the
  `test_cl_mapping_schema.py` pattern), `session_orientation.py` empty vs.
  populated `projects/` (subprocess, like `test_curation_guard.py`).
- **Integration (local, real API):** `cellxgene_loader` against a chosen public
  dataset id — must fail hard if unreachable, no mocks; `anndata_loader` against
  a small real local `.h5ad`/`.zarr` fixture.
- Keep the coverage floor; ratchet up.

## Verification (end-to-end)

1. Dev session on a fresh-ish state; run `/init-project`:
   - name → confirm branch `project/{name}` created off `main`.
   - **spreadsheet** path → valid `cell_type_annotations.json` written + passes
     `jsonschema`.
   - **CELLxGENE** path → DOI + annotations populated from a real dataset.
   - **local h5ad** path → obs-derived annotations.
2. `uv run pytest -m unit` green; `uv run pytest -m integration` (with keys)
   green locally.
3. SessionStart: new clone w/ no projects prints orientation; repo with
   `fetal_skin_atlas` prints the terse one-liner.
4. `/run-workflow` consumes an init-produced project unchanged (regression
   against `fetal_skin_atlas`).

## Deferred follow-ups

- **CAP loader** — implement CAS/cellannotation.org ingestion (stub → real).
- Fully retire `anndata-zarr-summary`'s bespoke output by routing it through
  `annotations_writer` (or have it emit schema-valid directly).
- Auto-emit `label_provenance.json` from obs study columns in every anndata path
  (closes the manual Path-C handoff to `local-paper-index`).
- Consider a PostToolUse validator hook for `cell_type_annotation.schema.json`.
