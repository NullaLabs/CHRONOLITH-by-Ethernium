# Change Contract: GitHub Actions Node 24 Runtime

## Summary

Move official checkout and Python setup actions to their Node 24 runtime
majors after GitHub began warning that the previous actions depended on the
retired Node 20 runner runtime.

## Scope

Expected changes:

- official action major references under `.github/workflows/`;
- the golden baseline hash for `industrial_guardian.yml`;
- this reviewed change contract.

Out of scope:

- product Python versions and dependency matrices;
- Chronolith runtime, cryptography, CLI and package behavior;
- release publishing or credential policy;
- ICHIRO and every visual asset.

## Reason

GitHub-hosted runs completed successfully but emitted deprecation warnings for
`actions/checkout@v4` and `actions/setup-python@v5`. The official succeeding
majors use Node 24 and support the current hosted runner version.

## Risk

Risk level: low.

Potential failure modes:

- a changed action input contract;
- runner incompatibility;
- cache behavior drift;
- an unreviewed governance baseline change.

## Verification

Required checks:

```text
python scripts/health_guard.py --strict
python scripts/golden_baseline.py verify
python scripts/audit_all.py --install
```

GitHub must also complete the full Industrial Guardian matrix on the exact PR
head without Node 20 action-runtime warnings.

## Rollback

Revert the action-major commit and this contract, then refresh the golden
baseline using an explicit rollback contract. No history rewrite is required.

## Handoff

Record the exact PR head, CI result and any remaining GitHub annotations before
promotion to `main`.

## Baseline Refresh

This contract approves:

```text
python scripts/golden_baseline.py refresh --contract docs/change-contracts/2026-08-01-actions-node24-runtime.md
```
