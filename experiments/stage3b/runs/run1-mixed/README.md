# Run 1 — mixed-model reader (KEEP: this is the Opus/Fable comparison set)

**Do not delete or overwrite.** This run is retained deliberately so the Sonnet
results in `../../` can be compared against a different reader model on
*identical* items, contexts and batching.

## What happened

Reader model was not pinned on dispatch, so subagents inherited whatever the
session model was at the time. The session model changed mid-run (Opus 5 →
Fable 5), and per-request routing varied within single agents. The result is a
run where the reader model differs **by arm**, which is why it cannot be used
as a clean six-arm matrix on its own — but is directly useful as a
model-comparison against run 2.

Model attribution was recovered after the fact from the session task
transcripts (assistant-message `model` fields), not from memory. Counts are in
`reader_provenance.json`; `dominant_model` is the modal model per job file.

| arm | dominant model | typical mix per job file |
|---|---|---|
| `blind` | `claude-opus-5` | clean |
| `whole` | `claude-opus-5` | clean |
| `local` | `claude-opus-5` | clean |
| `localfix-*` (2 singleton re-reads) | `claude-opus-5` | clean |
| `asta-sep` | `claude-opus-5` | 24 opus : 3 fable |
| `asta-comb` | `claude-opus-5` | 18 opus : 3 fable |
| **`local-comb`** | **`claude-fable-5`** | 12 fable : 4 opus |
| all judge batches | `claude-opus-5` | clean |

The minority-model calls in the mixed rows are a small share of assistant turns
and may be orchestration overhead rather than answer generation; the transcripts
do not separate the two, so the counts are reported raw.

## Contents

```
answers/      40 files, 332 reads (330 scored + 2 localfix re-reads)
verdicts/     185 judge verdicts (all judges Opus 5)
jobs/         40 job files — the exact prompts these readers saw
scores.json   deterministic outcomes before judge merge
final.json    330 scored rows after judge merge
judge_worklist.json
reader_provenance.json
```

## What is comparable, and what is not

**Comparable to run 2:** the items, the contexts, the reader contract and the
scoring code are identical. Batching differs — run 1 batched `blind`/`whole`/
`local` label-major (which caused the leakage described in the write-up) and
only the later three arms round-robin; run 2 is round-robin throughout. For
`whole` and `blind` batching is irrelevant (shared or absent context). For the
per-item-context arms, treat batching as a nuisance factor.

**Not comparable within run 1:** `local-comb` against the other arms, since it
alone was dominantly Fable.

## Headline (run 1, for reference)

| | blind | whole | local | asta-sep | asta-comb | local-comb |
|---|---|---|---|---|---|---|
| present (41) | 0 | 38 | 36 | 39 | 34 | 34 |
| absent (14) | 14 | 13 | 13 | 14 | 14 | 13 |
| **all (55)** | 14 | 51 | 49 | 53 | 48 | 47 |

reader: Opus 5 for all columns except `local-comb` (Fable 5).
