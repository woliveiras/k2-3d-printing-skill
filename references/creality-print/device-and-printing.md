# Device and printing

## Observation and authority boundary

The installed application was not launched. No Device page, account, printer, device address, firmware, camera, file, history, timelapse, LAN/cloud state, CFS, or print control was opened. The labels below come from official 7.2.1 source/localization and official Wiki documentation. A localization string proves a potential label, not availability on a particular printer or firmware. [C017] [C023]

Do not send, start, pause, stop, continue, reprint, feed/retract filament, or otherwise control a printer without separate authorization for that exact device and action.

## Device page areas

Enter through the top navigation label `Device`. Current localization defines these areas: [C005] [C017]

| Area/path | Exact labels | Runtime dependencies | Unit/default/effect boundary |
|---|---|---|---|
| `Device` → device list | `Device group`, `Device State`, `Device Type`, `Add Group`, `Scan Add`, `Manual Add`, `Current Device`, `Details` | Network path, discovered/added devices, account/LAN state | No default or exact list layout observed. Do not expose private addresses or names. |
| `Device` → current device → `Details` | `Printing Information`, `Control`, `File`, `Records`, `Timelapse Video`, `Camera` | Model, firmware, connection, permissions, current state | Exact tabs/placement and per-device availability unconfirmed. |
| Printing information | `Temperature`, `Layer`, `Printing time`, `Remaining time`, `Finish Time` | Active job and device telemetry | Units and default displays were not observed. Treat estimates as estimates. |
| Speed/control | `Ultrafast`, `Standard`, `Stable`, `Silent`, `Printing speed`, `Pause`, `Stop`, `Continue` | Active state, printer capability, firmware | These actions mutate a live job. No mode multipliers/defaults were confirmed. |
| Files/history | `Print File`, `Historical Records`, `Delayed Photography`, `Start printing`, `Start Printing (Calibrate First)`, restart/reprint, rename, delete | Stored file/history and printer state | Exact confirmation sequence and retention behavior unconfirmed. |
| Camera/timelapse | `Camera`, `Timelapse Video` | Camera-equipped compatible device, firmware, network | No stream, camera control, retention, or privacy behavior observed. |

Current localization also contains `Model fan`, `Case fan`, `Side fan`, and `LED`. Units, ranges, defaults, control paths, and availability were not confirmed for the physical printer. Do not invent a path from a string. [C017]

## Slice, export, send, and print actions

Current 7.2.1 source keeps these operations separate: [C011]

| Action | Source-confirmed path/label | Effect | Visibility dependencies | Authority |
|---|---|---|---|---|
| Slice current plate | `Prepare` → `Slice plate` | Generates toolpaths and opens Preview | Valid model/plate | Allowed as analysis only when not controlling hardware |
| Slice every plate | `Prepare` → slice dropdown → `Slice all` | Generates all plate toolpaths | Multi-plate project | Same |
| Export | post-slice action/dropdown → `Export G-code`, `Export all sliced file`, or `Export G-code file` | Writes a local export | Valid slice and selected output | File creation requires task scope; does not control printer |
| Transfer only | post-slice action/dropdown → `Send` / `Send all`, or send page → `Send Only` | Uploads/transfers without starting | `Send` hidden for unsupported third-party hosts; device/network required | Separate explicit authorization required |
| Print | post-slice → `Print plate` / `Print all` → send page → `Start Print` | Transfers and starts machine execution | Valid compatible device, mapping, connection, state | Separate explicit authorization required |
| Multi-device | post-slice dropdown → `Send to Multi-device` | Targets multiple enabled devices | Multi-machine feature enabled | Separate explicit authorization for every target |

The exact button placement was not visually observed. `Send` is suppressed in current source for third-party hosts that do not use the supported Creality network path; do not reuse a Creality path for a foreign printer/profile. [C011]

## Send page

The 7.2.1 send-page localization defines: [C014]

- `Start Print` and `Send Only`;
- `Print Device`, `My Device`, `Current Device`;
- `Filament Device`, `CFS`, `Spool Holder`, `Enable CFS`;
- `Print Calibration`;
- `Sliced Plate`, `Single Plate`, `All Plates`;
- `Model Color / Filament`, `Box Color / Filament`;
- `Local Network`, `Internet(Creality Cloud)`, `Local Device`, `Creality Cloud Device`;
- `File Name`.

It also contains warnings for printer/preset mismatch, missing filament mapping, camera operation, and an uncleared print platform. Read the live message before acting; do not paraphrase a hidden or unseen warning as a confirmed device state.

If any filament remains unmapped, the localized message says only sending is supported. Do not treat `Send Only` as permission to start later, and do not map by color alone.

## Pre-print checks

Before any authorized `Start Print`:

1. Confirm physical printer identity and current device.
2. Confirm printer/nozzle/plate/process/filament preset match.
3. Confirm the correct sliced plate(s), filename, and destination.
4. Review full Preview with Lite Mode disabled where required.
5. Confirm CFS/spool-holder mapping, support filament, purge/tower, and material amount.
6. Confirm the plate is clear and correctly installed from direct observation; do not rely solely on AI camera analysis.
7. Confirm the user explicitly authorizes `Start Print` rather than `Send Only` or export.

Creality 7.2.0 describes AI pre-print camera inspection for leftover parts, debris, and foreign objects and tells users to review the captured image before confirmation. Treat this as assistance, not a safety guarantee. [C016]

## Unconfirmed paths

The exact firmware-update route, update controls, device-specific camera/history/timelapse availability, remote-control layout, network configuration, and error-recovery screens were not confirmed. Do not install software, update firmware, or open a live Device control merely to resolve documentation without separate authorization.
