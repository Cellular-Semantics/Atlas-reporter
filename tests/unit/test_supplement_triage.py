"""Unit tests for relevance triage.

The signatures are a judgement about the aim — which files could describe cell
types and their properties — so these tests pin that judgement on the column
shapes real supplements actually have. Every column set below was taken from a
paper in the reproductive-atlas or prenatal-skin corpora.

The asymmetry that matters: a false ``relevant`` costs one wasted inspection, a
false ``irrelevant`` silently drops evidence. So the unmatched case must be
``unknown``, never ``irrelevant``.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from atlas_chat.services import supplement_triage as triage

pytestmark = pytest.mark.unit


def _table(columns: list[str], data: list[list[str]] | None = None, locator="Sheet1") -> dict:
    rows = [columns] + (data or [])
    return {"locator": locator, "rows": rows, "header_row_guess": 0, "n_rows": len(rows)}


# ------------------------------------------------------------------
# Column signatures, against real column sets
# ------------------------------------------------------------------


@pytest.mark.parametrize(
    ("columns", "verdict", "content_type", "source"),
    [
        # scanpy / Seurat differential expression
        (
            ["names", "scores", "logfoldchanges", "pvals", "pvals_adj"],
            "relevant",
            "deg_results",
            "Gopee Supplementary Table 22, macrophage subsets",
        ),
        (
            ["gene", "avg_log2FC", "p_val_adj", "cluster"],
            "relevant",
            "deg_results",
            "JCI insight, epithelium markers",
        ),
        # edgeR / limma dialect — the case that first came back unknown
        (
            ["description", "ensembl_gene_id", "F", "FDR", "gene_biotype"],
            "relevant",
            "deg_results",
            "JCI insight 195254, early-vs-proliferative",
        ),
        # DESeq2 dialect
        (["gene", "baseMean", "log2FoldChange", "padj"], "relevant", "deg_results", "DESeq2"),
        # cluster-to-name mapping — what name resolution depends on
        (["cluster", "annotation"], "relevant", "cluster_annotation", "typical"),
        (
            ["No.", "Microenvironment label"],
            "unknown",
            None,
            "Gopee Table 40 — 'label' without 'cluster' does not match",
        ),
        # enrichment
        (
            ["Gene_set", "Term", "Overlap", "P-value", "Adjusted P-value", "Odds Ratio"],
            "relevant",
            "enrichment",
            "Gopee Table 24, GSEA for iron-recycling macrophages",
        ),
        # interactions
        (
            ["gene_pair", "celltype_pair", "mean", "p", "padj"],
            "relevant",
            "interaction",
            "Gopee Table 28, CellPhoneDB",
        ),
        (["ligand", "target", "weight"], "relevant", "interaction", "Gopee Table 36, NicheNet"),
        # per-cell label transfer
        (
            ["", "LR_assignment", "Adipocyte", "B cell", "DC"],
            "relevant",
            "cell_metadata",
            "Gopee Table 10, murine projection",
        ),
        # sample metadata
        (["Sanger_id", "Donor", "PCW", "Sorting"], "relevant", "sample_metadata", "Gopee Table 1"),
        (["subject", "phase", "bmi"], "relevant", "sample_metadata", "JCI insight Figure 1B"),
        # abundance
        (
            ["PCW", "Donor", "Annotation_Fine", "Counts"],
            "relevant",
            "sample_metadata",
            "Gopee source data Fig 2b — matches on Donor first",
        ),
        # not relevant: inputs, not findings
        (
            ["RRID citation", "Antibody", "Vendor", "Cat no", "Clone"],
            "irrelevant",
            "reagents",
            "Gopee Table 38, antibodies",
        ),
        (
            ["positive regulation of angiogenesis (GO:0045766)"],
            "irrelevant",
            "gene_set",
            "Gopee Table 27, gene-set definitions",
        ),
    ],
)
def test_classify_table(columns, verdict, content_type, source) -> None:
    got_verdict, got_type, note = triage.classify_table(_table(columns))

    assert got_verdict == verdict, f"{source}: {note}"
    if content_type is not None:
        assert got_type == content_type, source


def test_unmatched_columns_are_unknown_not_irrelevant() -> None:
    """The asymmetry: a wrong 'irrelevant' silently drops evidence."""
    verdict, content_type, note = triage.classify_table(_table(["alpha", "beta", "gamma"]))

    assert verdict == "unknown"
    assert content_type is None
    assert "matched no signature" in note


def test_a_table_with_no_readable_header_is_unknown() -> None:
    verdict, _, note = triage.classify_table({"rows": [], "header_row_guess": 0})

    assert verdict == "unknown"
    assert "no header row" in note


def test_barcodes_make_a_table_relevant_despite_opaque_headers() -> None:
    """One row per cell is evidence about cell types whatever the columns say."""
    table = _table(
        ["", "0", "1", "2"],
        [["AAACCTGGTCAGTGGA-1-4834STDY7002879", "0.8", "0.1", "0.1"]],
    )

    verdict, content_type, note = triage.classify_table(table)

    assert verdict == "relevant"
    assert content_type == "cell_metadata"
    assert "barcode" in note


def test_columns_are_read_from_the_detected_header_row() -> None:
    """Publisher tables carry title rows; reading row 0 would see the title."""
    table = {
        "locator": "Sheet1",
        "rows": [
            ["DEG analysis for macrophage subpopulations"],
            ["", "names", "scores", "logfoldchanges", "pvals_adj"],
            ["", "DAB2", "150.7", "4.18", "0"],
        ],
        "header_row_guess": 1,
    }

    assert triage.columns_of(table) == {"names", "scores", "logfoldchanges", "pvals_adj"}
    assert triage.classify_table(table)[0] == "relevant"


# ------------------------------------------------------------------
# Captions
# ------------------------------------------------------------------


@pytest.mark.parametrize(
    ("entry", "expected"),
    [
        ({"caption": "Reporting Summary"}, "irrelevant"),
        ({"label": "Peer Review file"}, "irrelevant"),
        ({"caption": "Editorial policy checklist"}, "irrelevant"),
        # Uninformative captions must not be read as irrelevance: sixteen files
        # in the reproductive-atlas corpus say only this.
        ({"caption": "Supplementary Information"}, None),
        ({"caption": "Data S1 to S8"}, None),
        ({"label": "Supplementary Tables", "caption": "Supplementary Tables 1-40."}, None),
        ({}, None),
    ],
)
def test_classify_caption_rules_out_only_the_certain_cases(entry: dict, expected) -> None:
    result = triage.classify_caption(entry)

    assert (result[0] if result else None) == expected


# ------------------------------------------------------------------
# Triaging a stored paper
# ------------------------------------------------------------------


@pytest.fixture
def stored(tmp_path: Path):
    """A store holding one workbook, one reagent list and one peer review PDF."""
    openpyxl = pytest.importorskip("openpyxl")
    from atlas_chat.services.supplement_store import MANIFEST_VERSION, write_manifest

    files = tmp_path / "papers" / "10.1038_test" / "files"
    files.mkdir(parents=True)

    degs = files / "tables.xlsx"
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["names", "logfoldchanges", "pvals_adj"])
    sheet.append(["DAB2", 4.18, 0.0])
    wb.save(degs)

    reagents = files / "antibodies.xlsx"
    wb2 = openpyxl.Workbook()
    s2 = wb2.active
    s2.append(["RRID citation", "Antibody", "Vendor"])
    s2.append(["AB_123", "anti-CD45", "Abcam"])
    wb2.save(reagents)

    review = files / "review.pdf"
    review.write_bytes(b"%PDF-1.4 peer review")

    manifest = {
        "manifest_version": MANIFEST_VERSION,
        "paper": {"doi": "10.1038/test"},
        "files": [
            {
                "file_id": "tables.xlsx",
                "media_type": "xlsx",
                "status": "present",
                "path": "papers/10.1038_test/files/tables.xlsx",
            },
            {
                "file_id": "antibodies.xlsx",
                "media_type": "xlsx",
                "status": "present",
                "path": "papers/10.1038_test/files/antibodies.xlsx",
            },
            {
                "file_id": "review.pdf",
                "media_type": "pdf",
                "status": "present",
                "caption": "Peer Review file",
                "path": "papers/10.1038_test/files/review.pdf",
            },
            {"file_id": "gone.xlsx", "media_type": "xlsx", "status": "unavailable"},
        ],
    }
    write_manifest(tmp_path, "10.1038/test", manifest)
    return tmp_path


def test_triage_paper_records_a_verdict_for_every_file(stored: Path) -> None:
    manifest = triage.triage_paper(stored, "10.1038/test")

    by_id = {f["file_id"]: f for f in manifest["files"]}
    assert by_id["tables.xlsx"]["relevance"] == "relevant"
    assert "logfoldchanges" in by_id["tables.xlsx"]["relevance_note"]
    assert by_id["antibodies.xlsx"]["relevance"] == "irrelevant"
    assert by_id["review.pdf"]["relevance"] == "irrelevant"
    assert "caption" in by_id["review.pdf"]["relevance_note"]
    # Not on disk is not the same as not relevant.
    assert by_id["gone.xlsx"]["relevance"] == "unknown"


def test_indexable_excludes_only_the_irrelevant(stored: Path) -> None:
    manifest = triage.triage_paper(stored, "10.1038/test")

    names = {item["file_id"] for item in triage.indexable(manifest)}

    assert names == {"tables.xlsx"}, "unknown-but-absent files have nothing to open"


def test_triage_is_idempotent(stored: Path) -> None:
    first = triage.triage_paper(stored, "10.1038/test")
    second = triage.triage_paper(stored, "10.1038/test")

    assert [f.get("relevance") for f in first["files"]] == [
        f.get("relevance") for f in second["files"]
    ]


def test_an_unreadable_workbook_is_unknown_not_irrelevant(tmp_path: Path) -> None:
    """Europe PMC's bundle really does serve truncated workbooks."""
    from atlas_chat.services.supplement_store import MANIFEST_VERSION, write_manifest

    files = tmp_path / "papers" / "10.1038_test" / "files"
    files.mkdir(parents=True)
    broken = files / "truncated.xlsx"
    broken.write_bytes(b"PK\x03\x04" + b"\x00" * 200)  # starts like a zip, isn't one

    write_manifest(
        tmp_path,
        "10.1038/test",
        {
            "manifest_version": MANIFEST_VERSION,
            "paper": {"doi": "10.1038/test"},
            "files": [
                {
                    "file_id": "truncated.xlsx",
                    "media_type": "xlsx",
                    "status": "present",
                    "path": "papers/10.1038_test/files/truncated.xlsx",
                }
            ],
        },
    )

    manifest = triage.triage_paper(tmp_path, "10.1038/test")

    entry = manifest["files"][0]
    assert entry["relevance"] == "unknown"
    assert "not a readable .xlsx" in entry["relevance_note"]


