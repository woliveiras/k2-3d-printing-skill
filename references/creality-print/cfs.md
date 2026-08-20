# CFS

## Compatibility gate

Do not infer CFS compatibility from a Creality Print profile, `single_extruder_multi_material=1`, a CFS button, or localization strings. Confirm the physical printer model, firmware, CFS model, connection, and official compatibility before device-specific instructions.

The installed 7.2.1 profile tree has no `K2C` profile. A `Creality K2` profile cannot prove that a printer described by the user as `K2C` supports CFS. [C023]

No connected device or CFS was observed in this research.

## Device Details controls

Creality's CFS Wiki, updated 2025-04-29, places CFS functions in the printer's Device Details page. Current 7.2.1 localization supplies matching control labels. [C017] [C022]

| Task | Documented path/label | Mode/scope | Unit/default | Effect and risk |
|---|---|---|---|---|
| View RFID filament | `Device` → current CFS printer → `Details` → CFS slot | Device context, RFID spool | Units/default unconfirmed | Displays color, material type, remaining amount, and details for Creality RFID filament. Read data as reported; verify the physical spool. |
| Edit non-RFID filament | Device Details → select non-Creality-RFID/other slot → edit filament information | Device context | `Brand`, `Type`, `Color`, `Nozzle temperature`, and the source's exact `Pressure in advance` label exist; units/defaults unconfirmed | Wrong material or temperature metadata can produce unsafe/failed slicing. Do not silently normalize the awkward pressure label when navigating. RFID information is documented as non-editable. |
| Feed filament | Device Details → select slot → `Feed` | Live device action | Unconfirmed | Moves/heats hardware as required by the device; needs separate explicit authorization. |
| Retract filament | Device Details → select slot → `Retract` | Live device action | Unconfirmed | Moves/heats/cuts hardware as required; needs separate explicit authorization. |
| Configure box | Device Details → `Settings` → `Filament box setting` | CFS device settings | No defaults observed | Controls automatic reading/feeding behavior; changes live device configuration. |
| Read humidity | Device Details → `CFS Humidity` / humidity reading | Device telemetry | Numeric unit/ranges unconfirmed; source labels include `Normal`, `High`, `Too high` | Do not convert the label into a drying prescription or absolute RH without a visible value/manual. |
| Configure refill | Device Details → filament-box settings → `Automatic refill` | CFS device settings | Default unconfirmed | Wiki says it switches to another available spool with exactly matching properties when the active spool is depleted. Validate every matching field. |
| Switch CFS unit | Device Details → select the corresponding CFS on the right | Multiple connected CFS units | Not applicable | Exact placement unobserved; confirm the unit and slot before acting. |

Current localization also contains `Detection on insertion`, `Detection at startup`, and `Automatic feeding system`. The official Wiki describes automatic information reading and feeding controls, but exact defaults and supported firmware were not observed. [C017] [C022]

## Auto Mapping in Prepare

The official path is:

1. Open `Device`.
2. Set the CFS-connected printer as `Current Device`.
3. Return to the Prepare filament section.
4. Select `Auto Mapping` to map CFS slots sequentially to filament presets. [C022]

This path is official 2025 documentation, not a visually confirmed 7.2.1 path. If `Auto Mapping` is absent, verify physical compatibility, connection, current-device state, firmware, version, and filament-panel context before declaring it unavailable.

After automatic or manual mapping, compare:

- physical slot and spool;
- brand/product, material type, color, and diameter;
- nozzle-temperature range and any pressure-advance metadata;
- support-material pairing;
- available amount;
- model and purge/tower assignment in Preview.

Never accept color similarity as material compatibility.

## Send page mapping

The 7.2.1 send page distinguishes `CFS` from `Spool Holder`, `Model Color / Filament` from `Box Color / Filament`, and exposes `Enable CFS`. It reports that unmapped filaments support only sending. [C014]

Treat these as separate decisions:

- `Send Only`: transfer without starting;
- `Start Print`: execute the job;
- `Enable CFS`: select the multi-material source path;
- spool holder: use the external/single-spool path shown by the device.

Each live action needs explicit authorization. A completed mapping does not authorize sending or printing.

## Screenshot rules

For a CFS screenshot, record software version, current device, CFS unit and slot, RFID/manual state, exact visible material fields, humidity label/value, and print state. Do not expose serials, device addresses, network identifiers, or account details. Request another screenshot only if a hidden field changes compatibility or the intended action.
