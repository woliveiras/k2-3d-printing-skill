# PETG and PET

Treat PETG, high-flow PETG, PET, and PET-CF as separate grades. A PETG range does not establish a PET or PET-CF profile.

## Decision boundary

- **Base-K2 evidence:** the official K2 page lists PETG and PET. Apply this only after physical K2 confirmation; it does not endorse every high-flow, copolyester, filled, or annealable grade. [M001]
- **Standard CFS official fact:** PETG and PET are supported medium-hardness examples when spool dimensions and condition comply. [P024, M003]
- PET-CF is routed through [composites](composites.md); standard CFS suitability must be established for the exact brittle/abrasive grade.
- If `K2C` is the only identity evidence, stop model-specific claims and continue with product-level calibration guidance.

## Selection frame

Use PETG as a candidate when a part needs more ductility or environmental tolerance than a visually oriented PLA prototype, but require the exact TDS before claiming heat, chemical, impact, UV, or food-contact performance. Use plain PET only when the product is actually labeled PET and has its own TDS. Use a CF/GF grade only after the abrasive-tooling gate.

Finish, toughness, layer adhesion, stringing, stiffness, and translucency vary by formulation, color, moisture, and temperature. Treat these as measured product/part properties, not consequences of the acronym.

## Source-specific manufacturer ranges

| Exact product/source | Nozzle | Bed | Cooling | Published speed/flow | Drying | Evidence boundary |
|---|---:|---:|---|---|---|---|
| Creality CR-PETG generic chart | 230–250 °C | 60–100 °C | not resolved | 40–80 mm/s | not resolved | Manufacturer chart, not an exact SKU TDS. [M007] |
| Creality Hyper PETG product page | 190–260 °C | 45 °C | not resolved | 50–300 mm/s | not resolved | Very broad nozzle range and single bed value apply only to that product page. [M013] |
| Polymaker PolyLite PETG | 230–260 °C | 70–80 °C | 0–20% | 50–100 mm/s; maximum volumetric speed at or below 15 mm³/s | 65 °C for 6 h | Exact product page values. [M014] |
| Newer Polymaker PETG formulation | 240–260 °C | 60–70 °C | 20–60% | up to 300 mm/s; manufacturer gives 22 or 32 mm³/s only for named hardware contexts | 60 °C for 6 h | Do not copy a hardware-specific flow result to K2. [M015] |
| Polymaker Fiberon PET-CF17 | 270–300 °C | 70–80 °C | fan off | 30–300 mm/s | exact page requires dry handling | Hardened nozzle, all-metal hotend, manufacturer says no heated enclosure required; anneal 120 °C for 10 h only under its procedure. Read [composites](composites.md). [M039] |

The three unfilled PETG rows conflict substantially. Preserve each range under its exact product identity; never combine them into “PETG: 190–260 °C, bed 45–100 °C.”

The cited sources include no exact unfilled-PET TDS. The K2/CFS family listing cannot supply PET temperatures, fan, speed, drying, surface, or retraction; keep those fields **Unvalidated** until the spool is identified.

## Family-specific operating rules

Apply the [shared material card](INDEX.md#required-material-parameter-card) and [calibration workflow](../slicing/calibration.md), with these PETG/PET-specific constraints:

- Confirm whether the exact plate requires adhesive as adhesion aid, release layer, or both; PETG can adhere aggressively, so validate damage-free release on a first-layer coupon.
- Preserve the product-specific fan conflict: PolyLite PETG 0–20%, the M015 Polymaker PETG formulation 20–60%, and Fiberon PET-CF17 fan off. [M014, M015, M039]
- The cited sources provide no bridge/overhang speeds. Keep them **Unvalidated** until a feature coupon.
- Apply 15 mm³/s only to PolyLite PETG. The 22/32 mm³/s examples in M015 are hardware-specific and require an independent target-printer flow test. [M014, M015]
- For fit-critical parts, use a clearance/hole coupon in the final orientation, cooling, and wall-order state.

## Moisture, storage, CFS, and supports

- Apply only the exact drying instruction: 65 °C/6 h for cited PolyLite PETG and 60 °C/6 h for the cited newer Polymaker PETG. Do not assign either to Creality PETG or plain PET. [M014, M015]
- Verify spool temperature tolerance and dryer accuracy. Store sealed with suitable desiccant and record whether printing occurred from a dry box.
- Standard CFS officially lists PETG and PET, but wetness, brittleness, spool geometry, and exact product restrictions remain separate.
- PolyDissolve S1 rates PETG only partially compatible; UltiMaker PVA names PETG adhesion within its 2.85 mm ecosystem. These are pairing hypotheses, not guarantees for another brand or Creality profile. Test interface adhesion, purge, Z/XY gap, and dissolution on a coupon. [M030, M032]
- The cited primary sources do not establish HIPS or BVOH pairing with PETG. Mark it **Unvalidated**.

## Abrasion, post-processing, and care

- Plain PETG/PET nozzle wear is product-specific. Any CF/GF/mineral/metal fill triggers the [composite tooling](composites.md) gate.
- Annealing PET or PETG is not a family-wide recommendation. Fiberon PET-CF17's 120 °C/10 h cycle applies only to that product and can change dimensions. [M039]
- After a filled grade, follow its documented purge and inspect nozzle/drive wear. After any PETG/PET, clean the plate by its manufacturer method and seal the spool.

## Failure signatures

| Symptom | Separate these causes | One-variable test | Stop when |
|---|---|---|---|
| Stringing or fuzzy travels | moisture, excessive temperature, flow, travel/retraction | known-dry comparison; then temperature; then retraction | changes would exceed range or grind filament |
| Bubbles, rough surface, inconsistent extrusion | moisture or contamination | dry under exact TDS and compare same G-code | dryer/spool limit is unknown |
| Brittle or weak layers | too much cooling, low temperature, low flow, orientation | temperature/cooling coupon within range | use requires an unverified structural guarantee |
| Sagging bridges/overhangs | cooling, bridge flow/speed, moisture | feature coupon with one changed factor | unsupported span remains outside validated capability |
| Edge lift or first-layer release | surface mismatch, contamination, Z/mesh, bed state | first-layer coupon after plate procedure | bed command would exceed hardware/product limit |
| Plate damage or part will not release | incompatible surface or missing release layer | stop heating; allow cooling; follow plate maker removal procedure | force risks coating or glass damage |
| High-speed under-extrusion | volumetric flow exceeds hotend/material result | stepped flow test | clicking, grinding, temperature instability, or sustained flow loss |

## Family-specific release gate

Apply the [shared release decision](INDEX.md#release-decision). Also confirm the exact PETG/PET grade and the exact plate's adhesion or release-layer procedure; do not release a PETG job while damage-free removal remains untested.