def test_archive_members_are_triaged_individually(tmp_path: Path) -> None:
    """A bundle of forty tables is judged per table, not as one blob."""
    openpyxl = pytest.importorskip("openpyxl")
    from atlas_chat.services.supplement_store import MANIFEST_VERSION, write_manifest

    unpacked = tmp_path / "papers" / "10.1038_test" / "files" / "bundle__unpacked"
    unpacked.mkdir(parents=True)
    for name, columns in [
        ("Table 1.xlsx", ["names", "logfoldchanges", "pvals_adj"]),
        ("Table 2.xlsx", ["RRID citation", "Antibody", "Vendor"]),
    ]:
        wb = openpyxl.Workbook()
        wb.active.append(columns)
        wb.save(unpacked / name)

    base = "papers/10.1038_test/files/bundle__unpacked"
    write_manifest(
        tmp_path,
        "10.1038/test",
        {
            "manifest_version": MANIFEST_VERSION,
            "paper": {"doi": "10.1038/test"},
            "files": [
                {
                    "file_id": "bundle.zip",
                    "media_type": "zip",
                    "status": "present",
                    "path": "papers/10.1038_test/files/bundle.zip",
                    "members": [
                        {
                            "member_path": "Table 1.xlsx",
                            "media_type": "xlsx",
                            "extracted": True,
                            "path": f"{base}/Table 1.xlsx",
                        },
                        {
                            "member_path": "Table 2.xlsx",
                            "media_type": "xlsx",
                            "extracted": True,
                            "path": f"{base}/Table 2.xlsx",
                        },
                    ],
                }
            ],
        },
    )

    manifest = triage.triage_paper(tmp_path, "10.1038/test")

    members = {m["member_path"]: m["relevance"] for m in manifest["files"][0]["members"]}
    assert members == {"Table 1.xlsx": "relevant", "Table 2.xlsx": "irrelevant"}
    # The archive is relevant because something inside it is.
    assert manifest["files"][0]["relevance"] == "relevant"
    assert {i["member_path"] for i in triage.indexable(manifest)} == {"Table 1.xlsx"}


