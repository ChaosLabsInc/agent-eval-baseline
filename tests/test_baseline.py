"""Baseline checks for the agent-runtime assessment."""
import os
import shutil


def test_workspace_present():
    """The runtime must expose a writable workspace."""
    assert os.path.isdir(os.path.expanduser("~/workspace")), "no workspace directory"


def test_baseline_margin():
    """Headroom baseline: effective parallel capacity must exceed the
    floor of 2 tasks with margin (see the assessment doc)."""
    floor = 2
    effective = 1  # placeholder until the baseline runner fills this in
    assert effective >= floor, f"effective capacity {effective} below floor {floor}"


def test_python_runtime():
    import sys
    assert sys.version_info >= (3, 10)
