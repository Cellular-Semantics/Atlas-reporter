"""CLI for the per-project local snippet index (multi-paper corpus model).

Subcommands::

    discover-subatlas   Propose subatlas DOIs from label_provenance.json.
    init-corpus         Run the asta/jats/pdf waterfall + build atlas index.
    add                 Add a paper from a PDF or JATS file.
    list                List papers in the corpus.
    remove              Remove a paper from the corpus.
    search              Query the corpus.
    build               (legacy) Build only the atlas paper from JATS.

Project resolution: ``--project`` accepts either a path to a project dir or a
bare name. Bare names are looked up under ``./projects/``.
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path


def _resolve_project_dir(project_arg: str) -> Path:
    p = Path(project_arg)
    if p.is_dir():
        return p.resolve()
    candidate = Path.cwd() / "projects" / project_arg
    if candidate.is_dir():
        return candidate.resolve()
    raise FileNotFoundError(f"Project not found: {project_arg}")


def _doi_from_config(project_dir: Path) -> str | None:
    cfg = project_dir / "cell_type_annotations.json"
    if not cfg.exists():
        return None
    try:
        return json.loads(cfg.read_text()).get("source", {}).get("doi")
    except Exception:
        return None


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", maxsplit=1)[0])
    parser.add_argument("-v", "--verbose", action="store_true")
    sub = parser.add_subparsers(dest="cmd")

    p_disc = sub.add_parser("discover-subatlas")
    p_disc.add_argument("--project", required=True)

    p_init = sub.add_parser("init-corpus")
    p_init.add_argument("--project", required=True)
    p_init.add_argument("--force", action="store_true")

    p_add = sub.add_parser("add")
    p_add.add_argument("--project", required=True)
    p_add.add_argument("--doi", required=True)
    src = p_add.add_mutually_exclusive_group()
    src.add_argument("--pdf", type=Path, default=None)
    src.add_argument("--jats", type=Path, default=None)
    p_add.add_argument("--role", default="subatlas", choices=("atlas", "subatlas"))
    p_add.add_argument("--force", action="store_true")

    p_list = sub.add_parser("list")
    p_list.add_argument("--project", required=True)

    p_rm = sub.add_parser("remove")
    p_rm.add_argument("--project", required=True)
    p_rm.add_argument("--doi", required=True)

    p_search = sub.add_parser("search")
    p_search.add_argument("--project", required=True)
    p_search.add_argument("--query", required=True)
    p_search.add_argument("-k", type=int, default=10)
    p_search.add_argument("--paper", action="append", default=None)
    p_search.add_argument("--role", action="append", default=None, choices=("atlas", "subatlas"))

    p_build = sub.add_parser("build", help="(legacy) build only the atlas paper")
    p_build.add_argument("--project", required=True)
    p_build.add_argument("--doi", default=None)
    p_build.add_argument("--jats", type=Path, default=None)
    p_build.add_argument("--force", action="store_true")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    if args.cmd is None:
        parser.print_help()
        return 0

    project_dir = _resolve_project_dir(args.project)

    if args.cmd == "discover-subatlas":
        from atlas_chat.services.subatlas_resolver import discover

        result = discover(project_dir)
        print(json.dumps(result, indent=2))
        return 0

    if args.cmd == "init-corpus":
        from atlas_chat.services.subatlas_resolver import ingest

        result = ingest(project_dir, force=args.force)
        print(json.dumps(result, indent=2))
        return 0

    if args.cmd == "add":
        from atlas_chat.services.local_snippet_index import add_paper

        manifest = add_paper(
            project_dir,
            args.doi,
            pdf_path=args.pdf,
            jats_path=args.jats,
            role=args.role,
            force=args.force,
        )
        print(json.dumps(manifest, indent=2))
        return 0

    if args.cmd == "list":
        from atlas_chat.services.local_snippet_index import list_papers

        print(json.dumps(list_papers(project_dir), indent=2))
        return 0

    if args.cmd == "remove":
        from atlas_chat.services.local_snippet_index import remove_paper

        present = remove_paper(project_dir, args.doi)
        print(json.dumps({"removed": present}, indent=2))
        return 0

    if args.cmd == "search":
        from atlas_chat.services.local_snippet_index import search

        results = search(
            project_dir,
            args.query,
            k=args.k,
            papers=args.paper,
            roles=args.role,
        )
        print(json.dumps(results, indent=2))
        return 0

    if args.cmd == "build":
        from atlas_chat.services.local_snippet_index import build_local_index

        doi = args.doi or _doi_from_config(project_dir)
        if not doi:
            print(
                "ERROR: no DOI supplied and none found in cell_type_annotations.json",
                file=sys.stderr,
            )
            return 1
        manifest = build_local_index(project_dir, doi, args.jats, args.force)
        print(json.dumps(manifest, indent=2))
        return 0

    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
