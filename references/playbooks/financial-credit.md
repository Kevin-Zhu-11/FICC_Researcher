# Financial Credit

## Scope

Use this playbook for bank capital bonds, 二永债, TLAC, broker bonds, insurance subordinated bonds, and financial-sector credit bonds.

## When To Use

- The question mentions 二永债, 银行资本债, TLAC, 券商债, 保险债, 大金融, 次级债, or 资本工具.
- The analysis needs both issuer credit and bond-term subordination.
- The user asks whether financial credit spreads compensate capital-tool risk.

## Required Inputs

- Bank: capital adequacy, core tier-1 ratio, asset quality, NPL, provision coverage, profitability, deposit stability.
- TLAC/capital tools: loss-absorption terms, subordination, extension, coupon deferral, write-down or conversion.
- Broker/insurance: leverage, liquidity, capital pressure, investment assets, underwriting or claims pressure.
- Market: spread by issuer type, rating, tenor, subordination, liquidity, investor demand.
- Regulation: capital rules, TLAC schedule, systemic-importance status, solvency rules.

## Framework

```text
issuer systemic role and fundamentals
+ regulatory capital need
+ capital instrument terms and subordination
+ investor demand and liquidity
+ relative spread versus senior debt and peers
-> financial-credit risk compensation
```

System importance can reduce default probability, but it does not remove subordination, extension, coupon, or loss-absorption risk.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `FC-01` | 大金融信用债必须区分主体信用和工具条款风险。 | 二永债、TLAC、次级债等资本工具引入次级性、延期、递延、减记、转股和供给压力。 | 缺少条款、资本充足率、资产质量、赎回预期、利差和流动性数据。 |

## Analysis Steps

1. Classify issuer: bank, broker, insurer, leasing, AMC, or other financial.
2. Classify instrument: senior, subordinated, tier-2, perpetual, TLAC, or insurance capital tool.
3. Evaluate issuer fundamentals and regulatory pressure.
4. Read bond terms for loss absorption, extension, coupon, and ranking.
5. Compare spread against same issuer senior bonds, peer capital bonds, and rating/tenor buckets.
6. Check investor demand and liquidity.
7. State whether the trade is carry, spread compression, relative value, or should be avoided.

## Output Overlay

```text
使用 playbook: financial-credit
主体类型:
工具条款:
资本与资产质量:
估值与利差:
机构需求:
策略判断:
缺失数据:
风险与反例:
```

## Risk Checks

- Do not treat systemic importance as bond-level risk-free status.
- Distinguish senior issuer credit from subordinated capital-tool risk.
- Check coupon deferral, extension, write-down, and conversion terms.
- Check liquidity before assuming spread pickup is monetizable.
- Check regulatory schedule and issuance pressure before buying supply-heavy buckets.

## Source Reports

- `cicc-financial-credit-bonds-2025`
- `huatai-credit-bond-framework-2025`
- `huatai-institution-behavior-2025`

## Claim IDs

- `FC-01`

## Search Keywords

二永债, 银行资本债, TLAC, 大金融信用债, 券商债, 保险债, 次级债, 永续债, 资本充足率, 损失吸收
