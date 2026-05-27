# Cross Platform Usage

## Codex

Use this folder as a native skill directory. Load `SKILL.md` first, then `references/00-routing.md`, selected playbooks, `references/03-data-integration-policy.md`, and only the evidence cards needed for the question.

Recommended loading order for data-assisted work:

```text
SKILL.md -> references/00-routing.md -> references/10-workflow-entrypoints.md
-> references/09-data-interface-catalog.md -> selected playbooks
-> references/12-data-connector-mapping.md when provider-specific fields are needed
-> templates and evidence cards as needed
```

## Claude

Use `SKILL.md` as the entry instructions and attach references progressively. Do not paste all source reports into the main prompt. Keep credentials in Claude project settings, MCP config, or the local environment, not in the skill folder.

## OpenClaw

Place the folder under:

```text
~/.openclaw/workspace/skills/ficc-researcher
```

Keep the skill read-only for testing when possible. Configure Tushare, iFinD, Wind, or other data tools outside the skill folder. Verify with:

```bash
openclaw skills info ficc-researcher
openclaw agent --agent main --message "Use ficc-researcher to answer..."
```

OpenClaw connector outputs should be treated as data packets. The FICC skill should not store OpenClaw tokens, MCP secrets, or host-specific private paths.

Before syncing or troubleshooting OpenClaw skill discovery, read `references/13-openclaw-skill-hygiene.md`. Use Git-tracked public files for sync and keep backups outside the active `skills/` directory.

## Personal Agents

Load only these files by default:

```text
SKILL.md
references/00-routing.md
references/02-data-source-policy.md
references/03-data-integration-policy.md
selected playbooks
selected evidence cards
references/09-data-interface-catalog.md when data is required
references/12-data-connector-mapping.md when provider-specific fields are required
references/10-workflow-entrypoints.md when a repeatable report is requested
```

Do not load all source reports unless the user asks for source-level review.

## User-Provided Data

User files, tables, pasted data, and terminal output have priority over generic connector data. The agent must identify data type, timestamp, fields, units, and limitations before analysis.

## Connector Data

Connector results must include source, query, as-of date, retrieval time, fields, row count, and limitations. Treat connector output as data facts, not framework facts.

## Required Safety Contract

- No personalized investment advice.
- No fabricated yields, spreads, prices, ratings, holdings, NAV, or policy facts.
- No secrets in repository files.
- Do not paste real token values into `.mcp.example.json`, README, playbooks, eval prompts, or test logs.
- Broker reports are framework evidence, not current market data.
- Missing current data means no current market conclusion.

## Smoke Tests

Use these prompts after installation, or run the structured cases listed in `evals/smoke-prompts.yml`:

```text
What conditions would push the 10Y CGB yield higher in a low-rate environment?
How can credit bonds still generate returns when credit spreads are at low levels?
User-provided sample data: AAA 3Y credit spread = 32bp; DR007 = 1.72%. What conclusions can this data support?
```
