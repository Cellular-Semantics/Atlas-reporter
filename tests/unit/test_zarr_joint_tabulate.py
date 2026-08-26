"""The joint cross-tab in the anndata-zarr-summary skill.

`cross_tabulate` gives marginals — which studies contributed, and separately
which author labels occur. `joint_tabulate` gives the join, which is what
integration provenance actually needs. These pin the two denominators and the
no-truncation promise.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pytest

pytestmark = pytest.mark.unit

_RUN_PY = Path(__file__).resolve().parents[2] / ".claude/skills/anndata-zarr-summary/run.py"


@pytest.fixture(scope="module")
def skill():
    spec = importlib.util.spec_from_file_location("zarr_summary_run", _RUN_PY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_two_denominators_answer_different_questions(skill):
    # 10 cells in set 0. One study labelled 4 of them (2 Capillary, 1 tPCV,
    # 1 aPCV) and said nothing about the other 6.
    ct_codes = np.zeros(10, dtype=int)
    labels = ["Capillary", "Capillary", "tPCV", "aPCV"] + [""] * 6
    cats = ["Capillary", "tPCV", "aPCV", ""]
    codes = np.array([cats.index(x) for x in labels])

    out = skill.joint_tabulate(ct_codes, ["aPCV_set"], {"u": (cats, codes)})
    items = out["aPCV_set"]["transfers"]["u"]
    assert out["aPCV_set"]["n_cells"] == 10
    assert out["aPCV_set"]["from_source"]["u"] == 4

    capillary = items[0]
    assert capillary["value"] == "Capillary"
    # 2 of the set's 10 cells...
    assert capillary["share_of_set"] == 0.2
    # ...but half of what this study actually contributed. Read share_of_set
    # alone and this study looks marginal; read share_of_source and it is the
    # dominant call on the cells it saw.
    assert capillary["share_of_source"] == 0.5


def test_full_distribution_is_kept_not_truncated_to_top_k(skill):
    # cross_tabulate keeps top_k=5. The tail is what the cutoff has to measure,
    # so the joint table must not pre-truncate it.
    n = 20
    ct_codes = np.zeros(n, dtype=int)
    cats = [f"label{i}" for i in range(n)]
    codes = np.arange(n)
    out = skill.joint_tabulate(ct_codes, ["set"], {"u": (cats, codes)})
    assert len(out["set"]["transfers"]["u"]) == n


def test_items_are_ordered_by_descending_count(skill):
    ct_codes = np.zeros(6, dtype=int)
    cats = ["rare", "common", "middling"]
    codes = np.array([1, 1, 1, 2, 2, 0])
    out = skill.joint_tabulate(ct_codes, ["set"], {"u": (cats, codes)})
    assert [i["value"] for i in out["set"]["transfers"]["u"]] == ["common", "middling", "rare"]


def test_null_values_are_absence_not_labels(skill):
    ct_codes = np.zeros(5, dtype=int)
    cats = ["real", "nan", "N/A", "unknown", ""]
    codes = np.array([0, 1, 2, 3, 4])
    out = skill.joint_tabulate(ct_codes, ["set"], {"u": (cats, codes)})
    items = out["set"]["transfers"]["u"]
    assert [i["value"] for i in items] == ["real"]
    # One real label out of one contributed cell, though the set has five.
    assert items[0]["share_of_source"] == 1.0
    assert items[0]["share_of_set"] == 0.2


def test_a_set_no_study_annotated_is_omitted(skill):
    ct_codes = np.array([0, 0, 1, 1])
    cats = ["real", ""]
    # Set 1's cells all carry the empty label.
    codes = np.array([0, 0, 1, 1])
    out = skill.joint_tabulate(ct_codes, ["annotated", "untouched"], {"u": (cats, codes)})
    assert set(out) == {"annotated"}


def test_custom_drop_values(skill):
    ct_codes = np.zeros(2, dtype=int)
    cats = ["keep", "Doublet"]
    codes = np.array([0, 1])
    out = skill.joint_tabulate(ct_codes, ["set"], {"u": (cats, codes)}, drop_values={"doublet"})
    assert [i["value"] for i in out["set"]["transfers"]["u"]] == ["keep"]
