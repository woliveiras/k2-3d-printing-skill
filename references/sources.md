# Source register

Research cutoff: 2026-08-20 (Europe/Madrid). Recheck unstable claims before use. Entries identify source scope; they do not prove the user's physical printer, installed firmware, material lot, runtime UI state, safety, or physical printability.

Use the source-family prefixes as routing aids:

- `P`: printer, firmware, CFS hardware, maintenance, and model safety;
- `C`: Creality Print software, tagged source, releases, and local bundle observations;
- `M`: materials, CFS material path, FDM design, emissions, and material safety;
- `A`: secondary article used only for organization ideas;
- `D`: distribution/install documentation.

When an official page exposes no reliable revision date, record `Not stated by publisher` and keep the source-freshness warning. Do not substitute access date for publication date. `Review by` is the repository's re-verification deadline, not a publisher date.

## A001 — I Taught Claude to Design 3D-Printable Parts. Here's How

- Publisher: Nicolas Chourrout / Towards AI; accessed through Freedium mirror
- URL: https://freedium-mirror.cfd/https://pub.towardsai.net/i-taught-claude-to-design-3d-printable-parts-heres-how-675f644af78a
- Source type: Secondary article
- Published/revised: 2026-03-05
- Accessed: 2026-08-20T19:05:00+02:00
- Applies to: Skill organization and collaborative CAD workflow only
- Supports: General ideas of staged requirement gathering, parametric source, multi-view review, early feedback, and slicer feedback before finalization
- Limitations/conflicts: Original publisher returned HTTP 403 while the requested mirror returned HTTP 200 to a live curl request; no article value is authority for printer limits, parameters, compatibility, maintenance, or safety
- Confidence: Low for technical claims; Medium for accurately identifying the described workflow pattern
- Review by: 2027-02-20

## D001 — skills CLI reference

- Publisher: skills.sh / Vercel
- URL: https://www.skills.sh/docs/cli
- Source type: Official distribution documentation
- Published/revised: Not stated by publisher
- Accessed: 2026-08-20T18:52:00+02:00
- Applies to: Repository installation command and CLI telemetry notice
- Supports: `npx skills add owner/repo` installation form and `DISABLE_TELEMETRY=1` opt-out documented at access time
- Limitations/conflicts: CLI behavior and telemetry policy are time-dependent; the command was documented but not executed, and publication of this repository was not performed
- Confidence: High for the accessed documentation
- Review by: 2026-11-20

## D002 — skills CLI repository layout documentation at v1.5.23

- Publisher: Vercel Labs on GitHub
- URL: https://github.com/vercel-labs/skills/blob/435076e78988e1e6ec40d00b0b1d76bdbbc5419a/README.md
- Source type: Official distribution repository documentation pinned to a commit
- Published/revised: Commit `435076e78988e1e6ec40d00b0b1d76bdbbc5419a`; release `v1.5.23` published 2026-08-18
- Accessed: 2026-08-20T19:24:00+02:00
- Applies to: Repository discovery layout for the skills CLI
- Supports: Repository root and `skills/<name>/SKILL.md` discovery conventions; use of the nested standard layout for a complete skill payload
- Limitations/conflicts: Documentation describes discovery, while exact copied-file behavior is implementation-dependent and may change; recheck before publishing
- Confidence: High
- Review by: 2026-09-20

## D003 — skills CLI remote repository file filtering at v1.5.23

- Publisher: Vercel Labs on GitHub
- URL: https://github.com/vercel-labs/skills/blob/435076e78988e1e6ec40d00b0b1d76bdbbc5419a/src/blob.ts
- Source type: Official distribution implementation pinned to a commit
- Published/revised: Commit `435076e78988e1e6ec40d00b0b1d76bdbbc5419a`; release `v1.5.23` published 2026-08-18
- Accessed: 2026-08-20T19:24:00+02:00
- Applies to: Remote repository discovery and downloaded payload selection in skills CLI v1.5.23
- Supports: At the pinned revision, root-skill remote filtering selects `SKILL.md`, while a nested discovered skill retains files beneath its skill directory; this repository therefore keeps the complete payload under `skills/k2-3d-printing/`
- Limitations/conflicts: This is an implementation observation, not a permanent CLI contract; future versions may differ, and the install command was intentionally not executed
- Confidence: High for the pinned source
- Review by: 2026-09-20

## P001 — K2 Flagship Series

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series
- Source type: Official Wiki family index
- Published/revised: Last edited 2025-12-25
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2, K2 Pro, K2 Plus, K2 SE documentation routing
- Supports: Separate official family identities and model-scoped service documentation
- Limitations/conflicts: Index does not prove the user's physical model; K2 SE 4C appears on the store outside the inspected index
- Confidence: High
- Review by: 2026-11-20

## P002 — K2 User Manual HTML

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2/user-manual
- Source type: Official online manual
- Published/revised: Revision not shown on inspected HTML page
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Base K2
- Supports: Routing to the K2 manual and model-specific operating information
- Limitations/conflicts: HTML may change without a visible revision; does not identify the user's machine
- Confidence: High
- Review by: 2027-02-20

## P003 — K2 User Manual V1.0_EN

- Publisher: Creality Service / Shenzhen Creality 3D Technology
- URL: https://cdn.creality.com/ow/official/6bbb36e0-25b7-42b9-bb91-0451320ba2b0.pdf
- Source type: Official PDF user manual
- Published/revised: V1.0_EN; PDF created 2025-04-14 and modified 2025-07-08
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Base K2
- Supports: Official name, 260 mm cube volume, direct dual-gear extrusion, 0.4 mm nozzle, 300 °C nozzle, 100 °C bed, PEI spring-steel plate, listed materials, sensors/features, maintenance intervals, power and safety
- Limitations/conflicts: May not describe later firmware behavior; physical unit and hardware revision remain unobserved
- Confidence: High
- Review by: 2027-02-20

## P004 — K2 Combo 3D Printer

- Publisher: Creality Official Store
- URL: https://store.creality.com/products/k2-combo-3d-printer
- Source type: Official product page
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 and K2 Combo bundle
- Supports: K2 Combo consists of a K2 printer plus one original CFS; major advertised capabilities
- Limitations/conflicts: Marketing and regional content can drift; bundle identity does not prove the user's physical model
- Confidence: High for bundle identity; medium for performance claims
- Review by: 2026-11-20

## P005 — Creality K2 Plus vs K2 Pro vs K2

- Publisher: Creality Official Store
- URL: https://store.creality.com/blogs/buying-guides/creality-k2-plus-vs-k2-pro-vs-k2
- Source type: Official manufacturer buying guide
- Published/revised: Published 2025-08-25
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2, K2 Pro, K2 Plus
- Supports: Family-size and chamber distinctions, including lack of active chamber heating on base K2
- Limitations/conflicts: Marketing comparison; verify hard limits and repair details in manuals/service pages
- Confidence: Medium-high
- Review by: 2026-11-20

## P006 — K2 Nozzle Replacement

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2/replace-nozzle
- Source type: Official model-specific service procedure
- Published/revised: Last edited 2025-09-16
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Base K2 nozzle assembly
- Supports: Integrated heat-break/nozzle, hardened-steel tip, 0.4/0.6/0.8 mm options, 6 mm socket, thermal grease, controlled hot replacement and burn risk
- Limitations/conflicts: No torque, visible assembly SKU, or physical 0.2 mm option; ordered manipulation details must be reopened live
- Confidence: High
- Review by: 2026-11-20

## P007 — K2 Parts List

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2/parts-list
- Source type: Official model-specific parts catalog
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Base K2
- Supports: Model-scoped leveling, filament detection, fan, wiper, filter, camera, cutter, hotend and electrical-component identification
- Limitations/conflicts: Identification does not authorize removal; base nozzle/hotend SKU and cross-model compatibility are not exposed
- Confidence: High
- Review by: 2026-11-20

## P008 — K2 Extruder Jammed Filament

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2/extruder-jammed-filament
- Source type: Official model-specific troubleshooting procedure
- Published/revised: Last edited 2025-09-16
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Base K2 extruder jam
- Supports: Existence of a model-specific clearing path and extruder front-cover SKU 4001020081
- Limitations/conflicts: Does not establish other part numbers, tools, torques, or cross-model steps; reopen live for ordered disassembly
- Confidence: High
- Review by: 2026-11-20

## P009 — K2/K2 Pro PEI Double-Sided Frosted Build Plate

- Publisher: Creality Official Store
- URL: https://store.creality.com/uk/products/k2-k2-pro-pei-double-sided-frosted-build-plate
- Source type: Official accessory product page
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 and K2 Pro only as explicitly named
- Supports: Official optional double-sided frosted PEI plate compatibility for the two named models
- Limitations/conflicts: Does not prove compatibility with K2 Plus, either K2 SE, or third-party plates
- Confidence: High for named-model compatibility
- Review by: 2026-11-20

## P010 — K2 Pro Combo 3D Printer

