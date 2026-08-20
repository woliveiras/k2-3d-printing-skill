# Slicing decision workflow

## Build the constraint card

Infer a field only from evidence; otherwise ask the smallest question that changes the result.

| Field | What to record | Why it changes slicing |
|---|---|---|
| Part purpose | visual, prototype, fit check, functional, flexible, tooling, outdoor, heat/chemical exposure | Sets material and acceptance test |
| Physical printer | label/About evidence and exact variant | Sets hard limits and available controls |
| Material | manufacturer, product/SKU, color, batch if relevant, dry state | Sets TDS/SDS range, flow, cooling, shrinkage, CFS path |
| Tooling | physical nozzle diameter/material, hotend, extruder, CFS/direct path | Sets resolution, abrasion, flow, flexible-feed risk |
| Plate | exact surface and condition; adhesive/separation layer | Sets adhesion and release strategy |
| Geometry | dimensions, walls, details, holes, overhangs, bridges, cavities, contact area, center of mass | Sets orientation and support strategy |
| Loads | direction, magnitude/category, impact, creep, fatigue, heat | Sets layer direction, shells, infill, material |
| Appearance | visible/hidden faces, texture, seam tolerance, support-mark tolerance | Sets orientation, layer height, wall order, seam, ironing |
| Accuracy | critical dimensions, fit type, measurement method, tolerance coupon | Sets flow, hole/XY compensation only after calibration |
| Budget | deadline, allowed material, acceptable test coupons | Sets speed/detail and validation depth |
| Experience | beginner/intermediate/advanced and available instruments | Sets number of simultaneous changes and explanation depth |

## Gate the job

1. Stop if the model exceeds confirmed build bounds, the material exceeds a hardware limit, an abrasive product lacks the required nozzle, the plate/material pair is unconfirmed, or the selected CFS path is prohibited.
2. Repair or explicitly accept mesh/B-rep issues before parameter optimization.
3. Choose orientation before supports; choose supports before tuning cosmetic process values.
4. Calibrate the exact filament/nozzle/plate combination before dimensional or maximum-speed optimization.
5. Inspect Preview before estimating readiness.

## Objective workflows

### Maximum visual finish

- Put the most visible surface away from support contact and place the seam on a hidden edge or controlled painted path.
- Select a fine layer height that the confirmed nozzle/profile permits; use adaptive layers on changing curvature when Preview remains continuous.
- Lower external-wall speed and acceleration relative to the calibrated internal-wall profile; preserve volumetric-flow headroom.
- Increase top layers until sparse infill does not telegraph; use ironing only on suitable near-horizontal top surfaces after a coupon.
- Prefer orientation changes or sacrificial splits over supports on the show face.

### Balanced profile

- Start from the official profile for the confirmed printer/nozzle/material family.
- Keep standard layer height, moderate shells and sparse infill, automatic support only where Preview proves it is needed, and calibrated material limits.
- Change one constraint-driven value; retain a short test for fit or support release.

### Rapid prototype

- Use a larger permitted layer height and/or nozzle, fewer shells and top/bottom layers, low infill, and no support on non-critical cosmetic areas.
- Keep first-layer reliability and maximum volumetric flow inside calibrated bounds; speed does not justify under-extrusion.
- Preserve critical mating dimensions and print only the interface section when possible.

### Strong functional part

- Rotate the part so primary tensile/bending loads run through continuous extrusions rather than separating layers.
- Increase wall thickness before high infill when the load travels near the perimeter; add local geometry or modifiers at fasteners and stress concentrations.
- Reduce cooling or increase temperature only within the exact TDS/profile range when interlayer adhesion needs improvement.
- Validate with a representative coupon or sacrificial part under the actual load direction and environment.

### Dimensional fit

- Dry and calibrate material, temperature, flow, first layer, and pressure advance before applying compensation.
- Print a fit coupon containing the actual hole, pin, slot, wall orientation, and layer direction.
- Measure after cooling and conditioning; change hole/contour/elephant-foot compensation only for the measured systematic error.
- Keep the CAD clearance and slicer compensation separately documented.

### Flexible part

- Identify the exact polymer and Shore hardness; use the approved feed path and low-resistance spool path.
- Reduce speed and acceleration until feed is stable, minimize retraction, and avoid unnecessary travel across open features.
- Use wall geometry and infill pattern/density to tune compliance; do not infer softness from Shore value alone.
- Test hinges, snap regions, and compression in the intended direction.

### Abrasive material

- Confirm physical wear-resistant nozzle material and minimum diameter from printer and filament sources.
- Start below the calibrated maximum volumetric flow; monitor extrusion consistency and nozzle wear.
- Record post-print nozzle/path cleaning and dimensional/nozzle inspection.

### Tall and narrow part

- Maximize safe contact area with a brim or designed fixture, reduce upper-layer acceleration/speed, avoid a heavy purge structure collision zone, and check center-of-mass motion.
- Prefer splitting or reorientation when the layer load and wobble risk conflict.
- Inspect travel paths and every isolated upper section in Preview.

### Large and flat part

- Use a clean, correct plate; avoid unnecessary solid mass; use balanced wall/top/bottom layout and geometry that relieves shrinkage.
- Apply brim or local mouse ears to lifting corners before choosing a raft.
- Control enclosure, chamber, fan, door, and lid only from confirmed material/printer guidance.

### Thin walls

- Compare modeled wall width with the selected line-width multiples and thin-wall generation behavior.
- Prefer redesigning the wall to an integer-like extrusion layout; verify no missing wall in every layer.
- Do not rely on gap fill for a structural wall without a physical coupon.

### Curved ergonomic shell

- Preserve the touch/show surface by rotating support contact to the hidden interior or splitting along a natural seam.
- Use adaptive/fine layers where surface slope changes fastest; Preview for stair-stepping and tiny islands.
- Check that support cannot lock inside the shell and that interface removal will not crack thin edges.
- Print a cropped curvature/support coupon before a full mouse cover, grip, or case.

## Return the decision

State: confirmed printer/tooling/material; objective; chosen orientation; support strategy; parameter changes with claim labels; Preview evidence; test and acceptance criteria; time/material estimate from the sliced project; and residual uncertainty.
