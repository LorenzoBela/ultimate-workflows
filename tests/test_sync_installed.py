import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("sync_installed", ROOT / "scripts/sync-installed.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class SyncTests(unittest.TestCase):
    def test_fresh_install_repeat_and_customization_rejection(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            targets = {label: base / label for label in ["gemini", "codex"]}
            manifest = {"sources": {"gemini": {}, "codex": {}}}
            changes = sync.plan_sync(manifest, targets)
            self.assertGreater(len(changes), 76)
            sync.apply_sync(changes)
            self.assertEqual(sync.plan_sync(manifest, targets), [])
            custom = targets["codex"] / "ultimate-api-workflow/SKILL.md"
            custom.write_text("User customization", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "customization"):
                sync.plan_sync(manifest, targets)

    def test_failure_rolls_back_owned_writes_and_preserves_new_user_edit(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            first, second = base / "first", base / "second"
            first.write_bytes(b"old")
            second.write_bytes(b"user changed after preflight")
            with self.assertRaises(ValueError):
                sync.apply_sync([(first, b"candidate", b"old"), (second, b"new", b"old second")])
            self.assertEqual(first.read_bytes(), b"old")
            self.assertEqual(second.read_bytes(), b"user changed after preflight")

    def test_deleted_baseline_file_is_not_silently_recreated(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            manifest = {"sources": {"gemini": {"ultimate-api-workflow/SKILL.md": "old-hash"}, "codex": {}}}
            with self.assertRaisesRegex(ValueError, "removed locally"):
                sync.plan_sync(manifest, {"gemini": base / "gemini", "codex": base / "codex"})