- Publisher: Creality Official Store
- URL: https://store.creality.com/eu/products/creality-k2-pro-combo-3d-printer
- Source type: Official product page
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 Pro
- Supports: 300 mm cube volume, 300 °C nozzle, 110 °C bed, 60 °C active chamber, direct-drive extruder, CFS and advertised camera/sensor features
- Limitations/conflicts: Marketing source; does not apply to base K2
- Confidence: High for identity and published limits
- Review by: 2026-11-20

## P011 — K2 Pro User Manual V1.0_EN

- Publisher: Creality Service / Shenzhen Creality 3D Technology
- URL: https://cdn.creality.com/ow/official/d5e60536-b346-4f71-b7a1-e6dc23e854f4.pdf
- Source type: Official PDF user manual
- Published/revised: V1.0_EN; related Wiki manual record last edited 2025-08-18
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 Pro
- Supports: Model-specific volume, thermal, chamber, extrusion, plate, CFS and safety boundaries
- Limitations/conflicts: Does not identify the user's machine and must not be applied to base K2
- Confidence: High
- Review by: 2027-02-20

## P012 — K2 Plus 3D Printer

- Publisher: Creality Official Store
- URL: https://store.creality.com/products/creality-k2-plus-3d-printer
- Source type: Official product page
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 Plus
- Supports: 350 mm cube volume, 350 °C nozzle, 120 °C bed, 60 °C active chamber, tri-metal/hardened-tip hotend, active bed tilt and belt tension, CFS support
- Limitations/conflicts: Marketing source; parts and procedures are K2 Plus-specific
- Confidence: High for identity and published limits
- Review by: 2026-11-20

## P013 — K2 Plus User Manual

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2-plus/user-manual
- Source type: Official online user manual
- Published/revised: Last edited 2024-12-13
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 Plus
- Supports: Model-specific operating and safety context for K2 Plus
- Limitations/conflicts: Older than some service pages; not transferable to other K2 variants
- Confidence: High
- Review by: 2026-11-20

## P014 — K2 Plus Nozzle Replacement

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2-plus/replace-nozzle
- Source type: Official model-specific service procedure
- Published/revised: Last edited 2025-02-14
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 Plus only
- Supports: Separate integrated K2 Plus 0.4/0.6/0.8 mm nozzle-replacement procedure
- Limitations/conflicts: Explicitly not transferable to other K2 models; no torque captured
- Confidence: High
- Review by: 2026-11-20

## P015 — K2 SE Combo 3D Printer

- Publisher: Creality Official Store
- URL: https://store.creality.com/as/products/k2-se-combo-3d-printer
- Source type: Official product page
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 SE
- Supports: 220 × 215 × 245 mm build volume, 300 °C nozzle, 100 °C bed, epoxy-resin plate, original-CFS and camera claims
- Limitations/conflicts: The page's `0.4 mm filament diameter` field appears to confuse nozzle and filament diameter; no complete maintenance procedure captured
- Confidence: Medium-high except erroneous field
- Review by: 2026-11-20

## P016 — K2 SE 4C 3D Printer

- Publisher: Creality Official Store
- URL: https://store.creality.com/products/k2-se-4c-3d-printer
- Source type: Official product page
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 SE 4C
- Supports: Separate 220 × 215 × 245 mm integrated four-slot product, 300 °C nozzle, 100 °C bed, epoxy-resin plate
- Limitations/conflicts: Does not establish original-CFS behavior or maintenance procedures
- Confidence: High for product identity
- Review by: 2026-11-20

## P017 — K2 Firmware Downloads

- Publisher: Creality Cloud
- URL: https://www.crealitycloud.com/downloads/firmware/flagship-series/k2
- Source type: Official live firmware catalog
- Published/revised: Live entry observed through 2026-07-28
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 public firmware listing
- Supports: Public K2/K2 Pro V1.1.6.7 image filename and board association when combined with API data
- Limitations/conflicts: Does not prove installed version or universal OTA availability; K2/K2 Pro share an image
- Confidence: High for observed listing
- Review by: 2026-09-20

## P018 — K2 Pro Firmware Downloads

- Publisher: Creality Cloud
- URL: https://www.crealitycloud.com/downloads/firmware/flagship-series/k2-pro
- Source type: Official live firmware catalog
- Published/revised: Live entry observed through 2026-07-28
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 Pro public firmware listing
- Supports: Shared K2/K2 Pro V1.1.6.7 image listing and board association when combined with API data
- Limitations/conflicts: Shared image cannot distinguish physical K2 from K2 Pro; installed version unknown
- Confidence: High for observed listing
- Review by: 2026-09-20

## P019 — K2 Plus Firmware Downloads

- Publisher: Creality Cloud
- URL: https://www.crealitycloud.com/downloads/firmware/flagship-series/k2-plus
- Source type: Official live firmware catalog
- Published/revised: Live entry observed 2026-08-07; filename build stamp 20260731
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 Plus / CR0CN240110C10
- Supports: Public V1.1.6.4 listing and board association when combined with API data
- Limitations/conflicts: Does not prove installed version or universal OTA availability
- Confidence: High for observed listing
- Review by: 2026-09-20

## P020 — K2 SE Firmware Downloads

- Publisher: Creality Cloud
- URL: https://www.crealitycloud.com/downloads/firmware/flagship-series/k2-se
- Source type: Official live firmware catalog
- Published/revised: Live entry observed 2026-08-07
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 SE / CR4CU220812S12K1
- Supports: Public V2.3.6.77 listing and board association when combined with API data
- Limitations/conflicts: Does not prove installed version or apply to K2 SE 4C
- Confidence: High for observed listing
- Review by: 2026-09-20

## P021 — K2 Series and CFS Firmware Upgrade Guide

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2-series-cfs-firmware-upgrade-guide
- Source type: Official firmware service guide
- Published/revised: Last edited 2025-08-19
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Named K2-series printers and original CFS within the guide
- Supports: Printer `.img` and CFS `.bin` packages, CFS-through-printer update, filament retraction, and post-update input shaping/auto leveling
- Limitations/conflicts: Does not publish a current independent original-CFS version; no update authorization or installed-version evidence
- Confidence: High
- Review by: 2026-09-20

## P022 — Creality Filament System (CFS)

- Publisher: Creality Official Store
- URL: https://store.creality.com/ca/products/creality-filament-system-cfs
- Source type: Official accessory product page
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Original CFS
- Supports: Creality 485, 24 V/20 W, four slots, at most four CFS units, RFID, auto relay, passive desiccant storage, display, spool envelope, and narrower material list
- Limitations/conflicts: Compatibility wording drifts between K2-series/Hi and an older K2-Plus-only field; product page is marketing, not physical path validation
- Confidence: Medium-high
- Review by: 2026-11-20

## P023 — CFS User Manual

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/cfs/user-manual
- Source type: Official accessory manual
- Published/revised: English revision not visible; multilingual variants show V1.2 but do not establish the English revision
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Original CFS
- Supports: Grounding, power disconnection, no energized cable connection/disconnection, water/liquid boundary, spool cautions, and qualified-service/internal-cover limits
- Limitations/conflicts: Connected CFS generation and installed firmware remain unknown
- Confidence: High
- Review by: 2026-11-20

## P024 — CFS Filament Compatibility

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/cfs/cfs-filament-compatibility
- Source type: Official accessory compatibility guidance
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Original CFS filament path
- Supports: Medium-hard filament groups, dried PVA/BVOH, TPU/elastic and wet PVA/BVOH rejection, and brittle PPA-CF/PPS-CF breakage caution
- Limitations/conflicts: Broader than the store's normal-material list; does not guarantee every brand, formulation, hardness, or spool
- Confidence: High for cautions; medium-high for broad groups
- Review by: 2026-11-20

## P025 — CFS Maintenance Tips

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/cfs/maintenance-tips
- Source type: Official accessory maintenance guide
- Published/revised: Last edited 2024-11-19
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Original CFS
- Supports: 4 × 2.5 mm PTFE tubing, typical two-month replacement, monthly abrasive-material inspection, two-week desiccant checks, and three-month leak/damage warning
- Limitations/conflicts: Intervals depend on use, abrasiveness, environment, wear, and symptoms; exact replacement tools/parts beyond tube size not captured
- Confidence: High
- Review by: 2026-11-20

## P026 — Creality CFS-C

- Publisher: Creality Official Store
- URL: https://store.creality.com/uk/products/creality-cfs-c
- Source type: Official accessory product page
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: CFS-C
- Supports: Distinct K1-oriented device using CAN, 30 W, with no multi-unit expansion documented
- Limitations/conflicts: Marketing page; used to prevent confusion with original CFS, not to supply K2 procedures
- Confidence: High for device distinction
- Review by: 2026-11-20

## P027 — K2 Maintenance Tips

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2/maintenance-tips
- Source type: Official model-specific maintenance guide
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Base K2
- Supports: Cutter, wiper, fan, filter, camera-related context, X/Y/Z/lead-screw and input-shaping schedules by time/material/use
- Limitations/conflicts: Cadence conflicts with the V1.0 manual and newer K2-series rail pages; no supersession notice
- Confidence: High for individual tasks; medium for interval reconciliation
- Review by: 2026-11-20

