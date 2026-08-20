# PLA family

Use this file for plain PLA, Hyper/high-speed PLA, PLA+, Tough/Pro, Matte, Silk, foamed wood-look PLA, and genuinely particle-filled wood PLA. These names do not define standardized chemistry or performance. Identify the exact product before assigning temperature, speed, toughness, drying, or nozzle requirements.

## Decision boundary

- **Base-K2 evidence:** the official K2 page lists PLA and PLA-CF. Apply this only after physical K2 confirmation; it does not endorse every PLA derivative. [M001]
- **Standard CFS official fact:** PLA is a supported medium-hardness example. Exact spool dimensions and physical condition still govern. The cited CFS sources do not specifically approve real wood-filled, foaming, very brittle, or heavily filled PLA. [P024, M003]
- **CFS-C:** use its separate matrix; never transfer a CFS-C result to standard CFS. [M004]
- **K2C:** if this is the only identity supplied, stop model-specific limits until a rating label or `About` screen establishes the physical model.

## Choose the subtype by purpose

| Subtype | Reason to consider it | Do not assume |
|---|---|---|
| Plain PLA | Visual prototypes, fit checks, low-warp starting material | Outdoor durability, high heat resistance, impact performance, or certification |
| Hyper/high-speed PLA | Higher throughput after flow calibration | The product-page maximum is attainable for every feature or hotend |
| PLA+ / Tough / Pro | A vendor-specific balance of impact, stiffness, or speed | A standardized formulation or interchangeability between brands/revisions |
| Matte | Diffuse visual finish and reduced layer-line contrast | Equal layer adhesion, strength, or flow to plain PLA |
| Silk | Reflective/decorative surfaces | Structural equivalence to plain PLA or a universal temperature for gloss |
| Foamed wood-look PLA | Wood-like appearance without particles when the exact TDS says so | Actual wood content or the same density/flow as standard PLA |
| Particle-filled wood PLA | Texture and finishing potential | Non-abrasiveness, 0.4 mm nozzle compatibility, CFS compatibility, or plain-PLA strength |

Treat each row as a selection hypothesis until the exact TDS and an application-specific coupon confirm it.

## Source-specific manufacturer ranges

| Exact product or source class | Nozzle | Bed | Cooling | Published speed/flow | Drying | Evidence |
|---|---:|---:|---|---|---|---|
| Creality Hyper PLA | 190–230 °C | 25–60 °C | 100% fan | 30–600 mm/s | not stated in the cited product page | Manufacturer product values; 600 mm/s is a marketed ceiling, not an outer-wall start. [M008] |
| Creality CR-PLA / CR-Matte generic chart | 190–230 °C | unheated–60 °C | not resolved for every SKU | 40–100 mm/s; chart recommendation 200/50 °C and 50 mm/s | not resolved | Manufacturer chart, not an exact TDS. [M007] |
| Creality CR-Silk generic chart | 190–230 °C | 50–60 °C | not resolved | 40–80 mm/s | not resolved | Manufacturer chart; do not treat a speed as a gloss guarantee. [M007] |
| Creality CR-Wood generic chart | 190–230 °C | unheated–60 °C | not resolved | 40–100 mm/s | not resolved | Filler size, minimum nozzle, abrasion, and CFS status are absent. [M007] |
| Polymaker PLA Pro v6.0, 2026-01-30 | 210–230 °C | use the exact v6 document/profile | use exact document/profile | up to 300 mm/s | 55 °C for 6 h when moisture was absorbed | Exact revision evidence. [M009] |
| Older PolyLite PLA Pro page | 190–220 °C | 30–60 °C | fan on | 30–70 mm/s; 15 mm³/s maximum volumetric speed | use exact revision | Conflicts with v6.0; do not merge ranges. [M010] |
| Polymaker PolyWood PLA v2.0, 2026-06-08 | 190–210 °C | 25–60 °C | fan on | 50–100 mm/s | 55 °C for 6 h | Foamed PLA with no wood powder; cannot characterize other “wood” filament. [M011] |
| BASF Ultrafuse PLA v4.4 | 210–230 °C | 50–70 °C | exact TDS/profile | 40–80 mm/s; 0.4 mm or larger nozzle | drying not necessary as supplied under its documented condition | Demonstrates that automatic drying is not a family-wide rule. [M065] |

When the spool label and an older web page disagree, pause the numeric recommendation and obtain the current exact TDS. Do not average or union the ranges.

## Build the operational parameter card

### Temperature, bed, enclosure, and cooling

1. Intersect the exact product range with confirmed hardware limits.
2. Select a small temperature-tower range inside that intersection. Record the selected values as **Starting point**.
3. Calibrate the first layer on the exact plate before changing bed temperature to solve later-layer defects.
4. Use the exact cooling instruction when published. If only “fan on” is known, fan percentage and bridge behavior remain **Unvalidated** until a cooling/overhang coupon.
5. Do not infer a K2 door/lid position from the K2 Plus chamber page. Door state is **Unvalidated** unless the confirmed printer and exact material source specify it.

