---
name: k2-3d-printing
description: "Evidence-bounded FDM design, model inspection, material selection, Creality Print slicing, Preview review, calibration, troubleshooting, maintenance, and safe repair guidance. USE WHEN a task mentions Creality K2C, the Creality K2 family, Creality Print, STL, STEP, 3MF, G-code, FDM slicing, filament, CFS, orientation, supports, calibration, print failure, maintenance, or repair."
---

# K2 3D Printing

Resolve every relative reference and script path from the directory containing this `SKILL.md`.

## Establish the evidence boundary

1. Identify the physical printer before giving model-specific limits, compatibility, maintenance, or repair steps. Use this order:
   1. physical label and printed model number;
   2. the printer's `About` screen;
   3. official purchase document or product page tied to the unit;
   4. firmware identity shown by the unit;
   5. Creality Print profile;
   6. user-supplied photographs or screenshots.
2. Treat a slicer profile as configuration evidence, never proof of physical hardware. Distinguish K2, K2 Pro, K2 Plus, K2 SE, K1C, and any unverified `K2C` label.
3. If identity remains uncertain, stop only hardware-specific guidance. State the evidence, retain generic FDM guidance, and ask one objective question for the label or `About` screen.
4. Read [printer identity](references/printer-identity.md) before any K2-family hardware claim.

## Refresh unstable facts

1. Browse live primary sources before using `latest`, `current`, `supported`, `compatible`, or `safe`, or before giving firmware, software, temperature, material, part, or maintenance facts.
2. Prefer model-specific Creality manuals, Wiki pages, service instructions, firmware notes, official parts, the official Creality Print repository, and the exact filament manufacturer's TDS/SDS. Use occupational, electrical, and fire authorities for safety.
3. Use community material only to discover a hypothesis. Do not promote it to a hardware, material, UI, or safety authority.
4. Report every live material source with publisher, direct URL, source type, date, access timestamp, applicability, supported claims, limitations/conflicts, confidence, and review date. Cite an existing record in [sources](references/sources.md) when one applies.
5. Explain conflicts. Prefer the most specific and recent primary source, but preserve unresolved uncertainty.
6. Read [evidence and authority](references/evidence-and-authority.md) before researching, modifying a project, sending a print, or proposing a repair.

## Run the task workflow

1. Determine or infer the part's purpose, material, visible faces, desired finish, load and load direction, dimensional accuracy, time budget, installed nozzle, plate, support tolerance, and user experience. Ask only for missing facts that change the decision.
2. Inspect the source artifact before changing slicing parameters:
   - read [model inspection](references/model-inspection.md) for STL, STEP, 3MF, and G-code boundaries;
   - run `python3 scripts/inspect_3mf.py FILE.3mf` for a read-only 3MF structural and limited topology report;
   - run `python3 scripts/extract_creality_settings.py FILE` to inventory known embedded settings;
   - run `python3 scripts/compare_profiles.py LEFT RIGHT` to preserve typed differences and origins.
3. Check physical compatibility in this order: confirmed printer limits, installed hotend and nozzle, plate, enclosure/chamber behavior, CFS path, then the exact material TDS/SDS. Read the relevant file under [materials](references/materials/INDEX.md).
4. Choose the slicing objective and trade-offs from [slicing](references/slicing/INDEX.md). Treat every number as one of: official limit, manufacturer range, documented starting point, empirical adjustment, or unvalidated result.
5. Give Creality Print navigation only for an observed or sourced version and mode. Read [Creality Print](references/creality-print/INDEX.md). If a control is hidden, check version, interface mode, `Global` versus `Objects`, selection, prerequisites, search, and scroll state before declaring it absent.
6. Slice, then inspect Preview layer by layer using [Preview inspection](references/slicing/preview-inspection.md). Consult the active legend before interpreting color.
7. Calibrate proportionally: first layer; temperature; flow; pressure advance only when officially applicable; maximum volumetric flow; retraction/stringing; bridges/overhangs; dimensional tolerance; then vibration/input shaping only when officially supported.
8. Diagnose symptoms before changing multiple parameters. Use [failure diagnosis](references/slicing/failure-diagnosis.md) for print faults and [maintenance troubleshooting trees](references/maintenance/troubleshooting-trees.md) for hardware faults.

## Separate completion states

Report exactly one or more of these states without collapsing them:

- `Sliced`: toolpath generation completed.
- `Preview reviewed`: no apparent anomaly was found in the inspected views and legends; list what was not inspected.
- `Test print recommended`: uncertainty remains in fit, material, supports, surface, strength, or calibration.
- `Physically validated`: the stated printer, material batch, profile, orientation, and acceptance test were actually printed and measured.

Never infer physical success from a completed slice or a structurally valid 3MF.

## Protect safety and authority

1. Read [safety](references/safety.md) before material emissions, electrical, hot/moving-part, drying, solvent, domestic, overnight, or unattended-printing guidance.
2. Do not guarantee unattended printing. Distinguish active heating/motion from a completed print cooling in the machine.
3. Before maintenance, identify the model and procedure, stop motion, remove filament only as directed, power off, unplug, and cool unless an official step explicitly requires a controlled energized or heated state.
4. Do not invent torque, lubricant, part number, fastener position, connector, or service procedure. Stop at wiring, mains power, heaters, unknown sensors, inaccessible assemblies, or evidence conflicts and direct the user to official support.
5. Do not install or update Creality Print, update firmware, control the printer, send or start a print, or buy a part without separate authorization.
6. Keep scripts read-only by default. Never overwrite an input.

## Modify 3MF projects only when authorized

1. Record the original path and SHA-256.
2. Create a clearly named new file; never replace the original.
3. Change only the authorized fields and preserve unrelated archive members, types, units, and origins.
4. Re-run 3MF inspection and setting extraction; compare the original and copy.
5. Report structural validity and the remaining physical-printability boundary.
6. Do not send the resulting project to a printer without a separate authorization.

## Load only required references

Read [design for FDM](references/design-for-fdm.md) when the task changes geometry, fit, joinery, support access, or ergonomic surfaces. For a domain not already routed above, start at the [reference index](references/INDEX.md) and load only the relevant file.

## Format the answer

1. Lead with the decision or blocker.
2. State the confirmed physical model and evidence level, or state that hardware identity is unconfirmed.
3. Label each value as `official`, `manufacturer range`, `starting point`, `empirical adjustment`, or `unvalidated`.
4. Cite source IDs from `references/sources.md` with applicability and access date for unstable claims.
5. List Preview checks, stop criteria, validation test, and residual uncertainty.
6. State which actions require separate authorization.
