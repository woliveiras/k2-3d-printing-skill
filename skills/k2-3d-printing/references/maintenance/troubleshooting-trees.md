# Maintenance troubleshooting trees

Use symptom-first diagnosis. Change one domain at a time and preserve evidence before clearing an error, reslicing, calibrating, or disassembling.

## Universal entry gate

1. If there is smoke, burning odor, flame, liquid ingress, damaged mains wiring, uncontrolled heat, repeated collision, or exposed electrical damage, stop operation and follow [safety](../safety.md). Do not continue diagnosis while energized.
2. Confirm the physical printer/accessory. If `K2C` is the only evidence, stop model-specific hardware steps and ask for the physical rating label.
3. Preserve photos/video, exact error text, model/firmware, filament and path, nozzle/plate, project/profile, Preview layer, failure time/layer, and actions already attempted.
4. Classify the likely domain: model/profile mismatch, geometry/Preview, material/process, filament path/extrusion, bed/calibration, motion, thermal/sensor, CFS, camera/network, or internal electrical.
5. Use the lowest-risk observation first. Do not change slicing, calibration, and hardware simultaneously.

## Print-symptom routing

These routes diagnose whether maintenance is indicated; they do not replace material TDS or slicing calibration.

| Symptom | Observe first | Route | Stop/escalate |
|---|---|---|---|
| First-layer adhesion failure | Physical plate/nozzle/profile match; plate seating/visible contamination; first-layer Preview; leveling result | Use [bed and calibration](bed-and-calibration.md); clean only with exact plate guidance; run supported leveling; make supervised first-layer test | Nozzle drag/collision, loose/damaged bed/plate, repeated leveling/sensor failure |
| Warping | Material/plate, part footprint, chamber identity, door/enclosure state, brim/support in Preview | Use exact filament TDS and slicing workflow; base K2 has no documented active chamber heater, while only K2 Pro/Plus have P031 controls | Required temperature exceeds printer/material limit; bed damage; part lifts into collision path |
| Nozzle clog/no output | Normal load/output behavior, grind/noise, CFS/direct path, thermal error | Use [nozzle, hotend, and extruder](nozzle-hotend-extruder.md); confirmed base K2 may use P008 | Heater/sensor fault, smoke/odor, inaccessible molten material, unknown disassembly/part |
| Under-extrusion | Preview path/volumetric demand, normal extrusion check, spool/CFS path, nozzle output | Separate slicing/flow from feed restriction; inspect [CFS path](cfs-and-filament-path.md) or nozzle route before recalibrating flow | Repeated grinding, thermal error, broken internal filament, damaged path |
| Over-extrusion | Preview flow/line behavior versus material emerging outside intended nozzle outlet | If only toolpath/output amount, use slicing calibration; if leakage/assembly symptom, stop and use nozzle service boundary | Material outside intended nozzle outlet, unstable heat, recent unsourced nozzle work |
| Stringing | Travel/retraction Preview, exact material condition/TDS, nozzle output, CFS suitability | Use slicing calibration one variable at a time; do not force flexible or wet incompatible material through CFS | Symptom includes grinding, feed errors, thermal instability, or physical leak |
| Layer shift | Shift axis/layer, collision evidence, lifted part, Preview, visible motion obstruction | Use [motion system](motion-system.md); inspect accessible motion only while off/cool | Frayed belt, loose/damaged pulley, bent rail/screw, binding, cable/electrical damage |
| Ringing/ghosting | Repeatable surface echo, speed/acceleration Preview, machine stability, recent belt/motion work | Separate profile acceleration from hardware; run supported input shaping; use motion file | Calibration fails, abnormal noise/binding, unknown belt adjustment |
| Delamination | Material TDS, orientation/load direction, wall paths, temperature/fan/chamber Preview | Use material and slicing references; never exceed official limits or apply K2 Pro/Plus chamber control to base K2 | Crack coincides with collision, thermal error, or required process exceeds hardware limit |
| Spaghetti | First failed layer/region, detached part/support, unsupported island, collision, time-lapse/Preview | Stop print; inspect first layer, supports, bridges, islands, plate and motion; remove debris only off/cool | Blob surrounds hotend/wiring, toolhead displaced, sensor/cable damaged, repeated collision |
| Nozzle collision | Preview obstruction, warped/lifted part, accumulated material, wiper/plate seating, toolhead alignment | Stop promptly; power off/unplug/cool; use [motion system](motion-system.md) and bed checks | Displaced toolhead/nozzle, damaged sensor/bed/wiring, binding, repeat event |
| Abnormal noise | Axis/location/timing, feed versus motion, fan versus CFS, error text | Route to motion, CFS, nozzle/extruder, or fan section based on source; do not guess by sound alone | Grinding persists, collision, seized fan, damaged belt/cable, inaccessible source |

