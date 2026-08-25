"""Integration tests for the supplement store against real material.

Two kinds of real:

* Europe PMC — the article XML is fetched live, so a change in how they serve
  ``<supplementary-material>`` surfaces here rather than in a run.
* The prenatal skin atlas store in ``projects/test_projects/`` — real Nature
  supplements, including the 95 MB / 396k-row table that motivated giving
  spreadsheets their own size ceiling. Skipped when the files aren't on disk,
  since they are git-ignored; see that project's ``supplements/incoming/README.md``.

No mocks. The Europe PMC test fails hard if the network or the service is down.
"""

from __future__ import annotations

import re

import httpx
import pytest

from atlas_chat.services import supplement_store as store

pytestmark = pytest.mark.integration

ATLAS_DOI = "10.1038/s41586-024-08002-x"
PMCID = "PMC11578897"
EUROPEPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"

REPO_ROOT = __import__("pathlib").Path(__file__).resolve().parents[2]
STORE = REPO_ROOT / "projects" / "test_projects" / "fetal_skin_atlas" / "supplements"


@pytest.fixture(scope="module")
def live_jats(tmp_path_factory: pytest.TempPathFactory):
    """The prenatal skin atlas article XML, fetched from Europe PMC."""
    path = tmp_path_factory.mktemp("jats") / "paper.jats.xml"
    response = httpx.get(f"{EUROPEPMC}/{PMCID}/fullTextXML", timeout=60)
    response.raise_for_status()
    path.write_text(response.text)
    return path


def test_inventory_against_live_europepmc(live_jats) -> None:
    entries = store.inventory_from_jats(live_jats)

    by_id = {entry["file_id"]: entry for entry in entries}
    assert len(entries) == 6

    tables = by_id["41586_2024_8002_MOESM4_ESM.zip"]
    assert tables["label"] == "Supplementary Tables"
    assert tables["caption"].startswith("Supplementary Tables 1")
    assert tables["media_type"] == "zip"

    # The video is listed so a later step can deliberately skip it rather than
    # discovering half a gigabyte of MP4 the hard way.
    assert by_id["41586_2024_8002_MOESM5_ESM.mp4"]["media_type"] == "video"


def test_publisher_direct_serves_individual_files() -> None:
    """The route the retrieval half will use.

    Europe PMC's ``supplementaryFiles`` endpoint bundles every supplement into
    one zip — over 445 MB for this paper, because of the video, with no way to
    select files. The publisher's static host serves them individually, and the
    filenames come from the article XML.
    """
    url = (
        "https://static-content.springer.com/esm/"
        "art%3A10.1038%2Fs41586-024-08002-x/MediaObjects/"
        "41586_2024_8002_MOESM6_ESM.xlsx"
    )
    response = httpx.head(url, follow_redirects=True, timeout=60)

    assert response.status_code == 200
    assert int(response.headers["content-length"]) > 0


# ------------------------------------------------------------------
# The real store
# ------------------------------------------------------------------


def _material_on_disk() -> bool:
    """Whether the supplement *bytes* are here, not just the manifest.

    The manifest is committed; the files it describes are git-ignored, so a
    fresh worktree has the one without the other. Testing for the manifest alone
    makes these tests fail instead of skip wherever the material has not been
    fetched.
    """
    manifest = store.load_manifest(STORE, ATLAS_DOI)
    if manifest is None:
        return False
    return any(
        entry.get("path") and (STORE / entry["path"]).exists()
        for entry in manifest.get("files", [])
    )


needs_store = pytest.mark.skipif(
    not _material_on_disk(),
    reason=(
        "prenatal skin supplement files not on disk (git-ignored; the manifest "
        "is committed without them). Fetch them with `cli_supplements fetch` or "
        "see projects/test_projects/fetal_skin_atlas/supplements/incoming/README.md"
    ),
)


@needs_store
def test_real_manifest_is_valid_and_consistent() -> None:
    manifest = store.load_manifest(STORE, ATLAS_DOI)

    store.validate_manifest(manifest)
    assert store.cross_check_manifest(manifest) == []


@needs_store
def test_real_bundle_unpacked_including_the_big_table() -> None:
    manifest = store.load_manifest(STORE, ATLAS_DOI)
    bundle = next(
        entry for entry in manifest["files"] if entry["file_id"].endswith("MOESM4_ESM.zip")
    )

    members = {member["member_path"]: member for member in bundle["members"]}
    assert len(members) > 30

    # Supplementary Table 5 is ~95 MB — above any sensible general size cap, and
    # the largest table in the bundle. A blanket cap would drop exactly the file
    # a marker query most wants.
    big = next(name for name in members if name.endswith("Supplementary Table 5.xlsx"))
    assert members[big]["size_bytes"] > 80 * 1024 * 1024
    assert members[big]["extracted"] is True


