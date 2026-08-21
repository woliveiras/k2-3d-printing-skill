<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/k2-3d-printing-logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/k2-3d-printing-logo-light.svg">
    <img src="assets/k2-3d-printing-logo-light.svg" alt="K2 3D Printing logo" width="220">
  </picture>
</p>

# K2 3D Printing

`k2-3d-printing` is an installable Agent Skill for Creality K2-family printers, Creality Print, and FDM printing.

It helps an AI agent:

- choose filaments that match the printer, nozzle, build plate, enclosure, and CFS;
- inspect STL, STEP, 3MF, and G-code files;
- orient models and balance finish, speed, strength, material use, and support removal;
- navigate Creality Print, tune slicing settings, and review Preview;
- calibrate filaments, diagnose failed prints, and approach maintenance or repairs with verified procedures.

Before recommending a setting, the skill checks the exact printer and the available sources. It tells you which values come from official documentation, which are manufacturer ranges, and which still need testing. A successful slice is not treated as proof that the print will succeed.

## Install

Use the [skills CLI](https://www.skills.sh/docs/cli):

```bash
npx skills add woliveiras/k2-3d-printing-skill
```

The skill is self-contained: no other skill, paid service, or printer connection is required. Optional read-only tools require Python 3.10 or newer. They inspect files without modifying them or sending a print.

It does not edit projects, update software or firmware, control a printer, send a print, or buy parts without separate approval.

## Update

Installed skills are not updated automatically. Fetch the latest available version with:

```bash
npx skills update k2-3d-printing
```

Use `-g` to update a global installation or `-p` to update a project installation.

## Why it asks which K2 you own

The K2 family contains different machines with different hardware limits. If all you have is the name `K2C`, the skill will ask you to check the printer's physical label or `About` screen. It will not guess the hardware from a slicer profile.

## Explore

- [Skill instructions](skills/k2-3d-printing/SKILL.md)
- [Reference library](skills/k2-3d-printing/references/INDEX.md)
- [Source register](skills/k2-3d-printing/references/sources.md)
- [Changelog](CHANGELOG.md)

## License

[MIT](LICENSE) © 2026 William Oliveira.
