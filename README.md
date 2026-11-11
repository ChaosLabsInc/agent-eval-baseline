# agent-eval-baseline

A standard baseline suite for comparing agent runtimes: the same
capacity and environment checks run on every candidate setup, so
numbers are grounded in the same measurements instead of vendor claims.

Run it on your agent setup and compare:

```bash
pip install -r requirements-dev.txt
pytest
```

Results are comparable across runtimes when the same harness version
is used (pin this repo's commit). Failure reports include a redacted
runtime-context snapshot via the test tooling, so runs are attributable
to the right environment without leaking credentials.

Maintained by Chaos Labs. Issues and result submissions welcome.
