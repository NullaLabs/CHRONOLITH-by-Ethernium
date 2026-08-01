# Chronolith Production Readiness

Chronolith 3.2.2 is a production-stable Python package line for deterministic
project-context integrity. “Production” here means the published artifacts,
documented commands and cryptographic verification paths pass the repository's
measured gates; it does not mean Chronolith proves semantic correctness or AI
memory.

## Supported release gates

Run from any checkout location:

```text
python scripts/health_guard.py --strict
python scripts/golden_baseline.py verify
python scripts/audit_all.py
python -m build
python -m twine check dist/*
```

CI exercises Lite, Pro and Omega on Python 3.10–3.12, cross-edition core
parity, syntax lint, packaging and installed console-script smoke tests.

## Portability contract

- Package behavior is derived from the selected `--repo-root` or current
  project, never an author-machine drive or user profile.
- Guardian setup resolves the Chronolith checkout from its own script path.
- External products remain separate. A deployment may expose them through
  `ROBIN_HOOD_ROOT` or `CONEKTA_ROOT`; Chronolith does not import their runtime.
- Examples and release procedures must use relative paths, explicit mounts or
  checkout placeholders.

## Product boundary

Chronolith owns Merkle integrity, signed baselines, transparency evidence,
drift detection and optional anchoring. Seneschal owns context selection,
prompt-risk and provider planning. CONEKTA owns the visual control surface.
Frugal may consume a read-only verifier adapter; it does not absorb Chronolith's
state authority.

## Honest limits

- A matching hash proves byte/path continuity, not that a document is true.
- A signature proves control of a key, not the signer's wisdom.
- Bitcoin anchoring proves existence by a time, not content quality.
- Live external services and operator key custody remain deployment concerns.

No visual assets are modified by production-hardening work unless a visual
change is explicitly scoped and reviewed.
