# Contracts And Analysis Standards

Use this file as the canonical contract for FICC Researcher outputs, data packets, missing-data blocks, confidence labels, time horizons, language style, source traceability, and portfolio-action boundaries.

Other reference files may add workflow-specific blocks, but they must not redefine these contracts.

## Canonical Answer Contract

Every substantial answer should use these blocks in this order unless a workflow template explicitly adds more detail:

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
Portfolio actions:  # only when the user asks for duration, curve, leverage, credit allocation, sizing, stop conditions, or portfolio scenarios
```

Block meaning:

- `Framework facts`: stable mechanisms or research frameworks from playbooks, evidence cards, source reports, or decision chains.
- `Data facts`: timestamped current data, user-provided data, connector output, official releases, or clearly labelled historical examples.
- `Inferred judgments`: conditional interpretation that combines framework facts and data facts.
- `Confidence`: high, medium, or low, with one sentence explaining the basis.
- `Missing data`: fields needed before stronger current-market conclusions.
- `Portfolio actions`: scenario-based research expression only; do not present it as personalized investment advice.

## Minimum No-Data Contract

When current data is required but unavailable, use the same canonical labels:

```text
Question type:
Playbooks used:
Framework facts:
Inferred judgments:
Confidence: low, because current data is missing.
Missing data:
- Fields:
- Recommended sources:
- Time range:
- Frequency:
- Use:
Until these fields are available, provide framework-only analysis and do not make current-market conclusions.
Risks and counterexamples:
Follow-up indicators:
```

`Currently missing data` is accepted only as a legacy alias. New templates and evals should use `Missing data`.

## Canonical Data Packet Contract

Normalize every user file, MCP result, connector output, script result, official-source table, or web-derived official data table into this metadata packet before analysis:

```text
source:
provider:
interface_or_file:
query:
as_of:
retrieved_at:
time_range:
frequency:
universe:
fields:
row_count:
units:
schema_notes:
missing_fields:
limitations:
```

Rules:

- If a field is unknown, write `unknown`.
- Do not invent hidden query parameters, row counts, source permissions, timestamps, or units.
- `data_source` is a legacy alias for `source`; normalize it to `source`.
- `known_limitations` is a legacy alias for `limitations`; normalize it to `limitations`.
- Connector-specific files may list candidate interfaces, but this packet is the only output-facing data contract.

## Data Source Priority

Use one priority ladder for current-data analysis:

1. User-provided files, tables, terminal output, screenshots, or pasted data.
2. Verified local databases, MCP outputs, or locally configured finance connectors with source, timestamp, and schema.
3. Licensed or configured structured data providers such as iFinD, Wind, Tushare, or a local bond database.
4. Official public sources and issuer, exchange, clearing, central-bank, treasury, regulator, or statistics disclosures.
5. WebSearch only for official-source discovery, public news verification, and event context.
6. Broker research reports only as framework evidence, not as current market data.

Broker reports can be higher priority for framework reasoning, but never for current levels, spreads, holdings, NAV, transactions, or policy facts after the report date.

## Confidence Calibration

Use three labels:

- `high`: required current data is complete enough for the question, source and timestamp are clear, units and universe are checked, and the selected playbooks or decision chains point in the same direction.
- `medium`: key data is present but one or more supporting fields, comparisons, or market-pricing inputs are missing; conclusion must remain conditional.
- `low`: answer is framework-only, uses stale or incomplete data, lacks current market levels, or has unresolved cross-framework conflicts.

Do not use numeric probabilities unless the user provides a model, sample, and calibration method.

## Time Horizon Rules

State the relevant horizon when making inferred judgments:

- Macro data release commentary: release day to 1 month.
- Funding, repo, NCD, and leverage review: intraday to 2 weeks.
- Curve, duration, and futures-basis review: 2 weeks to 3 months.
- Credit allocation and spread review: 1 to 6 months.
- Convertible valuation and clause review: catalyst window plus 1 to 3 months unless terms imply otherwise.
- Strategic framework or allocation discussion: 3 to 12 months.

If the horizon is unknown, say so and avoid translating a short-term signal into a long-term allocation conclusion.

## Portfolio-Action Boundary

Allowed:

- Scenario-based research language, such as "if funding stays stable and curve data confirms X, a neutral-to-slightly-long duration stance is better supported than an outright short stance."
- Trigger, stop condition, risk path, and data requirement lists.
- Portfolio diagnostics when the user provides mandate, holdings, benchmark, liquidity, duration, DV01, leverage, and drawdown constraints.

Not allowed:

- Personalized investment advice.
- Guaranteed returns.
- Unconditional trades without mandate, data, trigger, stop, and risk path.
- Position sizing or leverage advice when product liabilities, liquidity, funding, and drawdown constraints are missing.

## Source Traceability Trigger

Read `references/16-source-claim-map.yml`, `references/01-source-index.yml`, and the relevant evidence card when:

- The user asks for source, provenance, "basis", "which research report this comes from", or comparison across institutions.
- The answer cites a broker framework as evidence.
- A playbook, evidence card, or source-derived rule is being edited.
- The conclusion depends on a non-obvious framework claim rather than general market knowledge.

If source-traceability is not needed, cite the playbook or data source used, but do not load source-report originals.

Use `references/15-playbook-framework-standard.md` when comparing or editing playbook framework claims.

## Cross-Framework Conflict Resolution

When playbooks point in different directions:

1. Name each channel separately.
2. State which data would decide the conflict.
3. Use scenario language instead of one-channel certainty.
4. Prefer `references/11-research-decision-chains.md` for fiscal supply, credit expansion, funding leverage, institution feedback, and policy-reaction conflicts.

Example:

```text
Fiscal expansion has two channels: stronger growth expectations can lift long-end yields, while heavier supply can raise term premium. If central-bank liquidity offsets are sufficient and bank allocation accounts absorb supply, long-end upward pressure may be weakened. Use issuance pace, payment settlement, central-bank net injection, allocation demand, and curve levels to identify the dominant channel.
```

## Language Policy

- Default answer language may follow the user's language.
- Use canonical English block labels from this file for structured research output.
- English market terms are acceptable when they are standard industry usage, for example `carry`, `rolldown`, `basis`, `term premium`, `DV01`, `NCD`.
- If local-language explanations are needed, keep the block labels in English and translate only the prose under each block.

## Concrete Inference Traps

Avoid these common shortcuts:

- weak social financing does not mechanically mean yields must fall.
- strong social financing does not automatically mean private endogenous demand is strong.
- Fiscal supply up does not mechanically mean long yields must rise; check central-bank liquidity offset and allocation demand.
- Carry is not risk-free income; check spread compensation, drawdown, liquidity, and exit.
- A single DR007 point does not justify leverage; check repo volume, NCD, liability stability, and liquidity.
- Policy support does not make every credit issuer safe.
- WebSearch snippets do not replace licensed or official market data.
