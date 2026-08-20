# ABS and ASA

Use this file for ABS and ASA model material. Use [support materials](support-materials.md) for HIPS as a support pairing. Do not merge ABS, high-flow/reduced-warp ABS, ASA, and HIPS processing ranges.

## Decision boundary

- **Base-K2 evidence:** the official K2 page lists ABS but not ASA or HIPS. Apply this only after physical K2 confirmation. [M001]
- **Standard CFS official fact:** ABS, ASA, and HIPS are named medium-hardness examples. That is feed-path evidence, not print-process endorsement. [P024]
- **Enclosure is formulation-specific:** Creality's generic CR-ABS chart recommends enclosure/environment control, while the Hyper ABS product page advertises a reduced-shrink formulation that can print without one. Preserve the conflict. [M007, M016]
- **K2 Plus chamber values apply only to K2 Plus.** Do not assign its 60 °C guidance to K2 or an unconfirmed K2C. [M006]

## Selection frame

Consider the exact ABS grade for a functional or impact-oriented part only after its mechanical and thermal TDS meets the load/environment. Consider the exact ASA grade for outdoor/weathering use only when its current TDS supports the required UV, temperature, color, and mechanical exposure. HIPS may be either a model material or an ABS support candidate; verify the precise role and removal chemistry before slicing.

Do not claim heat resistance, UV life, impact strength, chemical resistance, low warp, or a safe indoor emissions level from the family name.

## Source-specific manufacturer ranges and conflicts

| Exact product/source | Nozzle | Bed / environment | Cooling | Published speed | Drying | Evidence boundary |
|---|---:|---|---|---|---|---|
| Creality CR-ABS generic chart | 220–260 °C | bed 90–110 °C; environment 50–80 °C | not resolved | 40–80 mm/s | not resolved | Enclosure recommended. Base-K2 bed cannot cover the full range. [M007] |
| Creality Hyper ABS | 230–270 °C | bed 75–95 °C | not resolved | product-specific | exact product document required | Product page advertises reduced shrinkage and no enclosure; do not transfer to other ABS. [M016] |
| Polymaker PolyLite ABS | 245–265 °C | bed 90–100 °C; ambient enclosure | fan off | 50–200 mm/s | 70 °C for 6 h | Exact product page. [M018] |
| Creality HP-ASA product page | 200–300 °C | bed 50–100 °C | not resolved | 40–300 mm/s | exact product document required | Product-page values conflict with Creality's generic chart. [M017] |
| Creality HP-ASA generic chart | 240–260 °C | bed 80–110 °C; environment 60–90 °C | not resolved | 30–60 mm/s | not resolved | Cannot be silently merged with product page; upper bed range exceeds base K2. [M007] |
| Polymaker PolyLite ASA | 230–260 °C | bed 75–95 °C; enclosure | fan off | 50–200 mm/s | 70 °C for 7 h | Exact product page. [M019] |
| BASF Ultrafuse HIPS v2.2 | 240–260 °C | bed 100–120 °C | exact TDS/profile | 40–80 mm/s; 0.4 mm or larger nozzle | 60 °C for 4–16 h | Base K2 reaches only the bottom bed point; not an official K2 material. [M020] |

### Conflict rule

For HP-ASA, request the actual spool label and current TDS before providing a numeric profile. Do not use the union 200–300 °C / 50–110 °C or select the convenient source. For Hyper ABS, describe “no enclosure” only as that product page's formulation claim, not as an ABS-family fact.

## Thermal and environment gate

1. Confirm the physical printer, its maximum bed/nozzle temperatures, whether the enclosure is passive, and whether any chamber value is actually controlled.
2. Confirm that the exact product's full required operating point—not merely one boundary—can be maintained without commanding a hardware maximum as a routine target.
3. Follow the exact grade's enclosure, chamber, door, and cooling instruction. If absent, mark each **Unvalidated** and use a small warp/layer-adhesion test.
4. Never improvise a heated chamber, block ventilation, or relocate electronics to achieve a material target.
5. Keep environmental control stable across calibration and final part. Record ambient/chamber observation method rather than assuming a setpoint equals actual temperature.