@pytest.mark.parametrize(
    ("columns", "verdict", "source"),
    [
        (
            ["RRID citation", "Antibody", "Vendor", "Cat no", "Clonality", "Clone"],
            "irrelevant",
            "Gopee Table 38 — a real antibody list, with a supplier",
        ),
        (
            [
                "Gene",
                "Gene synonym",
                "Ensembl",
                "Antibody",
                "Biological process",
                "Blood concentration",
                "Protein class",
            ],
            "unknown",
            "Gopee Table 39 — the HPA secreted-protein database, which merely has "
            "an Antibody column. Ruling this out as a reagent list would be a "
            "wrong answer for a plausible reason",
        ),
        (["Primer name", "Sequence", "Supplier"], "irrelevant", "a primer list"),
    ],
)
def test_reagent_lists_are_told_apart_from_protein_reference_tables(
    columns: list[str], verdict: str, source: str
) -> None:
    assert triage.classify_table(_table(columns))[0] == verdict, source


def test_no_signature_can_produce_irrelevant_without_naming_its_reason() -> None:
    """Every exclusion must be auditable, since exclusions lose evidence."""
    for signature in triage.SIGNATURES:
        if not signature.relevant:
            assert signature.name, "an excluding signature needs a name for its note"
            assert signature.required or signature.any_of, "and real criteria"


