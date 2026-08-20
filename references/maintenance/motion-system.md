# Motion system

Use this file for rails, shafts, lead screws, belts, pulleys, layer shifts, ringing, collisions, or abnormal motion noise. Confirm the physical model before adjusting anything.

## Official family distinctions

| Area | K2 | K2 Pro | K2 Plus | K2 SE / K2 SE 4C | Sources |
|---|---|---|---|---|---|
| XY belt tension | manual official procedure | manual official procedure | automatic belt tension | no procedure captured | [P030] |
| X/Y/Z lubrication | base manual and maintenance page; schedule conflict with newer K2-series pages | model-specific X anti-rust oil versus Y/Z generic grease | separate maintenance page; do not import base schedule | no procedure captured | [P003] [P027] [P028] [P029] [P032] [P034] |
| Calibration after motion work | input shaping and auto leveling documented for base K2; input shaping after manual belt adjustment | input shaping after manual belt adjustment | use model-specific automatic procedure | no model-specific evidence captured | [P003] [P030] |

## Rails, shafts, and lead screws

For a confirmed applicable model, follow [cleaning and lubrication](cleaning-and-lubrication.md). The newer K2-series X-rail and Z-lead-screw pages require power-off service and name WD-40 Specialist Silicone, but their weekly/biweekly cadence conflicts with older base-K2 sources. [P028] [P029]

Do not apply lubricant to belts or unspecified bearings/pulleys. Do not infer that a product named for one rail is valid for every motion surface. No official pulley-removal, alignment, bearing-replacement, belt-frequency, or fastener-torque procedure was captured.

## Conditional K2/K2 Pro belt tension

The official family guide distinguishes K2/K2 Pro manual tension from K2 Plus automatic tension. For K2/K2 Pro it records two to three clockwise turns followed by input shaping, but the research did not capture torque or enough positional detail to identify the screws without the page images. [P030]

1. Confirm K2 or K2 Pro physically.
2. Open P030 live and match the printer, access point, screw pair, starting state, and illustrated direction.
3. Mark/record the initial position without removing or loosening unrelated fasteners.
4. Follow only the documented two-to-three-turn instruction; do not convert turns into an invented torque or belt frequency.
5. Run the documented input-shaping calibration.
6. Stop on binding, asymmetric motion, collision, repeated calibration failure, damaged belt/pulley, unclear screw identity, or any need to disassemble a pulley/motor.

For K2 Plus, do not perform this manual adjustment; use its automatic model-specific function and official documentation. For K2 SE variants, the researched evidence is insufficient—do not guess. [P030]

## Symptom routes

### Layer shift

1. Stop the print and retain the sliced project, Preview, layer/time of shift, axis direction, error text, and photo.
2. Rule out a sliced collision or unstable/tall part before treating it as belt hardware.
3. With power off, unplugged, and cool, visually inspect only accessible belts, pulley areas, rails, shafts, screws, loose debris, and cable interference. Do not disassemble or move against resistance.
4. If contamination is present, use only the confirmed cleaning procedure. If tension is suspect and the model is confirmed K2/K2 Pro, use P030; K2 Plus uses its automatic function.
5. Stop at frayed belt, loose/damaged pulley, bent rail/screw, unknown fastener, internal cable contact, or absent model-specific procedure. Escalate rather than inventing alignment or torque.
6. Validate with the supported motion calibration, then a supervised small test that exercises the affected axis.

### Ringing or vibration

1. Separate a Preview acceleration/speed issue from mechanical looseness; do not alter hardware and slicing simultaneously.
2. Confirm the printer is stable and free of visible loose objects/debris.
3. Run input shaping only when officially supported for the confirmed model. Base-K2 sources call for it every 300 hours and a separate maintenance page says monthly without filament; P030 requires it after K2/K2 Pro belt work. [P003] [P027] [P030]
4. If calibration fails or noise/looseness remains, stop and inspect through the exact model service source.
5. Validate with the same small geometry/profile before and after; do not claim improvement without the physical comparison.

### Collision or abnormal noise

1. Stop active motion promptly through normal controls; use emergency power removal if there is immediate fire/electrical danger.
2. Power off, unplug, and cool before reaching inside.
3. Capture where and when the event occurred, axis, toolhead/part position, Preview layer, loose material, and error text.
4. Inspect for a lifted/warped part, accumulated filament, loose debris, obstructed wiper, obvious cable interference, or visible motion damage.
5. Do not restart if the nozzle/toolhead is displaced, a belt/pulley/rail/screw is damaged, wiring is exposed, a sensor is loose, or motion binds.
6. After only a sourced correction, run the lowest-risk model self-test without a print, then a supervised small test. Escalate repeated collision or noise.

## Service boundary

Stop and use Creality support or qualified service for pulley or motor removal, bearing replacement, bent rails/shafts/screws, inaccessible belt routing, unknown tensioner fasteners, damaged stepper wiring, repeated motion-driver errors, or any torque/alignment requirement absent from the exact official model source.