## P028 — K2-Series X-Axis Guide-Rail Cleaning

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/clean-x-axis-guide-rail
- Source type: Official K2-series maintenance procedure
- Published/revised: Last edited 2025-08-29
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2-series scope named by page; exact variant applicability must be confirmed live
- Supports: Power-off cleaning, lint-free cloth, WD-40 Specialist Silicone, and weekly/biweekly cadence
- Limitations/conflicts: Page does not enumerate every variant in captured evidence; cadence conflicts with older base-K2 sources
- Confidence: High for procedure; medium for universal applicability
- Review by: 2026-11-20

## P029 — K2-Series Z-Axis Lead-Screw Cleaning

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/clean-z-axis-lead-screw
- Source type: Official K2-series maintenance procedure
- Published/revised: Last edited 2025-08-29
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2-series scope named by page; exact variant applicability must be confirmed live
- Supports: Power-off cleaning/lubrication, WD-40 Specialist Silicone, and weekly/biweekly cadence
- Limitations/conflicts: Page does not enumerate every variant in captured evidence; cadence conflicts with older base-K2 sources
- Confidence: High for procedure; medium for universal applicability
- Review by: 2026-11-20

## P030 — K2-Series XY Belt Tensioning

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/xy-belt-tensioning
- Source type: Official family service guide
- Published/revised: Last edited 2026-05-15
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 and K2 Pro manual belt tension; K2 Plus automatic belt tension
- Supports: Model distinction, two-to-three clockwise turns for the named manual path, and post-adjustment input shaping
- Limitations/conflicts: No torque; screw position must be taken from live official illustrations; no K2 SE procedure captured
- Confidence: High
- Review by: 2026-11-20

## P031 — K2 Pro and K2 Plus Chamber Temperature Guide

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2-pro-k2-plus-chamber-temp
- Source type: Official model-specific operating guide
- Published/revised: Revision not shown
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 Pro and K2 Plus only
- Supports: 60 °C chamber maximum, cooling/heating control regions, low-temperature-material cautions, and 110 V/ambient/heater-life limits
- Limitations/conflicts: Explicitly not evidence for active heating on base K2 or K2 SE variants; temperatures are not universal profiles
- Confidence: High
- Review by: 2026-11-20

## P032 — K2 Pro Motion Mechanism Lubrication

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2-pro/motion-mechanism-lubrication
- Source type: Official model-specific maintenance procedure
- Published/revised: Last edited 2025-08-18
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 Pro only
- Supports: Thin metal anti-rust oil for the X rail and generic grease for Y/Z shafts and lead screws
- Limitations/conflicts: Exact grease not named; do not transfer product locations to base K2 or other variants
- Confidence: High for K2 Pro only
- Review by: 2026-11-20

## P033 — K2 Camera Maintenance

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2/camera-maintenance
- Source type: Official model-specific maintenance procedure
- Published/revised: Last edited 2025-11-03
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Base-K2 monitoring camera
- Supports: Lint-free cloth and alcohol for dirty/blurry image; weekly attention with ABS
- Limitations/conflicts: Does not establish camera replacement, cable repair, network reset, emissions control, or cross-model compatibility
- Confidence: High
- Review by: 2026-11-20

## P034 — K2 Plus Maintenance Tips

- Publisher: Creality Service
- URL: https://wiki.creality.com/en/k2-flagship-series/k2-plus/maintenance-tips
- Source type: Official model-specific maintenance guide
- Published/revised: Last edited 2025-08-18
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: K2 Plus only
- Supports: K2 Plus-specific schedules, two-camera context, activated-carbon-filter maintenance, and model-specific distinctions
- Limitations/conflicts: Not transferable to base K2, K2 Pro, or K2 SE variants
- Confidence: High for K2 Plus only
- Review by: 2026-11-20

## P035 — Creality Cloud Firmware Printer-List API

- Publisher: Creality Cloud
- URL: https://www.crealitycloud.com/api/cxy/v2/device/firmwarePrinterList
- Source type: Official first-party public JSON endpoint used by the firmware UI; POST
- Published/revised: Live response on access date
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Public K2-family firmware catalog metadata
- Supports: Official catalog model names, build volumes, nozzle choices, internal IDs, and board identifiers
- Limitations/conflicts: POST-only and returns 404 to ordinary GET; K2/K2 Pro subtype labels/IDs conflict; not physical-unit proof
- Confidence: High for returned fields; medium for subtype mapping
- Review by: 2026-09-20

## P036 — Creality Cloud Firmware Search API

- Publisher: Creality Cloud
- URL: https://www.crealitycloud.com/api/cxy/search/firmwareSearch
- Source type: Official first-party public JSON endpoint used by the firmware UI; POST
- Published/revised: Live response through 2026-08-07 entries
- Accessed: 2026-08-20T18:56:01+02:00
- Applies to: Public K2, K2 Pro, K2 Plus, and K2 SE firmware records
- Supports: Versions, dates, filenames, board associations, and release-note fields observed in the official download UI
- Limitations/conflicts: POST-only and returns 404 to ordinary GET; public listing may differ from staged OTA/regional channels; installed versions unknown
- Confidence: High for observed records
- Review by: 2026-09-20

## C001 — Creality Print download

- Publisher: Creality
- URL: https://www.creality.com/download
- Source type: Official vendor download page
- Published/revised: Displays 2026-08-04 for Creality Print `V7.2.1.5476`
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Public Creality Print downloads on the access date
- Supports: Build `V7.2.1.5476`; macOS Apple and Intel download availability
- Limitations/conflicts: Dynamic page; does not expose complete release metadata; recheck before using `latest`
- Confidence: High
- Review by: 2026-09-20, or immediately when a newer release is reported

## C002 — Latest CrealityPrint release API record

- Publisher: CrealityOfficial on GitHub
- URL: https://api.github.com/repos/CrealityOfficial/CrealityPrint/releases/latest
- Source type: Official repository API
- Published/revised: `v7.2.1`, published 2026-08-04T13:23:29Z
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Latest public GitHub release at the access time
- Supports: `v7.2.1`; `draft=false`; `prerelease=false`; arm64 and x86_64 macOS asset names
- Limitations/conflicts: The `latest` endpoint is time-dependent and must be queried again for future claims
- Confidence: High
- Review by: 2026-09-20, or immediately when a newer release is reported

## C003 — Creality Print 7.2.1 Release Notes

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/releases/tag/v7.2.1
- Source type: Official release notes
- Published/revised: 2026-08-04T13:23:29Z
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1
- Supports: Context-aware AI inputs; 17 additional AI process parameters; localization changes; Prepare, support, G-code, camera, and setting-consistency fixes
- Limitations/conflicts: Release notes do not prove every runtime path, conditional feature, recommendation quality, or physical print result
- Confidence: High
- Review by: 2026-09-20

## C004 — Creality Print source tag v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/tree/v7.2.1
- Source type: Official tagged source
- Published/revised: Tag associated with the 2026-08-04 release
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 source
- Supports: Version-scoped implementation evidence for navigation, modes, Preferences, Process, Calibration, Preview, send/print actions, localization, and import formats
- Limitations/conflicts: Build flags and runtime state can hide source-defined controls; the installed UI was not launched
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

# Provisional material source records

These records cover the provisional M identifiers cited by the material and design references. Merge them into the repository source registry without dropping product applicability or conflicts.

## M001 — K2 Series 3D Printer support/specification page

- Publisher: Creality
- URL: https://www.creality.com/support/k2-series-3d-printer
- Source type: Official product support specification
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Creality K2; not proof that an unconfirmed K2C is K2
- Supports: 300 °C maximum nozzle; 100 °C maximum bed; all-metal hotend; steel-tipped trimetal 0.4 mm nozzle; listed PLA, ABS, PETG, PLA-CF, and PET materials
- Limitations/conflicts: Family listing does not endorse every formulation; no active chamber temperature was established; physical printer identity remains separate
- Confidence: High for stated K2 specifications
- Review by: 2026-11-20

## M002 — CFS Filament Compatibility Description

- Publisher: Creality Wiki
- URL: https://wiki.creality.com/en/cfs/cfs-filament-compatibility
- Source type: Official compatibility documentation
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Standard CFS, not CFS-C
- Supports: Spool diameter 197–202 mm and width 42–68 mm; named medium-hardness examples; TPU/elastic exclusion; moisture-softened PVA/BVOH exclusion; brittle PPA-CF/PPS-CF warning
- Limitations/conflicts: Family examples are not exhaustive SKU certification; more specific than the broad PA-CF product-page claim
- Confidence: High within standard-CFS scope
- Review by: 2026-11-20

## M003 — CFS: Creality Filament System product page

- Publisher: Creality Store
- URL: https://store.creality.com/au/products/cfs-creality-filament-system?country=AU&currency=AUD&variant=42512308076632
- Source type: Official product/marketing specification
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Standard CFS advertised material and spool envelope
- Supports: Advertised PLA, ABS, PETG, ASA, PET, PA-CF, and PLA-CF families; rejection of damp and flexible/TPU 95A filament
- Limitations/conflicts: Marketing family list lacks exact SKU matrix; constrain PA-CF with M002 brittle-material warning
- Confidence: Medium
- Review by: 2026-11-20