@pytest.mark.parametrize("kind", ["pdf", "docx", "video", "other"])
def test_uninspected_formats_say_so_explicitly(tmp_path: Path, kind: str) -> None:
    """A stated decision, not a silent gap: these are never read for columns."""
    from atlas_chat.services.supplement_store import MANIFEST_VERSION, write_manifest

    files = tmp_path / "papers" / "10.1038_test" / "files"
    files.mkdir(parents=True)
    (files / f"f.{kind}").write_bytes(b"whatever")
    write_manifest(
        tmp_path,
        "10.1038/test",
        {
            "manifest_version": MANIFEST_VERSION,
            "paper": {"doi": "10.1038/test"},
            "files": [
                {
                    "file_id": f"f.{kind}",
                    "media_type": kind,
                    "status": "present",
                    "path": f"papers/10.1038_test/files/f.{kind}",
                }
            ],
        },
    )

    manifest = triage.triage_paper(tmp_path, "10.1038/test")

    entry = manifest["files"][0]
    assert entry["relevance"] == "unknown", "never irrelevant — we simply did not look"
    assert "not inspected" in entry["relevance_note"]


# ------------------------------------------------------------------
# Sheet-level candidates
# ------------------------------------------------------------------


@pytest.mark.parametrize(
    ("columns", "content_type", "source"),
    [
        (
            ["gene", "cluster", "geneFrequency", "secondBestClusterName", "tfidf", "qval"],
            "marker_list",
            "s41586-022-04918-4 TF-IDF markers. 'name' as a substring of "
            "secondBestClusterName once made this a cluster-to-name mapping — the "
            "one field the corpus is short of, where a false positive is worst",
        ),
        (["cluster", "annotation"], "cluster_annotation", "a genuine mapping"),
        (["cluster", "name"], "cluster_annotation", "exact 'name' still counts"),
        (
            ["cluster", "Regulon", "NES", "p.value", "FDR"],
            "enrichment",
            "Dorothea regulon activity",
        ),
        (
            ["SOX9_LGR5--Preciliated", "Ciliated--Ciliated"],
            "interaction",
            "CellPhoneDB matrix: columns are cell-type pairs",
        ),
        (
            ["partner_a", "partner_b", "protein_name_a", "annotation_strategy"],
            "interaction",
            "CellPhoneDB's curated-interaction schema",
        ),
        (
            ["Product", "Description", "Company", "Product Number", "Final Concentration"],
            "reagents",
            "culture-medium components: says Company, not Vendor",
        ),
        (["TF", "target", "effect", "Source"], "gene_set", "a curated regulatory network"),
    ],
)
def test_extended_content_types(columns: list[str], content_type: str, source: str) -> None:
    assert triage.classify_table(_table(columns))[1] == content_type, source


