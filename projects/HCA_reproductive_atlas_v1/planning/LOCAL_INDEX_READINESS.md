# Local-index readiness — HCA reproductive atlas (report-only)

**Date:** 2026-08-03 · **Question:** do we have infrastructure on this branch
(`HCA_reproductive_atlas_v1`) to locally index subatlas papers that ASTA /
PMC can't reach, and is any of it on the HDCA branch? · **Scope:** investigation
only, nothing installed or built.

---

## Bottom line

**Yes — the full local-indexing stack is present on this branch and current.**
It is the multi-paper "corpus" version (matches the `local-paper-index` skill).
Three things stand between us and a working index, none of them missing code:

1. the `[local-index]` Python deps are **not installed** in this environment;
2. the automated **discover** step needs a `label_provenance.json` this project
   doesn't have (annotations came from `scripts/build_cas.py`, not the zarr skill);
3. the atlas paper's DOI won't resolve to JATS, so it must be indexed **from the
   PDF we already hold**.

All three are worked around via the `add --pdf/--jats` path, which is
standalone. **The HDCA branch adds no repro-specific content** — it only holds a
worked *example* of a built single-paper index (old layout).

---

## What's on this branch (all present, verified)

| Component | Path | State |
|---|---|---|
| CLI | `scripts/setup_local_index.py` | ✅ current — subcommands `discover-subatlas · init-corpus · add · list · remove · search · build(legacy)` |
| Corpus engine | `src/atlas_chat/atlas_chat/services/local_snippet_index.py` (44 KB) | ✅ `MANIFEST_VERSION 2`, corpus model, JATS + PDF, idempotent per-paper hash |
| Subatlas resolver | `…/services/subatlas_resolver.py` (15 KB) | ✅ `discover()` + `ingest()` |
| JATS parser | `…/services/_jats_parser.py` | ✅ vendored |
| PDF parser | `…/services/_pdf_parser.py` | ✅ `pymupdf4llm`-based |
| Fan-out hook | `…/services/citation_traverser.py` → `traverse_local()` | ✅ merges local snippets into fan-out, tagged `source_method: "local_snippet"`, id `CorpusId:local_<hash>` |
| Optional deps | `src/atlas_chat/pyproject.toml` → `[project.optional-dependencies] local-index` | ✅ `sentence-transformers>=5.0`, `numpy>=1.26`, `pymupdf4llm>=0.0.17` |
| Skill doc | `.claude/skills/local-paper-index/SKILL.md` | ✅ describes discover→review→ingest→add→search |
| Orchestrator wiring | `CLAUDE.md` §4b | ✅ documents the local-index merge path |

Handling of ASTA-blind papers is exactly what we need: `ingest()` marks each
confirmed subatlas entry `asta` (reachable — no local build), `local` (JATS/PMC
fetched and indexed), or **`needs_pdf`** (neither — logged to
`subatlas_todo.md`/`subatlas_missing.json` for a manual PDF drop). PDFs are then
indexed with `add --pdf` (Crossref metadata; no citation graph — fine for
retrieval). Default is `use_in_fanout: false`; flip it in `corpus.json` to blend
local hits into citation traversal.

---

## Three gaps to clear before a build (all workaround-able, no code missing)

1. **ML deps not installed here.** Checked: `sentence_transformers`,
   `pymupdf4llm`, `fitz`, `lxml`, `torch` all **MISSING** (only `numpy` present).
   → `uv sync --extra local-index` (or `uv pip install -e 'src/atlas_chat[local-index]'`).
   ~500 MB (MiniLM + torch + PyMuPDF). One-time.

2. **No `label_provenance.json` → `discover-subatlas` won't auto-run.**
   `discover()` reads that file's contributing-study labels; this project's
   `cell_type_annotations.json` was built by `scripts/build_cas.py` (not
   `anndata-zarr-summary`), so it was never produced, and `source` has no
   `subatlas_papers` block yet. Also note the flat `subatlas_pubs` DOI list
   (21 DOIs) is a **hand-maintained reference file — not consumed by any code.**
   → Either seed `source.subatlas_papers` by hand (DOIs already known, see below)
   and run `init-corpus`, or skip discovery entirely and `add` each paper
   directly. `add`/`build`/`search` don't depend on `label_provenance.json`.

