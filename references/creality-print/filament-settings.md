# Filament settings

## Evidence boundary

Current source contains the dialog labels `Filament settings` and `Edit Filament`. The official older interface page documents a multi-color filament preset area that can select, add, delete, and assign filaments. The running 7.2.1 panel, selected preset, field values, units, defaults, and CFS state were not observed. [C006] [C018] [C025]

## Locate and manage presets

| Task | Version-scoped path | Mode/scope | Dependency | Status |
|---|---|---|---|---|
| Select a filament preset | `Prepare` → filament preset panel → select preset | Not controlled by Process `Global`/`Objects` | Active printer preset and available catalog | General area officially documented; exact 7.2.1 click target visually unconfirmed |
| Edit a filament preset | `Prepare` → filament preset edit control → `Filament settings` / `Edit Filament` | Preset editor; not Process scope | Preset editability and user role | Exact dialog labels source-confirmed; icon/location unconfirmed |
| Add a system filament preset | `Prepare` → `Add/Delete Materials` or filament gear → `System Consumable` → check material → `Confirm` | 6.2 `Expert` path; System selection may be omitted in Basic | Version and role | Official 6.2 Wiki only; verify labels in 7.2.1 [C021] |
| Assign filament to a model | `Prepare` → multi-color filament panel / Object Management | Object assignment, distinct from process override | Multiple filament entries and selected object | Older official Wiki; exact 7.2.1 gesture unconfirmed [C018] |
| Map connected CFS slots | Set CFS printer as current in `Device` → return to Prepare filament section → `Auto Mapping` | Device-backed mapping | Compatible connected device and CFS | Official CFS Wiki, updated 2025-04-29; not observed locally [C022] |

Current source uses `Basic`/`Professional` under `Preferences` → `User Role`. Replace the 6.2 documentation's `Expert` label with `Professional` only after confirming the current screen; do not silently rewrite other 6.2 paths. [C010] [C021]

## Preset classes

The 6.2 Wiki defines three preset origins:

- **System:** built into the software; cannot be deleted; edit then `Save As` another type.
- **Project:** stored with the project; the documented process-project limitations may differ from printer/filament projects.
- **User:** local or account-associated depending on login and sync state. [C021]

Because cloud/account state was not observed, do not promise that a user preset is local, synchronized, or available on another machine. `Auto sync user presets(Printer/Filament/Process)` is conditional on the cloud build in 7.2.1 source. [C010]

## Required value record

Before recommending or changing a filament field, record:

- exact preset name and origin;
- filament manufacturer, product/grade, color, and diameter;
- exact English label, path, current value, unit, and visible default;
- printer/nozzle/plate/process compatibility shown by the active project;
- exact TDS/SDS range and hardware limit from the material references;
- interaction with temperature, cooling, flow, maximum volumetric flow, retraction, chamber/enclosure, and CFS;
- Preview view and physical calibration that will validate the change.

No temperature, flow, cooling, retraction, or CFS field default was observed in the running 7.2.1 UI. Never convert a bundled preset or manufacturer range into a universal default.

## Mapping and send checks

The 7.2.1 send-page strings distinguish:

- `Model Color / Filament` from `Box Color / Filament`;
- `CFS` from `Spool Holder`;
- `Enable CFS`;
- `Current Device`;
- `Send Only` from `Start Print`. [C014]

The send page states that unmapped filaments permit only sending. Before printing, verify each model filament against the intended CFS slot or spool holder, material type, color, nozzle/temperature range, available amount, and support-material pairing. Do not use a matching color as proof of matching material.

## Authority and validation

- Selecting or editing a preset does not confirm physical material compatibility.
- A bundled K2-family filament preset does not identify the physical printer.
- Do not overwrite an original 3MF when applying authorized changes.
- Do not feed/retract CFS filament, send a file, or start a print without separate authorization.
- Re-slice after a preset or mapping change and inspect Filament, Temperature, Fan Speed, Flow, tool changes, purge/tower, and material totals in Preview.
