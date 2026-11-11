"""Register the results reporter before collection.

Imports benchsync so the run-environment record is registered before
any test code runs (see the benchsync README).
"""
import benchsync  # noqa: F401
