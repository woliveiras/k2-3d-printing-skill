# Process settings

## Scope switch

Current 7.2.1 source labels the process panel `Process` and its scope switch `Global` / `Objects`. [C006]

- Use `Global` for the active process preset and project-wide values.
- Use `Objects` only after selecting the intended object, part, modifier, or layer range.
- Record inherited and overridden values separately. Do not assume that a value visible in Objects changed Global.
- Re-slice after any change; do not inspect a stale Preview.

The running panel was not visually observed, so the switch position, selected state, and scroll behavior remain unconfirmed.

## 7.2.1 category navigation

| Path | Exact label | Role/context dependency | Effect boundary | Preview validation |
|---|---|---|---|---|
| `Prepare` → `Process` → category | `Quality` | Available in current source | Opens quality-related groups | Inspect line type, line/layer width, seams, bridges, overhangs, and visible surfaces. |
| `Prepare` → `Process` → category | `Strength` | Available in current source | Opens wall, shell, and infill groups | Inspect wall/shell count, top/bottom closure, infill continuity, and load-oriented paths. |
| `Prepare` → `Process` → category | `Speed` | Visible only for `Professional` user role | Opens speed-related parameters | Inspect Speed, Flow, and Acceleration views and confirm the selected filament's calibrated limits. |
| `Prepare` → `Process` → category | `Support` | Visible in normal/global and normal per-object tabs; hidden for per-part and per-layer tabs | Opens support-generation groups | Inspect support, interface, islands, contact, trapped regions, and removal risk. |
| `Prepare` → `Process` → category | `Multimaterial` | Source-defined; may depend on printer/profile/context | Opens multi-material settings | Inspect filament mapping, changes, purge, tower, and per-filament totals. |
| `Prepare` → `Process` → category | `Others` | Available in current source | Opens skirt/brim/purge/special groups | Inspect skirt, brim, raft/purge structures, first-layer contact, and collision risk. |

An internal `Frequent` toolbar item exists in source but is hidden by the observed setup code. Do not direct a stable 7.2.1 user to `Frequent` unless it is visible in their build. [C007]

## Installed 7.2.1 subgroup labels

The installed `ProcessConfig.json` records these English groups. They are observed bundled-resource labels, not proof that every group is visible under every profile, role, or object context. [C023]

| Category | Subgroups |
|---|---|
| `Quality` | `Seam`, `Precision`, `Ironing`, `Wall generator`, `Walls and surfaces`, `Bridging`, `Overhangs`, `Layer height`, `Line Width` |
| `Strength` | `Walls`, `Top/bottom shells`, `Infill`, `Advanced` |
| `Support` | `Support`, `Raft`, `Support filament`, `Advanced`, `Tree supports` |
| `Others` | `Skirt`, `Brim`, `Prime tower`, `Flush options`, `Special mode` |

The current Process toolbar also defines `Speed` and `Multimaterial`, but the inspected local `ProcessConfig.json` did not provide their subgroup list. Mark those subsection names unconfirmed until read from the user's screen or an exact 7.2.1 setting definition.

## Objects, parts, modifiers, and layer ranges

Current source explicitly switches to per-object mode after adding a modifier or choosing object process settings. [C009]

The Support category is deliberately hidden for:

- a per-object **part** tab, because that tab has no Support page;
- a per-object **layer-range** tab, for the same reason. [C008]

It remains visible for the normal print tab. If Support disappears, first return to the object-level or Global process context; do not conclude that the feature was removed.

## Parameter evidence record

For an individual setting, use this record before recommending a change:

```text
Version/platform:
Edition: AI / Pro
User role: Basic / Professional
Path: Prepare > Process > Global|Objects > category > subgroup > exact label
Selected context:
Current value and unit:
Profile default and origin:
Official or observed effect:
Interactions:
Risk/stop condition:
Preview view and acceptance check:
Evidence ID / screenshot:
```

No individual 7.2.1 process-field defaults were visually observed in this research. Do not manufacture a unit, default, enabled state, tooltip, or interaction from the category name. A bundled profile value must be labelled `observed bundled profile value` and tied to its exact printer/nozzle/process/filament preset; it is not a universal default.

The 7.2.1 notes include fixes for interdependent settings and a bed-temperature selection defect. Treat a change in one field as potentially affecting another, re-open dependent fields, and re-slice before validation. [C003]

## Preset mutation

The official 6.2 preset documentation distinguishes system, project, and user process presets. Its UI uses `Expert`/`Basic`, while current 7.2.1 source uses `Professional`/`Basic`. Scope any `Save`, `Save As`, or preset-management path to the version actually visible. [C010] [C021]

Do not modify an original 3MF merely to apply a recommendation. When explicitly authorized, preserve the original, write a clearly named copy, inspect and compare its typed settings, then re-slice and review Preview.
