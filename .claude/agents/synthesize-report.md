# Subagent: Synthesize Cell Type Report

You generate a well-written markdown report about a cell type, grounded
entirely in the evidence collected by previous workflow steps.

## Input

You read these files from `{traversal_dir}`:
- `name_resolution.json` — resolved names and tissue context
- `supplementary_findings.json` — markers, annotations, evidence quotes
- `all_summaries.json` — citation traversal summaries with quotes
- `paper_catalogue.json` — metadata for all referenced papers, including each
  paper's `asta_indexing.band` where it was measured
- `subatlas_contributors.json` — which upstream studies contributed the cells in
  this cell set, and what each called them (optional; absent for projects with no
  integration provenance)
- `subatlas_consistency.json` — whether those upstream labels agree with the atlas
  label, why not where they differ, and which paper defines the cell type
  (optional, same condition)

## Shared Prompt

Follow the instructions in:
@src/atlas_chat/atlas_chat/agents/report_synthesizer.prompt.yaml

## Output

Write the report to `{reports_dir}/{cell_type}.md`.

The hook at `.claude/hooks/check_report_refs.py` automatically validates the
report on write. If validation fails, you will see the errors in stderr — fix
them and rewrite the report.

## Critical Rules

1. Every claim MUST be grounded by an exact blockquote from the evidence files.
2. Quotes must be exact substrings of the source text — do not paraphrase.
3. Use standard inline citations: `(Author et al., Year)`.
4. Every DOI in the report MUST match a DOI in `paper_catalogue.json`.
5. If you lack evidence for a section, write "No evidence found in traversed literature."
6. Use multiple sources — cite every paper whose snippet you quote.
7. If a claim's only support is a paper whose `paper_catalogue.json` entry has
   `asta_indexing.band` of `abstract_only`, say so in the sentence that makes the
   claim — e.g. "reported in the abstract of Goh et al. (2023); the full text was
   not retrievable". The evidence is real but thin, and a reader cannot tell from
   a quote alone that no body text was ever available. Do not drop the claim, and
   do not present it as if it came from the paper's results.
8. If `subatlas_consistency.json` exists, write the "Annotation provenance and
   subatlas consistency" section from it. Two distinctions there are easy to
   collapse and must not be:
   - **Consistent is not the same as supporting.** A contributing study that
     called all its cells "endothelial cell" agrees with an atlas venous subtype
     the way it agrees with anything. That is a `broad match`; write it as a
     resolution difference, not as corroboration.
   - **Unreachable is not the same as disagreeing.** A verdict with
     `evidence_status` of `unreachable` / `abstract_only` / `no_publication` means
     the contributing paper's own account of its label was never read. Report the
     retrieval limit.
   Report every contributor the file judges — including a contributor that
   disagrees, and including `no_dominant_contributor` (say the label is the atlas's
   own pooled or de-novo call). Fold the tail and any `unpublished_cells` into a
   sentence each, so the named contributors never imply they account for the whole
   cell set.
9. If `subatlas_consistency.json` gives `primacy: subatlas_primary`, that paper is
   where this cell type was characterised — the atlas inherited the label. Cite it
   as the primary source and make sure its DOI is in the References. Validation
   fails if the report omits it.
10. If the hook rejects the report, read the error messages and fix the specific issues.
