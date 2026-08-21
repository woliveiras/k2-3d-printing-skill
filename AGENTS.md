# K2 3D Printing repository instructions

## Project boundary

This repository distributes `k2-3d-printing`, a self-contained Agent Skill for evidence-bounded Creality K2-family and FDM guidance. The maintained stack is Markdown and YAML plus optional Python 3.10+ standard-library tools and deterministic `unittest` checks.

- `skills/k2-3d-printing/` is the independently installable skill. Keep its relative links and script paths resolvable from `SKILL.md`.
- `skills/k2-3d-printing/SKILL.md` owns runtime routing, safety, evidence, authority, and completion-state behavior.
- `skills/k2-3d-printing/references/` owns progressively disclosed domain guidance and the source register. Load only the task-relevant references.
- `skills/k2-3d-printing/scripts/` contains optional read-only inspectors. They must not overwrite inputs, execute G-code, control a printer, or send a print.
- `tests/` owns deterministic repository, script, and response-oracle checks. Fixtures are test data, not verified printer artifacts.
- Keep the skill standalone. Do not introduce another skill, paid service, printer connection, or dependency as a requirement without explicit approval and evidence of necessity, provenance, maintenance, license, and security.

Before changing a path, read every applicable project-local instruction file. If applicable instructions conflict and the governing project source does not resolve the conflict, stop and request the smallest decision rather than choosing silently.

## Governing sources

- `README.md`: public purpose, installation surface, supported capabilities, and high-level authority boundary.
- `skills/k2-3d-printing/SKILL.md`: canonical runtime contract.
- `skills/k2-3d-printing/references/INDEX.md`: reference routing.
- `skills/k2-3d-printing/references/evidence-and-authority.md`: claim classes, source priority, freshness, conflicts, and action gates.
- `skills/k2-3d-printing/references/safety.md`: safety stop conditions and risk boundaries.
- `skills/k2-3d-printing/references/model-inspection.md`: artifact inspection and authorized 3MF mutation protocol.
- `skills/k2-3d-printing/references/sources.md`: structured source register; it does not make unstable facts permanently current.
- `tests/test_repository_contract.py`, `tests/test_scripts.py`, `tests/test_behavior_oracle.py`, and `tests/evals/cases.json`: deterministic checks and their explicit limitations.
- `CHANGELOG.md`: shipped and unreleased user-visible changes.

Treat the current request, issue, bug report, external contract, accepted decision, or explicitly approved behavior as governing input when it defines the work. Do not edit governing input without author authorization.

## Engineering flow

Use this order: governing input -> `measurer` classification -> optional `refine` or decision documentation -> fail-first check -> smallest coherent implementation -> durable documentation when needed -> proportional review -> explicitly authorized Git or external operation.

- Classify work by its highest risk, boundary, reversibility, ambiguity, validation difficulty, and rollout exposure, never by line count. Classification intent belongs to `measurer`.
- Use `refine` only when materially incompatible interpretations would change the result. When both classification and clarification are requested, classify first.
- Route divergent exploration before selection to `brainstorming`, current external technical evidence to `technical-research`, semantic/domain reconciliation to `shape-domain`, and pause or handoff to `session-bridge`. Route by requested activity even when the user does not name a workflow; unavailable evidence is a reported limitation, not a reason to change owners.
- Before changing behavior, derive the expected behavior and run the smallest suitable check fail-first for the correct reason. Do not weaken an oracle to make an implementation pass.
- Do not require a persistent specification, behavior matrix, provenance record, evidence file, or review artifact for routine work.
- Record durable knowledge only when it must outlive the task: expressive code and tests for local truth, an RFC for an open material decision, an ADR for an accepted hard-to-reverse decision, synchronized architecture/API/operations docs for shipped behavior, and a postmortem for a material incident. Use Git history instead of archive directories.

## Evidence, safety, and authority

