"""CLI for reading a CAS+ document as a table.

Thin entry point:

.. code-block:: bash

    python -m atlas_chat.cli_report annotations --cas projects/<p>/cas.json
    python -m atlas_chat.cli_report annotations --cas <cas.json> --labelset L4 --out table.tsv

The implementation lives in :mod:`atlas_chat.services.cas_report`.
"""

from __future__ import annotations

from atlas_chat.services.cas_report import build_parser, main

__all__ = ["build_parser", "main"]

if __name__ == "__main__":
    raise SystemExit(main())
