# FICC Researcher 03B Data Workflow And Eval Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 `ficc-researcher` 从“可用的固收研究 skill”升级为“可跨 Codex、OpenClaw、Claude 和个人 agent 使用的固定收益研究工作流包”，重点补齐数据接口目录、workflow 入口、研报框架决策链和可回归验证体系。

**Architecture:** 保持单一 `ficc-researcher` skill 入口，继续遵守 `skill-creator` 的渐进披露原则：`SKILL.md` 只负责路由和核心纪律，专题框架放在 `references/`，可复用输出放在 `assets/templates/`，重复验证放在 `scripts/` 或 `evals/`。借鉴 Anthropic financial-services 的“core vertical plugin + workflow skills/commands + centralized connectors”思想，但不照搬其插件结构；FICC 内部用 `references/10-workflow-entrypoints.md` 模拟命令入口，用 `references/09-data-interface-catalog.md` 统一数据需求与连接器边界。

**Tech Stack:** Markdown, YAML, Python, Git, Codex skill conventions, OpenClaw workspace skills, optional Tushare/iFinD/Wind/local database/WebSearch connectors, broker-framework Markdown references.

---

## 背景与定位

### 为什么需要 03B

已有 `03-ficc-researcher-vm-framework-upgrade.md` 解决的是 VM 同步、宏观框架增强和 OpenClaw 文件滞后问题。本方案不重复 VM 同步，而是承接当前实测结果：

- FICC skill 能正确路由到 rates-macro、bond-strategy、macro glossary 和 policy reaction。
- OpenClaw 上 Tushare MCP / skill 已能完成 `trade_cal`、`sf_month`、`cn_m`、`cn_cpi`、`cn_ppi` 等最小联动测试。
- 目前输出质量已经可用，但仍依赖 agent 自己猜“该找哪些数据”和“该用哪个模板”。

03B 的核心目标是把这种隐性经验显式化，让下一个 agent 不需要重新摸索。

### 外部参考如何吸收

- `skill-creator`: 保持 `SKILL.md` 简洁，详细框架一层引用到 `references/`；脚本只做确定性验证，不把大量金融知识塞进主入口。
- Anthropic financial-services: 借鉴 agents / skills / commands / connectors 分层、集中 MCP 配置、file-based 管理、check 脚本和 workflow command 映射。
- Anthropic LSEG 插件: 借鉴固定收益任务拆分方式，例如 bond relative value、fixed-income portfolio、macro-rates monitor、swap curve strategy、bond futures basis。
- 华泰《基本面分析的道与术》: 吸收“经济温度/周期季节、五部门/四循环、领先/同步/滞后指标、预期差、政策到市场”链条。
- 华泰《固收分析框架》: 吸收“基本面、政策、情绪/定价”三角，以及从需求、供给、价格、政策、市场定价共同解释债市的框架。
- 中金固收宝典系列: 继续作为利率、信用、城投、二永、理财、转债、衍生品、ABS/REITs、离岸债和 AI 投研的领域框架底座。

### 完成标准

执行完 03B 后，skill 应达到以下状态：

- 当前数据分析不再只靠自由发挥，而是先查 `09-data-interface-catalog.md`。
- 常见固收任务不再只靠自然语言路由，而是映射到 `10-workflow-entrypoints.md`。
- 宏观、利率、信用、机构行为和组合动作能用统一决策链输出。
- GitHub 仓库不包含 token、私有源报告、付费接口数据或大段第三方文档复制。
- 本地验证能检查新增文件、workflow 入口和 eval case 的结构。
- OpenClaw 能用 3 到 5 个固定 prompt 回归测试 skill 路由、数据纪律和输出结构。

## 范围边界

### 本阶段做

- 新增连接器中立的数据接口目录。
- 新增 Anthropic command 风格的 workflow 入口目录。
- 把华泰/中金研报方法进一步抽成“决策链”和“常见误判清单”。
- 扩展 README、SKILL 路由、数据源政策、MCP 说明和验证脚本。
- 新增 eval prompt 和预期结构，用于 Codex/OpenClaw 人工或半自动回归。

### 本阶段不做

- 不把 `references/source-reports/**` 推到 GitHub。
- 不写入 Tushare、iFinD、Wind 或任何数据服务 token。
- 不把 FICC playbook 绑定到某个具体 MCP server 名称。
- 不复制大段 Tushare 或券商报告原文。
- 不做真实交易建议、自动下单、组合托管或个人投资建议。
- 不在本阶段新增真实数据库或依赖复杂服务。

