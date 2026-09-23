"""Evidence records on disk: finding them, and reading back the ones about a cell type.

A producer writes evidence where it makes sense for a producer to write it. A
paper read takes one paper and answers for many cell types; a scan across the
literature takes one cell type and works across many papers. Neither filing
order suits the other, and making either produce the other's shape means copying
an answer into several places — which then have to be kept identical.

So nothing is copied, and nothing infers what an item is about from where it
sits. Each item names the atlas cell set it is evidence about, and everything
that reads evidence back does it here, by asking for a cell type rather than by
knowing a path. A consumer that never learns the layout is a consumer that does
not break when the layout changes.

A file is evidence if it is named as evidence — ``*.evidence.json``, or one of
the legacy names. It is named after its cell type, which is for whoever runs
``ls``: the name is a label and the item's own ``cell_label`` is the identity.
Nothing checks one against the other, because a mismatch has no consequence —
everything reads the field.

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

#: What a new evidence file is called. Anything ending this way is evidence,
#: wherever it sits and whatever wrote it.
EVIDENCE_SUFFIX = ".evidence.json"

#: Names from before the suffix existed, still written and still read. The
#: single-item form is what a producer writing one answer at a time used.
LEGACY_NAMES = ("all_summaries.json",)
LEGACY_SUFFIX = "evidence_summary.json"


class EvidenceFileError(RuntimeError):
    """A file named as evidence that cannot be read as evidence.

    Raised rather than skipped. A file that claims to be evidence and is not
    readable is a producer fault someone has to see: quietly passing over it
    returns a short collection, and a consumer cannot tell a cell type with
    little evidence from one whose evidence failed to load.
    """


def is_evidence_file(path: Path | str) -> bool:
    """Whether this path names an evidence file.

    By name, not by content. The alternative — opening every JSON file in the
    tree and deciding from its shape — has to parse assembled papers to reject
    them, silently drops a file holding one malformed item, and gives a second
    definition of "evidence file" that can drift from this one. The hook that
    validates these files calls this, so there is only ever one answer.

    Args:
        path: any path; it need not exist.

    Returns:
        True for ``*.evidence.json`` and the legacy names.
    """
    name = Path(path).name
    return name.endswith(EVIDENCE_SUFFIX) or name in LEGACY_NAMES or name.endswith(LEGACY_SUFFIX)


def record_files(traversal_dir: Path) -> Iterator[Path]:
    """Every evidence file under this directory.

    Args:
        traversal_dir: the project's ``traversal_output``.

    Yields:
        Paths, in sorted order, so a collection is stable between runs.
    """
    yield from sorted(p for p in traversal_dir.rglob("*.json") if is_evidence_file(p))


def load_records(path: Path) -> list[dict[str, Any]]:
    """The evidence items in one file.

    Args:
        path: an evidence file.

    Returns:
        Its items. A single-item file is returned as a list of one.

    Raises:
        EvidenceFileError: the file does not parse, or holds something that is
            not evidence.
    """
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise EvidenceFileError(f"{path}: not readable as JSON ({exc})") from exc

    items = data if isinstance(data, list) else [data]
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            raise EvidenceFileError(f"{path}[{i}]: not an evidence item")
        label = item.get("cell_label")
        if label is not None and not isinstance(label, str):
            raise EvidenceFileError(
                f"{path}[{i}]: cell_label is {type(label).__name__}, not a cell type's name. "
                "One cell type per item; an answer bearing on two is two answers."
            )
    return items


def collect(traversal_dir: Path, cell_label: str) -> list[dict[str, Any]]:
    """Every evidence item about this cell type, wherever it was written.

    Args:
        traversal_dir: the project's ``traversal_output``.
        cell_label: the atlas cell set's CAS+ label. Required, and the only way
            to ask: a consumer that cannot name what it is reading for should
            not be reading.

    Returns:
        The items, in file order — from every producer that has written about
        this cell type, whether it filed under the paper it read or under the
        cell type it searched for.
    """
    out: list[dict[str, Any]] = []
    for path in record_files(traversal_dir):
        items = load_records(path)
        out.extend(i for i in items if i.get("cell_label") == cell_label)
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
        for item in load_records(path):
            label = item.get("cell_label")
            if label:
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
        items = load_records(path)
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
            item["cell_label"] = label
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
