# Rates Macro

## Scope

Use this playbook for rates direction, yield-curve shape, macro-policy transmission, funding conditions, duration timing, and questions about government bonds, policy-bank bonds, NCDs, repo, monetary policy, fiscal supply, inflation, growth, and FX constraints.

## When To Use

- The question mentions 利率, 宏观, 曲线, 久期, 资金面, 央行, 财政供给, 汇率约束, 国债, 国开, 存单, or 低利率.
- The user asks whether yields should rise or fall.
- The user asks why traditional growth/inflation models are less effective in a low-rate regime.
- The question needs a macro-to-bond-pricing bridge rather than only a trading tactic.

## Required Inputs

- Growth: GDP, PMI, industrial production, credit impulse, social financing, property indicators.
- Inflation: CPI, PPI, commodity prices, service inflation, output gap proxies.
- Funding: DR007, R007, repo volume, NCD issuance and yields, deposit trends.
- Policy: OMO, MLF, LPR, reserve requirement ratio, policy statements, fiscal deficit and bond issuance plans.
- Supply: treasury issuance, local-government-bond issuance, policy-bank supply, maturity distribution.
- External: USD/CNH, DXY, UST yields, FX policy constraints.
- Market: CGB and CDB yield curves, curve slope, term premium proxy, futures basis if relevant.

## Framework

Start from the old IS-LM intuition: rates are the internal price of funds. Then translate it into the bond-market operating chain:

```text
growth / inflation / policy / fiscal supply / funding / FX
-> nominal growth and liquidity expectations
-> short-rate anchor and term premium
-> yield-curve level, slope, and volatility
-> duration and curve strategy
```

In a low-rate environment, do not mechanically apply "growth up = yields up" or "inflation down = yields down". CICC's low-rate framework emphasizes that fiscal behavior, industrial-chain pricing, risk appetite, and institutional liability constraints can dominate traditional macro variables. Huatai's debt-market framework also pushes the analyst to map macro theory into observable rates, supply, and investor behavior.

## Analysis Steps

1. Classify the question: level, slope, volatility, short-end funding, long-end duration, or macro regime.
2. Identify the dominant driver: growth, inflation, policy, fiscal supply, funding, FX, or investor demand.
3. Separate what is structural from what is current data.
4. Check short-end anchor first: repo, NCD, policy rate, and bank balance-sheet pressure.
5. Check long-end driver next: nominal growth expectation, fiscal supply, insurance and bank demand, term premium.
6. Compare curve segments: bull flattening, bull steepening, bear flattening, bear steepening.
7. If data is missing, stop at the mechanism and produce the missing-data block.

## Output Template

```text
使用 playbook: rates-macro
问题归类:
框架事实:
当前数据事实:
缺少数据:
利率方向判断:
曲线含义:
风险与反例:
后续跟踪指标:
```

## Risk Checks

- Do not infer current yield level from old broker examples.
- Check whether fiscal supply or special-bond issuance offsets weak growth.
- Check whether funding is loose only because demand is weak, not because risk appetite is improving.
- Check whether external-rate or FX constraints limit domestic easing.
- Check whether institutional demand is duration-seeking enough to absorb supply.

## Source Reports

- `cicc-low-rate-macro-bond-pricing-2025`
- `cicc-bond-principles-strategy-2025`
- `cicc-low-rate-investor-behavior-2025`
- `huatai-bond-market-framework-2025`
- `huatai-asset-allocation-framework-2025`

## Search Keywords

利率, 宏观, 低利率, 收益率曲线, 久期, 资金面, 央行, 财政供给, 通胀, 汇率, IS-LM, 国债, 国开, 存单