## 文件职责

### 新增文件

- `references/09-data-interface-catalog.md`: 连接器中立的数据需求目录，列出研究任务、字段、优先来源、Tushare/iFinD/Wind/WebSearch 可选入口、限制和缺失数据处理。
- `references/10-workflow-entrypoints.md`: 类 command 的 workflow 入口表，定义宏观数据点评、曲线复盘、信用利差复盘、机构行为、组合动作、政策事件、转债、日报等任务如何路由。
- `references/11-research-decision-chains.md`: 从研报抽出的跨 playbook 决策链，例如宏观到曲线、信用到机构、数据到组合动作。
- `evals/smoke-prompts.yml`: 固定回归 prompt 清单，包含任务、应读文件、允许数据源、禁止行为和预期输出块。
- `evals/expected-output-contracts.yml`: 每类 workflow 的最小输出字段要求。
- `scripts/validate_eval_cases.py`: 结构校验脚本，检查 eval YAML 字段完整性、引用文件存在、workflow 名称可解析。
- `docs/review/03B-ficc-researcher-data-workflow-eval-review.md`: 本方案审查记录。
- `docs/review/03B-openclaw-smoke-results.md`: 后续执行时记录 OpenClaw 回归结果。

### 修改文件

- `SKILL.md`: 只新增到 09/10/11 的导航，不塞具体接口表。
- `README.md`: 增加 Optional Data Connectors 和 Eval/Smoke Test 使用说明。
- `agents/openai.yaml`: 如默认提示已不能覆盖 09/10/11，则轻微更新。
- `references/00-routing.md`: 增加 workflow entrypoint 路由规则。
- `references/02-data-source-policy.md`: 引导读取 09，补充接口中立原则。
- `references/03-data-integration-policy.md`: 明确 connector result 转 data packet 后再交给 playbook。
- `references/04-mcp-connectors.md`: 补充 Tushare skill / MCP / Python workflow 的角色边界，但不写 token。
- `references/05-cross-platform-usage.md`: 补充 Codex、OpenClaw、Claude、个人 agent 的加载顺序和本地复制边界。
- `references/07-macro-indicator-glossary.md`: 增补 09 中宏观字段映射的跳转。
- `references/08-policy-reaction-function.md`: 增补政策事件 workflow 的输出约束。
- `references/playbooks/*.md`: 按需要补“读取 09/10/11”的轻量提示和常见误判。
- `assets/templates/*.md`: 补足模板中 source、query、retrieved_at、fields、row_count、limitations 字段。
- `scripts/validate_skill_links.py`: 将 09/10/11 和 eval 目录纳入结构校验。

## 设计原则

### 1. 数据接口只做目录，不做绑定

FICC skill 负责告诉 agent “该要什么数据、为什么要、缺了会影响什么”。Tushare、iFinD、Wind、WebSearch 或用户文件负责取数。即使 OpenClaw 中工具名叫 `tushareMcp`，仓库内也不应该要求所有 agent 必须使用这个名称。

推荐表达：

```text
research_need:
required_fields:
preferred_sources:
optional_connectors:
provider_notes:
missing_data_behavior:
```

禁止表达：

```text
必须调用 mcp__tushareMcp__xxx
把 token 写入这里
如果接口失败就根据常识补数据
```

### 2. Workflow 入口模拟 commands，但不强依赖 commands

Anthropic 的 commands 很适合团队协作，但 Codex/OpenClaw/Claude 的可用机制不完全一致。本阶段先用 `references/10-workflow-entrypoints.md` 定义“命令语义”，后续如果需要再拆成真实 `commands/` 目录。

例如：

```text
macro-data-commentary
-> rates-macro + bond-strategy + 07 + 08 + 09
-> macro-data-commentary-template
-> eval case: social-financing-release
```

### 3. 研报不再摘要化，改为决策链

03B 不追求把研报摘得更多，而是把研究员真正使用的链条抽出来：

```text
指标事实
-> 口径与预期差
-> 经济循环是否顺
-> 政策目标是否被触发
-> 资金面和供给如何反应
-> 曲线和信用如何定价
-> 组合动作与风险触发
```

### 4. 验证分两层

- 确定性验证：脚本检查文件、YAML、引用、模板字段。
- 行为验证：OpenClaw/Codex 用固定 prompt 产出，人工记录是否满足输出契约。

不要让脚本假装能判断金融结论是否正确。

## Task 1: 建立数据接口目录

