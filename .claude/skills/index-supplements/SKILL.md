---
name: index-supplements
description: Index a paper's supplementary material into a store manifest that says precisely which file, sheet or page holds what — DEG results, cluster-to-name mappings, marker lists, cell metadata — and what the columns are. Reads captions first, opens files only when the captions don't answer it. Needs the [supplements] extra (openpyxl).
output:
  schema: src/atlas_chat/atlas_chat/schemas/supplement_manifest.schema.json
---

# index-supplements

Supplementary material carries content a report often cannot be written without:
DEG tables, cluster-to-name mappings, the marker lists name resolution depends on.
Your job is to produce a manifest that lets a later reader go straight to the right
sheet instead of re-scanning a bundle of forty workbooks.

You write the `tables`, `prose` and `gaps` sections of a paper's
`manifest.json`. The schema is the contract and is self-documenting — read its
field descriptions rather than looking for them here.

## What this is not

You are not extracting biology. Do not read a DEG table and write down the genes.
The manifest describes *where evidence lives and what shape it is in*; the
querying happens later, against a specific cell type.

## Requirements

- The `[supplements]` extra: `uv sync --extra supplements` (openpyxl).
- Files already in the store. Retrieval is a separate concern — see
  "Getting files in" below.

## The mechanical half

Everything that touches bytes is in `atlas_chat.services.supplement_store`,
behind a CLI. Use it rather than reading supplement files directly: a
supplementary table can run to hundreds of thousands of rows, and `Read` on one wrecks
your context for no gain.

```bash
# What supplements does this paper have? Labels and captions come from the
# article XML and exist nowhere else — this is the cheapest thing you will read.
uv run python -m atlas_chat.cli_supplements inventory --jats <paper.jats.xml>

# Take files a user dropped into incoming/ into the store.
uv run python -m atlas_chat.cli_supplements adopt \
  --store <store> --doi <doi> --incoming <dir> [--jats <xml>] [--pmcid <PMCID>]

# Expand archives, record the member tree. Videos are skipped, big tables are not.
uv run python -m atlas_chat.cli_supplements unpack --store <store> --doi <doi>

# Bounded description of one file's shape: sheet names, dimensions, the guessed
# header row, a few sample rows. Cost is flat in the size of the file.
uv run python -m atlas_chat.cli_supplements outline --file <path> [--rows N] [--cols N]

# Targeted read of one region, once you know which sheet you want.
uv run python -m atlas_chat.cli_supplements slice \
  --file <path> [--locator <sheet>] [--start N] [--limit N] \
  [--columns A B] [--header-row N]

# Read, and check, the manifest.
uv run python -m atlas_chat.cli_supplements show  --store <store> --doi <doi>
uv run python -m atlas_chat.cli_supplements check --store <store> --doi <doi>

# Retrieve: article XML -> Europe PMC bundle -> publisher -> manual.
uv run python -m atlas_chat.cli_supplements fetch \
  --store <store> --doi <doi> | --cas <cas.json> [--retry] [--no-bundle]

# Judge which stored files could describe cell types, from their columns.
uv run python -m atlas_chat.cli_supplements triage --store <store> --doi <doi>

# Draft pointers, one per SHEET, with everything mechanical already filled in:
# locator, header row, dimensions, columns, a suggested kind and a relevance
# verdict. Add a description to each and that is your `tables` section.
uv run python -m atlas_chat.cli_supplements triage --store <store> --doi <doi> --sheets

# Which papers does a project need supplements for?
uv run python -m atlas_chat.cli_supplements papers --cas <cas.json>
```

The order is **fetch → unpack → triage → assess → index**. Unpacking before triage
matters: a bundle of forty tables is one opaque item until it is expanded, and
its members are what get judged.

## Size limits, and why none of them are silent

Supplementary tables run to hundreds of thousands of rows, so every read here is
bounded. That is only safe if a bound never looks like an absence, so each one
leaves a trace:

