# Credit Strategy

## Scope

Use this playbook for credit bonds, credit spreads, asset shortage, rating frameworks, spread compression, credit beta, credit selection, downgrade/default risk, and low-spread investment strategy. City investment bonds, financial credit bonds, and ABS have dedicated playbooks and should only be routed here for common credit logic.

## When To Use

- The question mentions Credit bonds, credit spreads, asset shortage, credit downshift, rating, default, extension, industrial bonds, LGFV, Tier-2 capital bonds and perpetual bank bonds, or coupon carry.
- The user asks how to earn return when spreads are low.
- The user needs a framework for credit risk, valuation, and investor-demand interaction.

## Required Inputs

- Market: credit spread by rating, sector, tenor, issuer type, liquidity bucket.
- Issuance: net financing, cancellation, maturity wall, refinancing availability.
- Risk: rating actions, default or extension events, financial statements, cash-flow pressure.
- Valuation: treasury curve, policy-bank curve, benchmark spread, liquidity premium.
- Demand: wealth management, funds, bank book, insurance, product flows.
- Instrument: bond terms, guarantee, collateral, put/call, covenants, subordination.

## Framework

Credit return is a combination of coupon, spread change, liquidity premium, and credit event risk. In a low-spread environment, the question is not only "can spreads compress further" but also:

```text
spread level
+ issuer fundamental cushion
+ liquidity and investor demand
+ refinancing and policy support
+ portfolio drawdown tolerance
-> whether coupon pickup compensates credit and liquidity risk
```

City investment, financial credit, and sector-specific credit require specialized extensions. This playbook handles the common layer: spread valuation, risk screening, and strategy selection.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `CR-01` | Credit spread allocation depends on spread level, issuer fundamentals, refinancing, liquidity, supply, and institution demand. | Spread is compensation for credit, liquidity, and technical risks, not a standalone return metric. | Spread, issuer, refinancing, and liquidity data are missing. |
| `CR-02` | low spreads and asset shortage do not prove issuer safety; carry is not risk-free. | Crowded demand can compress compensation while issuer and liquidity risks remain. | Current spreads still compensate risk and exit liquidity is verified. |

## Analysis Steps

1. Define the credit universe: rating, sector, tenor, issuer type, liquidity, and eligible instruments.
2. Separate return objective: coupon carry, spread compression, credit beta, relative value, or event-driven repair.
3. Check valuation: current spread percentile, spread versus historical and peer groups, liquidity premium.
4. Check fundamentals: cash flow, leverage, refinancing, ownership, support, and risk events.
5. Check technicals: issuance, maturities, wealth/fund demand, redemption risk, and dealer liquidity.
6. Use `references/09-data-interface-catalog.md` to identify required spread, issuer, issuance, rating, liquidity, and institution-demand data.
7. Use `references/11-research-decision-chains.md` for the credit-spread-to-allocation chain.
8. Choose strategy: stay high grade, selective sinking, short-duration carry, sector rotation, barbell, or avoid.
9. Document risks and data gaps before making any current-market conclusion.

## Output Overlay

```text
Playbooks used: credit-strategy
Credit question type:
Valuation and spreads:
Issuer and instrument fundamentals:
Institution demand and liquidity:
Strategy selection:
Missing data:
Risks and counterexamples:
```

## Risk Checks

- Do not use rating alone as a credit-risk conclusion.
- Do not recommend credit sinking when spread compensation and liquidity are both weak.
- Check whether low spreads reflect asset shortage rather than improved issuer fundamentals.
- Do not treat policy support or asset shortage as proof that weak issuers are safe.
- Do not treat coupon carry as risk-free return.
- Check whether wealth or fund redemption pressure could widen spreads suddenly.
- For city investment, financial credit, ABS, or REITs details, route to the specialized playbooks.

## Source Reports

- `cicc-credit-strategy-low-spread-2025`
- `huatai-credit-bond-framework-2025`
- `cicc-city-investment-bonds-2025`
- `cicc-financial-credit-bonds-2025`
- `huatai-institution-behavior-2025`

## Claim IDs

- `CR-01`
- `CR-02`

## Search Keywords

Credit bonds, credit spreads, asset shortage, credit downshift, rating, default, extension, industrial bonds, LGFV, Tier-2 capital bonds and perpetual bank bonds, coupon carry, credit strategy
