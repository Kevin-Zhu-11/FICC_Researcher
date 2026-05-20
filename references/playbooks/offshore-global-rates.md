# Offshore Global Rates

## Scope

Use this playbook for US Treasuries, global rates, Chinese USD bonds, dim sum bonds, offshore RMB bonds, FX constraints, hedge cost, and cross-border funding.

## When To Use

- The question mentions 美债, 美国国债, UST, 美联储, 中资美元债, 点心债, 离岸人民币债, offshore, USD/CNH, or 套保成本.
- The answer needs to separate global rates risk from issuer credit risk.
- The user asks about cross-border relative value or offshore funding.

## Required Inputs

- Global rates: UST curve, Fed path, inflation, employment, term premium, real yields.
- FX: DXY, USD/CNH, hedge cost, basis, capital-flow pressure.
- Offshore credit: issuer rating, spread, bond terms, guarantee, standby letter of credit, liquidity.
- Onshore comparison: onshore curve, domestic issuer spread, funding alternatives.
- Policy: cross-border issuance rules, RMB internationalization, offshore liquidity, regulatory changes.

## Framework

```text
global risk-free curve
+ Fed path and term premium
+ FX and hedge cost
+ issuer credit and offshore bond terms
+ onshore/offshore funding substitution
+ market liquidity
-> offshore rates or credit valuation
```

Do not transfer an onshore credit conclusion directly to offshore bonds. Offshore instruments add currency, legal, liquidity, rating, and cross-border-policy layers.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `OFF-01` | 离岸估值必须拆成全球无风险利率、Fed path、FX/套保、主体信用、法律条款、跨境政策和流动性。 | 离岸债券叠加币种、法律、评级、流动性和跨境融资约束，不能直接套用境内信用结论。 | 缺少 UST、汇率、套保成本、离岸利差、条款和流动性数据。 |

## Analysis Steps

1. Classify instrument: UST, Chinese USD bond, dim sum bond, offshore RMB rate bond, or offshore credit.
2. Separate rates component, FX/hedge component, issuer credit component, and liquidity component.
3. Compare onshore and offshore alternatives only after currency and hedge costs.
4. Check bond terms, guarantee structure, rating, and legal ranking.
5. Assess investor base and liquidity.
6. State whether the analysis is macro rates, credit spread, FX carry, or relative value.
7. Return missing-data block if current yields, spreads, or FX data are unavailable.

## Output Overlay

```text
使用 playbook: offshore-global-rates
资产类型:
全球利率因素:
汇率和套保成本:
主体信用与条款:
境内外相对价值:
缺失数据:
风险与反例:
```

## Risk Checks

- Do not apply onshore implicit-support assumptions directly to offshore debt.
- Distinguish USD rate movement from issuer spread movement.
- Check FX hedge cost before claiming yield advantage.
- Check liquidity and legal terms.
- Check whether quoted spread is stale or based on illiquid trading.

## Source Reports

- `cicc-us-treasuries-framework-2025`
- `cicc-offshore-credit-usd-dim-sum-2025`
- `cicc-offshore-rmb-bonds-2025`

## Claim IDs

- `OFF-01`

## Search Keywords

美债, UST, Fed, 美联储, 中资美元债, 点心债, 离岸人民币债, USD/CNH, 套保成本, offshore, hedge cost
