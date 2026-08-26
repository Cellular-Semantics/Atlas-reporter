"""Decide which supplementary files are worth indexing, cheaply.

A corpus of twenty-odd papers yields a hundred-plus supplementary files, and
most of them have nothing to say about cell types. Deep indexing — opening every
workbook, describing every sheet — is the expensive step, so it should only run
on files that could carry evidence.

Two stages, matching where the information actually is:

**Captions, before any bytes move.** The article XML gives a label and caption
for each file. Some captions settle the question outright: a "Reporting Summary"
or a "Peer Review file" is never evidence about a cell type. Nothing else is
ruled out at this stage — captions like "Supplementary Information" are common
and say nothing, and treating silence as irrelevance would discard real tables.

**Column signatures, after the bytes arrive.** ``outline`` is bounded and fast
(a 396,880-row table describes itself in about two seconds), so every candidate
gets outlined and judged on what its columns actually are. A sheet headed
``names / logfoldchanges / pvals_adj`` is differential expression; one whose
first column holds cell barcodes is per-cell metadata; one headed
``RRID citation / Antibody / Vendor`` is a reagent list and no report will ever
cite it.

What counts as relevant is one editable table, :data:`SIGNATURES`, because it is
a judgement about the aim rather than a fact about spreadsheets. As set here:
differential expression, marker lists, cluster-to-name mappings, cell and sample
metadata, enrichment results and cell-cell interactions are relevant, because
each describes a cell type or one of its properties. Reagent lists and gene-set
definitions are not — they are inputs to an analysis, not findings about cells.
Figure source data is relevant only when it carries a cell-type column, which is
the difference between per-cell-type abundances and image quantification.

Anything the signatures do not match comes back ``unknown`` rather than being
guessed at, and a reader settles it. Silence is never read as irrelevance.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any

from atlas_chat.services.supplement_store import (
    SupplementStoreError,
    load_manifest,
    outline_file,
    write_manifest,
)

logger = logging.getLogger(__name__)

#: Captions that settle irrelevance on their own. Deliberately short: these are
#: publishing-process artefacts, not judgement calls. Everything else waits for
#: its columns to be seen.
NON_EVIDENCE_CAPTIONS = (
    "reporting summary",
    "peer review file",
    "peer review information",
    "reporting checklist",
    "author checklist",
    "editorial policy checklist",
)

#: A 10x-style cell barcode, the giveaway that a table has one row per cell.
BARCODE_RE = re.compile(r"^[ACGT]{12,20}(-\d+)?([-_].+)?$")


class Signature:
    """One recognisable kind of supplementary table.

    Args:
        name: What to call it in a note.
        content_type: The manifest ``TablePointer.content_type`` it maps to.
        relevant: Whether a table of this kind bears on describing cell types.
        required: Column names that must all be present, matched as substrings —
            loose on purpose, so ``logfoldchange`` catches ``logFoldChanges``.
        any_of: Column names of which at least one must be present, as substrings.
        exact_any_of: As ``any_of``, but matched against the whole column name.
            For tokens that collide: "name" as a substring matches
            ``secondBestClusterName`` in a TF-IDF marker table, which is how a
            marker table came to be labelled a cluster-to-name mapping.
    """

    def __init__(
        self,
        name: str,
        content_type: str,
        relevant: bool,
        required: tuple[str, ...] = (),
        any_of: tuple[str, ...] = (),
        exact_any_of: tuple[str, ...] = (),
    ):
        self.name = name
        self.content_type = content_type
        self.relevant = relevant
        self.required = required
        self.any_of = any_of
        self.exact_any_of = exact_any_of

    def matches(self, columns: set[str]) -> bool:
        if self.required and not all(
            any(req in column for column in columns) for req in self.required
        ):
            return False
        if self.any_of or self.exact_any_of:
            loose = any(any(opt in column for column in columns) for opt in self.any_of)
            exact = any(opt in columns for opt in self.exact_any_of)
            if not (loose or exact):
                return False
        return bool(self.required or self.any_of or self.exact_any_of)


#: Order matters: the first match wins, so the specific precede the general.
SIGNATURES: tuple[Signature, ...] = (
    # --- relevant: findings about cell types ------------------------------
    # Interactions first: a CellPhoneDB table's `gene_pair` contains "gene" and
    # its `padj` looks like differential expression, so the general DEG
    # signatures would claim it and mislabel what it is.
    Signature(
        "cell-cell interaction",
        "interaction",
        True,
        any_of=("celltype_pair", "gene_pair", "test_ligand"),
    ),
    Signature(
        "cell-cell interaction",
        "interaction",
        True,
        required=("ligand",),
        any_of=("target", "receptor", "weight"),
    ),
    # Differential expression, however the tool that produced it named things.
    # Seurat says avg_log2FC, scanpy says logfoldchanges, edgeR and limma say
    # logFC with an F statistic and an FDR, DESeq2 says log2FoldChange with a
    # baseMean. Matching only one dialect leaves most real DEG tables unjudged.
    Signature(
        "differential expression",
        "deg_results",
        True,
        any_of=("logfoldchange", "avg_log2fc", "log2foldchange", "logfc", "log2fc"),
    ),
    Signature(
        "differential expression",
        "deg_results",
        True,
        required=("fdr",),
        any_of=("gene", "genes", "ensembl_gene_id", "transcript", "names"),
    ),
    Signature(
        "differential expression",
        "deg_results",
        True,
        required=("padj",),
        any_of=("gene", "genes", "basemean", "ensembl_gene_id", "names"),
    ),
    Signature(
        "differential expression",
        "deg_results",
        True,
        required=("pvals_adj",),
        any_of=("names", "gene", "genes"),
    ),
    Signature(
        "marker list",
        "marker_list",
        True,
        required=("marker",),
    ),
    # A column literally named barcode is a per-cell table; the value-sniffing
    # below only catches the case where the barcode is the first column.
    Signature(
        "per-cell table",
        "cell_metadata",
        True,
        any_of=("barcode", "cell_id", "cell id", "cellid"),
    ),
    # clusterProfiler's dialect for enrichment, which names nothing "term".
    Signature(
        "enrichment results",
        "enrichment",
        True,
        any_of=("bgratio", "generatio", "p.adjust", "qvalue"),
    ),
    # A data dictionary describing the other sheets: the legend case, and worth
    # reading first for exactly the reason a legends document is.
    Signature(
        "data dictionary",
        "legend",
        True,
        required=("column",),
        any_of=("description", "definition", "meaning"),
    ),
    # TF-IDF marker tables carry a cluster column and a secondBestClusterName,
    # so they must be claimed here or the cluster signature mislabels them as a
    # naming table — the one field this corpus is short of, where a false
    # positive is worse than none.
    Signature(
        "TF-IDF marker table",
        "marker_list",
        True,
        any_of=("tfidf", "genefrequency"),
    ),
    Signature(
        "cluster-to-name mapping",
        "cluster_annotation",
        True,
        required=("cluster",),
        any_of=("annotation", "cell type", "celltype", "cell_type", "cell state"),
        exact_any_of=("name", "label", "cluster name", "cluster_name", "cell name"),
    ),
    # An interaction matrix names cell-type PAIRS in its columns
    # ("SOX9_LGR5--Preciliated"), which no other kind of table does.
    Signature(
        "cell-cell interaction matrix",
        "interaction",
        True,
        required=("--",),
    ),
    # CellPhoneDB's own schema for a curated interaction table.
    Signature(
        "curated interactions",
        "interaction",
        True,
        any_of=("partner_a", "partner_b", "interacting_pair"),
    ),
    # TF regulon activity: a normalised enrichment score per regulon per cluster.
    Signature(
        "regulon activity",
        "enrichment",
        True,
        required=("nes",),
        any_of=("regulon", "fdr", "p.value", "cluster"),
    ),
    # The curated TF-target network an activity analysis consumed — an input.
    Signature(
        "regulatory network",
        "gene_set",
        False,
        required=("target",),
        any_of=("regulon", "effect", "tf"),
    ),
    Signature(
        "enrichment results",
        "enrichment",
        True,
        required=("term",),
        any_of=("adjusted p-value", "odds ratio", "combined score", "overlap"),
    ),
    Signature(
        "label-transfer predictions",
        "cell_metadata",
        True,
        any_of=("lr_assignment", "predicted", "prediction"),
    ),
    Signature(
        "sample metadata",
        "sample_metadata",
        True,
        any_of=(
            "donor",
            "sample_id",
            "sanger_id",
            "pcw",
            "gestation",
            "patient",
            "subject",
            "gravida",
            "parity",
            "ethnicity",
        ),
    ),
    Signature(
        "abundance per cell type",
        "cell_metadata",
        True,
        required=("count",),
        any_of=("annotation", "cell type", "celltype", "cluster"),
    ),
    # --- not relevant: inputs and reagents, not findings ------------------
    # A reagent list needs a supplier, not just the word "antibody". The Human
    # Protein Atlas secreted-protein table has an Antibody column beside
    # Biological process and Blood concentration, and ruling that out as a
    # reagent list would be a wrong answer for a plausible-looking reason —
    # the failure direction that silently loses evidence.
    Signature(
        "reagent list",
        "reagents",
        False,
        any_of=(
            "vendor",
            "cat no",
            "catalogue no",
            "catalog no",
            "company",
            "product number",
            "supplier",
            "clonality",
            "dilution",
        ),
    ),
    Signature(
        "gene-set definitions",
        "gene_set",
        False,
        required=("go:",),
    ),
)


def columns_of(table: dict[str, Any]) -> set[str]:
    """Lowercased column names from an outlined table's detected header row."""
    rows = table.get("rows") or []
    index = table.get("header_row_guess", 0)
    if index >= len(rows):
        return set()
    return {str(cell).strip().lower() for cell in rows[index] if str(cell).strip()}


