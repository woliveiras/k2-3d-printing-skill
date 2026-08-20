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
| Complete material profile or print-readiness decision | [Recommendation workflow](recommendation-workflow.md) plus the exact family file |
| Walls, clearances, fits, holes, bridges, overhangs, inserts, splits, or curved shells | [Design for FDM](../design-for-fdm.md) |

## Claim and compatibility classification

Label consequential statements with the canonical [claim classes](../evidence-and-authority.md#claim-classes). Keep claim evidence separate from the material/hardware compatibility states below.

Classify material/hardware compatibility:

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
