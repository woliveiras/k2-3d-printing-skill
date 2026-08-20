#!/usr/bin/env python3
"""Deterministic lexical guardrail oracle for the bundled behavior cases."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CASES = ROOT / "tests" / "evals" / "cases.json"


def load_contract(path: Path = DEFAULT_CASES) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def find_case(contract: dict[str, Any], case_id: str) -> dict[str, Any]:
    for case in contract["cases"]:
        if case["id"] == case_id:
            return case
    raise KeyError(case_id)


def evaluate(case: dict[str, Any], response: str, global_forbidden: list[dict[str, str]]) -> dict[str, Any]:
    missing_groups: list[dict[str, Any]] = []
    forbidden_matches: list[dict[str, str]] = []
    for group in case["required_groups"]:
        if not any(re.search(pattern, response, re.IGNORECASE | re.DOTALL) for pattern in group["patterns"]):
            missing_groups.append({"id": group["id"], "patterns": group["patterns"]})
    for rule in [*global_forbidden, *case.get("forbidden", [])]:
        match = re.search(rule["pattern"], response, re.IGNORECASE | re.DOTALL)
        if match:
            forbidden_matches.append({"id": rule["id"], "match": match.group(0)})
    return {
        "case_id": case["id"],
        "pass": not missing_groups and not forbidden_matches,
        "missing_required_groups": missing_groups,
        "forbidden_matches": forbidden_matches,
        "limitations": (
            "This deterministic oracle checks explicit guardrail language only. It cannot establish factual "
            "accuracy, source quality, UI observation, hardware identity, or physical printability."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Evaluate a response against one deterministic behavior case.")
    parser.add_argument("case_id")
    parser.add_argument("response", help="UTF-8 text file containing the response")
    parser.add_argument("--cases", default=str(DEFAULT_CASES))
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        contract = load_contract(Path(args.cases))
        case = find_case(contract, args.case_id)
        response = Path(args.response).read_text(encoding="utf-8")
        result = evaluate(case, response, contract["global_forbidden"])
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result["pass"] else 1
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, KeyError) as exc:
        print(json.dumps({"pass": False, "error": str(exc)}, indent=2, sort_keys=True))
        return 2


if __name__ == "__main__":
    sys.exit(main())
