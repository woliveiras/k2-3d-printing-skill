# Design for FDM

Treat cited numbers as source-specific examples or starting points, not universal rules or K2 capability claims. Validate the exact material, toolpath, orientation, printer, and purpose.

## Establish the design brief

Use the [slicing decision workflow](slicing/decision-workflow.md) for purpose, material, hardware, visible faces, loads, accuracy, and time. Additionally record the CAD datum, mating parts and hardware, allowed support marks/post-processing, and measurable acceptance criteria for fit, deflection, strength, finish, and removal.

## Numeric evidence ledger

| Topic | Primary-source example | How to use it |
|---|---|---|
| Wall lines | Prusa's 0.4 mm nozzle / 0.45 mm extrusion-width example yields about 0.45, 0.90, 1.35, and 1.80 mm for one through four perimeters. [M051] | Design nominal walls as whole generated line widths for the actual profile; inspect Preview. |
| Minimum wall | UltiMaker reports 0.5 mm under its own example conditions. [M049] | Treat as a manufacturer example, not K2 minimum. A functional wall usually needs more than the minimum visible toolpath. |
| Layer height | Polymaker suggests roughly 25–75% of nozzle diameter as a quality envelope. [M048] | Stay within the exact printer/profile/material validation; use smaller layers for slope detail and larger only when flow/geometry permit. |
| Clearance | Prusa says no universal tolerance, reports at least about 0.2 mm accuracy in its Original Prusa context, and suggests at least 0.3 mm as a moving-parts start. [M051] | Print a clearance ladder in final orientation/material. Do not promise 0.2 mm accuracy on K2. |
| Print-in-place gap | UltiMaker gives 0.6 mm in its design example. [M049] | Use as a second manufacturer example showing process dependence, not a mandated gap. |
| Overhang | UltiMaker presents 45° as a general start; Prusa reports about 45–60° depending on nozzle/settings and up to 75° only on named Nextruder machines; Autodesk says the angle depends on material/machine/process. [M049, M051, M052] | Run an overhang coupon on the final setup. Never transfer 75° to K2. |
| Bridge | UltiMaker gives about 10 mm as a generic start and reports up to 25 mm only for a tuned Tough PLA example. [M049, M050] | Minimize span and test bridge speed/flow/cooling. Do not promise 25 mm. |
| Bottom chamfer | UltiMaker gives roughly 45° as one way to accommodate elephant-foot effects; Prusa explains why a bed-facing fillet can create steep early overhangs. [M049, M051] | Prefer a tested chamfer or explicit elephant-foot calibration on bed-facing edges. |
| Large-particle wood | Prusa suggests at least a 0.6 mm nozzle and 0.2 mm layer for wood products with large particles. [M012] | Apply only after exact filler/nozzle evidence; it is not a plain-PLA rule. |

## Wall and thin-feature workflow

1. Determine the slicer's actual line width for each feature; do not use nozzle diameter alone.
2. Express constant shell walls as an integer number of generated lines where possible.
3. Inspect every wall in Preview. A valid CAD solid can slice with missing or single-line regions.
4. For load-bearing shells, put material around load entry, fastener bosses, corners, and bending skins. Do not assume infill repairs an undersized shell.
5. Add local thickness gradually to reduce stress concentration and keep the transition printable.
6. Print a thin-wall coupon in the final orientation and measure thickness, voids, surface, and failure mode.

Stop if the slicer omits a required wall or converts it into an unintended gap fill. Redesign or choose a validated smaller nozzle; do not release because slicing completed.

## Tolerances, clearances, and fits

No universal clearance exists. It changes with:

- material shrinkage and moisture;
- orientation and anisotropy;
- outer/inner contour compensation and wall order;
- first-layer squish and elephant foot;
- hole direction, cooling, speed, and seam;
- insert/fastener geometry and post-processing.

Use a fit-coupon ladder:

1. Model several candidate clearances around the nominal requirement.
2. Use the final material, drying/conditioning, nozzle, line width, layer height, orientation, walls, plate, and cooling.
3. Include both assembly directions and the actual contact length.
4. Measure after the same cooling, annealing, water dissolution, or conditioning as the final part.
5. Select the clearance from measured acceptance, label it **Empirical adjustment**, and preserve the coupon record.

For press, slip, sliding, rotating, snap, and print-in-place fits, define a distinct force/play/cycle acceptance test. Do not reuse one gap for every fit class.

## Holes and bores

Horizontal circular holes create unsupported upper arcs and can shrink or become polygonal. The cited primary sources establish no universal K2 hole compensation.

Use this order:

1. Orient a critical bore vertically when load direction and part strength allow.
2. For horizontal holes, consider teardrop, diamond, or local-chamfer geometry as an **Engineering heuristic**; verify that it preserves mating/contact needs.
3. Add machining allowance for drill/ream/tap only when post-processing is allowed and accessible.
4. Keep bolt-head/nut/insert seats on printable planes or add support access.
5. Print a diameter/orientation coupon with the final walls, cooling, and material state.
6. Measure diameter, roundness, center position, insertion force, and wall breakout.

Do not hide a bad hole behind slicer XY compensation without measuring exterior dimensions and adjacent walls.

## Overhangs and bridges

