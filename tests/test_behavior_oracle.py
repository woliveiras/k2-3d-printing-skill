from __future__ import annotations

import json
import unittest
from pathlib import Path

from response_oracle import evaluate

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "tests" / "evals" / "cases.json"


class BehaviorOracleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))

    def test_has_all_fourteen_required_scenarios(self) -> None:
        expected = {
            "mouse-shell-pla-finish",
            "functional-petg",
            "tpu-cfs",
            "abrasive-composite-wrong-nozzle",
            "hidden-support-setting",
            "creality-print-version-difference",
            "first-layer-failure",
            "nozzle-clog",
            "hardware-incompatible-material",
            "overnight-printing",
            "screenshot-no-version",
            "foreign-3mf",
            "exceeds-official-limit",
            "unknown-torque-or-part",
        }
        actual = {case["id"] for case in self.contract["cases"]}
        self.assertEqual(actual, expected)

    def test_every_passing_fixture_passes(self) -> None:
        failures = []
        for case in self.contract["cases"]:
            result = evaluate(case, case["passing_response"], self.contract["global_forbidden"])
            if not result["pass"]:
                failures.append(result)
        self.assertEqual(failures, [])

    def test_every_failing_fixture_fails(self) -> None:
        false_accepts = []
        for case in self.contract["cases"]:
            result = evaluate(case, case["failing_response"], self.contract["global_forbidden"])
            if result["pass"]:
                false_accepts.append(case["id"])
        self.assertEqual(false_accepts, [])

    def test_global_authority_violations_are_rejected(self) -> None:
        case = self.contract["cases"][0]
        response = case["passing_response"] + " I sent the print job and overwrote the original 3MF."
        result = evaluate(case, response, self.contract["global_forbidden"])
        ids = {item["id"] for item in result["forbidden_matches"]}
        self.assertIn("unauthorized_send", ids)
        self.assertIn("original_overwrite", ids)


if __name__ == "__main__":
    unittest.main()
