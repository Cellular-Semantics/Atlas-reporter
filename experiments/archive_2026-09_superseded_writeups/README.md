# Superseded write-ups — archived 2026-09-04

These nine documents were the running record of the retrieval testing on branch
`test/retrieval-matrix`. They are **superseded** by a single integrated report:

> `experiments/retrieval_tests_report_2026-09.md`

They are kept unchanged because they contain reasoning, worked examples and
caveats the report only summarises, and because the report cites them. **Do not
quote figures from these files.** Three numbers in them do not match the data on
disk, and one whole class of result — anything resting on "was the marked
sentence in the context" — is now known to be unsound. Both are set out in the
report, §7.

The old documents used a Stage 1 / 2 / 3b numbering that had become
uninformative, and in one case ambiguous: "Stage 3b" named both the retrieval
matrix here *and* an unrelated claim-adjudication step in
`experiments/citation_traversal/`. The report drops the numbering.

## What replaced what

| archived file | what it was | replaced by |
|---|---|---|
| `retrieval_matrix_plan_2026-08.md` | the original plan for the whole programme | report §1 (aims), §2 (common methods) |
| `retrieval_stage1_setup_findings_2026-08.md` | what was learned building the harness | report §3, constraints established before testing |
| `retrieval_stage1_results_2026-08.md` | ranking inside a paper, no model | report §4, Test 1 |
| `retrieval_stage2_plan_2026-08.md` | plan for the reading test | report §5.1–5.3 |
| `retrieval_stage2_results_2026-08.md` | reading from a fixed context | report §5, Test 2 |
| `retrieval_test_items_draft_2026-08.md` | the 57 candidate items, with the reasoning behind each | report §4.2 and §5.2 (design); the items themselves are still the source of truth |
| `HANDOFF_stage3_extended_test.md` | session handoff; the hard-won scoring rules; the design for a supplement test | rules → report §11.4; the supplement test was **never run** → report §10 |
| `retrieval_stage3b_results_2026-08.md` | the retrieval matrix over 55 realistic questions | report §6, Test 3 |
| `RESTART_stage3b.md` | a scratch restart note, kept at the repo root, explicitly not for commit | folded into report §6 and §7; its "next actions" list into §10 |

## Still live, not archived

- `planning/citation_traversal/` — a separate strand on following citations *out*
  of the atlas paper. Not covered by the report.
- `planning/supplement_corpus_findings_2026-08.md` — a survey of what
  supplementary material can be reached. Related, but not one of these tests.

## The data is not here

Raw results, items, contexts, answers and verdicts stay where they were, under
`experiments/results/`, `experiments/stage2/` and `experiments/stage3b/`. Those
directory names still carry the old stage numbers so that paths quoted in these
archived documents continue to resolve. The report's §11.1 maps them.