**Files:**
- Create: `references/09-data-interface-catalog.md`
- Modify: `SKILL.md`
- Modify: `references/00-routing.md`
- Modify: `references/02-data-source-policy.md`
- Modify: `references/04-mcp-connectors.md`
- Modify: `README.md`

- [ ] **Step 1: 写入连接器中立的数据目录**

Create `references/09-data-interface-catalog.md` with these sections:

```markdown
# Data Interface Catalog

## Purpose
## Data Packet Standard
## Source Priority
## Macro Credit And Money
## Rates And Yield Curves
## Funding And Money Market
## Fiscal Supply
## Credit Spreads And Issuer Risk
## Institution Behavior
## Convertibles And Hybrid Assets
## Offshore And Global Rates
## ABS And REITs
## WebSearch And Official Sources
## Missing Data Rules
## Provider Compliance Notes
```

Core rules to include:

- Tushare can be listed as optional structured data source, not as mandatory dependency.
- Tushare `sf_month` can support social-financing aggregate fields such as `month`, `inc_month`, `inc_cumval`, `stk_endval` when permission allows.
- Tushare `yc_cb` can support ChinaBond treasury yield curve fields such as `trade_date`, `ts_code`, `curve_name`, `curve_type`, `curve_term`, `yield`, but the interface is separate-permission and should not be treated as guaranteed.
- 国开收益率、信用利差、二永债利差、城投区域利差、真实估值分位等优先使用 Wind、iFinD、ChinaBond、SHCH、local bond database or user-provided exports unless a verified Tushare interface exists.
- WebSearch can verify official releases and policy pages but cannot replace licensed current market data.

- [ ] **Step 2: Link 09 from `SKILL.md`**

Add one workflow step after current data-source policy:

```markdown
If a task needs live, historical, or user-supplied data fields, read `references/09-data-interface-catalog.md` to identify required fields, preferred sources, connector limitations, and missing-data behavior.
```

Do not add interface tables to `SKILL.md`.

- [ ] **Step 3: Link 09 from routing and policy files**

Update `references/00-routing.md`:

```markdown
- For current data, first route the research question, then read `references/09-data-interface-catalog.md` for field-level data requirements and source priority.
```

Update `references/02-data-source-policy.md`:

```markdown
For field-level connector mapping, read `references/09-data-interface-catalog.md`. This file defines data needs; it does not store credentials or provider-specific secrets.
```

- [ ] **Step 4: Update README connector section**

Add a short block:

```markdown
FICC Researcher does not bundle data, credentials, or proprietary datasets. It may work with Tushare, iFinD, Wind, local databases, official public pages, or WebSearch. Provider names in this repo are examples of optional data sources, not endorsements, sublicenses, or guarantees of coverage.
```

## Task 2: 建立 workflow 入口目录

**Files:**
- Create: `references/10-workflow-entrypoints.md`
- Modify: `SKILL.md`
- Modify: `references/00-routing.md`
- Modify: `README.md`
- Modify: `agents/openai.yaml`

- [ ] **Step 1: Define workflow entrypoints**

Create `references/10-workflow-entrypoints.md` with at least:

```markdown
# Workflow Entrypoints

## macro-data-commentary
## yield-curve-review
## credit-spread-review
## institution-flow-review
## portfolio-action-review
## policy-event-commentary
## convertible-review
## daily-bond-brief
## data-assisted-analysis
```

Each workflow must include:

```text
When to use:
Required playbooks:
Required references:
Required data:
Template:
Output blocks:
Forbidden shortcuts:
Eval case:
```

- [ ] **Step 2: Map workflows to existing templates**

Use this mapping:

| Workflow | Template |
| --- | --- |
| `macro-data-commentary` | `assets/templates/macro-data-commentary-template.md` |
| `yield-curve-review` | `assets/templates/yield-curve-review-template.md` |
| `credit-spread-review` | `assets/templates/credit-spread-review-template.md` |
| `institution-flow-review` | `assets/templates/framework-analysis-template.md` or new concise section in `daily-bond-brief-template.md` |
| `portfolio-action-review` | `assets/templates/portfolio-action-template.md` |
| `policy-event-commentary` | `assets/templates/policy-event-commentary-template.md` |
| `data-assisted-analysis` | `assets/templates/data-assisted-analysis-template.md` |
| `daily-bond-brief` | `assets/templates/daily-bond-brief-template.md` |

- [ ] **Step 3: Link workflows from `SKILL.md`**

Add:

```markdown
For recurring research products such as data commentary, curve review, credit-spread review, institution-flow review, policy-event commentary, or daily bond brief, read `references/10-workflow-entrypoints.md` and use the mapped template under `assets/templates/`.
```

- [ ] **Step 4: Update routing**

In `references/00-routing.md`, add:

```markdown
If the user asks for a repeatable research product rather than a one-off explanation, choose the workflow in `references/10-workflow-entrypoints.md` before choosing the final output template.
```

## Task 3: 抽取研报决策链

**Files:**
- Create: `references/11-research-decision-chains.md`
- Modify: `references/evidence-cards/macro-policy-evidence.md`
- Modify: `references/evidence-cards/rates-macro-evidence.md`
- Modify: `references/evidence-cards/credit-evidence.md`
- Modify: `references/evidence-cards/institution-wealth-evidence.md`
- Modify: `references/playbooks/rates-macro.md`
- Modify: `references/playbooks/bond-strategy.md`
- Modify: `references/playbooks/credit-strategy.md`
- Modify: `references/playbooks/institution-behavior.md`

- [ ] **Step 1: Create cross-playbook decision chains**

Create `references/11-research-decision-chains.md` with these chains:

```markdown
# Research Decision Chains

## Macro Release To Rates
指标事实 -> 口径/预期差 -> 经济循环 -> 政策反应 -> 资金/供给 -> 曲线 -> 组合动作

## Funding To Curve
央行操作 -> DR/R/NCD -> 杠杆成本 -> 短端锚 -> 曲线形态 -> 交易拥挤

## Fiscal Supply To Duration
发行计划 -> 缴款节奏 -> 配置吸收 -> 期限溢价 -> 10Y/30Y 风险

## Credit Spread To Allocation
利差水平 -> 基本面 -> 再融资 -> 机构需求 -> 流动性 -> 下沉/久期/票息

## Institution Behavior To Market
负债稳定性 -> 久期偏好 -> 杠杆能力 -> 净值波动 -> 赎回反馈 -> 利率/信用传导

## Policy Event To Portfolio
政策目标 -> 工具 -> 约束 -> 预期差 -> 可交易部分 -> 风险触发
```

- [ ] **Step 2: Add common misreadings**

Add concise bullets to the relevant playbooks:

- 社融高不等于私人需求强。
- PPI 反弹不等于全面需求过热。
- M2 强不等于交易活化。
- 财政发力同时包含增长支撑和债券供给压力。
- 信用利差低不等于信用风险消失。
- 宽资金不等于杠杆无风险。
- 研报历史样例不等于当前市场点位。

- [ ] **Step 3: Keep evidence cards as compressed source layer**

Do not paste long source-report passages. Add only:

```text
source_ids:
framework_points:
decision_chain:
common_errors:
data_needed:
```

## Task 4: 建立 eval prompt 和输出契约

**Files:**
- Create: `evals/smoke-prompts.yml`
- Create: `evals/expected-output-contracts.yml`
- Create: `scripts/validate_eval_cases.py`
- Modify: `scripts/validate_skill_links.py`
- Create: `docs/review/03B-openclaw-smoke-results.md`

- [ ] **Step 1: Create smoke prompt YAML**

Create `evals/smoke-prompts.yml` with cases:

```yaml
cases:
  - id: macro-social-financing
    workflow: macro-data-commentary
    prompt: "请使用 ficc-researcher 分析 2026 年 4 月社融、M1/M2、CPI/PPI 对债市的影响。优先使用已配置的结构化数据工具；缺少收益率和利差时必须列出缺口。"
    required_files:
      - SKILL.md
      - references/00-routing.md
      - references/07-macro-indicator-glossary.md
      - references/08-policy-reaction-function.md
      - references/09-data-interface-catalog.md
      - references/10-workflow-entrypoints.md
    forbidden:
      - fabricate_yields
      - fabricate_wind_consensus
      - personalized_investment_advice
  - id: yield-curve-no-data
    workflow: yield-curve-review
    prompt: "请评价当前 1Y/3Y/5Y/10Y/30Y 国债和国开曲线。若没有实时曲线数据，只能输出需要哪些数据和框架判断。"
    required_files:
      - references/playbooks/rates-macro.md
      - references/playbooks/bond-strategy.md
      - references/09-data-interface-catalog.md
    forbidden:
      - fabricate_current_curve
      - hide_missing_data
  - id: credit-spread-low-level
    workflow: credit-spread-review
    prompt: "请分析低利差环境下信用债下沉是否值得做，区分高等级、城投、二永债和弱资质主体。"
    required_files:
      - references/playbooks/credit-strategy.md
      - references/playbooks/city-investment-bonds.md
      - references/playbooks/financial-credit.md
      - references/11-research-decision-chains.md
    forbidden:
      - treat_carry_as_risk_free
  - id: institution-redemption
    workflow: institution-flow-review
    prompt: "如果理财和债基出现赎回压力，应如何分析对利率债、信用债和曲线的传导？"
    required_files:
      - references/playbooks/institution-behavior.md
      - references/playbooks/wealth-management-funds.md
      - references/11-research-decision-chains.md
    forbidden:
      - ignore_nav_feedback
```

