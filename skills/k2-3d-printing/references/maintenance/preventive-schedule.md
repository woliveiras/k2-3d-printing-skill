# Preventive maintenance schedule

Apply base-K2 rows only after the physical label or `About` screen confirms K2. Treat time/usage intervals as inspection triggers, not proof that a part must be replaced. Inspect sooner for symptoms, abrasive filament, dust, heavy use, or material residue.

## Conditional base-K2 schedule

| Trigger | Official task | Safe state | Validation | Sources |
|---|---|---|---|---|
| Before each print | Remove visible machine debris; inspect and clean the build platform | Print stopped; plate cool enough to handle; power off for internal debris near motion | Plate seated, no loose debris, first-layer Preview checked; supervise first layer | [P003] |
| After each filament change | Check that the hotend outputs material normally | Use only the normal load/extrude operation; keep clear of hot/moving parts | Stable extrusion without an error; stop on smoke, leak, grinding, or missing output | [P003] |
| Daily | Inspect the wiper dome | Off, unplugged, and cool unless the live official procedure says otherwise | Wiper present, seated, and free of obstructing debris | [P027] |
| Weekly | Inspect wiper tape; clean fans with power off | Off, unplugged, and cool; prevent fan movement | Wiper/fans unobstructed; no cable or blade damage; controlled power-on check | [P027] |
| Weekly when printing ABS | Clean a dirty or blurry base-K2 camera with a lint-free cloth and alcohol | Off and cool | Image is clear after controlled power-on; no liquid entered housing | [P033] |
| Every two weeks | Check original-CFS desiccant condition | CFS/printer powered down and disconnected as the CFS manual requires for service | No liquid/leak indication; humidity display behavior recorded after restart | [P023] [P025] |
| Monthly | Run input shaping with no filament loaded; inspect original-CFS PTFE monthly when using abrasive material | Use normal UI calibration only; no printer disassembly | Calibration completes without error; no new abnormal motion; PTFE has no visible wear/damage | [P027] [P025] |
| After five rolls of PLA, ABS, PETG, or PC when the cutter is used | Inspect the cutter | Off, unplugged, cool; open only as the exact base-K2 source allows | Cutter/path unobstructed; normal load/unload succeeds | [P027] |
| After one roll of fiber-filled filament when cutting frequently | Inspect the cutter | Same as above; use abrasion precautions | Same validation; stop if blade/seat/part identity is uncertain | [P027] |
| About every two months | Inspect and, if the exact original-CFS procedure supports it, replace 4 × 2.5 mm PTFE tubing | Power down and disconnect CFS/printer; unload only as directed | Correct routing, no pinch or missing connection; one supervised load/unload | [P025] |
| Every three months at about eight print hours/day | Replace the base-K2 filter per the exact official part/procedure; inspect Y/Z shafts and lead screws | Off, unplugged, cool | Air path unobstructed; controlled fan check; motion/calibration completes without noise/error | [P027] |
| Monthly under frequent use | Replace/inspect the filter more frequently | Same as above | Same as above | [P027] |
| Every 300 cumulative print hours | Lubricate XYZ/lead-screw motion; replace air filter; run input shaping and auto leveling | Follow exact model-specific pages; calibrations through normal UI | Both calibrations pass; supervised small test print | [P003] |
| Every three months maximum for CFS desiccant | Replace if ineffective; do not leave exhausted desiccant beyond the official warning | CFS powered down/disconnected; inspect for liquid before touching internals | No leak; compartment dry; humidity trend responds after restart | [P025] |
| Every five days during frequent ABS/ASA printing | Inspect/attend Y/Z shafts and lead screws under the base-K2 maintenance-page schedule | Off, unplugged, cool | Smooth controlled motion/self-test without abnormal noise | [P027] |

## Schedule conflict: rails and lead screws

The K2 V1.0 manual gives a 300-print-hour motion-lubrication interval. The base-K2 maintenance page gives monthly X-rail and three-month Y/Z/lead-screw attention, shortened to five days with frequent ABS/ASA. Newer K2-series X-rail and Z-lead-screw pages give weekly service for frequent use or every two weeks for infrequent use and name WD-40 Specialist Silicone. Creality does not explicitly mark one schedule as superseding the others. [P003] [P027] [P028] [P029]

Do not merge these into a false single interval. Record the model, source revision, actual print hours, elapsed time, material, environment, and symptoms. Prefer the newest task-specific official procedure only when its applicability to the confirmed machine is explicit; otherwise stop and ask Creality support to resolve the interval/product conflict.

## Other family members

- K2 Pro has a model-specific lubrication procedure that distinguishes thin metal anti-rust oil for the X rail from generic grease for Y/Z shafts and lead screws. It does not name an exact grease and must not be transferred to base K2. [P032]
- K2 Plus has its own maintenance page, two cameras, an activated-carbon filter, and automatic belt tension. Load its live model-specific procedure rather than this base-K2 schedule. [P012] [P013] [P030] [P034]
- P015 and P016 provide no complete K2 SE or K2 SE 4C preventive schedule. Treat schedules, lubricants, parts, and disassembly as unconfirmed until a model-specific official manual is opened.

## Symptom override

Stop routine operation and use [troubleshooting trees](troubleshooting-trees.md) immediately for loss of extrusion, layer shift, repeated collision, abnormal noise, thermal or sensor errors, burning odor, smoke, damaged cable, liquid ingress, CFS grinding/jam, fan failure, or a calibration that cannot complete. A calendar interval never overrides an active fault.
