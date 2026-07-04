# Plan: Improve Project Initialization & First-Run Orientation

Date: 2026-06-22
Author: do12 (drafted via curation-mode session)

## Context

The README's documented starting point is `/run-workflow`, which immediately
asks "What input do you have?" — it presupposes a `projects/{name}/` directory
with a hand-authored `cell_type_annotations.json` already in place. There is
**no documented path from "I have an atlas / zarr URL / DOI" to "I have a
runnable project"**, and nothing orients a user who starts Claude in a fresh
clone with no projects.

### Current state of initialization (as audited)

- A "project" = a directory under `projects/{name}/` whose only required input
  is `cell_type_annotations.json` (schema: `src/atlas_chat/atlas_chat/schemas/
  cell_type_annotation.schema.json`; requires `source.doi` + `annotations[]`).
- Only one project exists: `fetal_skin_atlas`.
- Three relevant entry mechanisms exist but are **disconnected**:
  - `/run-workflow` (`.claude/commands/run-workflow.md`) — assumes annotations
    already exist. The only path the README advertises.
  - `anndata-zarr-summary` skill — the *actual* ingestion tool (zarr `obs/` →
    `cell_type_annotations__<col>.json`). **Undiscoverable**: not referenced in
    README, CLAUDE.md, or run-workflow.
  - `/load-project-context` skill — loads an *existing* project's evidence.
    Undocumented in README.
  - `local-paper-index` skill — for preprints / closed-access papers; expects a
    `label_provenance.json` that the zarr skill does not currently emit.
- **No SessionStart hook** and no empty-state detection anywhere.

### Confirmed gaps

1. README documents the wrong front door (`/run-workflow` before a project
   exists).
2. No first-run / empty-state orientation.
3. Ingestion is fragmented and schema-mismatched (see "Known gaps", below) —
   even the good path (`anndata-zarr-summary`) emits a file the user must
   hand-edit before `/run-workflow` works, and nothing says so.
4. No single "front door" tying the on-ramps together.

### Decisions taken (user, 2026-06-22)

- **Surfacing:** add a **SessionStart hook (auto)** that detects the empty /
  uninitialized state and prints orientation text.
- **Ingestion scope:** **document the current (imperfect) flow now**, including
  the manual DOI/scope edit step; defer reconciling the zarr-skill output with
  the canonical schema to a follow-up.

### Execution constraint

All target files (README.md root, `.claude/` hook + settings, `src/` skill) are
**blocked under curation mode** for the current user (allowlist = `projects/`,
`planning/` only). **This plan must be executed from a dev-mode session**
(`CLAUDE_dev.md`). Note the guard's denylist blocks `.claude/`, `src/`, `tests/`
even for trusted users via the curation settings — the SessionStart hook +
settings edit must be made with the curation hook disabled (i.e. a genuine dev
session, not just a trusted user).

---

## Goal

One canonical "from nothing → runnable project" narrative that serves **double
duty**: (a) the README's Quick Start, and (b) the text a SessionStart hook shows
when no valid project exists. Single source of truth, no drift.

---

## Part A: Single source of truth — `docs/getting-started.md`

Create `docs/getting-started.md` as the canonical orientation doc. Both the
README and the SessionStart hook point to it (README links + inlines the short
version; hook prints a short pointer + the path).

Contents:

1. **What a project is** — a `projects/{name}/cell_type_annotations.json`; the
   workflow generates everything else.
2. **The three on-ramps**, as an explicit decision tree:
   - **Path A — from an AnnData-zarr URL** (recommended when the atlas is
     published as zarr): run `anndata-zarr-summary <url>`, then **manually
     edit** the output (fill real `source.doi`/`title`; the output's `source`
     uses `zarr_url`/`obs_column` and annotations lack `scope`/`granularity` —
     add what you need). Move/rename to
     `projects/{name}/cell_type_annotations.json`.
   - **Path B — from a DOI only**: author `cell_type_annotations.json` by hand
     from the template (below).
   - **Path C — preprints / closed-access**: after A or B, build a local
     snippet corpus with the `local-paper-index` skill so the citation traverse
     has text to work on.
3. **Minimal valid template** (copy-paste), matching the schema exactly.
4. **Then run it:** `/run-workflow` (or `/load-project-context {name}` to resume).
5. **The manual-edit caveat**, called out explicitly (the deferred schema fix).

## Part B: README rewrite

Rewrite README "Quick Start" + "Project Configuration" so the flow is:
Install → **Initialize a project** (link to `docs/getting-started.md`, inline
the decision tree + template) → `/run-workflow`. Add `anndata-zarr-summary` and
`local-paper-index` to a short "Tooling for setup" subsection so they are
discoverable. Keep the existing schema/output sections.

## Part C: SessionStart hook — `.claude/hooks/session_orientation.py`

New hook that:
- Scans `projects/` for any subdir containing a parseable
  `cell_type_annotations.json` with a non-empty `annotations` array and a
  `source.doi`.
- **If none found** → print the short orientation block to stdout (pointer to
  `docs/getting-started.md`, the decision tree in 3–4 lines, the template path).
- **If projects exist** → optionally print a one-line "N projects available:
  ..." summary, or stay silent (decide during impl; lean toward a terse
  one-liner so it is not noisy).
- Register under `SessionStart` in `.claude/settings.json`.
- Keep it read-only and fast; no network.

Open question for impl: SessionStart hooks fire on every session including
dev/workflow sessions — make the empty-state message clearly skippable/short so
it does not clutter `/run-workflow` sessions where a project already exists.

## Part D: Cross-link the skills

- `run-workflow.md`: add a pre-flight line — "If no project exists yet, see
  `docs/getting-started.md` (or the SessionStart orientation)."
- `anndata-zarr-summary` SKILL: add a "Next step" pointer to the manual edit +
  `/run-workflow`.

---

## Known gaps / deferred follow-ups (NOT in this plan)

Tracked here so the schema reconciliation is not lost:

1. **`anndata-zarr-summary` output ≠ canonical schema.**
   - `source` is `{zarr_url, obs_column, doi:null, title:null, _note_to_user}`
     vs schema's required `source.doi` (+ `title`).
   - Annotations carry `n_cells` + covariate fields but **no `granularity` /
     `scope`** (the workflow expects these).
   - Result: output is not directly runnable; requires manual editing.
   - **Follow-up:** make the skill emit schema-conformant output (prompt for /
     accept a DOI; infer or prompt for scope/granularity; drop extra fields or
     park them in a sibling `co_annotations.json`).
2. **`label_provenance.json`** is consumed by `local-paper-index` but not
   produced by `anndata-zarr-summary` — the Path C handoff is manual. Consider
   emitting it from the zarr skill.
3. Consider a single guided "init project" flow (DOI or zarr URL → valid
   annotations) once the schema is reconciled.

---

## Execution checklist (dev-mode session)

- [ ] Create `docs/getting-started.md` (Part A).
- [ ] Rewrite README Quick Start + Project Configuration (Part B).
- [ ] Add `.claude/hooks/session_orientation.py` + register SessionStart in
      `.claude/settings.json` (Part C).
- [ ] Cross-link `run-workflow.md` and `anndata-zarr-summary` SKILL (Part D).
- [ ] Verify hook fires correctly on (a) fresh clone with no projects, (b) repo
      with `fetal_skin_atlas` present.
