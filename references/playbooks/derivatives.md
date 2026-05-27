# Derivatives

## Scope

Use this playbook for China government-bond futures, interest-rate swaps, basis, IRR, hedging, curve trading, and interest-rate options.

## When To Use

- The question mentions China government bond futures, interest-rate swaps, IRS, basis, IRR, CTD, hedging, DV01, options, or curve hedging.
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

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `DER-01` | Derivatives decisions must review cash-bond exposure, funding conditions, futures/swap pricing, basis/DV01, hedging objective, margin, and liquidity together. | Derivatives change risk shape, but introduce basis, bond-switching, rollover, margin, funding, and model risk. | Missing CTD, conversion factor, IRR, repo, DV01, margin, or hedging objective. |

## Analysis Steps

1. Define objective: hedge, directional view, curve trade, basis trade, or relative value.
2. Map cash exposure into duration, key-rate DV01, and liquidity.
3. For futures, identify CTD, conversion factor, basis, IRR, implied repo, and delivery option.
4. For swaps, identify swap tenor, floating leg, fixing risk, collateral, and DV01.
5. Compare derivative exposure with cash-bond exposure.
6. State implementation risk: margin, funding, liquidity, roll, delivery, and hedge slippage.
7. If current market data is missing, provide required fields instead of trade conclusions.

## Output Overlay

```text
Playbooks used: derivatives
Trading or hedging objective:
Cash-bond risk exposure:
Derivative pricing metrics:
Basis or swap-curve view:
Hedge ratio or strategy path:
Missing data:
Risks and counterexamples:
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

## Claim IDs

- `DER-01`

## Search Keywords

China government bond futures, interest-rate swaps, IRS, basis, IRR, CTD, conversion factor, DV01, hedging, options, repo, swap curve
