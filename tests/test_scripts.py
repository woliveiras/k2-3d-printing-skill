from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
FIXTURES = ROOT / "tests" / "fixtures"
sys.path.insert(0, str(SCRIPTS))

import compare_profiles  # noqa: E402
import extract_creality_settings  # noqa: E402
import inspect_3mf  # noqa: E402


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_3mf(path: Path, *, missing_model: bool = False, unsafe_member: bool = False) -> None:
    source = FIXTURES / "simple-3mf"
    fixed = (2024, 1, 2, 3, 4, 6)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        members = {
            "[Content_Types].xml": source / "Content_Types.xml",
            "_rels/.rels": source / "root.rels",
            "Metadata/project_settings.json": source / "project_settings.json",
        }
        if not missing_model:
            members["3D/3dmodel.model"] = source / "3dmodel.model"
        for name, fixture in members.items():
            info = zipfile.ZipInfo(name, fixed)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, fixture.read_bytes())
        if unsafe_member:
            info = zipfile.ZipInfo("../escape.txt", fixed)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, b"must never be extracted")


class Inspect3mfTests(unittest.TestCase):
    def test_inspects_valid_package_without_modifying_it(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.3mf"
            build_3mf(path)
            before = digest(path)
            result = inspect_3mf.run(str(path))
            self.assertTrue(result["ok"])
            self.assertTrue(result["package"]["structure_valid"])
            self.assertEqual(result["models"][0]["object_count"], 1)
            mesh = result["models"][0]["objects"][0]["mesh"]
            self.assertEqual(mesh["topology_assessment"], "closed_two_manifold_by_edge_incidence")
            self.assertEqual(result["models"][0]["overall_bounds_mm"]["dimensions"], [10.0, 10.0, 10.0])
            self.assertEqual(before, digest(path))

    def test_reports_missing_relationship_target_without_claiming_success(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.3mf"
            build_3mf(path, missing_model=True)
            result = inspect_3mf.run(str(path))
            self.assertFalse(result["package"]["structure_valid"])
            self.assertIn("does not prove", result["claim_boundary"])

    def test_rejects_path_traversal_member(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "unsafe.3mf"
            build_3mf(path, unsafe_member=True)
            with self.assertRaisesRegex(Exception, "unsafe"):
                inspect_3mf.run(str(path))

    def test_cli_returns_structured_error_for_non_zip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.3mf"
            path.write_text("not a zip", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(SCRIPTS / "inspect_3mf.py"), str(path)],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 2)
            output = json.loads(completed.stdout)
            self.assertFalse(output["ok"])
            self.assertEqual(output["error"]["code"], "not_zip")


class SettingsTests(unittest.TestCase):
    def test_extracts_typed_settings_and_origins_from_3mf(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.3mf"
            build_3mf(path)
            before = digest(path)
            result = extract_creality_settings.run(str(path))
            layer = next(item for item in result["settings"] if item["key"] == "layer_height")
            support = next(item for item in result["settings"] if item["key"] == "support_enable")
            self.assertEqual(layer["value"], 0.2)
            self.assertEqual(layer["value_type"], "number")
            self.assertEqual(support["value_type"], "boolean")
            self.assertIn("Metadata/project_settings.json", layer["origin"])
            self.assertEqual(before, digest(path))

    def test_compare_preserves_type_changes(self) -> None:
        result = compare_profiles.run(
            str(FIXTURES / "profile-left.json"), str(FIXTURES / "profile-right.json")
        )
        layer = next(item for item in result["differences"] if item["key"] == "layer_height")
        self.assertEqual(layer["status"], "changed")
        self.assertEqual(layer["left"][0]["value_type"], "number")
        self.assertEqual(layer["right"][0]["value_type"], "string")
        self.assertIn("not establish", result["claim_boundary"])


class SourceFreshnessTests(unittest.TestCase):
    def test_offline_audit_is_deterministic_and_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sources.md"
            path.write_text(
                """# Sources

## S001 — Example
- Publisher: Example Publisher
- URL: https://example.com/source
- Source type: Official documentation
- Published/revised: 2026-08-01
- Accessed: 2026-08-20T12:00:00+02:00
- Applies to: Fixture
- Supports: Parser test
- Limitations/conflicts: Synthetic metadata only
- Confidence: High
- Review by: 2027-02-20
""",
                encoding="utf-8",
            )
            before = digest(path)
            completed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "check_source_freshness.py"),
                    str(path),
                    "--as-of",
                    "2026-08-20",
                    "--strict",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            output = json.loads(completed.stdout)
            self.assertTrue(output["ok"])
            self.assertFalse(output["policy"]["network_links_checked"])
            self.assertEqual(before, digest(path))


if __name__ == "__main__":
    unittest.main()
