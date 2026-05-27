# Research Decision Chains

Use this file when a question spans multiple playbooks or when an agent needs a repeatable reasoning path rather than a free-form essay.

Use `references/15-playbook-framework-standard.md` for the standard playbook claim format, and `references/16-source-claim-map.yml` to trace stable framework claims back to evidence-card sections and source report ids.

## Macro Release To Rates

```text
Indicator fact
-> Definition, frequency, release agency
-> Actual value versus expectation, previous value, seasonality, and base effect
-> Economic loop: consumption, manufacturing, property, external demand, fiscal and financial conditions
-> Policy objectives: growth, employment, prices, financial stability, and FX stability
-> Policy tools and constraints
-> Funding conditions, fiscal supply, and risk appetite
-> Yield-curve segments
-> Credit and institution behavior
-> Portfolio actions and risk triggers
```

Common errors:

- Strong social financing does not automatically mean private endogenous demand is strong.
- High M2 growth does not automatically mean transaction activity is improving.
- A PPI rebound does not automatically mean broad demand overheating.
- One weak monthly reading does not prove a trend-level credit contraction.
- Do not give current point-level yield or spread views before current yield and spread data is available.

Required data:

- Actual value, previous value, expectation if available, decomposition, release source, curve, funding, credit spread, and policy context.

## Funding To Curve

```text
Central-bank operations and fiscal payment settlement
-> DR007, R007, NCD, and Shibor
-> Bank liability cost and non-bank leverage cost
-> Short-end rate anchor
-> Belly carry and rolldown
-> Long-end term premium and allocation demand
-> Curve shape
-> Leverage and duration risk
```

Common errors:

- Loose funding does not make leverage risk-free.
- A low short end does not guarantee long-end yields will fall.
- Stable funding prices do not prove stable product liabilities.

Required data:

- Repo rates, repo volume, NCD yield and issuance, OMO/MLF operations, fiscal payment, product flows, and curve points.

## Fiscal Supply To Duration

```text
Budget and issuance plan
-> Issuance pace, payment settlement, and net financing
-> Allocation-account absorption capacity
-> Bank balance-sheet demand, insurance demand, fund demand, and wealth-management demand
-> Term premium
-> 10Y and 30Y volatility
-> Duration exposure and take-profit discipline
```

Common errors:

- Fiscal expansion can support growth and increase bond supply at the same time.
- A high single-month government-bond financing reading does not prove that fiscal spending has already become real activity.
- A fundamentally bullish signal for ultra-long bonds can be offset by supply pressure and crowded positioning.

Required data:

- Issuance calendar, net financing, maturity, payment date, fiscal expenditure, curve supply by tenor, and investor absorption.

## Credit Spread To Allocation

```text
Spread level and percentile
-> Issuer fundamentals
-> Refinancing environment
-> Supply and net financing
-> Institution demand and liability stability
-> Liquidity compensation
-> Downshift, duration extension, or high-grade carry choice
-> Exit conditions and risk triggers
```

Common errors:

- Low credit spreads do not mean credit risk has disappeared.
- Asset shortage does not make every low-quality issuer safe.
- Coupon carry is not risk-free income.
- Loose funding cannot replace issuer cash-flow and refinancing checks.

Required data:

- Spread by rating, sector, and tenor; issuer cash flow; maturity wall; issuance; cancellations; default or extension events; fund demand; and wealth-management demand.

## Institution Behavior To Market

```text
Liability stability
-> Duration preference
-> Leverage capacity
-> NAV volatility
-> Subscription, redemption, or allocation feedback
-> Rates-bond demand
-> Credit spreads
-> Curve and liquidity
```

Common errors:

- Do not look only at yield changes while ignoring product NAV and liability-side pressure.
- Do not treat banks, wealth products, funds, and insurers as the same marginal buyer.
- Do not ignore how redemption feedback can amplify credit-bond liquidity pressure.

Required data:

- AUM, flows, NAV drawdown, holdings, duration, leverage, insurance premium, bank deposits, and bond allocation.

## Policy Event To Portfolio

```text
Policy facts
-> Policy objectives
-> Tool type
-> Constraints
-> Whether the event is above or below expectation
-> Funding, supply, risk appetite, and credit-risk channels
-> Tradable component
-> Portfolio actions
-> Counterexamples and stop conditions
```

Common errors:

- Do not treat policy language as already-completed liquidity injection or fiscal spending.
- Do not focus only on growth support while ignoring supply pressure.
- Do not ignore FX, bank net interest margins, bond-market leverage, and financial-stability constraints.

Required data:

- Official policy text, release time, tool details, expected-versus-actual gap, market pricing before and after release, and implementation calendar.

## Convertible To Hybrid Allocation

```text
Underlying equity trend and volatility
-> Parity and conversion premium
-> Bond floor and credit protection
-> Clause status
-> Liquidity
-> Equity-like versus bond-like classification
-> Portfolio role
-> Risk triggers
```

Common errors:

- Do not look only at equity sensitivity while ignoring bond floor, premium, and clauses.
- Do not treat low-priced convertibles as automatically safe.
- Do not ignore rating, liquidity, redemption, and downward conversion-price revision constraints.

Required data:

- Convertible price, stock price, conversion price, parity, premium, bond floor, YTM, clause status, rating, and volume.

## Offshore Rates And Credit To Domestic FICC

```text
Offshore policy and UST curve
-> DXY and CNH
-> Hedging cost
-> Offshore funding and Chinese USD-bond spreads
-> Dim sum bond and offshore RMB-bond supply-demand
-> Domestic rates and credit relative value
```

Common errors:

- Do not compare onshore and offshore returns without FX and hedging costs.
- Do not equate a UST rally with an automatic domestic long-end rally.
- Do not ignore offshore liquidity and issuer-credit differences.

Required data:

- UST curve, Fed path, DXY/CNH, hedge cost, issuer spread, offshore issuance, rating, and liquidity.
