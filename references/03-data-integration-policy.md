# Data Integration Policy

This file defines how FICC Researcher combines the research framework with user-provided data, MCP data, local databases, Tushare, iFinD, Wind, and WebSearch.

For connector setup templates and boundaries, read `references/04-mcp-connectors.md`.
For field-level data needs and connector-source mapping, read `references/09-data-interface-catalog.md`.
For the canonical output contract, data packet, confidence labels, and missing-data block, read `references/14-contracts-and-analysis-standards.md`.

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
User-data identification:
- Data type:
- Time range:
- Frequency:
- Sample universe:
- judgments directly supported:
- judgments not supported:
```

## MCP Or Connector Workflow

When an MCP or connector is available:

1. Use the playbook to define fields first; do not query blindly.
2. Use `references/09-data-interface-catalog.md` to identify preferred sources and connector limitations.
3. Prefer narrow, auditable queries over broad dumps.
4. Request time range, frequency, field names, source, and retrieval timestamp.
5. Check empty results, stale data, duplicated keys, and unit mismatches.
6. Summarize the connector result before using it in conclusions.

Connector results should be cited as data facts, for example:

```text
Data facts:
- Source: Tushare / iFinD / Wind / local bond database
- Retrieved at:
- As of:
- Fields:
- Limitation:
```

Use the full canonical data packet from `references/14-contracts-and-analysis-standards.md` for handoffs, evals, and reusable reports.

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
Question type:
Playbooks used:
Data input:
Data quality checks:
Framework facts:
Data facts:
Inferred judgments:
Risks and counterexamples:
Missing data:
Follow-up indicators:
```

## Analysis Output Without Data

When data is not available, do not force a current conclusion. Use:

```text
Question type:
Playbooks used:
Framework facts:
Inferred judgments:
Confidence: Low, because current data is missing.
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
