# Data Connector Mapping

Use this file when an agent needs provider-specific candidate interfaces or citation requirements after reading `references/09-data-interface-catalog.md`.

For the canonical output contract, data packet, missing-data block, and provider-neutral boundary, read `references/14-contracts-and-analysis-standards.md`.

## Purpose

FICC Researcher defines research fields, data quality checks, and interpretation logic. External tools provide data. This file maps FICC research fields to optional data-source families without turning any provider into a required dependency.

## Compliance Boundary

- Treat Tushare, iFinD, Wind, local databases, official sources, and WebSearch as optional external data producers.
- Provider documentation, service terms, user permissions, and local licenses govern exact interface availability.
- Do not write concrete credentials, account identifiers, private endpoints, paid raw exports, or production database strings in this repository.
- Do not imply that this repository redistributes provider data or represents any provider.
- If a provider is unavailable, produce a missing-data block instead of substituting guesses.

## Data Packet Metadata

Every provider result must be converted into this packet before analysis:

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

If a metadata field is missing, write `unknown`. Do not infer hidden query parameters or unstated permissions.

## Tushare Candidate Interface Summary

These names are optional candidate interfaces, not required dependencies. Availability depends on the user's token, permission level, package/MCP implementation, and provider terms.

| Research need | Candidate interface | Use | Limit |
| --- | --- | --- | --- |
| Social financing aggregate | `sf_month` | Monthly aggregate increment, cumulative increment, and stock where available. | Does not replace full PBOC component decomposition. |
| Money supply | `cn_m` | M0, M1, M2 levels and同比/环比 fields where available. | Does not prove transaction活化 without M1 structure and activity data. |
| CPI | `cn_cpi` | CPI同比/环比 and selected breakdowns. | Needs NBS/source verification for official release commentary. |
| PPI | `cn_ppi` | PPI同比/环比 and selected breakdowns. | Separate energy, commodity, base effect, and demand channels. |
| GDP and activity context | `cn_gdp` and covered macro interfaces | Quarterly growth and activity context where licensed. | Do not call surprise without consensus or market-pricing data. |
| ChinaBond treasury curve | `yc_cb` | Treasury curve fields such as trade date, curve name/type, term, and yield where licensed. | Permissioned interface; not guaranteed for every token. |
| Shibor and selected rates | provider-covered Shibor/LPR interfaces | Funding context if exact fields are verified. | Does not replace DR/R repo, NCD, or interbank bond funding panels. |
| Convertible market data | covered convertible quote/terms/clause interfaces | Price, conversion terms, clause events, or related fields where available. | Verify fields before valuation; bond floor and clause status may require other sources. |

## Macro And Money

| Research field | Preferred official source | Optional structured sources | Tushare candidate | iFinD/Wind/local candidate | Required metadata | Missing-data downgrade |
| --- | --- | --- | --- | --- | --- | --- |
| Social financing aggregate | PBOC | Tushare, iFinD, Wind, local macro database | `sf_month` if licensed | Macro indicator panel or PBOC table export | period, value, unit, source, retrieved_at, fields, row_count, limitations | Without decomposition or consensus, compare only with previous value and state missing fields. |
| Social financing decomposition | PBOC | iFinD, Wind, local macro database | Not assumed complete | PBOC decomposition table, macro indicator panel | component, period, cumulative/single-month basis, unit, rounding limit | Do not explain structure with aggregate alone. |
| Money supply | PBOC | Tushare, iFinD, Wind | `cn_m` if licensed | Macro indicator panel | M0/M1/M2 level, yoy, mom, period, unit | If M1 or M2 is missing, avoid "money activation" conclusions. |
| CPI | NBS | Tushare, iFinD, Wind | `cn_cpi` if licensed | CPI indicator panel | yoy, mom, basket or headline/core if available | State price signal only; do not infer broad demand without activity data. |
| PPI | NBS | Tushare, iFinD, Wind | `cn_ppi` if licensed | PPI indicator panel | yoy, mom, industry breakdown if available | Separate energy, commodity, base effect, and demand channels. |
| GDP and activity | NBS | Tushare, iFinD, Wind | `cn_gdp` and covered activity interfaces if licensed | Macro indicator panel | actual, previous, expectation if available, frequency, revision | Do not call a release "above/below expectation" without consensus or market-pricing data. |

