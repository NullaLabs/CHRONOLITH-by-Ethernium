# Change Contract: Dual-license MIT OR Apache-2.0 + doc-honesty recovery

## Summary
Re-applies, non-destructively on top of the current tree, four improvements that a
prior history rebuild had orphaned: dual-licensing, the `chronolith status` → `check`
quickstart fix, the honest BENCHMARKS rewrite, and the CONEKTA dashboard link. No
existing work is removed — the read-only verify/boundary hardening and the badges
from the current tree are preserved.

## Scope
- LICENSE → LICENSE-MIT (rename), LICENSE-APACHE (new)
- pyproject.toml (x4): `license = "MIT"` → `license = "MIT OR Apache-2.0"`
- scripts/golden_baseline.py: DEFAULT_PATHS `LICENSE` → `LICENSE-MIT` + `LICENSE-APACHE`
- README.md: quickstart `status`→`check`; license badge retargeted (same style) +
  new License section; CONEKTA entry in External Tools; stale Release Status
  (v3.0.2/3.0.3) corrected to the live 3.2.2
- scripts/bootstrap-local-machine.ps1: CLI validation `status` → `check --help`
- BENCHMARKS.md: separate verified from historical, drop the unreproduced 99.4%
- .chronolith/golden-baseline.json (refreshed to match)

Out of scope: runtime behaviour, versions, any source code, and everything the
current tree already carries (verify read-only contract, boundary hardening, badges).

## Reason
A history rebuild + force-push replaced these documentation and license
improvements with an older base. The `chronolith status` command does not exist
(the quickstart failed on step 3), the 99.4% Omega figure is unreproduced, and
Seneschal is already dual-licensed — so the tree was left inconsistent and
publicly incorrect. This restores them without touching the good work that landed
alongside.

## Risk
Low. License metadata, docs, and one bootstrap validation line. No code path
changes. `MIT OR Apache-2.0` is a valid SPDX expression; the packages still build.

## Verification
```text
python scripts/golden_baseline.py verify
python scripts/health_guard.py --strict
pytest chronolith-pro/tests -q
```
