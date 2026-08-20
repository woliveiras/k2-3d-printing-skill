# Version and modes

## Version-scoped reference baseline

| Field | Verified value | Evidence class |
|---|---|---|
| Bundle snapshot | `7.2.1.5476`, macOS arm64 | Read-only version-scoped artifact |
| Official stable release at 2026-08-20 | `v7.2.1`, build `7.2.1.5476` | Creality download and GitHub release data |
| Release publication | 2026-08-04T13:23:29Z | Official GitHub release API |

The bundle snapshot matched both official release channels on 2026-08-20. Do not reuse that as an undated `latest` claim. Query Creality's download page and official GitHub releases API for a version-sensitive request. Do not update or install the application without separate authorization. [C001] [C002] [C003] [C023]

## Determine the user's version

Use, in order:

1. Read the version from the running application's About screen when the user can provide it.
2. On macOS, read `CFBundleShortVersionString` from the installed bundle without launching it.
3. Read a visible version from a screenshot only when the complete version is legible.
4. Treat a 3MF profile name or screenshot styling as a clue, not proof of software version.

Record the platform because menu placement and native shortcuts can differ. The reference baseline contains no running `About` screen or UI observation.

## Keep the three mode systems separate

| System | Exact 7.2.1 labels | Source-confirmed path | Effect | Dependencies and risks |
|---|---|---|---|---|
| Edition | `AI` / `Pro`; tooltip `Switch AI/Pro mode` | `Prepare` → upper-right switch | Selects the guided AI edition or professional workflow | Introduced in 7.2.0. The source stores AI as `easy_print_mode=1`. AI recommendations remain proposals requiring parameter and Preview review. [C005] [C016] |
| User role | `Basic` / `Professional` | macOS application menu → `Preferences` → `User Role` | Selects simple versus advanced parameter exposure | `Speed` in the Process category toolbar is explicitly Professional-only in current source. Other fields may also be filtered. [C007] [C010] [C011] |
| Preview rendering | `Lite Mode` | `Preview` → color/legend panel → `Lite Mode` | Filters nonessential rendered toolpaths only | Hidden for raw G-code-only Preview; changing it invalidates the slice and requires re-slicing. It does not modify G-code. [C012] [C013] [C020] |

Do not call AI edition `Basic mode`, do not call Professional user role `Pro edition`, and do not treat Lite Mode as a slicing-quality mode.

## Top navigation

Current `v7.2.1` source defines these exact top-level labels:

`Online Models` → `Prepare` → `Preview` → `Device`. [C005]

These labels are source-confirmed; pixel location, selected-state styling, and responsive layout remain unconfirmed.

## Preferences

On macOS, 7.2.1 source adds `Preferences` to the native application menu with Command-comma. Use `Creality Print` → `Preferences…` only as a source-confirmed, visually unconfirmed path until it is visible in the target build. [C011]

The 7.2.1 general Preferences source contains:

- `Language`, `Login Region`, and `Units`;
- `Enable Easy mode`, which controls the AI-edition flag;
- `Zoom to mouse position`;
- `Automatically Layout on Model File Import`;
- `User Role` → `Basic` / `Professional`;
- `Improve preparation rendering performance by lod`;
- `Improve preview rendering performance by lod`;
- `Memory-Optimized Preview`;
- `Enable advanced Gcode preview`;
- `Display Step Import Setting Dialog`;
- controls to clear remembered choices for unsaved presets and projects. [C010]

`Downloads`, `Default Page`, `Auto sync user presets(Printer/Filament/Process)`, and `User Experience Program` are conditional on the cloud build in source. Mark them unconfirmed until visible in the user's build; the cited source does not establish their defaults.

Apply the screenshot and visibility rules in the [Creality Print index](INDEX.md#navigation-rule).

## 7.2.1 release relevance

The official 7.2.1 notes document fixes affecting Prepare rendering, paint-on supports, tree supports, G-code loading, WAN camera viewing, AI edits to printer/filament settings, interdependent settings, and bed-temperature selection. They also add more AI-recommendable parameters. These changes explain why paths and behavior from 6.x or early 7.x may not reproduce exactly, but they do not validate a generated value or a physical print. [C003]
