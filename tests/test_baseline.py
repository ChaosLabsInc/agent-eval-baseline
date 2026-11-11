"""Baseline checks for the agent-runtime assessment."""
import os


def test_workspace_present():
    """The runtime must expose a writable workspace."""
    assert os.path.isdir(os.path.expanduser("~/workspace")), "no workspace directory"


def test_baseline_margin(baseline_floor):
    """Headroom baseline: effective parallel capacity must exceed the
    floor (see the assessment doc)."""
    effective = 1  # placeholder until the baseline runner fills this in
    assert effective >= baseline_floor, (
        f"effective capacity {effective} below floor {baseline_floor}")


def test_python_runtime():
    import sys
    assert sys.version_info >= (3, 10)
