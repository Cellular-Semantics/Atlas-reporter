"""Project-setup CLI: build the local snippet index for a fresh-preprint atlas.

Wraps `atlas_chat.services.local_snippet_index.build_local_index` with project
discovery (reads DOI from cell_type_annotations.json if --doi isn't passed).

Example:
    uv run python scripts/setup_local_index.py --project spatial_skin_atlas
    uv run python scripts/setup_local_index.py --project some_atlas --doi 10.1101/... --force
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
    # Try projects/<name>
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n", maxsplit=1)[0])
    parser.add_argument(
        "--project",
        required=True,
        help="Project directory or name (under projects/)",
    )
    parser.add_argument(
        "--doi",
        default=None,
        help="DOI of the preprint. Read from cell_type_annotations.json if omitted.",
    )
    parser.add_argument(
        "--jats",
        type=Path,
        default=None,
        help="Path to an existing JATS XML; skip fetch step.",
    )
    parser.add_argument("--force", action="store_true", help="Rebuild even if up to date")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )

    project_dir = _resolve_project_dir(args.project)
    doi = args.doi or _doi_from_config(project_dir)
    if not doi:
        print(
            "ERROR: no DOI supplied and none found in cell_type_annotations.json",
            file=sys.stderr,
        )
        return 1

    # Lazy import — keeps `--help` snappy when the heavy ML stack isn't installed.
    from atlas_chat.services.local_snippet_index import build_local_index

    manifest = build_local_index(project_dir, doi, args.jats, args.force)
    print(json.dumps(manifest, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
