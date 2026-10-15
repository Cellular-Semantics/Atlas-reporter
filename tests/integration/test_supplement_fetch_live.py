"""Integration tests for supplement retrieval against the real services.

No mocks. These fail hard if Europe PMC or a publisher host changes shape, which
is the point: every route here is someone else's API, and the failure modes that
matter were all discovered by running against real papers rather than by reading
documentation.

Papers are chosen from the reproductive-atlas corpus so each exercises a
different branch of the waterfall, and each is small enough to fetch quickly.
"""

from __future__ import annotations

from collections import Counter

import httpx
import pytest

from atlas_chat.services import supplement_fetch as fetch
from atlas_chat.services import supplement_store as store

pytestmark = pytest.mark.integration

# 3 files, ~3.6 MB — the smallest complete Springer case in the corpus.
SPRINGER = "10.1038/s41588-024-01873-w"
SPRINGER_PMCID = "PMC11387200"

# In PMC, but its full text is not open: no article XML, and the bundle answers
# HTTP 200 with a 165-byte non-zip body.
NO_OPEN_FULLTEXT = "10.1016/j.devcel.2023.07.014"

# Not in PMC at all — only a person can get this one.
NOT_IN_PMC = "10.1126/science.adx0659"


@pytest.fixture
def client():
    with httpx.Client(follow_redirects=True, timeout=fetch.TIMEOUT) as c:
        yield c


# ------------------------------------------------------------------
# The routes, individually
# ------------------------------------------------------------------


def test_resolve_pmcid(client) -> None:
    pmcid, title = fetch.resolve_pmcid(client, SPRINGER)

    assert pmcid == SPRINGER_PMCID
    assert title


def test_resolve_pmcid_is_empty_for_a_paper_not_in_pmc(client) -> None:
    """An empty PMCID is the signal that only a manual route remains."""
    pmcid, _ = fetch.resolve_pmcid(client, NOT_IN_PMC)

    assert pmcid == ""


def test_article_xml_yields_filenames_and_captions(client, tmp_path) -> None:
    path = fetch.fetch_jats(client, SPRINGER_PMCID, tmp_path / "paper.jats.xml")

    assert path is not None
    listed = store.inventory_from_jats(path)
    assert len(listed) == 3
    assert all(entry["file_id"].startswith("41588_2024_1873_") for entry in listed)
    # Captions exist nowhere else, which is why this route runs first.
    assert any(entry.get("caption") for entry in listed)


def test_article_xml_absent_for_a_paper_without_open_fulltext(client, tmp_path) -> None:
    pmcid, _ = fetch.resolve_pmcid(client, NO_OPEN_FULLTEXT)
    assert pmcid, "this paper should still have a PMC record"

    assert fetch.fetch_jats(client, pmcid, tmp_path / "paper.jats.xml") is None


def test_bundle_members_are_named_as_the_article_xml_lists_them(client) -> None:
    """What makes selective extraction possible, and skipping figure images."""
    result = fetch.fetch_bundle(client, SPRINGER_PMCID)

    assert result.archive is not None, result.reason
    with result.archive as archive:
        names = {n.rsplit("/", 1)[-1] for n in archive.namelist()}
    assert "41588_2024_1873_MOESM3_ESM.xlsx" in names


def test_bundle_answers_200_with_a_non_zip_when_nothing_is_open(client) -> None:
    """The trap: a naive fetch records this as an empty archive and moves on."""
    pmcid, _ = fetch.resolve_pmcid(client, NO_OPEN_FULLTEXT)

    result = fetch.fetch_bundle(client, pmcid)

    assert result.archive is None
    assert "not a zip" in result.reason or "empty" in result.reason


def test_springer_static_host_serves_files_individually(client) -> None:
    url = fetch.springer_url(SPRINGER, "41588_2024_1873_MOESM3_ESM.xlsx")
    assert url is not None

    response = client.head(url)

    assert response.status_code == 200
    assert int(response.headers["content-length"]) > 10_000


# ------------------------------------------------------------------
# The waterfall end to end
# ------------------------------------------------------------------


def test_springer_paper_is_fully_retrieved(tmp_path, client) -> None:
    manifest = fetch.fetch_supplements(tmp_path, SPRINGER, client=client)

    store.validate_manifest(manifest)
    assert store.cross_check_manifest(manifest) == []
    assert len(manifest["files"]) == 3
    # One of the three is this paper's Reporting Summary, which triage rules out
    # on its caption before any bytes move. Nothing is missing.
    statuses = Counter(f["status"] for f in manifest["files"])
    assert statuses == {"present": 2, "skipped": 1}
    assert manifest["gaps"] == []
    for entry in manifest["files"]:
        if entry["status"] != "present":
            assert "path" not in entry, "skipped means no bytes were fetched"
            continue
        assert (tmp_path / entry["path"]).stat().st_size == entry["size_bytes"]
        assert len(entry["retrieval"]["sha256"]) == 64


def test_publisher_direct_produces_the_same_bytes_as_the_bundle(tmp_path, client) -> None:
    """Two routes to the same file must agree, or the fallback is a silent lie."""
    via_bundle = fetch.fetch_supplements(tmp_path / "bundle", SPRINGER, client=client)
    via_publisher = fetch.fetch_supplements(
        tmp_path / "direct", SPRINGER, bundle_cap=1000, client=client
    )

    fetched = [f for f in via_publisher["files"] if f["status"] == "present"]
    assert {f["retrieval"]["route"] for f in fetched} == {"publisher_direct"}

    left = {
        f["file_id"]: f["retrieval"]["sha256"]
        for f in via_bundle["files"]
        if f["status"] == "present"
    }
    right = {f["file_id"]: f["retrieval"]["sha256"] for f in fetched}
    assert left == right


def test_unreachable_paper_degrades_to_an_actionable_gap(tmp_path, client) -> None:
    manifest = fetch.fetch_supplements(tmp_path, NOT_IN_PMC, client=client)

    store.validate_manifest(manifest)
    assert manifest["files"] == []
    gap = manifest["gaps"][0]
    assert "no PMC record" in gap["reason"]
    assert NOT_IN_PMC in gap["action"]


def test_negative_cache_stops_a_second_attempt(tmp_path, client) -> None:
    """A permanently missing supplement must not be re-requested every run."""
    first = fetch.fetch_supplements(tmp_path, NO_OPEN_FULLTEXT, client=client)
    gaps_first = len(first["gaps"])

    second = fetch.fetch_supplements(tmp_path, NO_OPEN_FULLTEXT, client=client)

    assert len(second["gaps"]) == gaps_first, "re-running must not accumulate gaps"
    store.validate_manifest(second)


def test_retrieved_files_are_immediately_indexable(tmp_path, client) -> None:
    """The two halves must meet: what fetch writes, the store can outline."""
    manifest = fetch.fetch_supplements(tmp_path, SPRINGER, client=client)

    workbook = next(f for f in manifest["files"] if f["file_id"].endswith(".xlsx"))
    outline = store.outline_file(tmp_path / workbook["path"])

    assert outline["tables"]
    table = outline["tables"][0]
    assert table["n_rows"] > 0
    assert "header_row_guess" in table
