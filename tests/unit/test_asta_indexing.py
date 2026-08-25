"""Band classifier regression — the calibration table is the contract.

The numbers pinned here are the measured band boundaries from the 21-paper
calibration recorded in :mod:`atlas_chat.services.asta_indexing`. If a threshold
moves, these tests are the place that says so out loud.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from atlas_chat.services.asta_indexing import IndexingReport, classify_rows

from atlas_chat.services import asta_indexing

FIXTURES = Path(__file__).parent / "fixtures" / "evidence"


def _rows(
    n: int, chars: int, sections: int, ref_mentions: int, *, corpus_id: str = "273400864"
) -> list[dict]:
    """Build ``n`` snippet rows carrying the given aggregate signals.

    Characters and refMentions are spread over the rows; ``sections`` distinct
    non-null section names are cycled through them, so a request for 0 sections
    yields the ``section: null`` chunks ASTA emits for title/abstract text.
    """
    if n == 0:
        return []
    per_row_chars, extra = divmod(chars, n)
    rows = []
    for i in range(n):
        text_len = per_row_chars + (1 if i < extra else 0)
        section = f"Section {i % sections}" if sections else None
        n_refs = ref_mentions // n + (1 if i < ref_mentions % n else 0)
        rows.append(
            {
                "score": 0.5,
                "paper": {"corpusId": corpus_id, "title": "A paper"},
                "snippet": {
                    "text": "x" * text_len,
                    "section": section,
                    "snippetKind": "body" if sections else "abstract",
                    "annotations": {
                        "refMentions": [{"start": 0, "end": 1, "matchedPaperCorpusId": "1"}]
                        * n_refs
                    },
                },
            }
        )
    return rows


# The calibration table: (label, snippets, chars, sections, refMentions) -> band.
# UNINDEXED and ABSTRACT_ONLY / FULL rows are the observed min and max of each
# measured band; the `partial` cases sit in the gap the bands left open.
CALIBRATION = [
    ("unindexed floor", 0, 0, 0, 0, "unindexed"),
    ("abstract_only min observed", 2, 1_219, 0, 0, "abstract_only"),
    ("abstract_only max observed", 4, 6_312, 0, 0, "abstract_only"),
    ("full min observed", 15, 18_802, 9, 50, "full"),
    ("full max observed", 72, 105_876, 30, 361, "full"),
]


@pytest.mark.unit
@pytest.mark.parametrize(
    ("label", "n", "chars", "sections", "refs", "expected"),
    CALIBRATION,
    ids=[row[0] for row in CALIBRATION],
)
def test_calibration_table_bands(
    label: str, n: int, chars: int, sections: int, refs: int, expected: str
) -> None:
    report = classify_rows(_rows(n, chars, sections, refs))
    assert report.band == expected, f"{label}: {report.reason}"
    assert report.snippets == n
    assert report.chars == chars
    assert report.sections == sections
    assert report.ref_mentions == refs


@pytest.mark.unit
def test_empty_response_is_unindexed() -> None:
    report = classify_rows([])
    assert report.band == "unindexed"
    assert not report.servable
    assert report.dead
    assert "0 snippets" in report.reason


@pytest.mark.unit
def test_abstract_only_needs_neither_sections_nor_refs() -> None:
    """Both signals must be absent — either one alone means body text."""
    assert classify_rows(_rows(3, 5_000, 0, 0)).band == "abstract_only"
    # A section name with no refMentions is thin, but it is body text.
    assert classify_rows(_rows(3, 5_000, 1, 0)).band == "partial"
    # refMentions with no section name likewise.
    assert classify_rows(_rows(3, 5_000, 0, 4)).band == "partial"


@pytest.mark.unit
@pytest.mark.parametrize(
    ("n", "chars", "sections", "refs"),
    [
        (asta_indexing.PARTIAL_SNIPPETS - 1, 40_000, 12, 80),  # too few snippets
        (30, asta_indexing.PARTIAL_CHARS - 1, 12, 80),  # too little text
        (30, 40_000, 12, 0),  # a body with no bibliography
    ],
    ids=["few snippets", "few chars", "no refMentions"],
)
def test_partial_guards_below_the_full_floor(n: int, chars: int, sections: int, refs: int) -> None:
    report = classify_rows(_rows(n, chars, sections, refs))
    assert report.band == "partial"
    assert not report.servable, "partial must not be served from ASTA"
    assert not report.dead, "partial still has references worth following"


@pytest.mark.unit
def test_only_full_is_servable() -> None:
    for band in asta_indexing.BANDS:
        assert (band == "full") == IndexingReport(band=band).servable


@pytest.mark.unit
def test_dead_bands_are_exactly_the_textless_ones() -> None:
    assert set(asta_indexing.DEAD_BANDS) == {"unindexed", "not_in_s2"}
    assert all(IndexingReport(band=b).dead for b in asta_indexing.DEAD_BANDS)
    assert not IndexingReport(band="abstract_only").dead


@pytest.mark.unit
def test_null_sections_are_not_counted() -> None:
    """``section: null`` is the abstract-chunk signal, not a section name."""
    rows = _rows(4, 4_000, 0, 0)
    assert all(row["snippet"]["section"] is None for row in rows)
    assert classify_rows(rows).sections == 0


@pytest.mark.unit
def test_missing_annotations_key_is_tolerated() -> None:
    """The ``annotations`` key may be absent or explicitly null."""
    rows = [
        {"paper": {"corpusId": "1"}, "snippet": {"text": "abc", "section": "Results"}},
        {"paper": {"corpusId": "1"}, "snippet": {"text": "de", "annotations": None}},
    ]
    report = classify_rows(rows)
    assert report.ref_mentions == 0
    assert report.chars == 5
    assert report.sections == 1


@pytest.mark.unit
def test_corpus_id_is_normalized_and_captured() -> None:
    report = classify_rows(_rows(2, 100, 0, 0, corpus_id="260956290"))
    assert report.corpus_id == "CorpusId:260956290"


@pytest.mark.unit
def test_classifies_the_real_asta_payload() -> None:
    """Runs against the recorded ASTA response the annotator tests also use."""
    raw = json.loads((FIXTURES / "asta_snippet_search.raw.json").read_text())

    from atlas_chat.services import snippet_annotator

    rows = snippet_annotator._coerce_data_list(raw)
    assert rows, "fixture should carry snippet rows"
    report = classify_rows(rows)
    assert report.band in asta_indexing.BANDS
    assert report.snippets == len(rows)
    assert report.chars > 0
    assert report.corpus_id and report.corpus_id.startswith("CorpusId:")


@pytest.mark.unit
def test_report_round_trips_through_the_cas_block() -> None:
    original = classify_rows(_rows(4, 6_312, 0, 0, corpus_id="260956290"))
    restored = IndexingReport.from_dict(original.to_dict())
    assert restored.band == original.band
    assert restored.snippets == original.snippets
    assert restored.chars == original.chars
    assert restored.corpus_id == original.corpus_id
    assert restored.probed_at == original.probed_at


@pytest.mark.unit
def test_cas_block_validates_against_the_schema() -> None:
    import jsonschema

    from atlas_chat.schemas import load_schema

    schema = load_schema("cas_annotation.schema.json")
    validator = jsonschema.Draft202012Validator(
        {"$defs": schema["$defs"], "$ref": "#/$defs/AstaIndexing"}
    )
    for band in asta_indexing.BANDS:
        block = IndexingReport(band=band, corpus_id="CorpusId:1").to_dict()
        assert not list(validator.iter_errors(block)), f"{band} block rejected"


@pytest.mark.unit
def test_missing_paper_errors_are_distinguished_from_faults() -> None:
    assert asta_indexing._is_missing_paper_error(ValueError("no such paper"))
    assert asta_indexing._is_missing_paper_error(ValueError("Paper not found"))
    assert not asta_indexing._is_missing_paper_error(ValueError("500 server error"))
    assert not asta_indexing._is_missing_paper_error(ValueError("timed out"))
    assert not asta_indexing._is_missing_paper_error(ValueError("connection reset"))


@pytest.mark.unit
def test_http_failures_are_judged_by_status_code_not_message() -> None:
    """A fault mentioning a paper id containing "404" must still propagate."""
    import httpx

    def error(status: int, text: str) -> httpx.HTTPStatusError:
        request = httpx.Request("POST", "https://asta-tools.allen.ai/mcp/v1")
        return httpx.HTTPStatusError(
            text, request=request, response=httpx.Response(status, request=request)
        )

    assert asta_indexing._is_missing_paper_error(error(404, "Not Found"))
    assert not asta_indexing._is_missing_paper_error(
        error(500, "internal error processing CorpusId:1404567")
    )
    assert not asta_indexing._is_missing_paper_error(error(429, "rate limited"))


@pytest.mark.unit
def test_asta_missing_paper_message_verbatim() -> None:
    """The exact wording ASTA returns, captured from the live endpoint.

    Recorded here so a change in the upstream message surfaces as a unit failure
    rather than as papers silently misbanded as ``unindexed``.
    """
    message = (
        "Asta tool snippet_search failed: Error executing tool snippet_search: "
        "No papers matching the provided paper ids "
        "(['DOI:10.1126/science.adx0659']) were found. Please double check the "
        "paper ids provided."
    )
    assert asta_indexing._is_missing_paper_error(ValueError(message))


# --------------------------------------------------------------------------
# cache
# --------------------------------------------------------------------------


@pytest.mark.unit
def test_config_path_prefers_cas_over_the_legacy_name(tmp_path: Path) -> None:
    legacy = tmp_path / "cell_type_annotations.json"
    legacy.write_text("{}")
    assert asta_indexing.config_path(tmp_path) == legacy

    cas = tmp_path / "cas.json"
    cas.write_text("{}")
    assert asta_indexing.config_path(tmp_path) == cas


@pytest.mark.unit
def test_cached_bands_keyed_by_both_corpus_id_and_doi(tmp_path: Path) -> None:
    (tmp_path / "cas.json").write_text(
        json.dumps(
            {
                "source": {
                    "doi": "10.1/atlas",
                    "subatlas_papers": [
                        {
                            "label": "Goh_et_al_2023",
                            "doi": "10.1/goh",
                            "status": "needs_pdf",
                            "asta_indexing": {
                                "band": "abstract_only",
                                "snippets": 4,
                                "chars": 6312,
                                "sections": 0,
                                "ref_mentions": 0,
                                "corpus_id": "CorpusId:260956290",
                            },
                        },
                        {"label": "No_probe_yet", "doi": "10.1/none"},
                    ],
                }
            }
        )
    )
    bands = asta_indexing.cached_bands(tmp_path)
    assert bands["CorpusId:260956290"].band == "abstract_only"
    assert bands["DOI:10.1/goh"].band == "abstract_only"
    assert "DOI:10.1/none" not in bands


@pytest.mark.unit
def test_cached_bands_survives_a_malformed_block(tmp_path: Path) -> None:
    (tmp_path / "cas.json").write_text(
        json.dumps(
            {
                "source": {
                    "subatlas_papers": [
                        {"doi": "10.1/a", "asta_indexing": {"no_band": True}},
                        {"doi": "10.1/b", "asta_indexing": "not an object"},
                        {
                            "doi": "10.1/c",
                            "asta_indexing": {"band": "full", "snippets": 30},
                        },
                    ]
                }
            }
        )
    )
    bands = asta_indexing.cached_bands(tmp_path)
    assert set(bands) == {"DOI:10.1/c"}


@pytest.mark.unit
def test_cached_bands_on_a_missing_or_broken_config(tmp_path: Path) -> None:
    assert asta_indexing.cached_bands(tmp_path) == {}
    (tmp_path / "cas.json").write_text("{not json")
    assert asta_indexing.cached_bands(tmp_path) == {}


@pytest.mark.unit
def test_probe_cached_reads_the_config_without_calling_asta(tmp_path: Path) -> None:
    """A persisted band must satisfy the probe — no ASTA_API_KEY, no network."""
    import asyncio

    asta_indexing.clear_cache()
    (tmp_path / "cas.json").write_text(
        json.dumps(
            {
                "source": {
                    "subatlas_papers": [
                        {
                            "doi": "10.1/x",
                            "asta_indexing": {
                                "band": "unindexed",
                                "corpus_id": "CorpusId:261701324",
                            },
                        }
                    ]
                }
            }
        )
    )
    report = asyncio.run(asta_indexing.probe_cached("CorpusId:261701324", project_dir=tmp_path))
    assert report.band == "unindexed"

    # Second call is served from the in-process memo, project_dir or not.
    assert asyncio.run(asta_indexing.probe_cached("CorpusId:261701324")).band == "unindexed"
    asta_indexing.clear_cache()


@pytest.mark.unit
def test_unrelated_tool_errors_are_not_read_as_missing_papers() -> None:
    """A fault must propagate, not be recorded as a band."""
    for message in (
        "Asta tool snippet_search failed: rate limit exceeded",
        "Asta MCP error calling snippet_search: internal error",
        "no snippets were found for the query",
    ):
        assert not asta_indexing._is_missing_paper_error(ValueError(message)), message
