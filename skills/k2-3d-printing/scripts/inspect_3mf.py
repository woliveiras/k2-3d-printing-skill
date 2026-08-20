#!/usr/bin/env python3
"""Inspect a 3MF package and mesh topology without extracting or modifying it."""

from __future__ import annotations

import argparse
import math
import posixpath
import sys
from collections import Counter
from pathlib import PurePosixPath
from typing import Any
from xml.etree import ElementTree as ET

from _common import (
    ToolError,
    error_envelope,
    open_checked_zip,
    print_json,
    resolve_input,
    success_envelope,
)

TOOL_NAME = "inspect_3mf"
CORE_NS = "http://schemas.microsoft.com/3dmanufacturing/core/2015/02"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
UNIT_TO_MM = {
    "micron": 0.001,
    "millimeter": 1.0,
    "centimeter": 10.0,
    "inch": 25.4,
    "foot": 304.8,
    "meter": 1000.0,
}
IDENTITY = (1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def parse_transform(raw: str | None) -> tuple[float, ...]:
    if not raw:
        return IDENTITY
    parts = raw.replace(",", " ").split()
    if len(parts) != 12:
        raise ValueError(f"expected 12 transform values, found {len(parts)}")
    values = tuple(float(value) for value in parts)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("transform contains a non-finite value")
    return values


def apply_transform(point: tuple[float, float, float], matrix: tuple[float, ...]) -> tuple[float, float, float]:
    x, y, z = point
    return (
        x * matrix[0] + y * matrix[3] + z * matrix[6] + matrix[9],
        x * matrix[1] + y * matrix[4] + z * matrix[7] + matrix[10],
        x * matrix[2] + y * matrix[5] + z * matrix[8] + matrix[11],
    )


def combine_transform(first: tuple[float, ...], second: tuple[float, ...]) -> tuple[float, ...]:
    """Compose row-vector 3MF transforms: apply first, then second."""
    basis = [
        apply_transform((1.0, 0.0, 0.0), first),
        apply_transform((0.0, 1.0, 0.0), first),
        apply_transform((0.0, 0.0, 1.0), first),
        apply_transform((0.0, 0.0, 0.0), first),
    ]
    transformed = [apply_transform(point, second) for point in basis]
    origin = transformed[3]
    return (
        transformed[0][0] - origin[0],
        transformed[0][1] - origin[1],
        transformed[0][2] - origin[2],
        transformed[1][0] - origin[0],
        transformed[1][1] - origin[1],
        transformed[1][2] - origin[2],
        transformed[2][0] - origin[0],
        transformed[2][1] - origin[1],
        transformed[2][2] - origin[2],
        origin[0],
        origin[1],
        origin[2],
    )


def bounds_for_points(points: list[tuple[float, float, float]]) -> dict[str, list[float]] | None:
    if not points:
        return None
    minimum = [min(point[axis] for point in points) for axis in range(3)]
    maximum = [max(point[axis] for point in points) for axis in range(3)]
    return {
        "min": minimum,
        "max": maximum,
        "dimensions": [maximum[axis] - minimum[axis] for axis in range(3)],
    }


def transform_bounds(bounds: dict[str, list[float]], matrix: tuple[float, ...]) -> dict[str, list[float]]:
    minimum = bounds["min"]
    maximum = bounds["max"]
    corners = [
        apply_transform((x, y, z), matrix)
        for x in (minimum[0], maximum[0])
        for y in (minimum[1], maximum[1])
        for z in (minimum[2], maximum[2])
    ]
    result = bounds_for_points(corners)
    assert result is not None
    return result


def merge_bounds(items: list[dict[str, list[float]]]) -> dict[str, list[float]] | None:
    if not items:
        return None
    minimum = [min(item["min"][axis] for item in items) for axis in range(3)]
    maximum = [max(item["max"][axis] for item in items) for axis in range(3)]
    return {
        "min": minimum,
        "max": maximum,
        "dimensions": [maximum[axis] - minimum[axis] for axis in range(3)],
    }


def scale_bounds(bounds: dict[str, list[float]] | None, factor: float | None) -> dict[str, list[float]] | None:
    if bounds is None or factor is None:
        return None
    return {key: [value * factor for value in values] for key, values in bounds.items()}


def triangle_area_twice(
    a: tuple[float, float, float], b: tuple[float, float, float], c: tuple[float, float, float]
) -> float:
    ab = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
    ac = (c[0] - a[0], c[1] - a[1], c[2] - a[2])
    cross = (
        ab[1] * ac[2] - ab[2] * ac[1],
        ab[2] * ac[0] - ab[0] * ac[2],
        ab[0] * ac[1] - ab[1] * ac[0],
    )
    return math.sqrt(sum(component * component for component in cross))


def inspect_mesh(mesh: ET.Element) -> tuple[dict[str, Any], dict[str, list[float]] | None, list[str]]:
    diagnostics: list[str] = []
    vertices_element = next((item for item in mesh if local_name(item.tag) == "vertices"), None)
    triangles_element = next((item for item in mesh if local_name(item.tag) == "triangles"), None)
    vertices: list[tuple[float, float, float]] = []
    invalid_vertices = 0
    if vertices_element is not None:
        for vertex in vertices_element:
            if local_name(vertex.tag) != "vertex":
                continue
            try:
                point = tuple(float(vertex.attrib[axis]) for axis in ("x", "y", "z"))
                if len(point) != 3 or not all(math.isfinite(value) for value in point):
                    raise ValueError
                vertices.append(point)  # type: ignore[arg-type]
            except (KeyError, ValueError):
                invalid_vertices += 1
    triangles: list[tuple[int, int, int]] = []
    invalid_triangle_references = 0
    degenerate_triangles = 0
    edges: Counter[tuple[int, int]] = Counter()
    if triangles_element is not None:
        for triangle in triangles_element:
            if local_name(triangle.tag) != "triangle":
                continue
            try:
                indices = tuple(int(triangle.attrib[key]) for key in ("v1", "v2", "v3"))
            except (KeyError, ValueError):
                invalid_triangle_references += 1
                continue
            triangles.append(indices)  # type: ignore[arg-type]
            if any(index < 0 or index >= len(vertices) for index in indices):
                invalid_triangle_references += 1
                continue
            if len(set(indices)) < 3 or triangle_area_twice(
                vertices[indices[0]], vertices[indices[1]], vertices[indices[2]]
            ) <= 1e-12:
                degenerate_triangles += 1
            for start, end in ((indices[0], indices[1]), (indices[1], indices[2]), (indices[2], indices[0])):
                edges[tuple(sorted((start, end)))] += 1
    boundary_edges = sum(count == 1 for count in edges.values())
    nonmanifold_edges = sum(count > 2 for count in edges.values())
    topology_assessment = "not_assessed"
    if triangles and not invalid_triangle_references:
        topology_assessment = (
            "closed_two_manifold_by_edge_incidence"
            if boundary_edges == 0 and nonmanifold_edges == 0 and degenerate_triangles == 0
            else "topology_anomalies_detected"
        )
    if invalid_vertices:
        diagnostics.append(f"Found {invalid_vertices} invalid vertex records.")
    if invalid_triangle_references:
        diagnostics.append(f"Found {invalid_triangle_references} invalid triangle records or references.")
    return (
        {
            "vertex_count": len(vertices),
            "triangle_count": len(triangles),
            "invalid_vertex_records": invalid_vertices,
            "invalid_triangle_records_or_references": invalid_triangle_references,
            "degenerate_triangles": degenerate_triangles,
            "boundary_edges": boundary_edges,
            "nonmanifold_edges": nonmanifold_edges,
            "topology_assessment": topology_assessment,
            "topology_limitations": (
                "Edge incidence does not detect self-intersections, inverted shells, duplicate coplanar faces, "
                "geometric clearances, or physical printability."
            ),
        },
        bounds_for_points(vertices),
        diagnostics,
    )


def source_part_for_relationship_part(path: str) -> str:
    if path == "_rels/.rels":
        return ""
    marker = "/_rels/"
    if marker not in path or not path.endswith(".rels"):
        return ""
    prefix, name = path.split(marker, 1)
    return f"{prefix}/{name[:-5]}"


def resolve_relationship_target(rel_part: str, target: str) -> str:
    if target.startswith("/"):
        return posixpath.normpath(target.lstrip("/"))
    source = source_part_for_relationship_part(rel_part)
    return posixpath.normpath(posixpath.join(posixpath.dirname(source), target))


def inspect_relationships(archive_names: set[str], archive: Any) -> tuple[list[dict[str, Any]], list[str]]:
    relationships: list[dict[str, Any]] = []
    diagnostics: list[str] = []
    for rel_path in sorted(name for name in archive_names if name.endswith(".rels")):
        try:
            root = ET.fromstring(archive.read(rel_path))
        except ET.ParseError as exc:
            diagnostics.append(f"Cannot parse relationship part {rel_path}: {exc}")
            continue
        for element in root.iter():
            if local_name(element.tag) != "Relationship":
                continue
            target = element.attrib.get("Target")
            target_mode = element.attrib.get("TargetMode", "Internal")
            resolved = None
            exists = None
            if target and target_mode.lower() != "external":
                resolved = resolve_relationship_target(rel_path, target)
                exists = resolved in archive_names
                if not exists:
                    diagnostics.append(f"Relationship target is missing: {rel_path} -> {resolved}")
            relationships.append(
                {
                    "source_relationship_part": rel_path,
                    "id": element.attrib.get("Id"),
                    "type": element.attrib.get("Type"),
                    "target": target,
                    "target_mode": target_mode,
                    "resolved_target": resolved,
                    "target_exists": exists,
                }
            )
    return relationships, diagnostics


def inspect_model(payload: bytes, member: str) -> tuple[dict[str, Any], list[str]]:
    diagnostics: list[str] = []
    try:
        root = ET.fromstring(payload)
    except ET.ParseError as exc:
        raise ToolError("model_xml_error", f"Cannot parse 3MF model part {member}: {exc}") from exc
    if local_name(root.tag) != "model":
        raise ToolError("not_3mf_model", f"Part {member} does not have a 3MF model root element.")
    namespace = root.tag[1:].split("}", 1)[0] if root.tag.startswith("{") else None
    unit = root.attrib.get("unit", "millimeter")
    unit_factor = UNIT_TO_MM.get(unit)
    if unit_factor is None:
        diagnostics.append(f"Unknown 3MF unit {unit!r}; millimeter dimensions were not calculated.")
    metadata = [
        {"name": element.attrib.get("name"), "value": (element.text or "").strip()}
        for element in root
        if local_name(element.tag) == "metadata"
    ]
    resources = next((item for item in root if local_name(item.tag) == "resources"), None)
    object_elements = [] if resources is None else [item for item in resources if local_name(item.tag) == "object"]
    object_data: dict[str, dict[str, Any]] = {}
    raw_bounds: dict[str, dict[str, list[float]]] = {}
    components: dict[str, list[tuple[str, tuple[float, ...]]]] = {}
    for element in object_elements:
        object_id = element.attrib.get("id")
        if not object_id:
            diagnostics.append("Found an object without an id.")
            continue
        mesh = next((item for item in element if local_name(item.tag) == "mesh"), None)
        component_root = next((item for item in element if local_name(item.tag) == "components"), None)
        mesh_report = None
        if mesh is not None:
            mesh_report, bounds, mesh_diagnostics = inspect_mesh(mesh)
            diagnostics.extend(f"Object {object_id}: {message}" for message in mesh_diagnostics)
            if bounds is not None:
                raw_bounds[object_id] = bounds
        refs: list[tuple[str, tuple[float, ...]]] = []
        if component_root is not None:
            for component in component_root:
                if local_name(component.tag) != "component":
                    continue
                ref = component.attrib.get("objectid")
                if not ref:
                    diagnostics.append(f"Object {object_id} has a component without objectid.")
                    continue
                try:
                    transform = parse_transform(component.attrib.get("transform"))
                except ValueError as exc:
                    diagnostics.append(f"Object {object_id} component {ref} has invalid transform: {exc}")
                    continue
                refs.append((ref, transform))
            components[object_id] = refs
        object_data[object_id] = {
            "id": object_id,
            "name": element.attrib.get("name"),
            "type": element.attrib.get("type", "model"),
            "part_number": element.attrib.get("partnumber"),
            "representation": "mesh" if mesh is not None else "components" if component_root is not None else "unknown",
            "mesh": mesh_report,
            "component_count": len(refs),
        }

    resolving: set[str] = set()

    def resolve_bounds(object_id: str) -> dict[str, list[float]] | None:
        if object_id in raw_bounds:
            return raw_bounds[object_id]
        if object_id in resolving:
            diagnostics.append(f"Component cycle detected at object {object_id}.")
            return None
        resolving.add(object_id)
        child_bounds: list[dict[str, list[float]]] = []
        for ref, transform in components.get(object_id, []):
            if ref not in object_data:
                diagnostics.append(f"Object {object_id} references missing component object {ref}.")
                continue
            bounds = resolve_bounds(ref)
            if bounds is not None:
                child_bounds.append(transform_bounds(bounds, transform))
        resolving.remove(object_id)
        merged = merge_bounds(child_bounds)
        if merged is not None:
            raw_bounds[object_id] = merged
        return merged

    for object_id, data in object_data.items():
        bounds = resolve_bounds(object_id)
        data["bounds_in_model_units"] = bounds
        data["bounds_mm"] = scale_bounds(bounds, unit_factor)

    build = next((item for item in root if local_name(item.tag) == "build"), None)
    build_items: list[dict[str, Any]] = []
    placed_bounds: list[dict[str, list[float]]] = []
    if build is not None:
        for index, item in enumerate(build):
            if local_name(item.tag) != "item":
                continue
            object_id = item.attrib.get("objectid")
            report: dict[str, Any] = {"index": index, "object_id": object_id, "part_number": item.attrib.get("partnumber")}
            if not object_id or object_id not in object_data:
                report["valid_reference"] = False
                diagnostics.append(f"Build item {index} references missing object {object_id!r}.")
            else:
                report["valid_reference"] = True
                try:
                    transform = parse_transform(item.attrib.get("transform"))
                    report["transform"] = list(transform)
                    bounds = resolve_bounds(object_id)
                    if bounds is not None:
                        placed = transform_bounds(bounds, transform)
                        report["bounds_in_model_units"] = placed
                        report["bounds_mm"] = scale_bounds(placed, unit_factor)
                        placed_bounds.append(placed)
                except ValueError as exc:
                    diagnostics.append(f"Build item {index} has invalid transform: {exc}")
                    report["transform_error"] = str(exc)
            build_items.append(report)
    else:
        diagnostics.append("The model part has no build element.")
    overall = merge_bounds(placed_bounds)
    return (
        {
            "member": member,
            "namespace": namespace,
            "core_namespace_matches_2015_spec": namespace == CORE_NS,
            "unit": unit,
            "unit_to_mm": unit_factor,
            "metadata": metadata,
            "object_count": len(object_data),
            "objects": [object_data[key] for key in sorted(object_data, key=lambda value: (not value.isdigit(), value))],
            "build_item_count": len(build_items),
            "build_items": build_items,
            "overall_bounds_in_model_units": overall,
            "overall_bounds_mm": scale_bounds(overall, unit_factor),
        },
        diagnostics,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Inspect a 3MF ZIP package, metadata, objects, and mesh topology.")
    parser.add_argument("input", help="3MF project to inspect")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")
    return parser


def run(raw_path: str) -> dict[str, Any]:
    path = resolve_input(raw_path)
    if path.suffix.lower() != ".3mf":
        raise ToolError("unexpected_extension", "Expected a .3mf input file.")
    archive, inventory = open_checked_zip(path)
    try:
        names = set(archive.namelist())
        relationships, relationship_diagnostics = inspect_relationships(names, archive)
        root_relationships = [item for item in relationships if item["source_relationship_part"] == "_rels/.rels"]
        model_targets = [
            item["resolved_target"]
            for item in root_relationships
            if item["resolved_target"]
            and item["target_exists"]
            and (str(item.get("type", "")).lower().endswith("/3dmodel") or str(item["resolved_target"]).lower().endswith(".model"))
        ]
        if not model_targets:
            model_targets = sorted(name for name in names if name.lower().endswith(".model"))
        diagnostics = list(relationship_diagnostics)
        if "[Content_Types].xml" not in names:
            diagnostics.append("Missing required [Content_Types].xml package part.")
        if "_rels/.rels" not in names:
            diagnostics.append("Missing required root relationship part _rels/.rels.")
        if not model_targets:
            diagnostics.append("No readable 3MF .model part was found.")
        models: list[dict[str, Any]] = []
        for target in model_targets:
            model, model_diagnostics = inspect_model(archive.read(target), target)
            models.append(model)
            diagnostics.extend(model_diagnostics)
        metadata_candidates = sorted(
            name
            for name in names
            if not name.endswith("/")
            and (
                name.startswith("Metadata/")
                or PurePosixPath(name).suffix.lower() in {".config", ".json", ".xml"}
            )
            and name not in {"[Content_Types].xml"}
        )
        structural_failures = [
            message
            for message in diagnostics
            if message.startswith(("Missing required", "Relationship target is missing", "No readable", "Cannot parse"))
        ]
        result = success_envelope(TOOL_NAME, path)
        result.update(
            {
                "archive": {
                    "entry_count": len(inventory.entries),
                    "total_uncompressed_bytes": inventory.total_uncompressed_bytes,
                    "entries": inventory.entries,
                    "crc_validated": True,
                    "unsafe_entries": inventory.unsafe_entries,
                },
                "package": {
                    "content_types_present": "[Content_Types].xml" in names,
                    "root_relationships_present": "_rels/.rels" in names,
                    "relationships": relationships,
                    "model_targets": model_targets,
                    "metadata_or_settings_candidates": metadata_candidates,
                    "structure_valid": not structural_failures,
                },
                "models": models,
                "diagnostics": diagnostics,
                "claim_boundary": (
                    "This is a structural and limited topology inspection. It does not prove correct scale intent, "
                    "printer compatibility, collision freedom, slicer behavior, support removability, material suitability, "
                    "or physical printability. Inspect the sliced Preview and validate physically."
                ),
            }
        )
        return result
    finally:
        archive.close()


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