| Limit | What it does | The trace it leaves |
|---|---|---|
| unpack size caps | leaves an oversized member unextracted | a `gaps` entry naming the file, its size and the flag to raise |
| `outline --rows` / `--cols` | shows the top-left of a table | `truncated_rows` / `truncated_cols` next to the true `n_rows` / `n_cols` |
| cell width | clips a long cell | a trailing `…` |
| `text --max-chars` | clips a document | `truncated: true` plus the true `chars` |
| `slice --limit` | returns one window | `start`, `returned` and the true `n_rows` |
| `columns` in a manifest | may list a prefix for a very wide table | compare its length against `n_columns` |

Two consequences for you:

- **Never conclude anything from a bounded read.** If `truncated_rows` is true,
  you have seen the top of the table, not the table. Say what the table *is*,
  from its columns and its legend; do not say what is or isn't in it.
- **Assume the reader after you must explore programmatically.** Nothing
  downstream can open one of these files whole either, so a pointer earns its
  keep by carrying `locator`, `header_row`, `n_rows` and `n_columns` — enough to
  slice straight to the right region. That, not a summary of the contents, is
  the deliverable.

## Getting files in

Three routes, cheapest first:

1. **Already in the store.** `show` tells you; a file with `status: "present"`
   has bytes on disk. Re-indexing an unchanged paper is wasted work — if
   `indexed_at` is set and the files' `sha256` values haven't changed, stop.
2. **Manually dropped.** Files under the project's `supplements/incoming/<doi-slug>/`
   get taken into the store by `adopt`. This is the only route for closed-access
   papers, and it is a first-class route, not a failure.
3. **Fetched.** For open-access papers, the article XML lists the filenames and
   the publisher's static host usually serves them individually. Automated
   retrieval is deliberately out of scope for this skill — if files are missing,
   record a gap saying which ones and let the operator drop them in.

## Triage first: only index what could describe a cell type

The aim is describing cell types, their properties, and the data supporting
them. Most of a supplement bundle does not bear on that, and deep indexing is
the expensive step, so run `triage` before you open anything.

Triage writes `relevance` and `relevance_note` on each file and archive member,
and with `--sheets` on each **sheet**. Sheet level is the one that matters: one
workbook can hold both the DEG table a report needs and an antibody list it
never will, and a verdict on the file cannot express that. Verdicts mean:

- **`irrelevant`** — ruled out, with the reason: either its caption says what it
  is ("Reporting Summary", "Peer Review file") or its columns do (a reagent list
  with a vendor and a catalogue number). Do **not** index these, and do not treat
  them as gaps — nothing is missing.
- **`relevant`** — its columns match a known kind: differential expression,
  marker lists, cluster-to-name mappings, per-cell tables, enrichment,
  cell-cell interactions, sample metadata. The note names the kind, so you start
  from a hypothesis rather than a blank sheet.
- **`unknown`** — the cheap signals did not settle it, most often because the
  format has no readable columns. **Index these.** Unknown means "look", never
  "skip".

Expect triage to rule out only a small fraction outright. Its value is less in
exclusion than in handing you a kind and a reason for much of what remains.

The asymmetry is deliberate, and worth preserving if you touch `SIGNATURES`: a
wrong `relevant` costs one wasted inspection, a wrong `irrelevant` silently
drops evidence. So anything unrecognised is `unknown`.

## Start from `--sheets`

`triage --sheets` gives you a draft pointer per sheet with every mechanical field
already correct: `file_id`, `member_path`, `locator`, `header_row`, `n_rows`,
`n_columns`, `columns`, a suggested `content_type` and its `relevance`. What is
missing is `description` — what the table is *for* — which is the judgement you
are here to make. Add it, set `evidence` to the rung you stopped on, and write
the list back as `tables`.

Carry the `relevance` through onto the pointer, including for the irrelevant
ones. A pointer that says "this sheet is an antibody list, irrelevant" accounts
for the sheet, so a later reader knows it was looked at.