### Feature speeds, acceleration, and volumetric flow

- The tables publish global speed ranges, not verified first-layer, outer-wall, inner-wall, infill, bridge, or overhang speeds.
- Start below the exact product ceiling, calibrate maximum volumetric flow, then choose feature speeds that remain below measured flow. Label them **Starting point**.
- Keep the first layer slow enough to observe continuous placement and adhesion, but do not invent a numeric value without an exact profile/test.
- The 15 mm³/s volumetric-flow value belongs only to the PolyLite PLA Pro source M010; do not assign it to Hyper PLA, v6 PLA Pro, Matte, Silk, or Wood.
- Acceleration remains **Unvalidated** until a ringing/tall-feature coupon. A filament name does not establish motion limits.

### Retraction, layer geometry, walls, and infill

- Calibrate retraction after temperature and flow on the actual direct-drive or Bowden path. The cited PLA sources establish no universal K2 retraction value.
- Choose layer height and line width from nozzle diameter and required detail; confirm every thin wall in Preview.
- Use whole generated line widths for shells. Put walls along the load path; use infill for internal support and buckling resistance. Neither a wall count nor an infill percentage is universal.
- For a visual part, test seam position, layer height, cooling, outer-wall speed, and orientation on a representative curve or corner rather than on an unrelated cube.

## Wood and filled-PLA gate

First determine whether “wood” is:

- a color/texture name;
- a foamed PLA without particles, such as cited PolyWood v2; or
- a genuinely particle-filled composite.

Prusa's manufacturer guidance says real wood/metal particle-filled products can clog more easily, may have weaker layer adhesion, and can be brittle in multi-material paths. It suggests at least a 0.6 mm nozzle and 0.2 mm layer height for wood products with large particles; metal-filled material is abrasive and requires hardened tooling. These are source-specific starting points, not universal requirements. [M012]

For any real filled PLA:

1. Require filler type, particle-size/nozzle statement, and current TDS/SDS.
2. Confirm nozzle material and minimum diameter.
3. Keep standard CFS status **Not validated** unless the exact product is approved.
4. Control dust during sanding, cutting, or drilling.
5. Purge according to an applicable manufacturer procedure and inspect nozzle/drive wear after use; do not invent a purge temperature or amount.

## Surface, supports, storage, and post-processing

- Use the exact plate maker's surface and release-layer instructions. Do not prescribe a universal adhesive.
- For soluble support, validate interface adhesion and contamination on a coupon. PolyDissolve S1 and UltiMaker PVA documents name PLA among compatible pairings, and Ultrafuse BVOH names PLA, but none guarantees every PLA formulation or CFS result. [M030, M031, M032, M033]
- Store sealed with suitable desiccant when the product requires it. Re-dry only at the exact product/spool-safe condition.
- Annealing, solvent smoothing, coating, and food-contact use are **Unvalidated** unless the exact product document and finished-process certification cover them. Annealing can alter dimensions; measure a coupon before a fit-critical part.

## Failure signatures and one-variable tests

| Observable symptom | Plausible causes to separate | Next test | Stop condition |
|---|---|---|---|
| First layer beads, gaps, or detaches | plate contamination, Z/mesh error, temperature, flow, wet filament | clean by plate procedure; run first-layer coupon at one verified temperature | temperature or bed command would exceed confirmed limit |
| Brittle line or snapping in CFS | brittle formulation, real filler, aging, path curvature | unload without forcing; inspect exact product and CFS approval | filament fractures in tube or requires dismantling without an official procedure |
| Gloss/matte inconsistency | temperature, outer-wall speed, cooling, flow | small finish coupon varying one factor | user expects a guaranteed color/finish without a physical sample |
| Stringing | temperature, moisture, flow, travel/retraction | known-dry comparison, then temperature, then retraction | retraction change risks grinding or contradicts exact profile |
| Missing fine wall | feature below generated line, flow or mesh issue | inspect Preview and test larger whole-line-width wall | slicer still omits the required structural feature |
| Wood/fill clogging | particle/nozzle mismatch, heat, contamination | stop; cool safely; confirm minimum nozzle and official cleaning procedure | torque, disassembly, or hot-pull method is unconfirmed |

## Release checklist

- Exact PLA product and revision identified.
- Physical printer, nozzle material/diameter, plate, and CFS variant confirmed.
- Every number labeled manufacturer range, starting point, or empirical result.
- First layer, temperature, flow, maximum volumetric flow, stringing, surface finish, bridge/overhang, and fit tests selected proportionally.
- Preview inspected for thin walls, seam, volumetric flow, cooling, unsupported paths, support contact, and actual material assignment.
- Final state reported as sliced, Preview reviewed, test print recommended, or physically validated.
