# Offshore Global Rates

## Scope

Use this playbook for US Treasuries, global rates, Chinese USD bonds, dim sum bonds, offshore RMB bonds, FX constraints, hedge cost, and cross-border funding.

## When To Use

- The question mentions U.S. Treasuries, U.S. Treasuries, UST, Fed, ChineseUSD bonds, dim sum bonds, offshore RMB bonds, offshore, USD/CNH, or hedging cost.
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
| `OFF-01` | Offshore valuation must decompose global risk-free rates, Fed path, FX/hedging, issuer credit, legal terms, cross-border policy, and liquidity. | Offshore bonds add currency, legal, rating, liquidity, and cross-border financing constraints; do not directly reuse onshore credit conclusions. | Missing UST, FX, hedging cost, offshore spreads, terms, or liquidity data. |

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
Playbooks used: offshore-global-rates
Asset type:
Global rates factors:
FX and hedging cost:
Issuer credit and terms:
Onshore-offshore relative value:
Missing data:
Risks and counterexamples:
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

U.S. Treasuries, UST, Fed, Fed, ChineseUSD bonds, dim sum bonds, offshore RMB bonds, USD/CNH, hedging cost, offshore, hedge cost