def test_exact_matching_does_not_fire_on_a_substring() -> None:
    """The mechanism behind the marker/mapping fix."""
    sig = triage.Signature("x", "other", True, required=("cluster",), exact_any_of=("name",))

    assert sig.matches({"cluster", "name"}) is True
    assert sig.matches({"cluster", "secondbestclustername"}) is False


def test_sheet_candidates_judges_each_sheet_separately(tmp_path: Path) -> None:
    """The point of sheet-level pointers: one workbook, two different answers."""
    openpyxl = pytest.importorskip("openpyxl")
    from atlas_chat.services.supplement_store import MANIFEST_VERSION, write_manifest

    files = tmp_path / "papers" / "10.1038_test" / "files"
    files.mkdir(parents=True)
    book = files / "mixed.xlsx"
    wb = openpyxl.Workbook()
    degs = wb.active
    degs.title = "DEGs"
    degs.append(["Supplementary Table 4 | DEGs by cluster"])  # a title row
    degs.append(["names", "logfoldchanges", "pvals_adj"])
    degs.append(["DAB2", 4.18, 0.0])
    ab = wb.create_sheet("Antibodies")
    ab.append(["Antibody", "Vendor", "Cat no"])
    ab.append(["anti-CD45", "Abcam", "ab123"])
    wb.save(book)

    write_manifest(
        tmp_path,
        "10.1038/test",
        {
            "manifest_version": MANIFEST_VERSION,
            "paper": {"doi": "10.1038/test"},
            "files": [
                {
                    "file_id": "mixed.xlsx",
                    "media_type": "xlsx",
                    "status": "present",
                    "path": "papers/10.1038_test/files/mixed.xlsx",
                }
            ],
        },
    )

    candidates = triage.sheet_candidates(tmp_path, "10.1038/test")

    by_sheet = {c["locator"]: c for c in candidates}
    assert by_sheet["DEGs"]["relevance"] == "relevant"
    assert by_sheet["DEGs"]["content_type"] == "deg_results"
    # The title row is skipped, so the recorded columns are the real ones.
    assert by_sheet["DEGs"]["header_row"] == 1
    assert [c["name"] for c in by_sheet["DEGs"]["columns"]] == [
        "names",
        "logfoldchanges",
        "pvals_adj",
    ]
    assert by_sheet["DEGs"]["n_rows"] == 1

    assert by_sheet["Antibodies"]["relevance"] == "irrelevant"
    assert by_sheet["Antibodies"]["content_type"] == "reagents"
    # An irrelevant sheet is still returned, so it is accounted for.
    assert len(candidates) == 2


def test_sheet_candidates_omits_description(tmp_path: Path, stored: Path) -> None:
    """What a table is FOR is the skill's judgement, not the service's."""
    candidates = triage.sheet_candidates(stored, "10.1038/test")

    assert candidates
    assert all("description" not in c for c in candidates)
    assert all(c["relevance"] in {"relevant", "irrelevant", "unknown"} for c in candidates)


def test_sheet_candidates_dedupes_repeated_block_columns(tmp_path: Path) -> None:
    """Multi-block sheets repeat a column group per subject."""
    openpyxl = pytest.importorskip("openpyxl")
    from atlas_chat.services.supplement_store import MANIFEST_VERSION, write_manifest

    files = tmp_path / "papers" / "10.1038_test" / "files"
    files.mkdir(parents=True)
    book = files / "blocks.xlsx"
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(["names", "logfoldchanges", "", "names", "logfoldchanges"])
    sheet.append(["DAB2", 4.1, None, "STAB1", 1.6])
    wb.save(book)
    write_manifest(
        tmp_path,
        "10.1038/test",
        {
            "manifest_version": MANIFEST_VERSION,
            "paper": {"doi": "10.1038/test"},
            "files": [
                {
                    "file_id": "blocks.xlsx",
                    "media_type": "xlsx",
                    "status": "present",
                    "path": "papers/10.1038_test/files/blocks.xlsx",
                }
            ],
        },
    )

    candidate = triage.sheet_candidates(tmp_path, "10.1038/test")[0]

    assert [c["name"] for c in candidate["columns"]] == ["names", "logfoldchanges"]
    assert candidate["n_columns"] == 5, "the true width is still reported"
