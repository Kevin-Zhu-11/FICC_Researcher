# Financial Credit

## Scope

Use this playbook for bank capital bonds, Tier-2 capital bonds and perpetual bank bonds, TLAC, broker bonds, insurance subordinated bonds, and financial-sector credit bonds.

## When To Use

- The question mentions Tier-2 capital bonds and perpetual bank bonds, bank capital bonds, TLAC, broker bonds, insurance bonds, financial-sector, subordinated bonds, or capital instruments.
- The analysis needs both issuer credit and bond-term subordination.
- The user asks whether financial credit spreads compensate capital-tool risk.

## Required Inputs

- Bank: capital adequacy, core tier-1 ratio, asset quality, NPL, provision coverage, profitability, deposit stability.
- TLAC/capital tools: loss-absorption terms, subordination, extension, coupon deferral, write-down or conversion.
- Broker/insurance: leverage, liquidity, capital pressure, investment assets, underwriting or claims pressure.
- Market: spread by issuer type, rating, tenor, subordination, liquidity, investor demand.
- Regulation: capital rules, TLAC schedule, systemic-importance status, solvency rules.

## Framework

```text
issuer systemic role and fundamentals
+ regulatory capital need
+ capital instrument terms and subordination
+ investor demand and liquidity
+ relative spread versus senior debt and peers
-> financial-credit risk compensation
```

System importance can reduce default probability, but it does not remove subordination, extension, coupon, or loss-absorption risk.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `FC-01` | Financial-sector credit analysis must separate issuer credit from instrument-term risk. | Bank capital instruments such as Tier-2 capital bonds, perpetual bank bonds, TLAC, and subordinated debt introduce subordination, extension, deferral, write-down, conversion-to-equity, and supply pressure. | Missing terms, capital adequacy ratio, asset quality, call/redemption expectations, spreads, or liquidity data. |

## Analysis Steps

1. Classify issuer: bank, broker, insurer, leasing, AMC, or other financial.
2. Classify instrument: senior, subordinated, tier-2, perpetual, TLAC, or insurance capital tool.
3. Evaluate issuer fundamentals and regulatory pressure.
4. Read bond terms for loss absorption, extension, coupon, and ranking.
5. Compare spread against same issuer senior bonds, peer capital bonds, and rating/tenor buckets.
6. Check investor demand and liquidity.
7. State whether the trade is carry, spread compression, relative value, or should be avoided.

## Output Overlay

```text
Playbooks used: financial-credit
Issuer type:
Instrument terms:
Capital and asset quality:
Valuation and spreads:
Institution demand:
Strategy assessment:
Missing data:
Risks and counterexamples:
```

## Risk Checks

- Do not treat systemic importance as bond-level risk-free status.
- Distinguish senior issuer credit from subordinated capital-tool risk.
- Check coupon deferral, extension, write-down, and conversion terms.
- Check liquidity before assuming spread pickup is monetizable.
- Check regulatory schedule and issuance pressure before buying supply-heavy buckets.

## Source Reports

- `cicc-financial-credit-bonds-2025`
- `huatai-credit-bond-framework-2025`
- `huatai-institution-behavior-2025`

## Claim IDs

- `FC-01`

## Search Keywords

Tier-2 capital bonds and perpetual bank bonds, bank capital bonds, TLAC, financial-sectorCredit bonds, broker bonds, insurance bonds, subordinated bonds, perpetual bonds, capital adequacy ratio, loss absorption
