"""Unit tests for the supplement retrieval waterfall.

Route ordering, the negative cache, URL derivation and the failure modes that
Europe PMC answers with HTTP 200. Network responses are served by an httpx mock
transport so the *decisions* can be tested in isolation; the routes themselves
are exercised for real in tests/integration/test_supplement_fetch_live.py.
"""

from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

import httpx
import pytest

from atlas_chat.services import supplement_fetch as fetch
from atlas_chat.services import supplement_store as store

pytestmark = pytest.mark.unit

DOI = "10.1038/s41588-024-01873-w"
PMCID = "PMC11387200"
STEM = "41588_2024_1873_"

JATS = f"""<?xml version="1.0"?>
<article xmlns:xlink="http://www.w3.org/1999/xlink"><body>
  <supplementary-material xlink:href="{STEM}MOESM1_ESM.pdf">
    <label>Supplementary Information</label>
    <caption><p>Supplementary Figures 1-9.</p></caption>
  </supplementary-material>
  <supplementary-material xlink:href="{STEM}MOESM3_ESM.xlsx">
    <label>Supplementary Tables</label>
    <caption><p>Supplementary Tables 1-12.</p></caption>
  </supplementary-material>
</body></article>
"""


def _zip(members: dict[str, bytes]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zf:
        for name, payload in members.items():
            zf.writestr(name, payload)
    return buffer.getvalue()


def _client(handler) -> httpx.Client:
    return httpx.Client(transport=httpx.MockTransport(handler), follow_redirects=True)


def _epmc_search_response() -> httpx.Response:
    return httpx.Response(
        200, json={"resultList": {"result": [{"pmcid": PMCID, "title": "A paper"}]}}
    )


# ------------------------------------------------------------------
# URL derivation
# ------------------------------------------------------------------


@pytest.mark.parametrize(
    ("doi", "expected"),
    [
        ("10.1038/s41586-024-08002-x", "41586_2024_8002_"),
        ("10.1038/s41588-021-00972-2", "41588_2021_972_"),
        ("10.1038/s41467-020-20358-y", "41467_2020_20358_"),
        ("10.1038/s42003-022-04384-8", "42003_2022_4384_"),
    ],
)
def test_springer_stem_derives_from_doi(doi: str, expected: str) -> None:
    """The DOI's 3-digit year and zero-padded article number render differently."""
    assert fetch.springer_esm_stem(doi) == expected


def test_springer_stem_declines_other_publishers() -> None:
    assert fetch.springer_esm_stem("10.1016/j.devcel.2024.01.006") is None


def test_springer_url_encodes_the_doi() -> None:
    url = fetch.springer_url("10.1038/s41586-024-08002-x", "x_MOESM6_ESM.xlsx")

    assert url is not None
    assert "art%3A10.1038%2Fs41586-024-08002-x" in url
    assert url.endswith("/MediaObjects/x_MOESM6_ESM.xlsx")


def test_no_template_for_unknown_publisher() -> None:
    """Absence of a template is a routing fact, not an error."""
    assert fetch.publisher_direct_url("10.1073/pnas.2404775121", "pnas.sd01.xlsx") is None


# ------------------------------------------------------------------
# The bundle's failure modes, all of which are HTTP 200
# ------------------------------------------------------------------


def test_bundle_empty_body_is_not_success() -> None:
    """Europe PMC answers 200 with a short non-zip body when nothing is open.

    Recorded as success this is an empty archive and a paper that looks as though
    it has no supplements.
    """
    handler = lambda request: httpx.Response(200, content=b"No supplementary files found")  # noqa: E731

    with _client(handler) as client:
        result = fetch.fetch_bundle(client, PMCID)

    assert result.archive is None
    assert "not a zip" in result.reason


def test_bundle_zero_bytes_is_not_success() -> None:
    handler = lambda request: httpx.Response(200, content=b"")  # noqa: E731

    with _client(handler) as client:
        result = fetch.fetch_bundle(client, PMCID)

    assert result.archive is None
    assert "empty" in result.reason


def test_bundle_abandoned_above_cap() -> None:
    handler = lambda request: httpx.Response(200, content=b"x" * 5000)  # noqa: E731

    with _client(handler) as client:
        result = fetch.fetch_bundle(client, PMCID, cap=1000)

    assert result.archive is None
    assert "exceeds the 1000-byte cap" in result.reason
    assert result.size > 1000


def test_bundle_http_error_is_reported() -> None:
    handler = lambda request: httpx.Response(503)  # noqa: E731

    with _client(handler) as client:
        result = fetch.fetch_bundle(client, PMCID)

    assert result.archive is None
    assert "HTTP 503" in result.reason


def test_bundle_returns_an_archive() -> None:
    payload = _zip({f"{STEM}MOESM1_ESM.pdf": b"%PDF-1.4"})
    handler = lambda request: httpx.Response(200, content=payload)  # noqa: E731

    with _client(handler) as client:
        result = fetch.fetch_bundle(client, PMCID)
        assert result.archive is not None
        assert result.archive.namelist() == [f"{STEM}MOESM1_ESM.pdf"]


# ------------------------------------------------------------------
# The negative cache
# ------------------------------------------------------------------


@pytest.mark.parametrize(
    ("entry", "retry", "expected", "note"),
    [
        ({"status": "present"}, False, False, "already on disk"),
        ({"status": "present"}, True, False, "retry never re-fetches what we have"),
        ({"status": "listed"}, False, True, "never tried"),
        (
            {
                "status": "unavailable",
                "retrieval": {"route": "none", "attempted_at": "2026-08-25T00:00:00+00:00"},
            },
            False,
            False,
            "tried and failed — do not ask again every run",
        ),
        (
            {
                "status": "unavailable",
                "retrieval": {"route": "none", "attempted_at": "2026-08-25T00:00:00+00:00"},
            },
            True,
            True,
            "retry overrides the cache",
        ),
        (
            {"status": "failed", "retrieval": {"route": "publisher_direct"}},
            False,
            True,
            "failed without a stamp is not cached",
        ),
    ],
)
def test_should_attempt(entry: dict, retry: bool, expected: bool, note: str) -> None:
    assert fetch.should_attempt(entry, retry) is expected, note


# ------------------------------------------------------------------
# The waterfall
# ------------------------------------------------------------------


def _waterfall_handler(
    *,
    jats: str | None = JATS,
    bundle: bytes | None = None,
    publisher_ok: bool = False,
    calls: list[str] | None = None,
):
    def handler(request: httpx.Request) -> httpx.Response:
        url = str(request.url)
        if calls is not None:
            calls.append(url)
        if "/search" in url:
            return _epmc_search_response()
        if url.endswith("/fullTextXML"):
            return httpx.Response(200, text=jats) if jats else httpx.Response(404)
        if url.endswith("/supplementaryFiles"):
            return (
                httpx.Response(200, content=bundle) if bundle else httpx.Response(200, content=b"")
            )
        if "static-content.springer.com" in url:
            return httpx.Response(200, content=b"payload") if publisher_ok else httpx.Response(404)
        return httpx.Response(404)

    return handler


def test_bundle_route_stores_only_listed_files(tmp_path: Path) -> None:
    """Figure images bloat the bundle; only the listed supplements are wanted."""
    bundle = _zip(
        {
            f"{STEM}MOESM1_ESM.pdf": b"%PDF-1.4",
            f"{STEM}MOESM3_ESM.xlsx": b"xlsx-bytes",
            "41588_2024_1873_g001.jpg": b"\xff\xd8\xff",  # a figure, not a supplement
        }
    )
    with _client(_waterfall_handler(bundle=bundle)) as client:
        manifest = fetch.fetch_supplements(tmp_path, DOI, client=client)

    by_id = {f["file_id"]: f for f in manifest["files"]}
    assert by_id[f"{STEM}MOESM1_ESM.pdf"]["status"] == "present"
    assert by_id[f"{STEM}MOESM1_ESM.pdf"]["retrieval"]["route"] == "europepmc_bundle"
    assert by_id[f"{STEM}MOESM3_ESM.xlsx"]["status"] == "present"
    assert "41588_2024_1873_g001.jpg" not in by_id
    # The caption from the article XML survives into the manifest.
    assert by_id[f"{STEM}MOESM3_ESM.xlsx"]["caption"] == "Supplementary Tables 1-12."
    assert manifest["paper"]["pmcid"] == PMCID


def test_publisher_direct_takes_over_when_the_bundle_is_capped(tmp_path: Path) -> None:
    calls: list[str] = []
    with _client(_waterfall_handler(bundle=b"x" * 5000, publisher_ok=True, calls=calls)) as client:
        manifest = fetch.fetch_supplements(tmp_path, DOI, bundle_cap=1000, client=client)

    routes = {f["file_id"]: f["retrieval"]["route"] for f in manifest["files"]}
    assert set(routes.values()) == {"publisher_direct"}
    assert all(f["status"] == "present" for f in manifest["files"])
    # The bundle was tried before the per-file route, not instead of it.
    assert any(u.endswith("/supplementaryFiles") for u in calls)
    assert any("static-content.springer.com" in u for u in calls)


def test_a_capped_bundle_is_not_a_gap_once_the_files_arrive(tmp_path: Path) -> None:
    """How we got the bytes is a detail; a gap means something is missing."""
    with _client(_waterfall_handler(bundle=b"x" * 5000, publisher_ok=True)) as client:
        manifest = fetch.fetch_supplements(tmp_path, DOI, bundle_cap=1000, client=client)

    assert manifest["gaps"] == []


def test_everything_failing_leaves_actionable_gaps(tmp_path: Path) -> None:
    with _client(_waterfall_handler(bundle=None, publisher_ok=False)) as client:
        manifest = fetch.fetch_supplements(tmp_path, DOI, client=client)

    assert all(f["status"] in {"failed", "unavailable"} for f in manifest["files"])
    assert all(f["retrieval"]["attempted_at"] for f in manifest["files"])
    assert manifest["gaps"]
    assert all("incoming/" in gap["action"] for gap in manifest["gaps"] if "action" in gap)


def test_no_pmc_record_records_the_manual_route(tmp_path: Path) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if "/search" in str(request.url):
            return httpx.Response(200, json={"resultList": {"result": []}})
        return httpx.Response(404)

    with _client(handler) as client:
        manifest = fetch.fetch_supplements(tmp_path, "10.1126/science.adx0659", client=client)

    assert manifest["files"] == []
    gap = manifest["gaps"][0]
    assert "no PMC record" in gap["reason"]
    assert "doi.org/10.1126/science.adx0659" in gap["action"]


def test_bundle_is_tried_even_with_no_article_xml(tmp_path: Path) -> None:
    """A paper with no open full text can still have open supplements.

    Without this the bundle is never attempted for such papers and their files
    are reported unavailable without anyone having looked.
    """
    bundle = _zip({"mmc1.xlsx": b"xlsx", "gr1.jpg": b"\xff\xd8\xff"})
    with _client(_waterfall_handler(jats=None, bundle=bundle)) as client:
        manifest = fetch.fetch_supplements(tmp_path, "10.1016/j.devcel.2024.01.006", client=client)

    by_id = {f["file_id"]: f for f in manifest["files"]}
    assert by_id["mmc1.xlsx"]["status"] == "present"
    assert "gr1.jpg" not in by_id
    # No captions are possible without the article XML — say so.
    assert any("no article XML" in gap["reason"] for gap in manifest["gaps"])


def test_second_run_does_not_refetch(tmp_path: Path) -> None:
    bundle = _zip({f"{STEM}MOESM1_ESM.pdf": b"%PDF", f"{STEM}MOESM3_ESM.xlsx": b"x"})
    calls: list[str] = []
    with _client(_waterfall_handler(bundle=bundle, calls=calls)) as client:
        fetch.fetch_supplements(tmp_path, DOI, client=client)
        first = len([u for u in calls if u.endswith("/supplementaryFiles")])
        fetch.fetch_supplements(tmp_path, DOI, client=client)
        second = len([u for u in calls if u.endswith("/supplementaryFiles")])

    assert first == 1
    assert second == 1, "files already present must not trigger another bundle download"


def test_manifest_stays_schema_valid_through_the_waterfall(tmp_path: Path) -> None:
    with _client(_waterfall_handler(bundle=None)) as client:
        manifest = fetch.fetch_supplements(tmp_path, DOI, client=client)

    store.validate_manifest(manifest)
    assert store.cross_check_manifest(manifest) == []


def test_video_is_never_fetched(tmp_path: Path) -> None:
    """Supplementary video is what makes bundles enormous and holds no tables."""
    jats = JATS.replace(f"{STEM}MOESM3_ESM.xlsx", f"{STEM}MOESM5_ESM.mp4")
    bundle = _zip({f"{STEM}MOESM1_ESM.pdf": b"%PDF", f"{STEM}MOESM5_ESM.mp4": b"video"})
    with _client(_waterfall_handler(jats=jats, bundle=bundle)) as client:
        manifest = fetch.fetch_supplements(tmp_path, DOI, client=client)

    video = next(f for f in manifest["files"] if f["file_id"].endswith(".mp4"))
    assert video["status"] == "listed", "listed so it is known, not fetched"


# ------------------------------------------------------------------
# Corpus level
# ------------------------------------------------------------------


def test_fetch_corpus_continues_past_a_failing_paper(tmp_path: Path, monkeypatch) -> None:
    cas = {
        "source": {
            "doi": "10.1038/atlas-1",
            "subatlas_papers": [{"label": "s", "doi": "10.1038/sub-1"}],
        }
    }
    seen: list[str] = []

    def fake(store_root, doi, **kwargs):
        seen.append(doi)
        if doi == "10.1038/atlas-1":
            raise httpx.ConnectError("network gone")
        return {"files": [{"status": "present"}], "gaps": []}

    monkeypatch.setattr(fetch, "fetch_supplements", fake)
    rows = fetch.fetch_corpus(tmp_path, cas)

    assert seen == ["10.1038/atlas-1", "10.1038/sub-1"]
    assert "error" in rows[0]
    assert rows[1]["present"] == 1


def test_cli_fetch_rejects_both_doi_and_cas(tmp_path: Path, capsys) -> None:
    cas = tmp_path / "cas.json"
    cas.write_text(json.dumps({"source": {"doi": "10.1038/x"}}))

    code = store.main(["fetch", "--store", str(tmp_path), "--doi", "10.1038/x", "--cas", str(cas)])

    assert code == 2
    assert "exactly one" in capsys.readouterr().err
