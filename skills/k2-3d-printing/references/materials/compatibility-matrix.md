# Material compatibility matrix

This matrix compares material requirements with the documented base K2. Apply its base-K2 classifications only after the rating label or `About` screen confirms K2. If `K2C` is the only identity supplied, keep the printer-specific status unconfirmed.

## Status codes

| Code | Meaning |
|---|---|
| OS | Officially supported for the exact named subsystem/family |
| C | Conditional on the stated exact product, nozzle, hotend, bed, surface, chamber, dryness, or path |
| NV | Not validated by an applicable exact source |
| NR | Not recommended by a primary source or because the complete requirement cannot be reproduced reliably |
| I | Incompatible because a minimum confirmed requirement exceeds the confirmed subsystem |

Base-K2 reference facts: 300 °C maximum nozzle, 100 °C maximum bed, all-metal hotend, steel-tipped trimetal 0.4 mm nozzle; named materials PLA, ABS, PETG, PLA-CF, and PET. [M001]

## Base K2 and standard CFS

| Material or exact grade | Base-K2 process status | Nozzle/hotend gate | Bed/chamber/surface gate | Standard CFS | Why |
|---|---|---|---|---|---|
| Plain PLA | OS at family level | exact SKU/profile | exact plate/product | OS example | Named by K2 and CFS; product calibration still required. [M001, P024] |
| Hyper PLA | C under PLA family | flow-capable nozzle/hotend; 600 mm/s is not a default | 25–60 °C product range | OS as PLA family; exact spool still checked | Exact SKU range 190–230 °C; maximum speed requires flow test. [M008] |
| PLA+, Tough/Pro, Matte, Silk | C under PLA family | exact formulation | exact product range/finish test | C; generic PLA path only | Names are not standardized; exact grade is not separately endorsed. [M007, M009, M010] |
| Foamed wood-look PLA without particles | C under PLA family | exact foaming profile | exact product | NV for exact grade | PolyWood v2 has no wood powder; CFS evidence is generic PLA only. [M011] |
| Real wood/metal-filled PLA | NV | product-specific; large particles may require at least 0.6 mm; metal requires hardened nozzle in cited guide | exact product/surface | NV | Filler changes clogging, wear, brittleness, and feed behavior. [M012] |
| Plain PETG | OS at family level | exact SKU/flow | exact plate; release-layer decision | OS example | Named by K2 and CFS; product ranges conflict and must not be merged. [M001, P024, M013, M014, M015] |
| Plain PET | OS at family level | exact PET TDS absent | exact PET TDS absent | OS example | Family is listed, but no exact unfilled-PET profile was established. [M001, P024] |
| ABS | OS at family level | exact formulation/flow | exact enclosure and bed condition | OS example | Named by K2/CFS; Hyper ABS no-enclosure claim cannot generalize. [M001, P024, M007, M016] |
| ASA | NV | exact grade | enclosure/bed required by exact grade | OS feed-path example | CFS acceptance does not prove printer process. Creality HP-ASA sources conflict. [P024, M007, M017] |
| Ultrafuse HIPS v2.2 | NR pending exact validation | 240–260 °C; 0.4 mm or larger | published bed 100–120 °C; base K2 reaches only lower boundary | OS feed-path example | Not on K2 list and complete bed range cannot be reproduced. [M020, M001, P024] |
| TPU/TPE | NV for printer | direct constrained path; exact Shore grade | exact product | NR / disallowed | Standard CFS explicitly disallows elastic filament; the base-K2 list omits TPU. [M001, P024, M003] |
| Unfilled PA6/PA12/other nylon | NV | exact TDS absent | moisture/chamber/surface unresolved | NV | Do not infer from filled PA or CoPA. |
| Polymaker CoPA | NV | all-metal; 250–270 °C | bed 25–50 °C; enclosure source conflict | NV | Exact range fits thermally, but no K2 endorsement and enclosure evidence conflicts. [M024] |
| Hyper PC | NV | 240–260 °C | bed 50–80 °C; chamber status not established | NV | Product page fits base-K2 temperatures but K2 compatibility is not stated. [M028] |
| PolyMax PC | NR pending exact chamber evidence | 250–270 °C | bed 90–105 °C; controlled chamber 70–100 °C | NV | Base-K2 bed misses the upper range and applicable chamber capability is unconfirmed. [M029] |
| PVA | NV for printer | exact 1.75 mm product/profile | moisture/dry feed; support pair | C only when dried/not softened | CFS accepts dry PVA; UltiMaker TDS is 2.85 mm ecosystem and not a Creality profile. [P024, M032] |
| BVOH | NV for printer | exact product 190–210 °C example | exact support pair; dry feed | C only when dried/not softened | CFS accepts dry BVOH; exact Ultrafuse conditions still govern. [P024, M033] |
| Unfilled PP | NV | exact product 220–240 °C example | exact PP tape/adhesive, 60–80 °C | NV | Not named by base K2 or standard CFS. [M034] |
| PP-GF30 | NV | 0.6 mm or larger; abrasion-aware tooling | two surface-specific bed ranges | NV | Exact surface system and filled-tooling condition required. [M035] |
| PLA-CF | OS at family level | exact grade/nozzle confirmation; the base-K2 supplied nozzle does not prove every grade | exact grade | OS example | Named by K2 and standard CFS. [M001, P024, M036] |
| Hyper PETG-CF | NV | hardened/wear-resistant nozzle; 240–260 °C | 70–90 °C | NV | Temperature fit is inference; not named on K2 list/CFS exact matrix. [M037] |
| Fiberon PET-CF17 | NV | hardened/all-metal; 270–300 °C | 70–80 °C; manufacturer says no heated enclosure | NR for CFS-C; standard CFS NV | Exact composite not K2-listed; CFS-C says Not Suggested. [M039, M004] |
| Fiberon PET-GF15 | NR | hardened; 280–310 °C | 70–80 °C | NV | Published range extends above the base-K2 nozzle maximum. Never command 310 °C. [M040] |
| Fiberon PA6-CF20 / PA12-CF10 / PA6-GF25 | NV | hardened/all-metal; 280–300 °C; dry feed | product-specific 40–50 °C bed and conditioning | C only after exact standard-CFS evidence; CFS-C lists generic PA6-CF/PA12-CF | Standard CFS marketing broadly names PA-CF but wiki warns brittle grades; exact SKU required. [M025, M026, M038, P024, M003, M004] |
| Creality PPA-CF | NR | 280–300 °C; exact nozzle/fill | bed 90–105 °C; enclosure; upper bed exceeds base K2 | NR: standard CFS brittleness warning; CFS-C Not Suggested | Not K2-listed; reaches thermal limits and has feed-path warning. [M041, P024, M004] |
| Ultrafuse PAHT-CF15 | NV | 250–270 °C; 0.6 mm or larger ruby/hardened | bed 65–85 °C; no chamber temperature stated | CFS-C Not Suggested; standard CFS NV | M042 records a conflict with a superseded v3.4 TDS; no official K2 support or confirmed drying rule. [M042, M004] |
| Fiberon PPS-CF10 | I | minimum nozzle 310 °C exceeds 300 °C | 80–90 °C bed; 25–80 °C ambient | NR: standard CFS brittle warning; CFS-C Not Suggested | Thermal incompatibility plus feed-path warning. [M043, P024, M004] |
| Ultrafuse PPSU | I | minimum nozzle 390 °C | bed 200–220 °C; chamber 170–210 °C | NV | All core thermal requirements exceed base K2. [M044] |
| PEI/ULTEM | I | minimum nozzle 370 °C | bed 150–155 °C; specialized equipment | NV | Thermal requirements exceed base K2. [M045] |

