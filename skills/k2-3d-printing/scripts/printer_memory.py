#!/usr/bin/env python3
"""Manage portable, user-approved printer memory without external dependencies."""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import math
import os
import platform
import re
import sys
import tempfile
from collections.abc import Mapping
from datetime import date
from pathlib import Path
from typing import Any

SCHEMA_VERSION = 1
PROPOSAL_VERSION = 1
TOOL_NAME = "printer_memory"
DATA_DIR_ENV = "K2_3D_PRINTING_DATA_DIR"
FILE_NAME = "printer-memory.json"
MAX_FILE_BYTES = 1024 * 1024
MAX_PRINTERS = 100

ALIAS_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")
EVIDENCE_RE = re.compile(r"^[a-z][a-z0-9_]{0,63}$")
IDENTITY_EVIDENCE = {
    "physical_label",
    "about_screen",
    "purchase_document",
    "firmware_identity",
    "user_supplied_photo",
}

FIELD_SPECS: dict[str, tuple[str, str]] = {
    "current_setup.nozzle.diameter_mm": ("positive_number", "current_setup.nozzle"),
    "current_setup.nozzle.material": ("string", "current_setup.nozzle"),
    "current_setup.plate.type": ("string", "current_setup.plate"),
    "current_setup.feed_path.type": ("string", "current_setup.feed_path"),
    "software.firmware.version": ("string", "software.firmware"),
    "software.creality_print.version": ("string", "software.creality_print"),
}


