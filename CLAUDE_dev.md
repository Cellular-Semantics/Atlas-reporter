# atlas-chat — Developer Guide (agentic workflows & skills)

**How to build and extend this project's agentic workflow, skills, and supporting code.**

> **This is the dev-mode guide. Load it explicitly when doing development work.**
> The default session loads `CLAUDE.md` (the run/content workflow). This file is
> for *building* the workflow — its skills, subagents, schemas, validators, and
> the Python utilities they call.

> **Deprecated — programmatic path.** This project began with a parallel
> **programmatic** PydanticAI graph (`src/.../graphs/`, the `atlas-report` CLI in
> `cli.py`). That path is deprecated and retained for reference / regression
> comparison only. **Build new functionality as agentic orchestrations (skills /
> subagents), not as graph nodes.** See "Deprecated: programmatic path" at the end.

---

## Schema-first commandment

**JSON Schema is the single source of truth.** Define the shape as a JSON Schema
file under `src/atlas_chat/atlas_chat/schemas/`, then generate Pydantic models from
it — never hand-write a Pydantic model that duplicates a schema.

```python
# 1. Define JSON schema (schemas/*.schema.json) — source of truth
# 2. Generate a Pydantic model from it (cellsem-llm-client utilities)
Model = create_model_from_json_schema(schema)
# 3. Validate / correct structured output
result = Model.model_validate(llm_output)            # strict
result = Model.model_validate(llm_output, strict=False)  # drop extras with warning
```

Load schemas with the existing helper rather than re-reading files:

```python
from atlas_chat.schemas import load_schema
schema = load_schema("cl_mapping.schema.json")
```

**Schema principles:**
- `additionalProperties: false` on objects — reject drift.
- Separate domain (biology) shapes from business/process shapes.
- Reuse components; the validation package imports from `atlas_chat.schemas`, never
  re-declares.

Current schemas: `cl_mapping.schema.json`, `cl_term_request.schema.json`,
`cell_type_annotation.schema.json`, `run_provenance.schema.json`,
`ontology_lookup_input.schema.json` (+ `example_*` / `workflow_output` placeholders).

---

## Modular orchestrations with declared shapes

The agentic workflow is built from small, composable **orchestration units** — a
`.claude` skill (`.claude/skills/*/SKILL.md`) or subagent (`.claude/agents/*.md`).
Each unit **declares its contract in YAML front-matter**: the input object it
expects and the output object it produces. Shapes are not described in prose —
they **reference declared JSON Schemas** (the schema-first commandment above).

```yaml
---
name: ontology-term-lookup
description: ...
model: sonnet
input:
  schema: src/atlas_chat/atlas_chat/schemas/ontology_lookup_input.schema.json
output:
  schema: src/atlas_chat/atlas_chat/schemas/cl_mapping.schema.json
---
```

**Why:**
- **Composability** — the output of one orchestration is the typed input of the
  next. The workflow in `CLAUDE.md` is a sequence of these contracts
  (name_resolution → supplementary_findings + all_summaries → report → cl_mapping
  → cl_term_request).
- **Enforced at the boundary** — a `PostToolUse` hook validates the produced object
  against the named **output** schema (e.g. `check_cl_mapping.py` →
  `cl_mapping.schema.json`, `check_cl_term_request.py` →
  `cl_term_request.schema.json`). Add a validator hook whenever you add an output
  schema, and register it in `.claude/settings.json`.
- **Discoverable** — `grep -rn "schema:" .claude/agents .claude/skills` lists every
  contract in the workflow.

**Conventions:**
- One orchestration = one clear input shape + one output shape. If a unit needs two
  unrelated outputs, it is probably two orchestrations.
- Input schema name mirrors the unit: `{unit}_input.schema.json`. Output schema is
  the domain object it yields.
