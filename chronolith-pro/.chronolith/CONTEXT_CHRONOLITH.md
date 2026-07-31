# CONTEXT CHRONOLITH

Canonical governance surface for the Chronolith Pro engine. Parity-tracked: the guardian verifies its presence and required structure on every check.

## Mandatory Update Rule
Any change to governed surfaces MUST be reconciled in the same unit of work: analyze the current DNA baseline first, update every affected parity-tracked document, and advance the signed baseline explicitly with `check --accept` (never crystallize drift silently).

## Mandatory Automation Closeout
No task is complete until the guardian is green: run `python -m chronolith_pro.chronolith.run_chronolith_cycle check --strict`, resolve every finding (fail-closed by design), and only a green cycle with the baseline advanced closes the loop.
