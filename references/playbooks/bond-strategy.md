# Bond Strategy

## Scope

Use this playbook for portfolio construction, duration, curve, leverage, carry, rolldown, coupon income, spread capture, secondary-market relative value, and expected holding-period return for China fixed-income portfolios.

## When To Use

- The user asks "债券怎么做收益", "久期怎么摆", "曲线怎么交易", "信用利差低位怎么做", or "组合如何构建".
- The answer requires connecting macro, supply, investor demand, yield curve, credit spread, leverage, and portfolio constraints.
- The question is about strategy implementation rather than only macro direction.

## Required Inputs

- Portfolio: current holdings, benchmark, duration, leverage, liquidity limits, rating limits, concentration limits.
- Market: treasury and policy-bank curves, credit spreads, repo funding, NCD, futures basis.
- Return components: coupon, carry, rolldown, price change, credit spread change, funding cost.
- Constraints: drawdown limit, liquidity buffer, accounting category, regulatory or mandate restrictions.
- Supply and demand: government-bond issuance, credit issuance, fund flow, bank and insurance demand.

## Framework

CICC's bond-portfolio framework can be reconstructed as:

```text
macro regime + funding liquidity + regulatory policy
+ bond supply + investor demand + product constraints
-> curve level and shape
-> credit spreads and liquidity premium
-> duration / curve / leverage / credit allocation
-> holding-period return and drawdown risk
```

Strategy should be stated as conditional scenarios, not as a single unconditional trade. The same low-yield level can imply different choices depending on carry, funding stability, valuation cushion, redemption risk, and policy volatility.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `BS-01` | Portfolio actions require scenario, trigger, return path, loss path, and stop condition. | The same market view has different implications under different mandates, accounting, liquidity, and drawdown budgets. | Portfolio constraints or current market data are missing. |
| `BS-02` | Carry and rolldown become usable return only after funding, liquidity, liability, and drawdown checks. | Funding cost, redemption risk, mark-to-market pressure, and liquidity can erase coupon/carry gains. | Funding and product-liability data are absent or unstable. |

## Analysis Steps

1. Define the investor and mandate: bank book, fund, wealth product, insurance, proprietary book, or absolute-return portfolio.
2. Decompose expected return into coupon, carry, rolldown, spread compression, and price change.
3. Assess funding cost and leverage stability before recommending leverage or carry trades.
4. Analyze curve opportunity by segment: short-end funding anchor, belly rolldown, long-end duration beta.
5. Compare rates versus credit: whether spread pickup compensates liquidity and credit risk.
6. Evaluate supply-demand balance and likely marginal buyer.
7. Use `references/09-data-interface-catalog.md` to identify required curve, funding, spread, supply, and portfolio fields.
8. Use `references/11-research-decision-chains.md` when the strategy depends on macro release, funding, fiscal supply, or institution behavior.
9. Translate into a portfolio action, scenario trigger, and stop condition with `references/06-portfolio-action-policy.md`.

## Output Overlay

```text
使用 playbook: bond-strategy
投资者/组合约束:
收益来源拆解:
可用策略:
缺失数据:
当前只能确认的部分:
组合动作:
风险控制:
跟踪指标:
```

## Risk Checks

- Do not recommend leverage without checking funding cost and stability.
- Do not treat carry as free return when redemption, liquidity, or mark-to-market pressure is high.
- Do not use spread pickup without issuer, rating, liquidity, and concentration checks.
- Check whether curve steepness comes from supply pressure rather than attractive rolldown.
- Do not state current curve, funding, spread, or portfolio metrics without a data packet or user-provided data.
- Distinguish trading book mark-to-market risk from hold-to-maturity accounting.
- Always state what happens if the rate view is wrong: loss channel, trigger, and de-risking action.

## Source Reports

- `cicc-bond-principles-strategy-2025`
- `cicc-low-rate-macro-bond-pricing-2025`
- `cicc-low-rate-investor-behavior-2025`
- `huatai-bond-market-framework-2025`
- `huatai-asset-allocation-framework-2025`
- `huatai-fixed-income-framework-2025`

## Claim IDs

- `BS-01`
- `BS-02`

## Search Keywords

债券策略, 组合构建, 久期, 曲线, 杠杆, 骑乘, 套息, 持有回报, 票息, 二级价差, 收益率曲线