- `ontology-term-lookup` is the worked exemplar. **Retrofitting the remaining
  subagents and skills (`resolve-name`, `scan-supplements`, `citation-traverse`,
  `synthesize-report`, `cl-term-request`, and the `.claude/skills/*`) with
  `input:`/`output:` front-matter and matching schemas is follow-up work** — do it
  as you touch each one.

---

## Testing

### Test-driven where it pays

**Use TDD for:** parsers, validators, data transformers (clear in/out); bug fixes
(red → green → refactor); core domain logic once understood.

**Skip TDD for:** exploratory prototypes, prompt-strategy spikes, first-cut API
integration. Exploratory work lives in `experiments/` (excluded from coverage,
mypy, ruff; not subject to TDD).

### Required test structure

```
tests/
├── unit/          # fast, isolated, no external deps   (@pytest.mark.unit)
├── integration/   # REAL external services              (@pytest.mark.integration)
└── conftest.py
```

- **Every test carries a marker** (`@pytest.mark.unit` / `@pytest.mark.integration`).
- **Integration tests use real APIs** — no mocks, no simulated responses. They must
  **fail hard** if credentials are missing (not skip), so quirks surface immediately.
- **CI runs unit tests only** (`uv run pytest -m unit`); integration runs locally.

### Regression tests for validation

The validation logic and orchestration contracts are the project's quality
backbone — they need a **growing regression suite** that pins behaviour as the
workflow evolves:

- **Schema regression** — for each output schema, keep good/bad golden fixtures and
  assert the schema (and any cross-field rules) accept/reject them. The CL-mapping
  baseline lives in `tests/unit/test_cl_mapping_schema.py`: it validates fixtures
  against `cl_mapping.schema.json` and checks the `match_type ↔ skos_mapping` and
  `new_term_needed` consistency rules enforced by `check_cl_mapping.py`. Extend this
  pattern for `cl_term_request` and each new contract.
- **Hook regression** — `tests/unit/test_curation_guard.py` pins the curation-mode
  write gate (allow `projects/` + `planning/`, block everything else, developer
  override). Drive hooks via subprocess with `ATLAS_CHAT_HOOK_USER` set.
- **Report-validation regression** — `validate_report()` and its pure helpers
  (`check_quotes`, `check_references` in `report_checker.py`) are the contract for
  quote/reference grounding; assert their behaviour on known inputs (see ROADMAP
  "Golden-data regression").

These run in CI and must pass before merge. When you change an orchestration's
output or a validator, update the golden fixtures in the same commit.

### Coverage targets

Commits must pass `pytest --cov` above the floor set in `pyproject.toml`
(`fail_under`). Ratchet the floor up as tests are added; do not lower it. Integration
tests are excluded from CI but count locally.

### Commands (uv)

```bash
uv sync --dev                     # install deps incl. dev tools
uv run pytest                     # all tests
uv run pytest -m unit             # unit only (CI)
uv run pytest -m integration      # integration (local, needs API keys)
uv run pytest --cov               # with coverage
uv run mypy src/                  # type check
uv run ruff check --fix src/ tests/
uv run ruff format src/ tests/
uv run pre-commit run --all-files
python scripts/check-docs.py      # build & check docs
```

---

## Code quality

Pre-commit hook runs automatically on each commit:

```bash
uv run ruff check --fix src/ tests/      # lint (blocks commit)
uv run ruff format --check src/ tests/   # format (blocks commit)
uv run pytest -m unit --cov              # unit + coverage floor (blocks commit)
uv run mypy src/                         # type check (encouraged locally; CI only initially)
```

---

## Environment configuration

Always bootstrap with dotenv; never hardcode secrets or commit `.env`.

```python
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("SOME_API_KEY")
```

**Precedence:** explicit constructor args → environment (`.env`) → sensible defaults.

---

## Documentation

Google-style docstrings with RST code blocks (`.. code-block:: python`, not markdown
backticks). Auto-generated API docs (Sphinx + AutoAPI); manual guides in `docs/`
(MyST markdown). Run `python scripts/check-docs.py` before committing.

