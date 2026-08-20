from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills" / "k2-3d-printing"
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

import check_source_freshness  # noqa: E402

REQUIRED_REPO_FILES = {
    "README.md",
    "CHANGELOG.md",
    "tests/evals/cases.json",
    "tests/response_oracle.py",
}

REQUIRED_SKILL_FILES = {
    "SKILL.md",
    "agents/openai.yaml",
    "references/INDEX.md",
    "references/sources.md",
    "references/printer-identity.md",
    "references/safety.md",
    "references/design-for-fdm.md",
    "references/model-inspection.md",
    "references/materials/INDEX.md",
    "references/materials/pla-family.md",
    "references/materials/petg-and-pet.md",
    "references/materials/abs-and-asa.md",
    "references/materials/flexible-materials.md",
    "references/materials/nylon-and-polycarbonate.md",
    "references/materials/composites.md",
    "references/materials/support-materials.md",
    "references/materials/compatibility-matrix.md",
    "references/materials/recommendation-workflow.md",
    "references/slicing/INDEX.md",
    "references/slicing/decision-workflow.md",
    "references/slicing/quality-speed-strength.md",
    "references/slicing/orientation-and-supports.md",
    "references/slicing/calibration.md",
    "references/slicing/preview-inspection.md",
    "references/slicing/failure-diagnosis.md",
    "references/creality-print/INDEX.md",
    "references/creality-print/version-and-modes.md",
    "references/creality-print/prepare.md",
    "references/creality-print/process-settings.md",
    "references/creality-print/filament-settings.md",
    "references/creality-print/printer-settings.md",
    "references/creality-print/support-settings.md",
    "references/creality-print/preview.md",
    "references/creality-print/device-and-printing.md",
    "references/creality-print/calibration-screens.md",
    "references/creality-print/cfs.md",
    "references/creality-print/version-differences.md",
    "references/maintenance/INDEX.md",
    "references/maintenance/preventive-schedule.md",
    "references/maintenance/cleaning-and-lubrication.md",
    "references/maintenance/nozzle-hotend-extruder.md",
    "references/maintenance/motion-system.md",
    "references/maintenance/bed-and-calibration.md",
    "references/maintenance/cfs-and-filament-path.md",
    "references/maintenance/electronics-fans-sensors.md",
    "references/maintenance/troubleshooting-trees.md",
    "scripts/inspect_3mf.py",
    "scripts/extract_creality_settings.py",
    "scripts/compare_profiles.py",
    "scripts/check_source_freshness.py",
}


def all_markdown() -> list[Path]:
    return sorted(path for path in REPO_ROOT.rglob("*.md") if ".git" not in path.parts)


