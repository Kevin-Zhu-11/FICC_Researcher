# Derivatives

## Scope

Use this playbook for China government-bond futures, interest-rate swaps, basis, IRR, hedging, curve trading, and interest-rate options.

## When To Use

- The question mentions 国债期货, 利率互换, IRS, 基差, IRR, CTD, 套保, DV01, 期权, or 曲线对冲.
- The answer needs to distinguish directional trading from hedging.
- The user asks how derivatives connect with cash bonds and funding costs.

## Required Inputs

- Futures: contract price, deliverable basket, CTD, conversion factor, basis, IRR, implied repo, open interest, liquidity.
- Cash bonds: yield curve, cheapest deliverable candidates, duration, DV01, repo eligibility.
- Funding: repo rate, financing haircut, margin, funding stability.
- Swaps: swap curve, fixing rate, floating leg convention, DV01, collateral and counterparty rules.
- Objective: hedge ratio, target duration, accounting treatment, risk budget, stop-loss rules.

## Framework

```text
cash-bond curve
+ funding cost and repo condition
+ futures or swap pricing
+ basis / IRR / DV01
+ hedge objective and liquidity
-> directional trade, curve trade, basis trade, or hedge
```

Derivatives can reduce or transform exposure, but they also add margin, basis, liquidity, and model risk.

## Analysis Steps

1. Define objective: hedge, directional view, curve trade, basis trade, or relative value.
2. Map cash exposure into duration, key-rate DV01, and liquidity.
3. For futures, identify CTD, conversion factor, basis, IRR, implied repo, and delivery option.
4. For swaps, identify swap tenor, floating leg, fixing risk, collateral, and DV01.
5. Compare derivative exposure with cash-bond exposure.
6. State implementation risk: margin, funding, liquidity, roll, delivery, and hedge slippage.
7. If current market data is missing, provide required fields instead of trade conclusions.

## Output Template

```text
使用 playbook: derivatives
交易/套保目标:
现券风险敞口:
衍生品定价指标:
基差或互换曲线判断:
对冲比例/策略路径:
缺失数据:
风险与反例:
```

## Risk Checks

- Do not mix a hedge objective with a directional trade recommendation.
- Check margin and liquidity before suggesting futures or swaps.
- Check basis risk and CTD switch risk.
- Check repo funding before relying on IRR or basis convergence.
- Check contract roll and delivery timing.

## Source Reports

- `cicc-interest-rate-derivatives-2025`
- `huatai-bond-market-framework-2025`

## Search Keywords

国债期货, 利率互换, IRS, 基差, IRR, CTD, 转换因子, DV01, 套保, 期权, repo, swap curve
