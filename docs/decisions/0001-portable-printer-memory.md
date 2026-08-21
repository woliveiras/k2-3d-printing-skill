# ADR 0001: Portable printer memory

- Status: Accepted
- Date: 2026-08-21

## Context

Repeated printer identity and installed-configuration questions add friction, while agent-native memory is not portable and slicer profiles do not prove physical hardware. The skill must support multiple printers without requiring administrator access, another agent, a service, a printer connection, or non-standard Python packages.

## Decision

Store current printer state in schema-versioned JSON under the operating system's per-user configuration directory, with an environment-variable override for an explicitly shared location. Keep the file outside the skill installation and project repository.

Bundle a Python 3.10+ standard-library manager that reads and validates memory, creates write-free proposals, and applies a proposal only after separate user approval. Reconstruct the candidate from the approved diff, use revision and content checks, and write by atomic replacement to reject hidden or stale concurrent changes. Treat temporary changes as conversation state and persist permanent hardware changes only after physical completion is confirmed.

Support multiple printers by user-selected aliases from the first schema version. Store current state, field evidence, and confirmation dates; do not store serial numbers, credentials, private network details, conversation transcripts, or an unbounded component history. Changing an alias to a different physical model requires an explicit reset of dependent setup and software state. A recent physical observation overrides stored memory. Slicer configuration may expose a conflict but cannot prove or overwrite physical identity.

## Consequences

Local agents that can execute Python and access the same file share the same memory. Remote or sandboxed agents need an explicitly accessible copy or data-directory override; the Agent Skills format does not provide a shared mutable store. The manager is the only bundled script authorized to write, and only to its resolved memory file, lock, atomic temporary file, and single recovery backup.
