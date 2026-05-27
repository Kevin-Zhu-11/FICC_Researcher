# Quant AI Research

## Scope

Use this playbook for fixed-income quant research, AI research workflows, factor extraction, monitoring, report automation, agent design, and data-to-framework research systems.

## When To Use

- The question mentions FICC quant research, AI-assisted research, factor, monitoring, agent, automated reporting, LLM, prompt, or data-driven research.
- The user wants to turn research reports or market data into repeatable signals or monitoring workflows.
- The answer needs model validation and human review boundaries.

## Required Inputs

- Decision target: curve direction, credit-spread allocation, funding stress, institution flow, convertible valuation, policy-event response, or report-monitoring workflow.
- Point-in-time data contract: source, as_of, retrieved_at, release_time, availability_lag, frequency, universe, entity id, field definition, units, and revision policy.
- FICC entities: curve point, bond, issuer, rating, sector, region, fund, wealth product, institution, policy event, macro release, futures contract, swap tenor, convertible, ABS pool, or REIT project.
- Factor or rule definition: expected sign, economic intuition, rebalance frequency, holding horizon, data latency, and transaction-cost assumption.
- Labels or outcomes: total return, yield bp change, spread change, carry/rolldown, drawdown, redemption event, default/extension, policy event, or realized liquidity.
- Validation: time-series split, out-of-sample period, walk-forward test, turnover, slippage, liquidity filter, stale-price handling, robustness, false positives, and human review.
- Monitoring: alert threshold, update cycle, dashboard/report format, escalation rule, owner, and failure log.

## Framework

```text
FICC decision target
-> point-in-time data contract and entity mapping
-> domain factor family or agent workflow
-> label construction and horizon alignment
-> walk-forward validation with costs, liquidity, and stale-value checks
-> monitoring, human review, and audit trail
```

AI can accelerate parsing, routing, summarization, candidate generation, monitoring, and report drafting. It is not a source of data facts unless connected to verified data packets.

FICC-specific factor families:

- Macro surprise and policy reaction: actual/expected/previous value, release time, revision, priced-in level, and policy constraints.
- Funding liquidity: DR/R, NCD, repo volume, OMO/MLF, fiscal payment, leverage condition, and product liability.
- Curve and duration: level, slope, butterfly, carry, rolldown, term premium proxy, supply by tenor, and institution demand.
- Credit spread: spread percentile, rating/sector/tenor/region, liquidity, issuance, cancellation, maturity wall, refinancing, and default/extension events.
- Institution behavior: fund flow, wealth NAV, insurance premium, bank balance sheet, holdings, duration, leverage, and redemption feedback.
- Convertible and hybrid: parity zone, premium, bond floor, implied volatility, clause triggers, equity beta, credit quality, and liquidity.
- Offshore and derivatives: UST, FX hedge cost, cross-border funding, CTD, basis, IRR, DV01, margin, and roll.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `QA-01` | FICC quant research starts from PIT data contracts, release lag, frequency alignment, entity mapping, labels, costs, and validation. | Bond and macro datasets have asynchronous releases, revisions, sparse liquidity, changing universes, and stale valuations. | The workflow uses end-of-period data, revised data, or unavailable-at-decision fields. |
| `QA-02` | AI agents can parse, route, summarize, monitor, and generate candidates, but they are not market-data sources or autonomous investment decision makers. | LLM output is reasoning text unless grounded in verified data packets and human review. | The agent fabricates data, hides missing fields, or turns draft research into personal advice. |

## Analysis Steps

1. Define the FICC decision target and horizon.
2. Specify the PIT data contract: universe, entity keys, fields, timestamp, release lag, frequency, units, and source.
3. Map factor family to the relevant playbooks and claim ids in `references/16-source-claim-map.yml`.
4. Build labels that are observable after the decision point and aligned to the intended horizon.
5. Define factor, rule, prompt workflow, or agent pipeline with expected sign and failure mode.
6. Establish validation: walk-forward split, out-of-sample metrics, costs, turnover, liquidity, stale valuation, and robustness.
7. Define monitoring, alert escalation, human review, and audit trail.
8. If data or labels are missing, return required data and validation design instead of a performance claim.

## Output Overlay

```text
Playbooks used: quant-ai-research
Research question:
Data contract:
PIT and frequency checks:
FICC factor families:
Label and validation window:
Factor, rule, or agent workflow:
Validation design:
Monitoring plan:
Missing data:
Risks and counterexamples:
```

## Risk Checks

- Do not treat LLM summaries as data facts.
- Do not accept factor performance without out-of-sample validation.
- Check look-ahead bias, survivorship bias, point-in-time availability, release lag, data revision, and transaction costs.
- Check frequency mismatch: monthly macro data cannot be used as if it were daily-known before release.
- Check stale valuation, sparse trading, callable/putable terms, rating migration, default/extension events, and changing bond universes.
- Check entity mapping across bond code, issuer, parent company, rating, region, sector, fund, and product.
- Check whether labels are observable at decision time.
- Separate backtest research from production monitoring and human decision review.
- Keep human review for investment and risk decisions.

## Source Reports

- `huatai-quant-ai-ficc-2025`
- `cicc-ficc-ai-agent-path-2025`

## Claim IDs

- `QA-01`
- `QA-02`

## Search Keywords

FICC quant research, AI-assisted research, factor, agent, monitoring, Prompt, LLM, Data contract, backtest, out-of-sample, automated reporting
