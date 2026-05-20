# Contracts And Analysis Standards

Use this file as the canonical contract for FICC Researcher outputs, data packets, missing-data blocks, confidence labels, time horizons, language style, source traceability, and portfolio-action boundaries.

Other reference files may add workflow-specific blocks, but they must not redefine these contracts.

## Canonical Answer Contract

Every substantial answer should use these blocks in this order unless a workflow template explicitly adds more detail:

```text
问题归类:
使用 playbook:
数据输入:
数据质量检查:
框架事实:
数据事实:
推断判断:
置信度:
缺失数据:
风险与反例:
后续跟踪:
组合动作:  # only when the user asks for duration, curve, leverage, credit allocation, sizing, stop conditions, or portfolio scenarios
```

Block meaning:

- `框架事实`: stable mechanisms or research frameworks from playbooks, evidence cards, source reports, or decision chains.
- `数据事实`: timestamped current data, user-provided data, connector output, official releases, or clearly labelled historical examples.
- `推断判断`: conditional interpretation that combines framework facts and data facts.
- `置信度`: high, medium, or low, with one sentence explaining the basis.
- `缺失数据`: fields needed before stronger current-market conclusions.
- `组合动作`: scenario-based research expression only; do not present it as personalized investment advice.

## Minimum No-Data Contract

When current data is required but unavailable, use the same canonical labels:

```text
问题归类:
使用 playbook:
框架事实:
推断判断:
置信度: 低，原因是缺少当前数据。
缺失数据:
- 字段:
- 推荐来源:
- 时间范围:
- 频率:
- 用途:
在缺少以上数据前，只能给出框架判断，不能给出当前市场结论。
风险与反例:
后续跟踪:
```

`当前缺少数据` is accepted only as a legacy alias. New templates and evals should use `缺失数据`.

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

- `高`: required current data is complete enough for the question, source and timestamp are clear, units and universe are checked, and the selected playbooks or decision chains point in the same direction.
- `中`: key data is present but one or more supporting fields, comparisons, or market-pricing inputs are missing; conclusion must remain conditional.
- `低`: answer is framework-only, uses stale or incomplete data, lacks current market levels, or has unresolved cross-framework conflicts.

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

- The user asks for source, provenance, "依据", "来自哪篇研报", or comparison across institutions.
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
财政发力有两个方向：增长预期修复可能抬升长端利率，供给放量也可能提高期限溢价；但如果央行对冲充分且银行配置盘吸收供给，长端上行会被削弱。需要发行节奏、缴款、央行净投放、配置需求和曲线点位来判断主导通道。
```

## Language Policy

- Default answer language is Chinese when the user asks in Chinese.
- Use canonical Chinese block labels.
- English market terms are acceptable when they are standard industry usage, for example `carry`, `rolldown`, `basis`, `term premium`, `DV01`, `NCD`.
- If a workflow or template uses English aliases, keep them as explanatory parentheses rather than replacing the canonical Chinese labels.

## Concrete Inference Traps

Avoid these common shortcuts:

- 社融弱 does not mechanically mean yields must fall.
- 社融高 does not automatically mean private endogenous demand is strong.
- Fiscal supply up does not mechanically mean long yields must rise; check央行对冲 and allocation demand.
- Carry is not risk-free income; check spread compensation, drawdown, liquidity, and exit.
- A single DR007 point does not justify leverage; check repo volume, NCD, liability stability, and liquidity.
- Policy support does not make every credit issuer safe.
- WebSearch snippets do not replace licensed or official market data.
