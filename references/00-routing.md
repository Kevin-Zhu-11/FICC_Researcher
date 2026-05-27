# FICC Researcher Routing

Use this file before reading playbooks. Route by the user's instrument, market driver, investor group, and required decision.

For canonical output labels, missing-data format, source-traceability triggers, portfolio-action boundaries, and cross-framework conflict handling, read `references/14-contracts-and-analysis-standards.md`.

For playbook framework expression, claim ids, and claim-to-source mapping, use `references/15-playbook-framework-standard.md` and `references/16-source-claim-map.yml`.

## Core Routes

| User question keywords | Primary playbooks | Source-report families | Required data direction |
| --- | --- | --- | --- |
| rates, macro, curve, duration, 10Y CGB, CDB, rate direction | `rates-macro.md`, `bond-strategy.md` | CICC bond principles and strategy; CICC low-rate macro and bond pricing; Huatai bond-market framework | Growth, inflation, funding, policy, fiscal supply, curve, term premium |
| social financing, M1, M2, CPI, PPI, PMI, industrial value added, investment, consumption, exports, expectation gap | `rates-macro.md`, `bond-strategy.md` plus `07-macro-indicator-glossary.md` and `08-policy-reaction-function.md` | Huatai fundamental-analysis framework; Huatai fixed-income framework | Indicator definition, frequency, expectation, previous value, surprise, transmission to policy and rates |
| funding, central bank, fiscal supply, NCD, short end, liquidity | `rates-macro.md`, `institution-behavior.md` | CICC low-rate investor behavior; Huatai institution behavior; Huatai bond-market framework | DR007, repo, NCD, deposit, fiscal payment, open-market operations |
| duration stance, curve trade, leverage, take-profit, stop-loss, portfolio action, holding-period return | `bond-strategy.md` plus `06-portfolio-action-policy.md` | CICC bond principles and strategy; Huatai fixed-income framework | Portfolio duration, curve buckets, leverage, carry, rolldown, funding cost, drawdown tolerance |
| credit spreads, asset shortage, credit downshift, credit beta, coupon strategy | `credit-strategy.md`, `institution-behavior.md` | CICC low-spread credit investment; Huatai credit-bond framework | Spread levels, rating migration, default risk, issuance, investor demand |
| LGFV, debt-resolution policy, regional spreads, platform transformation, implicit debt | `city-investment-bonds.md`, `credit-strategy.md` | CICC LGFV-bond framework | Region fiscal capacity, debt pressure, refinancing, policy support |
| Tier-2 capital bonds, perpetual bank bonds, bank capital bonds, broker bonds, insurance bonds, financial-sector credit | `financial-credit.md`, `institution-behavior.md` | CICC financial-sector credit framework | Capital adequacy, TLAC, issuer fundamentals, regulatory capital rules |
| wealth-management redemption, net-value transformation, bank wealth products, mutual funds, fund behavior | `wealth-management-funds.md`, `institution-behavior.md` | CICC wealth-management trends; CICC fixed-income-plus funds; Huatai institution behavior | Product NAV, duration, leverage, redemption flow, asset allocation |
| convertibles, exchangeables, parity, conversion premium, bond floor, downward conversion-price revision, redemption | `convertible-hybrid.md` | CICC convertible framework; Huatai convertible framework; CICC hybrid-asset framework | Equity price, conversion value, premium, bond floor, terms, liquidity |
| China government bond futures, interest-rate swaps, IRS, basis, hedging | `derivatives.md`, `rates-macro.md` | CICC interest-rate derivatives | Futures basis, swap curve, deliverable basket, repo, hedge objective |
| U.S. Treasuries, USD bonds, dim sum bonds, offshore RMB bonds, offshore, UST | `offshore-global-rates.md` | CICC U.S. Treasuries; CICC Chinese USD bonds and dim sum bonds; CICC offshore RMB bonds | Treasury curve, FX, cross-border funding, issuer spread, global policy |
| ABS, public REITs, asset securitization, underlying assets | `abs-reits.md` | CICC ABS framework; CICC public REITs framework | Asset pool, cash flow, senior/subordination, project NOI, valuation |
| FICC quant research, AI-assisted research, factor, monitoring, agent workflow | `quant-ai-research.md` | Huatai FICC quant and AI; CICC fixed-income-plus agents | Data schema, factor definition, model validation, monitoring target |

## Routing Rules

- If the question asks why or asks for a mechanism, prioritize framework playbooks and chart notes.
- If the question asks whether to buy now or how to assess current conditions, require current market data before concluding.
- If several playbooks match, choose the primary playbook by the user's decision target:
  - macro direction, policy reaction, and curve direction -> `rates-macro.md`;
  - portfolio expression, duration, curve, leverage, or stop conditions -> `bond-strategy.md` plus `06-portfolio-action-policy.md`;
  - credit spread, downshift, carry, issuer risk -> `credit-strategy.md` or the matching credit sub-playbook;
  - redemption, allocation, liability, or positioning feedback -> `institution-behavior.md`;
  - quant workflow, factor validation, monitoring design -> `quant-ai-research.md`.
- If the question spans macro and investor demand, combine `rates-macro.md` with `institution-behavior.md`.
- If the question spans credit returns and redemptions, combine `credit-strategy.md` with `institution-behavior.md`.
- If current data is unavailable, return the `Missing data` block from `references/14-contracts-and-analysis-standards.md` and avoid current-market conclusions.
- For MCP or connector usage, route data access decisions to `references/02-data-source-policy.md`.
- For current data, first route the research question, then read `references/09-data-interface-catalog.md` for field-level data requirements, preferred sources, and connector limits.
- If the user asks for a repeatable research product rather than a one-off explanation, choose the workflow in `references/10-workflow-entrypoints.md` before choosing the final output template.
- If the question spans several playbooks or channels point in different directions, use `references/11-research-decision-chains.md` to preserve the reasoning path and state scenario conditions.
- Do not combine playbooks mechanically. If a secondary playbook cannot change the conclusion or required data, mention it as a follow-up instead of loading it.
- Treat `credit-strategy.md` as the generic spread/risk layer. Route city investment, financial credit, ABS/REITs, convertibles, derivatives, or offshore questions to their specialized playbook first, and use credit strategy only as the shared valuation layer.
- Treat `bond-strategy.md` as portfolio reasoning and `references/06-portfolio-action-policy.md` as the action translation gate.
- For portfolio implementation, require scenario, action, trigger, expected return components, and stop condition from `references/06-portfolio-action-policy.md`.
- For macro data releases, require indicator definition, expectation gap, policy reaction, and bond-market transmission from `references/07-macro-indicator-glossary.md` and `references/08-policy-reaction-function.md`.
- For source traceability, follow the trigger rules in `references/14-contracts-and-analysis-standards.md`.

## Minimum Answer Skeleton

```text
Question type:
Playbooks used:
Data input:
Data quality checks:
Framework facts:
Data facts:
Inferred judgments:
Confidence:
Missing data:
Risks and counterexamples:
Follow-up indicators:
```
