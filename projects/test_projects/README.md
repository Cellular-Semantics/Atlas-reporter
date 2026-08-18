# Test projects

Sandbox projects for exercising the report-generation workflow end-to-end, kept
**separate from official reports** (which live on their own per-atlas project
branches). Nothing here is an authoritative report.

## What is committed vs generated

For each test project `test_projects/<name>/`:

- **Committed setup** (tracked): `cas.json` (the CAS+ config the run reads) and this
  project's `README.md` / any small source notes.
- **Generated output** (git-ignored): `traversal_output/`, `reports/`, `selections/`,
  and `runs/`. See `.gitignore`. Only the setup needed to reproduce a run is tracked.

## Running a test

Launch a session **inside this worktree** (agents load from the launch dir's
`.claude/`), then drive the workflow with the project addressed under this folder:

```
project = "test_projects/<name>"     # orchestrator reads projects/test_projects/<name>/cas.json
query   = "<free-text cell-type selection>"   # e.g. "all macrophages"
```

## Run tracking

Each test run writes a manifest to `runs/<UTC-timestamp>/run.json` (git-ignored)
recording the **directory it was run in** and the **nature of the run**:

```jsonc
{
  "run_id": "<uuid>", "timestamp": "<ISO-8601 UTC>", "mode": "agentic",
  "worktree_dir": "<abs path the run was driven from>",
  "git_branch": "...", "git_version": "<git describe --always --dirty>",
  "project": "test_projects/<name>", "query": "<the query>",
  "selected_cell_types": ["..."],
  "outputs": ["traversal_output/...", "reports/..."],
  "notes": "<what this run was testing>"
}
```

(This is a lightweight, test-scoped record. The heavier infra standard is
`src/atlas_chat/atlas_chat/schemas/run_provenance.schema.json` — align to it later
if test runs need to feed the validation-tools run-comparison.)
