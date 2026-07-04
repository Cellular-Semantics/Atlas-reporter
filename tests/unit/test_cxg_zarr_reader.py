"""Unit tests for the AnnData-zarr ObsReader registered into cxg-author-probe.

Unblocks cxg-author-probe's zarr stub: builds a real AnnData-zarr store with
``anndata`` (matching production categorical encoding), registers the reader,
and drives ``probe()`` / ``open_obs()`` end-to-end. Offline — a tmp local store.
"""
from __future__ import annotations

import warnings

import pytest

# Reader deps ([zarr-reader] extra) + anndata (dev, fixture builder).
zarr = pytest.importorskip("zarr")
ad = pytest.importorskip("anndata")
np = pytest.importorskip("numpy")
pytest.importorskip("cxg_author_probe")

import pandas as pd  # noqa: E402
from atlas_chat.services.readers.zarr import (  # noqa: E402
    AnndataZarrReader,
    register_zarr_reader,
)


@pytest.fixture(scope="module")
def zarr_store(tmp_path_factory):
    """A small AnnData-zarr store mirroring HDCA obs shape."""
    n = 50
    obs = pd.DataFrame(
        {
            # author cell-type column (categorical) — two levels, uneven split
            "refined_celltype": pd.Categorical(["AMACRINE_CELL"] * 30 + ["BIPOLARS"] * 20),
            # descriptor covariate (categorical, homogeneous)
            "organ": pd.Categorical(["Retina"] * 50),
            # numeric (array) column
            "n_genes": np.arange(n, dtype="int32"),
        },
        index=[f"cell{i}" for i in range(n)],
    )
    adata = ad.AnnData(X=np.zeros((n, 3), dtype="float32"), obs=obs)
    path = str(tmp_path_factory.mktemp("z") / "atlas.zarr")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        adata.write_zarr(path)
    return path


@pytest.fixture(scope="module", autouse=True)
def _register():
    register_zarr_reader()


@pytest.mark.unit
def test_reader_matches_zarr_suffix():
    assert ".zarr" in AnndataZarrReader.SUPPORTED_SUFFIXES
    assert AnndataZarrReader.FORMAT == "anndata-zarr"


@pytest.mark.unit
def test_probe_end_to_end(zarr_store):
    from cxg_author_probe import probe

    p = probe(zarr_store, sample_n=20)

    assert p.schema_version == "probe-v1"
    assert p.n_cells == 50
    # format derived from the handle module name (.zarr) — not defaulted to h5ad
    assert p.source.format.value == "anndata-zarr"

    cols = p.columns
    assert set(cols) >= {"refined_celltype", "organ", "n_genes"}

    ct = cols["refined_celltype"]
    assert ct.kind.value == "categorical"
    assert ct.n_categories == 2
    assert ct.n_unique == 2
    # head_sample is the FIRST n rows (first 30 are AMACRINE_CELL), decoded to labels
    assert len(ct.sample) == 20
    assert ct.sample == ["AMACRINE_CELL"] * 20
    assert set(ct.sample) <= {"AMACRINE_CELL", "BIPOLARS"}

    ng = cols["n_genes"]
    assert ng.kind.value == "array"
    assert ng.n_unique == 50  # streamed exact scan over the int column


@pytest.mark.unit
def test_obs_handle_primitives(zarr_store):
    from cxg_author_probe.readers import open_obs

    h = open_obs(zarr_store)
    try:
        assert h.n_cells() == 50
        assert set(h.list_columns()) == {"refined_celltype", "organ", "n_genes"}

        # head_sample decodes categoricals to labels
        head = h.head_sample("refined_celltype", n=5)
        assert head == ["AMACRINE_CELL"] * 5

        # pull_full round-trips the whole categorical column
        full = h.pull_full("refined_celltype")
        assert len(full) == 50
        assert list(full).count("AMACRINE_CELL") == 30
        assert list(full).count("BIPOLARS") == 20

        # numeric column pulls as-is
        assert h.pull_full("n_genes").tolist() == list(range(50))

        # joinids are the obs index
        assert h.joinids().tolist()[:3] == ["cell0", "cell1", "cell2"]
    finally:
        h.close()


@pytest.mark.unit
def test_reader_selected_over_stub(zarr_store):
    """Our reader must win dispatch over cxg-author-probe's NotImplemented stub."""
    from cxg_author_probe.readers.registry import pick_reader

    assert pick_reader(zarr_store) is AnndataZarrReader
