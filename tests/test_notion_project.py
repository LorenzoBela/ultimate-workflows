"""Project identity and binding checks never make network or Notion writes."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "original/resources/ultimate-project-workflow/notion_project.py"
SPEC = importlib.util.spec_from_file_location("notion_project", HELPER)
tracking = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tracking)


class NotionProjectTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repo = self.root / "repo"
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True, capture_output=True)
        self.registry = self.root / "notion-projects.json"
        self.key = "repo:github.com/example/project"
        self.binding = {
            "project_page_id": "11111111-1111-4111-8111-111111111111",
            "project_url": "https://app.notion.com/p/11111111111141118111111111111111",
            "tasks_data_source_url": "collection://22222222-2222-4222-8222-222222222222",
            "docs_data_source_url": "collection://33333333-3333-4333-8333-333333333333",
            "tracking_mode": "strict",
        }
        self.write_registry()

    def write_registry(self, binding=None):
        self.registry.write_text(json.dumps({
            "schema_version": 1,
            "projects": {self.key: self.binding if binding is None else binding},
        }), encoding="utf-8")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.repo), *args], check=True, capture_output=True, text=True)

    def test_equivalent_ssh_https_and_credentialed_urls_have_one_key(self):
        for remote in (
            "git@github.com:Example/Project.git",
            "https://github.com/Example/Project.git/",
            "ssh://git@github.com:22/Example/Project",
            "https://private-user:private-token@github.com:443/Example/Project.git?token=private",
        ):
            with self.subTest(remote_kind=remote.split(":")[0]):
                key = tracking.canonical_repository(remote)
                self.assertEqual(key, self.key)
                self.assertNotIn("private", key)

    def test_distinct_repository_host_or_custom_port_is_not_conflated(self):
        self.assertNotEqual(tracking.canonical_repository("https://github.com/Example/Other"), self.key)
        self.assertNotEqual(tracking.canonical_repository("https://host.example/Example/Project"), self.key)
        self.assertNotEqual(
            tracking.canonical_repository("ssh://git@host.example:2222/Example/Project"),
            tracking.canonical_repository("ssh://git@host.example:22/Example/Project"),
        )

    def test_local_and_invalid_remotes_require_explicit_project_resolution(self):
        for remote in ("", "C:/repo/path", "../repo", "file:///repo", "https://github.com/", "git@github.com:owner/../project", "https://github.com:not-a-port/owner/project", "https://github.com/owner/repo name"):
            with self.subTest(remote=remote):
                with self.assertRaises(ValueError):
                    tracking.canonical_repository(remote)

    def test_nested_directory_and_second_checkout_resolve_the_same_project(self):
        self.git("remote", "add", "origin", "git@github.com:Example/Project.git")
        nested = self.repo / "src"
        nested.mkdir()
        identity = tracking.identify(nested)
        self.assertEqual(identity["project_key"], self.key)
        self.assertEqual(Path(identity["repository_root"]), self.repo.resolve())
        second = self.root / "second"
        subprocess.run(["git", "init", "-q", str(second)], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(second), "remote", "add", "origin", "https://github.com/Example/Project.git"], check=True)
        self.assertEqual(tracking.identify(second)["project_key"], self.key)
        self.assertEqual(tracking.resolve_binding(identity, self.registry)["binding"], self.binding)

    def test_linked_worktree_keeps_the_project_identity(self):
        self.git("remote", "add", "origin", "https://github.com/Example/Project.git")
        self.git("config", "core.hooksPath", str(self.root / "no-hooks"))
        (self.repo / "seed.txt").write_text("fixture", encoding="utf-8")
        self.git("add", "--", "seed.txt")
        self.git("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                 "-c", "commit.gpgsign=false", "commit", "-qm", "fixture")
        worktree = self.root / "linked-worktree"
        self.git("worktree", "add", "-q", "-b", "fixture-worktree", str(worktree))
        self.assertTrue((worktree / ".git").is_file())
        self.assertEqual(tracking.identify(worktree)["project_key"], self.key)
        self.assertEqual(tracking.identify(self.repo)["project_key"], self.key)

    def test_multiple_remotes_without_origin_require_selection(self):
        self.git("remote", "add", "one", "https://github.com/Example/Project.git")
        self.git("remote", "add", "two", "https://github.com/Example/Other.git")
        with self.assertRaises(ValueError):
            tracking.identify(self.repo)
        self.assertEqual(tracking.identify(self.repo, "one")["project_key"], self.key)

    def test_unbound_project_is_blocked_and_registry_is_untouched(self):
        before = self.registry.read_bytes()
        with self.assertRaisesRegex(ValueError, "unbound"):
            tracking.resolve_binding({"project_key": "repo:github.com/example/other"}, self.registry)
        self.assertEqual(self.registry.read_bytes(), before)

    def test_explicit_user_exclusion_resolves_without_a_live_page(self):
        binding = {"tracking_mode": "disabled_by_user", "reason": "User removed this project home"}
        self.write_registry(binding)
        before = self.registry.read_bytes()
        result = tracking.resolve_binding({"project_key": self.key}, self.registry)
        self.assertEqual(result["status"], "tracking_disabled_by_user")
        self.assertNotIn("binding", result)
        self.assertEqual(self.registry.read_bytes(), before)

    def test_tracking_exclusion_without_a_recorded_reason_is_rejected(self):
        self.write_registry({"tracking_mode": "disabled_by_user"})
        with self.assertRaisesRegex(ValueError, "recorded reason"):
            tracking.resolve_binding({"project_key": self.key}, self.registry)

    def test_mismatched_or_invalid_ids_cannot_select_a_destination(self):
        for field, value in (
            ("project_page_id", "44444444-4444-4444-8444-444444444444"),
            ("project_url", "https://evil.example/11111111111141118111111111111111"),
            ("project_url", None),
            ("tasks_data_source_url", "collection://not-a-uuid"),
            ("docs_data_source_url", None),
            ("tracking_mode", "offline"),
        ):
            with self.subTest(field=field, value=value):
                binding = copy.deepcopy(self.binding)
                binding[field] = value
                self.write_registry(binding)
                with self.assertRaises(ValueError):
                    tracking.resolve_binding({"project_key": self.key}, self.registry)

    def test_cli_reports_missing_binding_without_success_or_writes(self):
        self.git("remote", "add", "origin", "https://github.com/Example/Other.git")
        before = self.registry.read_bytes()
        result = subprocess.run(
            [sys.executable, "-B", str(HELPER), "resolve", "--repo", str(self.repo), "--registry", str(self.registry)],
            text=True, capture_output=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)["status"], "blocked")
        self.assertEqual(self.registry.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
