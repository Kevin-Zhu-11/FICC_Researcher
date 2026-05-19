# MCP Connectors

## Principle

FICC Researcher should specify required fields and interpret verified data. MCP servers and external tools should fetch data and return source, timestamp, fields, and limitations. Keep connector configuration outside playbooks.

## Connector Matrix

| Connector | Best use | Not enough for |
| --- | --- | --- |
| Tushare | Macro, equity, funds, convertibles where covered, reproducible public datasets | Full bond microstructure, proprietary credit curves, real-time dealer quotes |
| iFinD | Broad China macro, bonds, funds, announcements, market data | Tasks outside licensed coverage or without verified indicator IDs |
| Wind Local Bridge | Curves, credit spreads, valuations, bond terms, holdings, issuer fundamentals | Environments without Wind terminal/export permission |
| Local Bond Database | Curated point-in-time curves, spreads, issuers, ratings, holdings, NAV, transactions | Data not ingested or not timestamped |
| WebSearch | Policy/news/source discovery and official-page leads | Licensed prices, yields, spreads, NAV, holdings, or trade data replacement |

## Tushare

Use Tushare when a token and package or MCP server are configured outside git. Require the connector to return the interface name, parameters, retrieval timestamp, row count, fields, and limitations. Treat Tushare as a useful public structured-data source, not as a complete China bond database.

### OpenClaw Registration Note

For OpenClaw 2026.5.x, do not add a top-level `mcpServers` key to `~/.openclaw/openclaw.json`. That shape is not accepted by the OpenClaw config validator and can stop the gateway.

Use OpenClaw's command interface instead:

```bash
openclaw mcp set <name> '{"command":"...","args":["..."],"env":{"TUSHARE_TOKEN":"${TUSHARE_TOKEN}"}}'
openclaw mcp list
openclaw mcp show <name>
```

Store the real token in `~/.openclaw/.env` or another local secret mechanism. Do not commit it.

Until a Tushare MCP server is registered, the VM can still use a local Tushare Python workflow as a data producer. In that case, pass the result into FICC Researcher as a data packet rather than treating FICC Researcher as the data-fetching layer.

## iFinD

Use iFinD for China macro, fixed-income, fund, announcement, and market datasets when exact identifiers and permissions are available. Verify indicator IDs, frequency, and units before making data conclusions.

## Wind Local Bridge

Use Wind or a local Wind-export bridge for professional fixed-income datasets: yield curves, credit spreads, bond valuation, terms, issuer fundamentals, ratings, fund holdings, and NAV. Keep terminal credentials, export paths, and account details outside this repository.

## Local Bond Database

Use a local bond database when it provides curated point-in-time data with schema, as-of date, update cycle, and permission boundaries. Prefer this for repeated research and backtests.

## WebSearch

Use WebSearch to find official policy pages, issuer announcements, regulator notices, and recent news. Do not use it as the primary source for current market levels unless the result is an official timestamped data page.

## Data Packet Contract

Every connector response should be converted into:

```text
source:
query:
as_of:
retrieved_at:
time_range:
frequency:
universe:
fields:
row_count:
units:
limitations:
```

## Security Rules

- Do not store tokens, passwords, API keys, account IDs, private endpoints, or production database strings in this repository.
- Use environment variables, local secret stores, or platform connector settings.
- Commit only examples and placeholders.
- If a connector is unavailable, return a missing-data block instead of fabricating data.

## Fallback Behavior

If the preferred connector is unavailable:

1. Check whether the user provided data.
2. Check local verified data.
3. Use another structured connector if equivalent.
4. Use official public sources for source verification.
5. Use WebSearch only for leads and background.
6. Return the missing-data block when no reliable data source exists.