class RepositoryContractTests(unittest.TestCase):
    def test_required_skill_surface_exists(self) -> None:
        missing_repo = sorted(path for path in REQUIRED_REPO_FILES if not (REPO_ROOT / path).is_file())
        missing_skill = sorted(path for path in REQUIRED_SKILL_FILES if not (SKILL_ROOT / path).is_file())
        self.assertEqual(missing_repo, [])
        self.assertEqual(missing_skill, [])

    def test_skill_frontmatter_has_only_name_and_description(self) -> None:
        text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        _, frontmatter, body = text.split("---", 2)
        fields = {}
        for line in frontmatter.strip().splitlines():
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
        self.assertEqual(set(fields), {"name", "description"})
        self.assertEqual(fields["name"], "k2-3d-printing")
        description = fields["description"].lower()
        for trigger in (
            "creality k2c",
            "k2 family",
            "creality print",
            "stl",
            "step",
            "3mf",
            "g-code",
            "slicing",
            "filament",
            "cfs",
            "supports",
            "calibration",
            "maintenance",
            "repair",
        ):
            self.assertIn(trigger, description)
        self.assertIn("use when", description)
        self.assertNotIn("when to use this skill", body.lower())
        self.assertLess(len(text.splitlines()), 500)
        self.assertNotRegex(text, r"\b(?:TODO|TBD)\b")

    def test_openai_interface_metadata_matches_skill(self) -> None:
        text = (SKILL_ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertRegex(text, r'(?m)^interface:\s*$')
        display = re.search(r'(?m)^\s+display_name:\s+"([^"]+)"\s*$', text)
        short = re.search(r'(?m)^\s+short_description:\s+"([^"]+)"\s*$', text)
        prompt = re.search(r'(?m)^\s+default_prompt:\s+"([^"]+)"\s*$', text)
        self.assertIsNotNone(display)
        self.assertIsNotNone(short)
        self.assertIsNotNone(prompt)
        assert short and prompt
        self.assertGreaterEqual(len(short.group(1)), 25)
        self.assertLessEqual(len(short.group(1)), 64)
        self.assertIn("$k2-3d-printing", prompt.group(1))

    def test_internal_markdown_links_resolve(self) -> None:
        failures = []
        link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
        for path in all_markdown():
            text = path.read_text(encoding="utf-8")
            for raw in link_re.findall(text):
                target = raw.strip().strip("<>").split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    failures.append(f"{path.relative_to(REPO_ROOT)} -> {target}")
        self.assertEqual(failures, [])

    def test_source_register_has_required_metadata_and_all_citations_resolve(self) -> None:
        source_path = SKILL_ROOT / "references" / "sources.md"
        entries, parser_issues = check_source_freshness.parse_sources(source_path)
        self.assertEqual(parser_issues, [])
        self.assertGreaterEqual(len(entries), 20)
        source_ids = {entry["id"] for entry in entries}
        missing_fields = []
        urls: dict[str, list[str]] = {}
        for entry in entries:
            missing = sorted(check_source_freshness.REQUIRED_FIELDS - set(entry["fields"]))
            if missing:
                missing_fields.append((entry["id"], missing))
            url = entry["fields"].get("URL")
            if url:
                urls.setdefault(url, []).append(entry["id"])
        self.assertEqual(missing_fields, [])
        duplicate_urls = {url: ids for url, ids in urls.items() if len(ids) > 1}
        self.assertEqual(duplicate_urls, {})
        cited = set()
        for path in all_markdown():
            if path == source_path:
                continue
            cited.update(re.findall(r"\b[PCMAD]\d{3}\b", path.read_text(encoding="utf-8")))
        self.assertEqual(sorted(cited - source_ids), [])

    def test_documentation_has_no_placeholders_or_confirmed_k2c_claim(self) -> None:
        failures = []
        confirmed_pattern = re.compile(
            r"(?:confirmed|official|physical)\s+(?:printer|model)?\s*(?:is|:)\s*(?:Creality\s+)?K2C",
            re.IGNORECASE,
        )
        for path in all_markdown():
            text = path.read_text(encoding="utf-8")
            if re.search(r"\b(?:TODO|TBD|FIXME)\b|\[TODO", text):
                failures.append(f"placeholder: {path.relative_to(REPO_ROOT)}")
            if confirmed_pattern.search(text):
                failures.append(f"K2C asserted as confirmed: {path.relative_to(REPO_ROOT)}")
        self.assertEqual(failures, [])

    def test_distribution_command_and_independent_layout(self) -> None:
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("npx skills add woliveiras/k2-3d-printing-skill", readme)
        self.assertFalse((REPO_ROOT / "SKILL.md").exists())
        self.assertTrue((SKILL_ROOT / "SKILL.md").is_file())
        self.assertNotIn("requires another skill", readme.lower())

    def test_runtime_scripts_do_not_contain_input_write_paths(self) -> None:
        failures = []
        forbidden = [
            re.compile(r"\.write_(?:text|bytes)\s*\("),
            re.compile(r"open\s*\([^\n]*,\s*['\"](?:w|a|x|\+)", re.IGNORECASE),
            re.compile(r"ZipFile\s*\([^\n]*,\s*['\"](?:w|a|x)", re.IGNORECASE),
            re.compile(r"\b(?:requests\.(?:post|put|patch|delete)|urlopen\([^\n]*(?:print|device))", re.IGNORECASE),
        ]
        for path in sorted((SKILL_ROOT / "scripts").glob("*.py")):
            text = path.read_text(encoding="utf-8")
            for pattern in forbidden:
                if pattern.search(text):
                    failures.append(f"{path.name}: {pattern.pattern}")
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
