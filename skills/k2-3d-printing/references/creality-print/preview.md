# Preview

Use Preview to inspect generated toolpaths. Do not interpret a successful slice as evidence that the job is physically printable.

## Enter Preview

Current 7.2.1 source defines `Slice plate` and `Slice all`; invoking either slice action selects `Preview`. [C011]

Record before inspection:

- software version and platform;
- selected printer/nozzle, plate, process, and filament presets;
- plate and object;
- `Lite Mode` state;
- active view and legend;
- every view or layer range not inspected.

## 7.2.1 view selector

| Exact label | Unit shown by current source | Effect | Dependencies / risks |
|---|---|---|---|
| `Line Type` | Categorical | Colors paths by extrusion/move role | Read the active legend. Actual roles depend on generated G-code. |
| `Custom` | Context-defined | Custom appearance view | Compile-flag dependent and excluded from raw G-code-only Preview; mark unavailable unless visible. |
| `Filament` | Filament index/color | Shows paths by filament | Verify mapping by label and slot/material, not color alone. |
| `Speed` | `mm/s` | Shows path speed | Compare cosmetic, bridge, overhang, and tall-part regions with calibrated flow/stability. |
| `Layer Height` | `mm` | Shows layer height | Check transitions and whether small details still generate paths. |
| `Line Width` | `mm` | Shows extrusion width | Check thin walls, gap-fill behavior, and unsupported widths. |
| `Flow` | `mm³/s` | Shows volumetric flow | Stop when demand exceeds the named filament/nozzle's calibrated maximum. |
| `Layer Time` | Time | Shows layer duration | Check short layers and cooling interactions. |
| `Layer Time (log)` | Logarithmic time scale | Expands time contrast | Do not compare color without that view's active scale. |
| `Fan Speed` | `%` | Shows commanded fan | Check material/tool/layer transitions and exact profile/TDS constraints. |
| `Temperature` | `°C` | Shows commanded temperature | Check first-layer and material changes against confirmed limits. |
| `Acceleration` | `mm/s²` | Shows acceleration | Check cosmetic walls, corners, bridges, and tall/slender regions. |

The source defines no universally valid default for these views or their values. `Tool` exists internally but is not added to the stable selector in the inspected code; do not direct the user to a `Tool` view unless visible. [C012]

## Line Type and filament statistics

The renderer knows labels including `Seams`, `Retract`, `Unretract`, `Filament Changes`, `Wipe`, and travel/extrusion roles. A label appears only when applicable to the G-code and render mode. [C012]

Filament statistics can separate:

- `Model`;
- `Support`;
- `Flushed`;
- `Tower`;
- `Total`;
- `Length` and `Weight` where available. [C012]

Use these categories to reconcile model material, support material, purge waste, prime tower demand, and spool capacity. Do not claim a value was reviewed if the corresponding column was not visible.

## Lite Mode

Current 7.2.1 source places `Lite Mode` beside the Preview view selector/legend. [C012]

- It displays only essential toolpath data and filters internal/nonessential rendering.
- It does not rewrite the G-code.
- It is hidden for imported raw G-code-only previews.
- Toggling it changes `gcode_preview_lite_mode`, invalidates the slice, and requires re-slicing.
- Its tooltip directs the user to disable it and re-slice to inspect internal parameters such as infill. [C012] [C013]

Creality's 6.2 Wiki says Lite Mode was introduced to reduce Preview memory use and hides internal sparse/solid infill rendering. This agrees with the current source but does not confirm current pixel placement. [C020]

Disable Lite Mode and re-slice for a complete inspection of internal walls/infill, support, travel, retractions, wipe/purge behavior, or any feature whose absence would change the decision.

## Layer-by-layer inspection

1. Inspect the entire first layer for every model, support, brim/raft, and purge structure.
2. Scrub to the first layer of every new island; reject unintended extrusion in air.
3. Inspect thin walls, holes, bridges, overhangs, top/bottom closure, and geometry transitions.
4. Inspect seams on visible, sealing, fitting, and high-stress surfaces.
5. Inspect support/interface contact, branch continuity, trapped support, and removal access.
6. Inspect speed, flow, acceleration, fan, and temperature through transitions and small layers.
7. Inspect travel/retraction across visible faces and collision-sensitive tall features.
8. Inspect every material change, CFS mapping, purge event, tower, and per-filament total.
9. Inspect each plate separately and compare object overrides with `Global`.

Use the complete checklist in [slicing Preview inspection](../slicing/preview-inspection.md).

## Readiness language

- `Sliced`: generation finished; Preview may be unreviewed.
- `Preview reviewed`: named views and layers were inspected with no apparent anomaly; list omissions.
- `Test print recommended`: fit, strength, support, material, surface, or calibration uncertainty remains.
- `Physically validated`: the stated printer/material/profile or representative acceptance test actually succeeded.

Never convert `Preview reviewed` into a guarantee of safety or print success.

## Observation boundary

No actual 7.2.1 Preview, sliced model, legend, colors, first layer, support interface, purge tower, or statistics panel was visually observed during research. All paths above are tagged-source or version-scoped Wiki evidence. If a screenshot lacks the version or active legend, report only the visible state and request more context only when necessary.
