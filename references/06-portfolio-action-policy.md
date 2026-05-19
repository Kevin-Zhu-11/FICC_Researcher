# Portfolio Action Policy

Use this file when the user asks for portfolio action, not only market explanation.

## When To Use

- 久期怎么摆
- 曲线怎么做
- 要不要加杠杆
- 利率债和信用债怎么配
- 如果判断错了怎么止损
- 某个宏观或政策事件对组合有什么动作含义

## Required Inputs

- Portfolio: current duration, benchmark duration, leverage, cash ratio, liquidity buffer.
- Mandate: max drawdown, rating floor, concentration limit, accounting category, benchmark.
- Market: treasury curve, policy-bank curve, credit spreads, repo/NCD funding, futures basis.
- Return components: coupon, carry, rolldown, spread change, capital gain/loss, funding cost.
- Risk budget: maximum acceptable loss under rate up/down scenarios and spread widening.

## Action Translation

Convert research judgment into a scenario table:

```text
情景:
触发条件:
组合动作:
久期:
曲线:
杠杆:
信用仓位:
预期收益来源:
主要亏损路径:
止盈/止损/降风险条件:
需要补充的数据:
```

## Duration Rules

- State whether action is duration-up, duration-down, neutral, or barbell.
- Name the segment: 1Y, 3Y, 5Y, 7Y, 10Y, 30Y, or policy-bank bucket.
- Explain whether the view comes from level, slope, rolldown, or hedge demand.
- If data is missing, describe the condition for action instead of recommending action.

## Curve Rules

- Identify bull steepening, bull flattening, bear steepening, or bear flattening.
- Separate short-end funding anchor from long-end supply, insurance demand, and term premium.
- Do not call a curve trade attractive without checking carry and rolldown.

## Leverage Rules

- Never recommend leverage without checking repo funding, liquidity, redemption risk, and margin pressure.
- State whether leverage return comes from carry, rolldown, spread compression, or curve view.
- Include a funding-cost break-even.

## Credit Allocation Rules

- Translate credit view into rating, sector, tenor, liquidity, and issuer-type limits.
- Avoid "credit sinking" language unless spread compensation and exit liquidity are adequate.
- If spreads are low, prefer explicit risk budget and liquidity buffer.

## Source Reports

- `cicc-bond-principles-strategy-2025`
- `huatai-fixed-income-framework-2025`
- `huatai-bond-market-framework-2025`
