# Composites, polypropylene, and high-temperature materials

Use this file for CF/GF, wood/metal/mineral particles, PLA-CF, PETG-CF, PET-CF, PA-CF, PA-GF, PP/PP-GF, PPA/PAHT, PPS/PPS-CF, PPSU, and PEI/ULTEM. Unfilled polypropylene is grouped here only because its filled grades share the same surface/tooling decision; it is not itself a composite.

## Hard gates

1. Confirm the physical printer. If `K2C` is the only identity supplied, keep hardware-specific classification blocked.
2. Confirm exact filler type/content, minimum nozzle diameter, nozzle and drive-gear material, and all-metal hotend requirement.
3. Confirm minimum nozzle, bed, and chamber conditions. A passive enclosure is not a controlled heated chamber.
4. Confirm standard CFS versus CFS-C. Feed-path approval is separate from print-process compatibility.
5. Confirm drying, dry-feed, spool heat limit, post-print anneal/conditioning, and dimensional change.
6. Use the exact SDS and control airborne dust during sanding, drilling, cutting, or grinding.
7. Stop when a minimum requirement exceeds confirmed hardware. Never bypass thermal limits or improvise electrical/chamber modifications.

## Base-K2 boundary

The official K2 page lists a 300 °C maximum nozzle, 100 °C maximum bed, all-metal hotend, steel-tipped trimetal 0.4 mm nozzle, and PLA-CF among its named materials. Apply these facts only after physical K2 confirmation; they do not approve every composite. [M001]

- **Official family only:** PLA-CF.
- **Not validated:** PETG-CF, PET-CF, PA6-CF, PA12-CF, PA-GF, PP, PP-GF, PPA-CF, and PAHT-CF even when part of a range fits.
- **Incompatible against base-K2 limits:** PPS-CF requiring at least 310 °C, PPSU requiring at least 390 °C nozzle/200 °C bed/170 °C chamber, and PEI requiring at least 370 °C nozzle/150 °C bed. [M043, M044, M045]

Do not call a material “possible with modification” unless the user explicitly requests a separate modification assessment. This skill must not propose temperature-limit bypasses, heater/thermistor swaps, improvised chambers, alternate firmware, root access, or sensor bypass.

## Source-specific manufacturer ranges

### PLA/PET/PETG and nylon composites

| Exact product | Nozzle | Bed/chamber | Cooling and speed | Tooling/drying/post-process | Evidence boundary |
|---|---:|---|---|---|---|
| Creality Hyper PLA-CF | 190–230 °C | bed 45 °C | 50–300 mm/s | page gives 55 °C/8 h forced-air or 75 °C/12 h heated-bed drying | K2 names PLA-CF, but page does not state nozzle wear; confirm exact grade/nozzle. [M036, M001] |
| Creality Hyper PETG-CF | 240–260 °C | bed 70–90 °C | fan 80%; 30–300 mm/s | hardened/wear-resistant nozzle required | Not named on the base-K2 material list. [M037] |
| Polymaker Fiberon PA6-CF20 | 280–300 °C | bed 40–50 °C; formulation-specific low ambient/bed | fan off; 30–300 mm/s | 20% CF; all-metal hotend; hardened nozzle; heated dry feed; anneal 100 °C/16 h | Warp-Free conditions do not generalize to PA6. [M025] |
| Polymaker Fiberon PA12-CF10 | 280–300 °C | bed 40–50 °C | fan off; 30–300 mm/s | hardened nozzle/all-metal hotend; dry feed; anneal 100 °C/16 h | Lower moisture sensitivity than cited PA6-CF is not immunity. [M026] |
| Polymaker Fiberon PA6-GF25 | 280–300 °C | bed 40–50 °C | fan off; 30–300 mm/s | hardened nozzle; dry feed; exact anneal procedure | Product-specific. [M038] |
| Polymaker Fiberon PET-CF17 | 270–300 °C | bed 70–80 °C; manufacturer says no heated enclosure required | fan off; 30–300 mm/s | all-metal hotend; hardened nozzle; anneal 120 °C/10 h | PET-CF is not plain PET. [M039] |
| Polymaker Fiberon PET-GF15 | 280–310 °C | bed 70–80 °C | fan off; 30–250 mm/s | hardened nozzle; anneal 120 °C/16 h | Upper range exceeds base K2; never command 310 °C. [M040] |
| BASF Ultrafuse PA v3.1 | 220–250 °C | bed 90–120 °C; passive closed chamber | 30–60 mm/s | glass reinforced/abrasive; hardened nozzle and drive wheels advised; dry 80 °C at least 40 h | Base K2 cannot reproduce the full bed range. [M027] |