def looks_per_cell(table: dict[str, Any]) -> bool:
    """Whether the first column holds cell barcodes.

    One row per cell means per-cell annotations — abundance, label transfer,
    predicted identity — which is evidence about cell types even when the column
    headers are opaque.
    """
    rows = table.get("rows") or []
    start = table.get("header_row_guess", 0) + 1
    return any(row and BARCODE_RE.match(str(row[0]).strip()) for row in rows[start : start + 3])


def classify_table(table: dict[str, Any]) -> tuple[str, str | None, str]:
    """Judge one outlined table.

    Returns:
        ``(verdict, content_type, note)`` where verdict is ``relevant`` /
        ``irrelevant`` / ``unknown``. ``unknown`` means the signals did not
        settle it and a reader should look — never that it is irrelevant.
    """
    columns = columns_of(table)
    if not columns:
        return "unknown", None, "no header row could be read"

    for signature in SIGNATURES:
        if signature.matches(columns):
            shown = sorted(columns)[:4]
            return (
                "relevant" if signature.relevant else "irrelevant",
                signature.content_type,
                f"columns {'/'.join(shown)} -> {signature.name}",
            )

    if looks_per_cell(table):
        return "relevant", "cell_metadata", "first column holds cell barcodes -> per-cell table"

    return "unknown", None, f"columns {'/'.join(sorted(columns)[:5])} matched no signature"