## M004 — CFS-C filament parameters

- Publisher: Creality Wiki
- URL: https://wiki.creality.com/en/cfs-c/filament-parameters
- Source type: Official compatibility matrix
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: CFS-C only
- Supports: Named Creality material statuses; TPU unavailable; PPA-CF, PAHT-CF, PET-CF, PPS-CF Not Suggested; generic PA6-CF/PA12-CF/PA612-CF and PVA/BVOH usable
- Limitations/conflicts: Cannot be transferred to standard CFS; feed status does not establish printer thermal compatibility
- Confidence: High within CFS-C scope
- Review by: 2026-11-20

## M006 — K2 Plus chamber temperature guide

- Publisher: Creality Wiki
- URL: https://wiki.creality.com/en/k2-flagship-series/k2-plus/chamber-temp
- Source type: Official operating guidance
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: K2 Plus chamber controls only
- Supports: 35 °C low-temperature-material and 60 °C high-temperature-material guidance; consult material manufacturer
- Limitations/conflicts: Must not be transposed to K2 or an unconfirmed K2C
- Confidence: High for K2 Plus; none for other variants
- Review by: 2026-11-20

## M007 — Creality 3D printer filament type and parameter guide

- Publisher: Creality Store
- URL: https://store.creality.com/blogs/all/creality-3d-printer-filaments-type-parameter
- Source type: Official manufacturer help/marketing article
- Published/revised: Not reliably exposed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Named Creality CR and HP filament families in its table
- Supports: CR-PLA, Matte, Silk, PETG, TPU, ABS, Wood, PLA Carbon, PA Carbon, HP-ASA, and HP-HIPS ranges; direct-drive and enclosure suggestions
- Limitations/conflicts: Not a controlled TDS; HP-ASA values conflict with M017; exact spool label/TDS has higher authority
- Confidence: Medium
- Review by: 2026-11-20

## M008 — Hyper PLA filament product page

- Publisher: Creality Store
- URL: https://store.creality.com/products/hyper-pla-filament-1-75mm-10kg-white-color
- Source type: Official product specification/marketing page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Named Creality Hyper PLA product
- Supports: 190–230 °C nozzle; 25–60 °C bed; 30–600 mm/s; 100% fan
- Limitations/conflicts: 600 mm/s is a product ceiling without a verified K2 flow guarantee; not a universal PLA profile
- Confidence: Medium
- Review by: 2026-11-20

## M009 — Polymaker PLA Pro TDS v6.0

- Publisher: Polymaker
- URL: https://polymaker.com/wp-content/uploads/lana-downloads/TDS_Polymaker_PLA-Pro_v6.0_2026-01-30_EN.pdf
- Source type: Official TDS
- Published/revised: v6.0, 2026-01-30
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Polymaker PLA Pro under its stated product/test conditions
- Supports: 210–230 °C nozzle; up to 300 mm/s; 55 °C for 6 h drying when moisture was absorbed
- Limitations/conflicts: Differs from older PolyLite PLA Pro M010; identify exact spool/revision
- Confidence: High
- Review by: 2027-01-30

## M010 — PolyLite PLA Pro wiki/product record

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/prime-materials/functional-pla/polylite-tm-pla-pro
- Source type: Official product parameter page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: PolyLite PLA Pro formulation described by the page
- Supports: 190–220 °C nozzle; 30–60 °C bed; 30–70 mm/s; 15 mm³/s maximum volumetric speed
- Limitations/conflicts: Conflicts with M009; do not merge ranges across revisions/products
- Confidence: High for the page; low for cross-revision use
- Review by: 2026-11-20

## M011 — PolyWood PLA TDS v2.0

- Publisher: Polymaker
- URL: https://polymaker.com/wp-content/uploads/TDS_Polymaker_Polywood-PLA_2.0_2026-06-08_EN.pdf
- Source type: Official TDS
- Published/revised: v2.0, 2026-06-08
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Polymaker PolyWood PLA
- Supports: Foamed PLA without wood powder; 190–210 °C nozzle; 25–60 °C bed; 50–100 mm/s; fan on; 55 °C for 6 h drying
- Limitations/conflicts: Name does not imply actual wood fill and cannot characterize other wood filaments
- Confidence: High
- Review by: 2027-06-08

## M012 — Composite materials with metal or wood particles

- Publisher: Prusa Research
- URL: https://help.prusa3d.com/article/composite-materials-with-metal-or-wood-particles_166863
- Source type: Official manufacturer help article
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Prusa-described particle-filled materials
- Supports: Clogging/brittleness and weaker-adhesion cautions; hardened nozzle for metal; at least 0.6 mm nozzle and 0.2 mm layer starting guidance for large-particle wood products
- Limitations/conflicts: Product-class starting points, not universal rules or K2 limits
- Confidence: Medium
- Review by: 2027-02-20

## M013 — Hyper PETG filament product page

- Publisher: Creality Store
- URL: https://store.creality.com/products/hyper-series-petg-3d-printing-filament-1kg
- Source type: Official product specification/marketing page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Named Creality Hyper PETG product
- Supports: 190–260 °C nozzle; 45 °C bed; 50–300 mm/s
- Limitations/conflicts: Unusually broad product-page range conflicts with narrower PETG products; exact spool controls
- Confidence: Medium
- Review by: 2026-11-20

## M014 — PolyLite PETG parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/prime-materials/petg/polylite-tm-petg
- Source type: Official product parameter page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: PolyLite PETG
- Supports: 230–260 °C nozzle; 70–80 °C bed; fan 0–20%; 50–100 mm/s; maximum volumetric speed at or below 15 mm³/s; 65 °C for 6 h drying
- Limitations/conflicts: Does not apply to Hyper PETG or newer Polymaker PETG
- Confidence: High
- Review by: 2026-11-20

## M015 — Polymaker PETG new formulation parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/prime-materials/petg/polymaker-tm-petg-new
- Source type: Official product parameter page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Newer named Polymaker PETG
- Supports: 240–260 °C nozzle; 60–70 °C bed; fan 20–60%; up to 300 mm/s; hardware-specific 22/32 mm³/s examples; 60 °C for 6 h drying
- Limitations/conflicts: High-flow examples are hardware-specific and not K2 defaults
- Confidence: High for product data; low for cross-printer flow
- Review by: 2026-11-20

## M016 — Hyper ABS filament product page

- Publisher: Creality Store
- URL: https://store.creality.com/eu/products/hyper-abs-3d-printing-filament
- Source type: Official product specification/marketing page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Named Creality Hyper ABS formulation
- Supports: 230–270 °C nozzle; 75–95 °C bed; reduced-shrinkage and no-enclosure product claims
- Limitations/conflicts: Conflicts with generic CR-ABS enclosure guidance; no-enclosure claim cannot generalize
- Confidence: Medium
- Review by: 2026-11-20

## M017 — HP ASA filament product page

- Publisher: Creality Store
- URL: https://store.creality.com/products/creality-hp-asa-3d-printing-filament
- Source type: Official product specification/marketing page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Named Creality HP ASA product
- Supports: 200–300 °C nozzle; 50–100 °C bed; 40–300 mm/s; ventilation recommendation
- Limitations/conflicts: Materially conflicts with M007 generic chart; exact current spool/TDS required
- Confidence: Low until product revision is identified
- Review by: 2026-10-20

## M018 — PolyLite ABS technical-data page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/abs-asa/polylite-tm-abs
- Source type: Official technical-data page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: PolyLite ABS
- Supports: 245–265 °C nozzle; 90–100 °C bed; fan off; 50–200 mm/s; ambient enclosure; 70 °C for 6 h drying
- Limitations/conflicts: Formulation-specific
- Confidence: High
- Review by: 2026-11-20

## M019 — PolyLite ASA technical-data page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/more-about-our-products/documents/technical-data-sheets/abs-asa/polylite-tm-asa
- Source type: Official technical-data page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: PolyLite ASA
- Supports: 230–260 °C nozzle; 75–95 °C bed; fan off; 50–200 mm/s; enclosure; 70 °C for 7 h drying
- Limitations/conflicts: Formulation-specific and cannot resolve Creality HP-ASA conflict
- Confidence: High
- Review by: 2026-11-20

## M020 — Ultrafuse HIPS TDS v2.2

- Publisher: BASF Forward AM
- URL: https://move.forward-am.com/hubfs/AES%20Documentation/Support%20Filaments/HiPS/TDS/Ultrafuse_HiPS_TDS_EN_v2.2.pdf
- Source type: Official TDS
- Published/revised: v2.2; date not separately displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Ultrafuse HIPS
- Supports: 240–260 °C nozzle; 100–120 °C bed; 0.4 mm or larger; 40–80 mm/s; 60 °C for 4–16 h drying; ABS support use
- Limitations/conflicts: Candidate K2 bed covers only the lowest point; pairing and removal need physical test
- Confidence: High
- Review by: 2027-08-20

## M063 — UltiMaker S8 Declaration of Safe Unattended Professional Use