## Rates And Curves

| Research field | Preferred official source | Optional structured sources | Tushare candidate | iFinD/Wind/local candidate | Required metadata | Missing-data downgrade |
| --- | --- | --- | --- | --- | --- | --- |
| China treasury curve | ChinaBond or verified curve source | Wind, iFinD, local bond database, Tushare where licensed | `yc_cb` if licensed and fields verified | Treasury curve table by tenor | curve type, tenor, yield, trade date, source, calculation method | Without current curve data, provide framework and required fields only. |
| CDB or policy-bank curve | ChinaBond, CFETS, verified market database | Wind, iFinD, local bond database | Not assumed complete | Policy-bank curve panel | bond type, tenor, yield, date, source | Do not infer policy-bank spreads from treasury data alone. |
| Curve changes | Verified curve panel | Wind, iFinD, local bond database | Possible only if same interface covers both dates | Curve time series | current date, comparison date, bp change, method | State that direction and slope cannot be confirmed without comparable dates. |
| Futures basis | Exchange and futures data source | Wind, iFinD, local database | Not assumed complete | Futures basis panel | contract, cheapest-to-deliver, conversion factor, basis, date | Do not make basis trade conclusions without CTD and carry data. |

## Funding And Money Market

| Research field | Preferred official source | Optional structured sources | Tushare candidate | iFinD/Wind/local candidate | Required metadata | Missing-data downgrade |
| --- | --- | --- | --- | --- | --- | --- |
| DR/R repo rates | CFETS, NIFC, verified money-market source | Wind, iFinD, local database | Not assumed complete | Repo rate and volume panel | rate name, tenor, date, value, volume where relevant | Without funding data, do not recommend leverage. |
| NCD rates and issuance | NIFC, CFETS, ChinaBond, verified database | Wind, iFinD, local database | Not assumed complete | NCD primary/secondary panel | issuer type, rating, tenor, rate, amount, date | Do not infer bank funding pressure from repo alone. |
| OMO, MLF, LPR, RRR | PBOC | Wind, iFinD, official web tables | Covered only if interface is verified | Policy-operation panel | operation type, amount, rate, maturity, date | Separate policy operation facts from market liquidity conclusions. |
| Shibor | Official Shibor source | Tushare, iFinD, Wind | Shibor interfaces if licensed | Money-market panel | tenor, date, value, source | Shibor does not replace DR/R or NCD for leverage decisions. |

## Credit Spreads

| Research field | Preferred official source | Optional structured sources | Tushare candidate | iFinD/Wind/local candidate | Required metadata | Missing-data downgrade |
| --- | --- | --- | --- | --- | --- | --- |
| Credit spread by rating and tenor | ChinaBond, SHCH, verified valuation source | Wind, iFinD, local bond database | Not assumed complete | Credit-spread curve panel | rating, tenor, sector, benchmark, date, source | Without spreads and benchmark, do not recommend credit beta or downshift. |
| City investment regional spread | ChinaBond, SHCH, local database | Wind, iFinD, local bond database | Not assumed complete | Regional city-investment spread table | region, rating, tenor, valuation source, date | Do not equate policy support with issuer safety. |
| Bank capital bond spread | ChinaBond, SHCH, local database | Wind, iFinD, local bond database | Not assumed complete | Bank capital bond valuation panel | instrument type, rating, call feature, tenor, date | State subordination and call-risk limits if data is incomplete. |
| Issuer risk | Issuer disclosures, rating agencies, audited financials | Wind, iFinD, local issuer database | Equity/financial fields only where covered | Issuer financial and rating history | issuer, period, cash flow, debt maturity, rating, source | Framework-only issuer risk review if fundamentals are missing. |

