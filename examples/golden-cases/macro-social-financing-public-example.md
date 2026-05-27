# Macro Social Financing Public Example

## Prompt

Use ficc-researcher to analyze how a social-financing and money-supply dataset affects the bond market. The data packet is at `examples/data/macro-social-financing-public-sample.yml`. If yield, spread, funding-rate, or market-expectation data is missing, provide only framework-based judgment and a gap list.

## Files The Agent Should Read

- `SKILL.md`
- `references/00-routing.md`
- `references/02-data-source-policy.md`
- `references/03-data-integration-policy.md`
- `references/07-macro-indicator-glossary.md`
- `references/08-policy-reaction-function.md`
- `references/09-data-interface-catalog.md`
- `references/10-workflow-entrypoints.md`
- `references/11-research-decision-chains.md`
- `references/12-data-connector-mapping.md`
- `references/playbooks/rates-macro.md`
- `references/playbooks/bond-strategy.md`
- `assets/templates/macro-data-commentary-template.md`

## Data Packet

Use `examples/data/macro-social-financing-public-sample.yml`.

The packet is synthetic and desensitized. A good answer must label it as example data and must not treat it as an official market fact.

## Expected Answer Shape

```text
Question type:
Playbooks used:
Data sources and time:
Data quality checks:
Data facts:
Expectation gap:
Policy reaction function:
Bond-market transmission:
Curve implication:
Credit and institution behavior:
Unconfirmed points:
Risks and counterexamples:
Follow-up indicators:
```

## Why This Is Good

- It separates synthetic data facts from stable framework facts.
- It refuses to call the release above or below expectation without consensus data.
- It treats social financing aggregate as an entry point, not as proof of private endogenous demand.
- It asks for current yield curve, funding, credit-spread, and institution-flow data before drawing current market conclusions.

## What Would Fail

- Calls the release "below expectation" without consensus, survey, or market-pricing evidence.
- Invents current 10Y CGB, 10Y CDB, DR007, NCD, or credit-spread levels.
- Treats aggregate social financing as private demand without decomposition.
- Presents synthetic example records as official PBOC or provider-returned data.
- Gives personalized portfolio advice or guaranteed return language.