def classify_caption(entry: dict[str, Any]) -> tuple[str, str] | None:
    """Rule a file out on its caption alone, or return None to keep looking.

    Only the certain cases: a reporting summary or a peer review file cannot
    describe a cell type. An uninformative caption ("Supplementary Information")
    returns None — sixteen files in the reproductive-atlas corpus carry captions
    that say nothing, and reading that as irrelevance would throw away real
    tables.
    """
    described = f"{entry.get('label', '')} {entry.get('caption', '')}".strip().lower()
    if not described:
        return None
    for phrase in NON_EVIDENCE_CAPTIONS:
        if phrase in described:
            return "irrelevant", f"caption: {entry.get('caption') or entry.get('label')}"
    return None


# ------------------------------------------------------------------
# Triaging a whole paper
# ------------------------------------------------------------------

#: Kinds whose columns we read. Deliberately just the delimited and spreadsheet
#: formats: they are where the tables that describe cell types actually live
#: (105 of the 107 inspectable items in the reproductive-atlas corpus are xlsx),
#: and their cost is flat in file size.
#:
#: PDF and docx are left alone on purpose. A Supplementary Information PDF may
#: well carry a cluster-to-name table, but getting at it needs text extraction
#: and layout reconstruction, which is a different and much larger job. They are
#: recorded ``unknown`` with a note saying they were not inspected, so the
#: absence of pointers for them is a stated decision rather than a silent gap.
INSPECTABLE = {"xlsx", "csv", "tsv", "txt"}


