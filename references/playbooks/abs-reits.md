# ABS REITs

## Scope

Use this playbook for asset-backed securities, structured credit, public REITs, asset-pool cash flow, tranche design, credit enhancement, valuation, and liquidity.

## When To Use

- The question mentions ABS, asset securitization, public REITs, underlying assets, cash flow, tranching, credit enhancement, NOI, distribution yield, or project valuation.
- The analysis needs to understand cash-flow structure rather than only issuer credit.
- The user provides asset-pool, REITs operation, or tranche data.

## Required Inputs

- ABS: asset pool, cash-flow waterfall, tranche priority, enhancement, servicer, default/prepayment, historical performance.
- REITs: underlying asset, NOI, occupancy, rent, capex, distribution, leverage, sponsor, valuation, secondary-market liquidity.
- Market: rates curve, credit spread, liquidity premium, comparable yield, trading volume, discount/premium.
- Legal/structure: true sale, bankruptcy remoteness, covenants, triggers, guarantee, disclosure.

## Framework

```text
underlying asset quality
+ cash-flow stability and waterfall
+ structural enhancement and legal isolation
+ interest-rate and credit valuation
+ secondary liquidity and investor demand
-> tranche or REITs risk-return assessment
```

Structured priority reduces some risks but does not remove asset-pool, servicer, prepayment, legal, or liquidity risk.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `ABS-01` | ABS/REITs analysis must start from underlying assets or project cash flow, tranching/distribution mechanisms, legal structure, valuation, liquidity, and investor demand. | Structural priority reallocates risk; it does not eliminate asset, operating, prepayment, legal, valuation, or liquidity risk. | Missing asset pool, cash flow, waterfall, NOI, valuation, discount/premium, or liquidity data. |

## Analysis Steps

1. Classify asset: ABS tranche, project REIT, infrastructure REIT, or other structured product.
2. Identify cash-flow source and asset performance drivers.
3. Check structure: waterfall, subordination, enhancement, trigger, and legal isolation.
4. Assess valuation against rates, credit spread, distribution yield, and comparable products.
5. Check liquidity and investor base.
6. State whether risk comes mainly from asset performance, structure, rates, or liquidity.
7. If pool or project data is missing, avoid current valuation conclusions.

## Output Overlay

```text
Playbooks used: abs-reits
Asset type:
Underlying assets and cash flow:
Structure and credit enhancement:
Valuation and liquidity:
Strategy assessment:
Missing data:
Risks and counterexamples:
```

## Risk Checks

- Do not treat senior tranche as risk-free.
- Check prepayment, default, servicer, and concentration risk.
- For REITs, distinguish operation risk from rates-driven valuation risk.
- Check disclosure frequency and liquidity.
- Do not compare REITs distribution yield with bond yield without growth, capex, and asset-value assumptions.

## Source Reports

- `cicc-abs-framework-2025`
- `cicc-public-reits-strategy-2025`
- `huatai-credit-bond-framework-2025`

## Claim IDs

- `ABS-01`

## Search Keywords

ABS, asset securitization, public REITs, underlying assets, cash flow, tranching, credit enhancement, NOI, distribution yield, valuation, liquidity
