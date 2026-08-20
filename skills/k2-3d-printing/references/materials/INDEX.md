# Materials index

Use this directory to decide whether an exact filament can be fed, melted, deposited, adhered, cooled, and handled safely on the confirmed physical printer. Do not infer physical hardware from a Creality Print profile. If `K2C` is the only identity supplied, obtain the physical label or `About` screen before applying K2 limits.

## Load only what the task needs

| Material or question | Read |
|---|---|
| PLA, Hyper/high-speed PLA, PLA+, Tough/Pro, Matte, Silk, or foamed wood-look PLA | [PLA family](pla-family.md) |
| PETG, high-flow PETG, PET | [PETG and PET](petg-and-pet.md) |
| ABS, ASA, or HIPS used as a model material | [ABS and ASA](abs-and-asa.md); for HIPS pairing also read [support materials](support-materials.md) |
| TPU, TPE, or Shore hardness | [Flexible materials](flexible-materials.md) |
| PA6, PA12, CoPA, other nylon, or PC | [Nylon and polycarbonate](nylon-and-polycarbonate.md) |
| PLA-CF, PETG-CF, PET-CF, PA-CF, PA-GF, particle-filled wood/metal PLA, PP/PP-GF, PPA, PAHT, PPS, PPSU, or PEI | [Composites and high-temperature materials](composites.md) |
| PVA, BVOH, HIPS support, or main/support pairing | [Support materials](support-materials.md) |
| Base-K2 comparison or CFS classification | [Compatibility matrix](compatibility-matrix.md) |
| Walls, clearances, fits, holes, bridges, overhangs, inserts, splits, or curved shells | [Design for FDM](../design-for-fdm.md) |

## Evidence and classification

Label every consequential statement:

- **Official**: the exact printer/CFS/manual explicitly states it.
- **Manufacturer range**: the exact filament SKU's TDS, SDS, or product document states it.
- **Starting point**: a selected value inside all confirmed limits for a named calibration.
- **Empirical adjustment**: a measured result for a recorded printer, nozzle, plate, filament lot, and test.
- **Inference**: a conclusion produced by comparing separate sources; show the comparison.
- **Unvalidated**: no exact official statement or physical test supports it.

Classify material/hardware compatibility separately:

1. **Officially supported**: the exact physical printer source names the material or exact grade.
2. **Conditional**: official or manufacturer evidence permits it only with a named nozzle, hotend, bed, chamber, surface, dry-feed system, or other condition.
3. **Not validated**: the ranges may appear to fit, but the confirmed printer is not officially listed or the exact grade is unknown.
4. **Not recommended**: a primary source warns against the combination, or required conditions cannot be reproduced reliably.
5. **Incompatible**: a minimum required temperature, geometry, feed-path property, or safety condition exceeds the confirmed hardware.

Do not collapse the following independent checks:

    physical printer
      -> hotend and temperature limit
      -> nozzle diameter and material
      -> bed temperature and surface
      -> passive enclosure or controlled heated chamber
      -> CFS model and feed path
      -> exact filament TDS/SDS
      -> sliced limits and Preview
      -> physical calibration and acceptance test

CFS feed-path compatibility never proves hotend, bed, chamber, support-pairing, or physical-print compatibility.

## Required material parameter card

When giving a material recommendation, fill every row below. Write **not stated by the cited manufacturer** or **unvalidated** instead of inventing a value.

