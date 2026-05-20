# City Investment Bonds

## Scope

Use this playbook for 城投债, 化债, 区域利差, 平台转型, 隐性债务, refinancing pressure, and local-government support analysis.

## When To Use

- The question mentions 城投, 化债, 区域利差, 平台, 隐债, 特殊再融资债, 土地财政, or 城投转型.
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

化债 improves refinancing visibility for some regions and issuers, but it does not make every platform risk-free. Treat policy support as one input, not as a substitute for debt-service capacity.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `CI-01` | 城投债分析必须同时看区域财政、债务压力、平台功能、现金流、再融资、政策支持、估值和流动性。 | 化债改善再融资能见度，但最终偿付能力仍取决于区域与主体现金流、融资通道和市场补偿。 | 缺少区域财政、主体现金流、债务期限、当前利差或再融资数据。 |

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
使用 playbook: city-investment-bonds
区域与主体:
区域财政和债务压力:
平台功能与现金流:
再融资和化债路径:
估值与区域利差:
策略判断:
缺失数据:
风险与反例:
```

## Risk Checks

- Do not use administrative level alone as credit quality.
- Do not equate 化债 policy with full guarantee for all issuers.
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

城投债, 化债, 区域利差, 财政自给率, 债务率, 隐性债务, 特殊再融资债, 平台转型, 再融资
