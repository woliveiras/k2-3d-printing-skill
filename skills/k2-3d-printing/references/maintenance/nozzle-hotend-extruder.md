# Nozzle, hotend, extruder, cutter, and wiper

Nozzle assemblies differ across the K2 family. Confirm the physical model, installed nozzle diameter/material, and actual assembly before heating or disassembly.

## Applicability

| Model | Confirmed official evidence | Unresolved boundary | Sources |
|---|---|---|---|
| K2 | Integrated heat-break/nozzle assembly with hardened-steel tip; 0.4 mm standard; 0.6 and 0.8 mm listed; official replacement and extruder-jam pages exist | No tightening torque or base-K2 nozzle/hotend SKU; physical 0.2 mm compatibility not confirmed | [P003] [P006] [P008] [P035] |
| K2 Pro | Product/manual thermal and extruder facts available | No cited nozzle-replacement procedure; do not use K2 steps | [P010] [P011] |
| K2 Plus | Separate integrated, model-specific 0.4/0.6/0.8 nozzle procedure; 350 °C maximum hardware limit | Procedure is explicitly not transferable to other models; no stated torque | [P012] [P013] [P014] |
| K2 SE / K2 SE 4C | Product-level 0.4 mm nozzle and 300 °C maximum claims | No cited service procedure, assembly compatibility, torque, or part number | [P015] [P016] |

## Conditional base-K2 nozzle replacement boundary

The official page confirms a 6 mm socket, thermal grease, an integrated heat-break/nozzle design, a hardened-steel tip, and a controlled hot replacement operation with burn risk. It provides neither a torque nor a visible base-K2 nozzle part number. [P006]

Before providing ordered replacement steps:

1. Confirm K2 from the physical label or `About` screen.
2. Open P006 live and verify its revision, assembly image, nozzle size, tools, hot-state sequence, exact hand positions, and any firmware/UI steps.
3. Obtain the exact officially compatible replacement assembly. A firmware/profile entry is not part compatibility.
4. Prepare the confirmed 6 mm socket and specified thermal grease; do not substitute an unknown compound.
5. Follow the source's controlled hot step only for the duration explicitly required. Keep clear of hot and moving parts.
6. Return the machine to stopped, powered-off, unplugged, and cooling state immediately after the hot step.
7. Do not invent a torque. If the source currently visible still omits one and secure installation cannot be verified without it, stop and ask Creality support.

The cited record does not preserve the detailed fastener order or manipulation sequence. Do not recreate them from memory or from a K2 Plus, video, or community procedure.

### Nozzle validation

Inspect for correct seating and no visible damage while off and cool. Then use normal controls for a supervised extrusion check, run applicable calibration, slice with the actual nozzle diameter, inspect Preview, and make a small supervised test print. Stop on a thermal error, smoke, burning odor, material appearing outside the intended nozzle outlet, grinding, collision, or unstable extrusion. Documentation does not establish physical success.

## Extrusion-loss and clog route

1. Stop the print before accumulated material can cause a collision.
2. Record the confirmed printer, filament, CFS/direct path, nozzle, temperatures commanded by the existing job, error text, and whether the extruder moves or grinds.
3. Use the manual's normal filament-load/output check. Keep hands clear of the hot nozzle and moving extruder. [P003]
4. If output is absent or irregular, stop changing slicing variables until the path and hardware are inspected.
5. For a confirmed base K2, open the model-specific extruder-jammed-filament procedure P008. It identifies the extruder front cover as SKU 4001020081; do not assume any other part number or torque.
6. For another family member, use only that model's official procedure. Never transplant base-K2 or K2 Plus disassembly.
7. If the fault involves heater/sensor errors, damaged wiring, smoke/odor, molten material in an inaccessible area, broken fasteners, or a step absent from the source, power off, unplug, cool, and escalate.
8. After model-supported clearing, perform a supervised normal extrusion check and a small test print. Record whether output, temperature stability, feeding, and surface extrusion pass.

## Cutter and wiper

For confirmed base K2, the official maintenance page says to inspect the cutter after five rolls of PLA, ABS, PETG, or PC when it is used, and after one roll of fiber-filled filament when cutting frequently. Inspect the wiper dome daily and its tape weekly. [P027]

| Procedure field | Cutter | Wiper |
|---|---|---|
| Risk | sharp edge, pinch/motion, unsupported disassembly | pinch/motion, hot contamination area, loose part |
| Tools/parts | not stated; do not invent | not stated; do not invent |
| Safe state | off, unplugged, cool; unload only as exact source directs | off, unplugged, cool |
| Source-supported action | inspect; remove only safely accessible loose debris | inspect dome/tape; remove only safely accessible loose debris |
| Validation | supervised load/unload and feed-path check | normal wipe sequence during a controlled test, with no obstruction |
| Stop | damaged/loose blade, uncertain position/SKU, unsupported cover removal | torn/loose wiper, unknown replacement, collision risk |

Do not purchase or install a cutter, wiper, nozzle, hotend, heater, thermistor, extruder gear, PTFE tube, or cover until an official source matches the exact model and part.