### Polypropylene

| Exact product | Nozzle | Bed/surface | Speed/nozzle | Drying | Evidence boundary |
|---|---:|---|---|---|---|
| BASF Ultrafuse PP v4.0 | 220–240 °C | 60–80 °C; named PP tape or adhesive | 20–50 mm/s; 0.4 mm or larger | 60 °C for 4–16 h | PP is absent from the base-K2 and standard-CFS lists. [M034] |
| BASF Ultrafuse PP GF30 v2.3 | 240–260 °C | 20–40 °C or 70–90 °C only with the corresponding named PP tape/PP-GF adhesive system | 30–80 mm/s; 0.6 mm or larger | 60 °C for 4–16 h | The bed ranges are surface-system alternatives, not one broad range. [M035] |

PP is a candidate for chemical/fatigue or living-hinge use only when the exact grade TDS and a representative cycle/environment test support it. Low surface energy makes surface selection critical; do not substitute a generic adhesive without a coupon.

### PPA, PAHT, PPS, PPSU, and PEI

| Exact product | Published minimum/full range | Base-K2 comparison | Classification |
|---|---|---|---|
| Creality PPA-CF | nozzle 280–300 °C; bed 90–105 °C; enclosure; dry 80 °C/8–12 h forced air | reaches nozzle maximum; upper bed exceeds 100 °C; not on K2 material list | **Not validated**; standard CFS wiki warns hard/brittle PPA-CF may break. [M041, P024] |
| BASF Ultrafuse PAHT-CF15 page recorded by M042 | nozzle 250–270 °C; bed 65–85 °C; 0.6 mm or larger ruby/hardened nozzle; no chamber temperature or drying rule stated | superseded v3.4 TDS recorded by M042 conflicted at 260–280 °C nozzle and 100–120 °C bed | **Not validated** for base K2; require the exact printer, nozzle, spool documentation, drying evidence, and a calibration coupon. [M042] |
| Polymaker Fiberon PPS-CF10 | nozzle 310–350 °C; bed 80–90 °C; ambient 25–80 °C; hardened nozzle; brittle clear path | minimum nozzle exceeds 300 °C | **Incompatible** with base K2. Its page explicitly says its flame claim is not UL 94 certification. [M043] |
| BASF Ultrafuse PPSU page recorded by M044 | nozzle 390–410 °C; bed 200–220 °C; chamber 170–210 °C; 25–100 mm/s; drying rule unconfirmed | all core thermal requirements exceed base-K2 limits | **Incompatible**. [M044] |
| PEI/ULTEM in Prusa high-temperature guidance | nozzle 370–420 °C; bed 150–155 °C; specialized equipment | exceeds base-K2 limits | **Incompatible**. [M045] |

## Wood, metal, and other particles

First distinguish:

- visual “wood” color;
- foamed wood-look PLA without powder, such as PolyWood PLA v2;
- genuine wood, metal, mineral, CF, or GF particles.

Prusa's manufacturer guide warns of clogging/brittleness and weaker layer adhesion for filled materials; for wood products with large particles it suggests at least a 0.6 mm nozzle and 0.2 mm layer height, while metal-filled filament needs hardened tooling. Use these only as product-class starting points. [M011, M012]

Do not call every wood-filled material abrasive or every foamed wood-look product nonabrasive. Require the exact filler statement and minimum nozzle.

## Abrasion and nozzle decision

| Evidence state | Action |
|---|---|
| Exact product explicitly requires hardened/wear-resistant nozzle | Require the specified nozzle material and diameter before slicing |
| Manufacturer portfolio states the fiber line is abrasive | Treat nozzle and drive wear as a condition; confirm exact product page |
| Product contains real metal/mineral/glass/carbon particles but tooling is silent | Classify nozzle suitability **Unvalidated**; do not assume a standard brass nozzle |
| Product name says CF/GF but composition is unclear | Obtain TDS/SDS; do not infer filler content or benefit |
| Current nozzle material/diameter is unknown | Stop composite-specific recommendation and ask for nozzle evidence |

