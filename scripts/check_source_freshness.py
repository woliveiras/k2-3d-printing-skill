#!/usr/bin/env python3
"""Audit the structured source register; check links only with explicit opt-in."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

from _common import SCHEMA_VERSION, ToolError, error_envelope, print_json, resolve_input

TOOL_NAME = "check_source_freshness"
HEADING_RE = re.compile(r"^##\s+(S\d{3})\s+[—-]\s+(.+?)\s*$")
FIELD_RE = re.compile(r"^-\s+([^:]+):\s*(.*?)\s*$")
ISO_DATE_RE = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
REQUIRED_FIELDS = {
    "Publisher",
    "URL",
    "Source type",
    "Published/revised",
    "Accessed",
    "Applies to",
    "Supports",
    "Limitations/conflicts",
    "Confidence",
    "Review by",
}


def parse_date_field(raw: str) -> date | None:
    match = ISO_DATE_RE.search(raw)
    if not match:
        return None
    try:
        return date.fromisoformat(match.group(1))
    except ValueError:
        return None


def parse_accessed(raw: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


def parse_sources(path: Path) -> tuple[list[dict[str, Any]], list[dict[str, str]]]:
    entries: list[dict[str, Any]] = []
    issues: list[dict[str, str]] = []
    current: dict[str, Any] | None = None
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as exc:
        raise ToolError("source_read_error", f"Cannot read source register: {exc}") from exc
    for line_number, line in enumerate(lines, start=1):
        heading = HEADING_RE.match(line)
        if heading:
            if current is not None:
                entries.append(current)
            current = {
                "id": heading.group(1),
                "title": heading.group(2),
                "heading_line": line_number,
                "fields": {},
            }
            continue
        field = FIELD_RE.match(line)
        if field and current is not None:
            key, value = field.groups()
            if key in current["fields"]:
                issues.append(
                    {
                        "severity": "error",
                        "source_id": current["id"],
                        "code": "duplicate_field",
                        "message": f"Field {key!r} appears more than once (line {line_number}).",
                    }
                )
            current["fields"][key] = value
    if current is not None:
        entries.append(current)
    if not entries:
        issues.append(
            {
                "severity": "error",
                "source_id": "register",
                "code": "no_sources",
                "message": "No source headings matching '## S001 — Title' were found.",
            }
        )
    ids = [entry["id"] for entry in entries]
    for duplicate in sorted({item for item in ids if ids.count(item) > 1}):
        issues.append(
            {
                "severity": "error",
                "source_id": duplicate,
                "code": "duplicate_source_id",
                "message": f"Source id {duplicate} is duplicated.",
            }
        )
    return entries, issues


def check_url(url: str, timeout: float) -> dict[str, Any]:
    headers = {"User-Agent": "k2-3d-printing-source-audit/1.0"}
    request = urllib.request.Request(url, method="HEAD", headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return {"checked": True, "reachable": True, "status": response.status, "final_url": response.url}
    except urllib.error.HTTPError as exc:
        if exc.code not in {400, 403, 405, 501}:
            return {"checked": True, "reachable": False, "status": exc.code, "error": str(exc)}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"checked": True, "reachable": False, "status": None, "error": str(exc)}
    fallback = urllib.request.Request(url, method="GET", headers={**headers, "Range": "bytes=0-0"})
    try:
        with urllib.request.urlopen(fallback, timeout=timeout) as response:
            response.read(1)
            return {"checked": True, "reachable": True, "status": response.status, "final_url": response.url}
    except urllib.error.HTTPError as exc:
        return {"checked": True, "reachable": False, "status": exc.code, "error": str(exc)}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {"checked": True, "reachable": False, "status": None, "error": str(exc)}


def audit(
    path: Path,
    *,
    as_of: date,
    max_age_days: int,
    check_links: bool,
    timeout: float,
    strict: bool,
) -> dict[str, Any]:
    entries, issues = parse_sources(path)
    audited: list[dict[str, Any]] = []
    for entry in entries:
        fields = entry["fields"]
        source_issues: list[dict[str, str]] = []
        missing = sorted(REQUIRED_FIELDS - set(fields))
        for field in missing:
            source_issues.append(
                {
                    "severity": "error",
                    "source_id": entry["id"],
                    "code": "missing_field",
                    "message": f"Missing required field: {field}.",
                }
            )
        published = parse_date_field(fields.get("Published/revised", ""))
        publication_value = fields.get("Published/revised", "")
        if "Published/revised" in fields and published is None:
            source_issues.append(
                {
                    "severity": "warning",
                    "source_id": entry["id"],
                    "code": "publication_date_not_stated",
                    "message": f"No valid publication/revision date is recorded ({publication_value!r}).",
                }
            )
        accessed = parse_accessed(fields.get("Accessed", "")) if "Accessed" in fields else None
        if "Accessed" in fields and accessed is None:
            source_issues.append(
                {
                    "severity": "error",
                    "source_id": entry["id"],
                    "code": "invalid_accessed_timestamp",
                    "message": "Accessed must be an ISO-8601 timestamp with a date.",
                }
            )
        age_days = None
        if accessed is not None:
            age_days = (as_of - accessed.date()).days
            if age_days < 0:
                source_issues.append(
                    {
                        "severity": "error",
                        "source_id": entry["id"],
                        "code": "future_access_timestamp",
                        "message": "Access timestamp is after the audit date.",
                    }
                )
            elif age_days > max_age_days:
                source_issues.append(
                    {
                        "severity": "warning",
                        "source_id": entry["id"],
                        "code": "access_too_old",
                        "message": f"Last access was {age_days} days ago; threshold is {max_age_days}.",
                    }
                )
        review_by = parse_date_field(fields.get("Review by", "")) if "Review by" in fields else None
        if "Review by" in fields and review_by is None:
            source_issues.append(
                {
                    "severity": "error",
                    "source_id": entry["id"],
                    "code": "invalid_review_date",
                    "message": "Review by must contain an ISO date.",
                }
            )
        elif review_by is not None and as_of > review_by:
            source_issues.append(
                {
                    "severity": "warning",
                    "source_id": entry["id"],
                    "code": "review_overdue",
                    "message": f"Review was due on {review_by.isoformat()}.",
                }
            )
        url = fields.get("URL")
        link = {"checked": False, "reason": "network check not requested"}
        if check_links and url:
            if not url.startswith(("https://", "http://")):
                link = {"checked": True, "reachable": False, "status": None, "error": "unsupported URL scheme"}
            else:
                link = check_url(url, timeout)
            if not link.get("reachable"):
                source_issues.append(
                    {
                        "severity": "error",
                        "source_id": entry["id"],
                        "code": "link_unreachable",
                        "message": f"Source URL was not reachable: {link.get('error') or link.get('status')}.",
                    }
                )
        issues.extend(source_issues)
        audited.append(
            {
                "id": entry["id"],
                "title": entry["title"],
                "heading_line": entry["heading_line"],
                "published_or_revised_date": published.isoformat() if published else None,
                "accessed_age_days": age_days,
                "review_by": review_by.isoformat() if review_by else None,
                "url": url,
                "link": link,
                "issue_codes": [item["code"] for item in source_issues],
            }
        )
    errors = sum(item["severity"] == "error" for item in issues)
    warnings = sum(item["severity"] == "warning" for item in issues)
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_NAME,
        "ok": errors == 0 and (not strict or warnings == 0),
        "input": str(path),
        "policy": {
            "as_of": as_of.isoformat(),
            "max_age_days": max_age_days,
            "network_links_checked": check_links,
            "strict": strict,
        },
        "summary": {"sources": len(entries), "errors": errors, "warnings": warnings},
        "sources": audited,
        "issues": issues,
        "claim_boundary": (
            "Reachability and dates do not prove that a source is correct, current in substance, or applicable. "
            "Review supported claims and conflicts manually."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit source metadata and optional URL reachability.")
    parser.add_argument("sources", nargs="?", default="references/sources.md", help="Structured sources.md file")
    parser.add_argument("--as-of", default=date.today().isoformat(), help="Audit date in YYYY-MM-DD form")
    parser.add_argument("--max-age-days", type=int, default=180, help="Warn after this many days since access")
    parser.add_argument(
        "--check-links",
        action="store_true",
        help="Perform network requests; use only when the caller has authorized network access",
    )
    parser.add_argument("--timeout", type=float, default=10.0, help="Per-request timeout in seconds")
    parser.add_argument("--strict", action="store_true", help="Return failure when warnings exist")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        path = resolve_input(args.sources)
        if args.max_age_days < 0:
            raise ToolError("invalid_threshold", "--max-age-days must be zero or greater.")
        if args.timeout <= 0:
            raise ToolError("invalid_timeout", "--timeout must be greater than zero.")
        try:
            as_of = date.fromisoformat(args.as_of)
        except ValueError as exc:
            raise ToolError("invalid_as_of", "--as-of must be YYYY-MM-DD.") from exc
        result = audit(
            path,
            as_of=as_of,
            max_age_days=args.max_age_days,
            check_links=args.check_links,
            timeout=args.timeout,
            strict=args.strict,
        )
        print_json(result, compact=args.compact)
        return 0 if result["ok"] else 1
    except ToolError as exc:
        print_json(error_envelope(TOOL_NAME, exc), compact=args.compact)
        return 2
    except KeyboardInterrupt:
        print_json(error_envelope(TOOL_NAME, ToolError("interrupted", "Operation interrupted.")))
        return 130


if __name__ == "__main__":
    sys.exit(main())
