# Electronics, fans, filters, camera, sensors, and firmware

Treat internal electrical and thermal systems as a service boundary unless a current, exact-model official user procedure explicitly permits the action.

## Safe boundary

- Use the supplied power cable and a grounded three-prong outlet for confirmed base K2. Install on a stable, cool, dust-free, well-ventilated surface away from heat sources and flammable/explosive material. [P003]
- Power off before cleaning and never connect or disconnect wiring while energized. Wait at least 30 minutes after switch-off before touching hot parts. [P003]
- Disconnect original CFS before servicing; keep it dry. Damaged cable, liquid/rain exposure, and internal/electrical failures require qualified service. Covered internal parts are not user-serviceable. [P023]
- Do not open a power supply, probe mains/heater circuits, bypass a sensor, root the printer, install alternative firmware, or invent a connector/pinout/test point.

## Confirmed component evidence versus permitted action

The base-K2 manual/parts catalog identifies an AI monitoring camera, auto leveling/strain-gauge component, filament-break detection, cutter, hotend, heat-break fan, back/side/filter-exhaust fans, air filter, and accessible external power/communications context. Identification in a parts diagram does not authorize removal or electrical diagnosis. [P003] [P007]

| Area | Applies to | Permitted from captured evidence | Tools/parts | Validation | Stop/escalate | Sources |
|---|---|---|---|---|---|---|
| Fans | confirmed base K2 | Clean weekly with power off; inspect accessible blockage/damage | Exact tools/SKUs not captured | Controlled restart: fans turn without rubbing/noise/error | Blade/cable damage, seized fan, inaccessible debris, repeat error, unknown cover/fastener | [P027] |
| Air filter | confirmed base K2 | Replace every 300 print hours per manual or around three months at eight hours/day; monthly under frequent use per maintenance page | Exact filter SKU/tool not captured | Correct seating, unobstructed path, normal controlled fan behavior | Unknown part/orientation/access, damaged housing, absent model-specific procedure | [P003] [P027] |
| Camera | confirmed base K2 | Clean dirty/blurry lens with lint-free cloth and alcohol; inspect weekly with ABS | lint-free cloth; alcohol | Image becomes clear after controlled restart | Liquid ingress, loose/scratched lens, no image after cleaning, network/app-only fault | [P033] |
| Leveling/strain gauge | confirmed base K2 component | Run normal auto leveling; inspect only visible obstruction while off/cool | No replacement tool/part captured | Calibration completes and supervised first layer passes | Repeat sensor/calibration error, nozzle/bed collision, loose/damaged component, wiring access | [P003] [P007] |
| Filament-break detection | confirmed base K2 component | Observe error and accessible filament path; use normal load/unload | No replacement procedure/SKU captured | Correct state after supervised load/unload | Repeat false state, damaged sensor/cable, internal access | [P007] |
| Firmware | exact confirmed model/board only | Read and record installed versions; compare to live official listing | No installation action authorized | If separately authorized, record before/after versions and complete official post-update calibrations | Model/board mismatch, unsigned/unofficial file, power instability, update error | [P017] [P018] [P019] [P020] [P021] [P035] [P036] |

K2 Plus has two documented cameras and an activated-carbon filter on its model-specific maintenance page; do not use those facts to identify or service base K2. [P034]

## Thermal or sensor error

1. Stop heating/motion through normal controls if responsive.
2. Power off, unplug, and let hot parts cool. If smoke, fire, liquid, or damaged mains wiring makes approach unsafe, follow local emergency procedure instead of touching the machine.
3. Record exact error text, model label, installed firmware, commanded and displayed temperatures, when the fault occurred, and visible damage—without opening protected covers.
4. Check only user-accessible obstruction, seated external cable that the manual explicitly permits handling while de-energized, and obvious damage. Do not reseat an unidentified connector.
5. Do not bypass the sensor, increase a limit, flash firmware, probe resistance/voltage, or restart repeated heating attempts.
6. Escalate repeated thermal/sensor faults, damaged wiring, heater instability, liquid ingress, odor/smoke, or any internal access to Creality support or qualified service.

## Camera or network symptom

Separate optical, application/network, and hardware failure:

1. Record whether the camera has no image, an obscured/blurry image, intermittent image, or only remote-access failure.
2. For a confirmed base K2 and only a dirty/blurry lens, use P033 while powered off and cool.
3. After restart, observe the local/device status without changing firmware or network configuration.
4. If the lens is clear but the image is absent/intermittent, record firmware, application/version, network context without exposing credentials, and exact error.
5. No model-specific camera replacement, cable procedure, or network-reset sequence was captured. Do not invent one; use official support.

## Firmware observation, not update

On 2026-08-20 the public listing showed K2/K2 Pro V1.1.6.7 for CR0CN200400C10, K2 Plus V1.1.6.4 for CR0CN240110C10, and K2 SE V2.3.6.77 for CR4CU220812S12K1. These values are dated observations, not proof of the installed version, not a stability guarantee, and not an instruction to update. The K2/K2 Pro API subtype mapping was inconsistent, making the physical label and board/filename combination essential. [P017] [P018] [P019] [P020] [P035] [P036]

Any firmware update requires separate authorization, exact-model/board/image verification, filament retraction as directed, uninterrupted suitable power, and post-update input shaping and automatic leveling. No update was performed during research. [P021]
