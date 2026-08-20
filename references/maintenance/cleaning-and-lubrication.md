# Cleaning and lubrication

Confirm the physical printer before selecting a product, interval, or disassembly path. The official K2 sources conflict on rail and lead-screw cadence; preserve that conflict rather than creating a universal schedule.

## Safe-state baseline

1. Finish or stop the print through normal controls and ensure motion has stopped.
2. Remove filament only when the exact procedure directs it.
3. Power off, unplug, and allow hot parts to cool. For K2, wait at least 30 minutes after switch-off before touching hot parts. [P003]
4. Keep liquid away from electronics, connectors, fans, sensors, CFS internals, and openings.
5. Use only the cleaning agent or lubricant explicitly named for the confirmed model and location.
6. Stop if the official page does not identify the model, location, product, or safe state.

## Task matrix

| Task | Applies to | Confirmed tools/consumables | Steps supported by researched source | Validation | Stop/escalate when | Sources |
|---|---|---|---|---|---|---|
| Machine debris and build-platform inspection | confirmed base K2 | No exact cleaner captured | Inspect and remove debris before each print; inspect/clean the platform before each print | Plate is seated, surface has no visible debris, and supervised first layer is uniform | Plate coating is cut, lifting, badly contaminated, or the correct cleaner is unknown | [P003] |
| X-axis guide-rail cleaning/lubrication | K2-series page; confirm exact listed applicability live | lint-free cloth; WD-40 Specialist Silicone | Power off; clean the rail; apply only the named product according to the live official page | Controlled self-test/input shaping finishes without abnormal noise or error | Rail is damaged/corroded, motion binds, product/location is uncertain, or residue can reach belt/electronics | [P028] |
| Z-axis lead-screw cleaning/lubrication | K2-series page; confirm exact listed applicability live | lint-free cloth; WD-40 Specialist Silicone | Power off; clean/lubricate only the lead-screw locations shown by the live official page | Auto leveling and controlled Z motion finish without noise/error | Screw is bent/damaged, motion binds, debris cannot be removed safely, or product/location is uncertain | [P029] |
| K2 Pro motion lubrication | confirmed K2 Pro only | thin metal anti-rust oil for X; generic grease for Y/Z in source | Follow the model-specific source and keep X product separate from Y/Z product | Model-supported motion calibration passes | Exact grease remains unidentified, machine is not K2 Pro, or lubricant could contact belts/electronics | [P032] |
| Camera lens | confirmed base K2 | lint-free cloth and alcohol | Clean when image is dirty/blurry; inspect weekly when using ABS | Camera image is clear after controlled restart | Liquid enters housing, lens is scratched/loose, image remains failed, or device identity differs | [P033] |
| Fans | confirmed base K2 schedule | No exact tool captured | Clean weekly with printer powered off; do not invent cover removal | Fan starts normally without rubbing/noise and airflow path is unobstructed | Blade/cable damage, rubbing, fan error, inaccessible debris, or disassembly not covered by source | [P027] |
| Air filter | confirmed base K2 schedule | Exact filter part number/tool not captured | Replace at the documented interval only after opening the exact official part/procedure | Filter is correctly seated; fan path is unobstructed; no warning/noise after restart | Part identity, orientation, access, or fastener procedure is unconfirmed | [P003] [P027] |
| Wiper dome/tape | confirmed base K2 schedule | Exact replacement part/tool not captured | Inspect dome daily and tape weekly; remove only safely accessible debris | Wiper is present, seated, and unobstructed | Wiper is torn/loose, replacement identity is unknown, or access requires unsupported disassembly | [P027] |

## Cadence conflict

| Source scope | X rail | Y/Z shafts and lead screws | Interpretation |
|---|---|---|---|
| K2 User Manual V1.0_EN | XYZ/lead-screw lubrication every 300 cumulative print hours | same | Base-K2 manual schedule [P003] |
| Base-K2 maintenance tips | X rail monthly | every three months; every five days with frequent ABS/ASA | Base-K2 symptom/material schedule [P027] |
| Newer K2-series task pages | weekly for frequent use; every two weeks for infrequent use | weekly for frequent use; every two weeks for infrequent use | More recent and task-specific, but page applicability must be checked for the exact model [P028] [P029] |

Creality did not publish an explicit supersession statement in the researched pages. Record actual usage and source revision. Do not average the intervals or silently choose the longest. If the newer page cannot be confirmed for the physical model, use the exact model manual for routine scheduling and ask Creality support to resolve the conflict before applying a different lubricant or cadence.

## Product boundaries

- Do not generalize WD-40 Specialist Silicone from the K2-series cleaning pages to every rail, shaft, bearing, belt, or printer model. [P028] [P029]
- Do not generalize the K2 Pro thin anti-rust oil/generic grease split to base K2, K2 Plus, or either K2 SE. [P032]
- Do not substitute grease, oil, solvent, adhesive, or cleaner by similarity. No complete official chemical compatibility list was captured.
- Keep all lubricant and cleaning liquid away from belts, plate printing surface unless explicitly intended, electronics, connectors, fans, camera openings, sensors, and filament path.
- No official torque was captured for any reassembled fastener. If removal requires a torque-controlled fastener and the source provides no torque, stop.

## Post-maintenance acceptance

1. Inspect the serviced location while powered off: no tool, cloth fiber, loose part, pooled liquid, misplaced cable, or obstruction.
2. Reinstall only parts whose orientation and fasteners are explicit in the live model-specific procedure.
3. Run the normal controlled self-test/calibration relevant to the location.
4. Stop on binding, collision, repeated calibration failure, abnormal noise, smoke, odor, sensor/thermal error, or fan failure.
5. If the self-test passes, make a small supervised test print and record the model, source revision, product used, date, print hours, observation, and result. Report `physically validated` only after this test meets stated acceptance criteria.