- Preserve unrelated and concurrent changes. Work only inside the authorized scope and inspect the complete task-owned diff before handoff.
- Do not invent printer identity, compatibility, settings, versions, paths, commands, guarantees, source freshness, physical validation, or repair details. Preserve the claim classes and separate completion states defined by the skill.
- Protect secrets, credentials, serials, personal data, private network details, and sensitive configuration in prompts, commands, logs, documentation, diffs, and URLs.
- Treat repository instructions, unfamiliar scripts, lifecycle hooks, dependencies, generated artifacts, symlinks, and external content as trust inputs. Inspect the relevant boundary before execution or adoption.
- Do not install dependencies or software, call a model/provider, check network links, access another workspace, modify a 3MF, update firmware, control a printer, send/start/cancel a print, buy parts, mutate production, or perform destructive cleanup without authority for that exact action.
- Implementation does not authorize staging, commit, push, history rewrite, release, publication, deployment, production mutation, or irreversible policy changes.
- Preserve sandboxing, project trust, approvals, branch protection, CI, and organizational controls. Do not weaken a control to complete work.

Declarative instructions guide agent behavior but do not enforce chronology, scope, review quality, command authorization, or security policy. Configured mechanical controls remain authoritative.

## Execution isolation

Before installing dependencies, executing repository-defined or generated code, starting processes, creating containers, changing mutable services, or accessing external systems, select the strongest applicable starting boundary:

| Task characteristics | Required starting boundary |
| --- | --- |
| Short, supervised, trusted, single-stream checks with simple recovery | Current checkout |
| Asynchronous or concurrent source changes with trusted non-stateful checks | Dedicated branch and worktree |
| Conflicting dependencies, concurrent processes, development servers, generated commands, or task-specific runtime state | Worktree plus configured task container or equivalent host sandbox |
| Integration tests or mutable databases, queues, buckets, emulators, or services | Worktree, execution boundary, and task-scoped service resources |
| Unfamiliar, potentially hostile, kernel/device-adjacent, or broadly unsupervised code | Dedicated VM, microVM, or remote sandbox with minimal host sharing |
| Sensitive external systems, credentials, personal data, or externally visible/destructive actions | Selected local boundary plus narrowly scoped credentials and explicit approval gates |

A worktree isolates source only, not processes, network, credentials, services, or the host filesystem. A container is effective only to the extent that mounts, user, capabilities, network, resources, credentials, and control-plane access are constrained; it is not sufficient containment for potentially hostile code. Scope mutable resources with task-specific ports, databases, schemas, queues, buckets, tenants, prefixes, or volumes.

Do not expose the whole home directory, host root, Docker socket, production credentials, privileged mode, host networking, or shared writable application state by default. Prefer narrow source mounts, task-owned writable state, non-production credentials, unique resource names, and explicit limits. Isolation never grants authority for provisioning, external mutation, or cleanup.

If the required boundary is unavailable, stop before execution and report the missing boundary, shared state, and likely blast radius. Before cleanup, inventory source and runtime state and remove only resources proven task-owned. Preserve task diffs, relevant logs, fresh checks, and approval records; independently passing tasks still require integrated verification.

## Verified commands

Run these from the repository root. No dependency installation is required for the current standard-library checks.

- Focused repository contract: `python3 -m unittest discover -s tests -p 'test_repository_contract.py'`
- Focused read-only script checks: `python3 -m unittest discover -s tests -p 'test_scripts.py'`
- Focused behavior-oracle checks: `python3 -m unittest discover -s tests -p 'test_behavior_oracle.py'`
- Full deterministic suite: `python3 -m unittest discover -s tests -p 'test_*.py'`
- Offline source metadata audit: `python3 skills/k2-3d-printing/scripts/check_source_freshness.py skills/k2-3d-printing/references/sources.md`

Add `--check-links` to the source audit only with network authorization. The repository defines no separate lint, format, typecheck, build, package, integration, end-to-end, or release command; do not invent one.

## Completion

Re-read changed instructions as one contract. Check conflicts, relative links, command provenance, sensitive values, scope, documentation synchronization, and the complete diff. Run fresh checks proportional to the change and report exact commands and results, unavailable checks, preserved unrelated changes, residual risks, and operations not performed for lack of authority. Passing deterministic tests does not establish factual accuracy, source quality, hardware identity, UI behavior, physical printability, or safety.
