# Orientation and supports

## Choose orientation

Score each candidate orientation against:

1. primary load relative to layer planes;
2. visible/fit-critical surfaces and seam placement;
3. bed contact area, center of mass, height, and moving-mass stability;
4. overhang/bridge amount and support access;
5. holes, pins, threads, snap features, and dimensional distortion;
6. purge tower/brim clearance and sequential-print collision envelopes;
7. time, material, and split/join work.

Reject an auto-orientation result that fails a critical criterion. Auto-orient is a candidate generator, not a printability proof.

## Decide whether support is required

- Inspect actual layer islands and bridge spans after slicing; do not decide from a single geometric angle alone.
- Prefer self-supporting chamfers, teardrop/diamond holes, bridges, rotated geometry, sacrificial membranes, split parts, or user-designed removable supports.
- Protect the show/fit surface from support contact. Ensure every support and interface has a removal path.
- Consider material compatibility and interface adhesion before using a second support material; soluble does not mean harmless, dry, CFS-compatible, or easy to dispose of.

## Normal versus tree/organic

| Choose | When it helps | Main risk |
|---|---|---|
| Normal/grid/snug | broad, planar, mechanically stable underside; predictable interface | more contact/material; trapped columns; scars |
| Tree/organic | isolated curved overhangs and reduced model contact | branch instability, collision, unexpected contact, longer generation |
| Painted/manual | preserve specific faces and force/forbid local support | missed islands or excessive hand-painted regions |
| Designed support | repeatable access, sacrificial tabs/membranes, production control | requires CAD revision and tolerance test |

## Contact and interface starting points

Use the official profile first. For same-material support, one layer-height Z gap and roughly one line-width XY gap are initial calibration hypotheses, not universal values. Start with 2 interface layers and a nonzero interface spacing unless the official profile/material pairing specifies otherwise. Then:

- Increase Z gap for easier release or reduce it for better underside only after a coupon.
- Increase XY gap when side scarring/fusion occurs; reduce it when overhang edges collapse.
- Add interface layers/density for a flatter underside; expect harder removal and more time/material.
- Use near-zero contact only for an officially compatible dissimilar/soluble interface and a validated dry-material workflow.
- Recheck actual generated gap in Preview; layer rounding can differ from the requested value.

## Bridges and overhangs

- Orient bridges along the shortest supported span and give them anchored ends.
- Start bridge speed below ordinary external-wall speed and tune fan/flow/temperature with the exact material.
- Use gradual chamfers or curved/self-supporting transitions instead of sharp shelves where function permits.
- Treat any threshold angle as a slicer selection rule, not a universal physical limit; material, line width, layer height, cooling, speed, and geometry change it.

## Adhesion structures

- Use a brim for a narrow footprint, tall part, or broad material shrinkage risk; keep it away from precision edges when removal damage matters.
- Use mouse ears at lifting corners to reduce cleanup/material compared with a full brim.
- Use raft only after plate preparation, first-layer calibration, orientation, brim/ears, and material environment fail or when the process specifically requires a sacrificial base.
- Remove the cooled part according to the exact plate guidance; do not pry against heaters, sensors, or a hot surface.

## Preview acceptance

Trace the first supported path of every object and support branch; examine interface reachability, support touching show faces, bridge anchors, Z/XY separation, brim/raft connection, travel through tall objects, purge structures, sequential collision envelopes, and the layer where each isolated region begins. If any view cannot be verified, classify the job as `test print recommended`.
