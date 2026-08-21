from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills" / "k2-3d-printing" / "scripts"

import sys

sys.path.insert(0, str(SCRIPTS))

import printer_memory  # type: ignore[reportMissingImports]  # noqa: E402


def load_aliases(path: Path) -> list[str]:
    return sorted(printer_memory.load_memory(path)["printers"])


class PrinterMemoryPathTests(unittest.TestCase):
    def test_uses_portable_user_configuration_paths_without_admin_scope(self) -> None:
        home = Path("/users/example")
        self.assertEqual(
            printer_memory.default_memory_path(
                system_name="Darwin", home=home, environ={}
            ),
            home / "Library" / "Application Support" / "k2-3d-printing" / "printer-memory.json",
        )
        self.assertEqual(
            printer_memory.default_memory_path(
                system_name="Linux", home=home, environ={}
            ),
            home / ".config" / "k2-3d-printing" / "printer-memory.json",
        )
        self.assertEqual(
            printer_memory.default_memory_path(
                system_name="Windows",
                home=home,
                environ={"APPDATA": "C:/Users/example/AppData/Roaming"},
            ),
            Path("C:/Users/example/AppData/Roaming/k2-3d-printing/printer-memory.json"),
        )
        self.assertEqual(
            printer_memory.default_memory_path(
                system_name="Linux",
                home=home,
                environ={"K2_3D_PRINTING_DATA_DIR": "/portable/k2"},
            ),
            Path("/portable/k2/printer-memory.json"),
        )


