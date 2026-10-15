"""The asta → jats → needs_pdf waterfall, gated on the measured indexing band.

The bug this pins (#22): the old probe returned True whenever the paper had a
CorpusId, so every paper short-circuited at the ASTA rung and papers with no
retrievable text never got a local index. The contract now is that **only band
``full`` is served from ASTA**; every other band falls through.

The probe itself is faked at the seam (``_probe_asta``) — its own behaviour is
pinned by ``test_asta_indexing.py`` for the classification and by
``tests/integration/test_asta_indexing_live.py`` against the real API.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
from atlas_chat.services.asta_indexing import IndexingReport

from atlas_chat.services import subatlas_resolver

ATLAS_DOI = "10.1038/s41586-024-08002-x"


def _write_config(
    project_dir: Path, subatlas: list[dict[str, Any]], name: str = "cas.json"
) -> Path:
    path = project_dir / name
    path.write_text(
        json.dumps({"source": {"doi": ATLAS_DOI, "title": "An atlas", "subatlas_papers": subatlas}})
    )
    return path


@pytest.fixture
def stub_waterfall(monkeypatch: pytest.MonkeyPatch) -> dict[str, list[str]]:
    """Neutralise the two I/O rungs and record what each was asked to do."""
    calls: dict[str, list[str]] = {"jats": [], "built": []}

    monkeypatch.setattr(subatlas_resolver, "_write_todo", lambda project_dir, todos: None)

    def fake_build(project_dir, doi, **kwargs):
        calls["built"].append(doi)
        return {"doi": doi}

    monkeypatch.setattr("atlas_chat.services.local_snippet_index.build_paper_index", fake_build)
    return calls


def _stub_probe(monkeypatch: pytest.MonkeyPatch, bands: dict[str, str]) -> list[str]:
    """Fake the probe, returning a band per DOI. Records the probe order."""
    probed: list[str] = []

    def fake_probe(doi: str) -> IndexingReport:
        probed.append(doi)
        return IndexingReport(band=bands[doi], snippets=3, chars=4_000, reason="stub")

    monkeypatch.setattr(subatlas_resolver, "_probe_asta", fake_probe)
    return probed


def _stub_jats(monkeypatch: pytest.MonkeyPatch, succeed_for: set[str], calls: dict) -> None:
    """Fake the JATS rung: succeeds only for the listed DOIs."""

    def fake_jats(doi: str, dest_dir: Path) -> Path | None:
        calls["jats"].append(doi)
        if doi not in succeed_for:
            return None
        path = dest_dir / "paper.xml"
        path.write_text("<article/>")
        return path

    monkeypatch.setattr(subatlas_resolver, "_try_jats_fetch", fake_jats)


@pytest.mark.unit
def test_full_band_is_served_from_asta_without_a_local_build(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, stub_waterfall: dict
) -> None:
    _write_config(tmp_path, [{"label": "A", "doi": "10.1/full"}])
    _stub_probe(monkeypatch, {"10.1/full": "full"})
    _stub_jats(monkeypatch, set(), stub_waterfall)

    result = subatlas_resolver.ingest(tmp_path)

    assert result["subatlas"]["asta"] == ["10.1/full"]
    assert stub_waterfall["jats"] == [], "a full paper must not be fetched as JATS"
    # Only the atlas paper is built locally.
    assert stub_waterfall["built"] == [ATLAS_DOI]

    entry = json.loads((tmp_path / "cas.json").read_text())["source"]["subatlas_papers"][0]
    assert entry["status"] == "asta"
    assert entry["asta_indexing"]["band"] == "full"


@pytest.mark.unit
@pytest.mark.parametrize("band", ["partial", "abstract_only", "unindexed", "not_in_s2"])
def test_every_non_full_band_falls_through_to_jats(
    band: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, stub_waterfall: dict
) -> None:
    """This is the regression: these papers used to be marked ``asta``."""
    _write_config(tmp_path, [{"label": "A", "doi": "10.1/thin"}])
    _stub_probe(monkeypatch, {"10.1/thin": band})
    _stub_jats(monkeypatch, {"10.1/thin"}, stub_waterfall)

    result = subatlas_resolver.ingest(tmp_path)

    assert result["subatlas"]["asta"] == []
    assert result["subatlas"]["local"] == ["10.1/thin"]
    assert stub_waterfall["jats"] == ["10.1/thin"]

    entry = json.loads((tmp_path / "cas.json").read_text())["source"]["subatlas_papers"][0]
    assert entry["status"] == "local"
    assert entry["source_type"] == "jats"
    # The band is recorded even though the paper was not served from ASTA — a
    # report resting on this paper needs to know ASTA held nothing quotable.
    assert entry["asta_indexing"]["band"] == band


@pytest.mark.unit
def test_non_full_band_with_no_jats_needs_a_pdf(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, stub_waterfall: dict
) -> None:
    _write_config(tmp_path, [{"label": "A", "doi": "10.1/nowhere"}])
    _stub_probe(monkeypatch, {"10.1/nowhere": "unindexed"})
    _stub_jats(monkeypatch, set(), stub_waterfall)

    result = subatlas_resolver.ingest(tmp_path)

    assert result["subatlas"]["needs_pdf"] == ["10.1/nowhere"]
    entry = json.loads((tmp_path / "cas.json").read_text())["source"]["subatlas_papers"][0]
    assert entry["status"] == "needs_pdf"
    assert entry["asta_indexing"]["band"] == "unindexed"


@pytest.mark.unit
def test_summary_tallies_bands_across_the_corpus(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, stub_waterfall: dict
) -> None:
    _write_config(
        tmp_path,
        [
            {"label": "A", "doi": "10.1/a"},
            {"label": "B", "doi": "10.1/b"},
            {"label": "C", "doi": "10.1/c"},
            {"label": "D", "doi": ""},
        ],
    )
    _stub_probe(monkeypatch, {"10.1/a": "full", "10.1/b": "full", "10.1/c": "abstract_only"})
    _stub_jats(monkeypatch, {"10.1/c"}, stub_waterfall)

    result = subatlas_resolver.ingest(tmp_path)

    assert result["subatlas"]["bands"] == {"full": 2, "abstract_only": 1}
    assert result["subatlas"]["unresolved"] == ["D"]


@pytest.mark.unit
def test_entry_without_a_doi_is_never_probed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, stub_waterfall: dict
) -> None:
    _write_config(tmp_path, [{"label": "Unconfirmed", "doi": ""}])
    probed = _stub_probe(monkeypatch, {})
    _stub_jats(monkeypatch, set(), stub_waterfall)

    subatlas_resolver.ingest(tmp_path)

    assert probed == []


@pytest.mark.unit
def test_legacy_config_name_still_works(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, stub_waterfall: dict
) -> None:
    """Projects predating CAS+ keep working; ``cas.json`` simply wins when both exist."""
    _write_config(tmp_path, [{"label": "A", "doi": "10.1/full"}], name="cell_type_annotations.json")
    _stub_probe(monkeypatch, {"10.1/full": "full"})
    _stub_jats(monkeypatch, set(), stub_waterfall)

    subatlas_resolver.ingest(tmp_path)

    written = json.loads((tmp_path / "cell_type_annotations.json").read_text())
    assert written["source"]["subatlas_papers"][0]["status"] == "asta"


@pytest.mark.unit
def test_written_config_still_validates_against_the_cas_schema(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, stub_waterfall: dict
) -> None:
    """The new ``asta_indexing`` block must not break CAS+ validation."""
    import jsonschema

    from atlas_chat.schemas import load_schema

    _write_config(tmp_path, [{"label": "A", "doi": "10.1/thin"}])
    _stub_probe(monkeypatch, {"10.1/thin": "abstract_only"})
    _stub_jats(monkeypatch, {"10.1/thin"}, stub_waterfall)

    subatlas_resolver.ingest(tmp_path)

    schema = load_schema("cas_annotation.schema.json")
    validator = jsonschema.Draft202012Validator(
        {"$defs": schema["$defs"], "$ref": "#/$defs/SubatlasPaper"}
    )
    entry = json.loads((tmp_path / "cas.json").read_text())["source"]["subatlas_papers"][0]
    assert list(validator.iter_errors(entry)) == []


@pytest.mark.unit
def test_probe_failure_falls_through_rather_than_aborting(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, stub_waterfall: dict
) -> None:
    """A transport failure must not be mistaken for a servable paper."""
    _write_config(tmp_path, [{"label": "A", "doi": "10.1/x"}])
    _stub_jats(monkeypatch, {"10.1/x"}, stub_waterfall)

    def boom(paper_id: str, **kwargs):
        raise ValueError("ASTA_API_KEY not set in environment")

    monkeypatch.setattr("atlas_chat.services.asta_indexing.probe", boom)

    result = subatlas_resolver.ingest(tmp_path)

    assert result["subatlas"]["asta"] == []
    entry = json.loads((tmp_path / "cas.json").read_text())["source"]["subatlas_papers"][0]
    assert entry["asta_indexing"]["band"] == "unindexed"
    assert "probe failed" in entry["asta_indexing"]["reason"]