Check the suggested `content_type` rather than trusting it: it comes from
column-name patterns, and patterns collide. The `relevance_note` names the
columns that drove the guess, which makes it quick to check.

## How to index — cheapest evidence first

Work down this ladder and stop as soon as you can characterise a table. Record
which rung you stopped on in the pointer's `evidence` field, so a reader can
tell a table described from its caption from one you actually opened.

1. **Captions** (`evidence: "caption"`). Run `inventory` and read the labels and
   captions. Publishers often describe the contents precisely — "Supplementary
   Tables 1–40", "Source Data Figs. 2 and 4". If a caption fully accounts for a
   file, you are done with it.
2. **A legend sheet** (`evidence: "legend_sheet"`). Multi-sheet workbooks and
   table bundles frequently carry a contents or legend sheet describing all the
   others. `outline` the file; if a sheet name or its first rows look like a
   legend, `slice` that one sheet and use it to characterise its siblings. One
   read then covers the whole bundle — this is the highest-leverage step, so try
   it before opening anything else.
3. **Headers** (`evidence: "headers"`). Otherwise `outline` each file. Sheet
   names plus the header row usually settle what a table is: `avg_log2FC` and
   `p_val_adj` mean DEG results; a cluster column beside a name column means a
   cluster-to-name mapping; one row per barcode means cell metadata.
4. **Rows** (`evidence: "rows_read"`). Only when the headers are genuinely
   ambiguous, `slice` a few data rows.

Mind the `header_row_guess` that `outline` reports. Publisher tables routinely
carry a title row above the real header ("Prenatal skin metadata"), and
sometimes two. The guess is usually right, but check it against the sample rows
before recording `header_row` — a reader that slices from the wrong row gets
nonsense.

## Describing the units: fan out to cheap judges

The ladder above is how *you* would characterise a bundle by hand. On a
forty-table supplement you should not: it is forty shallow judgements —
read the columns, say what the table is for — and they are better spent on a
cheap model in parallel than on your own context.

`atlas_chat.services.supplement_assess` does everything around those judgements
and none of them. It opens the files, bounds what is read, and hands you one
block per unit; you fan those out to `assess-supplement-content` subagents
(Haiku), collect what they say, and hand the verdicts back.

```bash
# 1. Prepare. Writes prose to disk under the paper directory and prints one
#    evidence block per unit — every sheet, plus every prose document.
uv run python -m atlas_chat.cli_supplement_assess units \
  --store <store> --doi <doi> [--cas <cas.json>] --out units.json

# 2. Judge — one assess-supplement-content subagent per unit, launched in
#    parallel. Give each the roster block and its own unit verbatim.

# 3. Record. Merges the verdicts into the manifest's `tables` and `prose`.
uv run python -m atlas_chat.cli_supplement_assess record \
  --store <store> --doi <doi> --verdicts verdicts.json
```

`--cas` is worth passing whenever the project has one. It puts the project's
real cell-type labels in front of the judge, which is what lets it recognise
`LC_1` or `mCL2` as a cell type at all. Without it the question is asked in
general terms and the answers are weaker.

**`verdicts.json` is an object keyed by `unit_id`** — copy each id back
verbatim from `units.json`. A verdict filed under a mangled id does not match
its unit, and `record` reports that unit as unassessed rather than guessing:

```json
{
  "table|MOESM4.zip|s4/Supplementary Table 22.xlsx|Sheet1": {
    "description": "Differential expression per macrophage subset ...",
    "mentions_cell_types": true,
    "mentions_cell_types_note": "block headers name four subsets"
  }
}
```

`record` exits 2 when any unit went unjudged and writes each as a `gap`. Re-run
those units rather than accepting the gaps — a unit nobody judged is unread, and
in a manifest an absent pointer reads as "there is nothing here".

### Prose and tables are used differently

