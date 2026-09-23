"""Evidence records on disk: finding them, and reading back the ones about a cell type.

A producer writes evidence where it makes sense for a producer to write it. A
paper read takes one paper and answers for many cell types; a scan across the
literature takes one cell type and works across many papers. Neither filing
order suits the other, and making either produce the other's shape means copying
an answer into several places — which then have to be kept identical.

So nothing is copied, and nothing infers what an item is about from where it
sits. Each item names the atlas cell sets it is evidence about, and everything
that reads evidence back does it here, by asking for a cell type rather than by
knowing a path. A consumer that never learns the layout is a consumer that does
not break when the layout changes.

Reading is a directory walk and a filter. There is no index, deliberately: an
index is a second thing that has to be kept true, and at a few hundred small
files the walk is not what anyone will be waiting for.

.. code-block:: bash

    python -m atlas_chat.cli_evidence collect --traversal <dir> --cell-label "Immune_oLAM"
    python -m atlas_chat.cli_evidence backfill --traversal <dir> --dry-run
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import Any

#: Fields every evidence item carries. Used to tell an evidence file from the
#: other JSON in a traversal directory without depending on filenames — job
#: files, subject blocks and selections all live there too, and a producer is
#: free to name its output what it likes.
_RECORD_FIELDS = ("source_paper", "summary", "quotes")


def looks_like_record(value: Any) -> bool:
    """Whether this object is an evidence item.

    Args:
        value: anything parsed out of a JSON file.

    Returns:
        True if it carries the fields every evidence item has. Duck-typing
        rather than schema validation: this decides whether a file is worth
        looking at, and a malformed item should be reported by the validator
        that owns that judgement, not skipped silently here.
    """
    return isinstance(value, dict) and all(f in value for f in _RECORD_FIELDS)


def record_files(traversal_dir: Path) -> Iterator[Path]:
    """Every file under this directory that holds evidence items.

    A traversal directory also holds assembled papers, subject blocks and cell
    type selections. Those are JSON objects; an evidence file is an array, so
    the top-level type rules most of them out before anything is inspected.

    Args:
        traversal_dir: the project's ``traversal_output``.

    Yields:
        Paths, in sorted order, so a collection is stable between runs.
    """
    for path in sorted(traversal_dir.rglob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, list) and data and all(looks_like_record(i) for i in data):
            yield path


def collect(traversal_dir: Path, cell_label: str) -> list[dict[str, Any]]:
    """Every evidence item about this cell type, wherever it was written.

    Args:
        traversal_dir: the project's ``traversal_output``.
        cell_label: the atlas cell set's CAS+ label. Required, and the only way
            to ask: a consumer that cannot name what it is reading for should
            not be reading.

    Returns:
        The items, in file order. Each one still carries its own
        ``cell_label``, so an item that also bears on other cell sets says so —
        which is what a report needs in order to describe a disagreement
        honestly rather than as a fact about one cell type.
    """
    out: list[dict[str, Any]] = []
    for path in record_files(traversal_dir):
        items = json.loads(path.read_text(encoding="utf-8"))
        out.extend(i for i in items if cell_label in (i.get("cell_label") or []))
    return out


def cell_labels(traversal_dir: Path) -> dict[str, int]:
    """Every cell type this directory holds evidence about, and how much.

    Args:
        traversal_dir: the project's ``traversal_output``.

    Returns:
        Labels mapped to their item count, so a caller can see what is there
        before asking for one — and see a label it did not expect, which is
        usually a producer filing under the wrong name.
    """
    counts: dict[str, int] = {}
    for path in record_files(traversal_dir):
        for item in json.loads(path.read_text(encoding="utf-8")):
            for label in item.get("cell_label") or []:
                counts[label] = counts.get(label, 0) + 1
    return dict(sorted(counts.items()))


def backfill(traversal_dir: Path, *, dry_run: bool = False) -> list[str]:
    """Fill ``cell_label`` on items written before items carried one.

    Evidence used to be identified by the directory it sat in, one per cell
    type. Where that is still the arrangement, the directory name is the label,
    and recovering it is a rename rather than a judgement — no re-read, no
    model.

    Args:
        traversal_dir: the project's ``traversal_output``.
        dry_run: report what would change without writing.

    Returns:
        One line per file touched or refused, for printing. An item that
        cannot be attributed is reported and left alone: a guessed label files
        evidence under a cell type nobody read.
    """
    report: list[str] = []
    for path in record_files(traversal_dir):
        items = json.loads(path.read_text(encoding="utf-8"))
        missing = [i for i in items if not i.get("cell_label")]
        if not missing:
            continue
        label = path.parent.name
        if path.parent == traversal_dir:
            report.append(
                f"skipped {path}: sits at the top of the traversal directory, "
                "so there is no cell type name to take"
            )
            continue
        for item in missing:
            item["cell_label"] = [label]
        if not dry_run:
            path.write_text(
                json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
            )
        verb = "would fill" if dry_run else "filled"
        report.append(f"{verb} {len(missing)} of {len(items)} in {path} with {label!r}")
    return report


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    """The command line, so evidence is readable without a Claude Code session."""
    parser = argparse.ArgumentParser(
        prog="python -m atlas_chat.cli_evidence",
        description="Read evidence items back by the cell type they are about.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    collect_p = sub.add_parser("collect", help="items about one cell type")
    collect_p.add_argument("--traversal", type=Path, required=True)
    collect_p.add_argument("--cell-label", required=True)
    collect_p.add_argument("--out", type=Path, help="write the items here instead of stdout")

    labels_p = sub.add_parser("labels", help="what this directory holds evidence about")
    labels_p.add_argument("--traversal", type=Path, required=True)

    backfill_p = sub.add_parser("backfill", help="fill cell_label from directory names")
    backfill_p.add_argument("--traversal", type=Path, required=True)
    backfill_p.add_argument("--dry-run", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    traversal: Path = args.traversal
    if not traversal.is_dir():
        print(f"no traversal directory at {traversal}", file=sys.stderr)
        return 2

    if args.command == "collect":
        items = collect(traversal, args.cell_label)
        text = json.dumps(items, indent=2, ensure_ascii=False) + "\n"
        if args.out:
            args.out.write_text(text, encoding="utf-8")
            print(f"{len(items)} items about {args.cell_label!r} -> {args.out}")
        else:
            print(text, end="")
        return 0

    if args.command == "labels":
        for label, count in cell_labels(traversal).items():
            print(f"{count:5d}  {label}")
        return 0

    for line in backfill(traversal, dry_run=args.dry_run):
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
