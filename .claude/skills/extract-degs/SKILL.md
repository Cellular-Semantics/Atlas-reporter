---
name: extract-degs
description: Convert a paper's published differential-expression tables into a per-cell-type store that later steps look genes up in, keeping the conversion code so it can be repeated. Use when setting up a project, when asked to "extract DEGs", "process the DE tables", "pull the differential expression", or when a report needs statistics for a marker and none are on disk.
output:
  schema: src/atlas_chat/atlas_chat/schemas/degs.schema.json
---

# extract-degs

Differential expression is the only quantitative evidence an atlas paper offers
about what identifies a cell type. This converts what a paper published into a
store keyed by cell set, once, at setup.

**You write the conversion code.** Every published table is laid out
differently, so no parser can anticipate them; what makes this repeatable is
that the code you write is kept beside its output.

## Instructions

### Step 1: Find the tables

The supplement manifest already says which sheets hold differential expression —
`index-supplements` marks them `content_type: deg_results` and describes what
each one compares.

```bash
uv run python -m atlas_chat.cli_supplements show --store <store> --doi <doi>
```

Read the `tables` entries. Their `description` and `locator` tell you what to
open and, often, what was compared. If none are marked, say so and stop: a paper
with no published DE tables is a normal outcome, not a failure.

### Step 2: Probe the structure, cheapest first

Do not open a table blind and do not assume its shape. Work up only as far as
you need:

```bash
# Sheet names, dimensions, the guessed header row, a few rows. Flat cost.
uv run python -m atlas_chat.cli_supplements outline --file <path>

# One region, once you know which sheet and where its header is.
uv run python -m atlas_chat.cli_supplements slice --file <path> \
  --locator "<sheet>" --start 0 --limit 12 --header-row <n>
```

A small table can be read whole. A large one cannot: check `n_rows` from the
outline before reading anything, and work from the header and a sample instead.

**Check the guessed header row against the sample rows.** Publisher tables
routinely carry a title row above the real header, sometimes two, and a reader
that slices from the wrong row gets nonsense.

Stop probing when you can state, for each table: which cell sets it covers, what
each was compared against, which column is the effect size, and where one table
ends and the next begins. If you cannot state all four, keep probing.

**Read `references/table-shapes.md` before writing any conversion.** It works
through layouts that corrupt output without raising anything. They are examples
rather than a list to check off — the useful question it teaches is *what would
this table look like if I had misread it, and would I be able to tell?*

### Step 3: Write the conversion

Write a script into the store directory, named for what it converts:

```
projects/<project>/degs/extract_<source>.py
```

It reads the supplementary file and writes one document per cell set, conforming
to `degs.schema.json`. Keep it plain and readable — it is the record of how the
numbers were obtained, so someone should be able to check it against the table.

Carry through, per comparison:

- **`comparison`** — what was compared against what, in the authors' words where
  the sheet states them, and set `comparison_is_quoted` when it is theirs.
- **`effect_field`** — which score carries direction. Name it; do not leave a
  consumer to guess, because guessing wrong inverts the answer.
- **`n_genes`**, and `n_up` — a gene missing from a short list may simply not
  have reached it; missing from a long one is a finding. Without the count those
  are indistinguishable.
- **`direction`** per gene, from the sign of the effect size.
- **`scores`** under the authors' own field names, unrenamed.

Do not normalise gene symbols. A symbol rewritten here cannot be matched against
the paper's own text.

### Step 4: Validate

```bash
uv run python -m atlas_chat.cli_degs --store projects/<project>/degs
```

Expected output: JSON giving `files`, `cell_sets`, `comparisons`, `genes`, and
`ok: true`. Exit code 2 and a list of errors means it is not done.

This checks conformance *and* that the counts agree with the rows — a stated
`n_genes` that disagrees with the genes listed is worse than no count, because
it is read as a statement about what the paper published.

It also fails when the conversion code or the note is missing. That is
deliberate: numbers nobody can trace back to a table are not evidence.

### Step 5: Write the note

`projects/<project>/degs/README.md`, saying for each converted source:

- the paper, and the supplementary file and sheet it came from, as the manifest
  names them;
- what each table compared, and anything the authors excluded before publishing;
- which script produced which files, and how to re-run it;
- anything you could not convert, and why.

Point at the manifest rather than copying it. The manifest is the record of what
the supplement holds; this is the record of what was taken from it.

## Example

**Three cell types in one sheet.** The outline shows one sheet, ~800 rows, and a
header row naming `gene_name`, `HCA_celltype_label`, `log2FC`, `padj`. Slicing
the first rows shows the header repeating three times across the columns, with
blank columns between, and a row above it naming three populations.

That is three tables side by side, not one. Converting it as one produces a
single gene list mixing three cell types.

The conversion takes each block separately — its own gene column, its own effect
size — and writes three documents. Within each block both directions are
present, so `direction` comes from the sign of `log2FC`, and `n_up` will be
smaller than `n_genes`.

## Troubleshooting

**`no conversion code kept`** — the script was written somewhere else, or
deleted. Put it in the store directory. The check is not pedantry: it is the
difference between numbers and numbers you can defend.

**`n_genes is N but M are listed`** — usually a filter applied while writing that
was not applied when counting, or a header row counted as data.

**`effect_field 'x' absent from N gene(s)`** — the named score is missing for
some rows, commonly because a block boundary was crossed and the columns shifted.

**Every gene comes out `up`** — the sign was taken from a column that is an
absolute value, or from a rank rather than a fold change. Check the effect field
against the table.

**The gene column contains cell type names** — the header row was read from the
row naming the blocks rather than the row naming the columns.
