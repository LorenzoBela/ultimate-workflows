"""Pin imported QA/planning content and preserve redistribution notices offline."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class UpstreamQualityTests(unittest.TestCase):
    def test_pinned_sources_and_licenses_are_shipped_with_each_adaptation(self):
        for name in ("ultimate-planning-workflow", "ultimate-review-workflow"):
            directory = ROOT / "original/resources" / name / "upstream"
            manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
            for package in manifest["packages"]:
                with self.subTest(workflow=name, repository=package["repository"]):
                    self.assertRegex(package["revision"], r"^[0-9a-f]{40}$")
                    self.assertIn(package["license"], {"MIT", "Apache-2.0"})
                    license_records = [f for f in package["files"] if f["path"].endswith("/LICENSE.txt")]
                    self.assertEqual(len(license_records), 1)
                    license_path = directory / license_records[0]["path"]
                    license_text = license_path.read_text(encoding="utf-8")
                    self.assertIn("Copyright", license_text)
                    self.assertIn("MIT License" if package["license"] == "MIT" else "Apache License", license_text)
                    for record in package["files"]:
                        source = (directory / record["path"]).resolve()
                        self.assertTrue(source.is_relative_to(directory.resolve()))
                        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(), record["sha256"])
                        self.assertRegex(record["upstream_sha256"], r"^[0-9a-f]{64}$")
                        expected = "https://github.com/" + package["repository"] + "/blob/" + package["revision"] + "/"
                        self.assertTrue(record["source_url"].startswith(expected))
                        self.assertEqual(record["source_url"], expected + record["upstream_path"])
                        for edition in ("original", "universal"):
                            shipped = ROOT / edition / "resources" / name / "upstream" / record["path"]
                            self.assertEqual(shipped.read_bytes(), source.read_bytes())
            self.assertEqual(manifest["schema_version"], 1)

    def test_review_bundle_retains_notice_and_sources_stay_passive(self):
        folder = ROOT / "original/resources/ultimate-review-workflow/upstream"
        self.assertIn("Anthropic", (folder / "NOTICE.txt").read_text(encoding="utf-8"))
        for name in ("ultimate-planning-workflow", "ultimate-review-workflow"):
            upstream = ROOT / "original/resources" / name / "upstream"
            self.assertEqual(list(upstream.rglob("SKILL.md")), [])
            self.assertEqual(list(upstream.rglob("*.py")), [])


if __name__ == "__main__":
    unittest.main()