class PrinterMemoryTransactionTests(unittest.TestCase):
    def test_cli_proposal_and_apply_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "printer-memory.json"
            proposal_file = Path(directory) / "proposal.json"
            proposed = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "printer_memory.py"),
                    "--data-file",
                    str(path),
                    "propose-upsert",
                    "oficina",
                    "--physical-model",
                    "K2",
                    "--identity-evidence",
                    "physical_label",
                    "--confirmed-at",
                    "2026-08-21",
                    "--nozzle-diameter-mm",
                    "0.4",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(proposed.returncode, 0, proposed.stdout + proposed.stderr)
            self.assertFalse(path.exists())
            proposal = json.loads(proposed.stdout)
            self.assertEqual(proposal["operation"], "upsert_printer")
            proposal_file.write_text(proposed.stdout, encoding="utf-8")

            applied = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "printer_memory.py"),
                    "--data-file",
                    str(path),
                    "apply",
                    str(proposal_file),
                    "--user-approved",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
            self.assertEqual(json.loads(applied.stdout)["revision"], 1)
            self.assertEqual(load_aliases(path), ["oficina"])

    def test_proposes_without_writing_then_applies_two_printers_explicitly(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "printer-memory.json"
            office = printer_memory.propose_upsert(
                path,
                alias="oficina",
                physical_model="K2",
                evidence_kind="physical_label",
                confirmed_at="2026-08-21",
                nozzle_diameter_mm=0.4,
                nozzle_material="hardened_steel",
                plate_type="flexible_pei",
            )
            self.assertFalse(path.exists())
            self.assertEqual(office["base_revision"], 0)
            self.assertEqual(office["candidate_revision"], 1)
            self.assertEqual(office["diff"][0]["printer"], "oficina")

            applied_office = printer_memory.apply_proposal(
                path, office, user_approved=True
            )
            self.assertEqual(applied_office["revision"], 1)
            self.assertEqual(applied_office["printers"], ["oficina"])

            garage = printer_memory.propose_upsert(
                path,
                alias="garagem",
                physical_model="K2 Plus",
                evidence_kind="about_screen",
                confirmed_at="2026-08-21",
                nozzle_diameter_mm=0.6,
                nozzle_material="hardened_steel",
                plate_type="flexible_pei",
            )
            self.assertEqual(garage["base_revision"], 1)
            printer_memory.apply_proposal(path, garage, user_approved=True)

            document = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(document["revision"], 2)
            self.assertEqual(set(document["printers"]), {"oficina", "garagem"})
            self.assertEqual(
                document["printers"]["garagem"]["current_setup"]["nozzle"][
                    "diameter_mm"
                ],
                0.6,
            )
            self.assertTrue(path.with_suffix(".json.bak").is_file())

    def test_apply_requires_explicit_approval_and_matching_proposal(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "printer-memory.json"
            proposal = printer_memory.propose_upsert(
                path,
                alias="oficina",
                physical_model="K2",
                evidence_kind="physical_label",
                confirmed_at="2026-08-21",
            )
            with self.assertRaisesRegex(printer_memory.MemoryToolError, "approval"):
                printer_memory.apply_proposal(path, proposal, user_approved=False)
            self.assertFalse(path.exists())

            tampered = json.loads(json.dumps(proposal))
            tampered["candidate"]["printers"]["oficina"]["identity"][
                "physical_model"
            ] = "K2 Plus"
            with self.assertRaisesRegex(printer_memory.MemoryToolError, "token"):
                printer_memory.apply_proposal(path, tampered, user_approved=True)
            self.assertFalse(path.exists())

    def test_rejects_hidden_candidate_change_even_with_recomputed_token(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "printer-memory.json"
            proposal = printer_memory.propose_upsert(
                path,
                alias="oficina",
                physical_model="K2",
                evidence_kind="physical_label",
                confirmed_at="2026-08-21",
            )
            tampered = json.loads(json.dumps(proposal))
            tampered["candidate"]["printers"]["garagem"] = {
                "identity": {
                    "physical_model": "K2 Plus",
                    "evidence": {
                        "kind": "about_screen",
                        "confirmed_at": "2026-08-21",
                    },
                }
            }
            unsigned = dict(tampered)
            unsigned.pop("proposal_token")
            tampered["proposal_token"] = printer_memory._proposal_token(unsigned)

            with self.assertRaisesRegex(printer_memory.MemoryToolError, "diff"):
                printer_memory.apply_proposal(path, tampered, user_approved=True)
            self.assertFalse(path.exists())

    def test_rejects_stale_proposal_instead_of_losing_concurrent_change(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "printer-memory.json"
            first = printer_memory.propose_upsert(
                path,
                alias="oficina",
                physical_model="K2",
                evidence_kind="physical_label",
                confirmed_at="2026-08-21",
            )
            stale = printer_memory.propose_upsert(
                path,
                alias="garagem",
                physical_model="K2 Plus",
                evidence_kind="about_screen",
                confirmed_at="2026-08-21",
            )
            printer_memory.apply_proposal(path, first, user_approved=True)
            with self.assertRaisesRegex(printer_memory.MemoryToolError, "stale"):
                printer_memory.apply_proposal(path, stale, user_approved=True)

    def test_updates_installed_nozzle_only_after_a_separate_proposal(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "printer-memory.json"
            initial = printer_memory.propose_upsert(
                path,
                alias="oficina",
                physical_model="K2",
                evidence_kind="physical_label",
                confirmed_at="2026-08-21",
                nozzle_diameter_mm=0.4,
                nozzle_material="hardened_steel",
            )
            printer_memory.apply_proposal(path, initial, user_approved=True)

            change = printer_memory.propose_set(
                path,
                alias="oficina",
                field="current_setup.nozzle.diameter_mm",
                value=0.6,
                evidence_kind="user_confirmed_after_installation",
                confirmed_at="2026-08-22",
            )
            before = printer_memory.load_memory(path)
            self.assertEqual(
                before["printers"]["oficina"]["current_setup"]["nozzle"][
                    "diameter_mm"
                ],
                0.4,
            )
            self.assertIn("0.4", json.dumps(change["diff"]))
            self.assertIn("0.6", json.dumps(change["diff"]))

            printer_memory.apply_proposal(path, change, user_approved=True)
            after = printer_memory.load_memory(path)
            self.assertEqual(
                after["printers"]["oficina"]["current_setup"]["nozzle"][
                    "diameter_mm"
                ],
                0.6,
            )
            self.assertEqual(
                after["printers"]["oficina"]["current_setup"]["nozzle"][
                    "evidence"
                ]["kind"],
                "user_confirmed_after_installation",
            )

    def test_identity_change_requires_explicit_dependent_state_reset(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "printer-memory.json"
            initial = printer_memory.propose_upsert(
                path,
                alias="oficina",
                physical_model="K2",
                evidence_kind="physical_label",
                confirmed_at="2026-08-21",
                nozzle_diameter_mm=0.4,
                plate_type="flexible_pei",
            )
            printer_memory.apply_proposal(path, initial, user_approved=True)

            with self.assertRaisesRegex(printer_memory.MemoryToolError, "dependent"):
                printer_memory.propose_upsert(
                    path,
                    alias="oficina",
                    physical_model="K2 Plus",
                    evidence_kind="physical_label",
                    confirmed_at="2026-08-22",
                )

            reset = printer_memory.propose_upsert(
                path,
                alias="oficina",
                physical_model="K2 Plus",
                evidence_kind="physical_label",
                confirmed_at="2026-08-22",
                reset_dependent_state=True,
            )
            self.assertNotIn(
                "current_setup", reset["candidate"]["printers"]["oficina"]
            )


class PrinterMemoryValidationTests(unittest.TestCase):
    def test_rejects_concurrent_lock_without_removing_it(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "printer-memory.json"
            proposal = printer_memory.propose_upsert(
                path,
                alias="oficina",
                physical_model="K2",
                evidence_kind="physical_label",
                confirmed_at="2026-08-21",
            )
            lock = path.with_suffix(".json.lock")
            lock.write_text("other operation", encoding="utf-8")
            with self.assertRaisesRegex(printer_memory.MemoryToolError, "locked"):
                printer_memory.apply_proposal(path, proposal, user_approved=True)
            self.assertTrue(lock.is_file())
            self.assertFalse(path.exists())

    @unittest.skipIf(os.name == "nt", "symlink creation is not portable on Windows")
    def test_refuses_symlink_target_without_touching_destination(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "printer-memory.json"
            destination = Path(directory) / "destination.json"
            proposal = printer_memory.propose_upsert(
                path,
                alias="oficina",
                physical_model="K2",
                evidence_kind="physical_label",
                confirmed_at="2026-08-21",
            )
            destination.write_text("untouched", encoding="utf-8")
            path.symlink_to(destination)
            with self.assertRaisesRegex(printer_memory.MemoryToolError, "symbolic-link"):
                printer_memory.apply_proposal(path, proposal, user_approved=True)
            self.assertEqual(destination.read_text(encoding="utf-8"), "untouched")

    def test_rejects_sensitive_or_unrecognized_fields(self) -> None:
        document = printer_memory.empty_memory()
        document["printers"]["oficina"] = {
            "identity": {
                "physical_model": "K2",
                "serial": "must-not-be-stored",
                "evidence": {"kind": "physical_label", "confirmed_at": "2026-08-21"},
            }
        }
        with self.assertRaisesRegex(printer_memory.MemoryToolError, "serial"):
            printer_memory.validate_memory(document)

    def test_rejects_slicer_profile_as_physical_identity_proof(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "printer-memory.json"
            with self.assertRaisesRegex(printer_memory.MemoryToolError, "physical identity"):
                printer_memory.propose_upsert(
                    path,
                    alias="oficina",
                    physical_model="K2",
                    evidence_kind="slicer_profile",
                    confirmed_at="2026-08-21",
                )


if __name__ == "__main__":
    unittest.main()
