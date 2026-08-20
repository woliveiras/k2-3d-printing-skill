# Creality Print reference index

Use this section only after identifying the Creality Print version and separating the selected slicer profile from the physical printer identity.

## Evidence boundary

The baseline combines official `v7.2.1` source with a read-only Creality Print `7.2.1.5476` macOS arm64 bundle snapshot captured on 2026-08-20. It includes no running UI or connected-device state. Recheck the official release and identify the target installation before version-sensitive navigation. [C001] [C002] [C003] [C023]

The version-scoped profile catalog contains `Creality K2`, `Creality K2 SE`, `Creality K2 Pro`, and `Creality K2 Plus`, but no `K2C` string. Never use a profile to prove the physical model or silently translate `K2C` into another K2-family name. [C023]

## Route by task

| Task | Read |
|---|---|
| Confirm version; distinguish AI/Pro, Basic/Professional, and Lite Mode | [Version and modes](version-and-modes.md) |
| Import and arrange a model; locate Prepare areas | [Prepare](prepare.md) |
| Change global or per-object process settings | [Process settings](process-settings.md) |
| Select, add, edit, or map filament presets | [Filament settings](filament-settings.md) |
| Select or inspect a printer preset | [Printer settings](printer-settings.md) |
| Find automatic/manual support controls | [Support settings](support-settings.md) |
| Inspect sliced toolpaths and statistics | [Preview](preview.md) |
| Distinguish export, send, start-print, and Device controls | [Device and printing](device-and-printing.md) |
| Locate source-confirmed calibration menus | [Calibration screens](calibration-screens.md) |
| Inspect CFS mapping and device-side CFS controls | [CFS](cfs.md) |
| Handle label, location, and availability changes | [Version differences](version-differences.md) |

## Navigation rule

1. Record the exact Creality Print version and platform.
2. Record the visible page: `Online Models`, `Prepare`, `Preview`, or `Device`.
3. Record the `AI`/`Pro` edition, `Basic`/`Professional` user role, `Global`/`Objects` state, selected object/part/layer, and Preview `Lite Mode` state when relevant.
4. Follow a 7.2.1 path only when it is source-confirmed here or visible in the user's screenshot.
5. Label older Wiki paths with their documented version/date. If a control cannot be located, mark it `not confirmed for this version` and request a version or screenshot only when indispensable.
6. Never infer a line type or value from color without the active Preview legend.

## Control-record rule

For any requested control, report:

- exact English label;
- page and click path;
- tab/subsection;
- required edition and user role;
- `Global` or `Objects` scope;
- visibility prerequisites;
- unit and default only when visible or source-confirmed for that exact version/profile;
- effect, risk, interactions, and Preview validation;
- evidence ID and observation state.

Use `unconfirmed` instead of filling any missing field from memory.
