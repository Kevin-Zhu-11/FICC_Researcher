# FICC Researcher 00 号设计思想目标

## 当前状态

- 仓库根目录: `D:\000AAA_Datas\Python\Skills\FICC_Researcher`
- Git 边界: 本 skill 独立使用 `FICC_Researcher/.git`，不使用 `D:\000AAA_Datas\Python\Skills` 根目录作为仓库。
- 已有资料: `references/source-reports/` 下保存 23 篇中金、华泰固定收益研究框架 Markdown。
- 当前目标: 将这些研报框架、Anthropic financial-services 的优秀组织方式、Codex `skill-creator` 的技能规范，合并成一个可维护、可验证、可扩展的固定收益分析 skill。

## 总目标

构建 `ficc-researcher` skill，使 Codex 在处理固定收益研究问题时，能够先判断问题类型，再读取必要 playbook 和源报告，最后输出有来源、有边界、有验证意识的分析结论。

本 skill 面向以下问题:

- 利率债、久期、曲线、资金面、货币政策、财政供给、债券组合策略。
- 信用债、信用利差、城投债、产业债、二永债、大金融信用债、资产荒。
- 银行、保险、理财、公募、券商自营、外资、年金等机构行为。
- 可转债、可交债、优先股、混合资本工具、雪球等混合型资产。
- ABS、公募 REITs、美元债、点心债、离岸人民币债、美债、利率衍生品。
- 固收量化、AI 投研、组合监控、专题报告生成。

本 skill 不负责:

- 直接给出不带约束的买卖建议。
- 伪造实时行情、利率、利差、评级、成交、持仓、基金净值等数据。
- 把历史券商框架或历史报告观点包装成当前市场观点。
- 保存任何 API key、token、账号密码或机构内部数据。
- 替代合规、投资决策、交易执行、风控审批。

## 核心设计原则

### 1. 渐进披露

遵循 `skill-creator` 的三层加载原则:

1. `SKILL.md`: 只放触发条件、路由规则、工作流、输出纪律。
2. `references/`: 放 playbook、索引、图表笔记、源报告映射，需要时再读。
3. `scripts/` 和 `assets/`: 放可重复校验脚本、模板和未来可复用资产。

因此，23 篇研报 Markdown 不直接进入 `SKILL.md`，只作为 `references/source-reports/` 的溯源材料。

### 2. 单 skill，多 playbook

第一阶段只建设一个 `ficc-researcher` skill，不拆成多个独立 skill。

原因:

- 固收问题经常跨主题，例如信用利差压缩同时涉及资金面、理财、机构行为和供给。
- 单 skill 可以统一数据源优先级、风险提示和输出风格。
- playbook 可以按主题扩展，不会让 `SKILL.md` 变成巨型文档。

未来拆分条件:

- 某个主题 playbook 超过 300 行且高频独立触发。
- 该主题需要独立脚本、模板或 MCP 工具链。
- 用户请求明显集中在某个工作流，例如组合风控、转债量化、债券相对价值。

### 3. 先路由，再分析

任何问题先进入 `references/00-routing.md`。

路由判断维度:

- 资产类型: 利率债、信用债、城投、金融债、转债、REITs、ABS、海外债。
- 分析动作: 解释框架、行情判断、策略制定、报告生成、数据核验、风险排查。
- 数据需求: 是否需要实时行情、历史序列、估值曲线、发行数据、机构持仓、基金净值。
- 来源要求: 是否指定中金、华泰，是否要求机构框架对比。

### 4. 区分三类事实

输出必须区分:

- 框架事实: 来自中金、华泰等源报告的分析方法、指标体系、历史经验。
- 数据事实: 来自本地数据库、MCP、iFinD、Tushare、Wind 或用户上传数据。
- 推断判断: Codex 根据框架和数据做出的当前分析。

如果缺少数据事实，只能给分析路径和数据清单，不能编造结论。

### 5. MCP 中央化

借鉴 Anthropic financial-services 的 `.mcp.json` 思路，未来所有外部数据连接器集中在仓库级配置或说明文件中管理，不散落到每个 playbook。

拟集中管理的连接器类型:

- Tushare: A 股、转债、基金、部分宏观和债券相关公开数据。
- iFinD: 宏观、债券、基金、公告、行业、资金和机构数据查询。
- Wind 或本地 Wind 导出: 收益率曲线、信用利差、债券估值、成交、发行、托管。
- 本地债券数据库: 若后续建立，用于沉淀历史曲线、估值、主体、债项、持仓、基金净值。
- Web 或公开资料: 仅作为补充核验，不作为机构级金融数据主来源。

MCP 配置原则:

- 连接器清单集中维护。
- playbook 只声明需要什么数据，不写死连接器调用细节。
- 没有连接器或没有权限时，skill 输出所需字段清单和手动获取路径。
- 不在仓库中保存任何密钥。

### 6. 数据源优先级

借鉴 Anthropic `comps-analysis` 的数据源纪律，FICC 数据使用优先级为:

