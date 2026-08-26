# Supplementary material: what a real corpus looks like

**August 2026.** Findings from building supplement retrieval and indexing (#21)
against the HCA reproductive atlas corpus — 22 papers across eight publishers —
with the prenatal skin atlas (Gopee et al. 2024) as a second reference. Every
number below was measured, not estimated; the code that produced them is
`services/supplement_{store,fetch,triage}.py` on `feature/supplement-retrieval`.

Written to be reusable: for tuning retrieval and indexing, for the retrieval
strategy evaluation (ROADMAP §5 B0), and as a source of concrete numbers if any
of this is published.

---

## 1. The corpus

The atlas paper plus the 21 subatlas DOIs in
`projects/HCA_reproductive_atlas_v1/subatlas_pubs`:

| Publisher | Papers |
|---|---|
| Springer Nature | 10 |
| Elsevier / Cell Press | 4 |
| JCI | 2 |
| AAAS | 2 |
| Wiley, Oxford, PNAS, bioRxiv | 1 each |

Deliberately not a single-publisher sample — the failure modes below are almost
all publisher-specific, and two examples from one journal is how we became
over-confident before.

---

## 2. What is reachable

| Stage | Papers |
|---|---|
| In the corpus | 22 |
| Have a PMC record | 17 |
| Have a served article XML (so filenames **and** captions) | **14** |
| Fully retrieved, nothing missing | **14** |

Of 114 files listed across those papers: **103 retrieved, 11 deliberately
skipped, 0 missing**. 434 MB on disk.

The 8 unreachable papers split into two kinds, and the distinction matters
because only one of them is fixable by us:

- **5 have no PMC record at all** (a 2025 Science paper, an Oxford paper, a very
  recent Cell Press paper, a Nature Medicine paper, and the atlas preprint
  itself). No programmatic route exists.
- **3 have a PMC record but no open full text.** Europe PMC knows them and flags
  `hasSuppl`, but serves neither article XML nor supplements.

**Implication.** A corpus of recent, high-profile papers will sit around 60-65%
programmatic reachability. Setup must treat manual supply as a normal route, not
an error path, and must say per paper which one it is — "no PMC record" needs a
human, whereas "closed full text" may open later.

---

## 3. Retrieval routes: what works

Measured route by route.

| Route | Verdict | Evidence |
|---|---|---|
| **Article XML** (`fullTextXML`) | Essential, first | The only source of publisher captions; reaches 14/22 |
| **Europe PMC bundle** (`supplementaryFiles`) | The workhorse | Produced **102 of 103** retrieved files, with no publisher-specific code |
| **Publisher-direct** | Necessary fallback | Produced 1 file — the one the bundle served corrupt |
| **NCBI OA package** (`oa.fcgi` → tar.gz) | **Dead** | Advertised for 14/17 PMC papers; every URL 404s over https regardless of licence, ftp returns nothing |
| **PNAS suppl URLs** | Blocked | HTTP 403 behind bot protection; would need TLS impersonation |

The bundle's virtue is that it needs no per-publisher knowledge: its members are
named exactly as the article XML lists them, so wanted files can be extracted
and the figure images that make up most of its bulk discarded. Its costs are
that it is all-or-nothing per article and occasionally corrupt (§4).

Springer's ESM filename stem turns out to be derivable from the DOI alone
(`10.1038/s41586-024-08002-x` → `41586_2024_8002_`), verified on 8 of 8 Springer
papers. That is what makes publisher-direct viable as a fallback without a
scraping step.

**Bundle sizes** (why there is a cap): most are 10-30 MB; a 34-file PNAS article
is 197 MB, mostly figure images we discard; the prenatal skin atlas exceeds
445 MB because of a supplementary video. The cap is 250 MB, and bytes spool to
disk past 32 MB so a generous cap costs disk rather than RAM.

---

## 4. Failure modes found by running it

None of these are in any documentation. All were found against real papers, and
each one would have produced a plausible-looking wrong answer.

1. **Europe PMC serves corrupt files.** Its copy of
   `41588_2021_972_MOESM3_ESM.xlsx` is 18,480,936 bytes where the publisher
   serves 35,702,391 — truncated so that no zip reader can open it. The bundle
   member *declares* the truncated size, so extraction succeeds and the file is
   stored with a checksum. **Every retrieved payload is now verified to be
   structurally the format it claims**, and a failed check falls through to the
   next route, which recovered the intact file.
2. **`HTTP 200` with an empty body.** For a PMC paper whose full text is not
   open, `supplementaryFiles` returns 165 bytes of non-zip. Stored naively that
   is an empty archive recorded as success, and the paper looks as though it has
   no supplements.
3. **A `.xlsx` extension is a claim, not a fact.** One truncated file raised
   `BadZipFile` out of openpyxl and killed a whole corpus run.
4. **Declared spreadsheet dimensions lie in two directions.** openpyxl reports
   `max_row` as `None` when a workbook carries no dimension record; and a
   workbook can declare a round extent (`A1:Z1000`) because formatting was
   applied past the data — a 9-row table claiming 1000 rows. Since `n_rows` is
   what tells a reader whether to slice or read whole, small declarations are
   now verified by streaming and large ones trusted (a 396,880-row sheet costs
   18 s to scan and its declaration is accurate).
5. **A paper with no article XML was never offered the bundle**, because nothing
   was listed to want — so closed-full-text-but-open-supplements could not be
   discovered.
6. **Header detection degraded with sample size.** Asking to *see* two rows made
   the header guess look at two rows, so a sheet with two title rows above its
   header reported row 0. How much a caller wants displayed must not change what
   is found.

---

## 5. Where the evidence actually is

### Captions

| Caption length | Files | Share |
|---|---|---|
| under 40 chars ("Supplementary Information") | 88 | 77% |
| 40-200 chars | 22 | 19% |
| 200-1000 | 2 | 2% |
| over 1000 — effectively a legend | 2 | 2% |

Captions are weak **on average** and occasionally decisive. The caption for
Garcia-Alonso et al. 2021's supplementary workbook is **6,108 characters and
describes all 19 tables individually**, which was enough to write pointers for
all 42 sheets of that file without opening a single one beyond reading headers.

**Implication.** Always read captions — they arrive free with the article XML —
but never depend on them. And never read an uninformative caption as evidence of
irrelevance: 77% of files would be wrongly discarded.

### Sheet names

Sheet names are the most consistently useful cheap signal, because they name the
comparison or the subset: `SupplementalTable2_early-vs-pro`, `MΦ subtype`,
`FIB subtype`, `SE_up_proliferative`, `jasin_male_filtered_markers_mnn`. Where
they are uninformative (`Table1`…`Table19c`), a legend usually exists elsewhere.

A separate legends **document** inside the bundle — the Gopee case, where
`Supplementary Table legends.docx` describes all forty tables in ~11,000
characters — is rare. Only 13 of 107 spreadsheets have an index-like sheet at
all, and 12 of those are the same `Abbreviations` sheet repeated across one
paper's files (a genuine `Column | Description` data dictionary, worth one read
for all its siblings).