@needs_store
def test_outline_stays_bounded_on_a_396k_row_table() -> None:
    manifest = store.load_manifest(STORE, ATLAS_DOI)
    bundle = next(
        entry for entry in manifest["files"] if entry["file_id"].endswith("MOESM4_ESM.zip")
    )
    big = next(
        member
        for member in bundle["members"]
        if member["member_path"].endswith("Supplementary Table 5.xlsx")
    )

    outline = store.outline_file(STORE / big["path"], sample_rows=4, max_cols=10)

    table = outline["tables"][0]
    assert table["n_rows"] > 100_000
    assert len(table["rows"]) == 4
    assert all(len(row) <= 10 for row in table["rows"])


@needs_store
def test_header_row_guess_skips_a_publisher_title_row() -> None:
    """Nature tables carry a title row above the header; slicing from row 0 is wrong."""
    manifest = store.load_manifest(STORE, ATLAS_DOI)
    bundle = next(
        entry for entry in manifest["files"] if entry["file_id"].endswith("MOESM4_ESM.zip")
    )
    table_one = next(
        member
        for member in bundle["members"]
        if member["member_path"].endswith("Supplementary Table 1.xlsx")
    )
    path = STORE / table_one["path"]

    outline = store.outline_file(path)
    guess = outline["tables"][0]["header_row_guess"]
    assert guess == 1
    assert outline["tables"][0]["rows"][0][0] == "Prenatal skin metadata"

    sliced = store.read_slice(path, start=guess + 1, limit=2, header_row=guess)
    assert sliced["header"][:3] == ["Sanger_id", "Donor", "PCW"]
    assert sliced["returned"] == 2


# ------------------------------------------------------------------
# Are the manifest's pointers actually actionable?
# ------------------------------------------------------------------


@needs_store
def test_every_table_pointer_resolves_to_its_recorded_columns() -> None:
    """The manifest's whole purpose: go straight to a sheet without searching.

    For each pointer, slice the file at the recorded header_row and check the
    recorded column names really are that table's columns. A pointer whose
    header_row is off by one sends a reader into the data.
    """
    manifest = store.load_manifest(STORE, ATLAS_DOI)
    files = {entry["file_id"]: entry for entry in manifest["files"]}

    checked = 0
    for pointer in manifest["tables"]:
        columns = pointer.get("columns")
        if not columns:
            continue  # the legends document carries no columns
        parent = files[pointer["file_id"]]
        if pointer.get("member_path"):
            member = next(
                m for m in parent["members"] if m["member_path"] == pointer["member_path"]
            )
            path = STORE / member["path"]
        else:
            path = STORE / parent["path"]

        sliced = store.read_slice(
            path,
            locator=pointer.get("locator"),
            start=pointer["header_row"] + 1,
            limit=1,
            header_row=pointer["header_row"],
        )
        header = [cell for cell in sliced["header"] if cell]
        recorded = [column["name"] for column in columns]
        assert header[: len(recorded)][:5] == recorded[:5], (
            f"{pointer.get('table_label') or pointer.get('locator')}: "
            f"recorded {recorded[:5]} but header row {pointer['header_row']} "
            f"reads {header[:5]}"
        )
        checked += 1

    assert checked > 40, f"only checked {checked} pointers"


@needs_store
def test_the_macrophage_marker_table_is_findable_and_readable() -> None:
    """The end-to-end case: the test cell type's markers live in a supplement.

    'Iron-recycling macrophage' is the project's reference cell type, and its
    differential expression is in one sheet of a 40-table bundle. A reader
    should reach it from the manifest alone.
    """
    manifest = store.load_manifest(STORE, ATLAS_DOI)

    pointer = next(
        p
        for p in manifest["tables"]
        if p["content_type"] == "deg_results" and "macrophage subsets" in p["description"]
    )
    assert pointer["table_label"] == "Supplementary Table 22"

    bundle = next(entry for entry in manifest["files"] if entry["file_id"] == pointer["file_id"])
    member = next(m for m in bundle["members"] if m["member_path"] == pointer["member_path"])

    sliced = store.read_slice(
        STORE / member["path"],
        locator=pointer["locator"],
        start=pointer["header_row"] + 1,
        limit=5,
        header_row=pointer["header_row"],
    )

    assert [c for c in sliced["header"] if c][:5] == [
        "names",
        "scores",
        "logfoldchanges",
        "pvals",
        "pvals_adj",
    ]
    # Real gene symbols, not a title row (HGNC symbols carry digits: DAB2, RNASE1).
    assert any(re.fullmatch(r"[A-Z][A-Z0-9.-]+", cell) for cell in sliced["rows"][0] if cell)


@needs_store
def test_gaps_explain_what_is_absent() -> None:
    """An empty tables list with no gaps would read as 'nothing useful here'."""
    manifest = store.load_manifest(STORE, ATLAS_DOI)

    reasons = {gap["file_id"]: gap["reason"] for gap in manifest["gaps"]}
    # The two PDFs and the video were never fetched; say so rather than implying
    # they hold nothing.
    assert "41586_2024_8002_MOESM5_ESM.mp4" in reasons
    assert any("never retrieved" in reason for reason in reasons.values())
