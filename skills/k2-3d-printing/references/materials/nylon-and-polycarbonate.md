# Nylon and polycarbonate

Use this file for PA6, PA12, PA6/6,6 blends such as CoPA, other polyamides, and PC. Use [composites](composites.md) for CF/GF reinforcement and high-temperature PPA/PAHT grades.

## Decision boundary

- The official K2 material list cited by M001 does not name nylon/PA or PC. A temperature range that fits is only an inference, not official compatibility.
- The cited sources include no exact unfilled PA6 or PA12 TDS. Do not derive their profiles from PA6-CF, PA12-CF, glass-reinforced PA, or CoPA.
- Standard CFS marketing lists PA-CF broadly, while the more specific CFS wiki warns that hard/brittle PPA-CF and PPS-CF can break in its tube. Resolve the exact SKU and physical brittleness; do not infer all nylon or PA-CF is accepted. [P024, M003]
- PC products in the evidence require radically different bed/chamber conditions. “PC” alone is insufficient to decide compatibility.

## Selection frame

Use the exact TDS to establish:

- moisture sensitivity and whether dry feeding is mandatory;
- tensile/impact/fatigue behavior before choosing a load-bearing PA;
- heat, chemical, creep, UV, and conditioning requirements;
- transparency/finish for PC;
- reinforcement, abrasion, annealing, and dimensional change.

Treat gears, bearings, clips, enclosures, high-temperature parts, and structural components as candidate applications only after the exact grade and a representative mechanical/thermal test meet the acceptance criteria.

## Source-specific manufacturer ranges

| Exact product | Polymer/fill | Nozzle | Bed/chamber | Cooling/speed | Drying and post-process | Evidence boundary |
|---|---|---:|---|---|---|---|
| Polymaker CoPA | PA6/PA6,6 blend | 250–270 °C | bed 25–50 °C | fan off; 50–200 mm/s | dry 100 °C for 8 h; anneal 80 °C for 6 h under its procedure | All-metal hotend. Page table says closure needed while FAQ says no enclosure; unresolved conflict. [M024] |
| Polymaker Fiberon PA6-CF20 | PA6, 20% CF | 280–300 °C | bed 40–50 °C; product-specific low ambient/bed condition | fan off; 30–300 mm/s | heated dry feed throughout; anneal 100 °C for 16 h | Hardened nozzle/all-metal hotend. Warp-Free behavior is product-specific. [M025] |
| Polymaker Fiberon PA12-CF10 | PA12, 10% CF | 280–300 °C | bed 40–50 °C | fan off; 30–300 mm/s | dry feed throughout; anneal 100 °C for 16 h | Hardened nozzle/all-metal hotend. Lower moisture sensitivity relative to cited PA6-CF is not moisture immunity. [M026] |
| BASF Ultrafuse PA v3.1 | glass-reinforced PA | 220–250 °C | bed 90–120 °C; passive closed chamber | 30–60 mm/s | dry 80 °C for at least 40 h | Abrasive; hardened nozzle/drive wheels advised. Base K2 cannot cover the full bed range. [M027] |
| Creality Hyper PC | proprietary PC product | 240–260 °C | bed 50–80 °C; no chamber claim established | 30–300 mm/s | exact current product document required | PEI/carbon-crystal surface listed; no K2 endorsement. [M028] |
| Polymaker PolyMax PC | proprietary PC product | 250–270 °C | bed 90–105 °C; chamber 70–100 °C | fan off; 50–200 mm/s; 12 mm³/s maximum volumetric speed | dry 75 °C for 6 h; anneal 90 °C for 2 h under its procedure | Requirements are much higher than Hyper PC and exceed the base-K2 bed at the upper end. [M029] |

Do not combine the Hyper PC and PolyMax PC rows. Do not transfer filled-PA settings to unfilled nylon.

## Moisture gate

1. Obtain the exact TDS, current spool condition, and safe spool/dryer limit.
2. Apply only the named drying cycle. “Nylon” is not one drying schedule.
3. When the TDS requires heated dry feed throughout, keep the spool in the specified controlled path for calibration and the final print.
4. Record initial mass or another repeatable dryness indicator if available; compare surface/extrusion against a known-dry sample.
5. Store sealed with suitable desiccant immediately after use.
6. Do not compensate wet-filament popping, roughness, weak extrusion, or dimensional variability with more retraction or excess temperature.

The cited examples span 75 °C/6 h for PolyMax PC, 80 °C/at least 40 h for Ultrafuse glass-reinforced PA, and 100 °C/8 h for CoPA. These are exact-product instructions, not a family chart. [M024, M027, M029]

## Thermal, chamber, and surface gate

- Confirm whether the physical printer has only a passive enclosure or a controlled heated chamber. A closed door does not create a verified 70–100 °C chamber.
- For CoPA, preserve the table/FAQ enclosure contradiction and request current manufacturer clarification before a large or warp-sensitive part. [M024]
- Hyper PC's lower product-page range does not prove generic PC can print without a chamber. PolyMax PC explicitly requires 70–100 °C chamber conditions. [M028, M029]
- Confirm the exact plate and adhesive/release-layer procedure. “PEI” in one product page does not define surface preparation for every PA/PC grade.
- Stop if the minimum required condition exceeds confirmed hardware. Never bypass temperature limits or improvise a heated chamber.

