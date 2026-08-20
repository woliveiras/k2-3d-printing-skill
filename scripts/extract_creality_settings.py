#!/usr/bin/env python3
"""Extract known printer, process, and filament settings without changing input."""

from __future__ import annotations

import argparse
import sys

from _common import (
    ToolError,
    error_envelope,
    extract_known_settings,
    print_json,
    resolve_input,
    success_envelope,
)

TOOL_NAME = "extract_creality_settings"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract known Creality/Orca-style settings from JSON, XML/config, or 3MF files."
    )
    parser.add_argument("input", help="Profile, configuration, or 3MF project to inspect")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")
    return parser


def run(raw_path: str) -> dict:
    path = resolve_input(raw_path)
    records, diagnostics = extract_known_settings(path)
    result = success_envelope(TOOL_NAME, path)
    result.update(
        {
            "settings": records,
            "counts": {
                "total": len(records),
                "printer": sum(item["category"] == "printer" for item in records),
                "process": sum(item["category"] == "process" for item in records),
                "filament": sum(item["category"] == "filament" for item in records),
            },
            "diagnostics": diagnostics,
            "claim_boundary": (
                "Extracted values describe the file only; they do not identify the physical printer, "
                "prove hardware compatibility, or validate printability."
            ),
        }
    )
    return result


def main() -> int:
    args = build_parser().parse_args()
    try:
        print_json(run(args.input), compact=args.compact)
        return 0
    except ToolError as exc:
        print_json(error_envelope(TOOL_NAME, exc), compact=args.compact)
        return 2
    except KeyboardInterrupt:
        print_json(error_envelope(TOOL_NAME, ToolError("interrupted", "Operation interrupted.")))
        return 130


if __name__ == "__main__":
    sys.exit(main())