- Publisher: UltiMaker
- URL: https://um-support-files.ultimaker.com/safety-compliance/DoSUPU/20250422_UM%20S8_USP25-Sy_DoSUPU.pdf
- Source type: Official model-specific manufacturer declaration
- Published/revised: 2025-04-22
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: UltiMaker S8 under the declaration's professional-use, manual, test, and material conditions
- Supports: Unattended-use status can be a narrow model- and scope-specific declaration
- Limitations/conflicts: Has no applicability to Creality K2 or K2C and cannot replace a missing Creality declaration
- Confidence: High within the declared scope
- Review by: 2027-04-22

## M036 — Hyper PLA-CF filament product page

- Publisher: Creality Store
- URL: https://store.creality.com/as/products/hyper-pla-carbon-fiber-3d-printing-filament-1kg
- Source type: Official product specification/marketing page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Named Creality Hyper PLA-CF product
- Supports: 190–230 °C nozzle; 45 °C bed; 50–300 mm/s; 55 °C/8 h forced-air or 75 °C/12 h heated-bed drying alternatives
- Limitations/conflicts: Page does not state hardened-nozzle need; silence does not prove non-abrasiveness
- Confidence: Medium
- Review by: 2026-11-20

## M037 — Hyper PETG-CF filament product page

- Publisher: Creality Store
- URL: https://store.creality.com/products/hyper-petg-cf-3d-printing-filament-1kg
- Source type: Official product specification/marketing page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Named Creality Hyper PETG-CF product
- Supports: 240–260 °C nozzle; 70–90 °C bed; fan 80%; 30–300 mm/s; hardened/wear-resistant nozzle requirement
- Limitations/conflicts: K2 page lists PLA-CF, not PETG-CF; thermal fit is not endorsement
- Confidence: High for tooling requirement; medium otherwise
- Review by: 2026-11-20

## M038 — Fiberon PA6-GF25 parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-wiki-pt/produtos-polymaker/filamentos-polymaker/fiberon-tm/fiberon-tm-pa6-gf25
- Source type: Official product parameter page; Portuguese locale
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Fiberon PA6-GF25
- Supports: 280–300 °C nozzle; 40–50 °C bed; fan off; 30–300 mm/s; hardened nozzle; dry feed; annealing procedure
- Limitations/conflicts: Product-specific; no K2 endorsement
- Confidence: High
- Review by: 2026-11-20

## M039 — Fiberon PET-CF17 parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pet-cf17
- Source type: Official product parameter page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Fiberon PET-CF17
- Supports: 270–300 °C nozzle; 70–80 °C bed; fan off; 30–300 mm/s; all-metal hotend; hardened nozzle; no heated enclosure required; 120 °C/10 h anneal
- Limitations/conflicts: PET-CF is not plain PET; annealing requires dimensional validation
- Confidence: High
- Review by: 2026-11-20

## M040 — Fiberon PET-GF15 parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pet-gf15
- Source type: Official product parameter page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Fiberon PET-GF15
- Supports: 280–310 °C nozzle; 70–80 °C bed; fan off; 30–250 mm/s; hardened nozzle; 120 °C/16 h anneal
- Limitations/conflicts: Upper nozzle range exceeds candidate K2; never command 310 °C
- Confidence: High
- Review by: 2026-11-20

## M041 — PPA-CF filament product page

- Publisher: Creality Store
- URL: https://store.creality.com/eu/products/ppa-cf-carbon-fiber-3d-printing-filament
- Source type: Official product specification/marketing page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Named Creality PPA-CF product
- Supports: 280–300 °C nozzle; 90–105 °C bed; enclosure; 80 °C forced-air drying for 8–12 h
- Limitations/conflicts: Not listed in K2 materials; reaches/exceeds candidate limits; standard CFS warns about PPA-CF brittleness
- Confidence: Medium for material parameters; no K2 endorsement
- Review by: 2026-11-20

## M042 — Ultrafuse PAHT-CF15 TDS v3.4

- Publisher: BASF Forward AM
- URL: https://ultrafusefff.jp/basf3d/wp-content/uploads/2021/03/Ultrafuse_PAHT_CF15_TDS_EN_v3.4.pdf
- Source type: Official TDS
- Published/revised: v3.4; upload path 2021-03
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Ultrafuse PAHT-CF15
- Supports: 260–280 °C nozzle; 100–120 °C bed; 0.6 mm or larger ruby/hardened nozzle; 30–80 mm/s; 70 °C/4–16 h or vacuum 80 °C/at least 40 h drying
- Limitations/conflicts: Full bed range exceeds candidate K2; no official K2 compatibility
- Confidence: High
- Review by: 2027-08-20

## M043 — Fiberon PPS-CF10 parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pps-cf10
- Source type: Official product parameter page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Fiberon PPS-CF10
- Supports: 310–350 °C nozzle; 80–90 °C bed; 25–80 °C ambient; hardened nozzle; brittle clear path; no AMS recommendation; 125 °C/16 h anneal
- Limitations/conflicts: Flame-performance wording is explicitly not UL 94 product certification
- Confidence: High
- Review by: 2026-11-20

## M044 — Ultrafuse PPSU TDS v1.5

- Publisher: BASF Forward AM
- URL: https://ultrafusefff.jp/basf3d/wp-content/uploads/2021/03/Ultrafuse_PPSU_TDS_EN_v1.5.pdf
- Source type: Official TDS
- Published/revised: v1.5; upload path 2021-03
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Ultrafuse PPSU
- Supports: 390–410 °C nozzle; 220 °C bed; 170–210 °C chamber; 0.4 mm or larger; 25–50 mm/s; vacuum 125 °C/8 h drying
- Limitations/conflicts: Requirements are outside candidate K2 specifications
- Confidence: High
- Review by: 2027-08-20

## M045 — PEI / ULTEM

- Publisher: Prusa Research
- URL: https://help.prusa3d.com/article/pei-ultem_725809
- Source type: Official manufacturer material guide
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: PEI/ULTEM high-temperature printing guidance
- Supports: 370–420 °C nozzle; 150–155 °C bed; specialized high-temperature equipment
- Limitations/conflicts: Not a K2 profile; establishes incompatibility against candidate limits
- Confidence: High
- Review by: 2027-02-20

## M046 — Creality filament dryer manual

- Publisher: Creality
- URL: https://cdn.creality.com/ow/official/091e8007-39af-4418-aa46-75e97f1fd6ef.pdf
- Source type: Official device manual
- Published/revised: Version/date not reliably exposed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Covered Creality dryer and its recommendation chart
- Supports: Material-family example drying times/temperatures; explicit instruction to follow actual filament manufacturer
- Limitations/conflicts: Cannot replace exact TDS/SDS, spool limit, or calibrated dryer
- Confidence: High within device scope
- Review by: 2027-02-20

## M047 — Drying filament

- Publisher: Prusa Research
- URL: https://help.prusa3d.com/article/drying-filament_332086
- Source type: Official manufacturer help article
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Named Prusament products and general dryer precautions
- Supports: Product-specific example cycles; do-not-exceed warning; spool heat resistance; household oven control/overheating risk; external thermometer
- Limitations/conflicts: Prusament chart is not a universal polymer chart
- Confidence: High
- Review by: 2027-02-20

## M048 — Polymaker Quality Options

- Publisher: Polymaker Wiki
- URL: https://wiki.polymaker.com/the-basics/3d-printers/quality-options
- Source type: Official manufacturer design/printing guidance
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Generic FDM starts under Polymaker assumptions
- Supports: Features narrower than line may disappear; clearance around half a nozzle as heuristic; layer height roughly 25–75% of nozzle diameter
- Limitations/conflicts: Heuristics, not K2 capability or dimensional certification
- Confidence: Medium
- Review by: 2027-02-20

## M049 — Design for FFF 3D printing: maximize your success

- Publisher: UltiMaker
- URL: https://ultimaker.com/learn/design-for-fff-3d-printing-maximize-your-success/
- Source type: Official manufacturer design guide
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Design starting points under UltiMaker examples
- Supports: Anisotropy/orientation; 45° overhang; about 10 mm generic bridge and tuned 25 mm Tough PLA example; 0.5 mm wall; 2 mm hole; 0.6 mm print-in-place gap; bottom chamfer
- Limitations/conflicts: Every number is machine/nozzle/material/profile dependent; not K2 limits
- Confidence: Medium for heuristics; high for named examples
- Review by: 2027-02-20

## M050 — How to design for FFF

- Publisher: UltiMaker
- URL: https://ultimaker.com/wp-content/uploads/2024/06/How-to-design-for-FFF-1.pdf
- Source type: Official manufacturer design guide PDF
- Published/revised: Upload path 2024-06; exact revision not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: General FFF design education
- Supports: 45-degree rule as a starting point; shorter bridges are more reliable; orientation/support considerations
- Limitations/conflicts: Not a material or printer qualification
- Confidence: Medium
- Review by: 2027-02-20

## M051 — Modeling with 3D printing in mind

