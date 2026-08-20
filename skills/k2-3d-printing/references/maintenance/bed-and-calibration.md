# Bed, build plate, and calibration

Confirm the printer and installed plate physically. A profile or 3MF selection does not prove either one.

## Plate boundaries

| Model | Official plate evidence | Boundary | Sources |
|---|---|---|---|
| K2 | supplied flexible PEI spring-steel plate; bed maximum 100 °C | A separate double-sided frosted PEI accessory explicitly names K2/K2 Pro; do not infer other plates/models | [P003] [P009] |
| K2 Pro | flexible PEI plate; bed maximum 110 °C | Confirm exact surface/accessory before choosing cleaning agent or adhesive | [P010] [P011] |
| K2 Plus | flexible plate; bed maximum 120 °C | K2/K2 Pro accessory evidence does not establish K2 Plus fit | [P012] [P013] |
| K2 SE / K2 SE 4C | epoxy-resin plate; bed maximum 100 °C | Do not use PEI-specific claims without the installed plate's official page | [P015] [P016] |

Hardware maxima are not material recommendations. Use the exact filament TDS, confirmed plate, adhesive/separation-layer documentation, and a calibrated starting point inside every limit.

## Before each print

For confirmed base K2, inspect and clean the platform before every print. [P003]

1. Let the plate reach a handling-safe temperature.
2. Confirm plate type, orientation, seating, and absence of visible debris or coating damage.
3. Use only a cleaner approved by the exact plate manufacturer. The cited K2 sources provide no chemical cleaning recipe; do not invent alcohol concentration, detergent, abrasive, solvent, or adhesive guidance.
4. Confirm that the selected printer, nozzle, plate, filament, and process profile match physical hardware.
5. Inspect first-layer toolpaths in Preview, including islands, gaps, brim/raft, purge structures, and build-volume exclusions.
6. Supervise the first layer. A completed calibration or slice does not prove adhesion.

Stop and replace/escalate only through a confirmed official part path if the plate is cracked, deeply gouged, delaminating, unable to seat, contaminated by an unknown chemical, or physically incompatible. No base-K2 plate fastener torque was found.

## Calibration triggers

| Trigger | Conditional base-K2 action | Conflict/boundary | Validation | Sources |
|---|---|---|---|---|
| Every 300 cumulative print hours | Run input shaping and automatic leveling | Manual schedule | Both routines complete without error; supervised small test | [P003] |
| Monthly | Run input shaping with no filament loaded | Separate maintenance-page schedule differs from 300-hour manual | Record which trigger/source was used | [P027] |
| After K2/K2 Pro manual belt work | Run input shaping | Applies only after exact P030 procedure | Calibration passes without abnormal motion | [P030] |
| After an authorized firmware update | Retract filament before update; then run input shaping and automatic leveling | Update requires separate authorization and exact model/image verification | Record versions and calibration results; stop on error | [P021] |
| First-layer failure, bed service, collision, or repeated dimensional shift | Inspect/clean plate and run only model-supported calibration after diagnosing visible cause | Do not use calibration to conceal damaged hardware or wrong profile | First-layer test and relevant dimension acceptance pass | [P003] |

K2 Plus advertises active bed tilt, but the cited sources provide no maintenance/repair sequence for it. Do not transfer base-K2 leveling steps. They also provide no complete K2 SE/K2 SE 4C calibration procedure. [P012] [P013] [P015] [P016]

## First-layer diagnosis

1. Stop if the nozzle drags, collides, deposits a large blob, or the plate moves.
2. Record physical model, plate surface, installed nozzle, filament, selected profiles, first-layer Preview, commanded temperatures, and a close photo.
3. Confirm plate seating and visible cleanliness while cool. Do not introduce an unverified chemical.
4. Confirm that the model fits the correct build volume and that no first-layer islands or missing lines appear in Preview.
5. Run the exact model's normal automatic-leveling routine if due or after a relevant service event.
6. Re-slice only after confirming the physical printer/nozzle/plate/material. Change one calibrated variable at a time through the slicing workflow; do not exceed official hardware or material limits.
7. Validate with a small supervised first-layer test covering representative bed areas. Define acceptance before printing: continuous lines, intended contact, no dragging, no detached islands, and no plate movement.

Escalate when leveling cannot complete, the plate or bed is visibly damaged/loose, a sensor error repeats, the nozzle contacts the plate, the surface height changes mechanically, or a fastener/torque/bed-tilt repair is required but absent from a model-specific official source.

## Calibration evidence record

Record model identity evidence, firmware, plate, nozzle, filament removed/loaded state, source/revision, trigger, routine names exactly as shown, completion/error result, before/after observation, Preview state, test artifact, and residual uncertainty. Report `calibration completed` separately from `first layer physically validated`.
