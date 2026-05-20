# Convertible Hybrid

## Scope

Use this playbook for convertible bonds, exchangeable bonds, hybrid capital instruments, preferred shares, mixed notes, structured notes, and other equity-credit hybrid assets. The first implementation focuses on China convertible bonds and exchangeable bonds.

## When To Use

- The question mentions 可转债, 可交债, 平价, 转股溢价率, 债底, 下修, 赎回, 回售, 隐含波动率, or 混合型资产.
- The user asks whether convertible valuation should focus on parity premium, bond floor, equity beta, or clauses.
- The answer needs both equity option logic and credit downside protection.

## Required Inputs

- Convertible terms: conversion price, maturity, coupon, redemption, put, downward revision, guarantee, rating.
- Equity: underlying stock price, volatility, liquidity, valuation, earnings, sector beta.
- Bond floor: discount curve, credit spread, rating, recovery, liquidity.
- Valuation: parity, conversion premium, pure-bond value, option value, implied volatility, YTM.
- Flow and market: issuance, redemption pressure, fund holdings, market liquidity, style regime.

## Framework

Convertible analysis is a balance between equity upside, bond-floor protection, and clause path dependence:

```text
underlying stock and volatility
+ conversion terms and clauses
+ credit quality and bond floor
+ market liquidity and investor demand
-> parity / premium / bond floor / implied option value
-> strategy: equity beta, balanced, defensive, clause/event-driven, or avoid
```

Do not answer "看平价还是债底" as an either-or rule. In high parity, equity beta and redemption risk dominate. In low parity, bond floor, credit quality, put/downward revision, and liquidity dominate. In the middle zone, premium and option value decide risk-reward.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `CH-01` | 转债价值由正股弹性、债底保护、期权价值、信用质量、流动性和路径依赖条款共同决定。 | 股性、债性和条款在不同市场状态下切换主导权。 | 缺少平价、溢价率、债底、YTM、条款状态、评级或流动性数据。 |
| `CH-02` | 平价区间决定主要风险来源。 | 高平价偏正股和赎回，低平价偏债底/信用/流动性，中间区间偏溢价率和期权价值。 | 未控制平价区间就比较溢价率或策略收益。 |

## Analysis Steps

1. Classify the convertible: equity-like, balanced, debt-like, distressed, or clause-driven.
2. Compute or request parity, conversion premium, bond floor, YTM, and implied volatility.
3. Check underlying equity quality and volatility regime.
4. Check credit downside: issuer quality, guarantee, bond floor, liquidity, rating, maturity.
5. Check clauses: redemption trigger, put trigger, downward revision probability, call protection.
6. Match strategy to investor objective: equity beta, low-volatility carry, event-driven, relative value, or hedging.
7. For non-convertible hybrid assets, state the extension path and required data rather than overfitting convertible logic.

## Output Overlay

```text
使用 playbook: convertible-hybrid
资产类型:
估值拆解:
条款路径:
权益上行:
债性保护:
策略判断:
缺失数据:
风险与反例:
```

## Risk Checks

- Do not ignore forced redemption risk for high-parity convertibles.
- Do not treat bond floor as protection when credit or liquidity is impaired.
- Do not compare conversion premium without controlling for parity zone.
- Check whether downward revision is legally possible and incentive-compatible.
- For exchangeable and other hybrid assets, verify terms before applying convertible shortcuts.

## Source Reports

- `cicc-convertible-bonds-framework-2025`
- `huatai-convertible-framework-2025`
- `cicc-hybrid-assets-framework-2025`

## Claim IDs

- `CH-01`
- `CH-02`

## Search Keywords

可转债, 可交债, 平价, 转股溢价率, 债底, 隐含波动率, 下修, 赎回, 回售, 混合型资产, 优先股, 混合票据, 雪球