- Publisher: Prusa Research
- URL: https://help.prusa3d.com/article/modeling-with-3d-printing-in-mind_164135
- Source type: Official manufacturer design guide
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Prusa examples and general DfAM heuristics
- Supports: 45–60° common overhang and named Nextruder up to 75°; split/orient; chamfer versus bed-facing fillet; 0.45 mm perimeter multiples; no universal tolerance; about 0.2 mm accuracy context and 0.3 mm moving-clearance start; anisotropy/manifold requirement
- Limitations/conflicts: Named printer performance is not K2 performance; tolerances require coupons
- Confidence: High for named Prusa examples; medium as general heuristic
- Review by: 2027-02-20

## M052 — Additive manufacturing design parameters reference

- Publisher: Autodesk
- URL: https://help.autodesk.com/cloudhelp/ENU/Fusion-GenerativeDesign/files/GD-ADDITIVE-REF.htm
- Source type: Official software/manufacturer design reference
- Published/revised: Live documentation; date not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Fusion additive constraints and their interpretation
- Supports: 45° common default; overhang angle and minimum thickness depend on material, machine, and process
- Limitations/conflicts: Software default, not a K2-measured limit
- Confidence: High for dependency statement; medium for default
- Review by: 2027-02-20

## M053 — Designing 3D printed snap-fit enclosures

- Publisher: Formlabs
- URL: https://formlabs.com/global/blog/designing-3d-printed-snap-fit-enclosures/
- Source type: Official manufacturer design article
- Published/revised: Not reliably displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Snap-fit design concepts and discussed processes
- Supports: FDM snap-fit orientation sensitivity; XY preferable to Z peel; longer/tapered/curved hooks reduce stress concentration
- Limitations/conflicts: Example dimensions are geometry/material/process specific
- Confidence: Medium
- Review by: 2027-02-20

## M054 — Threading and inserts for 3D printing

- Publisher: Protolabs
- URL: https://www.protolabs.com/resources/blog/threading-and-inserts-for-3d-printing/
- Source type: Official manufacturing-service engineering article
- Published/revised: 2024-10-29
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Additive thread/insert selection in discussed services
- Supports: As-printed thread reliability depends on process/material/size; critical threads need a controlled post-process or insert strategy
- Limitations/conflicts: Not K2-specific and not an insert-temperature source
- Confidence: Medium
- Review by: 2027-02-20

## M055 — Composites Design Guide

- Publisher: Markforged
- URL: https://static.markforged.com/downloads/CompositesDesignGuide.pdf
- Source type: Official manufacturer design guide
- Published/revised: Version/date not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Markforged composite-part design context
- Supports: Metal inserts/wear surfaces can improve thread durability/service over relying on printed composite threads
- Limitations/conflicts: Markforged context; dimensions and loading cannot transfer without supplier guidance
- Confidence: Medium
- Review by: 2027-02-20

## M056 — Approaches to Safe 3D Printing: A Guide for Makerspace Users, Schools, Libraries, and Small Businesses

- Publisher: U.S. National Institute for Occupational Safety and Health, CDC
- URL: https://www.cdc.gov/niosh/docs/2024-103/pdfs/2024-103.pdf
- Source type: Official government occupational-safety guide
- Published/revised: November 2023; NIOSH Publication No. 2024-103
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Additive-manufacturing risk management including material extrusion
- Supports: UFP/VOC/SVOC, heat, motion, electrical, solvent, and post-processing hazards; variable emissions; hierarchy of controls; maintenance de-energization
- Limitations/conflicts: General occupational guidance, not K2 certification or material-specific exposure limit
- Confidence: High
- Review by: 2027-08-20

## M057 — 3D Printing with Filaments: Health and Safety Questions to Ask

- Publisher: NIOSH, CDC
- URL: https://www.cdc.gov/niosh/docs/2020-115/pdfs/2020-115.pdf
- Source type: Official government guidance poster
- Published/revised: March 2020; NIOSH Publication No. 2020-115
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Filament-material-extrusion exposure control
- Supports: Prefer PLA over ABS when suitable; consider additives/temperature; ventilation/negative pressure; HEPA/local exhaust for particles and gas/vapor media for VOCs; access restriction; lowest effective temperature
- Limitations/conflicts: Qualitative controls; not a declaration that PLA is safe or a filter removes all emissions
- Confidence: High
- Review by: 2027-08-20

## M058 — Characterizing 3D Printing Emissions and Controls in an Office Environment

- Publisher: NIOSH, CDC
- URL: https://www.cdc.gov/niosh/bulletin/2018/3d-printing.html
- Source type: Official government field-study summary
- Published/revised: 2018-08-16
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Tested printers, PLA/ABS/Tough PLA, room, and controls
- Supports: Observed emissions and local-exhaust/HEPA reduction; absence of specific OELs for total 3D-printing emissions; toxicology uncertainty
- Limitations/conflicts: Study concentrations cannot generalize to another printer, material, room, or occupancy
- Confidence: High for study; low for extrapolation
- Review by: 2027-08-20

## M059 — Additive Manufacturing and 3D Printing

- Publisher: NIOSH, CDC
- URL: https://www.cdc.gov/niosh/manufacturing/additive/index.html
- Source type: Official government topic page
- Published/revised: 2026-03-03
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Additive-manufacturing hazards and controls
- Supports: FFF respiratory irritants; material/color effects on VOCs; nanomaterial-containing filament can emit nanomaterial particulate
- Limitations/conflicts: Broad hazard page, not a product exposure measurement
- Confidence: High
- Review by: 2027-03-03

## M060 — 3D Printing Research at EPA

- Publisher: U.S. Environmental Protection Agency
- URL: https://www.epa.gov/chemical-research/3d-printing-research-epa
- Source type: Official government research overview
- Published/revised: Exact displayed revision not captured
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Indoor emissions research including consumer and school contexts
- Supports: VOC/gas and UFP emissions; 1–100 nm particle scale and deep respiratory deposition concern
- Limitations/conflicts: Research overview, not a K2 risk assessment or exposure limit
- Confidence: High
- Review by: 2027-08-20

## M061 — ANSI/CAN/UL 2904 publication announcement

- Publisher: Underwriters Laboratories
- URL: https://ul.org/press-releases/underwriters-laboratories-publishes-ansi-can-ul-2904-standard-for-3d-printers/
- Source type: Official standards-organization announcement
- Published/revised: 2019
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: UL 2904 method and scope for 3D-printer emissions
- Supports: Measurement and assessment methods for particle and chemical emissions from indoor 3D printers
- Limitations/conflicts: Standard existence does not mean a printer/material is certified or low-emission
- Confidence: High
- Review by: 2027-08-20

## M062 — UL 200B Safe Use of 3D Printing for Institutions of Higher Education

- Publisher: Chemical Insights Research Institute of Underwriters Laboratories
- URL: https://chemicalinsights.ul.org/wp-content/uploads/2023/05/UL-200B_1.pdf
- Source type: Official institutional safe-use guideline
- Published/revised: File path 2023-05; UL 200B series
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Institutional additive-manufacturing risk controls
- Supports: Use SDS; address composite/nylon/chopped-CF emissions and post-processing; engineering, administrative, and PPE controls
- Limitations/conflicts: Institutional guidance, not K2 certification
- Confidence: High
- Review by: 2027-08-20

## M065 — Ultrafuse PLA TDS v4.4

- Publisher: BASF Forward AM
- URL: https://ultrafusefff.jp/basf3d/wp-content/uploads/2021/03/Ultrafuse_PLA_TDS_EN_v4.4.pdf
- Source type: Official TDS
- Published/revised: v4.4; upload path 2021-03
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Ultrafuse PLA
- Supports: 210–230 °C nozzle; 50–70 °C bed; 0.4 mm or larger; 40–80 mm/s; drying not necessary as supplied under documented condition
- Limitations/conflicts: Shows automatic drying is not universal; does not override another PLA TDS after moisture exposure
- Confidence: High
- Review by: 2027-08-20


## M021 — PolyFlex TPU95 parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/prime-materials/flexible-tpu/polyflex-tm-tpu95
- Source type: Official product parameter page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: PolyFlex TPU95
- Supports: Shore 95A; 210–230 °C nozzle; 25–60 °C bed; fan on; 30–50 mm/s; no enclosure; 70 °C for 8 h drying; direct drive recommended
- Limitations/conflicts: Hardness/profile do not apply to all TPU/TPE
- Confidence: High
- Review by: 2026-11-20

## M022 — Ultrafuse TPU 85A TDS

- Publisher: BASF Forward AM
- URL: https://ultrafusefff.jp/basf3d/wp-content/uploads/2024/11/Ultrafuse_TPU_85A_TDS_EN_v2.5.pdf
- Source type: Official TDS
- Published/revised: Document identifies v3.0; filename says v2.5
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Ultrafuse TPU 85A
- Supports: Shore 85A; 200–220 °C nozzle; 40 °C bed; no chamber; 0.4 mm or larger; 15–40 mm/s; 70 °C for at least 5 h drying; BVOH/HIPS pairing
- Limitations/conflicts: Filename/document version mismatch; support pairing still requires interface/purge validation
- Confidence: High for contents; medium for version metadata
- Review by: 2027-08-20

## M023 — Ultrafuse TPU 64D TDS v1.1

