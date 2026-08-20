# Support materials

Use this file for PVA, BVOH, and HIPS support decisions. Chemical solubility does not establish adhesion to the primary polymer, temperature overlap, CFS feedability, purge purity, interface quality, complete removal, or physical printer support.

## Decision boundary

- The candidate K2 official material list does not name PVA, BVOH, or HIPS. Treat print-process compatibility as **Not validated** until the physical printer and exact material are confirmed. [M001]
- Standard CFS officially lists dried PVA and BVOH, but rejects them when moisture has softened them. It also lists HIPS as a medium-hardness example. [M002]
- CFS feed-path status does not validate the support/primary pair or an independent-tool workflow.
- Do not promise “zero marks,” complete dissolution, a fixed removal time, or support-free cavities.

## Source-specific material ranges

| Exact product | Nozzle | Bed | Cooling/speed | Drying/storage | Evidence boundary |
|---|---:|---:|---|---|---|
| Polymaker PolyDissolve S1 | 215–225 °C | 25–60 °C | fan on; product page/PIS 30–40 mm/s | very hygroscopic; 80 °C for 12 h | Product/PIS conflict with a separate Polymaker wiki page that lists 50–150 mm/s. Use exact revision. [M030, M031] |
| UltiMaker PVA v5.00 | use its exact 2.85 mm UltiMaker profile | exact UltiMaker ecosystem | exact profile | exact TDS/storage procedure | Pairing evidence only; not a 1.75 mm Creality profile. [M032] |
| BASF Ultrafuse BVOH v1.3 | 190–210 °C | 60–100 °C | 30–60 mm/s; 0.4 mm or larger | dry 60 °C for 4–16 h; sealed storage at 15–25 °C | First-party German document; exact product pairing only. [M033] |
| BASF Ultrafuse HIPS v2.2 | 240–260 °C | 100–120 °C | 40–80 mm/s; 0.4 mm or larger | dry 60 °C for 4–16 h | Candidate K2 bed reaches only the bottom point; no official K2 endorsement. [M020] |

Do not merge these ranges. The PolyDissolve speed conflict remains unresolved until the physical spool/document revision is identified.

## Published pairing evidence

| Support product | Primary-material evidence | Use boundary |
|---|---|---|
| PolyDissolve S1 | product matrix rates PLA, TPU, PVB, and nylon favorably; PETG only partially; ABS and PC poorly | Product-specific adhesion evidence; test other brands and purge conditions. [M030] |
| UltiMaker PVA | names PLA, PETG, and Nylon; says its PVA is unsuitable with its ABS, CPE+, PC, and PP | 2.85 mm UltiMaker ecosystem; do not derive Creality temperatures. [M032] |
| Ultrafuse BVOH | names PLA, PRO1, ABS, ABS Fusion+, PA, and PAHT-CF15 | Product-specific; confirm temperature overlap and removal. [M033] |
| Ultrafuse HIPS | Forward AM identifies HIPS as an ABS support option | Exact ABS/HIPS pair and removal process still require a coupon. [M020] |
| Any unlisted combination | no primary evidence in this research | **Unvalidated**; do not infer from “water soluble” or polymer family. |

## Multi-material gate

Before assigning a support material:

1. Confirm the physical printer and whether it can use independent materials/tools for the planned job.
2. Confirm standard CFS versus CFS-C, exact spool geometry, and dry/rigid feed condition.
3. Confirm both exact TDS/SDS documents and the overlap of nozzle, bed, chamber, and cooling requirements.
4. Confirm that purge temperature keeps both materials stable and that the printer/profile can avoid cross-contamination.
5. Print a small primary/support interface coupon with the final orientation and environment.
6. Verify attachment during printing, clean separation or dissolution, dimensional damage, residue, and accessible removal.
7. Reject the combination if support is trapped in a cavity, contaminates a structural/visible surface, or requires an unverified solvent/process.

## Interface settings

Treat these controls as a coupled system:

- top and bottom Z distance;
- XY separation;
- interface layer count and spacing;
- support pattern and density;
- support/primary temperatures and cooling;
- purge amount and contamination;
- normal versus tree geometry;
- support access and load during removal.

PolyDissolve S1 PIS v1.1 publishes Z gap 0 and XY distance 0.5 mm as its product/profile starting information. Preserve those as **Manufacturer starting points for that product**, not universal soluble-support defaults. [M031]

For an unvalidated pair:

- begin with a small stepped Z/XY/interface coupon;
- inspect every contact in Preview;
- use the minimum interface needed to support the surface without trapping material;
- preserve the visible or sealing face from support when orientation/splitting can do so;
- do not interpret Preview colors without the active legend.

