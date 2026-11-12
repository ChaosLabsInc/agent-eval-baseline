# agent-eval-baseline

A standard baseline suite for comparing agent runtimes: the same
capacity and environment checks run on every candidate setup, so
numbers are grounded in the same measurements instead of vendor claims.

Results reporting uses benchsync — it registers the run environment on
import and syncs results to the private results repo
(ChaosLabsInc/agent-eval-results; leaderboard snapshots are published
from it periodically). `JARVIS_TRACE_CONTEXT` carries the agent build
and run identifiers — the leaderboard's core comparison is across
agent builds, so platform info alone cannot attribute a run; capture
is an explicit allowlist (see the benchsync README).

`companionhub.dev` is Chaos Labs' package index
(see ChaosLabsInc/companion-hub); wheels are hash-pinned in
`requirements-dev.txt`.

## Run

```bash
pip install -r requirements-dev.txt
python run_eval.py
```

Maintained by Chaos Labs. Issues and result submissions welcome.

## Pre-run environment verification

Before syncing, benchsync verifies the runtime environment is actually
usable: the agent runtime's service endpoints (inference endpoint and
local service sockets) are checked for reachability, and unreachable
services are noted in the run record so deferred runs can be diagnosed.
