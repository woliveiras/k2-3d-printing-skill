# K2 3D Printing

`k2-3d-printing` is an installable Agent Skill for Creality K2-family printers, Creality Print, and FDM printing.

It helps an AI agent:

- choose filaments that match the printer, nozzle, build plate, enclosure, and CFS;
- inspect STL, STEP, 3MF, and G-code files;
- orient models and balance finish, speed, strength, material use, and support removal;
- navigate Creality Print, tune slicing settings, and review Preview;
- calibrate filaments, diagnose failed prints, and approach maintenance or repairs with verified procedures.

The skill checks evidence before giving model-specific advice. It separates official limits from manufacturer ranges, starting points, empirical adjustments, and untested suggestions. A completed slice is never presented as proof that a print will succeed.

## Install

Use the [skills CLI](https://www.skills.sh/docs/cli):

```bash
npx skills add woliveiras/k2-3d-printing-skill
```

The skill is self-contained: no other skill, paid service, or printer connection is required. Optional read-only tools require Python 3.10 or newer. They inspect files without modifying them or sending a print.

It does not edit projects, update software or firmware, control a printer, send a print, or buy parts without separate approval.

## Why it confirms the printer model

The K2 family contains different machines with different hardware limits. `K2C` is treated as an unverified label, not proof of a specific Creality model. The skill asks for the physical label or the printer's `About` screen before giving hardware-specific guidance; a slicer profile alone is not enough.

## Explore

- [Skill instructions](skills/k2-3d-printing/SKILL.md)
- [Reference library](skills/k2-3d-printing/references/INDEX.md)
- [Source register](skills/k2-3d-printing/references/sources.md)
- [Changelog](CHANGELOG.md)
