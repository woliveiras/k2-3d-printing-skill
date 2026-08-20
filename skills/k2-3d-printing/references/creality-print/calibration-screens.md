# Calibration screens

## Stable 7.2.1 menu

On macOS, current source adds `Calibration` to the native menu bar. The stable entries below are enabled only while `Prepare` and the 3D editor are active. [C011]

| Exact path | Source-defined effect | Unit/default | Applicability and risk |
|---|---|---|---|
| `Calibration` → `Temperature` | Opens Temperature Calibration | Dialog values and units were not visually observed | Stay inside confirmed printer, hotend, nozzle, plate, and exact filament TDS limits. |
| `Calibration` → `Flow rate` → `Pass 1` | Starts the first flow-rate calibration workflow | Unconfirmed | Use the named printer/nozzle/filament/process and record the selected result. |
| `Calibration` → `Flow rate` → `Pass 2` | Opens the second/high-flow-rate dialog | Unconfirmed | Do not assume Pass 2's range or interpretation from another version. |
| `Calibration` → `Pressure advance` | Opens the pressure-advance dialog | Unconfirmed | Use only when the exact printer/firmware officially applies it. |
| `Calibration` → `Retraction test` → `Retraction distance test` | Opens retraction-distance test | Unconfirmed | Flexible and multi-material paths can require different constraints; do not copy a universal range. |
| `Calibration` → `Retraction test` → `Retraction speed test` | Opens retraction-speed test | Unconfirmed | Remain inside extruder/material limits and validate feeding. |
| `Calibration` → `Tolerance Test` | Creates/loads the bundled tolerance-test model in a new project | Model dimensions/default workflow unconfirmed | Confirm the new-project prompt and do not discard unsaved work. |
| `Calibration` → `Max flowrate` | Opens maximum-volumetric-speed test | Unconfirmed | Stop below hardware/TDS limits; validate for exact filament batch/nozzle. |
| `Calibration` → `Tutorial` | Opens Creality's calibration help URL | Not applicable | Documentation path may redirect or differ by language/version. |

The source path is current, but none of these dialogs was opened or executed. Internal dialog validation code is not an official physical-printer limit and must not be cited as one.

## Alpha-gated entries

The tagged stable source places these entries inside `isAlpha()`:

- `VFA`;
- `Speed calib` → `Limit speed`, `Speed tower`, `Jitter speed`, `Fan speed`;
- `Acceleration calib` → `Limit acceleration`, `Acceleration tower`, `Deceleration acceleration`;
- `Arc fitting test`. [C011]

Do not provide these as stable 7.2.1 paths unless the user's exact build visibly exposes them. The official 6.x calibration Wiki lists VFA, which conflicts with stable 7.2.1 source availability; preserve the conflict and prefer the exact current stable source for the UI path. [C019]

## When the menu is missing or disabled

1. Confirm version and platform.
2. Select `Prepare`; Preview and Device do not satisfy the stable enable condition.
3. Confirm a valid 3D editor/project state.
4. Confirm AI/Pro edition and Basic/Professional role if the surrounding UI differs.
5. Check the macOS native menu bar rather than searching only inside the canvas.
6. If still absent, mark it `not confirmed for this build` and request a screenshot/version; do not invent a toolbar path.

## Calibration sequence and validation

Generate only the calibration needed for the current uncertainty. A proportional sequence is first layer, temperature, flow, officially applicable pressure advance, maximum volumetric flow, retraction/stringing, bridges/overhangs, dimensional tolerance, then vibration/input shaping only when officially supported by the physical printer/firmware.

For every calibration:

1. Record physical printer identity, firmware, nozzle, plate, filament product/batch, drying state, ambient conditions, and starting preset.
2. Record exact dialog labels, values, units, and test geometry from the visible screen.
3. Reject values exceeding any official hardware or material limit.
4. Slice and inspect the calibration model in Preview.
5. Print only with separate authorization.
6. Measure the physical result and save the chosen value as an empirical result tied to those conditions.

The 6.x Wiki documents Temperature, two-pass Flow rate, Pressure advance, Max volume flow, and VFA concepts and directs users to inspect relevant Preview metrics after slicing. Use it as version-scoped method documentation, not evidence that every stable 7.2.1 menu item is present. [C019]
