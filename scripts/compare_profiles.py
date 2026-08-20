#!/usr/bin/env python3
"""Compare known settings from two profiles or 3MF projects."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from typing import Any

from _common import (
    SCHEMA_VERSION,
    ToolError,
    error_envelope,
    extract_known_settings,
    input_metadata,
    print_json,
    resolve_input,
)

TOOL_NAME = "compare_profiles"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare known settings while preserving values, types, units, and origins."
    )
    parser.add_argument("left", help="First profile, configuration, or 3MF project")
    parser.add_argument("right", help="Second profile, configuration, or 3MF project")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")
    return parser


def group(records: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[record["key"]].append(record)
    for key in grouped:
        grouped[key].sort(key=lambda item: (item["origin"], json.dumps(item["value"], sort_keys=True)))
    return dict(grouped)


def comparable(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "value": item["value"],
            "value_type": item["value_type"],
            "unit": item["unit"],
            "category": item["category"],
        }
        for item in records
    ]


def run(left_raw: str, right_raw: str) -> dict[str, Any]:
    left_path = resolve_input(left_raw)
    right_path = resolve_input(right_raw)
    left_records, left_diagnostics = extract_known_settings(left_path)
    right_records, right_diagnostics = extract_known_settings(right_path)
    left = group(left_records)
    right = group(right_records)
    differences: list[dict[str, Any]] = []
    unchanged = 0
    for key in sorted(set(left) | set(right)):
        left_values = left.get(key, [])
        right_values = right.get(key, [])
        if not left_values:
            status = "added"
        elif not right_values:
            status = "removed"
        elif comparable(left_values) == comparable(right_values):
            status = "unchanged"
            unchanged += 1
        else:
            status = "changed"
        if status != "unchanged":
            differences.append(
                {
                    "key": key,
                    "status": status,
                    "left": left_values,
                    "right": right_values,
                }
            )
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_NAME,
        "ok": True,
        "left_input": input_metadata(left_path),
        "right_input": input_metadata(right_path),
        "summary": {
            "left_setting_records": len(left_records),
            "right_setting_records": len(right_records),
            "different_keys": len(differences),
            "unchanged_keys": unchanged,
        },
        "differences": differences,
        "diagnostics": {"left": left_diagnostics, "right": right_diagnostics},
        "claim_boundary": (
            "Differences are file observations. They do not establish which profile is safer, "
            "compatible with a physical printer, or likely to print successfully."
        ),
    }


def main() -> int:
    args = build_parser().parse_args()
    try:
        print_json(run(args.left, args.right), compact=args.compact)
        return 0
    except ToolError as exc:
        print_json(error_envelope(TOOL_NAME, exc), compact=args.compact)
        return 2
    except KeyboardInterrupt:
        print_json(error_envelope(TOOL_NAME, ToolError("interrupted", "Operation interrupted.")))
        return 130


if __name__ == "__main__":
    sys.exit(main())