Use the [orientation and support workflow](slicing/orientation-and-supports.md#bridges-and-overhangs) for slicing and coupons. In CAD, replace abrupt overhangs with chamfers, gradual slopes, local relief, reorientation, or splits; shorten and anchor bridge spans; and add self-supporting ribs or arches when the validated span is insufficient. Keep every result material-specific.

## Chamfers, fillets, and stress transitions

- Use a chamfer on a bed-facing edge when a fillet would begin with a near-horizontal unsupported layer. [M051]
- Use fillets where the orientation makes their layers printable and where they reduce a known stress concentration.
- Increase radius/thickness progressively at snap roots, bosses, handles, and wall junctions.
- Avoid abrupt wall-thickness changes that concentrate cooling shrinkage and load.
- Check internal radii against nozzle path and mating-tool access.
- Test the final transition in its actual load direction; a visually smooth fillet can still peel along layers.

## Layer orientation and load path

FDM parts are anisotropic. Prusa and UltiMaker both emphasize orientation-dependent interlayer behavior. [M049, M051]

1. Draw the primary tension, compression, bending, shear, torque, and impact paths.
2. Prefer XY roads along primary tensile/bending load where geometry and surfaces permit.
3. Avoid a fastener or snap pulling directly across a small Z-layer area.
4. Increase cross-section or split/rejoin the part when no single orientation satisfies load, fit, and finish.
5. Place seams and support transitions away from peak stress and sealing/contact surfaces.
6. Validate with a representative coupon or the actual part at the required load, direction, temperature, duration, and cycles.

Do not infer isotropic strength from a material TDS specimen or a high infill percentage.

## Snap-fits and compliant features

Formlabs' manufacturer guide treats FDM snap fits as orientation-sensitive, recommends carrying stress preferentially in XY rather than Z peel, and explains that longer/tapered/curved hooks can reduce concentration. Its example dimensions are geometry/process specific. [M053]

For each snap:

1. Obtain the exact material's allowable strain and conditioning state.
2. Orient the flexing beam so layer interfaces do not open at the root.
3. Use a printable root transition and avoid a notch at the first stressed layer.
4. Model insertion lead-in, retention face, travel stop, and tool/access for release.
5. Print a coupon series varying beam length/thickness and clearance.
6. Test insertion force, retention, permanent set, and required cycles at use temperature.

Do not call a snap durable from one successful insertion.

## Threads, heat-set inserts, and captured hardware

Protolabs states that as-printed thread suitability depends on process, material, and size and should not be relied on for critical threads without a more controlled strategy. Markforged recommends inserts/wear surfaces for stronger, longer-lived service in its composite context. [M054, M055]

Choose among:

- printed thread for low-load, coarse, replaceable use after a gauge/torque test;
- tapped pilot hole with material-specific allowance;
- heat-set or press-fit insert using the insert supplier's hole and installation procedure;
- captured nut or through-bolt where access and geometry permit.

Never invent insert temperature, pilot diameter, torque, wall thickness, or pull-out rating. Keep enough surrounding material for the actual load path, maintain tool access, and test torque/pull-out/thermal cycles.

## Contact, sealing, and ergonomic surfaces

- Keep primary visible, skin-contact, sealing, sliding, optical, and mating surfaces away from support and purge interfaces where possible.
- Orient layer stair-stepping relative to hand motion, seal direction, and visible light.
- Add machining or finishing allowance only when the material/SDS and process permit it.
- For a flat seal or bearing face, consider printing it against a validated plate or post-machining it; test flatness and surface damage after removal.
- Do not claim food, skin, medical, electrical, or flame safety from raw filament alone. Finished-process certification and cleaning/aging matter.

## Deformation and large parts

For a large flat part, reduce abrupt thickness changes and long uninterrupted shrink paths; add relief or divide it into stable sections where the load and assembly permit. Validate the final footprint with the [large-and-flat workflow](slicing/decision-workflow.md#large-and-flat-part).

For a tall narrow part, enlarge or mechanically anchor the base, lower concentrated mass, or redesign it into stable sections. Validate motion and collision risk with the [tall-and-narrow workflow](slicing/decision-workflow.md#tall-and-narrow-part).

## Split models intentionally

Split when it improves:

- load orientation;
- visible-face finish;
- support access/removal;
- build-volume fit;
- flatness and warp control;
- independent material choice;
- repair/replacement or assembly.

Design the joint around a datum, assembly access, adhesive/fastener limits, and the load path. Add alignment features with coupon-validated clearance. Verify that the joint does not concentrate stress or trap soluble support.

## Removable and sacrificial supports

- Prefer integrated breakaway tabs, ribs, or sacrificial membranes only when their thickness is generated reliably and removal will not damage the part.
- Provide tool access and an escape path; avoid sealed cavities.
- Keep interface on a noncritical face and use a chamfer/lead-in at cleanup boundaries.
- For soluble support, validate purge, interface adhesion, dissolution, residue, and moisture effects using [support materials](materials/support-materials.md).
- Inspect support and interface layer by layer; generated support is not proof of removability.

## Curved and ergonomic shells

For a curved ergonomic shell:

1. Mark the visible/hand-contact exterior, mating rim, openings, bosses, fasteners, and force regions.
2. Keep the exterior free of support when possible; use a natural-seam split when it improves both faces and assembly.
3. Express shell thickness as whole generated line widths and thicken gradually around bosses and openings.
4. Print representative curve, opening, rim, and fit segments before the full shell.
5. Define measurable surface, fit, force, deflection, and cycle criteria.

Use the [orientation workflow](slicing/orientation-and-supports.md) and [Preview inspection](slicing/preview-inspection.md) for stair stepping, seam, support, motion, and toolpath validation.

## Design review checklist

Run [model inspection](model-inspection.md) and the [canonical Preview inspection](slicing/preview-inspection.md). Treat the design review as complete only when required walls generate, load paths and transitions are deliberate, fits have coupon evidence, and every support or split joint remains accessible and measurable.
