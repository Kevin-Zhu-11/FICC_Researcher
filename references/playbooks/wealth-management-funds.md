# Wealth Management Funds

## Scope

Use this playbook for bank wealth management products, net-value transformation, redemption pressure, fixed-income-plus funds, mutual fund behavior, product liabilities, NAV drawdown, and portfolio feedback loops.

## When To Use

- The question mentions bank wealth management products, net-value transformation, redemption, fixed-income-plus, mutual funds, fund duration, fund leverage, product liability side, or NAV below par.
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

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `WM-01` | Net-value wealth products and funds create feedback through NAV drawdowns, subscriptions/redemptions, liquidity management, and forced selling. | Investor behavior and open/closed product terms transmit market volatility into asset disposal and spread/curve pressure. | Missing product size, NAV, subscriptions/redemptions, holdings, duration, leverage, or liquidity-bucket data. |

## Analysis Steps

1. Identify product type: bank wealth, cash-like product, fixed-income fund, fixed-income-plus, or hybrid.
2. Check liability stability and redemption terms.
3. Check NAV drawdown, recent performance, and investor behavior.
4. Map holdings into rates, credit, cash, NCD, funds, convertibles, and liquidity buckets.
5. Assess whether selling pressure hits short-end rates, credit bonds, or liquid high-grade assets.
6. Combine with `institution-behavior.md` and `credit-strategy.md` when market impact is needed.
7. State missing data before making current redemption conclusions.

## Output Overlay

```text
Playbooks used: wealth-management-funds
Product type:
Liability-side condition:
Holdings and liquidity:
NAV and redemption feedback:
Impact on the bond market:
Missing data:
Risks and counterexamples:
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

## Claim IDs

- `WM-01`

## Search Keywords

bank wealth management products, net-value transformation, redemption, fixed-income-plus, mutual funds, fund duration, Leverage, liability side, NAV below par, cash management
