# Portable printer memory

Use printer memory to avoid repeating confirmed facts, never to replace current physical evidence. The JSON file belongs to the user and is separate from the skill installation, project repository, Git, and agent-native memory.

## Storage

`scripts/printer_memory.py` resolves the default file without administrator access:

| System | Default file |
|---|---|
| Windows | `%APPDATA%\k2-3d-printing\printer-memory.json` |
| macOS | `~/Library/Application Support/k2-3d-printing/printer-memory.json` |
| Linux and other Unix | `${XDG_CONFIG_HOME:-~/.config}/k2-3d-printing/printer-memory.json` |

Set `K2_3D_PRINTING_DATA_DIR` only when the user explicitly chooses another local or synchronized directory. Agents in remote or isolated filesystems cannot share local memory unless the user makes the file available there.

The manager stores schema version, revision, printer aliases, physical identity, current setup, software versions, preferences, evidence kind, and confirmation date. It rejects unknown fields so serial numbers, credentials, private network details, and conversation transcripts are not accepted. It stores current state, not an unbounded component history; an atomic write keeps one `.bak` recovery copy after the first update.

## Read workflow

Resolve and inspect memory without creating it:

```bash
python3 scripts/printer_memory.py path
python3 scripts/printer_memory.py list
python3 scripts/printer_memory.py show oficina
python3 scripts/printer_memory.py validate
```

When multiple printers exist and the request is ambiguous, ask only which alias applies. Reuse relevant stored fields after selection. Do not expose unrelated printers or fields in the response.

Apply this precedence:

1. recent physical observation;
2. recent explicit user confirmation;
3. stored memory with its evidence and date;
4. tied purchase evidence;
5. observed firmware identity;
6. slicer or project configuration;
7. inference.

A slicer/profile conflict may trigger a question but cannot overwrite physical identity or installed hardware. Reconfirm a stored field when a newer observation conflicts, the requested action is repair or purchase sensitive, or task-specific freshness changes the decision.

## Add or update a printer

Use a lowercase alias containing letters, digits, or hyphens. Create a write-free proposal only after physical identity has qualifying evidence:

```bash
python3 scripts/printer_memory.py propose-upsert oficina \
  --physical-model K2 \
  --identity-evidence physical_label \
  --confirmed-at 2026-08-21 \
  --nozzle-diameter-mm 0.4 \
  --nozzle-material hardened_steel \
  --plate-type flexible_pei
```

Accepted physical-identity evidence kinds are `physical_label`, `about_screen`, `purchase_document`, `firmware_identity`, and `user_supplied_photo`. A profile is configuration evidence, never physical-identity proof.

If an existing alias is corrected to a different physical model while it has setup or software state, the proposal stops. Re-run `propose-upsert` with `--reset-dependent-state` only after explaining that the stored nozzle, plate, feed path, and software state will be removed from the candidate. The approved diff must make that reset visible.

For a component change, first ask whether it is temporary or permanent. Keep a temporary change in conversation state only. For a permanent change, wait until the user confirms the physical work completed, then create a proposal:

```bash
python3 scripts/printer_memory.py propose-set oficina \
  current_setup.nozzle.diameter_mm \
  --value-json 0.6 \
  --evidence-kind user_confirmed_after_installation \
  --confirmed-at 2026-08-22
```

Evidence on `nozzle`, `plate`, and `feed_path` applies to the whole stored component. Before changing one retained nozzle field, confirm that the other stored nozzle fields still describe the installed assembly. If diameter and material both change, use one `propose-upsert` with both values and `--configuration-evidence user_confirmed_after_installation` so no mixed intermediate state is persisted.

Show the proposal's target file, base revision, exact diff, evidence, and claim boundary. Ask separately whether to save it. Do not represent installation intent as installed state.

Only after explicit approval, preserve the exact proposal JSON in a task-owned file and run:

```bash
python3 scripts/printer_memory.py apply /path/to/proposal.json --user-approved
```

`apply` rejects an altered token, another target file, an unsupported schema, a stale revision/hash, a candidate that contains changes outside its diff, a concurrent lock, a symlink target, or missing approval. The token detects accidental proposal changes; it is not authentication. `--user-approved` records the caller's assertion and cannot prove that approval occurred; never pass it before the user approves the displayed target and diff. The manager reconstructs the candidate from the single approved diff before writing through a same-directory temporary file and atomic replacement. Keep the full candidate in the task-owned proposal file and expose only the relevant diff, not unrelated printer records. Do not remove an unfamiliar lock automatically; report the path and likely concurrent operation.

The manager does not control a printer or verify that a stored change physically occurred. Report memory update separately from hardware installation, slicing, Preview review, test printing, and physical validation.