## Convertibles

| Research field | Preferred official source | Optional structured sources | Tushare candidate | iFinD/Wind/local candidate | Required metadata | Missing-data downgrade |
| --- | --- | --- | --- | --- | --- | --- |
| Convertible price and liquidity | Exchange, verified market database | Tushare, iFinD, Wind, local database | Covered convertible quote interfaces if licensed | Convertible market panel | code, price, volume, date, source | No valuation conclusion without price and liquidity. |
| Parity and premium | Exchange terms plus equity price | Tushare, iFinD, Wind, local database | Convertible terms and quote interfaces if licensed | Convertible valuation panel | stock price, conversion price, parity, premium, date | Do not infer equity sensitivity without parity. |
| Bond floor and YTM | Valuation database or internal model | Wind, iFinD, local convertible model | Not assumed complete | Valuation and model output | curve, credit spread, maturity, YTM, bond floor | Treat as missing if methodology is unknown. |
| Clause status | Issuer announcements, exchange disclosures | Tushare, iFinD, Wind, local parser | Convertible clause interfaces if licensed | Clause event panel | redemption, put, downward revision, trigger window | Do not discuss clause game without trigger status. |

## Institution Behavior

| Research field | Preferred official source | Optional structured sources | Tushare candidate | iFinD/Wind/local candidate | Required metadata | Missing-data downgrade |
| --- | --- | --- | --- | --- | --- | --- |
| Wealth product NAV and scale | Product disclosures, bank/wealth platforms | Wind, iFinD, local product database | Not assumed complete | Wealth product panel | product, NAV, drawdown, scale, date | Discuss mechanism only if flows are missing. |
| Bond fund flows and holdings | Fund disclosures, fund database | Wind, iFinD, local fund database | Selected fund fields where licensed | Fund flow and holding panel | fund, flow, NAV, duration, holding, date | Do not infer flows from price moves alone. |
| Insurance demand | Regulatory and insurer disclosures | Wind, iFinD, local database | Not assumed complete | Premium and allocation panel | premium, allocation, duration demand, date | Keep as structural demand framework if data unavailable. |
| Bank balance-sheet behavior | PBOC, NAFR, listed bank disclosures | Wind, iFinD, local database | Selected bank financial fields where licensed | Bank asset/liability panel | deposits, loans, bonds, capital, period | Avoid bank-demand claims without balance-sheet evidence. |

## Official Sources And WebSearch

Use official public sources for source verification and policy facts:

- PBOC: monetary policy, financial statistics, OMO, MLF, LPR, RRR.
- NBS: CPI, PPI, GDP, activity indicators, PMI where applicable.
- MOF and local finance bureaus: fiscal data, treasury and local-government-bond supply.
- Exchanges, ChinaBond, SHCH, CFETS, NIFC, issuer disclosures: bond terms, valuation, funding, issuance, policy or market infrastructure data where public.

Use WebSearch only to locate official pages, verify public announcements, or label media reports as background. WebSearch does not replace licensed current yields, spreads, NAV, holdings, or transaction data.

## Provider Citation Notes

When an answer uses Tushare, iFinD, Wind, WebSearch, official pages, a local database, or a user file, cite:

- Provider or source name.
- Interface, file, official page, or database table.
- Query parameters when safe to disclose.
- `as_of` and `retrieved_at`.
- Fields, row count, units, and known limitations.
- Whether the data is official, connector-returned, user-provided, synthetic, media background, or framework evidence.

## Missing Data Downgrade Rules

- No current market levels without current curve, spread, price, funding, or valuation data.
- No expectation surprise without consensus, survey, or market-pricing evidence.
- No credit-downshift conclusion without spread compensation, liquidity, and issuer fundamentals.
- No leverage recommendation without repo, NCD, product-liability, and liquidity indicators.
- No institution positioning claim without holdings, NAV, flows, or balance-sheet evidence.
- No provider substitution when the substitute lacks the required field, frequency, universe, or timestamp.