| Field | Required content |
|---|---|
| Identity | Manufacturer, exact product/grade, diameter, lot or revision when visible, and source IDs |
| Compatibility | One of the five classes above for printer, hotend, nozzle, plate, chamber/enclosure, and CFS separately |
| Properties | Mechanical, thermal, chemical, flexibility, moisture, and visual traits supported for the exact grade |
| Suitable uses | Load, environment, appearance, fatigue, flexibility, support, or prototype purpose |
| Limitations | Creep, brittleness, UV/weathering, chemical limits, warp, layer adhesion, finish, or certification boundaries |
| Nozzle temperature | Manufacturer range; never a family-wide range |
| Bed and chamber | Manufacturer range and named surface; distinguish passive enclosure from controlled chamber |
| Door/lid state | Exact official instruction, or **unvalidated**; never transfer K2 Plus chamber guidance to another K2-family model |
| Cooling | Exact fan range/state, or a calibration instruction |
| Speeds | First layer, outer wall, inner wall/infill, bridges, and overhangs; if only a global manufacturer range exists, preserve it and derive each feature speed through calibration |
| Motion | Acceleration and jerk/smoothing only when the exact profile/source states them; otherwise calibrate ringing and adhesion |
| Flow | Manufacturer maximum volumetric speed only when published for the named product and hardware context; otherwise measure |
| Retraction | Exact printer/profile value or a low-risk stringing calibration; never copy generic Bowden values to direct drive |
| Geometry | Layer height, line width, nozzle diameter, wall count, and infill chosen from feature size and load path |
| Surface | Exact plate and any adhesive or release layer; follow the plate/material manufacturer |
| Stability | Shrinkage, warping, delamination, first-layer and tall/flat-part risks |
| Moisture | Exact drying temperature/time/method, spool temperature limit, dry-feed need, and storage |
| Multi-material | Standard CFS versus CFS-C status; primary/support adhesion, purge, interface, and dissolution/removal test |
| Abrasion | Filler, required nozzle/drive-gear material, minimum diameter, and post-processing dust controls |
| Health | Exact SDS plus ventilation, particles/VOCs, skin/eye, solvent, and post-processing controls |
| Calibration | First layer, temperature, flow, maximum volumetric flow, retraction, bridge/overhang, and dimensional coupons as applicable |
| Post-processing | Annealing, conditioning, sanding, solvent, insert, machining, or coating only under an applicable procedure |
| Failure signs | Observable symptom, plausible mechanism, one-variable test, and stop criterion |
| After-use care | Purge/cleaning, plate cleaning, nozzle/gear inspection, dry storage, and contamination checks |
| Validation state | Sliced, Preview reviewed, test print recommended, or physically validated |

## Selecting starting values

1. Confirm the physical printer and installed nozzle/plate.
2. Identify the exact filament and retrieve its current TDS and SDS. If only a generic manufacturer chart exists, say so.
3. Intersect the manufacturer range with confirmed hardware limits. Do not use the printer maximum as a target.
4. Reject the workflow if the filament's minimum requirement exceeds a confirmed limit.
5. Select a conservative point inside the exact range for a small calibration object. Label it **Starting point**, not **Official default**.
6. Calibrate in this order: first layer; temperature; flow ratio; pressure advance only when officially applicable; maximum volumetric flow; retraction/stringing; bridges/overhangs; dimensional fit.
7. Change one causal group at a time and record filament lot, dryness, nozzle, plate, chamber/door state, ambient conditions, and result.
8. Re-slice and inspect first layer, temperatures, fan, feature speeds, volumetric flow, support interface, purge, and material changes in Preview.

## Shared speed, flow, and geometry rules

- A product-page speed maximum is a tested or marketed ceiling under unspecified or named conditions, not an outer-wall starting speed.
- If only one speed range is published, keep feature speeds unvalidated. Tune maximum volumetric flow first, then choose slower outer walls and bridges only as an explicit heuristic tied to an acceptance test.
- Do not set acceleration from a filament family name. Reduce it only to address a measured ringing, adhesion, tall-part, flexible-feed, or flow limit.
- Choose layer height and line width from the installed nozzle, required detail, material flow, and [design rules](../design-for-fdm.md). Confirm that thin walls appear in Preview.
- Choose walls from the load path and infill from internal support/buckling needs. A percentage alone does not establish strength.
- Retraction follows the actual direct/Bowden path, material elasticity, temperature, and travel. Calibrate after temperature and flow.

## Drying and storage rules

- Use the exact product document. Drying requirements vary from no drying as supplied to long drying with dry feed.
- Obey the lowest safe temperature among filament TDS, spool/container, dryer, and official device limits.
- Do not rely on an unverified household oven. Temperature overshoot can soften a spool or filament; use a controlled dryer and an independent thermometer where the manufacturer instructs it. [M046, M047]
- Return hygroscopic filament to a sealed container with suitable desiccant. Record whether the material was printed from a dry box.
- Dryness changes flow and failure diagnosis. Re-dry or compare against a known-dry sample before compensating moisture symptoms with retraction or temperature.

## Safety boundary

Read [safety](../safety.md) before emissions, drying, solvent, post-processing, domestic, overnight, or unattended-use guidance. No thermoplastic family is universally emission-free; use the exact SDS and process-specific exposure controls. [M056, M057, M058, M059, M060, M061, M062]

## Release decision

Complete the required material card, run the [canonical Preview inspection](../slicing/preview-inspection.md), and report the completion state defined in [SKILL.md](../../SKILL.md#separate-completion-states). Apply the selected family file's additional release gate; a completed slice is never physical validation.
