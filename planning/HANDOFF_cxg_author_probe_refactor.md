# HANDOFF: refactoring cxg-author-probe (start here)

**For:** a fresh session doing the upstream cxg-author-probe refactor.
**Written:** 2026-07-04. **Run this session FROM `Atlas-reporter_too/`** (not from
inside the cxg-author-probe repo) so you inherit this repo's `planning/` + memory
+ the editable `_codev/` checkout. Memory is keyed to this repo's path; a session
started inside cxg-author-probe sees none of it.

---

## Goal (one line)

Move CAS(+) production + obs/reader flexibility UPSTREAM into cxg-author-probe so
its job = "any dataset → CAP+ annotation collection", leaving atlas-reporter to
**map + report** on cell-type annotations (it CONSUMES a CAP+ doc as input).

## Re-establish the co-dev setup FIRST (state not committed)

The editable override was reverted before the last commit (so `main` stays
clean). To make `_codev` edits live in this repo's env again:

1. Confirm the checkout exists: `_codev/cxg-author-probe/` (gitignored, at SHA
   `ea4d9b0`). If missing: `git clone https://github.com/Cellular-Semantics/cxg-author-probe.git _codev/cxg-author-probe`.
2. Re-add the editable override to ROOT `pyproject.toml` `[tool.uv.sources]`:
   `cxg-author-probe = { path = "_codev/cxg-author-probe", editable = true }`
3. `uv sync`; verify: `python -c "import cxg_author_probe,os;print(os.path.dirname(cxg_author_probe.__file__))"` → should point into `_codev/…/src`.

⚠️ **TEARDOWN before ANY commit to atlas-reporter:** remove the editable
override, pin the atlas_chat dep to a git SHA/tag, `uv lock && uv sync`, run
tests. `_codev/` is gitignored → a committed path dep breaks everyone + CI.
(Full note in memory `adopt-cas-cxg-for-annotations` "CO-DEV SETUP".)

## Ordered tasks (from notes §"Candidate features to push upstream")

1. **Entry-point reader discovery** in cxg-author-probe's `readers/registry.py`
   (currently a hardcoded list + in-process `register_reader` only). Make it
   discover installed readers via entry points, so the CLI/plugin see external
   readers. SMALL, HIGH-LEVERAGE — unblocks the CLI/plugin zarr path.
2. **Promote our zarr reader upstream.** Move
   `src/atlas_chat/atlas_chat/services/readers/zarr.py` into
   `_codev/cxg-author-probe/src/cxg_author_probe/readers/zarr.py` (replacing the
   stub) + port its test. Then atlas-reporter deletes its local copy and relies
   on the module. (Note the module-name-ends-in-`.zarr` format-detection quirk —
   candidate to fix to key off the reader's `FORMAT` attr instead.)
3. **CAP+ schema + assembly upstream.** Hand `cas_annotation.schema.json` (+ its
   golden tests: `tests/unit/test_cas_annotation_schema.py`) to the module as the
   SEED SPEC for a `cas`/`cap+` output. Move `annotations_writer` (intermediate
   → CAS assembly) + composition cross-tabs + labelset hierarchy/rank upstream.
4. **Field classification → CxG (Fork A)** in the module: grow `picks-v1` into a
   `classification-v1` (every obs col → cell_type|tissue|development_stage|assay|
   disease|sex|self_reported_ethnicity|organism|cluster|id|none + ontology
   target). Preserve ONE shared CxG-field vocabulary (see notes §Alignment).
5. **Agentic reader improvisation** (bigger, later): detect → registered reader →
   else agent writes an `ObsHandle` impl → VERIFY vs contract invariants →
   cache → capture-and-promote. Gated by verification; sandboxed obs-only.

## What STAYS in atlas-reporter (do NOT move)

Map + report: `ontology-term-lookup`, `cl-term-request`, `resolve-name`,
`scan-supplements`, `citation-traverse`, `synthesize-report`, `report_checker`,
CL-mapping-into-header, the literature/ontology service stack. atlas-reporter
gains a CAP+ INPUT validator (reuse the landed schema) instead of a CAS writer.
Open boundary Q: `subatlas_resolver` (study→DOI) — lean STAY.

## Read these, in order

1. `planning/notes_cxg_author_probe_future_upstream_2026-07-04.md` — the spec:
   repositioning, reader flexibility, ordered candidates, alignment contract.
2. `planning/plan_adopt_cxg_author_probe_PROVISIONAL_2026-07-04.md` — what the
   module already is (verified from source) vs what's ours; Fork A decision.
3. `planning/mockup_cas_cxg_annotations_2026-06-24.md` — CAP+ shapes on real HDCA
   data (composition Variant B, transferred_annotations, hierarchy).
4. `planning/plan_cas_migration_bigbang_and_prog_agentic_split_2026-06-24.md` —
   the prog/agentic boundary principle + testing/over-fit strategy.
5. Memory `adopt-cas-cxg-for-annotations` — the running decision log.

## Cross-repo caveats

- Two git repos, two test suites. Keep cxg-author-probe's OWN tests green as you
  edit `_codev` (`cd _codev/cxg-author-probe && make test` or `pytest`).
- Treat each `_codev` edit as if it were a PR (scoped, tested) — the co-checkout
  removes PR friction, which was a feature.
- cxg-author-probe uses schema-generated Pydantic (`make models`, drift-guard
  test). If you add/change a schema there, regenerate models in the same change.
- The plugin sub-agent `cxg-author-probe:author-category-picker` is available as
  an agent type this session (the picker half).
