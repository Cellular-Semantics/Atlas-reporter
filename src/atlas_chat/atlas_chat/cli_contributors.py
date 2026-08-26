"""CLI for the subatlas-contributors view.

Thin entry point so the cutoff is applied identically wherever it runs:

.. code-block:: bash

    python -m atlas_chat.cli_contributors \
        --cas projects/test_projects/hca_reproductive/cas.json \
        --cell-type "Activated post-capillary venous endothelial" \
        --out traversal_output/<cell_type>/subatlas_contributors.json

The implementation lives in :mod:`atlas_chat.services.subatlas_contributors`.
"""

from __future__ import annotations

from atlas_chat.services.subatlas_contributors import build_parser, main

__all__ = ["build_parser", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