1. 用户提供的明确数据文件或本地数据库。
2. 已验证 MCP 或本地金融数据接口，包括 iFinD、Tushare、Wind、本地债券库。
3. 券商框架 Markdown 中的历史框架、定义、方法论。
4. 官方公告、交易所、央行、财政部、发改委、外汇局、中债登、上清所等公开资料。
5. 普通 Web 搜索，只用于补充背景或查找公开页面，不作为关键数据主来源。

### 7. 人类复核

所有输出应当默认用于研究草稿或分析辅助，必须保留人类复核空间。

必须提示复核的场景:

- 涉及当前收益率、利差、价格、净值、评级、违约、交易结构。
- 涉及投资建议、组合调整、久期、杠杆、信用下沉。
- 涉及监管政策、税收、发行规则、会计处理。
- 涉及跨境债券、美元债、点心债、美债、汇率和资本流动。

## Anthropic financial-services 可借鉴点

### 核心 vertical plugin 思路

Anthropic financial-services 将金融能力拆成:

- `plugins/vertical-plugins/`: 垂直领域能力包。
- `skills/`: 具体任务方法。
- `commands/`: 显式触发的工作流命令。
- `.mcp.json`: 共享数据连接器。
- `agent-plugins/`: 端到端 workflow agent。

FICC 第一阶段不做完整 plugin 和 agent，但借鉴其边界:

- `SKILL.md` 对应统一入口。
- `references/playbooks/` 对应多个 workflow skill 的方法库。
- `references/00-routing.md` 对应命令路由。
- 未来 `mcp/` 或 `.mcp.example.json` 对应集中连接器说明。

### LSEG partner 插件思路

LSEG 插件将固收任务拆成:

- `bond-relative-value`
- `fixed-income-portfolio`
- `macro-rates-monitor`
- `swap-curve-strategy`
- `bond-futures-basis`
- `fx-carry-trade`
- `option-vol-analysis`

FICC 第一阶段映射为 playbook:

- `rates-macro.md`: 宏观利率和收益率曲线。
- `bond-strategy.md`: 久期、曲线、杠杆、骑乘、套息、供需。
- `institution-behavior.md`: 银行、保险、理财、公募、券商、外资、年金。
- `credit-strategy.md`: 信用债、信用利差、资产荒和风险重估。
- `convertible-hybrid.md`: 转债、可交债、优先股、混合资本工具。
- `derivatives.md`: 国债期货、利率互换、期权和基差。
- `offshore-global-rates.md`: 美债、中资美元债、点心债、离岸人民币债。
- `abs-reits.md`: ABS 和公募 REITs。

### `comps-analysis` 的分析纪律

FICC 应借鉴:

- 明确适用场景和不适用场景。
- 前置数据源优先级。
- 保留方法论和数据来源说明。
- 每个输出都能被审计和复核。
- 提供常见错误清单。
- 使用逐步验证，而不是一次性生成完整结论。

## 目标目录形态

```text
FICC_Researcher/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── 00-routing.md
│   ├── 01-source-index.yml
│   ├── 02-data-source-policy.md
│   ├── playbooks/
│   ├── chart-notes/
│   └── source-reports/
├── scripts/
├── assets/
│   └── templates/
└── docs/
    ├── projects/
    └── review/
```

## 成功标准

- `SKILL.md` 少于 500 行，职责清晰，不堆长研报内容。
- 每个 playbook 可独立阅读，能回答适用问题、核心框架、关键指标、输出模板、风险与反例。
- `00-routing.md` 可以把常见固收问题路由到 1 到 3 个 playbook。
- `01-source-index.yml` 能列出 23 篇源报告的机构、主题、关键词、对应 playbook。
- `02-data-source-policy.md` 明确 MCP、iFinD、Tushare、Wind、本地数据库和 Web 的优先级。
- `chart-notes/key-framework-charts.md` 至少转写 5 张关键框架图，避免依赖临时 CDN 图片。
- 所有新增脚本能在本地运行并给出明确输出。
- skill 通过 `quick_validate.py`。

## 风险和控制

- 风险: playbook 写成读书笔记。控制: 每个 playbook 必须有问题入口、判断链条和输出模板。
- 风险: 原始 Markdown 太长导致误读。控制: 只在需要溯源时读取 `source-reports/`。
- 风险: CDN 图片失效。控制: 关键图转写到 `chart-notes`。
- 风险: MCP 或数据接口不可用。控制: 输出字段清单和人工获取路径。
- 风险: 金融分析越界成投资建议。控制: 输出中明确研究辅助和复核要求。

## 当前结论

FICC Researcher 的 00 号设计思想是:

```text
用一个轻量 skill 统一触发和路由，
用多个 playbook 承载固定收益专题方法论，
用 source index 保持券商研报可追溯，
用集中 MCP / 数据源政策管理实时数据边界，
用验证脚本和人类复核保证输出可审计。
```
