"""Subatlas paper resolver — atlas-init phase.

Two passes, both keyed off ``cell_type_annotations.json``:

1. ``discover``: seed ``source.subatlas_papers`` from ``label_provenance.json``.
   Reads contributing-study labels (e.g. ``Sridhar_et_al_2020_CellPress``),
   queries Semantic Scholar for best-match candidates, and writes draft entries
   with ``status: candidate`` and a ``proposed_doi``. The user edits the file
   to confirm/correct each DOI before re-running.

2. ``ingest``: for each confirmed entry in ``source.subatlas_papers`` (with a
   non-empty ``doi``), runs the resolution waterfall:

   * ASTA probe — if S2 already indexes the paper with retrievable snippets,
     mark ``status: asta`` (no local index built; fan-out reaches it directly).
   * JATS fetch via ``fetch_preprint`` (EuropePMC → bioRxiv) — on success,
     build the per-paper local index and mark ``status: local`` (source_type
     ``jats``).
   * Else — mark ``status: needs_pdf`` and add an entry to
     ``subatlas_todo.md``. The user downloads the PDF and runs
     ``setup_local_index.py add --pdf ...``.

The atlas paper itself is also processed (role ``atlas``); it always builds a
local index since its full text is the report's primary evidence base.
"""

from __future__ import annotations

import json
import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

# Study labels that don't refer to a single published paper. These are
# atlas-internal partitions (e.g. unpublished aggregated data) and are skipped
# during discovery.
_NON_PAPER_LABELS = {
    "whole_embryo",
    "unpublished",
    "atlas_internal",
    "this_study",
}


@dataclass
class StudyLabel:
    """Parsed contributing-study label."""

    raw: str
    first_author: str | None
    year: int | None
    venue: str | None
    total_cells: int = 0


# ------------------------------------------------------------------
# Label parsing + provenance reading
# ------------------------------------------------------------------


_LABEL_RE = re.compile(
    r"^(?P<author>[A-Z][A-Za-z'-]+)_et_al_(?P<year>\d{4})_(?P<venue>[A-Za-z0-9._-]+)$"
)
# Looser fallback: just author + year somewhere.
_FALLBACK_AUTHOR_YEAR = re.compile(r"(?P<author>[A-Z][A-Za-z'-]+).*?(?P<year>\d{4})")


def parse_label(label: str) -> StudyLabel:
    m = _LABEL_RE.match(label)
    if m:
        return StudyLabel(
            raw=label,
            first_author=m.group("author"),
            year=int(m.group("year")),
            venue=m.group("venue").replace("_", " "),
        )
    m = _FALLBACK_AUTHOR_YEAR.search(label)
    if m:
        return StudyLabel(
            raw=label,
            first_author=m.group("author"),
            year=int(m.group("year")),
            venue=None,
        )
    return StudyLabel(raw=label, first_author=None, year=None, venue=None)


def read_provenance_labels(project_dir: Path) -> list[StudyLabel]:
    """Aggregate contributing-study labels across all cell types.

    Returns one ``StudyLabel`` per distinct raw label, with ``total_cells``
    summed across cell types. Skips known non-paper labels.
    """
    prov_path = project_dir / "label_provenance.json"
    if not prov_path.exists():
        return []
    data = json.loads(prov_path.read_text())
    totals: dict[str, int] = {}
    for entry in data.values():
        for study, n_cells, _share in entry.get("studies", []):
            if study in _NON_PAPER_LABELS:
                continue
            totals[study] = totals.get(study, 0) + int(n_cells)
    out: list[StudyLabel] = []
    for raw, total in sorted(totals.items(), key=lambda x: -x[1]):
        sl = parse_label(raw)
        sl.total_cells = total
        out.append(sl)
    return out


# ------------------------------------------------------------------
# Semantic Scholar discovery
# ------------------------------------------------------------------


