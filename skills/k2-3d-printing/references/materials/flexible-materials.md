# Flexible materials

Use this file for TPU and other TPE filaments. TPU is a TPE subtype; TPE is not one printable chemistry. Identify the exact product and Shore scale before selecting a profile.

## Decision boundary

- **Base-K2 evidence:** the official K2 material list does not name TPU/TPE. Temperature fit or a direct-drive extruder is not official compatibility. [M001]
- **Standard CFS:** the official compatibility page disallows TPU and other elastic filament. Do not route flexible filament through standard CFS. [P024, M003]
- **CFS-C:** its separate table marks TPU unavailable. Do not transfer any future CFS-C result to standard CFS. [M004]
- Keep printer compatibility **Not validated** until the exact physical model and an applicable official source are confirmed.

## Interpret Shore hardness correctly

- Compare values only on the same Shore scale and under comparable test conditions.
- Within Shore A, a lower number is generally softer; Shore 64D is not equivalent to 64A and is not numerically comparable.
- Printed-part flexibility also depends on wall count, infill, geometry, layer direction, temperature, and strain rate. Spool hardness cannot predict the finished spring force by itself.
- If a user says only “TPU,” ask for brand, exact product, Shore value and scale, diameter, and whether it must pass through CFS.

## Source-specific manufacturer ranges

| Exact product/source | Hardness | Nozzle | Bed/chamber | Cooling | Published speed | Drying/path |
|---|---:|---:|---|---|---|---|
| Creality CR-TPU generic chart | not stated | 210–240 °C | 50 °C; chamber not resolved | not resolved | 10–50 mm/s | direct drive recommended; exact drying not resolved. [M007] |
| Creality HP-TPU generic chart | not stated | 200–220 °C | unheated–60 °C; chamber not resolved | not resolved | 30–120 mm/s | exact path/drying requires product document. [M007] |
| Polymaker PolyFlex TPU95 | Shore 95A | 210–230 °C | 25–60 °C; no enclosure | fan on | 30–50 mm/s | dry 70 °C for 8 h; direct drive recommended. [M021] |
| BASF Ultrafuse TPU 85A, document content v3.0 | Shore 85A | 200–220 °C | 40 °C; no chamber | exact profile | 15–40 mm/s; 0.4 mm or larger | dry 70 °C for at least 5 h; filename/document revision mismatch. [M022] |
| BASF Ultrafuse TPU 64D, filename v1.1/document v2.0 | Shore 64D | 230–255 °C | 40–60 °C | exact profile | 30–60 mm/s; 0.4 mm or larger | dry 70 °C for at least 5 h; preserve the filename/document revision mismatch. [M023] |

These ranges demonstrate that “flexible” does not select one temperature or speed. Keep CR-TPU and HP-TPU generic-chart data below an exact TDS in authority.

## Feed-path gate

1. Bypass CFS; load through only the printer's officially supported direct path.
2. Confirm direct-drive compatibility for the physical printer, a constrained filament path, and the exact filament diameter.
3. Minimize unsupported path length and sharp bends. Do not modify guides, cutters, sensors, or extruder tension without an official model-specific procedure.
4. Feed slowly and stop at buckling, folding, grinding, repeated slip, or unexpected resistance.
5. Do not force filament through a blocked path or dismantle CFS/extruder without the applicable maintenance procedure.

## Operational parameter card

### Temperature, first layer, bed, and cooling

- Select a temperature inside the exact product range and validate flow at low speed before increasing throughput.
- Calibrate the first layer on the exact plate; a flexible filament can deform under excessive squish, so assess line continuity and final part dimensions rather than copying a PLA Z setting.
- Use the named bed range and surface instructions from the exact product/plate. Do not prescribe a universal adhesive or release layer.
- Preserve “no enclosure” only for PolyFlex TPU95 and Ultrafuse TPU 85A. Door/lid state for K2 or unconfirmed K2C remains **Unvalidated**. [M021, M022]
- “Fan on” for PolyFlex TPU95 does not establish a percentage. Tune bridge/overhang cooling on a coupon.

### Feature speed, acceleration, flow, and retraction

