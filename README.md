# k2-3d-printing

`k2-3d-printing` is an agent-independent skill for evidence-bounded FDM work with Creality K2-family printers and Creality Print. It covers printer identity, filament and hardware compatibility, STL/STEP/3MF inspection, design for FDM, orientation, supports, slicing trade-offs, calibration, Preview review, failure diagnosis, preventive maintenance, and safe repair boundaries.

The repository contains one self-contained skill under `skills/k2-3d-printing/`. This standard nested layout keeps `SKILL.md`, references, scripts, and interface metadata together as one skills CLI payload. The operational contract does not depend on Codex, another skill, a paid service, or a printer connection.

## Installation

Install it from GitHub with the [skills CLI](https://www.skills.sh/docs/cli):

```bash
npx skills add woliveiras/k2-3d-printing-skill
```

Review `SKILL.md`, scripts, and the source policy before installing any third-party skill. Follow the current CLI documentation to configure telemetry.

## What the skill enforces

- Confirm the physical printer before model-specific advice; a slicer profile alone is insufficient.
- Refresh unstable claims from primary sources and date every source observation.
- Separate official limits, manufacturer ranges, recommended starting points, empirical adjustments, and unvalidated results.
- Inspect Preview instead of treating successful slicing as proof of printability.
- Preserve original 3MF projects and require explicit authorization for copies or edits.
- Require separate authorization for software/firmware updates, printer control, print submission, purchases, dependency installation, publication, and external-model evaluation.
- Stop repairs when model-specific parts, torque, wiring, heaters, sensors, or official procedures are not confirmed.

## Repository map

```text
skills/k2-3d-printing/
├── SKILL.md                       Core workflow and routing
├── agents/openai.yaml             Optional UI metadata
├── references/                    Indexed evidence and operating guidance
└── scripts/                       Read-only inspection and comparison tools
tests/                             Deterministic fixtures, unit tests, and response oracle
```

## Local scripts

The optional scripts require Python 3.10 or newer and use only the standard library. They write structured JSON to stdout and do not extract archives, modify inputs, send prints, or contact a printer.

```bash
python3 skills/k2-3d-printing/scripts/inspect_3mf.py project.3mf
python3 skills/k2-3d-printing/scripts/extract_creality_settings.py project.3mf
python3 skills/k2-3d-printing/scripts/compare_profiles.py baseline.json candidate.3mf
python3 skills/k2-3d-printing/scripts/check_source_freshness.py skills/k2-3d-printing/references/sources.md
```

Network link checks are opt-in and must be explicitly authorized:

```bash
python3 skills/k2-3d-printing/scripts/check_source_freshness.py skills/k2-3d-printing/references/sources.md --check-links
```

The tools report file evidence only. They do not prove hardware identity, compatibility, support removability, collision freedom, strength, safety, or physical printability.

## Development validation

```bash
python3 -m compileall -q skills/k2-3d-printing/scripts tests
python3 -m unittest discover -s tests -v
python3 -m json.tool tests/evals/cases.json >/dev/null
python3 /path/to/skill-creator/scripts/quick_validate.py skills/k2-3d-printing
git diff --check
```

The 14-case deterministic response oracle is deliberately limited: it verifies explicit guardrails and rejects known unsafe or unauthorized response patterns, but it cannot establish factual accuracy or replace real printer/material tests. No provider or external-model evaluation runs by default.

## Evidence baseline

The reference library is dated 2026-08-20. Its Creality Print baseline combines official `v7.2.1` source with a read-only `7.2.1.5476` macOS bundle snapshot; neither establishes a future user's installed version or runtime state. The evidence identifies K2, K2 Pro, K2 Plus, K2 SE, and K2 SE 4C, but no distinct physical model named `K2C`. Recheck [printer identity](skills/k2-3d-printing/references/printer-identity.md) and the [source register](skills/k2-3d-printing/references/sources.md) before version- or model-specific guidance.

## Contributing

Keep `skills/k2-3d-printing/SKILL.md` concise and imperative. Put detailed knowledge in the existing indexed reference domain, avoid duplicated facts, preserve source IDs, set a review date, and explain conflicts. Add deterministic tests for new parsing or authority behavior. Do not weaken an oracle to make an unsafe fixture pass.

See `CHANGELOG.md` for repository changes.
