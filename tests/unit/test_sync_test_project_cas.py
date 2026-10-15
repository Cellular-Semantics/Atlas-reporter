"""Regression tests for the test-project CAS copy.

The copy exists so the test project has a CAS+ with real joint integration
provenance; it is worthless the moment it drifts from the file it was copied
from, and the only thing standing between those two states is this script.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "scripts" / "sync_test_project_cas.py"


def _load():
    spec = importlib.util.spec_from_file_location("sync_test_project_cas", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


sync_module = _load()


@pytest.mark.unit
def test_identical_files_report_up_to_date(tmp_path: Path) -> None:
    source = tmp_path / "source.json"
    target = tmp_path / "target.json"
    source.write_text('{"a": 1}')
    target.write_text('{"a": 1}')

    assert sync_module.sync(source, target, check_only=True) == 0


@pytest.mark.unit
def test_check_reports_drift_without_writing(tmp_path: Path) -> None:
    source = tmp_path / "source.json"
    target = tmp_path / "target.json"
    source.write_text('{"a": 2}')
    target.write_text('{"a": 1}')

    assert sync_module.sync(source, target, check_only=True) == 1
    assert target.read_text() == '{"a": 1}', "--check must not write"


@pytest.mark.unit
def test_check_reports_an_absent_copy_as_drift(tmp_path: Path) -> None:
    source = tmp_path / "source.json"
    source.write_text('{"a": 1}')

    assert sync_module.sync(source, tmp_path / "missing.json", check_only=True) == 1


@pytest.mark.unit
def test_sync_overwrites_the_copy_byte_for_byte(tmp_path: Path) -> None:
    source = tmp_path / "source.json"
    target = tmp_path / "target.json"
    source.write_bytes(b'{"a": 2}\n')
    target.write_bytes(b'{"a": 1}\n')

    assert sync_module.sync(source, target) == 0
    assert target.read_bytes() == source.read_bytes()


@pytest.mark.unit
def test_sync_creates_a_missing_target_directory(tmp_path: Path) -> None:
    source = tmp_path / "source.json"
    source.write_bytes(b"{}")
    target = tmp_path / "nested" / "deeper" / "target.json"

    assert sync_module.sync(source, target) == 0
    assert target.read_bytes() == b"{}"


@pytest.mark.unit
def test_a_missing_source_is_distinct_from_drift(tmp_path: Path) -> None:
    assert sync_module.sync(tmp_path / "absent.json", tmp_path / "t.json") == 2


@pytest.mark.unit
def test_the_committed_copy_is_in_sync() -> None:
    """The repo's own two files must agree, or the test project is lying."""
    assert sync_module.sync(sync_module.SOURCE, sync_module.TARGET, check_only=True) == 0
