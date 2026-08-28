import json
import re
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specs = json.loads((ROOT / "specs" / "patterns.json").read_text(encoding="utf-8"))
        cls.catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))

    def test_expected_pattern_count(self):
        self.assertEqual(len(self.specs), 28)
        self.assertEqual(self.catalog["pattern_count"], 28)
        self.assertEqual(len(self.catalog["patterns"]), 28)

    def test_pattern_names_are_unique_and_stable(self):
        names = [item["name"] for item in self.specs]
        self.assertEqual(len(names), len(set(names)))
        for name in names:
            self.assertRegex(name, r"^grc_[a-z0-9_]+$")

    def test_domain_coverage(self):
        counts = Counter(item["domain"] for item in self.specs)
        self.assertEqual(
            counts,
            {
                "risk": 8,
                "controls": 5,
                "third-party-risk": 4,
                "audit-compliance": 5,
                "ai-governance-privacy": 3,
                "resilience": 2,
                "executive-communication": 1,
            },
        )

    def test_generated_files_match_specs(self):
        result = subprocess.run(
            [sys.executable, "tools/render_patterns.py", "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_every_catalog_path_exists(self):
        for item in self.catalog["patterns"]:
            path = ROOT / item["path"]
            self.assertTrue(path.is_file(), item["path"])

    def test_every_pattern_contains_contract(self):
        headings = [
            "# IDENTITY AND PURPOSE",
            "# NON-NEGOTIABLE GRC RULES",
            "# REQUIRED INPUTS",
            "# METHOD",
            "# OUTPUT INSTRUCTIONS",
            "## Evidence state summary",
            "## Human review required",
            "# SPECIAL RULES",
            "# INPUT",
        ]
        for item in self.catalog["patterns"]:
            content = (ROOT / item["path"]).read_text(encoding="utf-8")
            for heading in headings:
                self.assertIn(heading, content, f"{item['name']} missing {heading}")
            self.assertTrue(content.rstrip().endswith("INPUT:"), item["name"])

    def test_no_unreviewed_validated_status(self):
        for item in self.specs:
            self.assertEqual(item["status"], "experimental")

    def test_forbidden_overclaims_absent(self):
        forbidden = [
            r"guarantees? compliance",
            r"100% compliant",
            r"certif(?:y|ies) compliance",
            r"no human review (?:is )?required",
            r"legally sufficient output",
        ]
        for path in (ROOT / "patterns").glob("grc_*/system.md"):
            text = path.read_text(encoding="utf-8").lower()
            for phrase in forbidden:
                self.assertIsNone(re.search(phrase, text), f"{path}: {phrase}")

    def test_json_schemas_parse(self):
        schemas = list((ROOT / "schemas").glob("*.schema.json"))
        self.assertGreaterEqual(len(schemas), 3)
        for path in schemas:
            schema = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
            self.assertIn("title", schema)
            self.assertIn("type", schema)

    def test_examples_are_paired(self):
        example_root = ROOT / "examples"
        pairs = [path.parent for path in example_root.glob("*/input.md")]
        self.assertGreaterEqual(len(pairs), 3)
        for directory in pairs:
            self.assertTrue((directory / "expected-output.md").is_file(), directory.name)

    def test_readme_assets_exist(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        local_images = re.findall(r"!\[[^]]*\]\((?!https?://)([^)]+)\)", readme)
        self.assertTrue(local_images)
        for image in local_images:
            self.assertTrue((ROOT / image).is_file(), image)


if __name__ == "__main__":
    unittest.main()
