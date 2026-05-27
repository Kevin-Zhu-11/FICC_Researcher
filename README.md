# FICC Researcher

[English](README.md) | [Chinese](README.zh-CN.md)

FICC Researcher is an agent-oriented fixed-income research skill.

Think of it as a research desk in Markdown: a routing map at the door, a row of playbooks on the wall, evidence cards in the drawer, and a strict data policy that keeps every market conclusion tied to real data instead of imagination.

It is designed for Codex, OpenClaw, Claude-style agents, and personal research agents that need to reason about Chinese fixed-income markets with auditable structure.

## What It Does

FICC Researcher helps an agent answer fixed-income questions by separating three things that are often mixed together:

- Framework facts: stable mechanisms from broker research frameworks.
- Data facts: current data from user files, MCP connectors, official sources, or verified databases.
- Inferred judgments: conditional conclusions with assumptions, missing data, and risk checks.

The skill covers:

- Rates and macro
- Bond strategy and curve analysis
- Credit strategy
- City investment bonds
- Financial credit bonds
- Wealth management, funds, and institution behavior
- Convertible bonds and hybrid assets
- Interest-rate derivatives
- Offshore bonds, USD bonds, dim sum bonds, and US Treasuries
- ABS and public REITs
- FICC quant and AI research workflows

## Why This Exists

Fixed-income analysis is easy to make sound confident and hard to make auditable.

This repo tries to make the agent slow down in the right places:

- First route the question.
- Then choose the right playbook.
- Then ask what data is required.
- Then separate current facts from framework logic.
- Then state what cannot be confirmed.

The result should feel less like a one-shot opinion and more like a junior fixed-income researcher who learned to keep a clean notebook.

## Repository Map

```text
FICC_Researcher/
├── SKILL.md                         # Main agent entrypoint
├── agents/
│   └── openai.yaml                  # Agent-facing metadata
├── assets/templates/                # Reusable output templates
├── docs/projects/                   # Design and execution plans
├── docs/review/                     # Validation and review notes
├── examples/
│   ├── data/                        # Synthetic or official-public sample data packets
│   └── golden-cases/                # Golden answer examples for eval and style checks
├── references/
│   ├── 00-routing.md                # Question routing table
│   ├── 01-source-index.yml          # Source id index, without report originals
│   ├── 02-data-source-policy.md     # Data-source priority and missing-data rules
│   ├── 03-data-integration-policy.md
│   ├── 04-mcp-connectors.md         # MCP connector boundaries and examples
│   ├── 05-cross-platform-usage.md   # Codex/OpenClaw/Claude usage notes
│   ├── 06-portfolio-action-policy.md
│   ├── 07-macro-indicator-glossary.md
│   ├── 08-policy-reaction-function.md
│   ├── 09-data-interface-catalog.md # Field-level data needs and connector boundaries
│   ├── 10-workflow-entrypoints.md   # Portable command-like research workflows
│   ├── 11-research-decision-chains.md
│   ├── 12-data-connector-mapping.md # Provider candidate mapping and citation metadata
│   ├── 13-openclaw-skill-hygiene.md # Safe OpenClaw sync and skill discovery rules
│   ├── 14-contracts-and-analysis-standards.md # Canonical output/data contract
│   ├── 15-playbook-framework-standard.md # Canonical playbook framework structure
│   ├── 16-source-claim-map.yml      # Claim-to-evidence/source mapping
│   ├── playbooks/                   # Core research playbooks
│   ├── evidence-cards/              # Compressed source-evidence cards
│   └── chart-notes/                 # Chart and image-url notes
├── evals/                            # Smoke prompts and expected output contracts
└── scripts/                         # Validation and indexing helpers
```

## Quick Start

Use the GitHub release if you want a clean public package:

- Release page: <https://github.com/Kevin-Zhu-11/FICC_Researcher/releases/tag/v0.1.0-public-preview>
- Release asset: `ficc-researcher-v0.1.0-public-preview.zip`

Or clone the repository directly:

```bash
git clone https://github.com/Kevin-Zhu-11/FICC_Researcher.git ficc-researcher
cd ficc-researcher
python scripts/validate_skill_links.py
python scripts/validate_eval_cases.py
```

Then ask your agent to use the skill by name:

```text
Use the ficc-researcher skill to analyze how China social financing data for April 2026 affects the rates-bond curve.
If current yields, credit spreads, funding rates, or expectation data are missing, list the missing fields and do not invent market levels.
```

