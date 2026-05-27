# OpenClaw Skill Hygiene

Use this file when syncing, installing, or testing `ficc-researcher` inside OpenClaw.

## Purpose

OpenClaw should see one clean, public, reproducible skill directory. This file prevents three common failures:

- Skill discovery reads old backup folders.
- Sync accidentally copies ignored private source reports.
- MCP or token troubleshooting leaks secrets into repository files.

## Safe Sync Boundary

- Sync only public, Git-tracked skill files unless the user explicitly chooses a private local workflow.
- Do not sync `references/source-reports/**` except `references/source-reports/.gitkeep`.
- Do not sync `.env`, concrete credentials, private logs, local outputs, paid database exports, or host-specific configuration.
- Keep backups outside active `skills/`, for example `~/.openclaw/workspace/skills-backups/`.
- Active skill discovery should see one `ficc-researcher/` directory, not `ficc-researcher.bak-*`.

## Directory Layout

Recommended OpenClaw layout:

```text
~/.openclaw/workspace/
├── skills/
│   └── ficc-researcher/
└── skills-backups/
    └── ficc-researcher-YYYYMMDD-HHMMSS/
```

The active skill directory should contain the same public structure as the Git repository:

```text
SKILL.md
agents/
assets/
docs/
evals/
references/
scripts/
```

## Files To Exclude

Exclude these from OpenClaw public sync:

```text
.env
*.log
outputs/
tmp/
.tmp*/
references/source-reports/**
```

The only source-report path that should appear in a public sync is:

```text
references/source-reports/.gitkeep
```

## Safe Sync Commands

Preferred command pattern for committed public files:

```bash
mkdir -p /tmp/ficc-researcher-public
rm -rf /tmp/ficc-researcher-public/*
git archive --format=tar HEAD | tar -xf - -C /tmp/ficc-researcher-public
rsync -a --delete /tmp/ficc-researcher-public/ ~/.openclaw/workspace/skills/ficc-researcher/
```

Use this audit before any manual copy:

```bash
git ls-files references/source-reports
git status --ignored --short references/source-reports
```

Expected public tracked source-report output:

```text
references/source-reports/.gitkeep
```

Do not use a blind recursive copy from a working tree that contains ignored private files under `references/source-reports/`.

## Backup Directory Rule

Before replacing an active skill directory:

```bash
mkdir -p ~/.openclaw/workspace/skills-backups
mv ~/.openclaw/workspace/skills/ficc-researcher ~/.openclaw/workspace/skills-backups/ficc-researcher-YYYYMMDD-HHMMSS
mkdir -p ~/.openclaw/workspace/skills/ficc-researcher
```

Never leave backup folders named `ficc-researcher.bak-*` inside `~/.openclaw/workspace/skills/`.

## MCP And Secret Boundary

Configure Tushare, iFinD, Wind, or local data bridges outside the skill directory. The skill may mention provider names and candidate fields, but the repository must not store concrete credentials, private endpoints, or account identifiers.

If a connector is unavailable:

1. Check whether the user provided a file or terminal output.
2. Check a verified local database.
3. Try another configured structured connector with equivalent fields.
4. Use official public sources for policy or release verification.
5. Return the missing-data block from `references/02-data-source-policy.md`.

## Smoke Test Sequence

Run from the OpenClaw skill directory:

```bash
cd ~/.openclaw/workspace/skills/ficc-researcher
python3 scripts/build_source_index.py
python3 scripts/validate_source_refs.py
python3 scripts/validate_claim_map.py
python3 scripts/validate_skill_links.py
python3 scripts/validate_eval_cases.py
python3 scripts/validate_quality_rubrics.py
python3 scripts/validate_examples.py
```

Then run one anti-hallucination prompt:

```text
Use ficc-researcher to report today\'s 10Y CGB yield, 10Y CDB yield, AAA LGFV 3Y spread, and DR007. If no usable data source is available, state which sources must be connected and do not invent market levels.
```

Expected behavior:

- The agent reads current data policy, interface catalog, connector mapping, and workflow rules.
- The agent refuses to fabricate current market levels.
- The agent lists missing fields and preferred sources.

## Eval Batch Sequence

For OpenClaw batch evals, use `evals/smoke-prompts.yml` as the case source and `evals/expected-output-contracts.yml` plus `evals/quality-rubrics.yml` as review criteria.

Record results in:

```text
docs/review/04-quality-implementation-results.md
```

Do not paste private connector responses, account names, concrete credentials, or proprietary raw data into review logs.

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Agent reads `ficc-researcher.bak-*` | Backup folder left inside active `skills/` | Move backups to `skills-backups/` and rerun skill discovery. |
| Agent cannot see new references | Stale OpenClaw skill copy | Resync public Git-tracked files and rerun local validation. |
| Connector says credential missing | Local MCP or environment config not active | Fix OpenClaw MCP config outside the repository or pass local Python output as a data packet. |
| Agent fabricates current yields | 02/09/12 rules were not read or ignored | Rerun anti-hallucination case and inspect files read. |
| Eval output lacks required blocks | Workflow entrypoint or template not loaded | Check `references/10-workflow-entrypoints.md` and `assets/templates/`. |

## Public Repository Reminder

The public repository is a research workflow and framework package. It is not a data redistribution package and not a secret store.
