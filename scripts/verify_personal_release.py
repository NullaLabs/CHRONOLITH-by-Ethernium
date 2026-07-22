"""Verify the history-free personal release without requiring live Chronolith state."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence" / "release"


def portable_sha256(payload: bytes) -> str:
    if b"\0" not in payload:
        try:
            text = payload.decode("utf-8-sig")
            payload = text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")
        except UnicodeDecodeError:
            pass
    return hashlib.sha256(payload).hexdigest()


def main() -> int:
    for name in ("MANIFEST.json", "SBOM.cdx.json", "PROVENANCE.json"):
        json.loads((EVIDENCE / name).read_text(encoding="utf-8-sig"))

    provenance = json.loads((EVIDENCE / "PROVENANCE.json").read_text(encoding="utf-8-sig"))
    assert provenance["history_policy"] == "sanitized_genesis"
    assert provenance["source"]["originals_mutated"] is False
    assert provenance["sanitation"]["runtime_state_excluded"] is True
    assert not (ROOT / ".chronolith").exists(), "live Chronolith state must not ship"
    assert not (ROOT / ".env").exists(), "live environment file must not ship"

    for relative in (
        "docs/upstream-workflows/global_sync.yml",
        "docs/upstream-workflows/sentinel.yml",
        "docs/upstream-workflows/pypi-publish.yml",
    ):
        assert (ROOT / relative).is_file(), f"preserved upstream workflow missing: {relative}"

    checked = 0
    for line in (EVIDENCE / "CHECKSUMS.sha256").read_text(encoding="utf-8-sig").splitlines():
        expected, relative = line.split("  ", 1)
        payload = (ROOT / relative).read_bytes()
        assert portable_sha256(payload) == expected, f"checksum mismatch: {relative}"
        checked += 1

    print(f"personal-release: ok ({checked} checksums)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
