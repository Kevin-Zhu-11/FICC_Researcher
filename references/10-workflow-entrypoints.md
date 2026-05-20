# Workflow Entrypoints

Use this file when the user asks for a recurring research product rather than a one-off explanation. These entries act like portable command semantics across Codex, OpenClaw, Claude-style agents, and personal agents. They do not require a platform-specific slash-command implementation.

All workflows must include the canonical blocks in `references/14-contracts-and-analysis-standards.md`. The output blocks below are workflow-specific additions or aliases, not replacement contracts.
For framework consistency and source traceability, use `references/15-playbook-framework-standard.md` and `references/16-source-claim-map.yml` when a workflow cites broker-derived claims or compares playbooks.

## macro-data-commentary

When to use:

- 社融、M1/M2、CPI/PPI、PMI、财政、地产、出口、GDP、工增、投资、消费等宏观数据点评。

Required playbooks:

- `references/playbooks/rates-macro.md`
- `references/playbooks/bond-strategy.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/07-macro-indicator-glossary.md`
- `references/08-policy-reaction-function.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Actual value, previous value, expectation if available, release source, release time, key decompositions, current yield/spread/funding data if making market conclusions.

Template:

- `assets/templates/macro-data-commentary-template.md`

Output blocks:

- 问题归类, 数据来源与时间, 数据事实, 预期差, 政策反应函数, 债市传导, 曲线含义, 信用与机构行为, 缺失数据, 风险与反例, 后续跟踪。

Forbidden shortcuts:

- Do not call a release "超预期" without consensus or market-pricing evidence.
- Do not infer current yields or spreads from old reports.
- Do not treat high social financing as private endogenous demand before decomposition.

Eval case:

- `macro-social-financing`

Quality rubric:

- `macro-data-commentary`

## yield-curve-review

When to use:

- 国债/国开曲线复盘、1Y/3Y/5Y/10Y/30Y 分段、牛平/牛陡/熊平/熊陡、久期和曲线策略。

Required playbooks:

- `references/playbooks/rates-macro.md`
- `references/playbooks/bond-strategy.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/06-portfolio-action-policy.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Treasury/CDB curve points, comparison date, bp change, repo/NCD/funding data, supply calendar, key institution demand if available.

Template:

- `assets/templates/yield-curve-review-template.md`

Output blocks:

- 曲线数据来源, 期限分段, 短端驱动, 中端驱动, 长端驱动, 供需与机构行为, 可用策略, 缺失数据, 风险触发条件。

Forbidden shortcuts:

- Do not fabricate current curve levels.
- Do not recommend leverage without funding data.
- Do not treat curve steepness as attractive rolldown without carry/rolldown calculation.

Eval case:

- `yield-curve-no-data`

Quality rubric:

- `yield-curve-review`

## credit-spread-review

When to use:

- 信用利差、资产荒、信用下沉、票息策略、城投、二永债、评级/期限/行业利差比较。

Required playbooks:

- `references/playbooks/credit-strategy.md`
- `references/playbooks/city-investment-bonds.md`
- `references/playbooks/financial-credit.md`
- `references/playbooks/institution-behavior.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Spread by rating/tenor/sector/issuer type, issuance and net financing, default or extension events, rating changes, fund and wealth demand, liquidity indicators.

Template:

- `assets/templates/credit-spread-review-template.md`

Output blocks:

- 利差数据来源, 分评级, 分期限, 分主体类型, 信用风险, 流动性补偿, 机构需求, 下沉边界, 风险与反例。

Forbidden shortcuts:

- Do not treat carry as risk-free.
- Do not equate asset shortage with issuer safety.
- Do not recommend credit下沉 without spread compensation and exit liquidity.

Eval case:

- `credit-spread-low-level`

Quality rubric:

- `credit-spread-review`

## institution-flow-review

When to use:

- 理财赎回、债基申赎、保险配置、银行表内行为、机构负债约束、净值化反馈。

Required playbooks:

- `references/playbooks/institution-behavior.md`
- `references/playbooks/wealth-management-funds.md`
- `references/playbooks/bond-strategy.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Product scale, NAV drawdown, flow, duration, leverage, holdings, redemption/subscription, asset allocation.

Template:

- `assets/templates/daily-bond-brief-template.md` or `assets/templates/framework-analysis-template.md`

Output blocks:

- 机构类型, 负债稳定性, 资产配置, 久期/杠杆, 净值反馈, 对利率债/信用债/曲线影响, 缺失数据, 风险。

Forbidden shortcuts:

- Do not ignore NAV and redemption feedback.
- Do not infer fund flows from market moves alone.

Eval case:

