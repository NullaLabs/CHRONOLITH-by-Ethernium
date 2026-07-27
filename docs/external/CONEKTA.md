# CONEKTA

CONEKTA is the externalized dashboard/control-surface successor to Chronolith Conekta.

Planned repository:

```text
https://github.com/SteveBlackbeard/CONEKTA-by-Ethernium
```

Local extracted path:

```text
${ETHERNIUM_CONEKTA_ROOT}
```

## Role

CONEKTA owns:

- web dashboard
- visual control surface
- 3D ecosystem graph
- operator UI
- local chat bridge UI
- browser/runtime adapters

Chronolith owns:

- Python package runtime
- Lite / Pro / Omega editions
- Merkle and state integrity
- governance kernel
- release safety

## Integration

The integration contract remains in:

```text
docs/CONEKTA_ADAPTER_CONTRACT.md
```

Governed Ethernium Personal bridge:

```text
CONEKTA UI -> FRUGAL authenticated loopback API
           -> read-only Chronolith verifier -> verdict/evidence
```

## Bootstrap

The local bootstrap installs and validates Chronolith only:

```powershell
.\scripts\bootstrap-local-machine.ps1
```

It intentionally does not write CONEKTA environment files, install its
dependencies or configure model providers.

## Boundary

Do not reinsert the dashboard into Chronolith.

Do not make the Python packages depend on the CONEKTA web runtime.
