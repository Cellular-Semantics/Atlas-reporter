"""CLI for CAS+ integration provenance.

Thin entry point so ``transferred_annotations`` can be produced without a Claude
Code session:

.. code-block:: bash

    python -m atlas_chat.cli_cas transfer \
        --cas projects/test_projects/hca_reproductive/cas.json \
        --obs obs.tsv --cell-type-col celltype_HCA_fine --labelset L4 \
        --source "celltype_Ulrich2024=10.1073/pnas.2404775121;Ulrich;2024" \
        --source celltype_OvarySanger2026

    python -m atlas_chat.cli_cas backfill-totals --cas .../cas.json

The implementation lives in :mod:`atlas_chat.services.annotation_transfer`.
"""

from __future__ import annotations

from atlas_chat.services.annotation_transfer import build_parser, main

__all__ = ["build_parser", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
