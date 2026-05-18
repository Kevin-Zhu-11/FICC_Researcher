# FICC Researcher

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
├── references/
│   ├── 00-routing.md                # Question routing table
│   ├── 01-source-index.yml          # Source id index, without report originals
│   ├── 02-data-source-policy.md     # Data-source priority and missing-data rules
│   ├── 03-data-integration-policy.md
│   ├── 04-mcp-connectors.md         # MCP connector boundaries and examples
│   ├── 05-cross-platform-usage.md   # Codex/OpenClaw/Claude usage notes
│   ├── playbooks/                   # Core research playbooks
│   ├── evidence-cards/              # Compressed source-evidence cards
│   └── chart-notes/                 # Chart and image-url notes
└── scripts/                         # Validation and indexing helpers
```

## How Agents Should Use It

For substantial fixed-income analysis, the agent should follow this path:

```text
SKILL.md
-> references/00-routing.md
-> one to three relevant playbooks
-> data-source policy
-> data-integration policy if user data or MCP data is available
-> output template
```

Minimum output structure:

```text
问题归类:
使用 playbook:
框架事实:
数据事实:
推断判断:
缺少数据:
风险与反例:
后续跟踪:
```

## Example Prompt For OpenClaw

```text
请使用 ficc-researcher skill 分析 2026 年 4 月中国社会融资数据对债券市场的影响。

先通过 WebSearch 查找权威来源，优先使用中国人民银行数据。
然后读取 SKILL.md、references/00-routing.md、references/playbooks/rates-macro.md 和 references/playbooks/bond-strategy.md。

输出时必须区分：
- 搜索得到的数据事实
- playbook 中的框架事实
- 基于数据和框架的条件推断
- 仍然缺少的数据
- 风险与反例

不要编造没有查到的当前市场数据，不要给个人投资建议。
```

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
python .\scripts\validate_skill_links.py
python C:\Users\kevin\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\000AAA_Datas\Python\Skills\FICC_Researcher
```

Expected behavior:

- Public clone: source index and source-id references can be validated without report originals.
- Local research workspace: if `references/source-reports/*.md` exists, scripts also check that local source files align with the index.

## Status

Current completion level: approximately 95%.

The skill framework, routing, playbooks, evidence cards, templates, and OpenClaw regression checks are in place. The remaining 5% is live data-provider integration testing, especially Tushare MCP and future iFinD/Wind workflows.

## License

This repository is released under the MIT License. See `LICENSE`.

The license applies to the code, extracted playbooks, templates, and repository materials in this repo. It does not grant rights to any third-party broker reports or private source documents that are not included here.
