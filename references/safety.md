# Safety

Use the exact printer manual, filament SDS/TDS, adhesive/solvent SDS, and local electrical/fire/ventilation rules. This reference supplies decision boundaries, not a certification or a guarantee.

## Immediate stop conditions

Stop motion and heating, keep people clear, and use the official shutdown/emergency procedure for smoke, flame, sparking, damaged insulation or power cord, repeated breaker trip, strong new electrical odor, uncontrolled temperature, thermal/sensor error, liquid ingress, nozzle/bed collision, trapped clothing/hair, or abnormal grinding/impact. Disconnect power only when it is safe to approach. Do not resume until the cause and required service scope are confirmed.

## Hot and moving parts

- Keep hands, hair, clothing, jewelry, gloves, tools, children, and animals away from the moving toolhead, bed, belts, pulleys, fans, CFS path, and cutter.
- Treat the nozzle, hotend, bed, recently extruded polymer, chamber, and removed part as hot until measured or cooled for the manufacturer-stated interval.
- Do not wear loose gloves near active motion; entanglement can be worse than the contact they are meant to prevent.
- Stop, power off, unplug, and cool before ordinary cleaning or service. Follow an official model-specific procedure when a diagnostic step explicitly requires controlled heat or power; do not improvise live work.

## Power, grounding, and placement

- Use the manufacturer-supplied or explicitly approved cord and the model's rated voltage/current. Use a correctly grounded three-prong outlet; do not defeat protective earth.
- Place the printer on a stable, level, nonflammable support with the manual's clearances, away from heat, water, dust accumulation, flammable/explosive materials, blocked ventilation, and unstable extensions.
- Do not connect/disconnect internal cables while energized. Do not bypass fuses, sensors, interlocks, firmware limits, thermal protection, or grounding.
- Stop at protected electrical covers, mains wiring, heaters, damaged connectors/cables, liquid ingress, or unknown test points and use qualified service.

## Emissions and ventilation

NIOSH identifies ultrafine particles, VOCs/SVOCs, heat, motion, electrical energy, solvents, additives, and post-processing as additive-manufacturing hazards; emissions vary with printer, polymer, color/additives, temperature, and process [M056–M059]. EPA describes consumer 3D-printer VOC and ultrafine-particle research and notes that 1–100 nm particles can deposit deeply in the respiratory system [M060]. Therefore:

- Never call PLA, PETG, ABS, ASA, nylon, PC, TPU, or a composite emission-free or universally safe indoors.
- Prefer a lower-emission material such as PLA over ABS when it meets the job, as a reduction measure rather than a guarantee [M057].
- Keep the printer away from routinely occupied breathing zones. Prefer source capture, a ventilated enclosure, or local exhaust to an appropriate outdoor discharge where permitted.
- Use HEPA for particles and an appropriate maintained gas/vapor medium for VOCs when the system is designed for both. HEPA alone does not remove gases; unverified recirculation is not exhaust.
- Use the lowest validated nozzle temperature inside the exact TDS range; temperature can change emissions.
- Require an exact certification/report before calling a printer or material low-emission. UL 2904 defines an emissions measurement/assessment method; its existence does not certify this printer [M061].

### Material distinctions

| Material | Do not omit |
|---|---|
| PLA and filled PLA | Lower-emission comparisons do not mean no emissions. Pigment, wood, metal, CF/GF, glow, and additives change hazards. |
| PETG/PET | Ventilate; control string/fume temperature; consult exact SDS. Do not treat low odor as low exposure. |
| ABS/ASA/HIPS | Prioritize enclosure/source capture and ventilation; consult exact SDS and avoid occupied-room assumptions. |
| TPU/TPE | Exact formulation, additives, Shore grade, drying, and degradation temperature matter; avoid feed grinding/overheating. |
| PA/nylon and PC | Hygroscopic processing, higher temperatures, additives, and enclosure conditions can increase exposure/control needs. |
| CF/GF/metal/wood composites | Control dust and fragments during handling and post-processing. Do not touch sharp exposed fibers; consult exact SDS. |
| Soluble support | PVA/BVOH moisture sensitivity and disposal instructions are product-specific; dissolved polymer is not automatically suitable for a drain. |

