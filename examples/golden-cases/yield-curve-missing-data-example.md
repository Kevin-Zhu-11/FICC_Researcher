# Yield Curve Missing Data Example

## Prompt

Review the current 1Y/3Y/5Y/10Y/30Y CGB and CDB curves. If live curve, funding, supply, and institution data are unavailable, provide only framework judgment and required additional data.

## Missing Fields

```text
Currently missing data:
- Fields: 1Y/3Y/5Y/7Y/10Y/30Y CGB curve, CDB or policy-bank curve, DR007/R007, NCD rates, government-bond issuance and payment settlement, allocation-account demand, and China government bond futures basis.
- Recommended sources: ChinaBond, CFETS, SHCH, NIFC, Wind, iFinD, local bond database, user-provided exports.
- Time range: Current trading day and at least one comparison date.
- Frequency: Daily frequency; funding conditions and crowded-positioning indicators may use higher-frequency data.
- Use: Assess curve segmentation, tenor spreads, funding anchor, supply shock, allocation absorption, and portfolio risk.
Until these fields are available, provide framework-only analysis and do not make current-market conclusions.
```

## Allowed Framework Analysis

- Explain how short end depends on funding, central-bank operations, NCD pressure, and bank liability constraints.
- Explain how 3Y-7Y depends on carry, rolldown, allocation demand, and macro expectations.
- Explain how 10Y and 30Y depend on growth expectations, fiscal supply, insurer demand, term premium, and crowded positioning.
- State that weak macro data can be rates-friendly but may be offset by supply, policy expectations, or valuation.

## Forbidden Claims

- Do not give current curve levels without current source and timestamp.
- Do not say 10Y or 30Y must go down because data is weak.
- Do not recommend leverage without repo, NCD, product-liability, and liquidity data.
- Do not infer CDB or credit spreads from treasury levels alone.

## Expected Answer Shape

```text
Curve data sources:
Tenor segmentation:
Short-end drivers:
Belly drivers:
Long-end drivers:
Supply-demand and institution behavior:
Available strategies:
Missing data:
Risk triggers:
```
