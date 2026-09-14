"""Check a differential-expression store, and say what is in it.

Extraction itself is not here, and deliberately. Every published table is laid
out differently — three cell types side by side under one header, both
directions interleaved, a title row above the real one, a gene column that is
actually an index — so the conversion is written for the source in front of you
rather than by a parser trying to anticipate all of them. What belongs in code
that ships is the part that does not vary: whether the result conforms, and
whether someone could redo it.

Repeatability is the second of those and is checked, not assumed. A store holds
the converted files, the code that converted them, and a note saying where the
numbers came from. Any of the three missing means the numbers cannot be traced
back to the table they were read from.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

SCHEMA = "degs.schema.json"

#: Written by the conversion, alongside the files it produced.
README = "README.md"


class DegsError(RuntimeError):
    """Raised when a store cannot be read at all."""


@dataclass
class StoreReport:
    """What a store holds, and what is wrong with it."""

    files: int = 0
    cell_sets: list[str] = field(default_factory=list)
    comparisons: int = 0
    genes: int = 0
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors

    def to_dict(self) -> dict[str, Any]:
        return {
            "files": self.files,
            "cell_sets": self.cell_sets,
            "comparisons": self.comparisons,
            "genes": self.genes,
            "ok": self.ok,
            "errors": self.errors,
        }


def validate_document(doc: object) -> list[str]:
    """Schema errors in one document, plus the counts it states about itself.

    Args:
        doc: a parsed DEG document.

    Returns:
        One message per problem; empty when the document conforms.
    """
    import jsonschema  # type: ignore[import-untyped]

    from atlas_chat.schemas import load_schema

    validator = jsonschema.Draft202012Validator(load_schema(SCHEMA))
    errors = [
        f"{'.'.join(str(p) for p in e.absolute_path) or '(root)'}: {e.message}"
        for e in sorted(validator.iter_errors(doc), key=lambda e: list(e.path))
    ]
    if errors or not isinstance(doc, dict):
        return errors

    # A count that disagrees with the rows is worse than no count: it is read as
    # a statement about what the paper published and used to interpret absence.
    for index, comparison in enumerate(doc.get("comparisons") or []):
        genes = comparison.get("genes") or []
        stated = comparison.get("n_genes")
        if stated is not None and stated != len(genes):
            errors.append(f"comparisons[{index}]: n_genes is {stated} but {len(genes)} are listed")
        up = sum(1 for g in genes if g.get("direction") == "up")
        stated_up = comparison.get("n_up")
        if stated_up is not None and stated_up != up:
            errors.append(f"comparisons[{index}]: n_up is {stated_up} but {up} are marked up")
        effect = comparison.get("effect_field")
        missing = [g["symbol"] for g in genes if effect not in (g.get("scores") or {})]
        if missing:
            errors.append(
                f"comparisons[{index}]: effect_field {effect!r} absent from "
                f"{len(missing)} gene(s), first {missing[0]!r}"
            )
    return errors


def validate_file(path: Path) -> list[str]:
    """Schema and self-consistency errors in one file."""
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"unreadable: {exc}"]
    return validate_document(doc)


def check_store(store: Path) -> StoreReport:
    """Validate every document in a store, and that it can be reproduced.

    Args:
        store: the directory holding the converted files.

    Returns:
        Counts, and one error per problem found.

    Raises:
        DegsError: the directory does not exist.
    """
    if not store.is_dir():
        raise DegsError(f"no such store: {store}")

    report = StoreReport()
    for path in sorted(store.glob("*.json")):
        report.files += 1
        errors = validate_file(path)
        report.errors.extend(f"{path.name}: {e}" for e in errors)
        if errors:
            continue
        doc = json.loads(path.read_text(encoding="utf-8"))
        report.cell_sets.append(doc["cell_label"])
        for comparison in doc["comparisons"]:
            report.comparisons += 1
            report.genes += len(comparison.get("genes") or [])

    if not report.files:
        report.errors.append(f"no documents in {store}")
    if not (store / README).is_file():
        report.errors.append(
            f"no {README}: without it nobody can tell which table these numbers came from"
        )
    if not list(store.glob("*.py")):
        report.errors.append(
            "no conversion code kept: the extraction cannot be repeated or checked"
        )
    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m atlas_chat.cli_degs",
        description="Check a differential-expression store.",
    )
    parser.add_argument("--store", help="directory of converted files")
    parser.add_argument("--file", help="a single document")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if bool(args.store) == bool(args.file):
        print("give exactly one of --store or --file")
        return 2

    if args.file:
        errors = validate_file(Path(args.file))
        for error in errors:
            print(f"  - {error}")
        print("invalid" if errors else "valid")
        return 2 if errors else 0

    try:
        report = check_store(Path(args.store))
    except DegsError as exc:
        print(str(exc))
        return 2
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.ok else 2
