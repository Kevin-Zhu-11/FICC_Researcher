# Data Integration Policy

This file defines how FICC Researcher combines the research framework with user-provided data, MCP data, local databases, Tushare, iFinD, Wind, and WebSearch.

For connector setup templates and boundaries, read `references/04-mcp-connectors.md`.

## Core Principle

FICC Researcher does not own data retrieval. It owns the research question, required data specification, data-quality checks, and interpretation discipline.

Use this split:

```text
FICC skill:
  route question -> choose playbooks -> define required data -> interpret verified data

Data connectors:
  fetch data -> return fields, time range, timestamp, source, and limitations

Analysis agent:
  combine skill + data -> label framework facts, data facts, and inferred judgments
```

## Data Input Priority

Use this priority order for actual analysis:

1. User-provided files, tables, screenshots, terminal output, or pasted data.
2. Local verified databases or MCP outputs with source, timestamp, and schema.
3. iFinD, Wind, Tushare, or other licensed/structured data connectors.
4. Official public sources and issuer/regulator/exchange disclosures.
5. WebSearch, for news, policy, announcement discovery, and source leads.
6. Broker research reports, only as framework evidence, not as current market data.

If user-provided data conflicts with connector data, do not merge silently. Report the conflict and ask which source should be authoritative, or analyze both as separate scenarios.

## Required Data Packet Contract

When receiving data from a user, MCP, connector, or script, normalize it into this mental contract before analysis:

```text
data_source:
as_of:
retrieved_at:
time_range:
frequency:
universe:
fields:
units:
schema_notes:
missing_fields:
known_limitations:
```

If any of these fields are unknown, label them as unknown. Do not invent metadata.

## User-Provided Data Workflow

When the user uploads or pastes data:

1. Identify the data type: yield curve, credit spreads, bond list, issuer table, holdings, NAV, fund flow, macro time series, transaction data, or text evidence.
2. Inspect columns, date fields, units, frequency, and universe.
3. Map the user data to the selected playbook's `Required Inputs`.
4. State what the data can support directly.
5. List missing fields before making current-market conclusions.
6. Analyze the data using the framework, but keep raw facts separate from inferred judgments.

Use this output block:

```text
用户数据识别:
- 数据类型:
- 时间范围:
- 频率:
- 样本范围:
- 可直接支持的判断:
- 不能支持的判断:
```

## MCP Or Connector Workflow

When an MCP or connector is available:

1. Use the playbook to define fields first; do not query blindly.
2. Prefer narrow, auditable queries over broad dumps.
3. Request time range, frequency, field names, source, and retrieval timestamp.
4. Check empty results, stale data, duplicated keys, and unit mismatches.
5. Summarize the connector result before using it in conclusions.

Connector results should be cited as data facts, for example:

```text
数据事实:
- Source: Tushare / iFinD / Wind / local bond database
- Retrieved at:
- As of:
- Fields:
- Limitation:
```

## Tushare Boundary

Tushare is useful for reproducible China equity, fund, macro, and selected rates datasets when a token and package/MCP are configured.

Use Tushare for:

- Macro series such as CPI, PPI, PMI, GDP, money supply, social financing where available.
- Shibor or LPR-like rates where covered.
- Equity and convertible-related stock data, valuation, financials, and market behavior.
- Fund or index data where permission allows.

Do not assume Tushare covers:

- Complete interbank bond valuation.
- Full credit-spread curves by rating, sector, issuer, and tenor.
- Proprietary fund holdings, real-time bond transactions, or internal dealer quotes.

If Tushare is the only connector, state what it can and cannot cover for the FICC question.

## iFinD And Wind Boundary

Use iFinD or Wind for professional China fixed-income data when available:

- Treasury, CDB, and policy-bank curves.
- Credit spreads by rating, sector, tenor, issuer type, and liquidity bucket.
- Bond terms, ratings, issuer fundamentals, and valuation.
- Fund holdings, NAV, duration, leverage, and product behavior.
- Macro indicators and official-series lookup.

Keep credentials and terminal-specific paths outside the repository.

## WebSearch Boundary

Use WebSearch for:

- Recent policy announcements and official-source discovery.
- News, issuer announcement leads, regulator notices, and event context.
- Finding where to verify a source.

Do not use WebSearch as the source for:

- Current market prices, yields, spreads, NAV, holdings, or trade data unless the page is an official source and includes timestamped data.
- Licensed data that should come from iFinD, Wind, Tushare, or a local database.

When WebSearch is used, label the result as news or source-discovery evidence unless it is verified official data.

## Analysis Output With Data

When data is available, use this structure:

```text
问题归类:
使用 playbook:
数据输入:
数据质量检查:
框架事实:
数据事实:
推断判断:
风险与反例:
缺失数据:
后续跟踪:
```

## Analysis Output Without Data

When data is not available, do not force a current conclusion. Use:

```text
问题归类:
使用 playbook:
框架判断:
当前缺少数据:
- 字段:
- 推荐来源:
- 时间范围:
- 频率:
- 用途:
在缺少以上数据前，只能给出框架判断，不能给出当前市场结论。
```

## Data Quality Checks

Before using any data in a conclusion, check:

- Timestamp or as-of date exists.
- Frequency is clear.
- Units and scale are clear.
- Universe is clear.
- Key columns are present.
- Duplicates and missing values are understood.
- Current data and historical examples are not mixed.
- Source permission or limitation is noted when known.

## Cross-Agent Portability

For Codex, Claude, OpenClaw, or personal agents:

- Keep playbooks data-source agnostic.
- Put connector setup in external MCP or environment configuration.
- Pass user data and connector data as explicit artifacts.
- Require the agent to cite data source and timestamp.
- If the platform lacks a connector, return the missing-data block and proceed only with framework analysis.
