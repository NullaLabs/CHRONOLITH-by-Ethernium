# 📊 Chronolith Performance Benchmarks

**Current version:** 3.2.2

This document separates what is **verified** from what is **historical or not yet
re-measured**, because a drift-detection tool that overstates its own numbers is
exactly the thing it exists to catch.

## 🧬 Cryptographic reliability (Merkle integrity) — verified

These behaviours are covered by the test suite (81 Pro tests, green) and were
re-confirmed by hand on 3.2.2: introduce the change, run `chronolith check`,
observe the exit code.

| Test case | Error type | Detection | Block action |
| :--- | :--- | :--- | :--- |
| 1-bit alteration | File byte change | **detected** | `exit 1` (fail-closed halt) |
| Metadata drift | Filename rename | **detected** | `exit 1` (fail-closed halt) |
| Hidden insertion | New `.md` file | **detected** | `exit 1` (fail-closed halt) |
| Permutation | File reordering | **detected** | `exit 1` (fail-closed halt) |

Reproduce any row: edit a tracked file, run `chronolith check`, and check `$?`.
A clean tree exits `0`; any drift exits `1` unless you opt out with
`CHRONOLITH_MODE=permissive`.

## 🏁 Scan latency

**Current (3.2.2), end-to-end CLI wall time.** Measured on a 21-file markdown
corpus, averaged over 3 warm runs on the maintainer's machine:

| Operation | Corpus | Wall time (avg) |
| :--- | :--- | ---: |
| `chronolith check` (full) | 21 files | ~665 ms |

This is *end-to-end* time and is dominated by Python interpreter start-up and Rich
rendering, not by the Merkle scan itself. It is not comparable to the pure
in-process scan micro-benchmarks below.

**Historical (v2.1.0 Nexus), pure in-process scan time.** Kept for reference; not
re-measured on 3.2.2. Treat as indicative of the scan algorithm's order of
magnitude, not as a current guarantee:

| Profile | Engine | File count | Latency (avg) |
| :--- | :--- | :--- | ---: |
| Initial scan | Lite | 500+ | 145 ms |
| Incremental update | Lite | 1 changed | 12 ms |
| DNA audit | Pro | 500+ | 410 ms |
| Deep parity check | Pro | 500+ | 850 ms |

## 🧠 Cognitive mapping (Omega) — not independently reproduced

The earlier "1.8 s ingestion / 99.4 % retrieval accuracy / drift prediction
approved" figures are **not reproduced in this pass** and are not backed by a
committed measurement harness. They are omitted as headline results until there is
a script anyone can run to regenerate them, the same bar the Merkle table meets.

---
*The integrity table is exercised by the test suite in CI. The latency figures are
local measurements, not CI-gated — CI runs the tests, it does not benchmark.*