Expected behavior:

- The agent routes the question through `references/00-routing.md`.
- It reads the relevant playbooks and the canonical contract in `references/14-contracts-and-analysis-standards.md`.
- It separates framework facts, data facts, inferred judgments, confidence, missing data, and risks.
- It refuses to invent current market levels when no verified source is available.

## Installation

### Codex

Clone or copy the public repo into your Codex skills directory. The default location is usually `$CODEX_HOME/skills` or `~/.codex/skills`.

Windows PowerShell example:

```powershell
$skillsRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills" } else { Join-Path $HOME ".codex\skills" }
New-Item -ItemType Directory -Force $skillsRoot | Out-Null
git clone https://github.com/Kevin-Zhu-11/FICC_Researcher.git (Join-Path $skillsRoot "ficc-researcher")
```

If you use a release zip, extract it to:

```text
<codex-skills-root>/ficc-researcher/
```

The folder should contain `SKILL.md` at its root.

### OpenClaw

Install the skill into the active OpenClaw workspace:

```bash
mkdir -p ~/.openclaw/workspace/skills/ficc-researcher
git clone https://github.com/Kevin-Zhu-11/FICC_Researcher.git /tmp/ficc-researcher
cd /tmp/ficc-researcher
git archive --format=tar HEAD | tar -xf - -C ~/.openclaw/workspace/skills/ficc-researcher
cd ~/.openclaw/workspace/skills/ficc-researcher
python3 scripts/validate_skill_links.py
python3 scripts/validate_eval_cases.py
```

Keep only one active `ficc-researcher/` directory under `~/.openclaw/workspace/skills/`. Put backups outside the active skills folder, for example under `~/.openclaw/workspace/skills-backups/`.

Do not sync ignored local material from `references/source-reports/**`. The public skill needs only `references/source-reports/.gitkeep`.

### Claude-Style Or Other Agents

Use the repo as a read-only skill folder. Point the agent to:

```text
SKILL.md
references/00-routing.md
references/14-contracts-and-analysis-standards.md
references/10-workflow-entrypoints.md
```

Then let the router choose one to three playbooks under `references/playbooks/`.

## How Agents Should Use It

For substantial fixed-income analysis, the agent should follow this path:

```text
SKILL.md
-> references/00-routing.md
-> references/14-contracts-and-analysis-standards.md for canonical output and data contracts
-> references/15-playbook-framework-standard.md for framework consistency and conflict handling
-> references/16-source-claim-map.yml when source traceability is required
-> references/10-workflow-entrypoints.md when the user asks for a repeatable report
-> references/09-data-interface-catalog.md when current or historical data is required
-> references/12-data-connector-mapping.md when provider-specific fields are needed
-> one to three relevant playbooks
-> data-source policy
-> data-integration policy if user data or MCP data is available
-> output template
```

Minimum output structure:

```text
Question type:
Playbooks used:
Data input:
Data quality checks:
Framework facts:
Data facts:
Inferred judgments:
Confidence:
Missing data:
Risks and counterexamples:
Follow-up indicators:
```

## Example Prompt For OpenClaw

```text
Use the ficc-researcher skill to analyze how China social financing data for April 2026 affects the bond market.

First use WebSearch to locate authoritative sources, prioritizing PBOC data.
Then read SKILL.md, references/00-routing.md, references/playbooks/rates-macro.md, and references/playbooks/bond-strategy.md.

The output must separate:
- Data facts found through search
- Framework facts from the playbooks
- Conditional inferences based on data and framework logic
- Data that is still missing
- Risks and counterexamples

Do not fabricate current market data that was not found, and do not give personal investment advice.
```

## Data Connector Setup

FICC Researcher does not require a specific data provider. It works best when your agent can access at least one structured data path plus official public sources.

Typical setup:

1. Configure provider credentials outside this repository.
2. Register MCP servers or local data bridges in your agent runtime.
3. Ask the connector to return source metadata with every table.
4. Convert connector output into the canonical data packet before analysis.

The canonical data packet is:

```text
source:
provider:
interface_or_file:
query:
as_of:
retrieved_at:
time_range:
frequency:
universe:
fields:
row_count:
units:
schema_notes:
missing_fields:
limitations:
```

For OpenClaw, do not paste a top-level `mcpServers` block into `~/.openclaw/openclaw.json` unless your OpenClaw version explicitly supports it. Prefer the runtime's MCP command interface, for example:

