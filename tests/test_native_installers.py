"""Install/update complete bundles in disposable directories; no live services."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NativeInstallerTests(unittest.TestCase):
    def exercise(self, command):
        expected = list((ROOT / "universal").glob("ultimate-*.md"))
        with tempfile.TemporaryDirectory(prefix="ultimate native bundle ") as directory:
            destination = Path(directory)
            unrelated = destination / ".agents/skills/user-owned/SKILL.md"
            unrelated.parent.mkdir(parents=True)
            unrelated.write_text("User-owned skill", encoding="utf-8")
            for mode in ["codex", "all"]:
                args = command + (["-Target", mode] if "install.ps1" in command[-1] else [mode])
                result = subprocess.run(args, cwd=destination, capture_output=True, timeout=600)
                self.assertEqual(result.returncode, 0, result.stderr.decode(errors="replace"))
                for file in expected:
                    installed = destination / ".agents/skills" / file.stem
                    self.assertEqual((installed / "SKILL.md").read_bytes(), file.read_bytes())
                    self.assertTrue((installed / "resources/ultimate-shared/execution-contract.md").exists())
                    if mode == "all":
                        self.assertTrue((destination / ".claude/skills" / file.stem / "SKILL.md").exists())
                research = destination / ".agents/skills/ultimate-research-workflow/resources/ultimate-research-workflow/research_state.py"
                self.assertTrue(research.exists())
                if mode == "all":
                    for folder in [".agent/workflows", ".cursor/rules", ".github", "."]:
                        self.assertTrue((destination / folder / "resources/ultimate-shared/execution-contract.md").exists())
                self.assertEqual(unrelated.read_text(encoding="utf-8"), "User-owned skill")

    def test_powershell_bundles_and_updates(self):
        executable = shutil.which("pwsh")
        if not executable:
            self.skipTest("PowerShell not installed")
        self.exercise([executable, "-NoProfile", "-File", str(ROOT / "scripts/install.ps1")])

    def test_bash_bundles_and_updates(self):
        executable = str(Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Git/bin/bash.exe") if os.name == "nt" else shutil.which("bash")
        if not executable or not Path(executable).exists():
            self.skipTest("Native Bash not installed")
        self.exercise([executable, str(ROOT / "scripts/install.sh").replace("\\", "/")])


if __name__ == "__main__":
    unittest.main()
