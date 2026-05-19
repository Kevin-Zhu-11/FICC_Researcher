# FICC Researcher Routing

Use this file before reading playbooks. Route by the user's instrument, market driver, investor group, and required decision.

## Core Routes

| User question keywords | Primary playbooks | Source-report families | Required data direction |
| --- | --- | --- | --- |
| 利率, 宏观, 曲线, 久期, 10 年国债, 国开, 利率方向 | `rates-macro.md`, `bond-strategy.md` | 中金债券原理与策略, 中金低利率宏观与债券定价, 华泰债市分析框架 | Growth, inflation, funding, policy, fiscal supply, curve, term premium |
| 社融, M1, M2, CPI, PPI, PMI, 工增, 投资, 消费, 出口, 预期差 | `rates-macro.md`, `bond-strategy.md` plus `07-macro-indicator-glossary.md` and `08-policy-reaction-function.md` | 华泰基本面分析的道与术, 华泰固收分析框架 | Indicator definition, frequency, expectation, previous value, surprise, transmission to policy and rates |
| 资金面, 央行, 财政供给, 存单, 短端, 流动性 | `rates-macro.md`, `institution-behavior.md` | 中金低利率投资者行为, 华泰机构行为, 华泰债市分析框架 | DR007, repo, NCD, deposit, fiscal payment, open-market operations |
| 久期怎么摆, 曲线怎么做, 杠杆, 止盈, 止损, 组合动作, 持有期收益 | `bond-strategy.md` plus `06-portfolio-action-policy.md` | 中金债券原理与策略, 华泰固收分析框架 | Portfolio duration, curve buckets, leverage, carry, rolldown, funding cost, drawdown tolerance |
| 信用利差, 资产荒, 信用下沉, 信用 beta, 票息策略 | `credit-strategy.md`, `institution-behavior.md` | 中金低利差信用债投资, 华泰信用债分析框架 | Spread levels, rating migration, default risk, issuance, investor demand |
| 城投, 化债, 区域利差, 平台, 隐债 | `city-investment-bonds.md`, `credit-strategy.md` | 中金城投债分析框架 | Region fiscal capacity, debt pressure, refinancing, policy support |
| 二永债, 银行资本债, 券商债, 保险债, 大金融 | `financial-credit.md`, `institution-behavior.md` | 中金大金融信用债分析框架 | Capital adequacy, TLAC, issuer fundamentals, regulatory capital rules |
| 理财赎回, 净值化, 银行理财, 公募基金, 基金行为 | `wealth-management-funds.md`, `institution-behavior.md` | 中金理财发展趋势, 中金固收+基金, 华泰机构行为 | Product NAV, duration, leverage, redemption flow, asset allocation |
| 转债, 可交债, 平价, 转股溢价率, 债底, 下修, 赎回 | `convertible-hybrid.md` | 中金转债框架, 华泰可转债框架, 中金混合型资产框架 | Equity price, conversion value, premium, bond floor, terms, liquidity |
| 国债期货, 利率互换, IRS, 基差, 套保 | `derivatives.md`, `rates-macro.md` | 中金利率衍生品 | Futures basis, swap curve, deliverable basket, repo, hedge objective |
| 美债, 美元债, 点心债, 离岸人民币债, offshore, UST | `offshore-global-rates.md` | 中金美债, 中金中资美元债与点心债, 中金离岸人民币债 | Treasury curve, FX, cross-border funding, issuer spread, global policy |
| ABS, 公募 REITs, 资产证券化, 底层资产 | `abs-reits.md` | 中金 ABS 框架, 中金公募 REITs 框架 | Asset pool, cash flow, senior/subordination, project NOI, valuation |
| 固收量化, AI 投研, 因子, 监控, 智能体 | `quant-ai-research.md` | 华泰固收量化与 AI, 中金固收+智能体 | Data schema, factor definition, model validation, monitoring target |

## Routing Rules

- If the question asks "为什么" or "机制", prioritize framework playbooks and chart notes.
- If the question asks "现在能买吗/怎么看当前", require current market data before concluding.
- If the question spans macro and investor demand, combine `rates-macro.md` with `institution-behavior.md`.
- If the question spans credit returns and redemptions, combine `credit-strategy.md` with `institution-behavior.md`.
- If current data is unavailable, return the missing-data block from `references/02-data-source-policy.md` and avoid current-market conclusions.
- For MCP or connector usage, route data access decisions to `references/02-data-source-policy.md`.
- For portfolio implementation, require scenario, action, trigger, expected return components, and stop condition from `references/06-portfolio-action-policy.md`.
- For macro data releases, require indicator口径, expectation gap, policy reaction, and bond-market transmission from `references/07-macro-indicator-glossary.md` and `references/08-policy-reaction-function.md`.

## Minimum Answer Skeleton

```text
问题归类:
使用 playbook:
框架事实:
需要的数据:
当前可给出的判断:
不能确认的部分:
风险与反例:
后续跟踪:
```