The judge answers the same two questions for both, but the answers do different
work, and this is what `mentions_cell_types` is for:

- **Prose that names cell types is read whole**, alongside the paper text. It
  has no columns to slice and these documents are small — Gopee's table legends
  and Supplementary Discussion come to about 15 KB together, and the legends are
  where Supplementary Table 22 announces itself as the marker table for the four
  macrophage subsets.
- **Tables are never folded into a context**, however relevant. They get a
  description and their columns, and a reader slices what it needs. Supplementary
  Table 5 in the same bundle is 95 MB and 396,877 rows.

So there is no fold-in judgement to make: the format decides it. Do not fold a
spreadsheet into a context because its description sounds relevant.

### Bounded reads, again

Every unit is judged from a bounded view — a sheet from its columns and five
rows, a long document from its head, middle and tail. The evidence block says
which, and the pointer records it in `evidence`.

This means **a `mentions_cell_types: false` from a bounded read says "none in
what was seen", not "none in the file"**. `mentions_cell_types_note` should say
so, and nothing downstream may upgrade it into a claim that the unit is empty.

### When content feeds CAS+

Some of what a table holds is a fact about the atlas rather than per-cell-type
evidence — a cluster-to-name mapping, author full names, grounded synonyms — and
belongs in the project's CAS+ document once rather than in every run. When
`generate-cas` takes something from a unit, it stamps the pointer so a later run
can tell a CAS-supplied fact from a paper-found one:

```bash
uv run python -m atlas_chat.cli_supplement_assess cas-uptake \
  --store <store> --doi <doi> --unit-id "<unit_id>" \
  --note "cluster names taken into CAS+ cell_fullname" --at "<ISO-8601 UTC>"
```

The note survives re-assessment: `record` preserves any `cas_uptake` already on
a pointer, because it records something this pass knows nothing about.

## Writing the manifest

Read the current manifest with `show`, add your `tables` and `gaps`, and write
the whole file back with `Write`. A PostToolUse hook validates it against the
schema and rejects a table that points at a file which isn't there, so run
`check` if you want the same verdict before writing.

Keep these in mind:

- **Leave the `paper` block alone.** It carries the DOI and, if known, the
  PMCID — nothing else. Role, title and organism belong to the corpus's CAS+
  document; copying them into a fetch cache just creates a second copy that goes
  stale.
- **One pointer per table**, not per file. A workbook with twelve sheets that
  each hold different DEG comparisons is twelve pointers.
- **`description` is what the pointer is for.** Say what the table contains and
  what someone would use it for, in a sentence or two, grounded in what you
  actually read. "DEG results per cluster" is thin; "differential expression of
  each fine-grained cluster against all other cells in the same broad lineage,
  with log fold change and adjusted p-values" tells a reader whether it answers
  their question.
- **Columns matter as much as the table.** A reader picks a table by its columns
  without opening it. Give every column, in order, and describe the ones whose
  headers are not self-explanatory.
- **Do not enumerate which cell types appear.** That is a query-time question
  and the lists are long, stale-prone, and rarely complete.
- **Prose is not a table.** A Supplementary Discussion or a table-legends
  document has no header row and no columns, so it belongs in `prose`, not in
  `tables`. A bundle whose legends document has nowhere to go reads as though it
  did not have one.
- **Record what you couldn't do.** An empty `tables` list with no `gaps` reads
  as "this paper has no useful supplements", which is a claim. If a table was
  over the size cap, a PDF had no extractable text, or a file was never
  retrieved, say so in `gaps` with what a human could do about it. This is the
  difference between "there is nothing there" and "we didn't look".
- Stamp `indexed_at` when you finish
  (`touch_indexed_at` in the service, or write it yourself).

## Where the store lives

The store root is an argument, never derived. For a project the convention is
`projects/{project}/supplements/`, giving
`supplements/papers/<doi-slug>/{manifest.json, files/}`. Nothing in the service
knows that convention, so the same store works outside this repo.
