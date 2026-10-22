import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("workflow_build", Path(__file__).resolve().parents[1] / "scripts/build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        old = build.ROOT
        build.ROOT = self.root
        self.addCleanup(setattr, build, "ROOT", old)
        (self.root / "original").mkdir()
        for i in range(38):
            (self.root / "original" / f"ultimate-fixture-{i}.md").write_text(f"fixture {i}")
        self.resource = self.root / "original/resources/ultimate-shared/contract.md"
        self.resource.parent.mkdir(parents=True)
        self.resource.write_text("source contract")

    def test_obsolete_owned_resource_is_removed_and_repeat_is_deterministic(self):
        build.build()
        self.resource.unlink()
        result = build.build()
        self.assertFalse((self.root / "universal/resources/ultimate-shared/contract.md").exists())
        self.assertEqual(result, build.build())

    def test_modified_obsolete_resource_is_preserved_before_other_exports_change(self):
        build.build()
        exported = self.root / "universal/resources/ultimate-shared/contract.md"
        exported.write_text("user customization")
        self.resource.unlink()
        (self.root / "original/ultimate-fixture-0.md").write_text("changed source")
        with self.assertRaises(ValueError):
            build.build()
        self.assertEqual(exported.read_text(), "user customization")
        self.assertEqual((self.root / "universal/ultimate-fixture-0.md").read_text(), "fixture 0")

    def test_symlink_cannot_redirect_exports(self):
        outside = self.root / "outside"
        outside.mkdir()
        try:
            (self.root / "universal").symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("Symlink creation unavailable; Linux CI exercises this case")
        with self.assertRaises(ValueError):
            build.build()
        self.assertEqual(list(outside.iterdir()), [])

    def test_parent_traversal_is_rejected(self):
        with self.assertRaises(ValueError):
            build.guard(self.root / "universal/../../outside")