- Publisher: BASF Forward AM
- URL: https://ultrafusefff.jp/basf3d/wp-content/uploads/2024/11/Ultrafuse_TPU_64D_TDS_EN_v1.1.pdf
- Source type: Official TDS
- Published/revised: v1.1; upload path 2024-11
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Ultrafuse TPU 64D
- Supports: Shore 64D; 230–255 °C nozzle; 40–60 °C bed; 0.4 mm or larger; 30–60 mm/s; 70 °C for at least 5 h drying; BVOH/HIPS pairing
- Limitations/conflicts: Shore D is not numerically interchangeable with Shore A
- Confidence: High
- Review by: 2027-08-20

## M024 — PolyMide CoPA parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/prime-materials/nylon-pa/polymide-tm-copa
- Source type: Official product parameter and FAQ page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: CoPA PA6/PA6,6 blend
- Supports: 250–270 °C nozzle; 25–50 °C bed; all-metal hotend; 100 °C for 8 h drying; 80 °C for 6 h anneal
- Limitations/conflicts: Conditions table and FAQ disagree on enclosure need
- Confidence: High for temperatures; low for enclosure
- Review by: 2026-11-20

## M025 — Fiberon PA6-CF20 parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pa6-cf20
- Source type: Official product parameter page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Fiberon PA6-CF20
- Supports: 20% CF; 280–300 °C nozzle; 40–50 °C bed; fan off; hardened nozzle; all-metal hotend; dry feed; 100 °C for 16 h anneal
- Limitations/conflicts: Low-bed/ambient Warp-Free behavior is formulation-specific
- Confidence: High
- Review by: 2026-11-20

## M026 — Fiberon PA12-CF10 parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/fiberon-tm/fiberon-tm-pa12-cf10
- Source type: Official product parameter page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Fiberon PA12-CF10
- Supports: 280–300 °C nozzle; 40–50 °C bed; hardened nozzle; all-metal hotend; dry feed; 100 °C for 16 h anneal; lower moisture sensitivity relative to cited PA6 formulation
- Limitations/conflicts: Relative moisture claim is not moisture immunity
- Confidence: High
- Review by: 2026-11-20

## M027 — Ultrafuse PA TDS v3.1

- Publisher: BASF Forward AM
- URL: https://move.forward-am.com/hubfs/AES%20Documentation/Engineering%20Filaments/PA/TDS/Ultrafuse_PA_TDS_EN_v2.2.pdf?hsLang=en
- Source type: Official TDS
- Published/revised: Revised 2024-08-12; document v3.1; URL filename v2.2
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Ultrafuse glass-reinforced PA
- Supports: Abrasive glass reinforcement; hardened nozzle/drive wheels advised; 220–250 °C nozzle; 90–120 °C bed; passive closed chamber; 30–60 mm/s; 80 °C for at least 40 h drying; ventilation
- Limitations/conflicts: Filename/document version mismatch; not an unfilled-PA profile
- Confidence: High for document contents
- Review by: 2027-08-12

## M028 — Hyper PC filament product page

- Publisher: Creality Store
- URL: https://store.creality.com/ca/products/hyper-pc-filament-1-75mm-1kg
- Source type: Official product specification/marketing page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Named Creality Hyper PC product
- Supports: 240–260 °C nozzle; 50–80 °C bed; 30–300 mm/s; listed PEI/carbon-crystal surfaces
- Limitations/conflicts: No K2 endorsement or enclosure evidence; differs sharply from M029
- Confidence: Medium for product values; low for printer compatibility
- Review by: 2026-11-20

## M029 — PolyMax PC parameter page

- Publisher: Polymaker
- URL: https://wiki.polymaker.com/polymaker-products/polymaker-filaments/prime-materials/polycarbonate/polymax-tm-pc
- Source type: Official product parameter page
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: PolyMax PC
- Supports: 250–270 °C nozzle; 90–105 °C bed; 70–100 °C chamber; fan off; 50–200 mm/s; 12 mm³/s; 75 °C for 6 h drying; 90 °C for 2 h anneal
- Limitations/conflicts: Product-specific and much more demanding than Hyper PC
- Confidence: High
- Review by: 2026-11-20

## M030 — PolyDissolve S1 product page

- Publisher: Polymaker
- URL: https://shop.polymaker.com/en-eu/products/polydissolve-s1
- Source type: Official product specification
- Published/revised: Not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: PolyDissolve S1 support filament
- Supports: 215–225 °C nozzle; 25–60 °C bed; 30–40 mm/s; fan on; 80 °C for 12 h drying; hygroscopicity; named pairing matrix
- Limitations/conflicts: Separate Polymaker wiki page lists 50–150 mm/s; dissolution depends on geometry/process
- Confidence: High for product; low for unresolved speed
- Review by: 2026-11-20

## M031 — PolyDissolve S1 product information sheet v1.1

- Publisher: Polymaker
- URL: https://polymaker.com/wp-content/tech-docs/PolyDissolve_S1_PIS_EN_V1.1.pdf
- Source type: Official product information sheet
- Published/revised: v1.1; exact day not exposed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: PolyDissolve S1
- Supports: 215–225 °C nozzle; 25–60 °C bed; 30–40 mm/s; Z gap 0 and XY distance 0.5 mm product starting values
- Limitations/conflicts: Interface values are starts, not guarantees; speed conflicts with separate wiki
- Confidence: High for v1.1 parameters
- Review by: 2027-08-20

## M032 — UltiMaker PVA TDS v5.00

- Publisher: UltiMaker
- URL: https://um-support-files.ultimaker.com/materials/2.85mm/tds/PVA/Ultimaker-PVA-TDS-v5.00.pdf
- Source type: Official TDS
- Published/revised: v5.00; date not displayed
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: UltiMaker PVA in its 2.85 mm ecosystem
- Supports: Water solubility; named adhesion with PLA, PETG, Nylon; unsuitability with UltiMaker ABS, CPE+, PC, PP
- Limitations/conflicts: Pairing evidence only; not a 1.75 mm Creality profile
- Confidence: High within product scope
- Review by: 2027-08-20

## M033 — Ultrafuse BVOH TDS v1.3

- Publisher: BASF Forward AM
- URL: https://move.forward-am.com/hubfs/AES%20Documentation/Support%20Filaments/BVOH/TDS/Ultrafuse_BVOH_TDS_DE_v1.3.pdf
- Source type: Official TDS; German edition
- Published/revised: v1.3, 2019-11-11
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Ultrafuse BVOH
- Supports: Water solubility; 190–210 °C nozzle; 60–100 °C bed; 0.4 mm or larger; 30–60 mm/s; 60 °C for 4–16 h drying; named pairings; sealed 15–25 °C storage
- Limitations/conflicts: German first-party edition; pairing still requires interface/purge/removal testing
- Confidence: High
- Review by: 2027-08-20

## M034 — Ultrafuse PP TDS v4.0

- Publisher: BASF Forward AM
- URL: https://ultrafusefff.jp/basf3d/wp-content/uploads/2024/11/Ultrafuse_PP_TDS_EN_v4.0.pdf
- Source type: Official TDS
- Published/revised: v4.0; upload path 2024-11
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Ultrafuse PP
- Supports: 220–240 °C nozzle; 60–80 °C bed; PP tape/adhesive; 0.4 mm or larger; 20–50 mm/s; 60 °C for 4–16 h drying
- Limitations/conflicts: No K2 or CFS approval; surface system is product-specific
- Confidence: High
- Review by: 2027-08-20

## M035 — Ultrafuse PP GF30 TDS v2.3

- Publisher: BASF Forward AM
- URL: https://forward-am.com/wp-content/uploads/2021/07/Ultrafuse_PP_GF30_TDS_EN_v2.3-2.pdf
- Source type: Official TDS
- Published/revised: v2.3; upload path 2021-07
- Accessed: 2026-08-20T18:51:02+02:00
- Applies to: Ultrafuse PP GF30
- Supports: 240–260 °C nozzle; alternative 20–40 °C or 70–90 °C bed tied to named surfaces; 0.6 mm or larger; 30–80 mm/s; 60 °C for 4–16 h drying
- Limitations/conflicts: Bed alternatives cannot be detached from their tapes/adhesives; exact tooling must be confirmed
- Confidence: High
- Review by: 2027-08-20

## C005 — BBLTopbar.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/BBLTopbar.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 top navigation and edition switch
- Supports: `Online Models`, `Prepare`, `Preview`, `Device`; `AI`, `Pro`, and `Switch AI/Pro mode`; `easy_print_mode`
- Limitations/conflicts: Source placement is not visual observation; responsive layout and selected-state styling were not inspected
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

## C006 — ParamsPanel.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/ParamsPanel.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 Process and preset-edit panels
- Supports: `Process`; `Global`; `Objects`; `Printer settings`; `Filament settings`
- Limitations/conflicts: Does not prove actual selected context, scroll position, visible values, or defaults
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

## C007 — Plater.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/Plater.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 Process category toolbar
- Supports: `Frequent`, `Quality`, `Strength`, `Speed`, `Support`, `Multimaterial`, `Others`; Speed advanced-role visibility; STEP loading implementation
- Limitations/conflicts: `Frequent` is hidden in the inspected setup; category contents and runtime state are defined elsewhere
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

