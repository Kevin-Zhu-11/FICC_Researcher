# Macro Indicator Glossary

Use this file for macro data releases, especially when the user asks about social financing, credit, money supply, inflation, PMI, production, investment, consumption, or exports.

## Indicator Protocol

For every indicator, state:

```text
指标:
口径:
频率:
公布机构:
领先/同步/滞后:
关注分项:
债市传导:
常见误读:
需要对比:
```

## Macro Reading Order

Use the Huatai macro framework as the default reading order for China macro data:

```text
economic temperature and cycle season
-> demand, supply, price, policy, and market-pricing map
-> leading / coincident / lagging indicator layer
-> expectation gap and priced-in level
-> policy reaction function
-> funding, supply, curve, credit, and institution-behavior transmission
```

Do not read a single indicator in isolation. For China rates research, social financing, money, fiscal data, property, PMI, prices, and policy statements must be mapped into economic circulation and policy response.

## Indicator Timing Matrix

### Leading Indicators

- Credit and money: social financing, RMB loan structure, M1, M2, bill financing, loan demand index.
- Property front end: sales, prices, inventory, land transactions, new starts.
- Fiscal and policy: government-bond issuance, special-bond issuance, budget spending pace, policy statements.
- Market and high-frequency: term spread, bill discount rate, repo/NCD, commodity prices, RMB effective exchange rate.
- Confidence: consumer confidence, entrepreneur confidence, employment and income expectations.

Use leading indicators to identify turning points, but always check whether the market has already priced the direction.

### Coincident Indicators

- GDP, GDP deflator, industrial production, services production.
- PMI production and new orders, CPI, PPI.
- Fixed-asset investment, retail sales, exports, imports.
- Power consumption, freight, commodity volume and price, passenger-car sales.

Use coincident indicators to confirm whether the leading signal is transmitting into real activity and prices.

### Lagging Indicators

- Inventory, employment, tax revenue, corporate earnings, household income.

Use lagging indicators to verify the previous judgment, not to create a fresh rates conclusion by themselves.

## Economic Circulation Checks

For broad macro releases, check at least four circulation channels:

- Employment, income, and consumption.
- Manufacturing price signal, profit, investment, and capacity.
- Property sales, price, land, new starts, and investment.
- External demand, exports, production chain, and exchange-rate pressure.

If the circulation is blocked, traditional leading indicators can weaken. State this explicitly instead of forcing a linear interpretation.

## Credit And Money

### 社会融资规模

- Role: leading indicator for financing demand, policy support, and broad credit impulse.
- Focus: aggregate financing, RMB loans, government bonds, corporate bonds, trust loans, undiscounted bankers' acceptances.
- Read with: M1, M2, loan structure, government bond issuance, fiscal spending, property sales, and bill financing.
- Bond transmission: weak real financing demand is usually rates-friendly, but heavy government bond supply can offset the first-order signal.
- Common misreading: treating high social financing as pure growth strength without separating government-bond financing from private credit demand.
- Required decomposition: government bonds, corporate bonds, RMB loans, off-balance-sheet items, and bill-related items.
- Required formula when using single-month values from cumulative releases: `current cumulative - previous cumulative = single-month estimate`; include rounding limitation.

### 新增人民币贷款

- Role: bank-credit creation and sector financing demand.
- Focus: household short-term loans, household medium-long loans, corporate short-term loans, corporate medium-long loans, bill financing.
- Bond transmission: weak household and medium-long corporate loans point to weak endogenous demand; strong bill financing can indicate weak real loan demand.

### M1 / M2

- Role: money activity and liquidity state.
- Focus: M1-M2 gap, deposit migration, fiscal deposit movement, corporate demand deposits.
- Bond transmission: weak M1 may point to weak transaction activity and low inflation pressure; high M2 may not be growth-positive if deposit hoarding dominates.
- Common misreading: treating M2 strength as real-economy activity without checking M1, credit structure, and fiscal-deposit movement.

## Growth

### GDP

- Role: broad output summary.
- Frequency: quarterly.
- Read with: nominal GDP, real GDP, GDP deflator, industrial production, services production, employment, and income.
- Common misreading: treating GDP as a tradable surprise without checking whether monthly data already priced it.

### 工业增加值

- Role: production-side synchronous indicator.
- Read with: exports, power consumption, PMI production, commodity prices, profits, and capacity utilization.
- Bond transmission: production strength matters more when it links to prices, profits, and financing demand.

### 固定资产投资

- Role: investment demand and future supply.
- Focus: manufacturing, infrastructure, real estate, private investment.
- Bond transmission: infrastructure and government investment affect growth and bond supply at the same time.
- Required decomposition: manufacturing investment, infrastructure investment, property development investment, private investment.

### 社会消费品零售

- Role: goods-consumption proxy.
- Read with: services consumption, income, employment, confidence, property wealth effect.
- Common misreading: treating retail sales as total consumption.

### 出口

- Role: external demand and industrial-chain utilization.
- Read with: global PMI, shipping, exchange rate, export delivery value, trade policy.

## Inflation

### CPI

- Role: consumer inflation and policy constraint.
- Focus: food, energy, core goods, services.
- Bond transmission: CPI matters more when it changes policy constraints or inflation expectations.

### PPI

- Role: industrial price and profit signal.
- Focus: upstream materials, midstream equipment, downstream pass-through.
- Bond transmission: PPI weakness supports low nominal-growth expectations; supply-side restrictions can create price rebounds without broad demand recovery.

## Sentiment And Leading Data

### PMI

- Role: early soft indicator.
- Focus: new orders, production, employment, prices, supplier delivery, imports, exports.
- Common misreading: comparing official and Caixin PMI without considering sample and sector differences.

## Expectation-Gap Discipline

For each release, separate:

```text
actual value:
consensus expectation:
previous value:
revision:
seasonal effect:
base effect:
priced-in market move:
surprise direction:
```

The market trades the expectation gap and the policy reaction to it, not the raw value alone.

## Source Reports

- `huatai-fixed-income-framework-2025`
- `huatai-fundamental-analysis-method-2025`
