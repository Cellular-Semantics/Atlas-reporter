# Next steps — HCA reproductive atlas

Running log of decisions and open items. Newest entry first.

---

## 2026-08-12 — Decision gate: evaluate new citation-traversal skill before a full report run

**Status:** paused here to move to other tasks.

**Where things stand (done this session):**
- CAS build, source-reconciliation docs, and two validated draft reports
  (`reports/adventitial_fibroblast_PI16hi.md`, `reports/CD8_tissue_resident_memory_T.md`)
  produced with the **existing** citation-traversal architecture (ASTA
  `snippet_search` + report synthesis).
- CL mapping + two drafted NTRs for the adventitial-fibroblast family (T1/T2).
- Local snippet index built for the atlas preprint + 3 subatlas PDFs
  (Lardenois, science.adx0659, Huang); `use_in_fanout: true` in
  `local_index/corpus.json`. Deps installed via `[local-index]` extra.
  Non-shareable PDFs and the derived index are gitignored.

**Next action (do this before anything else): review the test results from the
new citation-traversal skill.**
- Compare the new skill's output against the two reports already produced with
  the existing architecture (same cell types make the cleanest A/B: adventitial
  fibroblast PI16-high and CD8 tissue-resident memory T).
- Judge on: (a) quote fidelity — do blockquotes remain exact substrings of the
  evidence corpus? (b) source breadth and relevance of retrieved snippets;
  (c) whether local-index (`use_in_fanout: true`) hits are picked up and merged
  correctly, esp. for the not-on-ASTA papers (Lardenois, atlas preprint);
  (d) citation/DOI correctness; (e) cost/latency per report.

**Decision to make after reviewing those results:**
- **Option A — proceed to a full run with the existing architecture.** Choose if
  the new skill shows no clear quality/coverage gain, or isn't ready. The current
  pipeline is validated end-to-end (0 blockquote/DOI violations on both reports).
- **Option B — adopt the new skill(s) for the full run.** Choose if the test
  results show materially better retrieval, grounding, or local-index handling.
  If so, first confirm it honours the project's tool rules (ASTA/MCP only, exact
  quotes, DOIs from catalogue) and the local-index merge path before scaling.

**Then (once the architecture is chosen):** run reports across the priority
target list — the headline novel populations in `ANNOTATION_INSPECTION.md`
(uterine perivascular cells, NCRhi ILC3s, LAMs incl. uftLAM, adventitial
fibroblasts, ectopic endometrial-like epithelium), plus Lardenois-dependent
gonadal-somatic types now that the local index covers that paper.

**Open items carried forward (not blockers for the decision above):**
- Author-facing edits are report-only so far; `SOURCE_RECONCILIATION_for_authors.md`
  is ready to share once reviewed. New media-4 duplicate `Neural_Schwann` finding
  (see `CAS_DOC_AUDIT.md`) still to be folded into the authors' memo.
- NTRs T1/T2 are drafted but **not posted** to `obophenotype/cell-ontology`
  (needs explicit go-ahead; step 10).
- CL subsumption flags (`Endo_ven`, `Mesen_OvarianFibs`) still awaiting author
  decision.
