# Quality, speed, and strength

All numerical ratios below are generic **starting points**, not Creality defaults or hardware limits. Keep them inside the confirmed profile, hardware, and TDS/SDS ranges and validate on the actual combination.

## Trade-off map

| Change | Likely gain | Likely cost/risk | Validate |
|---|---|---|---|
| Reduce layer height | finer Z detail and gentler curves | more layers/time; heat accumulation on small features | sliced wall continuity, cooling time, surface coupon |
| Increase nozzle diameter/layer height | time, flow capacity, thick-wall strength | lost small detail and corner resolution | minimum feature, bridge, dimensional coupon |
| Slow external walls/acceleration | surface consistency; less ringing | time | speed/acceleration Preview and ringing tower/coupon |
| Add walls | perimeter load capacity, sealing, screw/insert material | time/material and heat | actual shell thickness and load path |
| Add infill | support for top surfaces and distributed internal load | time/material; not a substitute for load-oriented shells | top surface and representative load test |
| Raise temperature inside allowed range | layer bonding and flow headroom | stringing, sag, gloss change, degradation | temperature tower and break comparison |
| Increase part cooling | bridges/overhangs, crisp detail | weaker interlayer adhesion, warping for some polymers | bridge/overhang coupon and layer break |
| Add support/interface | lower overhang risk | marks, trapped support, time/material | Preview access and removal coupon |
| Add brim/ears | bed stability | cleanup and elephant-foot interaction | first layer and release after cooling |

## Geometry-driven starting points

- Use layer height at roughly 25–50% of physical nozzle diameter as an initial search band only when the official profile permits it. Keep below the profile's maximum layer height.
- Start line width near 100–120% of nozzle diameter for ordinary walls; use the official profile first and inspect generated paths before changing it.
- Express wall thickness as generated line width × wall loops. Start with 2–3 loops for low-load visual/prototype work and 3–5 for ordinary functional trials, then size from the load and physical test.
- Start sparse infill around 10–20% for visual/prototype work and 20–35% for ordinary functional trials; increase for a measured reason, not as a universal strength control.
- Add top/bottom thickness in millimeters, then derive layer count. Confirm that the top skin bridges the chosen infill without pillowing or telegraphing.

## Speed and flow

1. Treat slicer speed as a request bounded by acceleration, path length, temperature, cooling, and maximum volumetric flow.
2. Calculate demanded flow conceptually as line width × layer height × path speed. Never set speed above the calibrated volumetric limit merely because the motion system advertises a higher speed.
3. Start external walls and bridges below internal-wall/infill speed; for cosmetic trials use roughly 40–70% of the calibrated internal speed and lower acceleration similarly.
4. Reduce speed on small perimeters, unsupported overhangs, sharp corners, flexible feed paths, and high-flow layer changes.
5. Diagnose matte/rough under-extruded high-speed regions as possible flow limitation before adding random temperature or flow compensation.

## Strength decisions

- Align continuous roads with primary tensile loads; avoid placing a critical tension plane between layers.
- Add radii/chamfers and local thickness at load transitions; remove sharp internal corners and abrupt cross-section changes.
- Use more shells around holes, inserts, fasteners, and bending surfaces. Use infill to support shells/top surfaces and distribute loads.
- Separate stiffness, yield, impact, creep, heat resistance, fatigue, and layer adhesion; one material or infill percentage does not optimize all.
- Condition hygroscopic material and test at service temperature/humidity.

## Finish decisions

- Put seam, support, brim, and purge contact away from the show surface.
- Use smaller layer height or adaptive layers for shallow curves; orientation can matter more than layer height.
- Use monotonic/top-surface patterns and sufficient top thickness before ironing. Treat ironing as a top-surface finishing pass, not a fix for under-extrusion or a curved side wall.
- Reduce external acceleration before reducing all speeds when ringing is the primary defect.
- Avoid excessive cooling/low temperature when layer lines look clean but the part delaminates.

## Material use and support removal

- Remove supports by changing orientation, splitting the model, using bridges/chamfers, or painting only necessary regions before weakening the part.
- Use the smallest interface that supports the surface and remains reachable. More support is not automatically safer.
- Prefer local brim ears for lifting corners; use a full brim for narrow contact; reserve raft for a demonstrated need because it consumes material and changes the bottom surface.
- Compare sliced grams and purge waste, not only model volume, particularly with CFS color/material changes.
