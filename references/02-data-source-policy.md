# Data Source Policy

This policy controls how FICC Researcher uses live data, broker frameworks, MCP connectors, and web sources.

For combining uploaded files, connector results, and playbooks in one answer, also read `references/03-data-integration-policy.md`.
For connector setup templates and boundaries, read `references/04-mcp-connectors.md`.
For field-level connector mapping and missing-data implications, read `references/09-data-interface-catalog.md`.

## Data Source Priority

1. User-provided files, tables, terminal output, or verified local databases.
2. Centralized MCP or local finance connectors configured outside this repository:
   - iFinD: broad China macro, rates, bonds, funds, announcements, and market data.
   - Tushare: A-share, funds, macro, rates where coverage and license permit.
   - Wind: local terminal/export bridge for China fixed-income, curve, credit, issuer, fund, and macro data.
   - Local bond database: internal curves, spreads, issuer fundamentals, ratings, holdings, fund NAV, and transaction history.
3. Broker framework Markdown files under `references/source-reports/`.
4. Official public sources: PBOC, MOF, NAFR, CSRC, exchanges, CCDC, SHCH, NIFC, issuer disclosures, and official statistics.
5. Web search for news verification or background only when current information is essential.

## MCP Centralization Principle

- Keep connector configuration centralized, not scattered across playbooks.
- Playbooks should specify required fields, frequency, time range, and use.
- Field-level source mapping belongs in `references/09-data-interface-catalog.md`, not inside individual playbooks.
- Connector outputs should be passed into analysis as explicit data packets, not hidden context.
- This repository must not store real credentials, tokens, API keys, account IDs, private service URLs, or production database strings.
- If an MCP connector is unavailable, downgrade to a missing-data block and explain what cannot be concluded.

## Connector Boundaries

### iFinD

Use iFinD when the task needs China macro indicators, rates, bonds, funds, announcements, sector data, or issuer-market lookup. Verify exact indicator IDs and frequencies before using data in conclusions.

### Tushare

Use Tushare for reproducible China market and macro datasets when the fields are covered and the token is configured outside git. Do not assume Tushare has complete bond microstructure coverage.

### Wind

Use Wind or Wind exports for professional fixed-income fields such as yield curves, valuations, credit spreads, issuer financials, ratings, fund holdings, and bond terms when locally available. Treat exported files as user-provided data and cite file path, timestamp, and fields.

### Local Bond Database

Prefer the local bond database when it has curated point-in-time curves, spreads, holdings, NAV, issuer fundamentals, ratings, and transaction history. Confirm schema, as-of date, and update cycle before using.

### Web

Use web sources for official announcements, recent policy changes, and source verification. Web snippets do not replace licensed market data for current prices, spreads, holdings, or valuations.

## Missing Data Format

Use this exact block when data is required but unavailable:

```text
当前缺少数据:
- 字段:
- 推荐来源:
- 时间范围:
- 频率:
- 用途:
在缺少以上数据前，只能给出框架判断，不能给出当前市场结论。
```

## Current Data Discipline

- 不得伪造实时收益率、信用利差、估值、评级、成交、持仓、净值、发行规模、回购利率或政策事实。
- Do not infer "current market level" from old research reports.
- When using historical examples, label them as examples and include their original report context.
- When data has a timestamp, include it. When data has no timestamp, treat it as unverified.

## Recommended Data Fields By Task

| Task | Core fields |
| --- | --- |
| Rates and macro | GDP, CPI, PPI, PMI, credit impulse, DR007, repo, NCD, OMO, MLF, LPR, treasury supply, local-government-bond supply, FX pressure |
| Curve and duration strategy | Treasury/CDB curve, key-rate changes, carry, rolldown, repo funding, futures basis, portfolio duration |
| Credit strategy | Spread by rating/sector/tenor, issuance, cancellation, default or extension events, rating changes, fund and wealth demand |
| Institution behavior | Balance-sheet growth, deposits, insurance premium, wealth product NAV and duration, fund flows, leverage, regulatory constraints |
| Convertibles | Stock price, conversion price, parity, conversion premium, bond floor, implied volatility, clauses, liquidity, redemption/downward revision status |
| Offshore and global rates | UST curve, Fed path, DXY/CNH, offshore funding, issuer spread, rating, FX hedge cost |
