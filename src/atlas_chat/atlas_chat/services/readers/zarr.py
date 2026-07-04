"""AnnData-zarr ObsReader for cxg-author-probe.

Registers an ``ObsReader`` (see ``cxg_author_probe.readers.base``) so
cxg-author-probe's ``probe()`` / ``pull()`` can read AnnData-zarr stores — its
built-in zarr reader is a stub. Reads only ``obs`` (never X/var), decoding the
AnnData categorical encoding (``categories`` + ``codes``, ``-1`` = NaN) for both
zarr v2 and v3 stores.

Deliberately lives in a module whose name ends in ``.zarr`` so
``cxg_author_probe.probe._format_from_reader_module`` derives ``anndata-zarr``
for the probe's ``source.format`` (it keys off the handle class's module name,
not the reader's ``FORMAT`` attribute).

``zarr`` / ``numpy`` are imported lazily so importing this module never requires
the ``[zarr-reader]`` extra until a store is actually opened. Register with
:func:`register_zarr_reader` before calling ``cxg_author_probe`` entry points.
"""
from __future__ import annotations

from collections.abc import Iterator
from typing import Any
from urllib.parse import urlparse


def _open_zarr_group(url: str) -> Any:
    """Open the root AnnData-zarr group at ``url`` read-only (local or remote)."""
    import zarr

    parsed = urlparse(url)
    if parsed.scheme in ("", "file"):
        path = parsed.path if parsed.scheme == "file" else url
        return zarr.open_group(path, mode="r")
    # Remote (http/https/s3/gs) via fsspec.
    try:
        from zarr.storage import FsspecStore

        store: Any = FsspecStore.from_url(url, read_only=True)
    except Exception:
        import fsspec

        store = fsspec.get_mapper(url)
    return zarr.open_group(store=store, mode="r")


class AnndataZarrObsHandle:
    """Lazy view into an AnnData-zarr ``obs`` group (cxg-author-probe ObsHandle)."""

    def __init__(self, root: Any) -> None:
        import numpy as np

        self._np = np
        self._root = root
        self._obs = root["obs"]
        self._attrs = dict(self._obs.attrs)
        self._index = self._attrs.get("_index", "_index")

    # --- structure helpers ---------------------------------------------------
    def _is_group(self, node: Any) -> bool:
        import zarr

        return isinstance(node, zarr.Group)

    def _is_categorical(self, node: Any) -> bool:
        return self._is_group(node) and node.attrs.get("encoding-type") == "categorical"

    def _decode(self, values: Any) -> list:
        """Decode a numpy array of obs values to JSON-serialisable primitives."""
        arr = self._np.asarray(values)
        return [v.decode() if isinstance(v, bytes) else v for v in arr.tolist()]

    # --- ObsHandle Protocol --------------------------------------------------
    def n_cells(self) -> int:
        return int(self._obs[self._index].shape[0])

    def list_columns(self) -> list[str]:
        cols = list(self._attrs.get("column-order", []))
        return [c for c in cols if c != self._index]

    def describe(self, col: str) -> Any:
        from cxg_author_probe.models import ColumnDescriptor, ColumnKind

        node = self._obs[col]
        if self._is_categorical(node):
            cats = node["categories"]
            codes = node["codes"]
            n_cat = int(cats.shape[0])
            return ColumnDescriptor(
                kind=ColumnKind.categorical,
                dtype=str(cats.dtype),
                n_unique=n_cat,  # categorical n_unique == n_categories (probe expects it preset)
                n_categories=n_cat,
                shape=list(codes.shape),
                encoding="categorical",
            )
        if self._is_group(node):
            return ColumnDescriptor(
                kind=ColumnKind.group,
                dtype="group",
                encoding=node.attrs.get("encoding-type"),
            )
        return ColumnDescriptor(
            kind=ColumnKind.array,
            dtype=str(node.dtype),
            shape=list(node.shape),
            encoding=node.attrs.get("encoding-type", "array"),
        )

    def head_sample(self, col: str, n: int = 20) -> list:
        node = self._obs[col]
        if self._is_categorical(node):
            cats = self._decode(node["categories"][:])
            codes = self._np.asarray(node["codes"][:n])
            return [cats[c] if c >= 0 else None for c in codes.tolist()]
        return self._decode(node[:n])

    def iter_chunks(self, col: str) -> Iterator[Any]:
        np = self._np
        node = self._obs[col]
        if self._is_categorical(node):
            cats = np.asarray(self._decode(node["categories"][:]), dtype=object)
            codes = node["codes"]
            step = codes.chunks[0] if getattr(codes, "chunks", None) else codes.shape[0]
            for i in range(0, codes.shape[0], step or codes.shape[0]):
                block = np.asarray(codes[i : i + step])
                yield np.array(
                    [cats[c] if c >= 0 else None for c in block.tolist()], dtype=object
                )
        else:
            step = node.chunks[0] if getattr(node, "chunks", None) else node.shape[0]
            for i in range(0, node.shape[0], step or node.shape[0]):
                yield np.asarray(node[i : i + step])

    def pull_full(self, col: str) -> Any:
        np = self._np
        chunks = [np.asarray(c) for c in self.iter_chunks(col)]
        if not chunks:
            return np.array([])
        return np.concatenate(chunks)

    def joinids(self) -> Any:
        return self._np.asarray(self._decode(self._obs[self._index][:]), dtype=object)

    def close(self) -> None:  # nothing to release for read-only local/fsspec stores
        pass


class AnndataZarrReader:
    """Factory binding a URL to an :class:`AnndataZarrObsHandle`."""

    SUPPORTED_SCHEMES: tuple[str, ...] = ("http", "https", "file", "s3", "gs")
    SUPPORTED_SUFFIXES: tuple[str, ...] = (".zarr", ".zarr/")
    FORMAT: str = "anndata-zarr"

    def open(self, url: str) -> AnndataZarrObsHandle:
        return AnndataZarrObsHandle(_open_zarr_group(url))


def register_zarr_reader() -> None:
    """Register :class:`AnndataZarrReader` at the front of cxg-author-probe's dispatch.

    Idempotent enough for practical use — re-registering just prepends another
    (equivalent) entry; the first match still wins.
    """
    from cxg_author_probe.readers.registry import register_reader

    register_reader(AnndataZarrReader)
