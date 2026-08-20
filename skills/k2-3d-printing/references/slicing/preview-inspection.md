# Preview inspection

Do not release a print because slicing completed. Record Creality Print version, selected printer/nozzle/plate/process/filament, object/plate, active Preview legend, and which sliders/views were inspected.

## Layer-by-layer pass

| View/check | Look for | Stop or revise when |
|---|---|---|
| First layer | every object/support/brim/purge structure starts on the plate; continuous contact; correct exclusions | floating island, missing contact, tiny unstable pad, path outside bounds |
| Line type | external/internal walls, top/bottom, gap fill, infill, support/interface, bridge | missing thin wall, unintended gap fill as structure, unsupported skin |
| Islands | first layer of each new region and its previous support | any extrusion begins in air without a validated bridge/support |
| Seams | location through all layers and on visible/fit faces | random scar on critical face or seam weakening a thin/high-stress feature |
| Overhang/bridge | anchors, span direction, fan/speed/flow, supported underside | unanchored bridge, excessive span, support gap not generated as expected |
| Support/interface | contact, Z/XY gaps, reachability, branch stability | trapped support, show-face contact, detached branch, interface fused by rounding |
| Adhesion | skirt/brim/ears/raft relation to part and plate | disconnected ear, precision edge contamination, collision with purge object |
| Speed/acceleration | external walls, small perimeters, bridges, upper tall layers | cosmetic/unsupported path uses a high value without flow/stability margin |
| Volumetric flow | peak and sustained high-flow regions | demand exceeds calibrated limit or abrupt surface-critical changes |
| Fan/temperature | layer/material/tool-change transitions | value outside exact profile/TDS/hardware range or wrong tool/material mapping |
| Retraction/travel | long crossings, open cavities, tall features, sequential mode | avoidable show-face crossing, collision envelope, excessive flexible retraction |
| Multi-material | CFS slot mapping, tool changes, purge volume/tower, flush into object/infill | wrong material/slot, unsupported purge tower, incompatible support pair, excessive or insufficient purge unvalidated |
| Time/material | sliced time, grams/meters, per-filament use and purge | estimate based on wrong profile or missing spool capacity |

Use the legend visible in that version. Never infer line type, speed, flow, fan, or material solely from color without reading the active legend.

## Cross-section checks

- Scrub slowly across the first 5–10 layers, every geometry transition, start/end of support, holes/bridges, top of infill, split joints, and last layers.
- Zoom into thin walls and small holes; check that paths actually exist.
- Inspect each plate and object independently. For object overrides, compare with `Global` and confirm the intended object selection.
- Re-slice after every material/profile/object/support change; do not rely on a stale Preview.

## Readiness states

- Use `Sliced` when generation finished but the views were not fully inspected.
- Use `Preview reviewed` only with the checklist and no apparent anomaly in the inspected views.
- Use `Test print recommended` for new material, fit, support interface, load, cosmetic face, high-flow region, foreign 3MF, or unresolved uncertainty.
- Use `Physically validated` only after the named job or representative acceptance test succeeds on the stated hardware/material conditions.

List every unobserved view or unknown value. Do not convert `Preview reviewed` into a safety or success guarantee.
