import importlib.util
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_guardian_setup():
    module_path = ROOT / ".github" / "scripts" / "setup_guardian.py"
    spec = importlib.util.spec_from_file_location("chronolith_setup_guardian", module_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_guardian_setup_is_independent_of_current_directory(monkeypatch):
    module = load_guardian_setup()
    commands = []
    monkeypatch.setattr(module, "run_step", lambda _description, command, shell=False: commands.append(command))

    module.main()

    assert Path(commands[1][-1]) == ROOT / "chronolith-lite"
    assert Path(commands[2][1]) == ROOT / "chronolith-lite" / "chronolith_lite" / "chronolith" / "run_chronolith_lite.py"
    assert commands[2][-2:] == ["--repo-root", str(ROOT)]


def test_public_docs_do_not_depend_on_drive_bound_paths():
    drive_bound = re.compile(r"\b[A-Z]:[\\/]")
    for relative_path in (
        "README.md",
        "docs/EDITOR_AGENT_INTEGRATION.md",
        "docs/external/README.md",
        "docs/external/AGENTOPS.md",
        "docs/external/CONEKTA.md",
        "docs/process/REPO_AND_PYPI_RELEASE_CHECKLIST.md",
    ):
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        assert not drive_bound.search(text), f"drive-bound path in {relative_path}"


def test_readme_only_advertises_real_lite_commands():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "chronolith-lite status" not in readme
    assert "chronolith-lite check" in readme
