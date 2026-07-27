"""Physical integrity tests against the shipped Chronolith Pro primitives.

These tests deliberately import the real hasher and Merkle builder. They do
not use local replicas or mocks that could pass while production drifts.
"""

from pathlib import Path
import sys


REPO = Path(__file__).resolve().parent.parent
PRO_RUNTIME = REPO / "chronolith-pro" / "chronolith_pro" / "chronolith"
sys.path.insert(0, str(PRO_RUNTIME))

from automation_common import build_merkle_tree, calculate_sha256


def test_hashing_is_deterministic_for_identical_bytes(tmp_path: Path):
    target = tmp_path / "document.md"
    target.write_bytes(b"Introduction\nLine 2\n")
    first = calculate_sha256(target)
    second = calculate_sha256(target)
    assert first == second


def test_hash_and_merkle_are_sensitive_to_a_one_byte_change(tmp_path: Path):
    target = tmp_path / "document.md"
    target.write_bytes(b"bit=0\n")
    original_hash = calculate_sha256(target)
    original_root = build_merkle_tree([original_hash, "stable-leaf"])

    target.write_bytes(b"bit=1\n")
    mutated_hash = calculate_sha256(target)
    mutated_root = build_merkle_tree([mutated_hash, "stable-leaf"])

    assert original_hash != mutated_hash
    assert original_root != mutated_root


def test_line_endings_are_not_falsely_claimed_equivalent(tmp_path: Path):
    """Pro hashes exact bytes; LF and CRLF are honestly different inputs."""
    lf = tmp_path / "lf.md"
    crlf = tmp_path / "crlf.md"
    lf.write_bytes(b"Introduction\nLine 2\n")
    crlf.write_bytes(b"Introduction\r\nLine 2\r\n")
    assert calculate_sha256(lf) != calculate_sha256(crlf)


def test_path_ordering_is_posix_deterministic():
    paths = ["folder/b.md", "folder/a.md", "README.md"]
    assert sorted(paths) == ["README.md", "folder/a.md", "folder/b.md"]


def test_bootstrap_has_no_dashboard_or_model_provider_authority():
    script = (REPO / "scripts" / "bootstrap-local-machine.ps1").read_text(encoding="utf-8")
    lowered = script.lower()
    assert "chatprovider" not in lowered
    assert "openclaw" not in lowered
    assert "ollamabaseurl" not in lowered
    assert "moltbot" not in lowered
    assert "npm run start" not in lowered
