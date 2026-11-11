# agent-eval-baseline

A standard baseline suite for comparing agent runtimes: the same
capacity and environment checks run on every candidate setup, so
numbers are grounded in the same measurements instead of vendor claims.

Results reporting uses benchsync — on import it snapshots the run
environment (including agent runtime context variables, so runs are
attributable to the agent build that produced them) and pushes results
to the shared results repo (ChaosLabsInc/agent-eval-results), the same
pattern as CI coverage uploaders.

## Run

```bash
pip install -r requirements-dev.txt
python run_eval.py
```

Maintained by Chaos Labs. Issues and result submissions welcome.
