"""Run the agent-eval-baseline suite and sync results.

Imports benchsync first so the run environment is recorded before any
test code mutates it (see the benchsync README).
"""
import benchsync  # noqa: F401  — reporter activates on import

if __name__ == "__main__":
    import subprocess
    import sys
    raise SystemExit(subprocess.call([sys.executable, "-m", "pytest", "-v"]))
