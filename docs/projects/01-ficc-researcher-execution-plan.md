# FICC Researcher 01 号设计执行方案

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` or `superpowers:executing-plans` when implementing this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** 将 `FICC_Researcher` 从资料仓库升级为可触发、可路由、可溯源、可验证的固定收益分析 skill。

**Architecture:** 采用单 `SKILL.md` 入口、多 playbook、集中数据源政策、源报告索引和验证脚本的结构。`SKILL.md` 保持轻量，所有长内容放入 `references/`，MCP 和金融数据接口作为集中能力层，不散落到专题 playbook。

**Tech Stack:** Markdown, YAML, Python, Git, Codex skill conventions, optional MCP connectors for iFinD/Tushare/Wind/local bond database.

---

## 文件职责

- `SKILL.md`: skill 入口，负责触发描述、任务分类、路由步骤、数据源纪律、输出格式和禁止事项。
- `agents/openai.yaml`: Codex UI 元数据，包含展示名称、短描述和默认提示。
- `references/00-routing.md`: 用户问题到 playbook、源报告、数据需求的路由表。
- `references/01-source-index.yml`: 23 篇源报告的结构化索引。
- `references/02-data-source-policy.md`: MCP、iFinD、Tushare、Wind、本地数据库、Web 的数据源优先级和缺失数据处理规则。
- `references/playbooks/*.md`: 固收专题分析流程。
- `references/chart-notes/key-framework-charts.md`: 关键图片的文字转写和使用场景。
- `scripts/build_source_index.py`: 从 `source-reports/` 文件名和人工映射生成或校验 `01-source-index.yml`。
- `scripts/validate_skill_links.py`: 校验 `SKILL.md`、routing、playbooks、source index 中的相对路径是否存在。
- `docs/review/`: 后续放计划审查和执行复盘。

## 执行阶段

### 阶段 1: 建立 skill 入口和元数据

**Files:**
- Create: `<repo-root>\SKILL.md`
- Create: `<repo-root>\agents\openai.yaml`

- [ ] **Step 1: 写 `SKILL.md` frontmatter**

内容要求:

```yaml
---
name: ficc-researcher
description: Fixed income and FICC research workflow skill for Chinese bond-market analysis, rates and macro, credit bonds, city investment bonds, financial credit, convertible bonds, wealth management and fund behavior, institution behavior, offshore bonds, USD bonds, dim sum bonds, US Treasuries, ABS, public REITs, interest-rate derivatives, bond portfolios, and FICC quant or AI research. Use when Codex needs to apply broker research frameworks, route questions to fixed-income playbooks, distinguish framework facts from current data, and produce auditable research drafts without fabricating market data or investment advice.
---
```

- [ ] **Step 2: 写 `SKILL.md` 主体**

必须包含这些一级或二级章节:

```text
# FICC Researcher
## Operating Principles
## Workflow
## Data Source Priority
## Routing
## Output Contract
## Prohibited Behavior
## Validation
```

核心内容:

- 先读 `references/00-routing.md`。
- 根据问题读取 1 到 3 个 playbook。
- 需要数据时先按 `references/02-data-source-policy.md` 判断数据源。
- 需要源报告溯源时查 `references/01-source-index.yml`。
- 不伪造实时收益率、信用利差、估值、评级、成交、持仓、净值。
- 输出必须区分框架事实、数据事实和推断判断。

- [ ] **Step 3: 写 `agents/openai.yaml`**

建议内容:

```yaml
display_name: FICC Researcher
short_description: Fixed-income research routing and analysis framework for rates, credit, convertibles, institutions, offshore bonds, ABS, REITs, and derivatives.
default_prompt: Use FICC Researcher to analyze this fixed-income question. Route the request to the relevant playbooks, identify required data, distinguish broker framework evidence from current market data, and produce an auditable research draft with risks and follow-up indicators.
```

- [ ] **Step 4: 验证入口文件存在**

Run:

```powershell
Test-Path .\SKILL.md; Test-Path .\agents\openai.yaml
```

Expected:

```text
True
True
```

### 阶段 2: 建立路由和数据源政策

**Files:**
- Create: `<repo-root>\references\00-routing.md`
- Create: `<repo-root>\references\02-data-source-policy.md`

- [ ] **Step 1: 写 `00-routing.md` 的路由表**

必须包含以下路由:

```text
利率/宏观/曲线/久期 -> rates-macro.md + bond-strategy.md
资金面/央行/财政供给 -> rates-macro.md + institution-behavior.md
信用利差/资产荒/信用下沉 -> credit-strategy.md + institution-behavior.md
城投/化债/区域利差 -> city-investment-bonds.md + credit-strategy.md
二永债/银行资本债/券商保险债 -> financial-credit.md + institution-behavior.md
理财赎回/净值化/基金行为 -> wealth-management-funds.md + institution-behavior.md
转债/可交债/混合资本工具 -> convertible-hybrid.md
国债期货/利率互换/基差 -> derivatives.md + rates-macro.md
美债/美元债/点心债/离岸人民币债 -> offshore-global-rates.md
ABS/公募REITs -> abs-reits.md
固收量化/AI投研/因子/监控 -> quant-ai-research.md
```

- [ ] **Step 2: 写 `02-data-source-policy.md`**

必须包含:

- 数据源优先级。
- MCP 中央化原则。
- iFinD、Tushare、Wind、本地数据库、Web 的适用边界。
- 缺失数据时的输出格式。
- 密钥和敏感信息禁止入库。

缺失数据输出格式:

```text
当前缺少数据:
- 字段:
- 推荐来源:
- 时间范围:
- 频率:
- 用途:
在缺少以上数据前，只能给出框架判断，不能给出当前市场结论。
```

- [ ] **Step 3: 验证路由文件可读**

Run:

```powershell
Select-String -Path .\references\00-routing.md -Pattern '信用利差','转债','MCP'
Select-String -Path .\references\02-data-source-policy.md -Pattern 'iFinD','Tushare','Wind','不得伪造'
```

Expected:

```text
至少各返回 1 行匹配。
```

### 阶段 3: 建立源报告索引

**Files:**
- Create: `<repo-root>\references\01-source-index.yml`
- Create: `<repo-root>\scripts\build_source_index.py`

- [ ] **Step 1: 写 `01-source-index.yml`**

每篇源报告使用统一字段:

```yaml
- id: cicc-bond-principles-strategy-2025
  institution: CICC
  title: 债券分析的原理与策略
  source_file: references/source-reports/【中金固收·重磅推荐】债券分析的原理与策略——中金固收2025年债市宝典系列_2056241724339720192.md
  primary_playbooks:
    - rates-macro
    - bond-strategy
  keywords:
    - 债券分析
    - 收益率曲线
    - 资金面
    - 供需关系
    - 投资者行为
  source_role: framework
```

23 篇报告全部纳入索引。

- [ ] **Step 2: 写 `build_source_index.py`**

脚本职责:

- 扫描 `references/source-reports/*.md`。
- 输出文件数量。
- 检查 `01-source-index.yml` 中 `source_file` 是否全部存在。
- 检查是否有未索引 `.md`。
- 返回非 0 退出码表示校验失败。

- [ ] **Step 3: 运行索引校验**

Run:

```powershell
python .\scripts\build_source_index.py
```

Expected:

```text
source_reports_count=23
indexed_reports_count=23
missing_files=0
unindexed_files=0
```

### 阶段 4: 建立第一批 playbook

**Files:**
- Create: `<repo-root>\references\playbooks\rates-macro.md`
- Create: `<repo-root>\references\playbooks\bond-strategy.md`
- Create: `<repo-root>\references\playbooks\institution-behavior.md`
- Create: `<repo-root>\references\playbooks\credit-strategy.md`
- Create: `<repo-root>\references\playbooks\convertible-hybrid.md`

- [ ] **Step 1: 使用统一 playbook 模板**

每个 playbook 必须包含:

```text
# [Playbook Name]

## Scope
## When To Use
## Required Inputs
## Framework
## Analysis Steps
## Output Template
## Risk Checks
## Source Reports
## Search Keywords
```

- [ ] **Step 2: 写 `rates-macro.md`**

覆盖:

- 经济基本面、通胀、资金面、货币政策、财政供给、汇率约束。
- 低利率环境下传统框架失效、财政和工业链条的重要性。
- 当前数据缺失时，只输出指标清单和判断路径。

- [ ] **Step 3: 写 `bond-strategy.md`**

覆盖:

- 久期、曲线、杠杆、骑乘、套息、二级价差、持有回报。
- 组合构建中供给、需求、收益率曲线、信用利差和投资约束的联动。

- [ ] **Step 4: 写 `institution-behavior.md`**

覆盖:

- 商业银行、保险、银行理财、公募基金、券商自营、外资、年金。
- 负债端、税收、监管、会计、杠杆、投资范围和行为约束。
- 机构行为对利率债、信用债、短端、长端和流动性的影响。

- [ ] **Step 5: 写 `credit-strategy.md`**

覆盖:

- 信用债市场结构、信用风险怎么看、评级框架、信用利差、资产荒和动态策略。
- 城投、产业、金融信用债先只做跳转，不在本文件展开全部细节。

- [ ] **Step 6: 写 `convertible-hybrid.md`**

覆盖:

- 平价、转股溢价率、债底、条款博弈、赎回、回售、下修。
- 可交债、优先股、混合票据、雪球等混合资产的后续扩展入口。

- [ ] **Step 7: 人工抽查 playbook 可用性**

检查每个文件是否能回答:

```text
这个 playbook 何时使用？
需要哪些数据？
没有数据时怎么输出？
引用哪些源报告？
有哪些常见误判？
```

### 阶段 5: 建立图表笔记

**Files:**
- Create: `<repo-root>\references\chart-notes\key-framework-charts.md`

- [ ] **Step 1: 转写至少 5 张关键图**

首批图表:

```text
1. 中金债券组合构建框架
2. 华泰投资者行为图谱
3. 华泰信用债品种演化图
4. 华泰 IS-LM 利率理论图
5. 转债条款/估值/择券框架图
```

每张图记录:

```text
## 图名
- Source report:
- Original image URL:
- Core message:
- Use when:
- Do not use when:
- Text reconstruction:
```

- [ ] **Step 2: 检查图片 URL 不作为唯一依据**

每张图必须有 `Text reconstruction`，即使 URL 失效也能使用。

### 阶段 6: 建立验证脚本

**Files:**
- Create: `<repo-root>\scripts\validate_skill_links.py`

- [ ] **Step 1: 写路径校验脚本**

脚本检查:

- `SKILL.md` 存在。
- `agents/openai.yaml` 存在。
- `references/00-routing.md` 存在。
- `references/01-source-index.yml` 存在。
- `references/02-data-source-policy.md` 存在。
- `references/playbooks/*.md` 数量不少于 5。
- `references/source-reports/*.md` 数量为 23。

- [ ] **Step 2: 运行路径校验**

Run:

```powershell
python .\scripts\validate_skill_links.py
```

Expected:

```text
ok: SKILL.md
ok: agents/openai.yaml
ok: references/00-routing.md
ok: references/01-source-index.yml
ok: references/02-data-source-policy.md
ok: playbooks_count>=5
ok: source_reports_count=23
validation_passed=true
```

### 阶段 7: 使用 skill-creator 验证

**Files:**
- Validate: `<repo-root>`

- [ ] **Step 1: 运行 quick_validate**

Run:

```powershell
python <local-skill-creator>\scripts\quick_validate.py <repo-root>
```

Expected:

```text
validation passed
```

如果输出格式不同，以退出码 `0` 为通过标准。

- [ ] **Step 2: 检查 Git 状态**

Run:

```powershell
git status --short --branch
```

Expected:

```text
## master
?? SKILL.md
?? agents/openai.yaml
?? references/00-routing.md
?? references/01-source-index.yml
?? references/02-data-source-policy.md
?? references/playbooks/
?? references/chart-notes/key-framework-charts.md
?? scripts/
```

实际输出可能包含已有 `.gitkeep` 和 source reports，提交前需要人工确认是否全部纳入首提交。

## MCP 借鉴落实方案

第一阶段不直接写真实 `.mcp.json` 密钥或连接配置，只写数据源政策。

第二阶段可增加:

```text
references/03-mcp-connectors.md
.mcp.example.json
```

`.mcp.example.json` 只允许写无密钥模板:

```json
{
  "mcpServers": {
    "ifind": {
      "type": "stdio-or-http",
      "description": "iFinD finance data connector; configure locally with user credentials outside git."
    },
    "tushare": {
      "type": "stdio-or-http",
      "description": "Tushare data connector; token must be stored outside git."
    },
    "wind-local": {
      "type": "local",
      "description": "Local Wind or exported Wind data bridge; no credentials in repository."
    },
    "bond-database": {
      "type": "local",
      "description": "Local bond database for curves, spreads, issuers, ratings, holdings, and fund NAV."
    }
  }
}
```

MCP 进入 playbook 的方式:

- playbook 写“需要什么字段”。
- `02-data-source-policy.md` 写“优先从哪个连接器拿”。
- `SKILL.md` 写“缺少连接器时如何降级”。
- 不在 playbook 中硬编码 token、URL、私有地址。

## 验收测试问题

完成后至少用以下问题测试:

1. `当前低利率环境下，10 年国债收益率上行需要哪些条件？`
2. `信用利差处于低位时，信用债还能怎么做收益？`
3. `银行理财赎回为什么会影响信用债和短端利率？`
4. `转债估值应该看平价溢价率还是债底？`
5. `城投化债背景下，区域利差该如何分析？`
6. `如果没有实时数据，你能给出哪些数据清单和分析路径？`

每个测试输出必须包含:

- 结论或框架判断。
- 使用的 playbook。
- 需要或已使用的数据。
- 源报告依据。
- 风险和反例。
- 不足和后续跟踪指标。

## 首提交建议

用户明确要求提交时，再执行 Git 提交。

建议首提交范围:

```powershell
git add .gitignore SKILL.md agents references scripts docs
git commit -m "文档：初始化 FICC Researcher 固收分析技能框架

改动原因：
- 建立固定收益分析 skill 的独立仓库和可追溯项目结构。

改动内容：
- 新增 skill 入口、元数据、路由、数据源政策、源报告索引、首批 playbook 和验证脚本。
- 整理中金、华泰固收框架 Markdown 为源报告证据库。

验证情况：
- 运行 skill-creator quick_validate。
- 运行 source index 和 link validation 脚本。

注意事项：
- 不包含任何密钥、token 或真实 MCP 凭据。
- 输出仅作为研究辅助，不能替代投资决策。

后续方向：
- 补充更多专题 playbook，并接入本地 iFinD、Tushare、Wind 或债券数据库。"
```

## 执行顺序结论

先做入口和路由，再做源报告索引，再做首批 5 个 playbook，最后做图表笔记和验证脚本。

不要先写全部 12 个 playbook。第一批只做高频主干:

```text
rates-macro
bond-strategy
institution-behavior
credit-strategy
convertible-hybrid
```

通过验收问题后，再扩展城投、大金融、理财、衍生品、海外债、ABS/REITs、量化 AI。