class MemoryToolError(Exception):
    """Represent a safe, user-facing memory error."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message

    def as_dict(self) -> dict[str, str]:
        return {"code": self.code, "message": self.message}


def default_memory_path(
    *,
    system_name: str | None = None,
    home: Path | None = None,
    environ: Mapping[str, str] | None = None,
) -> Path:
    """Return a per-user, agent-independent configuration path."""

    environment = os.environ if environ is None else environ
    user_home = Path.home() if home is None else home
    override = environment.get(DATA_DIR_ENV)
    if override:
        base = Path(override).expanduser()
    else:
        system = platform.system() if system_name is None else system_name
        if system == "Windows":
            base = Path(environment.get("APPDATA", str(user_home / "AppData" / "Roaming")))
        elif system == "Darwin":
            base = user_home / "Library" / "Application Support"
        else:
            base = Path(environment.get("XDG_CONFIG_HOME", str(user_home / ".config")))
        base = base / "k2-3d-printing"
    return base / FILE_NAME


def normalize_data_path(raw_path: str | Path | None) -> Path:
    path = default_memory_path() if raw_path is None else Path(raw_path).expanduser()
    return Path(os.path.abspath(path))


def empty_memory() -> dict[str, Any]:
    return {"schema_version": SCHEMA_VERSION, "revision": 0, "printers": {}}


def _exact_keys(value: dict[str, Any], allowed: set[str], context: str) -> None:
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise MemoryToolError(
            "unknown_field", f"Unrecognized or sensitive field in {context}: {unknown[0]}"
        )


def _require_object(value: Any, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise MemoryToolError("invalid_type", f"{context} must be a JSON object.")
    return value


def _require_string(value: Any, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise MemoryToolError("invalid_value", f"{context} must be a non-empty string.")
    if len(value) > 256:
        raise MemoryToolError("invalid_value", f"{context} exceeds 256 characters.")
    return value


def _validate_evidence(value: Any, context: str) -> None:
    evidence = _require_object(value, context)
    _exact_keys(evidence, {"kind", "confirmed_at"}, context)
    kind = _require_string(evidence.get("kind"), f"{context}.kind")
    if not EVIDENCE_RE.fullmatch(kind):
        raise MemoryToolError("invalid_evidence", f"{context}.kind has an invalid format.")
    confirmed_at = _require_string(evidence.get("confirmed_at"), f"{context}.confirmed_at")
    try:
        date.fromisoformat(confirmed_at)
    except ValueError as exc:
        raise MemoryToolError(
            "invalid_date", f"{context}.confirmed_at must use YYYY-MM-DD."
        ) from exc


def _validate_identity(value: Any, alias: str) -> None:
    identity = _require_object(value, f"printers.{alias}.identity")
    _exact_keys(identity, {"physical_model", "evidence"}, f"printers.{alias}.identity")
    _require_string(identity.get("physical_model"), f"printers.{alias}.identity.physical_model")
    _validate_evidence(identity.get("evidence"), f"printers.{alias}.identity.evidence")
    if identity["evidence"]["kind"] not in IDENTITY_EVIDENCE:
        raise MemoryToolError(
            "identity_evidence",
            "A slicer profile or user assertion cannot establish physical identity; use the "
            "physical label, About screen, tied purchase document, firmware identity, or photo.",
        )


def _validate_component(
    value: Any,
    *,
    context: str,
    allowed: set[str],
    required_any: set[str],
) -> None:
    component = _require_object(value, context)
    _exact_keys(component, allowed | {"evidence"}, context)
    if not required_any.intersection(component):
        raise MemoryToolError(
            "missing_value", f"{context} requires one of: {', '.join(sorted(required_any))}."
        )
    _validate_evidence(component.get("evidence"), f"{context}.evidence")
    for field in required_any.intersection(component):
        if field == "diameter_mm":
            number = component[field]
            if isinstance(number, bool) or not isinstance(number, (int, float)):
                raise MemoryToolError("invalid_value", f"{context}.{field} must be a number.")
            if not math.isfinite(number) or number <= 0:
                raise MemoryToolError("invalid_value", f"{context}.{field} must be positive.")
        else:
            _require_string(component[field], f"{context}.{field}")


def _validate_printer(value: Any, alias: str) -> None:
    printer = _require_object(value, f"printers.{alias}")
    _exact_keys(printer, {"identity", "current_setup", "software", "preferences"}, f"printers.{alias}")
    if "identity" not in printer:
        raise MemoryToolError("missing_identity", f"Printer {alias} requires physical identity.")
    _validate_identity(printer["identity"], alias)

    if "current_setup" in printer:
        setup = _require_object(printer["current_setup"], f"printers.{alias}.current_setup")
        _exact_keys(setup, {"nozzle", "plate", "feed_path"}, f"printers.{alias}.current_setup")
        if "nozzle" in setup:
            _validate_component(
                setup["nozzle"],
                context=f"printers.{alias}.current_setup.nozzle",
                allowed={"diameter_mm", "material"},
                required_any={"diameter_mm", "material"},
            )
        if "plate" in setup:
            _validate_component(
                setup["plate"],
                context=f"printers.{alias}.current_setup.plate",
                allowed={"type"},
                required_any={"type"},
            )
        if "feed_path" in setup:
            _validate_component(
                setup["feed_path"],
                context=f"printers.{alias}.current_setup.feed_path",
                allowed={"type"},
                required_any={"type"},
            )

    if "software" in printer:
        software = _require_object(printer["software"], f"printers.{alias}.software")
        _exact_keys(software, {"firmware", "creality_print"}, f"printers.{alias}.software")
        for key in software:
            _validate_component(
                software[key],
                context=f"printers.{alias}.software.{key}",
                allowed={"version"},
                required_any={"version"},
            )

    if "preferences" in printer:
        preferences = _require_object(printer["preferences"], f"printers.{alias}.preferences")
        _exact_keys(preferences, {"slicer_language", "measurement_units"}, f"printers.{alias}.preferences")
        for key, item in preferences.items():
            _require_string(item, f"printers.{alias}.preferences.{key}")


def validate_memory(document: Any) -> dict[str, Any]:
    memory = _require_object(document, "memory")
    _exact_keys(memory, {"schema_version", "revision", "printers"}, "memory")
    if memory.get("schema_version") != SCHEMA_VERSION:
        raise MemoryToolError(
            "unsupported_schema", f"Only memory schema {SCHEMA_VERSION} is supported."
        )
    revision = memory.get("revision")
    if isinstance(revision, bool) or not isinstance(revision, int) or revision < 0:
        raise MemoryToolError("invalid_revision", "Memory revision must be a non-negative integer.")
    printers = _require_object(memory.get("printers"), "memory.printers")
    if len(printers) > MAX_PRINTERS:
        raise MemoryToolError("printer_limit", f"Memory supports at most {MAX_PRINTERS} printers.")
    for alias, printer in printers.items():
        if not isinstance(alias, str) or not ALIAS_RE.fullmatch(alias):
            raise MemoryToolError(
                "invalid_alias", "Printer aliases must use 1-64 lowercase letters, digits, or hyphens."
            )
        _validate_printer(printer, alias)
    return memory


def _read_bytes(path: Path) -> bytes:
    if path.is_symlink():
        raise MemoryToolError("unsafe_path", "Refusing to read or replace a symbolic-link memory file.")
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise MemoryToolError("read_error", f"Cannot inspect memory file: {exc}") from exc
    if size > MAX_FILE_BYTES:
        raise MemoryToolError("file_too_large", f"Memory file exceeds {MAX_FILE_BYTES} bytes.")
    try:
        return path.read_bytes()
    except OSError as exc:
        raise MemoryToolError("read_error", f"Cannot read memory file: {exc}") from exc


def load_memory(path: Path) -> dict[str, Any]:
    if not path.exists():
        return empty_memory()
    raw = _read_bytes(path)
    try:
        document = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise MemoryToolError("invalid_json", f"Memory file is not valid UTF-8 JSON: {exc}") from exc
    return validate_memory(document)


def _file_sha256(path: Path) -> str | None:
    if not path.exists():
        return None
    return hashlib.sha256(_read_bytes(path)).hexdigest()


def _copy_json(value: Any) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False, allow_nan=False))


def _canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")


def _proposal_token(proposal_without_token: dict[str, Any]) -> str:
    return hashlib.sha256(_canonical_json(proposal_without_token)).hexdigest()


def _build_proposal(
    path: Path,
    *,
    base: dict[str, Any],
    candidate: dict[str, Any],
    operation: str,
    diff: list[dict[str, Any]],
) -> dict[str, Any]:
    candidate["revision"] = base["revision"] + 1
    validate_memory(candidate)
    proposal = {
        "proposal_version": PROPOSAL_VERSION,
        "tool": TOOL_NAME,
        "operation": operation,
        "data_file": str(path),
        "base_revision": base["revision"],
        "base_sha256": _file_sha256(path),
        "candidate_revision": candidate["revision"],
        "diff": diff,
        "candidate": candidate,
        "claim_boundary": (
            "This is a write-free proposal. It does not prove physical hardware or installation "
            "completion and must not be applied without explicit user approval."
        ),
    }
    proposal["proposal_token"] = _proposal_token(proposal)
    return proposal


def _evidence(kind: str, confirmed_at: str) -> dict[str, str]:
    evidence = {"kind": kind, "confirmed_at": confirmed_at}
    _validate_evidence(evidence, "evidence")
    return evidence


def propose_upsert(
    path: Path,
    *,
    alias: str,
    physical_model: str,
    evidence_kind: str,
    confirmed_at: str,
    nozzle_diameter_mm: float | None = None,
    nozzle_material: str | None = None,
    plate_type: str | None = None,
    feed_path_type: str | None = None,
    configuration_evidence_kind: str = "user_statement",
    reset_dependent_state: bool = False,
) -> dict[str, Any]:
    if evidence_kind not in IDENTITY_EVIDENCE:
        raise MemoryToolError(
            "identity_evidence", "A slicer profile cannot establish physical identity."
        )
    if not ALIAS_RE.fullmatch(alias):
        raise MemoryToolError("invalid_alias", "Printer alias has an invalid format.")
    base = load_memory(path)
    candidate = _copy_json(base)
    previous = _copy_json(candidate["printers"].get(alias))
    printer = candidate["printers"].setdefault(alias, {})
    previous_model = _nested_get(printer, "identity.physical_model")
    identity_changed = previous_model is not None and previous_model != physical_model
    dependent_state = any(key in printer for key in ("current_setup", "software"))
    if identity_changed and dependent_state and not reset_dependent_state:
        raise MemoryToolError(
            "dependent_state_reset",
            "Changing physical identity requires explicit reset of dependent setup and software state.",
        )
    if identity_changed and reset_dependent_state:
        printer.pop("current_setup", None)
        printer.pop("software", None)
    printer["identity"] = {
        "physical_model": physical_model,
        "evidence": _evidence(evidence_kind, confirmed_at),
    }
    setup = printer.setdefault("current_setup", {})
    configuration_evidence = _evidence(configuration_evidence_kind, confirmed_at)
    if nozzle_diameter_mm is not None or nozzle_material is not None:
        nozzle = setup.setdefault("nozzle", {})
        if nozzle_diameter_mm is not None:
            nozzle["diameter_mm"] = nozzle_diameter_mm
        if nozzle_material is not None:
            nozzle["material"] = nozzle_material
        nozzle["evidence"] = configuration_evidence
    if plate_type is not None:
        setup["plate"] = {"type": plate_type, "evidence": configuration_evidence}
    if feed_path_type is not None:
        setup["feed_path"] = {"type": feed_path_type, "evidence": configuration_evidence}
    if not setup:
        printer.pop("current_setup", None)
    diff = [{"printer": alias, "before": previous, "after": _copy_json(printer)}]
    return _build_proposal(
        path, base=base, candidate=candidate, operation="upsert_printer", diff=diff
    )


def _nested_get(root: dict[str, Any], dotted: str) -> Any:
    value: Any = root
    for part in dotted.split("."):
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    return value


def _nested_container(root: dict[str, Any], dotted: str) -> dict[str, Any]:
    value = root
    for part in dotted.split("."):
        child = value.setdefault(part, {})
        if not isinstance(child, dict):
            raise MemoryToolError("invalid_state", f"Cannot create object at {dotted}.")
        value = child
    return value


def _validate_field_value(field: str, value: Any) -> None:
    expected, _ = FIELD_SPECS[field]
    if expected == "string":
        _require_string(value, field)
    elif expected == "positive_number":
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise MemoryToolError("invalid_value", f"{field} must be a number.")
        if not math.isfinite(value) or value <= 0:
            raise MemoryToolError("invalid_value", f"{field} must be positive.")


def propose_set(
    path: Path,
    *,
    alias: str,
    field: str,
    value: Any,
    evidence_kind: str,
    confirmed_at: str,
) -> dict[str, Any]:
    if field not in FIELD_SPECS:
        raise MemoryToolError("unsupported_field", f"Unsupported memory field: {field}")
    _validate_field_value(field, value)
    base = load_memory(path)
    if alias not in base["printers"]:
        raise MemoryToolError("printer_not_found", f"Printer alias not found: {alias}")
    if field == "identity.physical_model" and evidence_kind not in IDENTITY_EVIDENCE:
        raise MemoryToolError("identity_evidence", "Physical identity requires stronger evidence.")

    candidate = _copy_json(base)
    printer = candidate["printers"][alias]
    before = _copy_json(_nested_get(printer, field))
    parts = field.split(".")
    container = _nested_container(printer, ".".join(parts[:-1]))
    container[parts[-1]] = value
    _, evidence_parent = FIELD_SPECS[field]
    _nested_container(printer, evidence_parent)["evidence"] = _evidence(
        evidence_kind, confirmed_at
    )
    diff = [
        {
            "printer": alias,
            "field": field,
            "before": before,
            "after": value,
            "evidence": _evidence(evidence_kind, confirmed_at),
        }
    ]
    return _build_proposal(
        path, base=base, candidate=candidate, operation="set_field", diff=diff
    )


def _atomic_write(path: Path, data: bytes) -> None:
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary)
    try:
        if hasattr(os, "fchmod"):
            os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_path, path)
    except Exception:
        try:
            temporary_path.unlink(missing_ok=True)
        except OSError:
            pass
        raise


def _validate_proposal(path: Path, proposal: Any) -> dict[str, Any]:
    value = _require_object(proposal, "proposal")
    required = {
        "proposal_version",
        "tool",
        "operation",
        "data_file",
        "base_revision",
        "base_sha256",
        "candidate_revision",
        "diff",
        "candidate",
        "claim_boundary",
        "proposal_token",
    }
    _exact_keys(value, required, "proposal")
    if set(value) != required:
        missing = sorted(required - set(value))
        raise MemoryToolError("invalid_proposal", f"Proposal is missing: {missing[0]}")
    if value["proposal_version"] != PROPOSAL_VERSION or value["tool"] != TOOL_NAME:
        raise MemoryToolError("invalid_proposal", "Proposal version or tool does not match.")
    if value["operation"] not in {"upsert_printer", "set_field"}:
        raise MemoryToolError("invalid_proposal", "Proposal operation is unsupported.")
    if not isinstance(value["diff"], list) or len(value["diff"]) != 1:
        raise MemoryToolError("invalid_diff", "Proposal must contain exactly one diff entry.")
    if Path(value["data_file"]) != path:
        raise MemoryToolError("proposal_path", "Proposal targets a different memory file.")
    supplied_token = value["proposal_token"]
    unsigned = dict(value)
    unsigned.pop("proposal_token")
    expected_token = _proposal_token(unsigned)
    if not isinstance(supplied_token, str) or not hmac.compare_digest(
        supplied_token, expected_token
    ):
        raise MemoryToolError("proposal_token", "Proposal token does not match its contents.")
    candidate = validate_memory(value["candidate"])
    if candidate["revision"] != value["candidate_revision"]:
        raise MemoryToolError("invalid_proposal", "Candidate revision does not match proposal.")
    return value


def _reconstruct_candidate(base: dict[str, Any], proposal: dict[str, Any]) -> dict[str, Any]:
    candidate = _copy_json(base)
    change = _require_object(proposal["diff"][0], "proposal.diff[0]")
    operation = proposal["operation"]
    if operation == "upsert_printer":
        _exact_keys(change, {"printer", "before", "after"}, "proposal.diff[0]")
        if set(change) != {"printer", "before", "after"}:
            raise MemoryToolError("invalid_diff", "Upsert diff is incomplete.")
        alias = change["printer"]
        if not isinstance(alias, str) or not ALIAS_RE.fullmatch(alias):
            raise MemoryToolError("invalid_diff", "Upsert diff has an invalid printer alias.")
        current = candidate["printers"].get(alias)
        if current != change["before"]:
            raise MemoryToolError("invalid_diff", "Upsert diff does not match current memory.")
        candidate["printers"][alias] = _copy_json(change["after"])
    else:
        expected = {"printer", "field", "before", "after", "evidence"}
        _exact_keys(change, expected, "proposal.diff[0]")
        if set(change) != expected:
            raise MemoryToolError("invalid_diff", "Set-field diff is incomplete.")
        alias = change["printer"]
        field = change["field"]
        if alias not in candidate["printers"] or field not in FIELD_SPECS:
            raise MemoryToolError("invalid_diff", "Set-field diff targets unknown state.")
        printer = candidate["printers"][alias]
        if _nested_get(printer, field) != change["before"]:
            raise MemoryToolError("invalid_diff", "Set-field diff does not match current memory.")
        _validate_field_value(field, change["after"])
        parts = field.split(".")
        _nested_container(printer, ".".join(parts[:-1]))[parts[-1]] = _copy_json(
            change["after"]
        )
        _, evidence_parent = FIELD_SPECS[field]
        evidence = _copy_json(change["evidence"])
        _validate_evidence(evidence, "proposal.diff[0].evidence")
        if field == "identity.physical_model" and evidence["kind"] not in IDENTITY_EVIDENCE:
            raise MemoryToolError("invalid_diff", "Identity diff lacks physical evidence.")
        _nested_container(printer, evidence_parent)["evidence"] = evidence
    candidate["revision"] = base["revision"] + 1
    return validate_memory(candidate)


def apply_proposal(
    path: Path, proposal: Any, *, user_approved: bool
) -> dict[str, Any]:
    if not user_approved:
        raise MemoryToolError(
            "approval_required", "Explicit user approval is required before memory is written."
        )
    path = normalize_data_path(path)
    value = _validate_proposal(path, proposal)
    parent = path.parent
    if parent.exists() and parent.is_symlink():
        raise MemoryToolError("unsafe_path", "Refusing a symbolic-link memory directory.")
    try:
        parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    except OSError as exc:
        raise MemoryToolError("directory_error", f"Cannot create memory directory: {exc}") from exc

    lock_path = path.with_suffix(path.suffix + ".lock")
    try:
        lock_descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise MemoryToolError(
            "memory_locked", "Memory is locked by another operation; do not remove the lock automatically."
        ) from exc
    except OSError as exc:
        raise MemoryToolError("lock_error", f"Cannot create memory lock: {exc}") from exc

    os.close(lock_descriptor)
    backup_created = False
    try:
        current = load_memory(path)
        current_sha = _file_sha256(path)
        if (
            current["revision"] != value["base_revision"]
            or current_sha != value["base_sha256"]
        ):
            raise MemoryToolError(
                "stale_proposal", "Proposal is stale because printer memory changed."
            )
        candidate = _reconstruct_candidate(current, value)
        if _canonical_json(candidate) != _canonical_json(value["candidate"]):
            raise MemoryToolError(
                "candidate_diff_mismatch",
                "Proposal candidate contains changes that are not represented by its diff.",
            )
        if path.exists():
            _atomic_write(path.with_suffix(path.suffix + ".bak"), _read_bytes(path))
            backup_created = True
        serialized = json.dumps(
            candidate, ensure_ascii=False, allow_nan=False, indent=2, sort_keys=True
        ).encode("utf-8") + b"\n"
        _atomic_write(path, serialized)
    except MemoryToolError:
        raise
    except OSError as exc:
        raise MemoryToolError("write_error", f"Cannot write printer memory: {exc}") from exc
    finally:
        try:
            lock_path.unlink()
        except OSError:
            pass

    return {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_NAME,
        "ok": True,
        "data_file": str(path),
        "revision": candidate["revision"],
        "printers": sorted(candidate["printers"]),
        "backup_created": backup_created,
        "claim_boundary": (
            "Memory was updated from an explicitly approved proposal. Stored state remains "
            "subordinate to newer physical observation and task-specific freshness checks."
        ),
    }


def _read_proposal_file(path: Path) -> dict[str, Any]:
    if not path.is_file() or path.is_symlink():
        raise MemoryToolError("proposal_file", "Proposal must be a regular, non-symlink file.")
    if path.stat().st_size > MAX_FILE_BYTES:
        raise MemoryToolError("proposal_file", "Proposal file is too large.")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise MemoryToolError("proposal_file", f"Cannot read proposal JSON: {exc}") from exc


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read and explicitly update portable printer memory.")
    parser.add_argument("--data-file", help="Override the resolved printer-memory JSON file")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("path", help="Show the resolved memory path")
    subparsers.add_parser("list", help="List stored printer aliases")
    show = subparsers.add_parser("show", help="Show one stored printer")
    show.add_argument("alias")
    subparsers.add_parser("validate", help="Validate the memory file without writing")

    upsert = subparsers.add_parser("propose-upsert", help="Propose adding or updating a printer")
    upsert.add_argument("alias")
    upsert.add_argument("--physical-model", required=True)
    upsert.add_argument("--identity-evidence", required=True)
    upsert.add_argument("--configuration-evidence", default="user_statement")
    upsert.add_argument("--confirmed-at", required=True)
    upsert.add_argument("--nozzle-diameter-mm", type=float)
    upsert.add_argument("--nozzle-material")
    upsert.add_argument("--plate-type")
    upsert.add_argument("--feed-path-type")
    upsert.add_argument("--reset-dependent-state", action="store_true")

    set_parser = subparsers.add_parser("propose-set", help="Propose one confirmed field change")
    set_parser.add_argument("alias")
    set_parser.add_argument("field", choices=sorted(FIELD_SPECS))
    set_parser.add_argument("--value-json", required=True)
    set_parser.add_argument("--evidence-kind", required=True)
    set_parser.add_argument("--confirmed-at", required=True)

    apply_parser = subparsers.add_parser("apply", help="Apply an approved proposal file")
    apply_parser.add_argument("proposal_file")
    apply_parser.add_argument("--user-approved", action="store_true", required=True)
    return parser


def _envelope(path: Path, command: str, result: Any) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": TOOL_NAME,
        "ok": True,
        "command": command,
        "data_file": str(path),
        "result": result,
    }


def _run_cli(args: argparse.Namespace, path: Path) -> dict[str, Any]:
    if args.command == "path":
        return _envelope(path, args.command, {"exists": path.is_file()})
    if args.command == "list":
        memory = load_memory(path)
        return _envelope(
            path,
            args.command,
            {"revision": memory["revision"], "printers": sorted(memory["printers"])},
        )
    if args.command == "show":
        memory = load_memory(path)
        if args.alias not in memory["printers"]:
            raise MemoryToolError("printer_not_found", f"Printer alias not found: {args.alias}")
        return _envelope(path, args.command, memory["printers"][args.alias])
    if args.command == "validate":
        memory = load_memory(path)
        return _envelope(
            path,
            args.command,
            {"revision": memory["revision"], "printer_count": len(memory["printers"])},
        )
    if args.command == "propose-upsert":
        return propose_upsert(
            path,
            alias=args.alias,
            physical_model=args.physical_model,
            evidence_kind=args.identity_evidence,
            confirmed_at=args.confirmed_at,
            nozzle_diameter_mm=args.nozzle_diameter_mm,
            nozzle_material=args.nozzle_material,
            plate_type=args.plate_type,
            feed_path_type=args.feed_path_type,
            configuration_evidence_kind=args.configuration_evidence,
            reset_dependent_state=args.reset_dependent_state,
        )
    if args.command == "propose-set":
        try:
            value = json.loads(args.value_json)
        except json.JSONDecodeError as exc:
            raise MemoryToolError("invalid_value_json", f"--value-json is invalid: {exc}") from exc
        return propose_set(
            path,
            alias=args.alias,
            field=args.field,
            value=value,
            evidence_kind=args.evidence_kind,
            confirmed_at=args.confirmed_at,
        )
    if args.command == "apply":
        return apply_proposal(
            path, _read_proposal_file(Path(args.proposal_file)), user_approved=args.user_approved
        )
    raise MemoryToolError("unknown_command", f"Unsupported command: {args.command}")


def main() -> int:
    args = _parser().parse_args()
    path = normalize_data_path(args.data_file)
    try:
        result = _run_cli(args, path)
        print(json.dumps(result, ensure_ascii=False, allow_nan=False, indent=2, sort_keys=True))
        return 0
    except MemoryToolError as exc:
        print(
            json.dumps(
                {
                    "schema_version": SCHEMA_VERSION,
                    "tool": TOOL_NAME,
                    "ok": False,
                    "error": exc.as_dict(),
                },
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
        )
        return 2
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(main())
