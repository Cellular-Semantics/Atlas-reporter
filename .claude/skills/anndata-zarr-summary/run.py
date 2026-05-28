#!/usr/bin/env python3
"""Reference implementation for the anndata-zarr-summary skill.

Pulls only `obs/` metadata from an AnnData-zarr store and produces:
- co_annotations__<col>.json (full distributions)
- cell_type_annotations__<col>.json (trimmed, atlas_chat-ready)

Supports zarr v2 and v3, http(s)/gs/file URLs, multiple cell-type columns,
disk caching keyed by URL hash.

Never downloads X/, var/, or any expression data.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import io
import json
import os
import struct
import sys
import urllib.parse
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

CACHE_ROOT = Path.home() / ".cache" / "anndata-zarr-summary"
CANDIDATE_CELL_TYPE_COLS = [
    "cell_type",
    "cell_type_ontology_term_id",
    "refined_celltype",
    "celltype",
    "Cluster",
    "annotation",
    "leiden",
    "louvain",
    "seurat_clusters",
]


# ---------------------------------------------------------------- URL helpers

def normalise_url(raw: str) -> tuple[str, bool]:
    """Return (base_url, is_local). gs:// → https://; ./local → file path."""
    if raw.startswith("gs://"):
        return "https://storage.googleapis.com/" + raw[5:].lstrip("/"), False
    if raw.startswith(("http://", "https://")):
        return raw.rstrip("/"), False
    if raw.startswith("file://"):
        return raw[7:].rstrip("/"), True
    # plain path
    p = Path(raw).resolve()
    return str(p), True


