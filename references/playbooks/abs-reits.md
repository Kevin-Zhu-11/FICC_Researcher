# ABS REITs

## Scope

Use this playbook for asset-backed securities, structured credit, public REITs, asset-pool cash flow, tranche design, credit enhancement, valuation, and liquidity.

## When To Use

- The question mentions ABS, 资产证券化, 公募 REITs, 底层资产, 现金流, 分层, 增信, NOI, 分派率, or 项目估值.
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

## Analysis Steps

1. Classify asset: ABS tranche, project REIT, infrastructure REIT, or other structured product.
2. Identify cash-flow source and asset performance drivers.
3. Check structure: waterfall, subordination, enhancement, trigger, and legal isolation.
4. Assess valuation against rates, credit spread, distribution yield, and comparable products.
5. Check liquidity and investor base.
6. State whether risk comes mainly from asset performance, structure, rates, or liquidity.
7. If pool or project data is missing, avoid current valuation conclusions.

## Output Template

```text
使用 playbook: abs-reits
资产类型:
底层资产和现金流:
结构和增信:
估值与流动性:
策略判断:
缺失数据:
风险与反例:
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

## Search Keywords

ABS, 资产证券化, 公募REITs, 底层资产, 现金流, 分层, 增信, NOI, 分派率, 估值, 流动性