def triage_paper(store_root: Path, doi: str) -> dict[str, Any]:
    """Record a relevance verdict for every stored file and archive member.

    Outlines each inspectable file, classifies it from its columns, and writes
    ``relevance`` / ``relevance_note`` into the manifest. Deep indexing then runs
    only over what came back ``relevant`` or ``unknown``.

    Returns:
        The manifest, written to disk.
    """
    manifest = load_manifest(store_root, doi)
    if manifest is None:
        raise SupplementStoreError(f"no manifest for {doi} in {store_root}")

    counts: dict[str, int] = {"relevant": 0, "irrelevant": 0, "unknown": 0}

    for entry in manifest.get("files", []):
        members = entry.get("members") or []
        if members:
            # The archive itself is a container; its members carry the verdicts.
            for member in members:
                verdict, note = _judge(store_root, member, member.get("member_path", ""))
                member["relevance"] = verdict
                member["relevance_note"] = note
                counts[verdict] += 1
            verdicts = {m["relevance"] for m in members}
            entry["relevance"] = (
                "relevant"
                if "relevant" in verdicts
                else ("unknown" if "unknown" in verdicts else "irrelevant")
            )
            entry["relevance_note"] = (
                f"{sum(1 for m in members if m['relevance'] == 'relevant')} of "
                f"{len(members)} members relevant"
            )
            continue

        caption_verdict = classify_caption(entry)
        if caption_verdict:
            entry["relevance"], entry["relevance_note"] = caption_verdict
            counts[entry["relevance"]] += 1
            continue

        verdict, note = _judge(store_root, entry, entry["file_id"])
        entry["relevance"] = verdict
        entry["relevance_note"] = note
        counts[verdict] += 1

    write_manifest(store_root, doi, manifest)
    logger.info(
        "%s: %d relevant, %d irrelevant, %d unknown",
        doi,
        counts["relevant"],
        counts["irrelevant"],
        counts["unknown"],
    )
    return manifest


def _judge(store_root: Path, entry: dict[str, Any], name: str) -> tuple[str, str]:
    """Verdict for one file or archive member."""
    caption_verdict = classify_caption(entry)
    if caption_verdict:
        return caption_verdict

    kind = entry.get("media_type") or ""
    path = entry.get("path")
    if not path:
        return "unknown", "not on disk, so its columns could not be read"
    if kind not in INSPECTABLE:
        return "unknown", (
            f"not inspected: {kind or 'unrecognised format'} — only spreadsheet and "
            "delimited files are read for columns. Its content may still be useful."
        )

    try:
        outline = outline_file(store_root / path, sample_rows=6, max_cols=60)
    except SupplementStoreError as exc:
        return "unknown", f"could not be outlined: {exc}"

    tables = outline.get("tables") or []
    if not tables:
        return "unknown", "no tabular content found"

    # A workbook is relevant if any of its sheets is; the deep index decides
    # which ones. Notes name the sheet that settled it.
    best = ("unknown", "")
    for table in tables:
        verdict, _content_type, note = classify_table(table)
        located = f"[{table.get('locator')}] {note}" if table.get("locator") else note
        if verdict == "relevant":
            return "relevant", located
        if verdict == "unknown" and best[0] != "unknown":
            best = ("unknown", located)
        elif not best[1]:
            best = (verdict, located)
    return best if best[1] else ("unknown", "no sheet matched a signature")


