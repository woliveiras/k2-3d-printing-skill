# Prepare

Use Prepare to import and arrange models, select printer/filament/process presets, apply object-specific configuration, and start slicing. The 7.2.1 UI was not launched during research; distinguish source-confirmed labels from the older official Wiki layout.

## Entry and exit

- Enter through the top navigation label `Prepare`. [C005]
- Use `Slice plate` for the active plate or `Slice all` for all plates. Current source switches to `Preview` after the slice action. [C011]
- Do not describe `Slice plate` as permission to print. Printing, sending, and export are separate post-slice actions.

## Model import

The 7.2.1 import filter includes 3MF, STL, OBJ, AMF, STEP/STP, and additional model formats. Preferences contains `Display Step Import Setting Dialog`. The macOS bundle registers Finder viewer associations for STL, OBJ, AMF, 3MF, CXPRJ, and G-code but not STEP; Finder association is not the import-support list. [C010] [C024] [C023]

| Control | Path | Mode/scope | Unit/default | Effect | Risk and validation |
|---|---|---|---|---|---|
| Model import | `Prepare` → import/open-model control | Edition-dependent presentation; not `Global`/`Objects` | Not applicable | Loads a model or project | Exact button label and pixel location in Pro edition were not visually observed. After import, verify units, scale, dimensions, object count, plate bounds, mesh warnings, and selected profiles. |
| `Import Model File` | AI workflow prompt → `Import Model File` | AI Edition, when no model is detected | Not applicable | Imports a local STL, OBJ, or another supported model | Officially described in 7.2.0; not visually observed in 7.2.1. [C016] |
| `Open New Project` | AI workflow prompt → `Open New Project` | AI Edition, when no model is detected | Not applicable | Opens a local 3MF project | Treat foreign printer/process settings as untrusted until inspected. [C016] |
| `Model Library` | AI workflow prompt → `Model Library` | AI Edition; service/login may be required | Not applicable | Browses online models | Network/account behavior was not observed. [C016] |

## Prepare toolbar

Creality's official interface page, created and updated 2024-06-01, documents the Prepare toolbar functions as import, add plate, move, rotate, scale, mirror, clone, support painting, and seam painting. It does not identify a 7.x version. Use these as older official functional labels, not as proof of 7.2.1 icon order or screen position. [C018]

For a screenshot-based instruction, distinguish the selected object, plate, modifier, support painter, seam painter, and transform gizmo. Units, defaults, keyboard shortcuts, and context-menu paths for these controls were not confirmed in this research.

## Preset areas

| Area | Source-confirmed label/path | Scope | Visibility dependencies | Continue in |
|---|---|---|---|---|
| Printer | `Prepare` → printer preset selector; current dialog title `Select/Remove Printer` [C025] | Project/printer preset; not physical identity | Selected vendor/profile and user role | [Printer settings](printer-settings.md) |
| Filament | `Prepare` → filament preset panel; edit surfaces include `Filament settings` and `Edit Filament` | Filament preset and plate mapping | Printer, number of filaments, CFS/device state | [Filament settings](filament-settings.md) |
| Process | `Prepare` → `Process` → `Global` / `Objects` | Project-wide or selected object context | User role, selection, part/layer context | [Process settings](process-settings.md) |

The older official Wiki calls the right-side areas Printer Presets, Multi-color Filament Presets, Object Management, and Process Presets. It says Object Management contains the plate, objects, and their used filaments. Use that description only as version-scoped documentation. [C018]

## Object and modifier context

Current source switches to per-object setting mode after adding a modifier and shows the instruction `Switch to per-object setting mode to edit modifier settings.` Choosing object process settings similarly switches to Objects and says `Switch to per-object setting mode to edit process settings of selected objects.` [C009]

Before changing an object override:

1. Confirm `Objects` is selected.
2. Confirm the intended object, part, modifier, or layer range is selected.
3. Record which value is inherited from `Global` and which is overridden.
4. Re-slice and compare the affected region in Preview.

## Source-versus-screen boundary

The exact running layout, scroll position, selected profiles, default values, toolbar icon order, and disabled states were not observed. If a path fails, check version, `AI`/`Pro`, `Basic`/`Professional`, `Global`/`Objects`, selection, prerequisites, search, and scrolling before marking the control unavailable.