### Column headers

The workhorse. A sheet headed `names / scores / logfoldchanges / pvals_adj` is
differential expression; `cluster / gene / avg_log2FC / pct.1 / pct.2` is
per-cell-type markers; `RRID citation / Antibody / Vendor / Cat no` is a reagent
list. **Dialects matter**: Seurat says `avg_log2FC`, scanpy `logfoldchanges`,
edgeR/limma `logFC` with `F` and `FDR`, DESeq2 `log2FoldChange` with `baseMean`.
Matching one dialect leaves most real DEG tables unrecognised — this was the
first thing the corpus corrected.

---

## 6. What the corpus contains

Recognised content, by paper (of the 14 retrievable):

| Content | Papers |
|---|---|
| Differential expression | **11** |
| Sample / donor metadata | 8 |
| Per-cell tables (label transfer, predictions) | 2 |
| Enrichment results | 1 |
| Marker list | 1 |
| Cluster-to-name mapping | **1** |
| Abundance per cell type | 1 |

**The important asymmetry: 11 papers have DEG tables, one has a cluster-to-name
mapping.** Marker evidence is abundant in supplements; cell-type *naming* is
almost absent from them. Since name resolution is what the whole downstream flow
depends on, this is the most consequential finding here.

### Are the mappings in the PDFs?

Tested directly: text extracted from all 21 supplementary PDFs and searched.
Five showed a cluster-to-name signal; on inspection three were methods prose or
figure legends about clustering. **Two were real**:

> "Clusters 0 and 9 were annotated as Stromal-1 and Stromal-2; clusters 12, 17,
> and 20 were annotated as SMC-1, SMC-2 and SMC-3"
> — jci.insight.153921 supplement

> "According to cell identity annotation and known marker genes … we confirmed
> that mCL2, mCL6, and mCL14 were Sertoli cells"
> — devcel.2024.01.006 supplement

The second is exactly the opaque-label case the roadmap names (`mCL2` → Sertoli
cells). Both are **prose, not tables**.

**Implication.** PDF supplements do not need table extraction; they need their
text in the snippet index, which already exists for PDFs
(`services/local_snippet_index.py`). That is a much cheaper mechanism than
layout reconstruction, and it is the right home for naming evidence. Hit rate is
low (2/21), so priority stays low — but the payoff is the hardest case in the
workflow.

---

## 7. Cost

The expensive-looking part is cheap; the cheap-looking part is slow.

| Quantity | Value |
|---|---|
| Spreadsheet items to index | 107 (of 131 relevant-or-unknown) |
| Sheets within them | 394 |
| Combined rows | 3,299,043 |
| Digest for the **whole corpus** (names, dimensions, header row, 2 sample rows) | **133 KB ≈ 34k tokens** |
| Mean digest per file | 1.2 KB ≈ 320 tokens |
| Largest single file (42 sheets) | 15 KB |

