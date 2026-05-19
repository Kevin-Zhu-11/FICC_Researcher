---
name: ficc-researcher
description: Fixed income and FICC research workflow skill for Chinese bond-market analysis, rates and macro, credit bonds, city investment bonds, financial credit, convertible bonds, wealth management and fund behavior, institution behavior, offshore bonds, USD bonds, dim sum bonds, US Treasuries, ABS, public REITs, interest-rate derivatives, bond portfolios, and FICC quant or AI research. Use when Codex needs to apply broker research frameworks, route questions to fixed-income playbooks, distinguish framework facts from current data, and produce auditable research drafts without fabricating market data or investment advice.
---

# FICC Researcher

Use this skill for fixed-income and FICC research tasks that need broker-framework reasoning, routing across rates, credit, convertibles, institution behavior, offshore bonds, ABS, REITs, derivatives, portfolio construction, or FICC quant and AI research.

## Operating Principles

- Start from `references/00-routing.md`, then read only the relevant playbooks.
- Keep `SKILL.md` lightweight; use `references/` for long framework details and source evidence.
- Separate framework facts, current data facts, and inferred judgments in every research output.
- Treat broker research Markdown files as framework evidence, not as live market data.
- Never fabricate real-time yields, spreads, prices, ratings, holdings, NAV, issuance, trading volume, or policy events.
- Use centralized data-source rules in `references/02-data-source-policy.md`; do not hardcode connector credentials or private endpoints in playbooks.
- When the user provides data or a connector returns data, apply `references/03-data-integration-policy.md` before analysis.

## Workflow

1. Classify the user question by topic, instrument, investor type, and time sensitivity.
2. Read `references/00-routing.md` and choose 1 to 3 playbooks.
3. Read the selected files under `references/playbooks/`.
4. If source-traceability is needed, consult `references/01-source-index.yml`.
5. If the answer needs broker-evidence synthesis, read the relevant file under `references/evidence-cards/` before reading full source reports.
6. If current data is needed, apply `references/02-data-source-policy.md` before drawing conclusions.
7. If the task needs live, historical, or user-supplied data fields, read `references/09-data-interface-catalog.md` for required fields, preferred sources, connector limits, and missing-data behavior.
8. If the user asks for a repeatable research product, read `references/10-workflow-entrypoints.md` and use the mapped template under `assets/templates/`.
9. If the answer spans multiple playbooks, use `references/11-research-decision-chains.md` to keep the reasoning path explicit.
10. If the user uploads data or an MCP/connector returns data, normalize it with `references/03-data-integration-policy.md`.
11. For connector setup templates and boundaries, read `references/04-mcp-connectors.md`.
12. For portfolio-action questions, use `references/06-portfolio-action-policy.md`.
13. For macro data releases, use `references/07-macro-indicator-glossary.md` and `references/08-policy-reaction-function.md`.
14. Produce an auditable research draft with assumptions, data gaps, risk checks, and follow-up indicators.

## Data Source Priority

Use this priority order:

1. User-provided data or local verified databases.
2. Verified finance data connectors such as iFinD, Tushare, Wind, or local bond databases.
3. Broker research frameworks in `references/source-reports/`.
4. Official public sources and exchange, clearing, central bank, treasury, regulator, or issuer disclosures.
5. Web search only as background or news verification when a reliable current source is required.

If required data is missing, output the missing-data block from `references/02-data-source-policy.md` and limit the conclusion to framework analysis.

If the user provides a table, file, or pasted dataset, analyze that data first. State what the data can support, what it cannot support, and which connector or official source would fill the gap.

For field-level data needs, use `references/09-data-interface-catalog.md`. It is connector-neutral: it may mention Tushare, iFinD, Wind, local databases, official sources, or WebSearch as optional sources, but it must not be treated as credential setup or provider endorsement.

## Routing

Use `references/00-routing.md` for routing. For broad or ambiguous questions:

- Rates, macro, curve, duration: `rates-macro.md` and `bond-strategy.md`.
- Credit spreads, asset shortage, credit beta: `credit-strategy.md` and `institution-behavior.md`.
- Wealth management redemptions and fund behavior: `wealth-management-funds.md` and `institution-behavior.md`.
- Convertibles and hybrid assets: `convertible-hybrid.md`.
- Derivatives, offshore bonds, ABS, REITs, city investment, and financial credit: route to the matching playbook and use source reports or evidence cards for traceability.
- Repeatable research products: select the workflow in `references/10-workflow-entrypoints.md` for macro data commentary, yield-curve review, credit-spread review, institution-flow review, portfolio-action review, policy-event commentary, convertible review, daily bond brief, or data-assisted analysis.

## Output Contract

Every substantial answer should include:

- Question classification and selected playbooks.
- Framework facts: stable mechanisms from broker frameworks.
- Data facts: current or user-provided data, with source and timestamp.
- Data input: user file, MCP result, connector output, official source, or WebSearch lead.
- Inferred judgments: conditional conclusions and confidence level.
- Missing data: fields, recommended source, time range, frequency, and use.
- Risks and counterexamples.
- Follow-up indicators or monitoring checklist.
- Portfolio action block when the user asks for duration, curve, leverage, credit allocation, or risk triggers.

For reusable output formats, use `assets/templates/` when producing reports or handoff drafts.

## Prohibited Behavior

- Do not provide personalized investment advice or guarantee returns.
- Do not invent current market levels, spreads, prices, ratings, holdings, NAV, policy decisions, or issuer events.
- Do not treat old research-report examples as current market facts.
- Do not hide material uncertainty or missing data.
- Do not put passwords, tokens, API keys, account identifiers, or private service URLs in repository files.

## Validation

Before treating this skill as ready, run:

```powershell
python .\scripts\build_source_index.py
python .\scripts\validate_skill_links.py
python .\scripts\validate_eval_cases.py
python C:\Users\kevin\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\000AAA_Datas\Python\Skills\FICC_Researcher
```
