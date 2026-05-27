# Playbook Framework Standard

Use this file when writing, editing, or interpreting any FICC Researcher playbook. It standardizes framework expression so agents do not have to switch between incompatible reasoning styles.

## Relation To Other Contracts

- `references/14-contracts-and-analysis-standards.md` defines answer output and data packet contracts.
- This file defines playbook framework structure.
- `references/16-source-claim-map.yml` maps framework claims to evidence-card sections and source report ids.
- `references/11-research-decision-chains.md` resolves multi-playbook and cross-channel conflicts.

## Standard Playbook Structure

Each playbook should preserve these sections:

```text
# Playbook Name
## Scope
## When To Use
## Required Inputs
## Framework
## Framework Claims
## Analysis Steps
## Output Overlay
## Risk Checks
## Source Reports
## Claim IDs
## Search Keywords
```

`Output Overlay` is not a replacement for the canonical answer contract. It only adds workflow-specific fields that may appear under `Framework facts`, `Data facts`, `Inferred judgments`, `Missing data`, `Risks and counterexamples`, or `Portfolio actions`.

## Required Inputs Standard

Group inputs by use, not by provider:

```text
Decision context:
Current market data:
Issuer or instrument data:
Policy and event data:
Institution and flow data:
Validation or comparison data:
```

If a category is irrelevant, omit it. Do not mix required data fields with framework concepts. Put field-level source candidates in `references/09-data-interface-catalog.md` or `references/12-data-connector-mapping.md`.

## Framework Expression Standard

Every framework should contain:

1. A compact chain or equation.
2. A mechanism explanation.
3. A failure condition.
4. A link to source claim ids.

Preferred form:

```text
inputs and constraints
-> transmission mechanism
-> pricing or behavior channel
-> decision implication
```

Do not use a chain as a mechanical conclusion. Use it to identify which data decides the channel.

## Framework Claims Table

Each playbook should list 2 to 4 stable claims:

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `RM-01` | Low-rate regimes weaken one-factor macro beta. | Fiscal behavior, institution liabilities, supply, and policy constraints can dominate growth/inflation prints. | Current curve, funding, supply, and institution data point to a different dominant channel. |

Rules:

- Claim ids must appear in `references/16-source-claim-map.yml`.
- Claims should be stable framework claims, not current-market facts.
- Do not encode live data levels in claims.
- If a claim applies across playbooks, keep one primary claim and reference it from secondary playbooks.

## Conflict Resolution Standard

When frameworks conflict, do not choose by file order. Use competing channels:

```text
Channel A:
- mechanism:
- data needed:
- implication if dominant:

Channel B:
- mechanism:
- data needed:
- implication if dominant:

Resolution:
- current dominant channel:
- missing data:
- confidence:
```

Examples:

- Fiscal expansion can support growth and increase bond supply; duration impact depends on issuance, payment,central-bank liquidity offset, and allocation demand.
- Wide carry can improve expected return but increase drawdown risk if funding, product liability, or liquidity weakens.
- Asset shortage can compress spreads but does not improve issuer fundamentals.

## Source Claim Mapping Standard

Use `references/16-source-claim-map.yml` for source traceability:

```text
claim_id:
playbook:
claim:
evidence_card:
evidence_section:
source_ids:
decision_chain:
```

Source ids must exist in `references/01-source-index.yml`. Evidence cards compress source frameworks; they do not replace current data.

## Quant And AI Special Rule

FICC quant or AI playbooks must be domain-specific:

- Use point-in-time availability and release lag rules.
- Distinguish daily market data from monthly macro data and event-time labels.
- Treat curves, spreads, bonds, issuers, funds, and policy events as different data entities.
- Validate transaction cost, turnover, liquidity, and stale valuation risk.
- Keep LLMs as parsing, routing, summarization, and monitoring tools unless connected to verified data packets.

## Maintenance Rules

- New playbook claim -> update `16-source-claim-map.yml`.
- New evidence card -> update `scripts/validation_config.py`.
- New workflow smoke -> update `evals/smoke-prompts.yml` and `evals/quality-rubrics.yml` if needed.
- New source report id -> update `01-source-index.yml` and run `validate_source_refs.py` plus `validate_claim_map.py`.
