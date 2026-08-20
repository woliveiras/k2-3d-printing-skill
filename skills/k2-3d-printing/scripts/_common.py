#!/usr/bin/env python3
"""Shared, dependency-free readers for the k2-3d-printing tools."""

from __future__ import annotations

import hashlib
import json
import re
import stat
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from xml.etree import ElementTree as ET

SCHEMA_VERSION = 1
MAX_ARCHIVE_ENTRIES = 10_000
MAX_MEMBER_BYTES = 64 * 1024 * 1024
MAX_TOTAL_UNCOMPRESSED_BYTES = 256 * 1024 * 1024
MAX_COMPRESSION_RATIO = 1_000


class ToolError(Exception):
    """Raise a user-facing error that can be serialized safely."""

    def __init__(self, code: str, message: str, *, detail: Any | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.detail = detail

    def as_dict(self) -> dict[str, Any]:
        data: dict[str, Any] = {"code": self.code, "message": self.message}
        if self.detail is not None:
            data["detail"] = self.detail
        return data


def json_type(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_input(raw_path: str) -> Path:
    path = Path(raw_path).expanduser().resolve()
    if not path.exists():
        raise ToolError("input_not_found", f"Input does not exist: {path}")
    if not path.is_file():
        raise ToolError("input_not_file", f"Input is not a regular file: {path}")
    return path


def input_metadata(path: Path) -> dict[str, Any]:
    return {
        "path": str(path),
        "name": path.name,
        "size_bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def unsafe_member_reason(info: zipfile.ZipInfo) -> str | None:
    name = info.filename
    posix = PurePosixPath(name)
    if posix.is_absolute() or name.startswith(("/", "\\")):
        return "absolute_path"
    if ".." in posix.parts:
        return "parent_traversal"
    unix_mode = (info.external_attr >> 16) & 0xFFFF
    if unix_mode and stat.S_ISLNK(unix_mode):
        return "symbolic_link"
    if info.file_size > MAX_MEMBER_BYTES:
        return "member_too_large"
    if info.compress_size == 0 and info.file_size > 0:
        return "invalid_compressed_size"
    if info.compress_size and info.file_size / info.compress_size > MAX_COMPRESSION_RATIO:
        return "suspicious_compression_ratio"
    return None


@dataclass(frozen=True)
class ArchiveInventory:
    entries: list[dict[str, Any]]
    total_uncompressed_bytes: int
    unsafe_entries: list[dict[str, str]]


def inventory_zip(archive: zipfile.ZipFile) -> ArchiveInventory:
    infos = archive.infolist()
    if len(infos) > MAX_ARCHIVE_ENTRIES:
        raise ToolError(
            "archive_entry_limit",
            f"Archive contains {len(infos)} entries; limit is {MAX_ARCHIVE_ENTRIES}.",
        )
    total = sum(item.file_size for item in infos)
    if total > MAX_TOTAL_UNCOMPRESSED_BYTES:
        raise ToolError(
            "archive_size_limit",
            f"Archive expands to {total} bytes; limit is {MAX_TOTAL_UNCOMPRESSED_BYTES}.",
        )
    unsafe: list[dict[str, str]] = []
    entries: list[dict[str, Any]] = []
    for info in infos:
        reason = unsafe_member_reason(info)
        if reason:
            unsafe.append({"path": info.filename, "reason": reason})
        entries.append(
            {
                "path": info.filename,
                "compressed_bytes": info.compress_size,
                "uncompressed_bytes": info.file_size,
                "crc32": f"{info.CRC:08x}",
                "is_directory": info.is_dir(),
            }
        )
    return ArchiveInventory(entries, total, unsafe)


def open_checked_zip(path: Path) -> tuple[zipfile.ZipFile, ArchiveInventory]:
    if not zipfile.is_zipfile(path):
        raise ToolError("not_zip", "The input is not a valid ZIP container.")
    try:
        archive = zipfile.ZipFile(path, "r")
        inventory = inventory_zip(archive)
        if inventory.unsafe_entries:
            archive.close()
            raise ToolError(
                "unsafe_archive_member",
                "The archive contains a path or member that is unsafe to process.",
                detail=inventory.unsafe_entries,
            )
        corrupt = archive.testzip()
        if corrupt is not None:
            archive.close()
            raise ToolError("crc_failure", f"CRC validation failed for archive member: {corrupt}")
        return archive, inventory
    except ToolError:
        raise
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        raise ToolError("zip_read_error", f"Cannot read ZIP container: {exc}") from exc


KNOWN_SETTINGS: dict[str, tuple[str, str | None]] = {
    # Printer and hardware profile
    "printer_model": ("printer", None),
    "printer_variant": ("printer", "mm"),
    "printer_technology": ("printer", None),
    "printable_area": ("printer", "mm"),
    "printable_height": ("printer", "mm"),
    "nozzle_diameter": ("printer", "mm"),
    "nozzle_type": ("printer", None),
    "gcode_flavor": ("printer", None),
    "support_chamber_temp_control": ("printer", None),
    "support_air_filtration": ("printer", None),
    "single_extruder_multi_material": ("printer", None),
    "machine_max_acceleration_extruding": ("printer", "mm/s^2"),
    "machine_max_acceleration_travel": ("printer", "mm/s^2"),
    "machine_max_speed_x": ("printer", "mm/s"),
    "machine_max_speed_y": ("printer", "mm/s"),
    "retraction_length": ("printer", "mm"),
    "retraction_speed": ("printer", "mm/s"),
    # Process profile
    "layer_height": ("process", "mm"),
    "initial_layer_print_height": ("process", "mm"),
    "line_width": ("process", "mm"),
    "outer_wall_line_width": ("process", "mm"),
    "inner_wall_line_width": ("process", "mm"),
    "wall_loops": ("process", "count"),
    "top_shell_layers": ("process", "count"),
    "bottom_shell_layers": ("process", "count"),
    "sparse_infill_density": ("process", "%"),
    "sparse_infill_pattern": ("process", None),
    "outer_wall_speed": ("process", "mm/s"),
    "inner_wall_speed": ("process", "mm/s"),
    "sparse_infill_speed": ("process", "mm/s"),
    "travel_speed": ("process", "mm/s"),
    "initial_layer_speed": ("process", "mm/s"),
    "bridge_speed": ("process", "mm/s"),
    "outer_wall_acceleration": ("process", "mm/s^2"),
    "inner_wall_acceleration": ("process", "mm/s^2"),
    "default_acceleration": ("process", "mm/s^2"),
    "support_enable": ("process", None),
    "support_type": ("process", None),
    "support_style": ("process", None),
    "support_threshold_angle": ("process", "degree"),
    "support_top_z_distance": ("process", "mm"),
    "support_bottom_z_distance": ("process", "mm"),
    "support_object_xy_distance": ("process", "mm"),
    "support_interface_top_layers": ("process", "count"),
    "support_interface_spacing": ("process", "mm"),
    "brim_type": ("process", None),
    "brim_width": ("process", "mm"),
    "raft_layers": ("process", "count"),
    "seam_position": ("process", None),
    "ironing_type": ("process", None),
    "enable_prime_tower": ("process", None),
    # Filament profile
    "filament_type": ("filament", None),
    "filament_vendor": ("filament", None),
    "filament_diameter": ("filament", "mm"),
    "filament_density": ("filament", "g/cm^3"),
    "filament_flow_ratio": ("filament", "ratio"),
    "nozzle_temperature": ("filament", "degC"),
    "nozzle_temperature_initial_layer": ("filament", "degC"),
    "bed_temperature": ("filament", "degC"),
    "bed_temperature_initial_layer": ("filament", "degC"),
    "chamber_temperature": ("filament", "degC"),
    "filament_max_volumetric_speed": ("filament", "mm^3/s"),
    "filament_retraction_length": ("filament", "mm"),
    "filament_retraction_speed": ("filament", "mm/s"),
    "fan_min_speed": ("filament", "%"),
    "fan_max_speed": ("filament", "%"),
    "compatible_printers": ("filament", None),
    "compatible_printers_condition": ("filament", None),
    "required_nozzle_HRC": ("filament", "HRC"),
}

_SETTING_KEY_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]{0,127}$")


def normalize_setting_key(raw: str) -> str:
    key = raw.strip().replace(" ", "_").replace("-", "_")
    return key


def make_setting_record(key: str, value: Any, origin: str) -> dict[str, Any] | None:
    normalized = normalize_setting_key(key)
    if normalized not in KNOWN_SETTINGS:
        return None
    category, unit = KNOWN_SETTINGS[normalized]
    return {
        "key": normalized,
        "value": value,
        "value_type": json_type(value),
        "unit": unit,
        "category": category,
        "origin": origin,
    }


def walk_json(value: Any, origin: str, path: str = "$") -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            record = make_setting_record(str(key), child, f"{origin}#{child_path}")
            if record is not None:
                yield record
            yield from walk_json(child, origin, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_json(child, origin, f"{path}[{index}]")


def parse_json_settings(payload: bytes, origin: str) -> list[dict[str, Any]]:
    try:
        document = json.loads(payload.decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        return []
    return list(walk_json(document, origin))


def parse_xml_settings(payload: bytes, origin: str) -> list[dict[str, Any]]:
    try:
        root = ET.fromstring(payload)
    except ET.ParseError:
        return []
    records: list[dict[str, Any]] = []
    for index, element in enumerate(root.iter()):
        location = f"{origin}#element[{index}]"
        key = element.attrib.get("key") or element.attrib.get("name")
        if key:
            raw_value: Any = element.attrib.get("value")
            if raw_value is None and element.text and element.text.strip():
                raw_value = element.text.strip()
            record = make_setting_record(key, raw_value, location)
            if record is not None:
                records.append(record)
        local_tag = element.tag.rsplit("}", 1)[-1]
        if _SETTING_KEY_RE.match(local_tag) and element.text and element.text.strip():
            record = make_setting_record(local_tag, element.text.strip(), location)
            if record is not None:
                records.append(record)
    return records


def dedupe_records(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    unique: list[dict[str, Any]] = []
    seen: set[str] = set()
    for record in records:
        marker = json.dumps(record, sort_keys=True, ensure_ascii=False)
        if marker not in seen:
            unique.append(record)
            seen.add(marker)
    return sorted(unique, key=lambda item: (item["category"], item["key"], item["origin"]))


def extract_known_settings(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    diagnostics: list[str] = []
    records: list[dict[str, Any]] = []
    if path.suffix.lower() == ".3mf":
        archive, _ = open_checked_zip(path)
        try:
            candidates = [
                item
                for item in archive.infolist()
                if not item.is_dir()
                and PurePosixPath(item.filename).suffix.lower()
                in {".json", ".config", ".xml", ".model"}
            ]
            for item in candidates:
                payload = archive.read(item)
                origin = f"{path.name}!/{item.filename}"
                parsed = parse_json_settings(payload, origin)
                if not parsed:
                    parsed = parse_xml_settings(payload, origin)
                records.extend(parsed)
            if not records:
                diagnostics.append("No known Creality/Orca-style settings were found in readable metadata members.")
        finally:
            archive.close()
    else:
        try:
            payload = path.read_bytes()
        except OSError as exc:
            raise ToolError("input_read_error", f"Cannot read input: {exc}") from exc
        records = parse_json_settings(payload, path.name)
        if not records:
            records = parse_xml_settings(payload, path.name)
        if not records:
            diagnostics.append("No known settings were found; only JSON/XML/config/profile inputs are supported.")
    return dedupe_records(records), diagnostics


def success_envelope(tool: str, path: Path) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": tool,
        "ok": True,
        "input": input_metadata(path),
    }


def error_envelope(tool: str, error: ToolError) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "tool": tool,
        "ok": False,
        "error": error.as_dict(),
    }


def print_json(data: Any, *, compact: bool = False) -> None:
    print(json.dumps(data, indent=None if compact else 2, sort_keys=True, ensure_ascii=False))