So indexing a 22-paper corpus is **one modest model call per file** — about 107
calls and 34k tokens of input in total. Retrieval, by contrast, took minutes of
wall clock, almost all of it waiting on bundle downloads.

**Implication.** Do not price indexing per sheet (394) — price it per file
(107). And do not optimise indexing cost before retrieval throughput; the
bottleneck is I/O, and `fetch_corpus` is still serial.

Bounded reads are what make this possible: a 396,880-row × 88-column sheet
describes itself in about 2 seconds, and no supplement file is ever loaded whole
into a model's context.

---

## 8. Triage: what it is and isn't worth

Two-stage relevance judgement — captions before fetching, column signatures
after.

| Verdict | Reproductive atlas | Prenatal skin |
|---|---|---|
| relevant | 53% | 65% |
| unknown | 39% | 24% |
| irrelevant | **8%** | **13%** |

**Triage excludes little.** On the reproductive corpus the exclusions are 11
files (8%) and all of them from captions — Reporting Summaries and Peer Review
files. The column-signature stage excluded nothing there, because that corpus has
no reagent or gene-set tables; on the prenatal skin bundle it excluded three
(antibody list, gene-set definitions, and one more).

Its real value is different, and worth stating plainly so it isn't oversold as a
cost saver: **it hands the indexer a kind and a reason for about half the
items**, so the model starts from a hypothesis instead of a blank sheet. Roughly
40% remains `unknown`, most of it PDFs whose columns cannot be read at all.

**The asymmetry to preserve.** A wrong `relevant` costs one wasted inspection; a
wrong `irrelevant` silently loses evidence. So anything unrecognised is
`unknown`, and `unknown` is indexed. One near-miss proved the point: the Human
Protein Atlas secreted-protein table has an `Antibody` column and was ruled a
reagent list — a wrong answer for a plausible reason. A reagent list now needs a
supplier column too.

---

## 9. Indexing output, and one schema limitation

Four papers indexed as a sample, chosen to stress different shapes:

| Paper | Files | Pointers | Route to the description |
|---|---|---|---|
| jci.insight.195254 | 10 | 10 | Sheet names carried the comparison |
| s41588-021-00972-2 | 3 | **42** | The 6 KB caption legend, all 42 sheets matched |
| devcel.2024.01.006 | 7 | 7 | Captions carried the table titles |
| s41467-024-55440-2 | 18 | 88 | Sheet names plus an `Abbreviations` dictionary |

147 pointers, every manifest schema-valid and cross-check clean.

**Limitation found:** `content_type` is too coarse. Of the 42 pointers for
Garcia-Alonso, 34 came out `other` — TF activity scores, CellPhoneDB
interactions, confusion matrices, reagent lists and enrichment results all
collapse into one value. Descriptions carry the meaning, but the enum cannot be
used to filter, which is what a query-time consumer will want. Worth extending
with at least `enrichment`, `interaction` and `reagents`.

**Also:** relevance is recorded per file and per archive member, but not per
sheet — and a 42-sheet workbook mixes DEG tables with antibody lists. Pointers
currently carry that distinction implicitly via `content_type` and description.
If sheet-level filtering matters, relevance belongs on `TablePointer`.

---

## 10. What this says about the strategy

1. **Bundle-first, publisher-direct as a verified fallback.** 102 of 103 files
   came from a route that needs no publisher-specific code. Resist adding
   templates until a corpus demands one.
2. **Verify every payload.** A route returning bytes is not a route returning
   the file. This is cheap and caught a real corruption.
3. **Expect a third of a corpus to need a human**, and design setup to say which
   third and why.
4. **Captions are free, weak, and occasionally decisive** — always read, never
   depend, never read silence as irrelevance.
5. **Indexing is cheap; batch per file.** 34k tokens for 22 papers.
6. **Retrieval is the bottleneck.** Parallelising `fetch_corpus` is the next real
   speed-up; it is currently serial.
7. **Supplements are a marker source, not a naming source.** For naming, route
   PDF text into the snippet index rather than building table extraction.
8. **For the retrieval evaluation (§5 B0):** supplements are now on disk for 14
   of 22 papers, so marker recall can finally be scored per source. Score body
   text and supplements separately — and stratify by whether the paper was
   reachable at all, or the arm that happened to draw the 8 unreachable papers
   will lose for the wrong reason.

---

## Reproducing this

```bash
# retrieve a corpus from its CAS+ document
python -m atlas_chat.cli_supplements fetch --store S --cas projects/<p>/cas.json
python -m atlas_chat.cli_supplements unpack --store S --doi <doi>
python -m atlas_chat.cli_supplements triage --store S --doi <doi>
# then the index-supplements skill over what triage returns
```

Manifests are the durable artifact and are committed; the supplement bytes are
git-ignored. The store used for this report was built at `/tmp/repro_v2` from
the 22 DOIs listed above and is reproducible from that one `fetch` command.