The base K2's steel-tipped trimetal 0.4 mm nozzle is official K2 evidence, not proof that it meets every composite's material/diameter requirement. [M001]

## CFS decision

- Standard CFS officially lists PLA-CF and its product page broadly lists PA-CF. The wiki warns hard/brittle PPA-CF/PPS-CF can break in the tube. Use the more specific material-behavior warning for those exact grades. [P024, M003]
- CFS-C separately marks PPA-CF, PAHT-CF, PET-CF, and PPS-CF **Not Suggested**, while listing generic PA6-CF/PA12-CF/PA612-CF as usable. This does not apply to standard CFS. [M004]
- PP, PP-GF, PETG-CF, wood/metal fill, and other composites remain **Not validated** in standard CFS unless the exact SKU appears in its applicable official matrix.
- Stop if filament cracks, sheds, kinks, or resists the path. Do not force it or dismantle the system without an official procedure.

## Family-specific operating rules

Apply the [shared material card](INDEX.md#required-material-parameter-card) and [calibration workflow](../slicing/calibration.md), with these composite-specific constraints:

- Determine maximum volumetric flow with the exact abrasive nozzle; bore and material change flow.
- Avoid repeated large retractions that can grind or fracture brittle filament.
- Apply fan off or 80% only to the named products in the table.
- Obey the exact minimum nozzle and confirm particle-sensitive walls in Preview. Short fibers do not eliminate FDM layer anisotropy; test representative load coupons.
- Use the exact named surface system. PP-GF30's two bed ranges belong to different surface systems. [M035]
- Never transfer `no heated enclosure` from Fiberon PET-CF17 or `low bed` from PA6-CF20 to another composite.

## Drying, storage, post-processing, and health

- Apply only the exact drying method. Forced-air, vacuum, heated-bed drying, and dry-feed instructions are not interchangeable.
- Verify spool/container temperature resistance and dryer calibration; store sealed with suitable desiccant.
- Apply annealing only to the named product and procedure. Measure a same-orientation coupon before and after; expect possible dimensional/property change.
- NIOSH says nanomaterial-containing filament can emit nanomaterial particulate, and UL guidance includes composite/nylon/chopped-CF exposure controls. Use exact SDS, source ventilation, and controlled cleanup. [M056, M057, M059, M062]
- For sanding, drilling, cutting, or grinding, use local capture or material-compatible wet methods and suitable PPE from the SDS/risk assessment. Do not dry-sand in occupied domestic space or clean dust with compressed air.
- Inspect nozzle bore, tip, drive gears, filament path, and plate after use. Follow only applicable purge/cleaning procedures; do not invent torque, hot-pull temperature, or replacement interval.

## Failure signatures

| Symptom | Plausible causes | Next test | Stop when |
|---|---|---|---|
| Nozzle clogs or flow decays | particle/nozzle mismatch, wear, moisture, contamination, flow | stop; confirm exact minimum nozzle and cleaning procedure | hot procedure/disassembly is unconfirmed |
| Lines widen or detail degrades over time | abrasive bore wear | compare measured extrusion/nozzle inspection by official procedure | nozzle identity/replacement part is unknown |
| Filament snaps in CFS/path | brittleness, moisture state, curvature, unsuitable grade | unload without forcing; inspect exact matrix | fragment is inaccessible or procedure requires system disassembly |
| Popping/rough extrusion | moisture | exact dry/dry-feed cycle and comparison | dryer/spool limit unknown |
| Warp/delamination | chamber/bed/surface, geometry, cooling, dryness | representative flat/oriented coupon | required condition exceeds confirmed hardware |
| Annealed part no longer fits | shrink/growth/warp under procedure | measure before/after coupon | fit-critical dimensions were not characterized |
| Temperature request exceeds limit | wrong product/printer/profile | reject profile and select compatible material | never bypass or modify limits |
| Dust escapes during finishing | absent capture/unsafe method | stop work; implement SDS-based control | effective containment/PPE unavailable |

## Family-specific release gate

Apply the [shared release decision](INDEX.md#release-decision). Also confirm filler and tooling requirements and reject any minimum thermal requirement above the confirmed printer limit; do not reframe hardware incompatibility as a slicer adjustment.
