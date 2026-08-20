# Printer identity and K2-family boundaries

## When the user says `K2C`

Treat `K2C` as an unconfirmed physical identity until the rating label or `About` screen resolves it. The evidence set identifies K2, K2 Pro, K2 Plus, K2 SE, and K2 SE 4C, but no distinct physical model named `K2C`. The official product page defines **K2 Combo** as a K2 printer bundled with one original CFS; the bundle name does not prove that a particular unit is a K2. [P001] [P004] [P017] [P018] [P019] [P020] [P035]

Never use a Creality Print profile as physical identity proof. K2 and K2 Pro also share the public board identifier and firmware image in the researched listing, so firmware alone may not distinguish them. [P017] [P018] [P035] [P036]

## Family comparison

| Physical printer | Build volume | Official thermal limits | Enclosure and chamber | Supplied/advertised plate | CFS boundary | Sources |
|---|---:|---|---|---|---|---|
| K2 | 260 × 260 × 260 mm | nozzle 300 °C; bed 100 °C | fully enclosed; passive chamber; no active chamber heater documented | flexible PEI spring-steel plate | original CFS; K2 Combo includes one; at most four original CFS units documented | [P002] [P003] [P004] [P005] |
| K2 Pro | 300 × 300 × 300 mm | nozzle 300 °C; bed 110 °C; active chamber 60 °C | fully enclosed; actively heated chamber | flexible PEI plate | original CFS; at most four documented | [P010] [P011] [P031] |
| K2 Plus | 350 × 350 × 350 mm | nozzle 350 °C; bed 120 °C; active chamber 60 °C | fully enclosed; actively heated chamber | flexible plate | original CFS; at most four documented | [P012] [P013] [P031] |
| K2 SE | 220 × 215 × 245 mm | nozzle 300 °C; bed 100 °C | no active heated chamber documented | epoxy-resin plate | original-CFS support advertised; verify the exact bundle/hardware | [P015] |
| K2 SE 4C | 220 × 215 × 245 mm | nozzle 300 °C; bed 100 °C | no active heated chamber documented | epoxy-resin plate | integrated four-slot system; do not infer original-CFS behavior | [P016] |

Do not propagate the K2 SE product page's `0.4 mm filament diameter` field; it appears to confuse filament and nozzle diameter. Preserve it as a source defect. [P015]

The active-chamber control guide applies only to K2 Pro and K2 Plus. It documents a 60 °C maximum and different cooling/heating behavior below and above 40 °C. It does not authorize any chamber setpoint on K2, K2 SE, or K2 SE 4C. [P031]

## Conditional base-K2 record

Apply this section only after the physical label or `About` screen confirms **K2**.

| Field | Official record | Evidence boundary | Sources |
|---|---|---|---|
| Official name | K2 3D Printer | `K2 Combo` names the K2-plus-CFS package | [P003] [P004] |
| Process | FFF | Capability, not a process profile | [P003] |
| Build volume | 260 × 260 × 260 mm | Reconfirm for the physical unit | [P003] |
| Extruder | proximal/direct-drive dual-gear; 1.75 mm filament | Manual and store use different equivalent descriptions | [P003] [P004] |
| Hotend/nozzle | integrated heat-break-and-nozzle service assembly with hardened-steel tip | No base-K2 assembly part number or tightening torque was found | [P006] |
| Supplied nozzle | 0.4 mm | The official service page also lists 0.6 and 0.8 mm | [P003] [P006] |
| 0.2 mm nozzle | visible in official firmware/profile metadata only | Physical base-K2 replacement compatibility remains unconfirmed | [P035] [P036] |
| Maximum nozzle temperature | 300 °C | Official hardware limit, not a material recommendation | [P003] |
| Plate | flexible PEI spring-steel build plate | A separate double-sided frosted PEI accessory explicitly names K2 and K2 Pro | [P003] [P009] |
| Maximum bed temperature | 100 °C | Official hardware limit, not a material recommendation | [P003] |
| Chamber | fully enclosed, passive; no active heater documented | Do not transfer K2 Pro/Plus chamber controls | [P005] [P031] |
| Original CFS | compatible; up to four documented | Original CFS is not CFS-C; verify exact connected unit | [P004] [P022] [P026] |
| Sensors/features | automatic leveling, strain-gauge leveling component, filament-break detection, AI monitoring camera, input shaping/vibration optimization, power-loss recovery | Feature presence is model evidence only after K2 is confirmed | [P003] [P007] |
| Supported-material list in manual | PLA, PETG, ABS, PLA-CF, PET | Printer support does not prove CFS compatibility or provide a slicing profile | [P003] [P024] |
| Manual evidence | K2 User Manual V1.0_EN; PDF created 2025-04-14 and modified 2025-07-08 | Recheck before a repair or limit-sensitive answer | [P002] [P003] |

