# Changelog

All notable changes to this repository are documented here.

## Unreleased

### Added

- Initialized the `k2-3d-printing` skill with the official skill-creator scaffold and generated `agents/openai.yaml`.
- Added read-only, standard-library tools for 3MF inspection, Creality/Orca-style setting extraction, typed profile comparison, and source freshness audits.
- Added deterministic 3MF/profile fixtures and a 14-scenario response oracle covering hardware identity, materials, Creality Print uncertainty, safety, authority, Preview, and repair boundaries.
- Added the evidence, material, slicing, Creality Print, maintenance, safety, and FDM design reference library.
- Packaged the complete installable payload under `skills/k2-3d-printing/` so the pinned skills CLI behavior retains references, scripts, and interface metadata.

### Changed

- Removed authoring-session and pre-release context from runtime references.
- Centralized duplicated material, design, Creality Print, Preview, calibration, support, safety, firmware, and CFS guidance behind indexed references.
