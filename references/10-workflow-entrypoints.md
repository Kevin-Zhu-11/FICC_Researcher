# Workflow Entrypoints

Use this file when the user asks for a recurring research product rather than a one-off explanation. These entries act like portable command semantics across Codex, OpenClaw, Claude-style agents, and personal agents. They do not require a platform-specific slash-command implementation.

All workflows must include the canonical blocks in `references/14-contracts-and-analysis-standards.md`. The output blocks below are workflow-specific additions or aliases, not replacement contracts.
For framework consistency and source traceability, use `references/15-playbook-framework-standard.md` and `references/16-source-claim-map.yml` when a workflow cites broker-derived claims or compares playbooks.

## macro-data-commentary

When to use:

- Macro data commentary on social financing, M1/M2, CPI/PPI, PMI, fiscal policy, property, exports, GDP, industrial value added, investment, and consumption.

Required playbooks:

- `references/playbooks/rates-macro.md`
- `references/playbooks/bond-strategy.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/07-macro-indicator-glossary.md`
- `references/08-policy-reaction-function.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Actual value, previous value, expectation if available, release source, release time, key decompositions, current yield/spread/funding data if making market conclusions.

Template:

- `assets/templates/macro-data-commentary-template.md`

Output blocks:

- Question type, Data sources and time, Data facts, Expectation gap, Policy reaction function, Bond-market transmission, Curve implication, Credit and institution behavior, Missing data, Risks and counterexamples, Follow-up indicators.

Forbidden shortcuts:

- Do not call a release "above expectation" without consensus or market-pricing evidence.
- Do not infer current yields or spreads from old reports.
- Do not treat high social financing as private endogenous demand before decomposition.

Eval case:

- `macro-social-financing`

Quality rubric:

- `macro-data-commentary`

## yield-curve-review

When to use:

- CGB/CDB curve review, 1Y/3Y/5Y/10Y/30Y segmentation, bull flattening, bull steepening, bear flattening, bear steepening, duration, and curve strategy.

Required playbooks:

- `references/playbooks/rates-macro.md`
- `references/playbooks/bond-strategy.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/06-portfolio-action-policy.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Treasury/CDB curve points, comparison date, bp change, repo/NCD/funding data, supply calendar, key institution demand if available.

Template:

- `assets/templates/yield-curve-review-template.md`

Output blocks:

- Curve data sources, Tenor segmentation, Short-end drivers, Belly drivers, Long-end drivers, Supply-demand and institution behavior, Available strategies, Missing data, Risk triggers.

Forbidden shortcuts:

- Do not fabricate current curve levels.
- Do not recommend leverage without funding data.
- Do not treat curve steepness as attractive rolldown without carry/rolldown calculation.

Eval case:

- `yield-curve-no-data`

Quality rubric:

- `yield-curve-review`

## credit-spread-review

When to use:

- credit spreads, asset shortage, credit downshift, coupon strategy, LGFV, Tier-2 capital bonds and perpetual bank bonds, rating/tenor and sector spread comparison.

Required playbooks:

- `references/playbooks/credit-strategy.md`
- `references/playbooks/city-investment-bonds.md`
- `references/playbooks/financial-credit.md`
- `references/playbooks/institution-behavior.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Spread by rating/tenor/sector/issuer type, issuance and net financing, default or extension events, rating changes, fund and wealth demand, liquidity indicators.

Template:

- `assets/templates/credit-spread-review-template.md`

Output blocks:

- Spread data sources, By rating, By tenor, By issuer type, Credit risk, Liquidity compensation, Institution demand, Credit downshift boundary, Risks and counterexamples.

Forbidden shortcuts:

- Do not treat carry as risk-free.
- Do not equate asset shortage with issuer safety.
- Do not recommend credit downshift without spread compensation and exit liquidity.

Eval case:

- `credit-spread-low-level`

Quality rubric:

- `credit-spread-review`

## institution-flow-review

When to use:

- wealth-management product redemptions, bond fund subscriptions and redemptions, insurance allocation, bank balance-sheet behavior, institution liability constraints, net-value transformation feedback.

Required playbooks:

- `references/playbooks/institution-behavior.md`
- `references/playbooks/wealth-management-funds.md`
- `references/playbooks/bond-strategy.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Product scale, NAV drawdown, flow, duration, leverage, holdings, redemption/subscription, asset allocation.

Template:

- `assets/templates/daily-bond-brief-template.md` or `assets/templates/framework-analysis-template.md`

Output blocks:

- Institution type, Liability stability, Asset allocation, Duration/Leverage, NAV feedback, impact on rates bonds, credit bonds, and the curve, Missing data, Risk.

Forbidden shortcuts:

- Do not ignore NAV and redemption feedback.
- Do not infer fund flows from market moves alone.

Eval case:

- `institution-redemption`

Quality rubric:

- `institution-flow-review`

## portfolio-action-review

When to use:

- Duration stance, curve trade, whether to add leverage, credit allocation, take-profit/stop-loss, and portfolio scenario table.

Required playbooks:

- `references/playbooks/bond-strategy.md`
- selected domain playbooks by instrument.

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/06-portfolio-action-policy.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Portfolio mandate, holdings, benchmark, duration, DV01 if available, leverage, liquidity limit, funding cost, yield curve, spreads, drawdown tolerance.

Template:

- `assets/templates/portfolio-action-template.md`

Output blocks:

- Portfolio context, Current assessment, Scenario table, Holding-period return decomposition, Main loss paths, Missing data, Follow-up indicators.

Forbidden shortcuts:

- Do not give personalized investment advice.
- Do not provide unconditional trades without triggers and stop conditions.

Eval case:

- `funding-leverage`

Quality rubric:

- `portfolio-action-review`

## policy-event-commentary

When to use:

- Commentary on central-bank, fiscal, property, industrial, debt-resolution, regulatory, FX, or capital-market stabilization policy.

Required playbooks:

- `references/playbooks/rates-macro.md`
- selected credit/institution playbooks if relevant.

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/08-policy-reaction-function.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Official policy text, release time, policy tool, target, constraint, market pricing before and after if available.

Template:

- `assets/templates/policy-event-commentary-template.md`

Output blocks:

- Policy facts, objectives, tools, Constraints, Expectation gap, Bond-market transmission, Risks and counterexamples, Follow-up indicators.

Forbidden shortcuts:

- Do not treat policy rhetoric as delivered liquidity or fiscal spending.
- Do not ignore policy constraints such as FX, bank NIM, leverage, supply, or financial stability.

Eval case:

- `overseas-rates-linkage`

Quality rubric:

- `policy-event-commentary`

## convertible-review

When to use:

- convertible bonds, exchangeable bonds, parity, premium, bond floor, downward conversion-price revision, redemption, clause game, hybrid assets.

Required playbooks:

- `references/playbooks/convertible-hybrid.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/09-data-interface-catalog.md`

Required data:

- Convertible price, underlying equity price, conversion price, parity, conversion premium, bond floor, YTM, clause status, rating, liquidity.

Template:

- `assets/templates/framework-analysis-template.md` or `assets/templates/data-assisted-analysis-template.md`

Output blocks:

- Instrument identification, Data source, Valuation decomposition, Underlying equity sensitivity, Bond-floor protection, Clause status, liquidity, Risks and counterexamples.

Forbidden shortcuts:

- Do not value a convertible without parity, premium, bond floor, and clause data.

Eval case:

- `convertible-missing-valuation`

Quality rubric:

- `convertible-review`

## daily-bond-brief

When to use:

- daily brief, weekly brief, morning-meeting notes, post-close review.

Required playbooks:

- `references/playbooks/rates-macro.md`
- `references/playbooks/bond-strategy.md`
- `references/playbooks/credit-strategy.md`
- `references/playbooks/institution-behavior.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/09-data-interface-catalog.md`
- `references/10-workflow-entrypoints.md`

Required data:

- Yield curve, funding, credit spreads, issuance, policy/news, institution flow if available.

Template:

- `assets/templates/daily-bond-brief-template.md`

Output blocks:

- Today's conclusion, Data facts, Rates bonds, Credit bonds, Funding conditions, Supply and primary market, Institution behavior, Offshore and FX, Next-day watchlist, Risks and counterexamples.

Forbidden shortcuts:

- Do not write a market brief from framework alone; if current data is absent, say so and produce a framework-only brief.

Eval case:

- `daily-brief-no-live-data`

Quality rubric:

- `daily-bond-brief`

## data-assisted-analysis

When to use:

- user-uploaded tables, pasted terminal output, MCP-returned structured data, script output dataframe or JSON.

Required playbooks:

- Route by `references/00-routing.md`.

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/03-data-integration-policy.md`
- `references/09-data-interface-catalog.md`

Required data:

- Provided columns, dates, units, universe, source, limitations, missing fields.

Template:

- `assets/templates/data-assisted-analysis-template.md`

Output blocks:

- Data input, Data quality checks, judgments directly supported, judgments not supported, Framework facts, Data facts, Inferred judgments, Missing data.

Forbidden shortcuts:

- Do not silently merge conflicting sources.
- Do not infer missing columns from file names.

Eval case:

- `user-data-minimal-table`

Quality rubric:

- `data-assisted-analysis`