- [ ] **Step 2: Create expected output contracts**

Create `evals/expected-output-contracts.yml` with required blocks:

```yaml
contracts:
  macro-data-commentary:
    required_blocks:
      - 问题归类
      - 使用 playbook
      - 数据来源与时间
      - 数据事实
      - 预期差
      - 政策反应函数
      - 债市传导
      - 不能确认的部分
      - 风险与反例
  yield-curve-review:
    required_blocks:
      - 曲线数据来源
      - 期限分段
      - 资金面
      - 供给与配置
      - 缺少数据
      - 风险触发
  credit-spread-review:
    required_blocks:
      - 利差数据来源
      - 信用风险
      - 流动性补偿
      - 机构需求
      - 下沉边界
      - 风险与反例
```

- [ ] **Step 3: Add deterministic validator**

Create `scripts/validate_eval_cases.py`:

```python
"""
文件路径: scripts/validate_eval_cases.py
文件作用: 校验 FICC Researcher eval prompt 与输出契约文件的结构完整性。
主要内容:
- load_simple_yaml: 使用 PyYAML 或内置降级解析读取 YAML
- validate_cases: 检查 case id、workflow、prompt、required_files、forbidden
- validate_contracts: 检查 workflow 输出契约
依赖关系:
- pathlib
- sys
- yaml 可选
使用场景:
- 修改 evals/*.yml 后运行，确认 smoke prompt 引用文件存在且 workflow 有输出契约
注意事项:
- 本脚本只校验结构，不评判金融分析质量
"""
```

If PyYAML is unavailable, fail with a clear message:

```text
missing_dependency: pyyaml
```

No new dependency should be installed in this task; the existing `.tmp_pyyaml` fallback can be reused when available.

- [ ] **Step 4: Extend `validate_skill_links.py`**

Add required files:

```python
"references/09-data-interface-catalog.md",
"references/10-workflow-entrypoints.md",
"references/11-research-decision-chains.md",
"evals/smoke-prompts.yml",
"evals/expected-output-contracts.yml",
"scripts/validate_eval_cases.py",
```

Expected final output:

```text
validation_passed=true
```

## Task 5: 强化模板的数据纪律

**Files:**
- Modify: `assets/templates/macro-data-commentary-template.md`
- Modify: `assets/templates/yield-curve-review-template.md`
- Modify: `assets/templates/credit-spread-review-template.md`
- Modify: `assets/templates/daily-bond-brief-template.md`
- Modify: `assets/templates/data-assisted-analysis-template.md`
- Modify: `assets/templates/portfolio-action-template.md`

- [ ] **Step 1: Add common data metadata block**

Each substantial template should include:

```text
数据来源:
接口/文件/网页:
查询参数:
as_of:
retrieved_at:
字段:
row_count:
单位:
limitations:
```

- [ ] **Step 2: Add missing-data fallback**

Each template should include:

```text
当前缺少数据:
- 字段:
- 推荐来源:
- 时间范围:
- 频率:
- 用途:
在缺少以上数据前，只能给出框架判断，不能给出当前市场结论。
```

- [ ] **Step 3: Add no-investment-advice line where action language appears**

For `portfolio-action-template.md`, add:

```text
以下为研究框架表达，不构成个人投资建议或收益承诺。
```

## Task 6: 更新跨平台与 README 说明

**Files:**
- Modify: `README.md`
- Modify: `references/05-cross-platform-usage.md`
- Modify: `.mcp.example.json`

- [ ] **Step 1: Cross-platform loading order**

Document:

```text
Codex:
SKILL.md -> routing -> workflow/data interface -> playbooks -> templates

OpenClaw:
workspace skill copy -> configured MCP/skill tools -> FICC data packet contract -> output template

Claude-style agents:
skill folder -> optional command semantics -> connector-neutral data packet

Personal agents:
copy public repo -> keep source reports local -> configure external data outside repo
```

