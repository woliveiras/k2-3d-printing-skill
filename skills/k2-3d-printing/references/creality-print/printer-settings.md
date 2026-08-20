# Printer settings

## Identity gate

Treat the active printer preset as configuration evidence only. Confirm the physical model from its label or About screen before using build volume, hotend, nozzle, bed, chamber, CFS, firmware, maintenance, or repair claims.

The installed 7.2.1 profile tree contains no `K2C` string. If the user says `K2C`, do not select `Creality K2` or another family profile as a substitute. Stop only the hardware-specific recommendation and ask for the physical model label or printer About screen. [C023]

## Bundled K2-family inventory

The counts below are observed local resource records, calculated by exact `printer_model` or `compatible_printers` match. Nozzle counts exclude the separate machine-model descriptor. [C023]

| Bundled model | Nozzle presets | Process presets | Filament presets |
|---|---:|---:|---:|
| `Creality K2` | 4: `0.2`, `0.4`, `0.6`, `0.8` | 10 | 54 |
| `Creality K2 SE` | 1: `0.4` | 3 | 20 |
| `Creality K2 Pro` | 4: `0.2`, `0.4`, `0.6`, `0.8` | 10 | 62 |
| `Creality K2 Plus` | 4: `0.2`, `0.4`, `0.6`, `0.8` | 27 | 154 |

These counts show bundled slicer coverage, not official physical compatibility.

## Locate and edit a printer preset

| Task | Path | Mode/scope | Dependencies | Observation state |
|---|---|---|---|---|
| Select a printer | `Prepare` → printer preset selector | Project-level preset; not Process `Global`/`Objects` | Installed catalog | Area officially documented; exact 7.2.1 selector placement not visually observed [C018] |
| Add/remove a printer | `Prepare` → printer selector/control → `Select/Remove Printer` | Preset management | Build and catalog | Dialog title is current-source-confirmed; click icon unconfirmed [C025] |
| Edit selected printer | `Prepare` → printer preset → edit control → `Printer settings` | Printer preset editor | Preset editability and role | Dialog label current-source-confirmed; icon/location unconfirmed [C006] |
| Add a system printer preset | `Select/Remove Printer (System Preset)` or printer gear → `System` → check printer → `Confirm` | Official 6.2 `Expert` workflow | Version and role | Version-scoped; verify 7.2.1 labels [C021] |
| Save a derived preset | Open editable system/user preset → modify → `Save As` | Project or user preset | Origin and version | Official 6.2 workflow; exact current choices unconfirmed [C021] |

Current 7.2.1 uses `Professional` instead of the older Wiki's `Expert`. Do not assume every remaining 6.2 label migrated unchanged. [C010]

## Observed raw K2 0.4 profile fields

The installed `Creality K2 0.4 nozzle` JSON declares the following. Preserve the raw field name and evidence class when mentioning a value. [C023]

| Raw field | Bundled value | What it does not prove |
|---|---|---|
| `printer_model` | `Creality K2` | Physical printer identity |
| `printable_area` | `0x0,260x0,260x260,0x260` | Official measured build area of an unconfirmed unit |
| `printable_height` | `260` | Official height of an unconfirmed unit |
| `nozzle_diameter` | `0.4` | Installed nozzle diameter |
| `nozzle_type` | `hardened_steel` | Supplied or currently installed nozzle material |
| `min_layer_height` / `max_layer_height` | `0.08` / `0.32` | Universal printable range for every material/nozzle/profile |
| `single_extruder_multi_material` | `1` | Physical CFS compatibility |
| `machine_ptc_exist` | `1` | Official chamber hardware or safe chamber temperature |
| `support_chamber_temp_control` | `0` | Complete physical chamber behavior |
| default process | `0.20mm Standard @Creality K2 0.4 nozzle` | Best process for a particular part |
| default filament | `Hyper PLA @Creality K2 0.4 nozzle` | Loaded material or universal recommendation |

The model descriptor associates PLA, PETG, ABS, ASA, TPU, PLA-CF, and other generic/Creality presets. Association is not an official support, safety, or CFS statement. Confirm each material against the physical printer and exact filament documentation.

No displayed printer-setting unit, UI default, tooltip, editability, or disabled state was observed. Raw JSON values must remain labelled `observed bundled profile value`, never `official hardware limit`.

## Cross-check before slicing or sending

1. Confirm physical model and installed nozzle.
2. Confirm selected printer and nozzle preset.
3. Confirm plate type and printable bounds.
4. Confirm the process and filament preset are intended for that printer/nozzle.
5. Inspect imported 3MF printer provenance; do not accept a foreign preset automatically.
6. Slice and verify bounds, first layer, toolpaths, temperatures, flow, acceleration, and material mapping.

The 7.2.1 send-page strings include `The current printer does not match the preset settings of the selected printer`. Treat that warning as a stop condition until the physical device and preset are reconciled. [C014]
