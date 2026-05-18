# Wealth Management Funds

## Scope

Use this playbook for bank wealth management products, net-value transformation, redemption pressure, 固收+ funds, mutual fund behavior, product liabilities, NAV drawdown, and portfolio feedback loops.

## When To Use

- The question mentions 银行理财, 净值化, 赎回, 固收+, 公募基金, 基金久期, 基金杠杆, 产品负债端, or 破净.
- The analysis needs to explain how product liabilities affect credit bonds, short-end rates, fund flows, or forced selling.
- The user provides NAV, holdings, duration, leverage, or redemption data.

## Required Inputs

- Product: NAV, drawdown, share, subscription/redemption, investor type, open/closed period, risk level.
- Portfolio: duration, leverage, cash buffer, asset allocation, rating distribution, issuer concentration, liquidity buckets.
- Market: credit spreads, short-end rates, repo funding, NCD, turnover, bid-ask spread.
- Behavior: redemption flow, ranking pressure, product migration, wealth channel demand.
- Fund: fund shares, duration, leverage, holdings, performance, redemption, benchmark.

## Framework

```text
liability stability
+ NAV drawdown and product liquidity terms
+ holdings liquidity and valuation sensitivity
+ duration, leverage, and credit exposure
+ investor redemption behavior
-> selling pressure, spread movement, short-end funding demand, and feedback loops
```

Net-value products transmit market volatility to investors faster than old expected-return products. Redemption pressure can force selling of liquid assets first, not necessarily the riskiest assets first.

## Analysis Steps

1. Identify product type: bank wealth, cash-like product, fixed-income fund, 固收+, or hybrid.
2. Check liability stability and redemption terms.
3. Check NAV drawdown, recent performance, and investor behavior.
4. Map holdings into rates, credit, cash, NCD, funds, convertibles, and liquidity buckets.
5. Assess whether selling pressure hits short-end rates, credit bonds, or liquid high-grade assets.
6. Combine with `institution-behavior.md` and `credit-strategy.md` when market impact is needed.
7. State missing data before making current redemption conclusions.

## Output Template

```text
使用 playbook: wealth-management-funds
产品类型:
负债端状态:
持仓与流动性:
净值和赎回反馈:
对债市影响:
缺失数据:
风险与反例:
```

## Risk Checks

- Do not treat product return as full holdings information.
- Do not assume redemption pressure only sells risky credit; liquid rates and high-grade credit may be sold first.
- Check open period and investor type before inferring redemption intensity.
- Check duration and leverage before judging rate sensitivity.
- Distinguish bank wealth products from mutual funds and insurance products.

## Source Reports

- `cicc-wealth-management-net-value-2025`
- `cicc-fixed-income-plus-fund-framework-2025`
- `huatai-institution-behavior-2025`
- `cicc-low-rate-investor-behavior-2025`

## Search Keywords

银行理财, 净值化, 赎回, 固收+, 公募基金, 基金久期, 杠杆, 负债端, 破净, 现金管理
