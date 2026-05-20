# Data Interface Catalog

Use this file when a fixed-income question needs current data, historical data, user-provided data, or connector-returned data. It defines what data is needed and where an agent may try to obtain it. It does not define credentials, private endpoints, or mandatory tool names.

For provider-specific candidate interfaces, citation metadata, and missing-data downgrade rules, read `references/12-data-connector-mapping.md` after identifying the required fields here.
For the canonical output contract and data packet, read `references/14-contracts-and-analysis-standards.md`.

## Purpose

FICC Researcher owns:

- Research question decomposition.
- Required field specification.
- Data-quality checks.
- Missing-data discipline.
- Interpretation of verified data.

External tools own:

- Fetching data.
- Returning source, query, timestamp, fields, row count, units, and limitations.

## Data Packet Standard

Convert every user file, MCP result, connector output, script result, or official-source table into this contract before analysis:

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

If a field is unknown, write `unknown`. Do not invent metadata.

## Source Priority

1. User-provided files, tables, terminal output, or verified local databases.
2. Licensed or configured structured connectors: iFinD, Wind, Tushare, local bond database.
3. Official public sources: PBOC, MOF, NBS, NAFR, CSRC, exchanges, CCDC, SHCH, CFETS, issuer disclosures.
4. WebSearch for source discovery, policy/news verification, and official-page leads.
5. Broker research files only as framework evidence, never as current market data.

Provider names below are optional examples. Users must configure their own credentials and comply with each provider's terms.
Exact provider candidates are summarized in `references/12-data-connector-mapping.md`; this catalog remains the research-field and missing-data source of truth.

## Macro Credit And Money

Research needs:

- Social financing, RMB loan structure, M1, M2, CPI, PPI, PMI, GDP, industrial production, fixed-asset investment, retail sales, exports, fiscal data.

Required fields:

- Indicator name, period, actual value, previous value, consensus expectation if available, revision, units, source, release time.
- For cumulative indicators: current cumulative, previous cumulative, single-month difference, rounding limitation.
- For social financing: aggregate increment, cumulative increment, stock, RMB loans, government bonds, corporate bonds, off-balance-sheet items, bill-related items where available.

Preferred sources:

- PBOC, NBS, MOF official pages and tables.
- Wind or iFinD for consensus, historical panels, and decompositions.
- Tushare for reproducible macro datasets where permission and fields allow.
- WebSearch only to locate official pages or public releases.

Tushare examples:

- `sf_month`: monthly social financing aggregate. Useful fields include `month`, `inc_month`, `inc_cumval`, `stk_endval`. It does not replace full PBOC decomposition when detailed components are needed.
- `cn_m`: money supply. Useful for M0, M1, M2 level and同比/环比 fields where available.
- `cn_cpi`: CPI series.
- `cn_ppi`: PPI series.
- `cn_gdp`: GDP series where quarterly context is needed.

Missing-data behavior:

- If consensus expectation is unavailable, do not say "超预期" or "低于预期"; compare only with previous value and seasonality.
- If only Tushare aggregate social-financing data is available, state that detailed PBOC components are missing.

## Rates And Yield Curves

Research needs:

- China treasury curve, CDB/policy-bank curve, key-rate changes, term spread, curve slope, carry, rolldown, futures basis, term premium proxy.

Required fields:

- Curve type, instrument type, tenor, yield, trade date, source, calculation method when known.
- At minimum for curve review: 1Y, 3Y, 5Y, 7Y, 10Y, 30Y treasury and policy-bank points where available.
- For changes: current date, comparison date, bp change by tenor.

Preferred sources:

- Wind, iFinD, ChinaBond, CFETS, local bond database, user-provided exports.
- Tushare only for verified and permissioned curve interfaces.

Tushare examples:

- `yc_cb`: ChinaBond treasury yield curve. Useful fields include `trade_date`, `ts_code`, `curve_name`, `curve_type`, `curve_term`, `yield`. This is a separate-permission interface and should not be treated as guaranteed.

Important limits:

- Do not assume Tushare has complete CDB, policy-bank, credit-spread, or real-time interbank curve coverage unless the interface and permission are verified.
- Do not infer current curve levels from old broker-report examples.

## Funding And Money Market

Research needs:

- DR007, R007, repo rates, repo volume, OMO, MLF, LPR, RRR, NCD issuance and yields, Shibor, bank funding pressure.

Required fields:

- Rate name, tenor, date, value, change, volume if relevant, source, frequency.
- For NCD: issuer type, tenor, rating, issuance rate, secondary yield, net financing where available.

Preferred sources:

- Wind, iFinD, CFETS, PBOC, NIFC, local database, user-provided exports.
- Tushare may support selected rate series such as Shibor or LPR where available.
- WebSearch can verify policy-operation announcements but not replace licensed funding panels.

Missing-data behavior:

- Without DR/R/NCD data, only discuss funding mechanism and list required fields before making leverage or short-end conclusions.

## Fiscal Supply

Research needs:

- Treasury issuance, local-government special bonds, ultra-long special treasury bonds, policy-bank supply, maturity, net financing, fiscal spending pace.

Required fields:

- Issuer, bond type, issue date, payment date, maturity, amount, coupon or yield if needed, net financing, calendar, budget progress, fiscal expenditure.

Preferred sources:

- MOF, local finance bureaus, Wind, iFinD, ChinaBond, local bond database, official issuance calendars.

Missing-data behavior:

- If supply data is missing, separate "growth support from fiscal policy" from "duration supply pressure" and do not make a strong long-end call.

## Credit Spreads And Issuer Risk

Research needs:

- Credit spreads by rating, tenor, sector, issuer type, region, liquidity bucket; issuance, cancellations, defaults/extensions, rating changes, issuer fundamentals.

Required fields:

- Spread, yield, benchmark curve, rating, tenor, sector, issuer type, region, sample universe, valuation source, date.
- For issuer risk: financial statements, cash flow, debt maturity, refinancing access, rating history, guarantee and collateral where relevant.

Preferred sources:

- Wind, iFinD, ChinaBond, SHCH, local bond database, issuer disclosures, rating-agency reports, user-provided exports.
- Tushare is not assumed to provide full professional credit-spread curves.

Missing-data behavior:

- Without current spreads and issuer data, do not recommend credit下沉. Provide framework, required fields, and risk checks only.

## Institution Behavior

Research needs:

- Bank, wealth-management, fund, insurance, broker, and proprietary-desk behavior; product flows; holdings; NAV; duration; leverage; redemption pressure.

Required fields:

- AUM or product scale, fund flow, NAV drawdown, duration, leverage, asset allocation, holdings, subscription/redemption, liability stability, regulatory constraints.

Preferred sources:

- Wind, iFinD, local product database, fund disclosures, wealth-management product data, insurance premium data, user-provided holdings.
- Tushare may support selected fund or market datasets where permission allows, but should not be treated as a complete institution-flow database.

Missing-data behavior:

- Without flows and NAV data, discuss likely behavior channels and feedback loops, not current positioning strength.

## Convertibles And Hybrid Assets

Research needs:

- Convertible valuation, equity linkage, bond floor, conversion premium, implied volatility, clauses, redemption/downward revision status, liquidity, rating.

Required fields:

- Convertible code, stock code, price, parity, conversion price, conversion premium, bond floor, YTM, rating, issue terms, remaining maturity, volume, clause status.

Preferred sources:

- Wind, iFinD, Tushare where covered, exchange disclosures, issuer announcements, local convertible database.

Tushare examples:

- Convertible基础、行情、转股价、赎回、评级等接口 may be useful where permission allows. Always verify exact fields before conclusion.

Missing-data behavior:

- Without parity, premium, bond floor, and clause data, do not make a valuation or trading conclusion.

## Offshore And Global Rates

Research needs:

- UST curve, Fed path, DXY/CNH, offshore RMB liquidity, USD bond spread, dim sum bond issuance, FX hedge cost, global policy divergence.

Required fields:

- Yield curve by tenor, policy expectation, FX spot/forward, cross-currency basis or hedge cost, issuer spread, rating, maturity, liquidity.

Preferred sources:

- Wind, iFinD, LSEG/Bloomberg-like terminals if available, US Treasury/Fed official data, HKMA, CFETS, local offshore database, user-provided exports.

Missing-data behavior:

- Without FX and hedge-cost data, do not infer offshore relative value.

## ABS And REITs

Research needs:

- Asset pool quality, cash-flow waterfall, senior/subordination, prepayment/default behavior, project NOI, occupancy, distribution yield, valuation.

Required fields:

- Underlying asset type, pool balance, cash-flow date, tranche, credit enhancement, default/prepayment, valuation, liquidity, project operating metrics.

Preferred sources:

- Exchange disclosures, issuer reports, trustee reports, Wind, iFinD, local ABS/REITs database, user-provided documents.

Missing-data behavior:

- Without asset-pool or project-operation data, only provide framework and due-diligence checklist.

## WebSearch And Official Sources

Use WebSearch for:

- Official release discovery.
- Policy statement verification.
- Issuer or regulator announcement leads.
- Recent event context.

Do not use WebSearch for:

- Replacing licensed current yield, spread, NAV, holding, or transaction data.
- Filling missing data with media guesses.

When WebSearch is used, label whether the source is official, media转引, or background.

## Missing Data Rules

Use this block whenever required fields are unavailable:

```text
缺失数据:
- 字段:
- 推荐来源:
- 时间范围:
- 频率:
- 用途:
在缺少以上数据前，只能给出框架判断，不能给出当前市场结论。
```

## Provider Compliance Notes

- Do not store tokens, passwords, account IDs, API keys, private URLs, or production database strings in this repository.
- Do not copy large provider documentation into the skill.
- Do not imply official partnership, endorsement, sublicense, or guaranteed coverage.
- Provider examples are optional data-source notes. The user is responsible for provider configuration and license compliance.
