# Model and project inspection

## Establish the artifact boundary

Preserve the original file and record its name, format, byte size, and hash before any authorized mutation. Treat model geometry, slicer settings, selected printer, and physical printer as separate evidence. Never execute G-code to inspect it.

## STL

1. Determine whether the STL is binary or ASCII and whether the importing application applied millimeters by convention; STL carries no normative unit.
2. Check imported dimensions against a known physical dimension before accepting scale.
3. Inspect triangle count, invalid indices, degenerate/duplicate faces, open boundaries, non-manifold edges, disconnected shells, inconsistent winding, self-intersections when the available geometry tool supports them, and zero-volume features.
4. Measure walls, holes, clearances, small details, contact area, overhangs, bridges, center of mass, and fit-critical surfaces against the confirmed nozzle, line width, layer height, material, orientation, and calibration.
5. Do not describe a repaired or closed mesh as physically printable until slicing, Preview, and a relevant physical test pass.

## STEP

1. Preserve the B-rep/parametric source as the authority for dimensions; do not replace it with an STL when editing is required.
2. Inspect units, bodies/components, open or invalid shells, suppressed features, mating interfaces, minimum radii/walls, assembly interference, and export tolerance.
3. Select tessellation tolerance deliberately when exporting for FDM. Verify that curves remain smooth enough without creating an unnecessarily large mesh.
4. Record the CAD kernel/tool and export settings. Re-import the mesh and compare bounding dimensions to the STEP source.

## 3MF

Run:

```bash
python3 scripts/inspect_3mf.py project.3mf
python3 scripts/extract_creality_settings.py project.3mf
```

Review ZIP validity and CRC, package content types, relationships and missing targets, model units, objects/components, build transforms, bounds, mesh edge-incidence indicators, metadata/settings candidates, embedded printer/process/filament profiles, plate count, and foreign-slicer evidence. Treat edge-incidence manifoldness as limited: it does not detect self-intersection, inverted or overlapping shells, clearances, strength, support access, or slicer behavior.

If the project came from another slicer or printer, reselect the confirmed printer/nozzle/plate/material and re-slice. A profile inside 3MF is not physical identity evidence.

## G-code

1. Treat G-code as machine instructions for a particular firmware/profile, not a portable model.
2. Inspect only as text unless the user separately authorizes a safe simulator. Never upload, stream, or execute it.
3. Identify generator/version comments, machine flavor, units/modes, temperature commands, bed/chamber commands, tool changes, motion bounds, extrusion modes, start/end macros, fan control, acceleration/flow limits, pauses, and unknown custom commands.
4. Reject direct reuse when the physical printer, firmware dialect, build volume, toolhead/nozzle, offsets, plate, material, or start/end macros differ or are unknown. Prefer re-slicing the source geometry.

## Pre-slice checklist

- Confirm unit, scale, dimensions, and fit inside the build volume including exclusions and purge structures.
- Check mesh/B-rep integrity, normals/winding where relevant, open surfaces, loose components, and minimum printable features.
- Check contact area, center of mass, tall-part stability, load orientation, visible faces, holes, mating clearances, interference, overhangs, bridges, and supports trapped in cavities.
- Check that supports do not damage the critical exterior face or become inaccessible.
- Confirm the physical nozzle, plate, filament product, and printer rather than trusting embedded selections.

## Preview checklist

Inspect the first layer, unsupported islands, suspended paths, missing walls, gap fill, seams, bridges, overhangs, support/interface, brim/raft, speeds, acceleration, volumetric flow, fan, temperatures, retractions, travels, possible collisions, tool/material changes, purge, total time, and filament. Use the active legend for each color view.

## Authorized 3MF mutation

1. Hash and preserve the original.
2. Write a new, explicit filename.
3. Change only authorized members or settings; preserve ZIP members and relationship targets.
4. Do not weaken hardware limits or inject printer-control commands.
5. Re-run inspection, extraction, and profile comparison.
6. Report `structure valid` separately from `Preview reviewed` and `physically validated`.