## Operational parameter card

### First layer, shrinkage, and delamination

- Calibrate the first layer after drying, using the final plate and environmental state.
- Use a representative large/flat coupon to test warp; use an oriented mechanical coupon to test layer adhesion.
- Brim/mouse ears, surface system, orientation, and geometry changes are controlled variables. A raft does not prove dimensional or layer integrity.
- Cool/remove only by the plate/material procedure. Do not force a highly adhered PC/PA part from an unknown surface.

### Speeds, flow, acceleration, fan, and retraction

- The published speed ranges are global. Feature speeds remain **Unvalidated** until tested.
- Preserve fan off only for the cited CoPA, PA6-CF20, PA12-CF10, and PolyMax PC products. Do not generalize.
- Respect 12 mm³/s only for PolyMax PC. All other PA/PC K2 maximum volumetric flow values remain **Unvalidated**. [M029]
- Tune maximum flow after drying and temperature. Reduce speed before exceeding a temperature limit.
- Choose acceleration from ringing, corner, tall-part, flow, and adhesion tests.
- Tune retraction last; moisture, chamber state, and temperature can imitate stringing.

### Layer geometry, walls, infill, and loads

- Use whole generated line widths and confirm small features in Preview.
- Align major tensile and bending loads in XY where possible; inspect bolt bosses, snap roots, and thin transitions for interlayer peel.
- Put shell material around load entry/fasteners; choose infill for shear transfer and surface support.
- Print fit and hole coupons after the material has reached the same drying, chamber, cooling, and conditioning state as the final part.
- Treat annealed and moisture-conditioned dimensions as a different state from as-printed dimensions.

## CFS and support pairing

- Do not infer standard CFS compatibility from a PA-CF marketing family alone. Check exact spool geometry, stiffness/brittleness, dryness, and the applicable CFS matrix. [P024, M003]
- The standard CFS wiki specifically warns about brittle PPA-CF/PPS-CF. CFS-C has a separate matrix for PA6-CF, PA12-CF, PA612-CF, PPA-CF, PAHT-CF, and PPS-CF. [P024, M004]
- PolyDissolve S1 rates nylon highly in its product matrix but rates PC poorly. UltiMaker PVA names Nylon compatible but says its product is unsuitable with its PC. Ultrafuse BVOH names PA/PAHT-CF15 pairings. Validate exact products, temperature overlap, interface, purge, and dissolution. [M030, M032, M033]
- A chemical pairing does not establish a CFS path or an independent-tool workflow.

## Abrasion, conditioning, health, and maintenance

- CoPA and Hyper/PolyMax PC are not automatically non-abrasive; check exact additives. The cited CF/GF products require hardened tooling. [M025, M026, M027]
- Inspect nozzle and drive gears after filled products. Use applicable purge/cleaning procedures; never invent a hot-pull temperature.
- Annealing cycles listed above apply only to the named product. Expect possible dimensional change and validate an identically oriented coupon before fit-critical use.
- Some PA products specify post-print moisture conditioning. Follow only the exact TDS; do not soak or condition a part generically.
- Use the exact SDS, effective ventilation, and dust control. NIOSH notes that material/color/additives affect emissions and nanomaterial-containing filament can emit nanomaterial particulate. [M056, M057, M059, M062]

## Failure signatures

| Symptom | Separate these causes | Next test | Stop when |
|---|---|---|---|
| Popping, steam, rough/frosted extrusion | moisture, contamination, too much heat | exact drying and known-dry extrusion comparison | dryer/spool limit or TDS is unknown |
| Edge lift or split layers | product chamber/bed requirement, surface, cooling, geometry, dryness | representative flat and oriented coupons | required chamber/bed exceeds confirmed hardware |
| Weak or dimensionally unstable part after conditioning | grade, anneal/conditioning, orientation, moisture state | measure before/after exact procedure | safety-critical requirement lacks qualified testing |
| PC warps despite “PC profile” | exact formulation mismatch, chamber, bed/surface, cooling | compare exact Hyper PC or PolyMax PC conditions—not a merged profile | physical printer cannot satisfy minimum conditions |
| CF/GF nozzle wear or widening lines | unsuitable nozzle, abrasive fill, accumulated wear | stop and inspect against official nozzle procedure | part requires disassembly/part identity not confirmed |
| Stringing | moisture, temperature, flow, retraction | dry first, then temperature, then retraction | repeated retraction causes grind/jam |
| High-speed under-extrusion | measured flow ceiling, temperature, obstruction | stepped flow test | clicking, grinding, thermal error, or sustained flow loss |

## Release checklist

- Exact PA/PC grade identified; no filled product is treated as unfilled.
- Printer identity, hotend/nozzle, bed/surface, passive enclosure versus controlled chamber, and CFS variant confirmed.
- Drying, dry-feed, storage, annealing, and conditioning states recorded.
- First-layer, temperature, flow, warp, layer adhesion, bridge/overhang, and dimensional/functional coupons completed as required.
- Preview inspected for temperatures, fan, volumetric flow, thin walls, support/purge, and material assignment.
- Structural, thermal, wear, chemical, or certification claims remain bounded to the exact product and physical acceptance test.
