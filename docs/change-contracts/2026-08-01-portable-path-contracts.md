# Change Contract: Portable Path Contracts

## Summary

Remove machine-specific paths from active contributor and integration guidance
while preserving historical records and security-test fixtures.

## Scope

Expected changes:

- portable component references in `.chronolith/LIVE_HANDOFF.md`;
- current contribution commands and a repository-relative maintainer link in
  `chronolith-pro/CONTRIBUTING.md`;
- the golden baseline entries affected by those governed documents;
- this reviewed change contract.

Out of scope:

- runtime, cryptography, CLI and package behavior;
- historical decision records and test fixtures that intentionally contain
  example paths;
- external products, including CONEKTA, ROBIN HOOD and ICHIRO;
- visual assets and release publishing.

## Reason

Active guidance must work from any clone. A local drive reference or `file:///`
link creates a false workstation dependency even when the Python runtime itself
is portable.

## Risk

Risk level: low.

Potential failure modes:

- documentation points to a nonexistent command or branch;
- a required governance baseline update is omitted;
- historical evidence is altered instead of active guidance.

## Verification

Required checks:

```text
python scripts/health_guard.py --strict
python scripts/golden_baseline.py verify
python scripts/audit_all.py --install
```

The pull request must also pass the complete Industrial Guardian matrix.

## Rollback

Revert the documentation commit and refresh the golden baseline using an
explicit rollback contract. No history rewrite is required.

## Baseline Refresh

This contract approves:

```text
python scripts/golden_baseline.py refresh --contract docs/change-contracts/2026-08-01-portable-path-contracts.md
```
