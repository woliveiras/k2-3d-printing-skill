# Maintenance and safe repair index

Load this index plus one subsystem file. Do not load every maintenance file unless the symptom crosses subsystems.

| Need | Read |
|---|---|
| Schedule by print hours, filament, elapsed time, material, or symptom | [Preventive schedule](preventive-schedule.md) |
| Rails, shafts, screws, surface cleaning, and lubricant evidence | [Cleaning and lubrication](cleaning-and-lubrication.md) |
| Nozzle, hotend, extruder, clog, cutter, or wiper | [Nozzle, hotend, and extruder](nozzle-hotend-extruder.md) |
| Belts, pulleys, rails, shafts, lead screws, layer shift, or abnormal motion | [Motion system](motion-system.md) |
| Plate, first layer, automatic leveling, or vibration calibration | [Bed and calibration](bed-and-calibration.md) |
| Original CFS, CFS-C, spool, PTFE, desiccant, or feed path | [CFS and filament path](cfs-and-filament-path.md) |
| Fans, filters, camera, sensors, firmware, network, cable, or electrical issue | [Electronics, fans, and sensors](electronics-fans-sensors.md) |
| Symptom-first routing | [Troubleshooting trees](troubleshooting-trees.md) |

## Mandatory procedure contract

Before giving or following a maintenance procedure:

1. Confirm the physical printer and accessory identity using [printer identity](../printer-identity.md). `K2C` and a slicer profile are not sufficient evidence.
2. Open the cited official procedure live. Confirm model, hardware revision, required tools, parts, consumables, safe state, exact fastener location, and post-service test.
3. State the procedure's source ID, applicability, revision/access date, risks, tools, parts, safe state, ordered steps, inspection, validation, stop criteria, and service-escalation criteria.
4. Use the source's safe state. Otherwise stop motion normally, remove filament only when directed, power off, unplug, and let hot parts cool. The researched K2 manual says to wait at least 30 minutes after switch-off before touching hot parts. [P003]
5. Treat controlled hot or energized service as an exception allowed only by an exact model-specific official step. Isolate burn and motion hazards and return to powered-off/unplugged state immediately after the required measurement or release operation.
6. Never invent torque, lubricant, part number, screw position, connector, cable route, test point, or disassembly step. Never use a part from another K2 variant by resemblance.
7. Stop at mains input, power supply, heater wiring, damaged insulation, liquid ingress, smoke, burning odor, repeated thermal/sensor faults, inaccessible electronics, or any instruction/source conflict that can change safety or hardware compatibility. Escalate to Creality support or qualified service.
8. Validate at the lowest-risk level: visual inspection while off and cool; controlled power-on self-test; model-supported calibration; then a small supervised test print. Never declare repair success before its acceptance test passes.

## Evidence labels

- `Official`: directly stated for the exact model/accessory in a cited Creality source.
- `Conditional`: official for a named model but physical identity is not yet confirmed.
- `Conflict`: official sources disagree or differ in scope/date; preserve both.
- `Unconfirmed`: not captured in a model-specific official source; do not perform or fabricate.
- `Physically validated`: the actual machine passed the stated post-maintenance test; documentation alone cannot establish this.

## Authority boundary

Maintenance guidance does not authorize firmware updates, printer control, starting a print, buying a part, opening protected electrical covers, root access, sensor bypass, or electrical modification. Ask for separate authorization where the action is otherwise safe and supported; refuse to improvise unsafe or unsupported work.