## Hardware and accessory trees

### Thermal failure

```text
thermal error or unstable displayed temperature
├─ smoke, odor, liquid, damaged wiring, or uncontrolled heat
│  └─ stop, power down only if safe, do not touch/open, escalate immediately
└─ no immediate hazard
   ├─ record exact error, model, firmware, commanded/displayed temperatures
   ├─ power off, unplug, cool for at least the model-required interval
   └─ do not bypass, probe, reseat unknown connectors, or repeat heating
      └─ use Creality support or qualified service
```

The cited sources provide no heater, thermistor, board, connector, electrical-measurement, or torque procedure. [P003] [P007] [P023]

### Sensor or calibration failure

```text
sensor/calibration error
├─ physical obstruction or loose debris visible without disassembly
│  └─ remove only while off, unplugged, cool; rerun normal supported routine once
├─ nozzle/bed collision, loose component, damaged cable, or repeat error
│  └─ stop and escalate; do not bypass the sensor
└─ routine passes
   └─ validate with a small supervised test; passing calibration is not physical validation
```

Base-K2 component evidence includes strain-gauge leveling and filament-break detection, but the cited sources provide no replacement procedure. [P003] [P007]

### Original-CFS jam

```text
feed or jam error
├─ accessory is CFS-C or identity unknown
│  └─ stop original-CFS procedure; confirm hardware
└─ original CFS confirmed
   ├─ TPU/elastic, wet PVA/BVOH, deformed/out-of-envelope spool
   │  └─ do not force; use normal official unload path
   ├─ very hard/brittle filled filament
   │  └─ treat breakage as likely path risk; stop repeated feed commands
   └─ compatible material/spool
      ├─ power down/disconnect; inspect accessible spool and external 4 × 2.5 mm PTFE
      └─ inaccessible break, grinding, liquid, cable/sensor/electrical fault
         └─ qualified service
```

Validate only with a supervised load/unload, then a small single-material print. [P022] [P023] [P024] [P025]

### Printer feed problem without CFS

1. Record whether the spool turns, filament reaches the printer inlet, extruder moves/grinds, and nozzle outputs normally.
2. Use only normal load/unload and the model-specific extruder/nozzle route.
3. Do not assume CFS tubing, cutter, sensor, extruder, or hotend parts fit a direct path or another K2 variant.
4. Stop at repeated grinding, inaccessible broken filament, thermal error, damaged sensor/cable, or unsourced disassembly.

### Camera problem

```text
camera symptom
├─ image exists but is dirty/blurry on confirmed base K2
│  └─ power off/cool; clean with lint-free cloth and alcohol per P033; retest
├─ image absent/intermittent while lens is clear
│  └─ record firmware/app/network state; do not open camera or invent a reset
└─ liquid, loose lens, damaged cable, or failure persists
   └─ official support
```

### Network/device problem

1. Separate printer-local operation, camera image, Creality Print/Device view, and network reachability.
2. Record exact printer firmware, software version/mode, on-device network status, error, and whether local printing/UI still works; protect credentials and private network data.
3. The cited sources provide no model-specific network-reset, camera-cable, or board procedure. Do not factory-reset, update firmware, open the printer, or change router/security settings as a maintenance guess.
4. Use the live exact-model manual/support path. Escalate if the fault follows electrical damage, liquid, heat, repeated reboots, or inaccessible hardware.

## Exit states

Report one of these without overstating certainty:

- `Cause not isolated`: evidence is insufficient; list the next read-only check.
- `Model-specific procedure required`: stop until the exact official page and hardware identity are available.
- `Safe correction completed`: a sourced action was performed; state what remains untested.
- `Calibration passed`: the named routine completed; no print-success claim.
- `Physically validated`: the actual machine passed the defined supervised test print and acceptance criteria.
- `Service escalation required`: state the stop criterion and do not add speculative repair steps.