#: Columns recorded per sheet before the list is treated as a prefix. A
#: label-transfer table has one column per cell state and can run to hundreds;
#: the first two dozen tell a reader what it is.
CANDIDATE_COLUMN_CAP = 25


def sheet_candidates(
    store_root: Path, doi: str, manifest: dict[str, Any] | None = None
) -> list[dict[str, Any]]:
    """One draft pointer per sheet, with everything mechanical already filled in.

    Relevance is a per-sheet property: the same workbook holds the DEG table a
    report needs and the antibody list it never will, so a verdict on the file
    cannot express it. This opens every indexable file once and returns a
    candidate per sheet carrying its locator, header row, dimensions, columns, a
    suggested ``content_type`` and its own relevance verdict.

    What is deliberately absent is ``description`` — what a table is *for* is the
    judgement the indexing skill makes, and inventing it here would be guessing.
    A caller fills that in and writes the result as the manifest's ``tables``.

    Returns:
        Candidates in file then sheet order. Sheets from files triage ruled
        irrelevant are included, marked as such, so nothing is silently absent.
    """
    manifest = manifest or load_manifest(store_root, doi)
    if manifest is None:
        raise SupplementStoreError(f"no manifest for {doi} in {store_root}")

    out: list[dict[str, Any]] = []
    for entry in manifest.get("files", []):
        for item in entry.get("members") or [entry]:
            path = item.get("path")
            kind = item.get("media_type") or ""
            if not path or kind not in INSPECTABLE:
                continue
            try:
                outline = outline_file(store_root / path, sample_rows=6, max_cols=200)
            except SupplementStoreError as exc:
                logger.warning("%s: %s", path, exc)
                continue
            for table in outline.get("tables") or []:
                verdict, content_type, note = classify_table(table)
                header_row = table.get("header_row_guess", 0)
                candidate: dict[str, Any] = {
                    "file_id": entry["file_id"],
                    "locator": table.get("locator"),
                    "content_type": content_type or "other",
                    "relevance": verdict,
                    "relevance_note": note,
                    "columns": _unique_columns(table, header_row),
                    "n_columns": table.get("n_cols", 0),
                    "header_row": header_row,
                    "n_rows": max((table.get("n_rows") or 0) - header_row - 1, 0),
                }
                if item is not entry:
                    candidate["member_path"] = item["member_path"]
                out.append(candidate)
    logger.info("%s: %d sheet candidate(s)", doi, len(out))
    return out


def _unique_columns(table: dict[str, Any], header_row: int) -> list[dict[str, str]]:
    """Column names from the header row, de-duplicated, order preserved.

    Multi-block sheets repeat a group of columns once per subject, so the same
    names recur; recording the distinct set is what a reader needs.
    """
    rows = table.get("rows") or []
    if header_row >= len(rows):
        return []
    seen: list[str] = []
    for cell in rows[header_row]:
        name = str(cell).strip()
        if name and name not in seen:
            seen.append(name)
    return [{"name": name} for name in seen[:CANDIDATE_COLUMN_CAP]]


def indexable(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """The files and members deep indexing should open.

    Everything judged ``relevant`` or ``unknown`` — never the ``irrelevant``.
    Each item carries ``file_id``, optional ``member_path``, ``path``,
    ``relevance`` and ``relevance_note`` so a caller can go straight to it.
    """
    out: list[dict[str, Any]] = []
    for entry in manifest.get("files", []):
        members = entry.get("members") or []
        if members:
            for member in members:
                if member.get("relevance") in {"relevant", "unknown"} and member.get("path"):
                    out.append(
                        {
                            "file_id": entry["file_id"],
                            "member_path": member["member_path"],
                            "path": member["path"],
                            "relevance": member["relevance"],
                            "relevance_note": member.get("relevance_note", ""),
                        }
                    )
            continue
        if entry.get("relevance") in {"relevant", "unknown"} and entry.get("path"):
            out.append(
                {
                    "file_id": entry["file_id"],
                    "path": entry["path"],
                    "relevance": entry["relevance"],
                    "relevance_note": entry.get("relevance_note", ""),
                }
            )
    return out
