# Version differences

Use the exact observed version for navigation. Do not silently merge labels or paths from different releases.

## Dated comparison

| Version/source date | Observed or official difference | Navigation consequence |
|---|---|---|
| Official interface page, 2024-06-01 | Documents `Prepare`, `Preview`, and `Device`; Prepare toolbar; printer, multi-color filament, object, and process areas | Use for general areas only. It predates 7.x AI edition and cannot prove 7.2.1 icon order or location. [C018] |
| Creality Print 6.2 documentation, 2025-07 | Introduces Preview `Lite Mode`; preset documentation uses `Expert` / `Basic` | Current 7.2.1 source uses `Professional` / `Basic`. Keep 6.2 preset paths version-labelled. [C020] [C021] |
| Creality Print 7.0.0, published 2025-12-29 | Adds AI Smart Analysis for support detection/recommendation when AI Cloud Service is enabled | Record service dependency; do not use AI analysis as Preview or physical validation. [C015] |
| Creality Print 7.2.0, published 2026-06-30 | Introduces AI Edition and Professional Edition first-run choice and upper-right Prepare switch; adds guided import, CFS mapping, print-risk analysis, pre-print camera inspection, color mixing, and other workflow changes | Ask which edition is visible. Pro retains full parameters; AI actions must be reviewed. [C016] |
| Creality Print 7.2.1, published 2026-08-04 | Adds context-aware AI, 17 more AI-recommendable process parameters, and fixes relevant Prepare/support/G-code/camera/settings defects | Use current source labels, but validate every AI-applied value and Preview result. [C003] [C004] |

## Confirmed label differences

| Concept | Older documented label | 7.2.1 source label | Rule |
|---|---|---|---|
| Advanced user role | `Expert` | `Professional` | Use the label visible in the user's version; do not rewrite an older click path without checking it. [C010] [C021] |
| Guided versus full workflow | Not present in 2024 interface documentation | `AI` / `Pro`; tooltip `Switch AI/Pro mode` | Keep distinct from User Role. [C005] [C016] |
| Preview memory reduction | Introduced as `Lite Mode` in 6.2 | Still source-defined as `Lite Mode` in 7.2.1 | It changes rendering only and requires re-slicing when toggled. [C012] [C020] |

## Availability conflicts

The 6.x calibration Wiki lists VFA. Stable tagged 7.2.1 source places `VFA`, `Speed calib`, `Acceleration calib`, and `Arc fitting test` behind `isAlpha()`. Prefer stable 7.2.1 source for availability and mark the older Wiki path version-limited. [C011] [C019]

The current source contains conditional controls:

- `Custom` Preview view depends on a compile flag and is hidden in raw G-code-only Preview. [C012]
- cloud preferences such as preset sync and Default Page depend on the cloud build. [C010]
- Device, CFS, camera, history, timelapse, send, and print controls depend on model, firmware, connection, service, profile, and state. [C014] [C017]
- `Send` is hidden for unsupported third-party print hosts. [C011]

Do not classify a conditional control as removed merely because it is not visible.

## Unobserved 7.2.1 screens

The application was not launched during the 2026-08-20 research. These remain visually unconfirmed:

- About and first-run edition chooser;
- Online Models interactions;
- selected printer, process, and filament panels;
- actual Global/Objects state and modifiers;
- support/seam painting canvas;
- calibration dialogs and their values;
- sliced Preview, legends, colors, and statistics;
- send page and all Device/CFS/camera/history/timelapse screens;
- firmware/update navigation.

Source-defined labels may be used with `source-confirmed, visually unobserved`. Pixel paths, defaults, and disabled states require a screenshot or direct version-matched observation.

## Refresh procedure

For any version newer or older than 7.2.1:

1. Read About or installed bundle metadata.
2. Query the official download page and GitHub releases API live.
3. Read the exact release notes and tag/source when available.
4. Compare top navigation, edition/user-role labels, Process categories, support visibility, calibration menu, Preview views/Lite Mode, send actions, Device, and CFS.
5. Record renamed, moved, gated, added, and removed controls separately.
6. Preserve conflicts and observation state in `sources.md`.
7. Do not update the application without authorization merely to make the documentation match.