def _s2_search_candidates(label: StudyLabel, max_results: int = 3) -> list[dict[str, Any]]:
    """Query Semantic Scholar /paper/search for plausible matches for a label.

    Filters by year (±1) when available. Returns up to ``max_results``
    candidates as dicts with ``doi``, ``title``, ``year``, ``corpus_id``.
    """
    import httpx

    if not label.first_author:
        return []
    query_parts = [label.first_author]
    if label.venue:
        query_parts.append(label.venue)
    query = " ".join(query_parts)
    params: dict[str, str | int] = {
        "query": query,
        "limit": max(max_results, 5),
        "fields": "externalIds,title,year,authors,venue",
    }
    if label.year:
        params["year"] = f"{label.year - 1}-{label.year + 1}"
    try:
        with httpx.Client(timeout=30) as client:
            resp = client.get(
                "https://api.semanticscholar.org/graph/v1/paper/search",
                params=params,
            )
            if resp.status_code != 200:
                logger.warning("S2 search returned %d for %s", resp.status_code, label.raw)
                return []
            data = resp.json().get("data", []) or []
    except Exception as exc:
        logger.warning("S2 search failed for %s: %s", label.raw, exc)
        return []

    out: list[dict[str, Any]] = []
    for p in data:
        if not p:
            continue
        ext = p.get("externalIds") or {}
        # Require first-author match to filter out coincidental hits.
        if label.first_author:
            au_text = " ".join((a.get("name") or "") for a in (p.get("authors") or [])).lower()
            if label.first_author.lower() not in au_text:
                continue
        out.append(
            {
                "doi": ext.get("DOI", ""),
                "title": p.get("title", ""),
                "year": p.get("year"),
                "corpus_id": str(ext.get("CorpusId", "")) if ext.get("CorpusId") else "",
                "venue": p.get("venue", ""),
            }
        )
        if len(out) >= max_results:
            break
    return out


def discover(project_dir: Path) -> dict[str, Any]:
    """Pass 1: propose ``subatlas_papers`` entries.

    Reads ``label_provenance.json``, queries S2 for each contributing study,
    and writes draft entries into ``cell_type_annotations.json``.

    Returns a summary dict. Does NOT build any indices.
    """
    cfg_path = project_dir / "cell_type_annotations.json"
    if not cfg_path.exists():
        raise FileNotFoundError(f"No cell_type_annotations.json at {project_dir}")
    cfg = json.loads(cfg_path.read_text())
    source = cfg.setdefault("source", {})

    labels = read_provenance_labels(project_dir)
    if not labels:
        logger.warning("No contributing-study labels in label_provenance.json")
        source.setdefault("subatlas_papers", [])
        cfg_path.write_text(json.dumps(cfg, indent=2))
        return {"n_labels": 0, "candidates": 0}

    existing = {e.get("label"): e for e in source.get("subatlas_papers", []) if e.get("label")}
    drafts: list[dict[str, Any]] = []
    n_with_proposal = 0
    for label in labels:
        if label.raw in existing and existing[label.raw].get("doi"):
            drafts.append(existing[label.raw])
            continue
        candidates = _s2_search_candidates(label)
        entry: dict[str, Any] = {
            "label": label.raw,
            "first_author": label.first_author,
            "year": label.year,
            "venue": label.venue,
            "total_cells": label.total_cells,
            "doi": "",
            "status": "candidate",
            "proposed": candidates,
        }
        if candidates:
            entry["proposed_doi"] = candidates[0]["doi"]
            n_with_proposal += 1
        drafts.append(entry)

    source["subatlas_papers"] = drafts
    cfg_path.write_text(json.dumps(cfg, indent=2))

    logger.info(
        "discover: %d labels, %d with S2 proposals (drafts written to cell_type_annotations.json)",
        len(labels),
        n_with_proposal,
    )
    return {
        "n_labels": len(labels),
        "candidates": n_with_proposal,
        "note": (
            "Review cell_type_annotations.json: copy proposed_doi → doi for each entry you "
            "accept (or replace with the correct DOI), then run `ingest`."
        ),
    }


# ------------------------------------------------------------------
# Ingest waterfall
# ------------------------------------------------------------------


def _probe_asta(doi: str, title: str | None) -> bool:
    """Return True iff S2 indexes this paper. Best-effort, non-fatal."""
    import httpx

    try:
        with httpx.Client(timeout=30) as client:
            resp = client.get(
                f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
                params={"fields": "externalIds,isOpenAccess,openAccessPdf"},
            )
            if resp.status_code != 200:
                return False
            data = resp.json() or {}
            return bool(data.get("externalIds", {}).get("CorpusId"))
    except Exception as exc:
        logger.debug("ASTA probe failed for %s: %s", doi, exc)
        return False


def _try_jats_fetch(doi: str, dest_dir: Path) -> Path | None:
    """Try ``fetch_preprint``; return the JATS path on success, ``None`` on failure."""
    from atlas_chat.services.fetch_preprint import PreprintFetchError, fetch_preprint

    try:
        result = fetch_preprint(doi, dest_dir)
        return result.jats_path
    except PreprintFetchError as exc:
        logger.info("JATS fetch failed for %s: %s", doi, exc)
        return None
    except Exception as exc:
        logger.warning("JATS fetch errored for %s: %s", doi, exc)
        return None