```bash
openclaw mcp list
openclaw mcp set <provider-name> '<json-config-with-env-placeholders>'
openclaw mcp show <provider-name>
```

Use environment variables or your runtime's secret manager for credentials. Keep `.env`, tokens, private endpoints, account names, and paid raw data exports out of this repo.

## Data Boundary

This skill does not hardcode live market data.

It is meant to work with external data providers such as:

- User-provided tables or files
- Tushare MCP
- iFinD
- Wind
- Local bond databases
- Official public sources
- WebSearch for current verification

The FICC skill tells the agent what data is needed and how to reason with it. Connectors provide the data.

Provider names in this repository are optional data-source examples, not endorsements, sublicenses, guarantees of coverage, or official partnerships. Users must configure their own credentials and comply with each provider's terms. Do not paste real token values into `.mcp.example.json`, README, playbooks, eval prompts, or test logs.

Use `references/09-data-interface-catalog.md` for field-level data needs and provider boundaries. For example, Tushare can be useful for selected macro datasets such as social-financing aggregates and money supply where permission allows, while professional bond curves, credit spreads, institution flows, and issuer-risk datasets often require Wind, iFinD, ChinaBond, CFETS, SHCH, a local database, or user-provided exports.

Use `references/12-data-connector-mapping.md` for provider-specific candidate fields, required metadata, and missing-data downgrade rules. These mappings are optional and permission-dependent; they are not provider endorsements or guarantees.

## Quality Evaluation And Examples

The `evals/` folder now has two layers:

- `expected-output-contracts.yml`: minimum output blocks for each workflow.
- `quality-rubrics.yml`: hard gates and scoring dimensions for human or agent-assisted review.

The `examples/data/` folder contains small sample packets. The `examples/golden-cases/` folder contains answer-shape examples that demonstrate missing-data discipline. Example data is synthetic, desensitized, or official-public only; it is not a licensed market-data export.

To run smoke checks manually, pick one prompt from `evals/smoke-prompts.yml`, run it in your target agent, and review the answer against:

```text
evals/expected-output-contracts.yml
evals/quality-rubrics.yml
examples/golden-cases/
```

For current-market prompts, a good result may be a refusal to provide point estimates. If no verified connector or official source is available, the answer should list missing fields and preferred sources.

## OpenClaw Usage Hygiene

Read `references/13-openclaw-skill-hygiene.md` before syncing this skill into OpenClaw.

The safe default is to sync Git-tracked public files only, keep backups outside the active `skills/` directory, and never copy ignored `references/source-reports/**` material into a public OpenClaw skill folder.

## Source Report Boundary

The original broker-report Markdown files are intentionally not included in this GitHub repository.

`references/source-reports/*.md` is ignored by Git because the source reports may carry copyright or distribution restrictions. The public repo keeps the extracted framework layer:

- Playbooks
- Evidence cards
- Source id index
- Chart notes
- Data policies
- Templates

If you have lawful local access to the original report Markdown files, you can keep them locally under:

```text
references/source-reports/
```

The validation scripts are designed so the public repo remains usable without those private files.

## Validation

Run these from the repo root:

```powershell
python .\scripts\build_source_index.py
python .\scripts\validate_source_refs.py
python .\scripts\validate_claim_map.py
python .\scripts\validate_skill_links.py
python .\scripts\validate_eval_cases.py
python .\scripts\validate_quality_rubrics.py
python .\scripts\validate_examples.py
```

If Codex `skill-creator` is installed locally, also run its `quick_validate.py` against this repo using your own local skill path.

Expected behavior:

- Public clone: source index and source-id references can be validated without report originals.
- Local research workspace: if `references/source-reports/*.md` exists, scripts also check that local source files align with the index.
- Eval prompts: `evals/smoke-prompts.yml` defines cross-agent smoke cases, `evals/expected-output-contracts.yml` defines the minimum output blocks each workflow should satisfy, and `evals/quality-rubrics.yml` defines quality review gates.

## Status

Current completion level: approximately 98%.

The skill framework, routing, playbooks, evidence cards, templates, quality rubrics, golden examples, connector mapping, and OpenClaw regression checks are in place. The remaining work is live data-provider integration testing and provider-specific expansion for future iFinD/Wind/local database workflows.

## License

This repository is released under the MIT License. See `LICENSE`.

The license applies to the code, extracted playbooks, templates, and repository materials in this repo. It does not grant rights to any third-party broker reports or private source documents that are not included here.