---

## Repository structure

```
atlas-chat/
├── CLAUDE.md            # default: run/content workflow (the orchestrator's instructions)
├── CLAUDE_dev.md        # this file: developer guide
├── .claude/
│   ├── settings.json    # hooks (curation guard + validators), permissions, MCP servers
│   ├── agents/          # subagents — orchestration units (declare input/output shapes)
│   ├── skills/          # skills — orchestration units (declare input/output shapes)
│   ├── commands/        # /run-workflow etc.
│   └── hooks/           # curation_guard.py + check_*.py output validators
├── src/
│   └── atlas_chat/atlas_chat/
│       ├── schemas/     # JSON schemas — source of truth
│       ├── agents/      # *.prompt.yaml canonical prompts
│       ├── services/    # API integrations (e.g. local_snippet_index, fetch_preprint)
│       ├── validation/  # report_checker.py and cross-cutting validators
│       ├── utils/
│       └── graphs/      # DEPRECATED programmatic PydanticAI graph (reference only)
├── projects/            # CONTENT — per-atlas reports & traversal output (curation zone)
├── planning/            # notes, postmortems, dev requests (curation zone)
└── tests/{unit,integration}/
```

Prompts are co-located with the code/agents that use them, always as `*.prompt.yaml`
(`find . -name "*.prompt.yaml"`; review with `git diff '**/*.prompt.yaml'`).

---

## Curation-mode hook (how it works)

The default session is curation/content mode. `.claude/hooks/curation_guard.py`
(`PreToolUse` on `Edit|MultiEdit|Write`, registered in `.claude/settings.json`) lets
non-developer users write **only** under `projects/` and `planning/`, and blocks
everything else (`src/`, `.claude/`, schemas, docs, root files, anything outside the
repo). The repo developer is recognised by `git config user.email` (in `TRUSTED_USERS`)
and bypasses the gate; tests override the identity via `ATLAS_CHAT_HOOK_USER`. To do
dev work you either have the trusted git identity or run an explicit dev session.

---

## Forbidden / required

**Never:**
- ❌ Mock or simulate responses in integration tests (use real APIs).
- ❌ Skip tests with `pytest.mark.skip` (fix or remove).
- ❌ Build generic abstractions before a specific case works.
- ❌ Rewrite working code without a documented reason.
- ❌ Add new functionality to the deprecated programmatic graph.

**Required:**
- ✅ Real integration tests from day 1.
- ✅ Every orchestration declares input/output shapes referencing JSON Schemas.
- ✅ A validator hook for every output schema, registered in `.claude/settings.json`.
- ✅ Regression fixtures updated in the same commit as a contract/validator change.
- ✅ Extend existing code in preference to rewriting.

---

## Decision checklist (before writing production code)

- [ ] Is the data shape captured as a JSON Schema (source of truth)?
- [ ] Does the orchestration declare `input:`/`output:` front-matter pointing at schemas?
- [ ] Is there an output-validator hook + regression fixture?
- [ ] Have we tested the real external API (integration test first)?
- [ ] Can we extend existing code instead of rewriting?

---

## Deprecated: programmatic path

Retained for reference and regression comparison only — **do not extend**:

- `src/atlas_chat/atlas_chat/cli.py` — the `atlas-report` console script.
- `src/atlas_chat/atlas_chat/graphs/` — `report_graph.py`, `graph_agent.py`,
  `definitions.py` (PydanticAI graph orchestration, `pydantic-graph`).
- `deep-research-client` usage tied to the graph path.

New orchestration goes in `.claude/agents/` and `.claude/skills/` as units with
declared shapes (above). Note: `services/local_snippet_index.py` and
`services/fetch_preprint.py` are **not** part of the deprecated path — they back the
agentic `local-paper-index` skill and remain supported.
