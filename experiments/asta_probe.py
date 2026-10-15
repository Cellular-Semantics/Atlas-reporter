#!/usr/bin/env python3
"""Direct CLI wrapper over the ASTA MCP endpoint, for retrieval tuning.

Why this exists
---------------
Retrieval tuning needs to see raw scores, chunk counts and citation payloads
without going through the report pipeline. This talks straight to the ASTA MCP
endpoint so you can vary one thing at a time.

Facts about the endpoint that this script encodes (verified 2026-08-21):

- It is **MCP over JSON-RPC 2.0**, not REST: ``POST /mcp/v1`` with a
  ``tools/call`` method. Auth is the ``x-api-key`` header.
- Responses come back as **SSE** (``event: message\\ndata: {...}``), and the
  useful payload is **double-encoded**: ``result.content[0].text`` is a JSON
  *string* that must be parsed again.
- With ``paper_ids`` set, ``limit`` saturates at the paper's indexed chunk
  count (e.g. 72 for the prenatal skin atlas). Asking for more is free and
  tells you the paper's true ceiling.
- Scores are **query-relative, not absolute**. Compare distributions within a
  single query; never across queries. See ``--mentions`` for a filter that
  does transfer.

Two retrieval backends, one display layer
-----------------------------------------
``snippets --backend local`` runs the same query against a locally built
snippet index instead of ASTA, so the two can be compared under identical
filters and stats. The local side is *not* a reimplementation — it calls the
production code the report pipeline uses (``fetch_preprint`` →
``build_paper_index`` → ``local_snippet_index.search``), including the PMC
JATS fetch. See the "local backend" section below for what is and is not
comparable.

Subcommands::

    snippets   snippet_search — the main event (scores, sections, refMentions)
    paper      get_paper / get_paper_batch metadata
    citations  get_citations (papers citing the target)
    tools      tools/list — the endpoint's own schema, i.e. the "Swagger"

Examples::

    # whole paper, see the score distribution and the ceiling
    ./asta_probe.py snippets -q "dermal papilla markers location function" \
        -p CorpusId:273400864 --limit 100

    # flag which chunks actually name the cell type (the filter that transfers)
    ./asta_probe.py snippets -q "TML macrophage TREM2 microglia-like" \
        -p CorpusId:273400864 --limit 100 \
        --mentions 'TML|TMLM|TREM2|microglia' --stats

    # corpus-wide free search, keep the top slice only
    ./asta_probe.py snippets -q "TREM2 microglia-like macrophage fetal skin" \
        --limit 20 --min-score 0.4

    # what can I follow from here?
    ./asta_probe.py snippets -q "..." -p CorpusId:273400864 --limit 100 --refs

    # save slim records for offline analysis
    ./asta_probe.py snippets -q "..." -p CorpusId:273400864 --limit 100 \
        --out /tmp/probe.json

    # the same query against locally chunked+embedded JATS (fetched from PMC
    # on first use, then cached). Paper-scoped by DOI; identical filters/stats.
    ./asta_probe.py snippets --backend local -p DOI:10.1038/s41586-024-08002-x \
        -q "dermal papilla markers location function" --limit 100 \
            --mentions 'dermal papilla|DP' --stats

    # search a project's curated corpus instead of the throwaway probe cache
    ./asta_probe.py snippets --backend local --project fetal_skin_atlas \
        -p DOI:10.1038/s41586-024-08002-x -q "..." --limit 50

Docs: https://asta-tools.allen.ai/mcp/v1/docs (human-readable tool reference;
there is no OpenAPI/Swagger spec — ``tools`` is the machine-readable equivalent).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any
from uuid import uuid4

ASTA_MCP_URL = "https://asta-tools.allen.ai/mcp/v1"

PAPER_FIELDS = (
    "abstract,authors,citations,fieldsOfStudy,isOpenAccess,journal,"
    "publicationDate,references,tldr,url,venue,year"
)


# --------------------------------------------------------------------------
# transport
# --------------------------------------------------------------------------
def _api_key() -> str:
    """Resolve the API key: environment, then .env (project convention)."""
    key = os.getenv("ASTA_API_KEY", "")
    if key:
        return key
    try:
        from dotenv import load_dotenv  # noqa: PLC0415
    except ImportError:
        pass
    else:
        load_dotenv()
        key = os.getenv("ASTA_API_KEY", "")
    if key:
        return key
    sys.exit(
        "ASTA_API_KEY not set. Export it, put it in .env, or note that this repo "
        "keeps it in .claude/settings.local.json (which only Claude Code loads)."
    )


def _extract_rpc_payload(text: str) -> dict[str, Any]:
    """Pull the JSON-RPC object out of a plain-JSON or SSE response body."""
    text = text.strip()
    if not text:
        raise ValueError("empty response from ASTA MCP endpoint")
    if text.startswith("{"):
        return json.loads(text)
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("data:"):
            body = line[len("data:"):].strip()
            if body.startswith("{"):
                payload = json.loads(body)
                # an SSE stream may carry several frames; the one with a
                # result/error is the one we want.
                if "result" in payload or "error" in payload:
                    return payload
    raise ValueError(f"could not parse ASTA response: {text[:200]!r}")


def call_tool(tool: str, arguments: dict[str, Any], *, timeout: int = 120) -> Any:
    """Call an ASTA MCP tool and return its unwrapped payload."""
    body = json.dumps(
        {
            "jsonrpc": "2.0",
            "id": str(uuid4()),
            "method": "tools/call",
            "params": {"name": tool, "arguments": arguments},
        }
    ).encode()
    req = urllib.request.Request(
        ASTA_MCP_URL,
        data=body,
        headers={
            "Accept": "application/json, text/event-stream",
            "Content-Type": "application/json",
            "x-api-key": _api_key(),
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode()
    except urllib.error.HTTPError as exc:
        sys.exit(f"HTTP {exc.code} from ASTA: {exc.read().decode()[:300]}")
    except urllib.error.URLError as exc:
        sys.exit(f"could not reach ASTA: {exc.reason}")

    payload = _extract_rpc_payload(raw)
    if "error" in payload:
        sys.exit(f"ASTA MCP error calling {tool}: {payload['error']}")
    result = payload.get("result", {})
    if result.get("isError"):
        sys.exit(f"ASTA tool error calling {tool}: {json.dumps(result)[:400]}")

    # Preferred: structuredContent carries the payload already parsed, and it
    # keeps multi-item results (get_paper_batch, get_citations) intact.
    structured = result.get("structuredContent")
    if isinstance(structured, dict):
        return structured.get("result", structured)

    # Fallback: content[] holds text parts, each a JSON *string*. Batch calls
    # split across several parts, so collect them all rather than taking [0].
    content = result.get("content")
    if isinstance(content, list) and content:
        parts: list[Any] = []
        for item in content:
            text = item.get("text", "")
            if isinstance(text, str) and text.strip()[:1] in "{[":
                parts.append(json.loads(text))
            elif text:
                parts.append(text)
        if len(parts) == 1:
            return parts[0]
        return parts
    return result


def list_tools(timeout: int = 60) -> Any:
    """Call tools/list — the endpoint's self-description."""
    body = json.dumps(
        {"jsonrpc": "2.0", "id": str(uuid4()), "method": "tools/list", "params": {}}
    ).encode()
    req = urllib.request.Request(
        ASTA_MCP_URL,
        data=body,
        headers={
            "Accept": "application/json, text/event-stream",
            "Content-Type": "application/json",
            "x-api-key": _api_key(),
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return _extract_rpc_payload(resp.read().decode()).get("result", {})


# --------------------------------------------------------------------------
# snippet handling
# --------------------------------------------------------------------------
def _rows(payload: Any) -> list[dict[str, Any]]:
    """Normalize a snippet_search payload to a list of rows."""
    if isinstance(payload, dict):
        for key in ("data", "snippets", "results"):
            if isinstance(payload.get(key), list):
                return payload[key]
        inner = payload.get("result")
        if isinstance(inner, dict):
            return _rows(inner)
    return payload if isinstance(payload, list) else []


def _slim(row: dict[str, Any]) -> dict[str, Any]:
    """Flatten one snippet row into the fields worth looking at."""
    snip = row.get("snippet") or {}
    paper = row.get("paper") or {}
    # refMentions live under snippet.annotations, and the key may be absent or
    # explicitly null; each entry carries matchedPaperCorpusId (bare digits) plus
    # the character offsets of the citation marker within `text`. An entry with
    # no matchedPaperCorpusId is a citation ASTA could not resolve.
    annotations = snip.get("annotations") or {}
    refs = []
    for ref in annotations.get("refMentions") or []:
        cid = ref.get("matchedPaperCorpusId") or ref.get("corpus_id")
        refs.append(
            {
                "corpus_id": f"CorpusId:{cid}" if cid and str(cid).isdigit() else cid,
                "start": ref.get("start"),
                "end": ref.get("end"),
            }
        )
    return {
        "score": row.get("score"),
        "text": snip.get("text") or "",
        "section": snip.get("section"),
        "kind": snip.get("snippetKind"),
        "offset": snip.get("snippetOffset"),
        "sentences": annotations.get("sentences"),
        "corpus_id": paper.get("corpusId") or paper.get("corpus_id"),
        "title": paper.get("title"),
        "ref_mentions": refs,
        "unresolved_refs": sum(1 for r in refs if not r["corpus_id"]),
    }


# --------------------------------------------------------------------------
# local backend: PMC JATS -> chunks -> MiniLM, via the production index
# --------------------------------------------------------------------------
# Deliberately NOT a reimplementation. This calls the same three functions the
# report pipeline uses, so a `--backend local` run differs from `--backend asta`
# in *retrieval only*, not in how the text was prepared:
#
#   fetch_preprint()      DOI -> EuropePMC search -> PMCID -> /fullTextXML.
#                         PMC is the first rung; bioRxiv (curl_cffi, then
#                         playwright) is the fallback for unindexed preprints.
#   build_paper_index()   JATS -> body segments -> 2800/200-char chunks ->
#                         all-MiniLM-L6-v2 embeddings. Hash-idempotent, so a
#                         repeat run of the same paper costs nothing.
#   search()              cosine over the chunk matrix; ASTA-shape rows out.
#
# What is NOT comparable between backends, and why:
#
#   scores        ASTA's come from an opaque reranker and are query-relative;
#                 local's are raw MiniLM cosine (typically 0.0-0.5). Compare
#                 rank order, set overlap and --mentions precision. Never the
#                 numbers. --min-score means something different per backend.
#   chunk bounds  ASTA's are unknown and it emits `kind: "title"` pseudo-
#                 snippets; local is a fixed 2800/200 split. There is no
#                 snippet-identity join — compare by text containment.
#   coverage      ASTA may hold only a title/abstract for a paper (see the
#                 `audit` subcommand). Local JATS is always the full body, but
#                 `extract_body_segments` takes only <p> under abstract/body,
#                 so tables and figure captions are DROPPED. Marker-aspect
#                 queries are therefore biased against the local backend.
#   refMentions   local keeps only refs it could resolve to a CorpusId, so
#                 `unresolved` is structurally 0 here, not a finding.
#   free search   there is no corpus-wide local search. Local is always
#                 paper-scoped, so only paper-scoped ASTA runs are a fair
#                 comparison.

LOCAL_CACHE_DIR = Path(__file__).resolve().parent / ".local_probe_cache"


def _import_local_index() -> Any:
    """Import the production local index, with install guidance on failure."""
    try:
        from atlas_chat.services import local_snippet_index  # noqa: PLC0415
    except ImportError as exc:
        sys.exit(
            f"could not import atlas_chat.services.local_snippet_index ({exc}).\n"
            "The local backend needs the project venv plus the [local-index] extra "
            "(~500 MB of MiniLM):\n"
            "  uv pip install -e 'src/atlas_chat[local-index]'\n"
            "  uv run python experiments/asta_probe.py snippets --backend local ..."
        )
    return local_snippet_index


def _local_dois(paper_ids: str) -> list[str]:
    """Parse -p into bare DOIs. The local backend cannot resolve other id types."""
    out: list[str] = []
    for raw in paper_ids.split(","):
        pid = raw.strip()
        if not pid:
            continue
        low = pid.lower()
        if low.startswith("doi:"):
            pid = pid[4:].strip()
        elif low.startswith(("http://", "https://")):
            pid = re.sub(r"^https?://(dx\.)?doi\.org/", "", pid, flags=re.I)
        elif not pid.startswith("10."):
            sys.exit(
                f"--backend local needs DOIs, got {pid!r}. A CorpusId/PMID/PMCID "
                "cannot be turned into a fetchable source here — pass "
                "DOI:10.xxxx/yyyy (comma-separated for several)."
            )
        out.append(pid)
    if not out:
        sys.exit("--backend local needs at least one DOI in -p/--paper-ids")
    return out


def _ensure_local_papers(lsi: Any, dois: list[str], cache_dir: Path, force: bool) -> None:
    """Fetch + chunk + embed each DOI into ``cache_dir``. Idempotent."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    for i, doi in enumerate(dois):
        # A publisher PDF dropped at the source path wins over a JATS fetch —
        # the escape hatch for closed-access papers EuropePMC will not serve.
        pdf = cache_dir / "local_index" / "papers" / lsi.paper_slug(doi) / "source" / "paper.pdf"
        kwargs = {"pdf_path": pdf} if pdf.exists() else {}
        try:
            manifest = lsi.build_paper_index(
                cache_dir,
                doi,
                role="atlas" if i == 0 else "subatlas",
                force=force,
                **kwargs,
            )
        except Exception as exc:
            sys.exit(
                f"could not build a local index for {doi}: {exc}\n"
                "If EuropePMC has no full text for it (closed access), drop the "
                f"publisher PDF at\n  {pdf}\nand re-run."
            )
        print(
            f"local index: {doi} [{manifest.get('source_type')}] "
            f"{manifest.get('n_chunks', 0)} chunks -> {cache_dir}",
            file=sys.stderr,
        )
    # build_paper_index() does not invalidate search()'s lru_cache, so a
    # build-then-search in one process would otherwise serve a stale matrix.
    lsi._load_index.cache_clear()


def _slim_local(row: dict[str, Any]) -> dict[str, Any]:
    """Map a local_snippet_index.search() row onto _slim()'s shape."""
    refs = []
    for ref in (row.get("annotations") or {}).get("refMentions") or []:
        cid = ref.get("matchedPaperCorpusId") or ref.get("corpus_id")
        cid = str(cid) if cid else None
        if cid and cid.isdigit():
            cid = f"CorpusId:{cid}"
        refs.append({"corpus_id": cid, "start": ref.get("start"), "end": ref.get("end")})
    return {
        "score": row.get("score"),
        "text": row.get("snippet") or "",
        "section": row.get("section"),
        "kind": "chunk",
        "offset": {"chunk_id": row.get("chunk_id")},
        "sentences": None,
        "corpus_id": row.get("corpus_id"),
        "title": row.get("title"),
        "ref_mentions": refs,
        "unresolved_refs": sum(1 for r in refs if not r["corpus_id"]),
    }


def _resolve_project_dir(project_arg: str) -> Path:
    """Same resolution as scripts/setup_local_index.py: a path, or a bare name."""
    candidate = Path(project_arg)
    if candidate.is_dir():
        return candidate.resolve()
    named = Path.cwd() / "projects" / project_arg
    if named.is_dir():
        return named.resolve()
    sys.exit(f"project not found: {project_arg}")


def _local_rows(args: argparse.Namespace) -> list[dict[str, Any]]:
    """Run the query against a local snippet index. Returns raw search rows."""
    if args.venues or args.inserted_before:
        sys.exit("--venues/--inserted-before are ASTA-only filters")
    lsi = _import_local_index()
    dois = _local_dois(args.paper_ids)

    if args.project:
        # An existing curated corpus — search it as-is, never rebuild.
        index_dir = _resolve_project_dir(args.project)
        if not lsi.has_local_index(index_dir):
            sys.exit(
                f"{index_dir} has no local_index/. Build it with the "
                "local-paper-index skill, or omit --project to use the probe cache."
            )
    else:
        index_dir = Path(args.cache_dir).expanduser().resolve()
        _ensure_local_papers(lsi, dois, index_dir, args.force_rebuild)

    if args.show_request:
        print(
            json.dumps({"index_dir": str(index_dir), "dois": dois, "k": args.limit}, indent=2),
            file=sys.stderr,
        )
    return lsi.search(index_dir, args.query, k=args.limit, papers=dois)


def _fmt(text: str, width: int) -> str:
    return " ".join(text.split())[:width]


def cmd_snippets(args: argparse.Namespace) -> int:
    if args.backend == "local":
        payload = _local_rows(args)
        slim = _slim_local
        # local retrieval is always paper-scoped; there is no free search
        paper_scoped = True
    else:
        arguments: dict[str, Any] = {"query": args.query, "limit": args.limit}
        if args.paper_ids:
            arguments["paper_ids"] = args.paper_ids
        if args.venues:
            arguments["venues"] = args.venues
        if args.inserted_before:
            arguments["inserted_before"] = args.inserted_before

        if args.show_request:
            print(json.dumps(arguments, indent=2), file=sys.stderr)

        payload = call_tool("snippet_search", arguments, timeout=args.timeout)
        slim = _slim
        paper_scoped = bool(args.paper_ids)

    if args.raw:
        json.dump(payload, sys.stdout, indent=1)
        print()
        return 0

    rows = [slim(r) for r in _rows(payload)]
    rows.sort(key=lambda r: -(r["score"] or 0))
    returned = len(rows)

    pattern = re.compile(args.mentions, re.I) if args.mentions else None
    if pattern and args.mentions_only:
        rows = [r for r in rows if pattern.search(r["text"])]
    if args.min_score is not None:
        rows = [r for r in rows if (r["score"] or 0) >= args.min_score]
    if args.top:
        rows = rows[: args.top]

    if args.out:
        with open(args.out, "w") as fh:
            json.dump(rows, fh, indent=1)
        print(f"wrote {len(rows)} records -> {args.out}", file=sys.stderr)

    ceiling = ""
    if paper_scoped and returned < args.limit:
        ceiling = f"  (asked {args.limit}: this is the indexed ceiling)"
    print(f"{returned} snippets returned{ceiling}; showing {len(rows)}")

    for i, r in enumerate(rows, 1):
        flag = ""
        if pattern:
            flag = " MENTION" if pattern.search(r["text"]) else "        "
        nrefs = len(r["ref_mentions"])
        ref = f" refs={nrefs}" if args.refs and nrefs else ""
        where = r["section"] if paper_scoped else (r["corpus_id"] or "")
        score = r["score"] if r["score"] is not None else float("nan")
        print(
            f"{i:>3}. {score:.3f}{flag} [{str(where)[:34]:<34}]{ref} "
            f"{_fmt(r['text'], args.width)}"
        )
        if args.refs and nrefs:
            ids = sorted({str(x["corpus_id"]) for x in r["ref_mentions"] if x["corpus_id"]})
            print(f"      -> {', '.join(ids) or '(all unresolved)'}")

    if args.stats:
        _print_stats(rows, returned, pattern)
    return 0


def _print_stats(
    rows: list[dict[str, Any]], returned: int, pattern: re.Pattern[str] | None
) -> None:
    scores = [r["score"] for r in rows if r["score"] is not None]
    print("\n-- stats --")
    if scores:
        print(
            f"score  min={min(scores):.3f}  median={statistics.median(scores):.3f}  "
            f"max={max(scores):.3f}"
        )
        print("NB scores are query-relative; do not compare across queries.")
    sections: dict[str, int] = {}
    for r in rows:
        sections[str(r["section"])] = sections.get(str(r["section"]), 0) + 1
    top = sorted(sections.items(), key=lambda kv: -kv[1])[:8]
    print(f"sections ({len(sections)} distinct): " + ", ".join(f"{k[:26]}={v}" for k, v in top))

    all_refs = {
        str(x["corpus_id"])
        for r in rows
        for x in r["ref_mentions"]
        if x["corpus_id"]
    }
    with_refs = sum(1 for r in rows if r["ref_mentions"])
    unresolved = sum(r["unresolved_refs"] for r in rows)
    print(
        f"refMentions: {with_refs}/{len(rows)} snippets carry one; "
        f"{len(all_refs)} distinct resolvable CorpusIds (the follow-set); "
        f"{unresolved} unresolved"
    )
    if pattern:
        m = sum(1 for r in rows if pattern.search(r["text"]))
        denom = len(rows) or 1
        print(
            f"mentions: {m}/{len(rows)} shown match (precision {m / denom:.0%}); "
            f"{returned} returned in total"
        )


# --------------------------------------------------------------------------
# indexing audit ("is this paper actually in ASTA?")
# --------------------------------------------------------------------------
# GRADUATED: the band classifier below is the calibration record for #22. The
# production implementation lives at `atlas_chat.services.asta_indexing`, under
# unit tests (`tests/unit/test_asta_indexing.py`) and a live integration test
# against the papers in the acceptance criteria. It talks to ASTA through the
# production `AstaProvider` rather than the urllib+SSE wrapper in this file, and
# it adds a `not_in_s2` band for papers absent from Semantic Scholar entirely.
# Change the production module; this file is kept for the measurement it records.
#
# Calibrated 2026-08-21 over 21 papers from the fetal_skin_atlas run. The three
# bands separated with no overlap at all:
#
#   band           snippets   chars           sections   refMentions
#   UNINDEXED      0          0               0          0            (n=6)
#   ABSTRACT_ONLY  2..4       1,219..6,312    0          0            (n=3)
#   FULL           15..72     18,802..105,876 9..30      50..361      (n=12)
#
# `sections` (distinct non-null section names) and `refMentions` are the two
# decisive signals, and they are orthogonal: body chunks carry section names,
# and only a body carries a bibliography. Gaps are large (0 vs >=9 sections;
# 0 vs >=50 refMentions), so the thresholds are not finely tuned.
#
# Deliberately NOT used as signals:
#   - isOpenAccess — no predictive value: 3 of 6 UNINDEXED papers are OA:true,
#     2 of 3 ABSTRACT_ONLY are OA:true, and one FULL paper is OA:false.
#   - chars / abstract_length ratio — breaks when the abstract is missing
#     (ratio 0.0 for a paper with 6,312 indexed chars) or truncated
#     (ratio 426 for a 118-char abstract).
MIN_SECTIONS = 1        # >=1 distinct section name means body text is indexed
PARTIAL_SNIPPETS = 10   # below the observed FULL floor of 15
PARTIAL_CHARS = 15_000  # below the observed FULL floor of 18,802

# The set returned for a paper-scoped search is the paper's whole indexed chunk
# set, independent of the query — verified by running unrelated queries against
# the same paper and getting identical counts. So the audit query is arbitrary;
# it only affects ordering. Override with --query if you want to check that.
AUDIT_QUERY = "cell types methods results discussion"


def audit_paper(pid: str, query: str, limit: int, timeout: int) -> dict[str, Any]:
    """Probe one paper's ASTA indexing depth. One API call in the common case."""
    try:
        payload = call_tool(
            "snippet_search",
            {"query": query, "paper_ids": pid, "limit": limit},
            timeout=timeout,
        )
        rows = [_slim(r) for r in _rows(payload)]
    except SystemExit as exc:  # tool error — record rather than abort the sweep
        return {
            "paper": pid,
            "verdict": "ERROR",
            "error": str(exc),
            "snippets": 0,
            "chars": 0,
            "sections": 0,
            "ref_mentions": 0,
            "distinct_refs": 0,
            "title": None,
        }

    sections = {r["section"] for r in rows if r["section"]}
    refs = sum(len(r["ref_mentions"]) for r in rows)
    distinct = {x["corpus_id"] for r in rows for x in r["ref_mentions"] if x["corpus_id"]}
    chars = sum(len(r["text"]) for r in rows)
    title = next((r["title"] for r in rows if r["title"]), None)

    if not rows:
        verdict, why = "UNINDEXED", "0 snippets — ASTA holds nothing for this paper"
    elif len(sections) < MIN_SECTIONS and refs == 0:
        verdict, why = (
            "ABSTRACT_ONLY",
            f"{len(rows)} snippets, no section names, no refMentions — "
            "title/abstract only, no body text",
        )
    elif len(rows) < PARTIAL_SNIPPETS or chars < PARTIAL_CHARS or refs == 0:
        verdict, why = (
            "PARTIAL",
            f"{len(rows)} snippets / {chars:,} chars / {refs} refMentions — "
            "below the observed full-text floor; check manually",
        )
    else:
        verdict, why = "FULL", f"{len(rows)} snippets across {len(sections)} sections"

    return {
        "paper": pid,
        "verdict": verdict,
        "reason": why,
        "snippets": len(rows),
        "chars": chars,
        "sections": len(sections),
        "ref_mentions": refs,
        "distinct_refs": len(distinct),
        "title": title,
    }


def cmd_audit(args: argparse.Namespace) -> int:
    ids = [i.strip() for i in (args.paper_ids or "").split(",") if i.strip()]
    if args.from_catalogue:
        with open(args.from_catalogue) as fh:
            cat = json.load(fh)
        ids += [k for k in (cat if isinstance(cat, dict) else []) if k not in ids]
    if not ids:
        sys.exit("no paper ids: pass --paper-ids and/or --from-catalogue")

    results = [audit_paper(p, args.query, args.limit, args.timeout) for p in ids]

    if args.json:
        json.dump(results, sys.stdout, indent=1)
        print()
    else:
        print(
            f"{'paper':<24} {'verdict':<14} {'snip':>5} {'chars':>8} "
            f"{'sect':>5} {'refs':>5}  title"
        )
        for r in sorted(results, key=lambda x: (x["verdict"], -x["snippets"])):
            print(
                f"{r['paper']:<24} {r['verdict']:<14} {r['snippets']:>5} "
                f"{r['chars']:>8,} {r['sections']:>5} {r['ref_mentions']:>5}  "
                f"{str(r['title'] or '')[:44]}"
            )
        counts: dict[str, int] = {}
        for r in results:
            counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
        print("\n" + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
        bad = [r for r in results if r["verdict"] != "FULL"]
        if bad:
            print(
                "\nNot usable for snippet retrieval or citation traversal — build a "
                "local index (see the local-paper-index skill):"
            )
            for r in bad:
                print(f"  {r['paper']}: {r['reason']}")

    if args.strict and any(r["verdict"] != "FULL" for r in results):
        return 1
    return 0


def cmd_paper(args: argparse.Namespace) -> int:
    ids = [i.strip() for i in args.paper_ids.split(",") if i.strip()]
    if len(ids) == 1:
        payload = call_tool(
            "get_paper", {"paper_id": ids[0], "fields": args.fields}, timeout=args.timeout
        )
    else:
        payload = call_tool(
            "get_paper_batch", {"ids": ids, "fields": args.fields}, timeout=args.timeout
        )
    json.dump(payload, sys.stdout, indent=1)
    print()
    return 0


def cmd_citations(args: argparse.Namespace) -> int:
    arguments: dict[str, Any] = {"paper_id": args.paper_id, "fields": args.fields}
    if args.limit:
        arguments["limit"] = args.limit
    if args.date_range:
        arguments["publication_date_range"] = args.date_range
    payload = call_tool("get_citations", arguments, timeout=args.timeout)
    json.dump(payload, sys.stdout, indent=1)
    print()
    return 0


def cmd_tools(args: argparse.Namespace) -> int:
    result = list_tools(timeout=args.timeout)
    if args.raw:
        json.dump(result, sys.stdout, indent=1)
        print()
        return 0
    for tool in result.get("tools", []):
        params = (tool.get("inputSchema") or {}).get("properties") or {}
        required = set((tool.get("inputSchema") or {}).get("required") or [])
        print(f"\n{tool['name']}")
        for name, spec in params.items():
            req = "required" if name in required else "optional"
            default = spec.get("default")
            extra = f", default={default!r}" if default not in (None, "") else ""
            print(f"    {name}: {spec.get('type', '?')} [{req}{extra}]")
        first = (tool.get("description") or "").strip().split("\n")[0]
        if first:
            print(f"    -- {first}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Probe the ASTA MCP endpoint directly (retrieval tuning).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Docs: https://asta-tools.allen.ai/mcp/v1/docs",
    )
    p.add_argument("--timeout", type=int, default=120, help="HTTP timeout, seconds")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("snippets", help="snippet_search (ASTA or local index)")
    s.add_argument("-q", "--query", required=True, help="query text")
    s.add_argument(
        "--backend",
        choices=("asta", "local"),
        default="asta",
        help="asta = the MCP endpoint; local = PMC JATS chunked + MiniLM-embedded "
        "via the production local_snippet_index. Local is always paper-scoped and "
        "its scores are NOT comparable with ASTA's (see module docstring).",
    )
    s.add_argument(
        "-p",
        "--paper-ids",
        default="",
        help="comma-separated ids to restrict to (CorpusId:/DOI:/PMID:/PMCID:/ARXIV:); "
        "omit for a corpus-wide free search. Up to 100.",
    )
    s.add_argument("--limit", type=int, default=20, help="snippets requested (default 20)")
    s.add_argument("--venues", default="", help='e.g. "Nature,Science"')
    s.add_argument("--inserted-before", default="", help="YYYY-MM-DD | YYYY-MM | YYYY")
    s.add_argument("--min-score", type=float, help="drop rows below this score")
    s.add_argument("--top", type=int, help="keep only the top N after sorting")
    s.add_argument(
        "--mentions",
        metavar="REGEX",
        help="flag rows whose text matches (e.g. subject aliases). This filter "
        "transfers across queries and papers; score thresholds do not.",
    )
    s.add_argument(
        "--mentions-only", action="store_true", help="keep only rows matching --mentions"
    )
    s.add_argument("--refs", action="store_true", help="show resolved CorpusIds per row")
    s.add_argument("--stats", action="store_true", help="score/section/refMention summary")
    s.add_argument("--width", type=int, default=90, help="text preview width")
    s.add_argument("--out", help="write slim records as JSON here")
    s.add_argument("--raw", action="store_true", help="dump the raw payload")
    s.add_argument("--show-request", action="store_true", help="echo arguments to stderr")
    s.add_argument(
        "--project",
        help="[local] search an existing project's curated local_index instead of "
        "the probe cache (path or bare name under ./projects/). Never rebuilds.",
    )
    s.add_argument(
        "--cache-dir",
        default=str(LOCAL_CACHE_DIR),
        help="[local] where the probe builds its throwaway corpus "
        f"(default {LOCAL_CACHE_DIR.name}/ beside this script)",
    )
    s.add_argument(
        "--force-rebuild",
        action="store_true",
        help="[local] re-fetch and re-embed even if the cached hash matches",
    )
    s.set_defaults(func=cmd_snippets)

    a = sub.add_parser(
        "audit",
        help="smell-test papers for incomplete ASTA indexing",
        description="Classify papers as FULL / PARTIAL / ABSTRACT_ONLY / UNINDEXED. "
        "Costs one snippet_search call per paper. isOpenAccess is not a usable "
        "proxy for this — you have to probe.",
    )
    a.add_argument("-p", "--paper-ids", default="", help="comma-separated ids")
    a.add_argument(
        "--from-catalogue",
        metavar="FILE",
        help="a paper_catalogue.json (keys are CorpusIds) to audit in bulk",
    )
    a.add_argument("--limit", type=int, default=100, help="probe depth (default 100)")
    a.add_argument(
        "--query",
        default=AUDIT_QUERY,
        help="probe query; affects ordering only, not which chunks exist",
    )
    a.add_argument("--json", action="store_true", help="machine-readable output")
    a.add_argument(
        "--strict", action="store_true", help="exit 1 if any paper is not FULL"
    )
    a.set_defaults(func=cmd_audit)

    g = sub.add_parser("paper", help="get_paper / get_paper_batch")
    g.add_argument("-p", "--paper-ids", required=True, help="one id, or comma-separated")
    g.add_argument("--fields", default=PAPER_FIELDS)
    g.set_defaults(func=cmd_paper)

    c = sub.add_parser("citations", help="get_citations (papers citing the target)")
    c.add_argument("-p", "--paper-id", required=True)
    c.add_argument("--fields", default="title,year,authors,externalIds")
    c.add_argument("--limit", type=int, default=100)
    c.add_argument("--date-range", help="YYYY-MM-DD:YYYY-MM-DD (either side optional)")
    c.set_defaults(func=cmd_citations)

    t = sub.add_parser("tools", help="tools/list — the endpoint's own schema")
    t.add_argument("--raw", action="store_true")
    t.set_defaults(func=cmd_tools)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    sys.exit(main())