3. **Atlas paper DOI won't JATS-resolve — index it from the PDF.**
   The atlas DOI is `10.64898/2026.06.10.731198` (non-standard prefix, not
   `10.1101`); `_biorxiv_meta()` hits `api.biorxiv.org/.../biorxiv/{doi}` which
   expects `10.1101`, and there's no PMC copy (preprint). `ingest()`'s automatic
   atlas step will likely error on the JATS fetch.
   → We already hold `inputs/2026.06.10.731198v1.full.pdf`; index it explicitly:
   `add --role atlas --doi 10.64898/2026.06.10.731198 --pdf inputs/2026.06.10.731198v1.full.pdf`.

---

## Which subatlas papers actually need local indexing

From the ASTA-access audit in `notes/ANNOTATION_INSPECTION.md` (21 unique subatlas
DOIs), **3 are not cleanly ASTA/PMC-traversable.** But priority depends on
whether a paper *contributed transferred labels* into the CAS obs (the 8
`celltype_*` columns in `scripts/build_cas.py`) versus being cited context only:

| DOI | Paper | ASTA status | Contributes CAS labels? | Priority |
|---|---|---|---|---|
| `10.1016/j.devcel.2025.09.011` | Lardenois 2025 (gonadal somatic) | indexed but **title/abstract only** | **Yes** — `celltype_Lardenois2026`, 70 fine types | **High** |
| `10.1126/science.adx0659` | (Science; not identified) | **not in Semantic Scholar** | No | Low (context only) |
| `10.1093/cei/uxad029` | Huang 2023 (endometriosis immune) | in S2 but **non-OA, no PMC, no snippets** | No | Low (context only) |

Plus the **atlas preprint itself** (gap 3) — always needed for grounding, and
only indexable from the PDF.

**So the minimum corpus to unblock report drafting is two PDFs:** the atlas
preprint (have it) and Lardenois 2025 (Cell Press, GREEN OA — a repository PDF
should be findable). `science.adx0659` and `cei/uxad029` are optional and only
matter if a report cites them as literature context. Every other transferred-
label source (GarciaAlonso 2021/2022, Ulrich 2022/2024, Weigert 2025, Lorenzi
2025, Marečková/HECA) was marked ASTA-traversable — no local index required.

---

## What the HDCA branch offers

`origin/HDCA_Neurons` (project `projects/HDCA_neurons/`) contains a **built
single-paper local index** — `manifest.json` (version **1**, old root layout),
`source/paper.jats.xml`, `chunks/`, `citations/`, `snippet_index/snippets.json`
for DOI `10.64898/2026.03.30.714220` (84 chunks, 193 refs, 181 CorpusIds
resolved). It is:

- a useful **worked example / smoke-test** of the JATS build path end-to-end;
- in the **pre-corpus layout** — `local_snippet_index` auto-migrates such indexes
  to `papers/<slug>/` on first read, so it's not a blocker, just a reference;
- **not repro-specific** — none of its content applies to this atlas.

`subatlas_resolver.py` exists on **both** branches (it's already here), so there
is nothing on HDCA we need to port. Net: HDCA is confirmation the stack works,
not a source of missing pieces.

---

## Suggested path (for when we act — not done here)

1. `uv sync --extra local-index` (gap 1).
2. Index the atlas preprint from PDF (gap 3) — `add --role atlas … --pdf inputs/…full.pdf`.
3. Fetch a Lardenois 2025 PDF; `add --role subatlas --doi 10.1016/j.devcel.2025.09.011 --pdf …`.
4. (Optional) same for `science.adx0659` and `cei/uxad029` if reports will cite them.
5. `search --project HCA_reproductive_atlas_v1 --query "…"` to smoke-test, then
   set `use_in_fanout: true` in `corpus.json` if we want local hits blended into
   traversal.
6. (Optional) seed `source.subatlas_papers` / a `label_provenance.json` if we
   want the automated discover pass rather than manual `add`s.

*Nothing was installed, built, or edited during this investigation.*