- Begin within the exact global speed range, at its conservative end for initial feed validation. This is a **Starting point**, not a universal TPU speed.
- Keep the first layer, outer wall, inner/infill, bridge, and overhang speeds **Unvalidated** until a representative coupon; the researched sources publish only global ranges.
- Measure maximum volumetric flow. None of the cited TPU sources gives a K2-specific volumetric limit.
- Reduce acceleration only when a measured feed, ringing, corner, or tall-part result requires it. Avoid rapid pressure reversals on a very soft filament.
- Start with minimal necessary retraction and tune only after drying, temperature, and flow. Large/frequent retractions can buckle or grind flexible filament; no universal direct-drive value was found.

### Layer geometry, walls, infill, and part stiffness

- Choose layer height and line width from nozzle/profile capability and confirm thin walls in Preview.
- Use wall count and geometry as intentional spring elements. More walls, thicker sections, short spans, and dense infill generally reduce flexibility, but quantify the finished part with a deflection or fit test.
- Orient layers so repeated bending does not peel them apart. Test at the intended strain, temperature, and cycle count.
- For a seal, grip, foot, wearable, or snap feature, validate contact pressure, compression set, surface texture, and skin/chemical requirements from the exact grade; do not infer them from Shore hardness.

## Supports and multi-material

- PolyDissolve S1 names TPU as a compatible primary material in its product matrix. BASF TPU 85A/64D documents name BVOH and HIPS support compatibility. These are product-specific pairings, not universal TPU support guarantees. [M030, M022, M023]
- Because standard CFS disallows TPU, a pairing may require an officially supported independent tool path; do not promise multi-material operation from chemical compatibility alone.
- Validate primary/support adhesion, purge contamination, interface density, Z/XY gaps, support access, and removal on a small coupon.
- Prefer orientation or a model split that avoids support on a flexible sealing or visible surface.

## Drying, storage, health, and maintenance

- Apply 70 °C/8 h only to PolyFlex TPU95 and 70 °C/at least 5 h only to the cited Ultrafuse products. Confirm spool temperature limit and current TDS. [M021, M022, M023]
- Store sealed with suitable desiccant and print from a dry path when the exact product requires it. Compare against a known-dry sample before increasing retraction for bubbles/stringing.
- Consult the exact SDS and provide source ventilation. Material, additives, color, and temperature change particle/VOC emissions. [M056, M057, M059, M060]
- After printing, unload without stretching or snapping filament into the path, inspect drive gears for chewed material, clean the plate by its manufacturer procedure, and reseal the spool. Do not invent extruder-tension settings.

## Failure signatures

| Symptom | Separate these causes | One-variable test | Stop when |
|---|---|---|---|
| Filament coils or jams before gears/hotend | CFS use, unsupported path, resistance, excessive feed/retraction | unload; use confirmed direct path at low speed | filament enters inaccessible path or official recovery procedure is absent |
| Grinding or repeated slip | extruder tension/path, excessive speed/flow, low temperature | low-speed extrusion inside range | continued feed damages filament or gears |
| Under-extrusion at corners/infill | flow ceiling, elastic compression, acceleration, partial obstruction | stepped low-speed/flow test | thermal instability, clicking, or blockage |
| Stringing/bubbles | moisture, temperature, retraction | exact drying then temperature test | drying condition/spool limit is unknown |
| Part too stiff or too soft | Shore grade, walls, infill, geometry, orientation | representative flex coupon | requested behavior lacks measurable acceptance criteria |
| Poor bridges/overhangs | cooling, speed, flow, sag under self-weight | small feature coupon | critical geometry remains unsupported |
| Weak repeated bend | layer orientation, strain concentration, material grade | cyclic coupon in intended orientation | failure could create a safety hazard without qualified testing |

## Release checklist

- Exact product and Shore scale confirmed.
- Physical printer's direct flexible-filament path officially confirmed; CFS bypassed.
- TDS/SDS, nozzle, plate, drying, and storage recorded.
- First layer, temperature, flow, retraction, bridge/overhang, dimensional fit, and finished-flex response tested proportionally.
- Preview checked for speeds, flow, retractions, unsupported paths, support interface, and thin flexible walls.
- Result labeled test print or physically validated for a measurable flex requirement; never guaranteed from Shore hardness alone.