## Standard CFS facts

- Spool diameter: 197–202 mm. [P022]
- Spool width: 42–68 mm. [P022]
- Supported medium-hardness examples: PLA, PETG, ABS, PLA-CF, PET, ASA, HIPS, dried PVA, and BVOH. [P024]
- Disallowed/unsuitable examples: TPU and other elastic filament; PVA/BVOH softened by moisture; hard/brittle PPA-CF and PPS-CF that can break in the feed tube. [P024]
- The CFS product page broadly lists PA-CF. Resolve that marketing claim with the more specific wiki warning and exact SKU behavior. [M003]

## CFS-C matrix boundary

The official CFS-C table recorded by M004:

- marks named Hyper PLA, ABS, PLA-CF, PETG and several CR PLA/Silk/Matte products usable;
- marks TPU unavailable;
- marks PPA-CF, PAHT-CF, PET-CF, and PPS-CF **Not Suggested**;
- marks generic PA6-CF, PA12-CF, PA612-CF, PVA, and BVOH usable. [M004]

Do not apply those statuses to standard CFS or to an exact SKU not named by the matrix.

## Compatibility decision procedure

1. Obtain physical label/About evidence. If absent, report **hardware identity unconfirmed** and stop hardware-specific classification.
2. Record printer hotend/nozzle/bed/chamber/plate evidence and firmware/profile only as separate configuration evidence.
3. Identify exact filament, TDS/SDS revision, diameter, filler, hardness, and spool dimensions.
4. Check minimum requirements before maximums. Reject any minimum above a confirmed limit.
5. Require named nozzle/hotend/surface/chamber/dry-feed conditions.
6. Check standard CFS or CFS-C separately; reject elastic, wet-softened, or brittle filament where its applicable source warns.
7. Choose a calibration point inside the exact intersection; label it **Starting point**.
8. Inspect sliced temperatures, fan, flow, feature speeds, support/purge, and material mapping in Preview.
9. Report the final state and residual uncertainty. Only a measured physical test earns **Physically validated**.

## Stop conditions

Stop and ask for one objective missing fact when:

- the physical model is still inferred from a slicer profile;
- nozzle material/diameter or hotend limit is unknown for an abrasive/high-temperature material;
- the exact product cannot be distinguished from a generic family;
- first-party sources conflict in a way that can exceed a hardware limit;
- CFS model or filament brittleness/moisture state is unknown;
- a support pair lacks overlapping conditions;
- a proposed value exceeds an official printer or product limit;
- success would require firmware, sensor, heater, electrical, or chamber modification.
