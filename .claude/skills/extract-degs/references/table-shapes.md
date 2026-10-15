# Layouts that silently corrupt a conversion

**These are examples, not a checklist, and they are nowhere near exhaustive.**
They are simply the ones met so far, in a handful of papers. The next table you
open may be malformed in a way nobody here has seen, and finding that none of
these apply tells you nothing about whether it is safe.

What generalises is the failure mode, not the list: each of these produces a
plausible-looking output rather than an error. So the question to hold while
probing is not "is it one of these?" but **"what would this table look like if I
had misread it, and would I be able to tell?"** If the answer is that a
misreading would look fine, keep probing until it would not.

Read them as worked examples of that question being asked.

## Several tables share one sheet

Blocks of columns side by side, separated by blank columns, under a row naming
the populations and a second row naming the columns:

```
            uftLAM                                    Mac_LYVE1hi
 gene_name  HCA_celltype_label  log2FC  padj          gene_name  HCA_celltype_label  ...
 SHISAL2A   Immune_uftLAM       4.73    1.1e-79       NRP1       Immune_Mac_LYVE1hi  ...
```

Reading "the gene column" gets the first population only. Reading every column
whose header is `gene_name` and concatenating gets one list mixing several cell
types, each gene attributed to whichever population happens to be first.

**How to spot it:** the header row repeats across the columns; there is a row
above it holding a few labels in widely spaced columns; blank columns separate
groups.

**What to do:** treat each block as its own table, keyed by the population named
above it. The per-row cell type column, where there is one, is the check — every
row in a block should carry the same value.

## Both directions in one list

Enriched and depleted genes interleaved, distinguished only by the sign of the
effect size. In one measured case 60 of 211 rows were depleted.

Anything reading gene names without checking the sign reports a third of them as
markers of the cell type they are *depleted* in — an error that inverts the
biology and reads perfectly well.

**How to spot it:** a legend cell saying "Upregulated genes" and another saying
"Downregulated genes"; negative values in the effect column.

**What to do:** set `direction` from the sign, and record `n_up`. Never filter
the depleted genes away — a gene depleted in a cell set is a real published
result, and the report may want it.

## Direction shown by colour

The same table may also fill enriched and depleted rows with different
background colours. Where it does, the colour is usually redundant with the
sign — but do not rely on it, and do not rely on the sign being redundant with
the colour either. Check one against the other on a sample: if they disagree,
the sign is the number the authors computed and the colour is a human
annotation.

## A title row above the header

One or two rows of prose above the real header, often the table's caption:

```
 Supplementary Table 3A. Differentially expressed genes between …
 (blank)
 Upregulated genes
 gene_name  log2FC  padj
```

A header-row guess can land on the caption. Every column then reads as a single
long string and the first data row is consumed as headers.

**What to do:** check the guessed header row against the sample rows before
using it. That caption is worth keeping — it is usually the authors' own
statement of what was compared, which is what `comparison` should carry.

## A gene column that is an index

Some exports write the gene as the row index with no header, so the first column
has an empty header cell and the named columns are all statistics.

**What to do:** where the header is blank and the values are symbols, that is the
gene column.

## Wide format: one column per cell type

Instead of a cell type column, one column of effect sizes per population, gene
per row. Converting this as long format attributes every gene to one population.

**What to do:** melt it — one document per column, the column header being the
cell set.

## The same shapes, in JSON

A JSON dump is usually one of these layouts already flattened, and the same
misreadings survive the change of format — with less to warn you, since there is
no header row to check and no blank column to notice.

- **Keyed by cell set** — an object whose keys are the populations, each holding
  a gene list. The analogue of several tables in one sheet, and the easy case:
  the key is the cell set, so nothing can be silently misattributed.
- **A flat list of records** — every row carries the cell set in a field.
  Converting it without grouping on that field produces one document holding
  every population's genes.
- **Both directions in one array**, exactly as above: sign of the effect size,
  never the order.
- **The effect size under an unhelpful name** — `score`, `stat`, `value`. Which
  one carries direction is not a guess to make from the name: find a gene you
  know the direction of, or a field whose values are signed where a rank or an
  absolute value would not be.

A `.json` extension is a claim, not a fact. A file of one JSON object per line
fails to parse whole and is read a line at a time.