## C008 — GLToolbarProcess.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/GLToolbarProcess.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 Process category visibility
- Supports: Support hidden for per-part and per-layer tabs and visible for the normal print tab
- Limitations/conflicts: No running panel or actual selected object was observed
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

## C009 — GUI_ObjectList.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/GUI_ObjectList.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 per-object and modifier process mode
- Supports: Automatic switch to per-object mode and the modifier/object process instruction strings
- Limitations/conflicts: Does not document every override precedence or screen gesture
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

## C010 — Preferences.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/Preferences.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 Preferences
- Supports: `Basic`/`Professional`; `User Role`; language, region, units, Easy mode, rendering, Preview, STEP-dialog, and conditional cloud settings
- Limitations/conflicts: Cloud-build fields are conditional; current defaults and running state were not observed
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

## C011 — MainFrame.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/MainFrame.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 macOS menus, slicing, calibration, export, send, and print actions
- Supports: macOS Preferences; stable and alpha-gated Calibration entries; `Slice plate`, `Slice all`, `Print plate`, `Print all`, `Send`, `Send all`, export actions, and conditional multi-device action
- Limitations/conflicts: Runtime enablement depends on page, valid slice, vendor, host, device, and build; button layout was not visually observed
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

## C012 — BaseRenderer.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/GCodeRenderer/BaseRenderer.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 Preview renderer
- Supports: View labels and units; Line Type labels; filament statistics; Lite Mode location, filtering, tooltip, and re-slice behavior
- Limitations/conflicts: Compile flags and actual G-code determine visible views/roles; no active legend or sliced model was observed
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

## C013 — GUI_Preview.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/GUI_Preview.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 Preview loading and Lite Mode gating
- Supports: Raw G-code and G-code-only 3MF previews use normal/non-Lite rendering; Lite filtering is applied to project slice results
- Limitations/conflicts: Does not provide a visual screenshot or physical-print validation
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

## C014 — SendPage.pot at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/localization/i18n/SendPage.pot
- Source type: Official tagged English localization template
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 send page
- Supports: `Start Print`, `Send Only`, plate/device/network labels, CFS/spool-holder mapping labels, mismatch and unmapped-filament messages
- Limitations/conflicts: Strings prove potential labels, not exact layout or availability on a particular printer
- Confidence: High for labels; medium for navigation
- Review by: 2026-09-20, or immediately when documenting another version

## C015 — Creality Print 7.0.0 Release Notes

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/releases/tag/v7.0.0
- Source type: Official release notes
- Published/revised: 2025-12-29T03:21:20Z
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.0.0 feature introduction
- Supports: AI Smart Analysis support detection/recommendation and AI Cloud Service dependency
- Limitations/conflicts: Does not establish 7.2.1 visual location or physical reliability
- Confidence: High
- Review by: 2026-09-20

## C016 — Creality Print 7.2.0 Release Notes

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/releases/tag/v7.2.0
- Source type: Official release notes
- Published/revised: 2026-06-30T09:03:32Z
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.0 features retained where confirmed in 7.2.1
- Supports: AI/Professional editions; upper-right Prepare switch; guided import; CFS mapping; print-risk analysis; pre-print camera inspection; color mixing
- Limitations/conflicts: AI features are beta/service-dependent; release notes do not prove all 7.2.1 paths or results
- Confidence: High
- Review by: 2026-09-20

## C017 — DeviceList.pot at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/localization/i18n/DeviceList.pot
- Source type: Official tagged English localization template
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 Device and CFS pages
- Supports: Device list/details, printing information, control, file/history, timelapse, camera, speed, CFS, humidity, feed/retract, and automatic-refill labels
- Limitations/conflicts: Strings do not prove exact layout, units/defaults, or availability on a particular model/firmware
- Confidence: High for labels; medium for navigation
- Review by: 2026-09-20, or immediately when documenting another version

## C018 — Creality Print Interface Layout Introduction

- Publisher: Creality Wiki
- URL: https://wiki.creality.com/en/software/update-released/Basic-introduction/Interface-introduction
- Source type: Official Wiki documentation
- Published/revised: Created and revised 2024-06-01
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Older or unspecified Creality Print interface
- Supports: Prepare/Preview/Device workflow; Prepare toolbar functions; printer, filament, object, and process areas
- Limitations/conflicts: Predates 7.x AI edition and cannot confirm 7.2.1 pixel placement, labels, or visibility
- Confidence: Medium-high, version-limited
- Review by: 2026-09-20

## C019 — Calibration Tutorial

- Publisher: Creality Wiki
- URL: https://wiki.creality.com/en/software/6-0/calibration-tutorial
- Source type: Official Wiki documentation
- Published/revised: Created and revised 2025-10-28
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 6.x calibration concepts
- Supports: Temperature, two-pass flow, pressure advance, maximum volume flow, VFA, and Preview-oriented calibration concepts
- Limitations/conflicts: VFA is alpha-gated in stable tagged 7.2.1 source; does not prove current menu availability or physical-printer applicability
- Confidence: Medium-high, version-limited
- Review by: 2026-09-20

## C020 — Lite Mode

- Publisher: Creality Wiki
- URL: https://wiki.creality.com/en/software/6-0/lite-mode
- Source type: Official Wiki documentation
- Published/revised: Created 2025-06-19; revised 2025-07-18
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 6.2 Lite Mode introduction
- Supports: Preview-only filtering, hidden internal sparse/solid infill rendering, no G-code change, and need to disable/re-slice for full inspection
- Limitations/conflicts: Current 7.2.1 placement comes from tagged source, not this older screenshot
- Confidence: High for 6.2 behavior; version-limited for layout
- Review by: 2026-09-20

## C021 — 6.2 Preset Function Description

- Publisher: Creality Wiki
- URL: https://wiki.creality.com/en/software/6-0/Preset-Description
- Source type: Official Wiki documentation
- Published/revised: Created 2025-07-04; revised 2025-07-07
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 6.2 preset management
- Supports: System/project/user preset classes; printer and filament add/edit/save paths; role-dependent presentation
- Limitations/conflicts: Uses `Expert` where 7.2.1 source uses `Professional`; exact current paths require visual confirmation
- Confidence: Medium-high, version-limited
- Review by: 2026-09-20

## C022 — Guide to Using CFS on the Creality Print

- Publisher: Creality Wiki
- URL: https://wiki.creality.com/en/software/update-released/Basic-introduction/CFS-tutorial
- Source type: Official Wiki documentation
- Published/revised: Created 2024-08-26; revised 2025-04-29
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: CFS controls documented for Creality Print in 2025
- Supports: Device Details location; RFID/manual filament data; Feed/Retract; filament-box settings; refill; humidity; multiple CFS units; Auto Mapping
- Limitations/conflicts: Does not identify compatible printer/firmware combinations or confirm 7.2.1 pixel layout; live actions were not executed
- Confidence: Medium-high, dependency-limited
- Review by: 2026-09-20

## C023 — Installed Creality Print 7.2.1.5476 bundle and resources

- Publisher: Creality; locally observed signed application bundle
- URL: N/A — local artifacts under `/Applications/Creality Print.app/Contents/`, including `Info.plist`, `Resources/printers/version.txt`, `Resources/profiles/Creality.json`, `Resources/profiles/Creality/`, and `Resources/images/process/ProcessConfig.json`
- Source type: Read-only local artifact observation
- Published/revised: Bundle signed 2026-08-04; local modification timestamp 2026-08-04T16:22:28+02:00
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Installed macOS arm64 build `7.2.1.5476`
- Supports: Version, identifier, architecture, valid Creality signature, catalog identifiers, K2-family profile counts, absence of `K2C`, raw K2 0.4 fields, process subgroup labels, Finder document associations
- Limitations/conflicts: Application was not launched; bundle profiles are not hardware identity, compatibility, safety, or official physical-limit evidence
- Confidence: High for local bundle facts
- Review by: 2026-09-20, or immediately after the installed application changes

## C024 — GUI_App.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/GUI_App.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 file-dialog filters
- Supports: STEP `.stp`/`.step`, STL, OBJ, 3MF, AMF, G-code, CAD/model wildcard definitions
- Limitations/conflicts: A listed filter does not guarantee every individual file parses or is printable; macOS Finder associations differ
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version

## C025 — CreatePresetsDialog.cpp at v7.2.1

- Publisher: CrealityOfficial on GitHub
- URL: https://github.com/CrealityOfficial/CrealityPrint/blob/v7.2.1/src/slic3r/GUI/CreatePresetsDialog.cpp
- Source type: Official tagged source file
- Published/revised: `v7.2.1`, released 2026-08-04
- Accessed: 2026-08-20T18:52:48+02:00
- Applies to: Creality Print 7.2.1 printer and filament preset dialogs
- Supports: Current dialog labels `Select/Remove Printer` and `Edit Filament`
- Limitations/conflicts: Does not prove the exact click target, selected preset, field defaults, or screen position
- Confidence: High
- Review by: 2026-09-20, or immediately when documenting another version
