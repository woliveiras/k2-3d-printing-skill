# Failure diagnosis

Preserve evidence before changing settings: photograph the failure and plate, note the layer/time, physical model, firmware, profile names, nozzle/plate/material/feed path, temperatures, speeds, flow, fan, chamber/door state, material dry history, sounds/errors, and whether the fault repeats. Change one cause at a time.

| Symptom | Distinguish first | Ordered checks | Stop/escalate |
|---|---|---|---|
| No first-layer adhesion | no contact, contamination, wrong plate/profile, low adhesion, nozzle drag | cool plate; approved cleaning; correct plate/material; seating; nozzle; leveling/first-layer test; then permitted bed/nozzle/fan/adhesive | scraping, damaged coating, heater/sensor error |
| Warping/corner lift | first-layer release vs later shrinkage | plate prep/contact; brim/ears; avoid drafts; material-specific enclosure/chamber/door/fan; reduce solid mass and stress | material requires environment hardware cannot provide |
| Clog/no flow | empty/tangled spool, CFS path, extruder grind, partial nozzle clog, heat-creep | stop; inspect external path; use exact official unload/clear procedure; inspect nozzle/extruder only within service scope | heater/sensor/wiring, seized part, repeated thermal fault |
| Under-extrusion | intermittent feed vs high-flow-only | dry/material diameter; path/friction; gears; nozzle wear/clog; temperature; flow demand versus calibrated maximum | abrasive wear or hardware disassembly unconfirmed |
| Over-extrusion | wrong flow/diameter/profile vs first-layer squish | profile/material identity; filament diameter setting; calibrated flow; temperature; elephant foot separately | do not use flow to hide a mechanical/sensor problem |
| Stringing | wet material vs temperature/retraction/travel | dry per exact TDS; temperature tower; minimal direct-drive retraction; travel/wipe; flexible-feed stability | grinding/jam after retraction increase |
| Layer shift | loose motion/transmission, collision, acceleration, obstruction | stop; inspect collision evidence and belt/pulley/rails only by official procedure; reduce unsupported/tall acceleration after mechanics pass | impact, damaged belt/pulley, unknown tension/torque |
| Ringing/ghosting | mechanical play vs commanded acceleration | stable surface; official belt/fastener inspection; external-wall acceleration; official vibration routine if supported | loose/damaged motion part or abnormal noise |
| Delamination | material/environment vs low temperature/excess fan/load orientation | exact TDS; dry material; enclosure/door/chamber; temperature/fan within limits; rotate load; thicker transitions | required chamber/nozzle exceeds hardware |
| Spaghetti | initial adhesion, later detachment, unsupported island, part collision | stop; recover evidence; inspect Preview at first failed layer; adhesion/support/tall stability; camera is not proof of prevention | repeated collision or hardware damage |
| Nozzle collision/scrape | warped part, over-extrusion, loose nozzle/hotend, bad Z, travel | stop immediately; power/cool; inspect part/plate/nozzle externally; Preview travels and warping; official mechanical inspection | hotend looseness, bent part, sensor/leveling fault |
| Abnormal noise | fan, CFS/extruder, belt/pulley, linear/Z motion, impact | stop motion; localize only from safe external observation; remove debris after power/cool; follow official subsystem procedure | mains/electronics, grinding, smoke, heat, repeated impact |
| Thermal error | open/short sensor, heater unable to track, fan/environment, firmware | stop; power off/unplug; let cool; record exact code and conditions; use official model code/procedure | never bypass sensor; use service for heater/wiring/electronics |
| Sensor error | transient obstruction vs connection/hardware | record exact code; safe restart only if official; clean externally accessible sensor as directed | repeated error, connector/wiring/access panel required |
| CFS jam/feed fault | spool tangle, incompatible filament, path obstruction, cutter/buffer/extruder | stop automatic retries; identify CFS vs CFS-C and material; follow exact unload/path procedure | flexible/brittle/wet-softened material, cutter/drive disassembly |
| Camera/network issue | local printer works vs UI/account/LAN/WAN only | do not alter printing safety state; record app/firmware/network scope; check official status and non-destructive reconnect steps | do not reset/update/control remotely without authorization |

After any correction, run the smallest safe validation: first-layer patch, extrusion line, calibration coupon, dry motion check only when official, or short non-critical print. Report whether the symptom disappeared, changed, or remains intermittent; do not call intermittent success a repair.