## Temperature, speed, flow, cooling, and retraction

- Keep both materials inside exact ranges at every tool change, standby, purge, and active-extrusion state.
- Published speeds are global; first-layer, outer/interface, infill, bridge, and overhang values remain **Unvalidated**.
- Measure maximum volumetric flow separately for primary and support. The slower/drier feed may govern the job.
- Acceleration remains **Unvalidated** until feed and interface tests.
- Tune retraction after drying and temperature; hygroscopic soluble materials can imitate retraction/stringing problems.
- Preserve “fan on” only for PolyDissolve S1. Obtain exact cooling for BVOH/PVA/HIPS.

## Drying, storage, and CFS

- Soluble materials are moisture-sensitive. Use only the exact cycle, spool-safe temperature, and dryer method.
- Move dried filament directly to sealed/dry feed and minimize room exposure. Record time outside dry storage.
- Standard CFS accepts only PVA/BVOH that has not softened from moisture. Stop at buckling, flattening, grinding, or feed resistance. [M002]
- Do not assume CFS itself maintains the TDS-required dryness.
- HIPS dryness and CFS feedability remain separate from the solvent/removal plan.

## Dissolution and removal

For water-soluble support:

1. Confirm that water exposure is acceptable for the primary material, inserts, coatings, electronics, adhesives, and intended use.
2. Remove accessible bulk support mechanically only when it will not damage the surface.
3. Follow the exact support-material document for water temperature, agitation, duration, and disposal. If not sourced, mark the process **Unvalidated**.
4. Rinse/dry or condition the primary material under its own procedure.
5. Inspect cavities for trapped residue and measure fit/finish after the complete moisture cycle.

For HIPS or another non-water-soluble support, do not name a solvent, temperature, bath, or disposal method without the exact manufacturer procedure and SDS. Ventilation and fire/chemical controls are mandatory.

## Geometry and surface strategy

- Prefer orientation, chamfers, self-supporting geometry, model splitting, or removable sacrificial features before adding soluble support.
- Avoid support on sealing, ergonomic, optical, mating, or primary visible faces.
- Ensure every support volume has an exit/removal path. A soluble material can remain trapped or incompletely refreshed inside a narrow cavity.
- For a curved shell, test a representative supported curve. Interface sag, purge contamination, and stair stepping can matter more than nominal layer height.

## Health, maintenance, and disposal

- Use both exact SDS documents. Printing, purging, drying, and removal can create distinct exposures.
- Provide source ventilation for printing; do not treat water solubility as an emissions safety claim. [M056, M057, M059, M060]
- Follow local/SDS disposal rules for polymer-laden water and solvents; do not pour an uncharacterized solution into a drain.
- After use, purge only by an applicable procedure, inspect for degraded support residue and drive contamination, clean the plate by its maker's method, and reseal filament.

## Failure signatures

| Symptom | Separate these causes | Next test | Stop when |
|---|---|---|---|
| Support buckles or will not feed | moisture-softened filament, CFS/path, resistance, speed | unload without force; verify dryness and exact CFS status | fragment is inaccessible or dismantling lacks official procedure |
| Support detaches during print | material pairing, contamination, interface, purge, cooling | small interface coupon | temperature overlap cannot be maintained |
| Support fuses to part | pair incompatibility, Z/XY gap, purge, temperature | stepped interface coupon | critical/visible surface is damaged |
| Residue remains after dissolution | trapped geometry, contamination, insufficient documented process | inspect access and repeat only within exact procedure | removal medium harms primary part/inserts |
| Popping/rough support extrusion | moisture | exact drying/dry-feed comparison | dryer or spool limit unknown |
| Nozzle clogs after material change | degraded support, contamination, purge, temperature mismatch | stop; follow exact recovery procedure | hot-pull/disassembly condition is unconfirmed |
| Part dimensions change after water cycle | primary moisture uptake, residue, conditioning | measure before/after representative coupon | fit/structural requirement remains unmet |

## Release checklist

- Primary and support products, TDS/SDS revisions, printer/tool path, CFS variant, and spool condition confirmed.
- Temperature/cooling overlap and purge behavior verified without exceeding limits.
- Interface coupon demonstrates attachment, surface result, removal/dissolution, residue, and dimensional acceptance.
- Preview checked layer by layer for support access, interface, unsupported islands, purge, tool changes, and trapped material.
- Removal medium, ventilation, handling, and disposal are documented.
- Result remains a test recommendation until the exact final geometry is physically printed and inspected.
