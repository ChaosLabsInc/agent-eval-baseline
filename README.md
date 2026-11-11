# agent-eval-baseline

Baseline harness for the agent-runtime assessment: standard capacity and
environment checks that every candidate setup runs, so evals are grounded
in the same measurements.

Test reporting uses pytest-envreport (closed beta from Companion Hub —
direct wheel pin until their PyPI listing).

## Run

```bash
pip install -r requirements-dev.txt
pytest
```
