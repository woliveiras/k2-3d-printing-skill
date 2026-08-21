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

1. Recheck model-, version-, and SKU-specific primary sources before using `latest`, `current`, `supported`, `compatible`, or `safe`, or before giving firmware, software, temperature, material, part, maintenance, or safety facts.
2. Follow [evidence and authority](references/evidence-and-authority.md) for source priority, claim classes, conflicts, freshness, and action gates. Use community material only to form a testable hypothesis.
3. For each new live source, report publisher, direct URL, source type, publication and access dates, applicability, supported claims, conflicts, confidence, and review date. Cite an existing record in [sources](references/sources.md) when one applies.

## Run the task workflow

1. Read [portable printer memory](references/printer-memory.md) when a request may reuse a printer alias, physical identity, installed setup, software version, or preference. Use stored facts only with their evidence and confirmation date. A newer physical observation overrides memory; memory never upgrades slicer configuration into physical proof.
2. When multiple printers are stored and the request is ambiguous, ask only which alias applies. Determine or infer the part's purpose, material, visible faces, desired finish, load and load direction, dimensional accuracy, time budget, installed nozzle, plate, support tolerance, and user experience. Ask only for missing facts that change the decision.
3. Inspect the source artifact before changing slicing parameters:
   - read [model inspection](references/model-inspection.md) for STL, STEP, 3MF, and G-code boundaries;
   - run `python3 scripts/inspect_3mf.py FILE.3mf` for a read-only 3MF structural and limited topology report;
   - run `python3 scripts/extract_creality_settings.py FILE` to inventory known embedded settings;
   - run `python3 scripts/compare_profiles.py LEFT RIGHT` to preserve typed differences and origins.
4. Check physical compatibility in this order: confirmed printer limits, installed hotend and nozzle, plate, enclosure/chamber behavior, CFS path, then the exact material TDS/SDS. Read the relevant file under [materials](references/materials/INDEX.md).
5. Choose the slicing objective and trade-offs from [slicing](references/slicing/INDEX.md). Classify consequential claims with the canonical [claim classes](references/evidence-and-authority.md#claim-classes).
6. Give Creality Print navigation only for an observed or sourced version and mode. Read [Creality Print](references/creality-print/INDEX.md). If a control is hidden, check version, interface mode, `Global` versus `Objects`, selection, prerequisites, search, and scroll state before declaring it absent.
7. Slice, then inspect Preview layer by layer using [Preview inspection](references/slicing/preview-inspection.md). Consult the active legend before interpreting color.
8. Calibrate only applicable factors in the order and stop criteria defined by [calibration](references/slicing/calibration.md).
9. Diagnose before changing multiple parameters. Use [failure diagnosis](references/slicing/failure-diagnosis.md) for print faults; for hardware or preventive work, load the [maintenance index](references/maintenance/INDEX.md), then the [troubleshooting trees](references/maintenance/troubleshooting-trees.md) when routing symptom-first.

## Separate completion states

Report every reached completion state separately:

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
6. Keep inspection scripts read-only and never overwrite an input. `scripts/printer_memory.py` is the only state writer: read memory automatically when relevant, create proposals without writing, ask whether a component change is temporary or permanent, wait for confirmed physical completion, show the exact diff, and apply it only after separate explicit approval. Never persist installation intent as installed state.

## Modify 3MF projects only when authorized

Preserve and hash the original, write a clearly named copy, change only authorized fields, re-inspect and compare both files, and report structural and physical-validation states separately. Never send the copy without separate authorization. Follow [authorized 3MF mutation](references/model-inspection.md#authorized-3mf-mutation) and [authority gates](references/evidence-and-authority.md#authority-gates).

## Load only required references

Read [design for FDM](references/design-for-fdm.md) when the task changes geometry, fit, joinery, support access, or ergonomic surfaces. For a domain not already routed above, start at the [reference index](references/INDEX.md) and load only the relevant file.

## Format the answer

Lead with the decision or blocker. Include only task-relevant identity evidence, claim classes, citations, Preview or stop checks, validation, residual uncertainty, and actions requiring separate authorization. For unstable claims, include source ID, applicability, and access date.
