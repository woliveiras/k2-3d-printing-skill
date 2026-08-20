# Support settings

## Locate support controls

| Purpose | Path | Scope | Visibility dependencies | Status |
|---|---|---|---|---|
| Global automatic support settings | `Prepare` → `Process` → `Global` → `Support` | Whole active process/project | Normal print tab | Current 7.2.1 source-confirmed [C006] [C007] [C008] |
| Per-object support settings | `Prepare` → `Process` → `Objects` → select object → `Support` | Selected normal object context | The object-level tab must contain Support | Current source-confirmed; exact screen not observed [C008] [C009] |
| Manual support painting | `Prepare` toolbar → support-painting control | Selected model surface | Model selection and tool context | Official 2024 interface documentation; 7.2.1 icon/path visually unconfirmed [C018] |
| AI support analysis | AI workflow after model/slice analysis | AI Edition and AI Cloud Service | Service, login/network, supported model state | Introduced in 7.0; not a physical validation [C015] [C016] |

The installed 7.2.1 resource groups under `Support` are `Support`, `Raft`, `Support filament`, `Advanced`, and `Tree supports`. Individual field labels, units, defaults, and enabled states were not observed. [C023]

## Why Support can disappear

Current source intentionally hides the Support category for:

- a per-object **part** parameter tab;
- a per-object **layer-range** parameter tab. [C008]

When the user cannot find it:

1. Confirm Creality Print version.
2. Confirm `Pro` versus `AI` edition.
3. Confirm `Basic` versus `Professional` user role.
4. Confirm `Global` versus `Objects`.
5. In Objects, select the top-level object rather than a part or layer range.
6. Check scrolling and search/filter state.
7. If still absent, mark it `not confirmed for this version/context` and request a screenshot only if required.

Do not invent an alternate menu.

## Global, object, and painted intent

- Use `Global` for the baseline support-generation policy.
- Use `Objects` for a documented override on one selected object.
- Treat painting as geometry-local intent, not proof that generated support is continuous or removable.
- Record blockers, enforcers, painted regions, and object overrides separately.
- Re-slice after every change and confirm the active object selection before comparing results.

The exact precedence among every 7.2.1 support field, modifier, and painted region was not inspected. If two controls conflict, preserve both observations and validate the generated toolpath rather than asserting precedence from memory.

## AI boundary

Creality 7.0 release notes say AI Smart Analysis can detect whether support may be required and recommend Normal or Tree when AI Cloud Service is enabled. Creality 7.2.0 notes add post-slice risk checks for unsupported overhangs, missing supports, and collapse-prone areas and may offer automatic repair/support generation. These are vendor feature claims, not guarantees. [C015] [C016]

Review any AI-applied change exactly like a manual change. Confirm what settings and painted regions changed, re-slice, and inspect every affected layer.

## Preview acceptance

Before calling support configuration reviewed:

- disable Preview Lite Mode and re-slice when internal support paths might be hidden;
- inspect every island and the first layer of each supported region;
- distinguish model, support, interface, brim/raft, and prime/purge structures through the active legend;
- inspect contact on visible faces, trapped cavities, removal access, branch continuity, and build-plate anchoring;
- inspect bridges and overhangs rather than assuming support is necessary or sufficient;
- verify support-material and CFS mapping for multi-material jobs;
- record any unobserved interface gap, XY clearance, or tree-support parameter as unconfirmed.

Slicing success or AI risk clearance does not establish removable support, acceptable surface finish, or physical print success.