The manual also lists 600 mm/s maximum advertised speed, 20,000 mm/s² maximum advertised acceleration, 2.4 GHz Wi-Fi, USB/Wi-Fi transfer, 8 GB eMMC, and G-code/3MF input. Treat these as advertised capabilities, never as recommended slicing values. [P003]

## Firmware identity record

The public firmware catalog was examined live on 2026-08-20. These are the newest entries observed in that public listing, not installed versions and not authorization to update:

| Model and board in listing | Observed public entry | Listing evidence | Boundary | Sources |
|---|---|---|---|---|
| K2 / K2 Pro; CR0CN200400C10 | V1.1.6.7; `CR0CN200400C10_R_202607231728_ota_img_V1.1.6.7.img` | listed 2026-07-28; note says known issues fixed | Shared image cannot identify K2 versus K2 Pro. API subtype labels/IDs conflict; retain model, board, and filename together | [P017] [P018] [P035] [P036] |
| K2 Plus; CR0CN240110C10 | V1.1.6.4; filename build stamp 20260731 | public entry timestamp 2026-08-07 11:49 CEST | K2 Plus only | [P019] [P036] |
| K2 SE; CR4CU220812S12K1 | V2.3.6.77 | public entry timestamp 2026-08-07 11:55 CEST | K2 SE only | [P020] [P036] |

Record the installed printer and CFS versions from their own screens. The official guide distinguishes printer `.img` from CFS `.bin`, routes original-CFS updates through the connected printer, and calls for filament retraction before the update plus input shaping and automatic leveling afterward. It does not establish the installed version or a current independently published original-CFS firmware number. Never update without separate authorization. [P021]

## Original CFS versus CFS-C

| Device | Official interface/power | Expansion | Intended boundary | Sources |
|---|---|---|---|---|
| Original CFS | two Creality 485 ports; 24 V DC, 20 W; four slots | up to four CFS units | Advertised for K2-series/Hi contexts; verify exact printer and page wording | [P022] |
| CFS-C | CAN; 30 W | no multi-unit expansion documented | Separate K1-oriented device | [P026] |

Never interchange their firmware, wiring, procedures, or compatibility claims. The original-CFS product page itself contains wording drift between broad K2-series/Hi compatibility and an older K2-Plus-only field; retain the conflict and confirm the attached hardware. [P022] [P026]

## Unresolved facts

Do not invent or infer:

- the user's physical model, hardware revision, serial-specific configuration, installed nozzle, plate, CFS generation, or installed firmware;
- any base-K2 nozzle, hotend, sensor, fan, filter, cutter, wiper, cable, or motion-part number except the explicitly sourced extruder front-cover SKU 4001020081; [P008]
- nozzle, hotend, belt, bed, extruder, chassis, or other fastener torque;
- cross-model compatibility unless an official part page names every affected model;
- physical base-K2 0.2 mm nozzle compatibility from firmware/profile metadata;
- active chamber heating on base K2 or either K2 SE variant;
- internal electrical repair steps, connector pinouts, test points, alternative firmware, root access, or sensor bypass procedures.

Recheck official model-specific sources before every part purchase, repair, firmware decision, or use of the words `current`, `latest`, `supported`, `compatible`, or `safe`.
