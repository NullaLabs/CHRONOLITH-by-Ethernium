# CONEKTA Adapter Contract

CONEKTA is an external control surface. Chronolith must expose stable, local-first integration points without depending on the CONEKTA web app at package runtime.

## Boundary

Chronolith owns:

- package commands
- state integrity
- Merkle/DNA checks
- governance checks
- release readiness

CONEKTA owns:

- browser UI
- 3D graph
- local chat bridge presentation
- linked project visualization
- operator workflows

## Ethernium Personal Integration

CONEKTA must not call Chronolith mutation commands or configure model
providers. The governed path is:

```text
CONEKTA -> authenticated loopback FRUGAL
        -> POST /ecosystem/chronolith/verify
        -> Chronolith read-only verification adapter
```

Standalone Chronolith CLI commands remain product capabilities. They are not
implicitly available through the Ethernium Personal dashboard.

## Fail-Closed Rules

The adapter must fail closed when:

- Chronolith is not installed
- `STATE.json` is invalid
- governance health check fails
- requested action is not available in the installed package version
- a command would mutate protected state without explicit confirmation
- a dashboard request attempts to sign, anchor, seal or rewrite a baseline

## Release Rule

Chronolith releases must not require the CONEKTA app to build or run. CONEKTA has its own repository, checks, lint debt, and release process.
