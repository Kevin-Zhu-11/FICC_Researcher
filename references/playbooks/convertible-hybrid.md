# Convertible Hybrid

## Scope

Use this playbook for convertible bonds, exchangeable bonds, hybrid capital instruments, preferred shares, mixed notes, structured notes, and other equity-credit hybrid assets. The first implementation focuses on China convertible bonds and exchangeable bonds.

## When To Use

- The question mentions convertible bonds, exchangeable bonds, parity, conversion premium, bond floor, downward conversion-price revision, redemption, put option, implied volatility, or hybrid assets.
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

Do not answer "whether to focus on parity or bond floor" as an either-or rule. In high parity, equity beta and redemption risk dominate. In low parity, bond floor, credit quality, put/downward revision, and liquidity dominate. In the middle zone, premium and option value decide risk-reward.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `CH-01` | Convertible value is jointly driven by underlying equity sensitivity, bond-floor protection, option value, credit quality, liquidity, and path-dependent clauses. | Equity-like exposure, bond-like exposure, and clauses take turns dominating under different market states. | Missing parity, premium, bond floor, YTM, clause status, rating, or liquidity data. |
| `CH-02` | The parity zone determines the main risk source. | High parity leans toward underlying equity and redemption risk; low parity leans toward bond floor, credit, and liquidity; the middle zone leans toward premium and option value. | Do not compare premiums or strategy returns without controlling for the parity zone. |

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
Playbooks used: convertible-hybrid
Asset type:
Valuation decomposition:
Clause path:
Equity upside:
Bond-like protection:
Strategy assessment:
Missing data:
Risks and counterexamples:
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

convertible bonds, exchangeable bonds, parity, conversion premium, bond floor, implied volatility, downward conversion-price revision, redemption, put option, hybrid assets, preferred shares, hybrid notes, snowball notes