def fetch_bytes(base: str, path: str, is_local: bool) -> bytes | None:
    """Fetch one path under the zarr root. Returns None on 404."""
    if is_local:
        f = Path(base) / path
        if not f.exists():
            return None
        return f.read_bytes()
    url = base + "/" + path
    req = urllib.request.Request(url, headers={"User-Agent": "anndata-zarr-summary/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code in (404, 410):
            return None
        if e.code in (401, 403):
            raise RuntimeError(
                f"Got HTTP {e.code} on {url}. This store requires authentication; "
                "this skill does not handle auth. Resolve the URL with a separate "
                "step or supply a public mirror."
            ) from None
        raise


def fetch_json(base: str, path: str, is_local: bool) -> dict | None:
    raw = fetch_bytes(base, path, is_local)
    if raw is None:
        return None
    return json.loads(raw)


# ---------------------------------------------------------------- zarr v2/v3

def detect_format(base: str, is_local: bool) -> str:
    """Return 'v3' or 'v2' for the root."""
    if fetch_json(base, "zarr.json", is_local) is not None:
        return "v3"
    if fetch_json(base, ".zattrs", is_local) is not None:
        return "v2"
    raise RuntimeError(f"No zarr.json or .zattrs found at {base} — not an AnnData-zarr root")


def read_group_meta(base: str, path: str, is_local: bool, fmt: str) -> dict:
    """Read the attributes dict for a group at `path` (path relative to root, no leading /)."""
    if fmt == "v3":
        meta = fetch_json(base, f"{path}/zarr.json", is_local) or {}
        return meta.get("attributes", {})
    else:  # v2
        return fetch_json(base, f"{path}/.zattrs", is_local) or {}


def read_array_meta(base: str, path: str, is_local: bool, fmt: str) -> dict:
    """Read array metadata (shape, dtype, chunks)."""
    if fmt == "v3":
        return fetch_json(base, f"{path}/zarr.json", is_local) or {}
    else:
        zarray = fetch_json(base, f"{path}/.zarray", is_local) or {}
        # normalise to v3-like shape
        return {
            "shape": zarray.get("shape"),
            "data_type": zarray.get("dtype", "").lstrip("|<>"),
            "chunk_grid": {"configuration": {"chunk_shape": zarray.get("chunks")}},
            "codecs": [{"name": "zstd"}] if "zstd" in str(zarray.get("compressor", "")).lower() else [],
            "_zarray_raw": zarray,
        }


def chunk_path(idx: int, fmt: str) -> str:
    """v3: 'c/0' ; v2 (1-D): 'c/0.0' (but actually v2 uses '0' at root or 'c/0' depending on version).

    AnnData v2 stores typically use plain numeric chunk filenames at the array root.
    But spec-compliant writers (older zarr-python v2) write to '0' at the array dir,
    not 'c/0'. We try both.
    """
    if fmt == "v3":
        return f"c/{idx}"
    return f"{idx}"


# ---------------------------------------------------------------- decoding

def zstd_decompress(raw: bytes) -> bytes:
    try:
        import zstandard as zstd
    except ImportError as e:
        raise RuntimeError("zstandard package required: pip install zstandard") from e
    return zstd.ZstdDecompressor().decompress(raw)


def decode_vlen_utf8(blob: bytes) -> list[str]:
    """AnnData zarr vlen-utf8 encoding for string arrays:
    [4-byte LE count][per item: 4-byte LE length, then UTF-8 bytes].
    """
    pos = 0
    (n,) = struct.unpack("<I", blob[pos : pos + 4])
    pos += 4
    out = []
    for _ in range(n):
        (L,) = struct.unpack("<I", blob[pos : pos + 4])
        pos += 4
        out.append(blob[pos : pos + L].decode("utf-8"))
        pos += L
    return out


def numpy_dtype_for(data_type: str) -> str:
    """Map AnnData/zarr data_type strings to numpy dtype."""
    dt = data_type.lower().lstrip("|<>")
    return {
        "int8": "<i1",
        "i1": "<i1",
        "int16": "<i2",
        "i2": "<i2",
        "int32": "<i4",
        "i4": "<i4",
        "int64": "<i8",
        "i8": "<i8",
    }.get(dt, dt)


def num_chunks(shape: list[int], chunk_shape: list[int]) -> int:
    """Number of chunks along first dim (obs columns are 1-D)."""
    import math

    return math.ceil(shape[0] / chunk_shape[0])


def decode_codes(chunks: list[bytes], data_type: str, n_cells: int):
    import numpy as np

    pieces = [zstd_decompress(c) if _looks_zstd(c) else c for c in chunks]
    blob = b"".join(pieces)
    return np.frombuffer(blob, dtype=numpy_dtype_for(data_type))[:n_cells]


def _looks_zstd(b: bytes) -> bool:
    return len(b) >= 4 and b[:4] == b"\x28\xb5\x2f\xfd"


# ---------------------------------------------------------------- cache

def cache_dir_for(zarr_url: str, column: str) -> Path:
    h = hashlib.sha256(zarr_url.encode("utf-8")).hexdigest()[:16]
    d = CACHE_ROOT / h / column
    d.mkdir(parents=True, exist_ok=True)
    return d


# ---------------------------------------------------------------- main flow

def list_categorical_columns(base: str, is_local: bool, fmt: str) -> tuple[dict[str, dict], dict]:
    """Return (col_meta, root_meta) where col_meta is {col_name: {n_categories, codes_meta}}."""
    obs_attrs = read_group_meta(base, "obs", is_local, fmt)
    col_order = obs_attrs.get("column-order", [])
    if not col_order:
        raise RuntimeError("obs/ has no column-order attribute — not a valid AnnData dataframe")

    col_meta = {}
    for col in col_order:
        attrs = read_group_meta(base, f"obs/{col}", is_local, fmt)
        if attrs.get("encoding-type") != "categorical":
            continue
        cats_meta = read_array_meta(base, f"obs/{col}/categories", is_local, fmt)
        codes_meta = read_array_meta(base, f"obs/{col}/codes", is_local, fmt)
        if not cats_meta.get("shape") or not codes_meta.get("shape"):
            continue
        col_meta[col] = {
            "n_categories": cats_meta["shape"][0],
            "codes_meta": codes_meta,
        }
    n_cells = next(iter(col_meta.values()))["codes_meta"]["shape"][0]
    return col_meta, {"n_cells_total": n_cells, "n_columns_total": len(col_order)}


def load_column(
    base: str, is_local: bool, fmt: str, col: str, codes_meta: dict, n_cells: int, cache: Path, no_cache: bool
) -> tuple[list[str], "np.ndarray", dict]:
    """Return (categories, codes_array, stats) — using cache when available."""
    import numpy as np

    cats_file = cache / "categories.json"
    codes_file = cache / "codes.npy"
    stats = {"cache_hit": False, "chunks_downloaded": 0}

    if not no_cache and cats_file.exists() and codes_file.exists():
        categories = json.loads(cats_file.read_text())
        codes = np.load(codes_file)
        stats["cache_hit"] = True
        return categories, codes, stats

    # categories — always 1 chunk for string arrays in practice
    cats_raw = fetch_bytes(base, f"obs/{col}/categories/{chunk_path(0, fmt)}", is_local)
    if cats_raw is None:
        # try v2-flat (just numeric)
        cats_raw = fetch_bytes(base, f"obs/{col}/categories/0", is_local)
    if cats_raw is None:
        raise RuntimeError(f"Could not fetch categories chunk for column {col}")
    categories = decode_vlen_utf8(zstd_decompress(cats_raw))
    stats["chunks_downloaded"] += 1

    # codes
    chunk_shape = codes_meta["chunk_grid"]["configuration"]["chunk_shape"]
    n_chunks = num_chunks(codes_meta["shape"], chunk_shape)

    # parallel chunk fetch
    def fetch_chunk(i):
        for path_fn in (lambda i: chunk_path(i, fmt), lambda i: str(i)):
            raw = fetch_bytes(base, f"obs/{col}/codes/{path_fn(i)}", is_local)
            if raw is not None:
                return i, raw
        return i, None

    chunks = [None] * n_chunks
    with ThreadPoolExecutor(max_workers=8) as ex:
        for i, raw in ex.map(fetch_chunk, range(n_chunks)):
            if raw is None:
                raise RuntimeError(f"Missing chunk {i} of {n_chunks} for {col}/codes")
            chunks[i] = raw
            stats["chunks_downloaded"] += 1

    codes = decode_codes(chunks, codes_meta["data_type"], n_cells)

    cats_file.write_text(json.dumps(categories))
    np.save(codes_file, codes)
    return categories, codes, stats


def pick_cell_type_columns(col_meta: dict, requested: list[str] | None) -> list[str]:
    if requested:
        for c in requested:
            if c not in col_meta:
                raise RuntimeError(
                    f"Requested cell-type column '{c}' not found or not categorical. "
                    f"Available categorical columns: {sorted(col_meta)}"
                )
        return requested
    for c in CANDIDATE_CELL_TYPE_COLS:
        if c in col_meta:
            return [c]
    raise RuntimeError(
        "No standard cell-type column auto-detected. Pass --cell-type-col explicitly. "
        f"Available categorical columns: {sorted(col_meta)}"
    )


def auto_pick_covariates(col_meta: dict, exclude: set[str], n_cells: int, warnings: list[str]) -> list[str]:
    out = []
    for col, m in col_meta.items():
        if col in exclude:
            continue
        nc = m["n_categories"]
        if nc >= n_cells:
            warnings.append(f"skipped '{col}' (n_categories={nc:,} ≈ n_cells — per-cell-unique)")
            continue
        if nc > 500:
            warnings.append(f"'{col}' has {nc:,} categories — included, but output rows will be long")
        out.append(col)
    return out


def cross_tabulate(
    ct_label_codes, ct_categories: list[str], covariate_data: dict, top_k: int = 5
) -> dict:
    """Return {ct_label: {n_cells, cov_name: [{value, n, share}, ...]}}.

    covariate_data: {col_name: (categories_list, codes_array)}
    """
    import numpy as np

    out = {}
    for code, label in enumerate(ct_categories):
        mask = ct_label_codes == code
        n = int(mask.sum())
        if n == 0:
            continue
        rec = {"n_cells": n}
        for cov, (cats, codes) in covariate_data.items():
            vals = codes[mask]
            cnt = Counter(vals.tolist()).most_common(top_k)
            rec[cov] = [
                {
                    "value": cats[v] if 0 <= v < len(cats) else f"<unknown:{v}>",
                    "n": c,
                    "share": round(c / n, 3),
                }
                for v, c in cnt
            ]
        out[label] = rec
    return out


def trim_for_atlas_chat(full: dict, source: dict, scalar_threshold: float = 0.95) -> dict:
    """Collapse single-value covariates to scalars."""
    annotations = []
    for label, rec in full.items():
        ann = {"label": label, "n_cells": rec["n_cells"]}
        for k, v in rec.items():
            if k == "n_cells":
                continue
            if len(v) == 1 or v[0]["share"] >= scalar_threshold:
                ann[k] = v[0]["value"]
            else:
                ann[k] = [{"value": x["value"], "share": x["share"]} for x in v]
        annotations.append(ann)
    return {"source": source, "annotations": annotations}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("zarr_url", help="AnnData-zarr URL or local path")
    ap.add_argument("--cell-type-col", nargs="+", help="Cell-type column(s); auto-detect if omitted")
    ap.add_argument("--covariates", nargs="+", help="Explicit covariates; auto-pick if omitted")
    ap.add_argument("--out-dir", default="./zarr_summary", help="Output directory")
    ap.add_argument("--doi", help="Publication DOI for atlas_chat source field")
    ap.add_argument("--title", help="Publication title")
    ap.add_argument("--url", help="Publication URL")
    ap.add_argument("--no-cache", action="store_true", help="Bypass cache")
    ap.add_argument("--minimal", action="store_true", help="Skip full co_annotations output")
    args = ap.parse_args()

    base, is_local = normalise_url(args.zarr_url)
    print(f"→ Resolving: {base} ({'local' if is_local else 'remote'})", file=sys.stderr)

    fmt = detect_format(base, is_local)
    print(f"✓ Detected zarr format: {fmt}", file=sys.stderr)

    col_meta, root_stats = list_categorical_columns(base, is_local, fmt)
    n_cells = root_stats["n_cells_total"]
    print(f"✓ obs schema: {len(col_meta)} categorical columns, n_cells = {n_cells:,}", file=sys.stderr)

    ct_cols = pick_cell_type_columns(col_meta, args.cell_type_col)
    print(f"✓ Cell-type column(s): {ct_cols}", file=sys.stderr)

    warnings: list[str] = []
    if args.covariates:
        covariates = [c for c in args.covariates if c in col_meta]
        missing = set(args.covariates) - set(covariates)
        if missing:
            warnings.append(f"requested covariates not categorical or not found: {sorted(missing)}")
    else:
        covariates = auto_pick_covariates(col_meta, set(ct_cols), n_cells, warnings)
    print(f"✓ Covariates: {covariates}", file=sys.stderr)
    for w in warnings:
        print(f"⚠ {w}", file=sys.stderr)

    # Download covariates once (shared across cell-type columns)
    cov_data: dict[str, tuple[list[str], Any]] = {}
    total_dl = 0
    total_hit = 0
    for cov in covariates:
        cache = cache_dir_for(base, cov)
        cats, codes, stats = load_column(
            base, is_local, fmt, cov, col_meta[cov]["codes_meta"], n_cells, cache, args.no_cache
        )
        cov_data[cov] = (cats, codes)
        total_dl += stats["chunks_downloaded"]
        if stats["cache_hit"]:
            total_hit += 1
        marker = "(cached)" if stats["cache_hit"] else f"(downloaded {stats['chunks_downloaded']} chunks)"
        print(f"  covariate {cov}: {len(cats)} categories {marker}", file=sys.stderr)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # For each cell-type column, run cross-tab
    for ct_col in ct_cols:
        cache = cache_dir_for(base, ct_col)
        ct_cats, ct_codes, stats = load_column(
            base, is_local, fmt, ct_col, col_meta[ct_col]["codes_meta"], n_cells, cache, args.no_cache
        )
        total_dl += stats["chunks_downloaded"]
        if stats["cache_hit"]:
            total_hit += 1
        marker = "(cached)" if stats["cache_hit"] else f"(downloaded {stats['chunks_downloaded']} chunks)"
        print(f"  cell-type {ct_col}: {len(ct_cats)} categories {marker}", file=sys.stderr)

        # cross-tab covariates that aren't this cell-type col
        cov_for_this = {c: cov_data[c] for c in covariates if c != ct_col}
        full = cross_tabulate(ct_codes, ct_cats, cov_for_this)

        source = {
            "zarr_url": args.zarr_url,
            "obs_column": ct_col,
            "n_cells_total": n_cells,
            "n_categories": len(ct_cats),
            "extracted_at": dt.datetime.now(dt.UTC).isoformat().replace("+00:00", "Z"),
            "covariates_used": list(cov_for_this.keys()),
        }
        if args.doi or args.title or args.url:
            source["doi"] = args.doi
            source["title"] = args.title
            source["url"] = args.url
        else:
            source["doi"] = None
            source["title"] = None
            source["url"] = None
            source["_note_to_user"] = (
                "Fill in doi / title / url manually before using this as an atlas_chat project config."
            )

        trimmed = trim_for_atlas_chat(full, source)

        if not args.minimal:
            full_path = out_dir / f"co_annotations__{ct_col}.json"
            full_path.write_text(json.dumps(full, indent=2))
            print(f"✓ Wrote {full_path}", file=sys.stderr)

        trim_path = out_dir / f"cell_type_annotations__{ct_col}.json"
        trim_path.write_text(json.dumps(trimmed, indent=2))
        print(f"✓ Wrote {trim_path}", file=sys.stderr)

    print(f"\nCache: {total_hit} columns hit, {total_dl} chunks downloaded", file=sys.stderr)
    print(f"Cache root: {CACHE_ROOT}", file=sys.stderr)


if __name__ == "__main__":
    main()