- `institution-redemption`

Quality rubric:

- `institution-flow-review`

## portfolio-action-review

When to use:

- 久期怎么摆、曲线怎么做、杠杆能不能加、信用仓位如何配、止盈止损、组合情景表。

Required playbooks:

- `references/playbooks/bond-strategy.md`
- selected domain playbooks by instrument.

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/06-portfolio-action-policy.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Portfolio mandate, holdings, benchmark, duration, DV01 if available, leverage, liquidity limit, funding cost, yield curve, spreads, drawdown tolerance.

Template:

- `assets/templates/portfolio-action-template.md`

Output blocks:

- 组合背景, 当前判断, 情景表, 持有期收益拆解, 主要亏损路径, 缺失数据, 后续跟踪。

Forbidden shortcuts:

- Do not give personalized investment advice.
- Do not provide unconditional trades without triggers and stop conditions.

Eval case:

- `funding-leverage`

Quality rubric:

- `portfolio-action-review`

## policy-event-commentary

When to use:

- 央行、财政、地产、产业政策、化债、监管、汇率或资本市场稳定政策点评。

Required playbooks:

- `references/playbooks/rates-macro.md`
- selected credit/institution playbooks if relevant.

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/08-policy-reaction-function.md`
- `references/09-data-interface-catalog.md`
- `references/11-research-decision-chains.md`

Required data:

- Official policy text, release time, policy tool, target, constraint, market pricing before and after if available.

Template:

- `assets/templates/policy-event-commentary-template.md`

Output blocks:

- 政策事实, 目标, 工具, 约束, 预期差, 债市传导, 风险与反例, 后续跟踪。

Forbidden shortcuts:

- Do not treat policy rhetoric as delivered liquidity or fiscal spending.
- Do not ignore policy constraints such as FX, bank NIM, leverage, supply, or financial stability.

Eval case:

- `overseas-rates-linkage`

Quality rubric:

- `policy-event-commentary`

## convertible-review

When to use:

- 可转债、可交债、平价、溢价率、债底、下修、赎回、条款博弈、混合资产。

Required playbooks:

- `references/playbooks/convertible-hybrid.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/09-data-interface-catalog.md`

Required data:

- Convertible price, underlying equity price, conversion price, parity, conversion premium, bond floor, YTM, clause status, rating, liquidity.

Template:

- `assets/templates/framework-analysis-template.md` or `assets/templates/data-assisted-analysis-template.md`

Output blocks:

- 标的识别, 数据来源, 估值拆解, 正股弹性, 债底保护, 条款状态, 流动性, 风险与反例。

Forbidden shortcuts:

- Do not value a convertible without parity, premium, bond floor, and clause data.

Eval case:

- `convertible-missing-valuation`

Quality rubric:

- `convertible-review`

## daily-bond-brief

When to use:

- 日报、周报、晨会材料、盘后复盘。

Required playbooks:

- `references/playbooks/rates-macro.md`
- `references/playbooks/bond-strategy.md`
- `references/playbooks/credit-strategy.md`
- `references/playbooks/institution-behavior.md`

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/09-data-interface-catalog.md`
- `references/10-workflow-entrypoints.md`

Required data:

- Yield curve, funding, credit spreads, issuance, policy/news, institution flow if available.

Template:

- `assets/templates/daily-bond-brief-template.md`

Output blocks:

- 今日结论, 数据事实, 利率债, 信用债, 资金面, 供给与一级, 机构行为, 海外与汇率, 明日关注, 风险与反例。

Forbidden shortcuts:

- Do not write a market brief from framework alone; if current data is absent, say so and produce a framework-only brief.

Eval case:

- `daily-brief-no-live-data`

Quality rubric:

- `daily-bond-brief`

## data-assisted-analysis

When to use:

- 用户上传表格、粘贴终端输出、MCP 返回结构化数据、脚本输出 dataframe 或 JSON。

Required playbooks:

- Route by `references/00-routing.md`.

Required references:

- `references/14-contracts-and-analysis-standards.md`
- `references/03-data-integration-policy.md`
- `references/09-data-interface-catalog.md`

Required data:

- Provided columns, dates, units, universe, source, limitations, missing fields.

Template:

- `assets/templates/data-assisted-analysis-template.md`

Output blocks:

- 数据输入, 数据质量检查, 可直接支持的判断, 不能支持的判断, 框架事实, 数据事实, 推断判断, 缺失数据。

Forbidden shortcuts:

- Do not silently merge conflicting sources.
- Do not infer missing columns from file names.

Eval case:

- `user-data-minimal-table`

Quality rubric:

- `data-assisted-analysis`
