# Evidence and authority

## Claim classes

| Label | Meaning | Required evidence |
|---|---|---|
| Observed | Directly visible in a supplied artifact, screenshot, physical label, `About` screen, installed application bundle, or command output | Record artifact, version/path, observation, and inspection date |
| Official | Stated by the manufacturer or governing authority for the exact model/version/material | Cite source ID, applicable subject, source date, and access date |
| Manufacturer range | Processing or safety range in the exact product TDS/SDS | Name vendor, product/grade, document revision, and limits |
| Starting point | A conservative first calibration value inside all confirmed limits | State dependencies and validation test; never relabel as official/default |
| Empirical adjustment | A measured change from a named printer/material/profile/test | Record test conditions and result; do not generalize |
| Inference | A conclusion from multiple observations | Show the observations and state what would falsify it |
| Unvalidated | Plausible but not physically tested or not supported by a specific source | Keep uncertainty explicit and avoid release language |

## Source order

1. Use the physical label and the unit's `About` screen for identity.
2. Use the exact official manual, Wiki/service page, firmware note, parts page, or Creality Print release/profile for product behavior.
3. Use the exact filament TDS and SDS for processing and hazards.
4. Use official occupational, electrical, and fire guidance for risk controls.
5. Use an original standards document or peer-reviewed study when manufacturer guidance is silent.
6. Use forums, videos, Reddit, blogs, and mirrored articles only to generate testable hypotheses.

## Conflict handling

1. Confirm that the sources discuss the same model, regional variant, hardware revision, firmware, Creality Print version, material product, nozzle, plate, and environment.
2. Prefer the primary source that is more specific and more recently revised.
3. Do not silently merge ranges or select the more convenient value.
4. Report both claims with their source IDs, explain the conflict, and state confidence.
5. Stop hardware-specific or safety-critical guidance if the conflict could exceed a limit or change a repair.

## Freshness

- Recheck software releases and firmware notes at each version-sensitive task.
- Recheck product/manual/parts pages before hardware compatibility or repair.
- Recheck TDS/SDS before giving product-specific temperatures, drying, storage, emissions, or solvent advice.
- Run `python3 scripts/check_source_freshness.py references/sources.md`; add `--check-links` only with network authorization.
- Avoid `latest`, `current`, `supported`, `compatible`, and `safe` without a live date and applicable source.

## Authority gates

| Action | Default | Required authorization and controls |
|---|---|---|
| Read files, inspect screenshots, compare profiles, research public sources | Allowed | Protect secrets, serials, private network details, and unrelated files |
| Read/validate printer memory or create a write-free proposal | Allowed | Use only relevant aliases/fields; keep evidence, date, conflict, and physical-proof limits explicit |
| Apply a printer-memory proposal | Denied | Separate explicit approval after showing target, revision, diff, evidence, and physical-completion status |
| Create a recommendation or calibration plan | Allowed | Stay inside confirmed limits and identify validation |
| Copy and edit a 3MF | Denied | Explicit scope; preserve original; name copy; hash, inspect, compare, and report |
| Install/update Creality Print | Denied | Separate explicit authorization and version/source confirmation |
| Update firmware, root a printer, bypass a sensor, or perform an electrical modification | Denied | Do not proceed from this skill; require an explicit new scope and official safety evidence |
| Send/start/cancel a print or control a printer | Denied | Separate explicit authorization for the exact job/device/action |
| Buy parts or consumables | Denied | Separate explicit authorization after exact part/material confirmation |
