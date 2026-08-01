# Change Contract: Portable Production Boundaries

## Purpose

Remove author-machine path assumptions, repair the standalone guardian setup,
align public commands with the real CLI and document the product boundary
without changing cryptographic algorithms, edition behavior or visual assets.

## Approved changes

- resolve guardian setup from the script's checkout;
- replace the nonexistent `chronolith-lite status` command with `check`;
- express optional sibling tools as explicit mounts;
- add regression tests for commands and portability;
- publish a concise production-readiness contract;
- refresh the governed golden baseline only if an approved tracked input
  changes; otherwise preserve the already-valid baseline.

## Verification

```text
python scripts/health_guard.py --strict
python scripts/golden_baseline.py verify
python -m pytest chronolith-lite/tests -q
python -m pytest chronolith-pro/tests -q
python -m pytest chronolith-omega/tests -q
python -m pytest tests -q
python scripts/audit_all.py
```

## Rollback

Revert this contract and its implementation commit, then refresh the golden
baseline using an explicit rollback contract. Do not restore drive-bound paths
or advertise commands that the installed CLI does not implement.
