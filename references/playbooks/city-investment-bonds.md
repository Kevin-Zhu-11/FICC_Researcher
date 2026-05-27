# City Investment Bonds

## Scope

Use this playbook for LGFV bonds, debt-resolution policy, regional spreads, platform transformation, implicit debt, refinancing pressure, and local-government support analysis.

## When To Use

- The question mentions LGFV, debt-resolution policy, regional spreads, platform, implicit debt, special refinancing bonds, land-finance model, or LGFV transformation.
- The answer needs to separate regional fiscal support from issuer-level cash-flow risk.
- The user asks whether policy support changes credit-risk compensation.

## Required Inputs

- Region: fiscal revenue, fiscal self-sufficiency, transfer payments, debt ratio, hidden-debt pressure, land-sale revenue.
- Issuer: business role, public-service function, operating cash flow, financing cash flow, bank credit line, shareholder support.
- Bonds: maturity wall, coupon, rating, guarantee, collateral, use of proceeds, secondary-market spread.
- Policy: debt-resolution tools, special refinancing bonds, local-government support statements, restructuring events.
- Market: regional spread, rating spread, issuance success, cancellation, turnover, institutional demand.

## Framework

```text
regional fiscal capacity
+ debt pressure and hidden-debt resolution path
+ issuer platform function and cash-flow quality
+ refinancing channel and policy support
+ market valuation and liquidity
-> regional spread and issuer-specific credit compensation
```

debt-resolution policy improves refinancing visibility for some regions and issuers, but it does not make every platform risk-free. Treat policy support as one input, not as a substitute for debt-service capacity.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `CI-01` | LGFV-bond analysis must review regional fiscal position, debt pressure, platform function, cash flow, refinancing, policy support, valuation, and liquidity together. | Debt-resolution policy improves refinancing visibility, but final debt-service capacity still depends on regional and issuer cash flow, financing channels, and market compensation. | Missing regional fiscal position, issuer cash flow, debt maturity profile, current spreads, or refinancing data. |

## Analysis Steps

1. Identify region, administrative level, issuer role, and bond type.
2. Assess regional fiscal capacity and debt pressure.
3. Assess issuer function, cash flow, financing access, and asset quality.
4. Check refinancing path: bank credit, public bonds, special refinancing, asset disposal, restructuring risk.
5. Compare regional spread with fiscal pressure and policy support.
6. State whether the opportunity is regional beta, issuer selection, maturity selection, or avoid.
7. If current spreads or issuer data are missing, return the missing-data block.

## Output Overlay

```text
Playbooks used: city-investment-bonds
Region and issuer:
Regional fiscal position and debt pressure:
Platform function and cash flow:
Refinancing and debt-resolution path:
Valuation and regional spread:
Strategy assessment:
Missing data:
Risks and counterexamples:
```

## Risk Checks

- Do not use administrative level alone as credit quality.
- Do not equate debt-resolution policy policy with full guarantee for all issuers.
- Check whether debt-resolution pressure shifts risk from public bonds to non-standard debt or suppliers.
- Check whether land-sale weakness undermines fiscal support.
- Distinguish short-term refinancing relief from long-term business transformation.

## Source Reports

- `cicc-city-investment-bonds-2025`
- `huatai-credit-bond-framework-2025`
- `cicc-credit-strategy-low-spread-2025`

## Claim IDs

- `CI-01`

## Search Keywords

LGFV bonds, debt-resolution policy, regional spreads, fiscal self-sufficiency ratio, debt ratio, implicit debt, special refinancing bonds, platform transformation, refinancing
