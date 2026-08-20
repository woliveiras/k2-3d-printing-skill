# CFS and filament path

Identify the accessory before giving compatibility, firmware, PTFE, or repair guidance. Original CFS and CFS-C are different devices.

## Accessory identity

| Device | Official identifiers | Expansion | Boundary | Sources |
|---|---|---|---|---|
| Original CFS | two Creality 485 ports; 24 V DC, 20 W; four slots | at most four original CFS units | K2-series/Hi wording appears alongside an older K2-Plus-only field; verify connected printer and accessory | [P022] |
| CFS-C | CAN; 30 W | no multi-unit expansion documented | Separate K1-oriented device; do not use original-CFS firmware or procedures | [P026] |

Original CFS has passive desiccant storage and temperature/humidity display; it is not an active dryer. It supports nominal 1.75 ± 0.05 mm filament and documents a 197–202 mm spool diameter and 42–68 mm spool width. [P022]

## Material and spool gate

Official pages differ. The product page gives a narrower list—PLA, PETG, ABS, ASA, PET, and PLA-CF—while the Wiki compatibility page additionally describes HIPS and **dried** PVA/BVOH as usable. The Wiki rejects TPU/elastic filament and wet PVA/BVOH and warns that very hard/brittle PPA-CF and PPS-CF can break in the path. Preserve the difference; do not convert it into universal brand compatibility. [P022] [P024]

Before loading:

1. Confirm original CFS versus CFS-C and the physical printer.
2. Record exact filament product, diameter tolerance, stiffness/flexibility, moisture state, abrasiveness, and manufacturer TDS/SDS.
3. Measure/check spool geometry and reject deformed cardboard or a spool outside the documented original-CFS envelope.
4. Keep TPU/elastic filament and wet PVA/BVOH out of original CFS. Treat very hard/brittle filled filament as a breakage risk even if the printer hotend could process it.
5. Printer material support does not imply CFS-path support.

## Preventive path maintenance

| Trigger | Original-CFS task | Tools/parts | Safe state | Validation | Sources |
|---|---|---|---|---|---|
| Every two weeks | Check desiccant effectiveness/condition | Exact replacement not stated | Power down and disconnect before service; keep water away | No liquid/leak; compartment dry; humidity trend recorded after restart | [P023] [P025] |
| No later than three months when desiccant is ineffective/aged | Replace; official page warns aged material can leak water and damage electronics | Confirm exact desiccant from official procedure | Same | No leak or electrical symptom | [P025] |
| About every two months | Inspect/replace documented 4 × 2.5 mm PTFE tube according to the official procedure | Correct officially compatible tube; tool not stated | Power down/disconnect; unload only as directed | Tube seated/routed without pinch; supervised load/unload succeeds | [P025] |
| Monthly with abrasive filament | Inspect PTFE sooner for wear | Same | Same | No visible wear/debris; feed succeeds without grinding/error | [P025] |

The intervals are official maintenance guidance, not a guarantee. Shorten inspection based on visible wear, abrasive material, feed resistance, grinding, or repeated errors. Never assume external tube size proves compatibility with an internal path component.

## Jam or feed-failure tree

1. Stop the print before a feed fault creates starvation, purge failure, or collision.
2. Record accessory identity, slot, spool geometry, material, dryness, RFID/manual mapping, error text, printer model/firmware, CFS firmware if visible, and whether the failure occurs at spool pickup, CFS exit, external PTFE, printer inlet, extruder, or nozzle.
3. If the material violates P024, do not force it through CFS. Remove it only through the normal official unload path.
4. Power down and disconnect before touching the CFS path. Do not connect/disconnect cables while energized. [P023]
5. Inspect only user-accessible spool rotation, deformation, loose filament, external 4 × 2.5 mm PTFE routing, visible pinch/wear, and correctly seated accessible connections. Do not pull against a powered motor or open protected covers.
6. Separate CFS/path failure from printer-extruder/nozzle failure by observing where motion stops. Do not repeatedly command loads when grinding or resistance persists.
7. Replace PTFE or desiccant only with an exact original-CFS procedure and compatible part. The cited sources provide no internal feeder-gear, sensor, motor, connector, or torque procedure.
8. Validate with one supervised load, unload, and feed to the printer; then a small single-material test before multicolor operation.

Stop and escalate for liquid/desiccant leakage, damaged cable/connector, rain or water exposure, burning odor, smoke, repeated motor grinding, inaccessible broken filament, internal sensor/electronics error, protected-cover access, or any part/procedure mismatch. The CFS manual directs qualified service for electrical/liquid/internal failures and states that covered internal parts are not user-serviceable. [P023]

## Firmware boundary

The official guide uses `.bin` for original-CFS firmware and routes the update through the connected printer; a printer firmware update can require a CFS update. It says to retract filament before updating and to recalibrate the printer afterward. The installed original-CFS firmware and a current independently published original-CFS version were not observed. Do not update firmware without separate authorization and exact printer/accessory/version verification. [P021]
