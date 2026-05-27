---
name: ficc-researcher
description: Fixed income and FICC research workflow skill for Chinese bond-market analysis, rates and macro, credit bonds, city investment bonds, financial credit, convertible bonds, wealth management and fund behavior, institution behavior, offshore bonds, USD bonds, dim sum bonds, US Treasuries, ABS, public REITs, interest-rate derivatives, bond portfolios, and FICC quant or AI research. Use when Codex needs to apply broker research frameworks, route questions to fixed-income playbooks, distinguish framework facts from current data, and produce auditable research drafts without fabricating market data or investment advice.
---

# FICC Researcher

Use this skill for fixed-income and FICC research tasks that need broker-framework reasoning, routing across rates, credit, convertibles, institution behavior, offshore bonds, ABS, REITs, derivatives, portfolio construction, or FICC quant and AI research.

## Operating Principles

- Start from `references/00-routing.md`, then read only the relevant playbooks.
- Keep `SKILL.md` lightweight; use `references/` for long framework details and source evidence.
- Use `references/14-contracts-and-analysis-standards.md` as the canonical source for output blocks, data packets, missing-data format, confidence labels, time horizons, source traceability, and portfolio-action boundaries.
- Use `references/15-playbook-framework-standard.md` to interpret or edit playbook frameworks, and `references/16-source-claim-map.yml` when source-level traceability is required.
- Separate framework facts, current data facts, and inferred judgments in every research output.
- Treat broker research Markdown files as framework evidence, not as live market data.
- Never fabricate real-time yields, spreads, prices, ratings, holdings, NAV, issuance, trading volume, or policy events.
- Use centralized data-source rules in `references/02-data-source-policy.md`; do not hardcode connector credentials or private endpoints in playbooks.
- When the user provides data or a connector returns data, apply `references/03-data-integration-policy.md` before analysis.

## Workflow

1. Classify the user question by topic, instrument, investor type, and time sensitivity.
2. Read `references/00-routing.md` and choose 1 to 3 playbooks.
3. Read `references/14-contracts-and-analysis-standards.md` for the canonical output and data contract.
4. Read `references/15-playbook-framework-standard.md` when the task requires framework comparison, playbook editing, or cross-playbook conflict resolution.
5. Read the selected files under `references/playbooks/`.
6. If the user asks for a repeatable research product, read `references/10-workflow-entrypoints.md` and use the mapped template under `assets/templates/`.
7. If source traceability is triggered by `references/14-contracts-and-analysis-standards.md`, consult `references/16-source-claim-map.yml`, `references/01-source-index.yml`, and the relevant file under `references/evidence-cards/`.
8. If the task needs live, historical, or user-supplied data, read `references/09-data-interface-catalog.md` to define required fields before choosing sources.
9. Apply `references/02-data-source-policy.md` to choose source priority and missing-data behavior.
10. If provider-specific field mapping is needed, read `references/12-data-connector-mapping.md`.
11. If the user uploads data or an MCP/connector returns data, normalize it with `references/03-data-integration-policy.md`.
12. If the answer spans multiple playbooks or channels conflict, use `references/11-research-decision-chains.md`.
13. For connector setup templates and boundaries, read `references/04-mcp-connectors.md`.
14. For portfolio-action questions, use `references/06-portfolio-action-policy.md`.
15. For macro data releases, use `references/07-macro-indicator-glossary.md` and `references/08-policy-reaction-function.md`.
16. If deploying or syncing this skill into OpenClaw, read `references/13-openclaw-skill-hygiene.md`.
17. Produce an auditable research draft using the canonical contract in `references/14-contracts-and-analysis-standards.md`.

## Data Source Priority

Use the canonical current-data priority in `references/14-contracts-and-analysis-standards.md`, with operational rules in `references/02-data-source-policy.md`.

If required data is missing, output the `Missing data` block from `references/14-contracts-and-analysis-standards.md` and limit the conclusion to framework analysis.

If the user provides a table, file, or pasted dataset, analyze that data first. State what the data can support, what it cannot support, and which connector or official source would fill the gap.

For field-level data needs, use `references/09-data-interface-catalog.md`. It is connector-neutral: it may mention Tushare, iFinD, Wind, local databases, official sources, or WebSearch as optional sources, but it must not be treated as credential setup or provider endorsement.

For provider-specific field candidates and citation metadata, use `references/12-data-connector-mapping.md`. Treat every provider mapping as optional and permission-dependent.

## Routing

Use `references/00-routing.md` for routing. For broad or ambiguous questions:

- Rates, macro, curve, duration: `rates-macro.md` and `bond-strategy.md`.
- Credit spreads, asset shortage, credit beta: `credit-strategy.md` and `institution-behavior.md`.
- Wealth management redemptions and fund behavior: `wealth-management-funds.md` and `institution-behavior.md`.
- Convertibles and hybrid assets: `convertible-hybrid.md`.
- Derivatives, offshore bonds, ABS, REITs, city investment, and financial credit: route to the matching playbook and use source reports or evidence cards for traceability.
- Repeatable research products: select the workflow in `references/10-workflow-entrypoints.md` for macro data commentary, yield-curve review, credit-spread review, institution-flow review, portfolio-action review, policy-event commentary, convertible review, daily bond brief, or data-assisted analysis.

## Output Contract

Every substantial answer should follow `references/14-contracts-and-analysis-standards.md`:

- `Question type`
- `Playbooks used`
- `Data input`
- `Data quality checks`
- `Framework facts`
- `Data facts`
- `Inferred judgments`
- `Confidence`
- `Missing data`
- `Risks and counterexamples`
- `Follow-up indicators`
- `Portfolio actions` when the user asks for duration, curve, leverage, credit allocation, sizing, or risk triggers.

For reusable output formats, use `assets/templates/` when producing reports or handoff drafts.

## Prohibited Behavior

- Do not provide personalized investment advice or guarantee returns.
- Do not invent current market levels, spreads, prices, ratings, holdings, NAV, policy decisions, or issuer events.
- Do not treat old research-report examples as current market facts.
- Do not hide material uncertainty or missing data.
- Do not put passwords, tokens, API keys, account identifiers, or private service URLs in repository files.
- Do not use mechanical shortcuts such as `data weak = yields down`, `supply up = yields up only`, `carry = risk-free`, `policy support = issuer safety`, or `single DR007 point = leverage signal`.

## Validation

Before treating this skill as ready, run:

```powershell
python .\scripts\build_source_index.py
python .\scripts\validate_source_refs.py
python .\scripts\validate_claim_map.py
python .\scripts\validate_skill_links.py
python .\scripts\validate_eval_cases.py
python .\scripts\validate_quality_rubrics.py
python .\scripts\validate_examples.py
```

If the local Codex `skill-creator` system skill is installed, also run its `quick_validate.py` against this skill directory using the local machine's own skill path.