## Family-specific operating rules

Apply the [shared material card](recommendation-workflow.md#material-parameter-card) and [calibration workflow](../slicing/calibration.md), with these ABS/ASA-specific constraints:

- Use a representative flat/long coupon for shrinkage and edge lift and an intended-orientation coupon for layer adhesion; a small cube cannot validate a large enclosed part.
- Treat brim, mouse ears, orientation, and geometry relief as starting tools, not a warp guarantee; raft changes the bottom surface.
- The cited sources establish no K2-specific volumetric-flow limit.
- Keep fan off only for the cited PolyLite ABS and PolyLite ASA products; do not generalize it to bridges or other formulations. [M018, M019]

## CFS and support pairing

- Standard CFS names ABS, ASA, and HIPS as supported medium-hardness examples, subject to spool dimensions and condition. [P024]
- CFS status does not confirm the thermal process or the physical printer.
- Forward AM identifies HIPS as an ABS support option, but the cited HIPS bed range is 100–120 °C and the exact ABS/HIPS pair still needs an interface and removal test. [M020]
- PolyDissolve S1 rates ABS poorly and UltiMaker says its PVA is unsuitable with its ABS. Do not recommend those pairings as generic soluble support. [M030, M032]
- Ultrafuse BVOH names ABS and ABS Fusion+ among pairings. Treat this as product-specific; validate adhesion, purge contamination, Z/XY gaps, support entrapment, and dissolution/removal. [M033]

## Drying, storage, health, and post-processing

- Use 70 °C/6 h only for PolyLite ABS, 70 °C/7 h only for PolyLite ASA, and 60 °C/4–16 h only for Ultrafuse HIPS. [M018, M019, M020]
- Follow spool heat limits and dryer accuracy. Store sealed with desiccant as the exact product requires.
- Creality's HP-ASA product page recommends ventilation. NIOSH identifies material-extrusion particles/VOCs and recommends exposure controls; it specifically suggests choosing PLA instead of ABS when PLA meets the task. This reduces exposure potential but does not make PLA emission-free. [M017, M056, M057, M058, M059]
- Keep ABS/ASA/HIPS printing and solvent/post-processing emissions away from occupied breathing zones. Use source capture/exhaust and exact SDS controls. An unvented enclosure is not verified exposure control.
- Do not recommend acetone, limonene, or another solvent unless the exact filament/support procedure and solvent SDS establish the task. Never heat a solvent without an explicit applicable procedure.
- Any annealing, coating, painting, food contact, flame rating, or outdoor-life claim is **Unvalidated** without the exact product/finished-process document.

## Failure signatures

| Symptom | Plausible causes to separate | Next test | Stop condition |
|---|---|---|---|
| Corners lift or part bows | surface, first layer, bed, enclosure stability, geometry, cooling | representative flat coupon; change one factor | required bed/chamber exceeds confirmed limit |
| Layers split | low layer temperature, excessive cooling, unstable enclosure, flow, load orientation | oriented adhesion coupon inside exact range | part is safety-critical without mechanical validation |
| Strong odor or irritation | inadequate source control, temperature, exact additives | stop print, ventilate according to site plan, review SDS | symptoms persist or effective ventilation is unavailable |
| HIPS support detaches or fuses | incompatible pair, temperature, purge, interface/gap | small two-material interface coupon | removal requires an unverified solvent/process |
| Fine cracks after cooling | residual stress, geometry, enclosure transition, material condition | smaller geometry/orientation coupon | crack path affects required load or containment |
| High-speed under-extrusion | flow limit, temperature, partial obstruction | stepped flow test within range | clicking, grinding, thermal instability, or sustained flow loss |

## Family-specific release gate

Apply the [shared release decision](recommendation-workflow.md#make-the-release-decision). Also resolve the HP-ASA source conflict for the physical spool and confirm the exact enclosure/chamber, ventilation, occupancy, warp, and layer-adhesion conditions.
