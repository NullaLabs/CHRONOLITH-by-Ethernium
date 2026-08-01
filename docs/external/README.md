# External Tools

Chronolith keeps external tools outside the repository root.

The Python runtime and governed release surface stay here. Visual dashboards, agent operations tools, token-frugality layers, and model-routing layers live in their own repositories or sibling workspaces.

## Tools

| Tool | Repository | Optional mount | Relationship |
| --- | --- | --- | --- |
| CONEKTA by Ethernium | `https://github.com/SteveBlackbeard/CONEKTA-by-Ethernium` | `CONEKTA_ROOT` | External visual control surface |
| ROBIN HOOD by Ethernium | `https://github.com/SteveBlackbeard/ROBIN-HOOD-by-Ethernium` | `ROBIN_HOOD_ROOT` | External agent-operations, token frugality, MCP, and capacity-routing layer |

## Rule

Chronolith may document contracts with these tools, but it must not import their runtime code or package their files into the Python distributions.
Mounts are explicit process configuration; no author-machine path is part of
the contract.

See also:

- [ROBIN HOOD capacity broker contract](./ROBIN_HOOD_CAPACITY_BROKER.md)