## Composite and post-processing controls

- Capture sanding, cutting, drilling, sawing, or grinding dust at source; use a method and PPE selected from the exact SDS and task risk.
- Prefer compatible wet methods or maintained HEPA-filtered collection where appropriate; do not dry sweep or use compressed air to redistribute fine CF/GF/pigment/polymer dust.
- Inspect composite parts for exposed fibers and finish/seal only with a compatible documented process.
- Keep food-contact, skin-contact, medical, electrical, flame-retardant, and structural certification out of scope unless the exact SKU and finished process are certified for that use.

## Drying and storage

- Treat drying temperature/time as a product-and-spool limit, not a family constant. Enforce the lowest limit among the exact TDS/SDS, spool/container, dryer, and device manual.
- Do not assume a household oven controls temperature accurately or that a spool tolerates the polymer's drying temperature. Use a purpose-suitable device and independent verification when the manufacturer requires it [M053].
- Never heat an unknown adhesive, solvent, desiccant, spool, container, or filament. Stop on odor, smoke, discoloration, deformation, or temperature-control error.
- Store dry material in a sealed, labeled container with maintained desiccant where required. Do not call a passive CFS humidity display or desiccant bay an active dryer.

## Adhesives and solvents

- Use only products compatible with the exact plate and polymer, in the documented quantity, temperature state, and ventilation.
- Read the SDS for flammability, vapor, skin/eye, storage, and disposal controls. Keep ignition sources away and do not mix products.
- Treat glue as adhesion aid or separation layer according to plate/material guidance; more adhesive is not a substitute for plate cleaning, calibration, or compatible surface selection.
- Do not recommend vapor smoothing or heated solvent work without an explicit separately authorized procedure, engineered controls, and exact SDS evidence.

## Domestic use, children, and animals

- Restrict the operating and post-processing area. An enclosure reduces contact risk but does not eliminate emissions, electrical, mechanical, or fire hazards.
- Supervise children as the manual requires; do not rely on a camera, lock screen, or AI detection as physical protection.
- Prevent animals from reaching hot parts, moving equipment, filament, purge waste, desiccant, adhesives, solvents, fine dust, or small sharp composite fragments.

## Overnight and unattended printing

No primary source reviewed for the candidate K2 grants a general unattended/overnight guarantee. Manufacturer declarations elsewhere are narrow to a named model, professional-use conditions, materials, tests, and manual [M063]; they do not transfer to Creality equipment.

1. Never answer that unattended or overnight printing is generally safe.
2. Identify the physical printer and condition, material, site, electrical circuit, nonflammable placement, ventilation, detection/suppression plan, and manufacturer supervision statement.
3. Explain that a camera or notification cannot suppress fire, remove emissions, or guarantee intervention.
4. Prefer postponing an active print when a person able to intervene cannot meet the manufacturer's supervision/site rules.
5. Distinguish an actively heating and moving printer from a completed job with heaters off and motion stopped. A finished part may remain hot; wait for the documented cooling state before handling.

## After completion

- Confirm the job actually ended, heaters are off, motion has stopped, and no thermal/error state remains.
- Ventilate for the material/process as required; do not open a hot chamber into an occupied breathing zone without considering exposure.
- Let the plate, part, nozzle, chamber, purge waste, and supports cool before handling. Remove the part by the exact plate guidance, not by levering against heaters or sensors.
- Collect purge/string/support waste and sharp composite fragments; store/dispose of polymer, dissolved support, adhesives, solvents, filters, desiccant, and contaminated wipes under product/local rules.
- Power down only as the manual permits and leave the area in a non-heating, stable state.

## Safety claim boundary

State the source/model/material scope and remaining unknowns. Do not convert `no apparent anomaly`, enclosure, filtration, AI monitoring, grounding, or successful prior prints into `safe`. Use `risk controls identified` and list the controls actually verified.