- [ ] **Step 2: Connector safety block**

Add:

```text
Do not paste real token values into `.mcp.example.json`, README, playbooks, eval prompts, or test logs.
```

- [ ] **Step 3: Keep `.mcp.example.json` generic**

The example should show placeholders only. It should not include the user's real VM path, token, private endpoint, or host-specific details.

## Task 7: 本地验证与审查

**Files:**
- Modify: `docs/review/03B-ficc-researcher-data-workflow-eval-review.md`

- [ ] **Step 1: Run deterministic validation**

Run:

```powershell
python .\scripts\build_source_index.py
python .\scripts\validate_source_refs.py
python .\scripts\validate_skill_links.py
python .\scripts\validate_eval_cases.py
```

Expected:

```text
validation_passed=true
eval_validation_passed=true
```

- [ ] **Step 2: Run skill quick validate**

Run:

```powershell
python <local-skill-creator>\scripts\quick_validate.py <repo-root>
```

Expected:

```text
Skill is valid!
```

- [ ] **Step 3: Check ignored source reports**

Run:

```powershell
git ls-files references/source-reports
git status --short --ignored
```

Expected:

```text
references/source-reports/.gitkeep
```

Source report originals and images must remain ignored.

## Task 8: OpenClaw 回归测试记录

**Files:**
- Create or update: `docs/review/03B-openclaw-smoke-results.md`

- [ ] **Step 1: Sync public skill copy**

Use the existing public archive/sync approach. Exclude:

```text
.git/
.tmp*/
references/source-reports/**
outputs/
tmp/
```

- [ ] **Step 2: Run 3 to 5 prompts from `evals/smoke-prompts.yml`**

Minimum cases:

- `macro-social-financing`
- `yield-curve-no-data`
- `credit-spread-low-level`

- [ ] **Step 3: Record outputs**

For each case, record:

```text
case_id:
agent:
model:
retrieved_at:
tools_used:
files_read:
data_sources:
passed_blocks:
failed_blocks:
fabrication_check:
missing_data_check:
notes:
```

## Commit And Push Rules

Only commit/push when the user asks.

Before commit:

```powershell
git -c safe.directory='D:/000AAA_Datas/Python/Skills/FICC_Researcher' status --short --branch
git ls-files references/source-reports
```

Commit message must be Chinese and include:

- 改动原因
- 改动内容
- 验证情况
- 注意事项
- 后续方向

## Risks And Rollback

### Risks

- 数据接口目录可能让 agent 误以为 Tushare 覆盖所有固收数据。控制方式：每个接口都写“可尝试/需权限/优先替代来源”。
- eval prompt 可能变成形式主义。控制方式：输出契约只检查结构，金融结论仍需人工审查。
- Workflow 入口过多会稀释 skill。控制方式：只覆盖高频固收研究产品，不建完整 command 系统。
- README 引用外部数据源可能被误读为背书。控制方式：写明 optional connector、用户自行合规、无数据再分发。

### Rollback

- 若 09/10/11 让 SKILL 过重，保留文件但从 `SKILL.md` 中移除默认读取，只在 routing 中按需读取。
- 若 eval 目录增加维护成本，保留 `smoke-prompts.yml`，移除脚本强校验。
- 若 OpenClaw 对新增文件无感，回滚同步目录到备份副本。

## Current Status

本地 03B-A 与 03B-B 已执行完成：

- 已新增 `references/09-data-interface-catalog.md`、`references/10-workflow-entrypoints.md`、`references/11-research-decision-chains.md`。
- 已新增 `evals/smoke-prompts.yml`、`evals/expected-output-contracts.yml` 和 `scripts/validate_eval_cases.py`。
- 已更新 `SKILL.md`、README、routing、data policy、connector policy、cross-platform usage、核心 playbook 与模板。
- 已通过本地结构校验、source id 校验、eval case 校验和 `skill-creator` quick validate。

OpenClaw 03B-C 已完整执行：

- 已同步 03B 公开 skill 副本到 VM。
- VM 上结构校验和 eval 校验通过。
- `current-market-data-anti-hallucination` 最小 prompt 通过，agent 未编造实时点位。
- 旧 backup skill 目录已从 `skills/` 移到 `skills-backups/`，避免干扰 skill 读取。
- 已执行 `evals/smoke-prompts.yml` 中全部 10 个 OpenClaw eval case，10/10 PASS，0 FAIL，全部 `stderr_chars=0`。
