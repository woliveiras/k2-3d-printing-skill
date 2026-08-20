# Calibration

Calibrate the exact physical printer, firmware, nozzle, plate, feed path, filament SKU/color/batch, dry state, and environment. Start from an official profile and stay within confirmed limits. Change one variable per test and save results under a new profile name.

## Proportional sequence

### 1. First layer

- Confirm plate type/profile, cleanliness, seating, nozzle condition, leveling prerequisites, and material bed range.
- Print a small multi-zone first-layer pattern. Look for continuous adjacent lines without gaps, ridges, tearing, transparent over-squish, or nozzle contact.
- Resolve first-layer faults before all later tests.

### 2. Temperature

- Use the exact TDS/profile range and a representative speed/flow.
- Compare layer bonding, bridge/overhang shape, stringing, surface/gloss, small features, and any odor/smoke anomaly.
- Choose the lowest or highest result only when it meets the actual objective; record the tested range.

### 3. Flow ratio

- Use a method supported by the installed Creality Print version and printer. Measure only after extrusion, temperature, and first layer are stable.
- Avoid compensating for wrong filament diameter, wet material, partial clog, worn nozzle, or flow-limit sub-extrusion.
- Validate walls/top surfaces and dimensions, not only one visual patch.

### 4. Pressure advance / flow dynamics

- Run only when the confirmed firmware/printer/profile officially supports the method.
- Use a representative material, temperature, acceleration, and speed. Reject results with flow limitation or unstable extrusion.
- Save the result to the correct filament/printer context; do not assume another material/color/nozzle shares it.

### 5. Maximum volumetric flow

- Increase flow gradually inside temperature and speed limits until surface/extrusion degradation begins; retain margin below the first failure.
- Check demanded volumetric flow in Preview. Do not convert advertised motion speed into a flow limit.

### 6. Retraction and stringing

- Dry hygroscopic material and stabilize temperature first.
- Start from the direct-drive official profile. Tune distance minimally, then speed/travel behavior; excessive retraction can jam, grind, or pull softened filament into the heat break.
- For flexible material, prioritize feed stability and minimal retraction.

### 7. Bridges and overhangs

- Test representative spans/angles with the chosen layer, line width, temperature, bridge flow/speed, and fan.
- Record supported span and acceptable underside for that combination; do not create a universal angle rule.

### 8. Dimensional tolerance

- Print actual mating shapes in relevant X/Y/Z orientations after thermal conditioning.
- Measure with a suitable tool, record systematic error, then adjust CAD clearance or slicer compensation separately.
- Revalidate holes, pins, slots, elephant foot, and shrinkage for each material.

### 9. Vibration/input shaping

- Use only the model/firmware's official routine. Ensure the machine is mechanically sound and on its final stable surface.
- Do not mask loose belts, pulleys, fasteners, or frame problems with a software calibration.

## Calibration record

Record date; physical model/serial category without exposing it publicly; firmware; Creality Print version; printer/process/filament profile names; nozzle/plate; material SKU/color/batch/dry state; room/chamber conditions; test artifact; values tested; selected value and reason; rejected symptoms; measurement; and whether the result was physically validated.

## Stop criteria

Stop on thermal errors, unexpected smoke, electrical odor, abnormal grinding/impact, nozzle scraping the plate, material outside a confirmed limit, feed damage, sensor disagreement, or a test that would exceed motion/flow limits. Power down and use the maintenance tree rather than continuing calibration.