def _write_todo(project_dir: Path, todos: list[dict[str, Any]]) -> None:
    if not todos:
        # Remove a stale todo file if all are now resolved.
        path = project_dir / "subatlas_todo.md"
        if path.exists():
            path.unlink()
        return
    lines = [
        "# Subatlas papers needing PDF",
        "",
        "These contributing studies could not be fetched via ASTA or JATS. Download",
        "the PDF from the publisher and run:",
        "",
        "```bash",
        "uv run python scripts/setup_local_index.py add \\",
        f"  --project {project_dir.name} --doi <DOI> --pdf <path/to/paper.pdf> --role subatlas",
        "```",
        "",
    ]
    for t in todos:
        lines.append(f"## {t.get('label', t['doi'])}")
        lines.append("")
        lines.append(f"- DOI: `{t['doi']}`")
        if t.get("title"):
            lines.append(f"- Title: {t['title']}")
        if t.get("year"):
            lines.append(f"- Year: {t['year']}")
        if t.get("venue"):
            lines.append(f"- Venue: {t['venue']}")
        lines.append(f"- Cells contributed to atlas: {t.get('total_cells', 'unknown')}")
        lines.append(f"- DOI link: https://doi.org/{t['doi']}")
        lines.append("")
    (project_dir / "subatlas_todo.md").write_text("\n".join(lines))


def ingest(project_dir: Path, *, force: bool = False) -> dict[str, Any]:
    """Pass 2: run the asta/jats/pdf waterfall for confirmed subatlas entries.

    Also (re)builds the atlas paper's local index.
    """
    from atlas_chat.services.local_snippet_index import build_paper_index

    cfg_path = project_dir / "cell_type_annotations.json"
    if not cfg_path.exists():
        raise FileNotFoundError(f"No cell_type_annotations.json at {project_dir}")
    cfg = json.loads(cfg_path.read_text())
    source = cfg["source"]
    atlas_doi = source.get("doi")
    if not atlas_doi:
        raise ValueError("cell_type_annotations.json source.doi is required")

    summary: dict[str, Any] = {
        "atlas_doi": atlas_doi,
        "atlas_status": "skipped",
        "subatlas": {"asta": [], "local": [], "needs_pdf": [], "unresolved": []},
    }

    # Atlas paper — always try to build (it's the primary evidence base).
    try:
        build_paper_index(project_dir, atlas_doi, role="atlas", force=force)
        summary["atlas_status"] = "local"
    except Exception as exc:
        logger.error("Atlas paper build failed: %s", exc)
        summary["atlas_status"] = f"error: {exc}"

    refs = source.get("subatlas_papers", []) or []
    todos: list[dict[str, Any]] = []

    for entry in refs:
        doi = entry.get("doi") or ""
        if not doi:
            entry["status"] = "unresolved"
            summary["subatlas"]["unresolved"].append(entry.get("label") or "<no-label>")
            continue

        # 1. ASTA probe
        title = entry.get("title") or (entry.get("proposed") or [{}])[0].get("title", "")
        if _probe_asta(doi, title):
            entry["status"] = "asta"
            summary["subatlas"]["asta"].append(doi)
            continue

        # 2. JATS fetch + local build
        slug_dir = project_dir / "local_index" / "papers" / _slug(doi) / "source"
        slug_dir.mkdir(parents=True, exist_ok=True)
        jats_path = _try_jats_fetch(doi, slug_dir)
        if jats_path and jats_path.exists():
            try:
                build_paper_index(
                    project_dir, doi, jats_path=jats_path, role="subatlas", force=force
                )
                entry["status"] = "local"
                entry["source_type"] = "jats"
                summary["subatlas"]["local"].append(doi)
                continue
            except Exception as exc:
                logger.warning("Local build failed for %s: %s", doi, exc)

        # 3. needs_pdf
        entry["status"] = "needs_pdf"
        summary["subatlas"]["needs_pdf"].append(doi)
        todos.append(
            {
                "label": entry.get("label"),
                "doi": doi,
                "title": title,
                "year": entry.get("year"),
                "venue": entry.get("venue"),
                "total_cells": entry.get("total_cells"),
            }
        )

    cfg_path.write_text(json.dumps(cfg, indent=2))
    _write_todo(project_dir, todos)
    logger.info(
        "ingest: atlas=%s | subatlas asta=%d local=%d needs_pdf=%d unresolved=%d",
        summary["atlas_status"],
        len(summary["subatlas"]["asta"]),
        len(summary["subatlas"]["local"]),
        len(summary["subatlas"]["needs_pdf"]),
        len(summary["subatlas"]["unresolved"]),
    )
    return summary


def _slug(doi: str) -> str:
    # Re-export from local_snippet_index to avoid a circular import at module load.
    from atlas_chat.services.local_snippet_index import paper_slug

    return paper_slug(doi)


__all__ = [
    "StudyLabel",
    "discover",
    "ingest",
    "parse_label",
    "read_provenance_labels",
]
