# FICC Researcher 04 Quality Examples And Connector Mapping Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 `ficc-researcher` 从“能跑通 10 个 OpenClaw eval case”升级为“有质量评分、公共样例、连接器映射和 OpenClaw 部署卫生标准的可复用固收研究 skill”。

**Architecture:** 继续保持单一 skill 入口和渐进披露结构：`SKILL.md` 只放核心路由和纪律，长框架放入一层 `references/`，可复用样例放入 `examples/`，确定性检查放入 `scripts/`，行为测试放入 `evals/` 和 `docs/review/`。Tushare、iFinD、Wind、WebSearch、用户文件和本地数据库都是外部数据生产者；FICC Researcher 只定义研究问题、数据字段、质量检查和解释框架。

**Tech Stack:** Markdown, YAML, Python, Git, Codex skill conventions, OpenClaw workspace skills, optional Tushare/iFinD/Wind/local database/WebSearch connectors.

---

## 背景

03B 已经完成：

- `SKILL.md` 能路由到 09 数据接口目录、10 workflow 入口、11 决策链。
- OpenClaw 10 个 eval case 全部 PASS。
- Tushare MCP / skill 已完成最小交易日历和宏观接口冒烟测试。
- 公开仓库没有纳入 `references/source-reports/**` 私有源研报。

04 号不再继续扩写研报摘要，而是解决下一层问题：

1. skill 入口和高频引用是否足够省上下文。
2. eval 是否能从“命令成功”升级到“质量可评分”。
3. agent 是否有 1 到 2 个可模仿的公开或脱敏黄金样例。
4. Tushare/iFinD/Wind/WebSearch 是否有清楚的字段映射，但不把凭证或具体 MCP 名称写死进 playbook。
5. OpenClaw 是否能避免旧备份目录、错误复制范围、源研报误同步等部署卫生问题。

## 范围边界

### 本阶段做

- 压缩并审查 `SKILL.md` 和高频引用文件的上下文预算。
- 新增质量评分 rubric 和对应结构校验。
- 新增 1 到 2 个公共或脱敏 golden examples。
- 新增连接器映射层，说明 Tushare/iFinD/Wind/WebSearch 与 FICC 数据字段之间的关系。
- 新增 OpenClaw skill 发现、同步、备份目录和验证的卫生规则。
- 更新 README、SKILL 导航和验证脚本。

### 本阶段不做

- 不提交 `references/source-reports/**` 源研报正文、图片或版权敏感材料。
- 不提交 Tushare、iFinD、Wind、OpenClaw、GitHub 或任何服务的 token、账号、私有端点。
- 不把 FICC playbook 绑定到 `mcp__tushareMcp__*` 这类平台专有工具名。
- 不实现真实数据下载服务或数据库。
- 不做自动交易、个人投资建议或收益承诺。

## 文件职责

### 预计新增

- `evals/quality-rubrics.yml`: 定义每个 workflow 的质量评分维度、硬性 gate 和人工评分说明。
- `scripts/validate_quality_rubrics.py`: 校验 rubric YAML 结构、workflow 覆盖、score/gate 字段和引用一致性。
- `examples/golden-cases/macro-social-financing-public-example.md`: 使用公开宏观数据或脱敏数据展示社融点评的合格输出结构。
- `examples/golden-cases/yield-curve-missing-data-example.md`: 展示缺少实时曲线数据时如何拒绝编造并输出数据需求。
- `examples/data/macro-social-financing-public-sample.yml`: 体积很小的公共或脱敏 data packet 样例。
- `references/12-data-connector-mapping.md`: 连接器中立的字段映射表，覆盖 Tushare/iFinD/Wind/WebSearch/local database 的适用边界。04A 先创建可校验的最小骨架，04D 再扩展完整映射。
- `references/13-openclaw-skill-hygiene.md`: OpenClaw skill 同步、发现、备份、eval 运行和敏感数据排除规则。04A 先创建可校验的最小骨架，04E 再扩展完整运行说明。
- `docs/review/04-quality-implementation-results.md`: 后续执行时记录质量评分、样例和 OpenClaw 复测结果。

### 预计修改

- `SKILL.md`: 只增加 12/13 的导航规则；不塞接口表和运行命令。
- `README.md`: 增加 quality eval、golden examples、connector mapping 和 OpenClaw hygiene 的说明。
- `references/02-data-source-policy.md`: 补充 provider 引用和许可边界。
- `references/04-mcp-connectors.md`: 指向 12，强调 connector 配置外置。
- `references/05-cross-platform-usage.md`: 指向 13，说明 Codex/OpenClaw/Claude/个人 agent 的复制边界。
- `references/09-data-interface-catalog.md`: 保持研究字段目录职责，必要时把 provider-specific 细节移到 12。
- `references/10-workflow-entrypoints.md`: 给每个 workflow 标注对应 rubric。
- `evals/smoke-prompts.yml`: 可选地给 case 增加 `rubric` 字段。
- `evals/expected-output-contracts.yml`: 保持输出块契约，不承担质量评分。
- `scripts/validate_eval_cases.py`: 如新增 `rubric` 字段，则校验对应 rubric 存在。
- `scripts/validate_skill_links.py`: 纳入 12/13、examples 和新增校验脚本的存在性检查。

## 设计原则

### 1. SKILL.md 只做启动器

`SKILL.md` 应回答：

- 什么时候触发。
- 第一批该读哪些文件。
- 数据纪律是什么。
- 输出合同是什么。

`SKILL.md` 不应回答：

- 每个 Tushare 接口怎么调用。
- 每种券商框架的全部细节。
- OpenClaw 如何写入 token。
- 某个市场的当前点位。

### 2. Eval 分两层

- `expected-output-contracts.yml`: 检查回答有没有关键块。
- `quality-rubrics.yml`: 检查回答质量，包含硬性 gate 和人工评分维度。

脚本只做结构校验和基础统计，不假装能自动判断金融结论全部正确。金融质量需要抽样人工复核或另一个 agent 做盲评。

### 3. Golden examples 只用公开或脱敏数据

样例的作用是让 Codex/OpenClaw/Claude 明白合格答案长什么样，不是分发数据。

允许：

- 官方公开网页上可引用的少量指标。
- 用户明确可公开的脱敏 data packet。
- “缺少数据时如何回答”的结构样例。

禁止：

- 券商研报大段原文。
- Wind/iFinD/付费数据库导出表。
- 私有持仓、账户、订单、token、内网地址。

### 4. Provider 映射不等于绑定

`references/12-data-connector-mapping.md` 可以写：

```text
research_field: social_financing_increment
preferred_sources: PBOC, iFinD, Wind, Tushare where licensed
tushare_candidate: sf_month
required_metadata: source, provider, interface_or_file, query, as_of, retrieved_at, fields, row_count, limitations
missing_data_behavior: only compare with previous value if consensus is unavailable
```

不可以写：

```text
必须调用 mcp__tushareMcp__sf_month
write a concrete provider credential assignment in repository files
如果接口没有数据就根据新闻补一个数
```

### 5. OpenClaw 卫生优先于多实例复杂度

OpenClaw 侧重点是一个干净、可复现、只读的 skill 副本：

- active skill 目录只保留 `ficc-researcher/`。
- 旧备份目录移到 `skills-backups/`，避免被 skill discovery 误读。
- `source-reports/` 不同步或只保留 `.gitkeep`。
- eval 输出放在 `outputs/openclaw-evals/`，不提交私有日志。

## Task 1: 压缩入口和高频引用

**Files:**
- Modify: `SKILL.md`
- Modify: `references/09-data-interface-catalog.md`
- Modify: `references/10-workflow-entrypoints.md`
- Create: `references/12-data-connector-mapping.md` as a minimal but valid stub before linking from `SKILL.md`
- Create: `references/13-openclaw-skill-hygiene.md` as a minimal but valid stub before linking from `SKILL.md`
- Create or update after execution: `docs/review/04-quality-implementation-results.md`

- [ ] **Step 1: 记录上下文预算基线**

Run:

```powershell
(Get-Content .\SKILL.md | Measure-Object -Line -Word).ToString()
(Get-Content .\references\09-data-interface-catalog.md | Measure-Object -Line -Word).ToString()
(Get-Content .\references\10-workflow-entrypoints.md | Measure-Object -Line -Word).ToString()
```

Expected:

```text
SKILL.md stays comfortably below 500 lines.
09 and 10 may be longer, but must remain targeted and directly linked from SKILL.md.
```

- [ ] **Step 2: Create minimal 12/13 reference stubs before linking**

Create `references/12-data-connector-mapping.md` with this minimal content:

```markdown
# Data Connector Mapping

## Purpose

Map FICC research fields to optional data-source families. This file defines field expectations, provider boundaries, citation metadata, and missing-data downgrades. It does not configure credentials, private endpoints, or mandatory MCP tool names.

## Compliance Boundary

- Treat Tushare, iFinD, Wind, local databases, official sources, and WebSearch as optional external data producers.
- Do not write tokens, API keys, account identifiers, private endpoints, or paid raw exports in this repository.
- Provider documents, user permissions, and service terms govern exact interface availability.

## Minimal Mapping

| Research field | Preferred official source | Optional structured sources | Required metadata | Missing-data downgrade |
| --- | --- | --- | --- | --- |
| Social financing aggregate | PBOC | Tushare, iFinD, Wind, local macro database | provider, interface_or_file, query, as_of, retrieved_at, fields, row_count, limitations | Without decomposition or consensus, compare only with previous value and state missing fields. |
| China treasury curve | ChinaBond or official/market data source where available | Wind, iFinD, local bond database, Tushare where licensed | curve type, tenor, yield, trade date, source, retrieved_at, fields, limitations | Without current curve data, provide framework and required fields only. |

## Expansion Plan

04D expands this file into macro, rates, funding, credit, convertibles, institution behavior, official-source, and WebSearch sections.
```

Create `references/13-openclaw-skill-hygiene.md` with this minimal content:

```markdown
# OpenClaw Skill Hygiene

## Purpose

Define safe sync, discovery, backup, and smoke-test rules for using `ficc-researcher` inside OpenClaw.

## Safe Sync Boundary

- Sync only public, Git-tracked skill files unless the user explicitly chooses a private local workflow.
- Do not sync `references/source-reports/**` except `references/source-reports/.gitkeep`.
- Do not sync `.env`, tokens, private logs, local outputs, or paid database exports.
- Keep backup directories outside active `skills/`, for example `skills-backups/`.

## Minimum Smoke Test

After sync, run local validation scripts in the OpenClaw skill directory and one anti-hallucination prompt before trusting current-data answers.

## Expansion Plan

04E expands this file into detailed directory layout, sync commands, eval sequence, and troubleshooting.
```

- [ ] **Step 3: 去除重复说明**

Check whether the same rule is repeated in `SKILL.md`, `02-data-source-policy.md`, `04-mcp-connectors.md`, and `09-data-interface-catalog.md`.

Keep this pattern:

```markdown
- `SKILL.md`: one-line instruction and link.
- `02-data-source-policy.md`: source priority and missing-data discipline.
- `04-mcp-connectors.md`: connector configuration boundary.
- `09-data-interface-catalog.md`: research fields and provider limits.
- `12-data-connector-mapping.md`: provider-specific field mapping.
```

- [ ] **Step 4: Add a small navigation link to 12 and 13**

Update `SKILL.md` workflow with concise lines:

```markdown
If provider-specific field mapping is needed, read `references/12-data-connector-mapping.md`.
If deploying or syncing this skill into OpenClaw, read `references/13-openclaw-skill-hygiene.md`.
```

- [ ] **Step 5: Validate**

Run:

```powershell
python .\scripts\validate_skill_links.py
python <local-skill-creator>\scripts\quick_validate.py .
```

Expected:

```text
validation_passed=true
Skill is valid!
```

## Task 2: 将 eval 升级为质量评分

**Files:**
- Create: `evals/quality-rubrics.yml`
- Create: `scripts/validate_quality_rubrics.py`
- Modify: `evals/smoke-prompts.yml`
- Modify: `scripts/validate_eval_cases.py`
- Modify: `README.md`

- [ ] **Step 1: Create `evals/quality-rubrics.yml`**

Use this schema:

```yaml
rubrics:
  macro-data-commentary:
    hard_gates:
      - no_fabricated_market_data
      - source_and_timestamp_present
      - missing_data_block_when_needed
      - no_personalized_investment_advice
    scoring:
      source_traceability:
        max_score: 2
        pass_threshold: 1
      data_quality_discipline:
        max_score: 2
        pass_threshold: 1
      playbook_routing:
        max_score: 2
        pass_threshold: 1
      ficc_reasoning_depth:
        max_score: 3
        pass_threshold: 2
      risk_and_counterexample:
        max_score: 2
        pass_threshold: 1
      actionability_without_advice:
        max_score: 2
        pass_threshold: 1
    minimum_total_score: 9
```

Cover all workflows currently in `evals/expected-output-contracts.yml`.

- [ ] **Step 2: Add rubric references to smoke cases**

Update each case in `evals/smoke-prompts.yml`:

```yaml
    rubric: macro-data-commentary
```

The value must match a key under `quality-rubrics.yml`.

- [ ] **Step 3: Implement validator**

Create `scripts/validate_quality_rubrics.py` with the same file-header style used by existing scripts:

```python
"""
文件路径: scripts/validate_quality_rubrics.py
文件作用: 校验 FICC Researcher 质量评分 rubric 的结构完整性。
主要内容:
- load_yaml: 读取 YAML，并在本地 .tmp_pyyaml 存在时自动加入路径
- validate_rubrics: 检查 hard_gates、scoring、minimum_total_score
- main: 输出校验结果并用退出码表示是否通过
依赖关系:
- pathlib
- sys
- yaml 可选，本仓库可使用 .tmp_pyyaml 作为本地校验依赖
使用场景:
- 修改 evals/quality-rubrics.yml 或 evals/*.yml 后运行
注意事项:
- 本脚本只校验 rubric 结构，不判断金融结论质量
"""
```

Responsibilities:

```text
- Load evals/quality-rubrics.yml.
- Load evals/expected-output-contracts.yml.
- Ensure every output contract has a rubric.
- Ensure every smoke case with rubric points to an existing rubric.
- Ensure every rubric has hard_gates, scoring, and minimum_total_score.
- Ensure scoring dimensions use positive integer max_score and pass_threshold <= max_score.
```

- [ ] **Step 4: Wire eval-case validation**

Extend `scripts/validate_eval_cases.py`:

```text
- If a smoke case has a rubric field, check it exists.
- Do not require rubric for backward compatibility until 04 is complete.
```

- [ ] **Step 5: Validate**

Run:

```powershell
python .\scripts\validate_eval_cases.py
python .\scripts\validate_quality_rubrics.py
```

Expected:

```text
eval_validation_passed=true
quality_rubrics_validation_passed=true
```

## Task 3: 增加公共或脱敏 golden examples

**Files:**
- Create: `examples/golden-cases/macro-social-financing-public-example.md`
- Create: `examples/golden-cases/yield-curve-missing-data-example.md`
- Create: `examples/data/macro-social-financing-public-sample.yml`
- Create: `scripts/validate_examples.py`
- Modify: `README.md`
- Modify: `scripts/validate_skill_links.py`

- [ ] **Step 1: Create data packet sample**

Create `examples/data/macro-social-financing-public-sample.yml`:

```yaml
source: official_public_or_desensitized_example
provider: synthetic_desensitized_example
interface_or_file: examples/data/macro-social-financing-public-sample.yml
query: macro_social_financing_monthly_sample
as_of: "2026-04"
retrieved_at: "2026-05-20 09:00:00 Asia/Shanghai"
time_range: "2026-03 to 2026-04"
frequency: monthly
universe: china_macro
fields:
  - indicator
  - period
  - value
  - unit
  - source_note
row_count: 2
units: mixed
limitations:
  - "Synthetic desensitized sample for output-shape training; do not use as market fact."
  - "Do not paste licensed database exports into this example file."
records:
  - indicator: social_financing_increment
    period: "2026-04"
    value: 6200
    unit: "CNY 100mn"
    source_note: "synthetic rounded value; replace with official or connector data in real analysis"
  - indicator: m2_yoy
    period: "2026-04"
    value: 8.6
    unit: "percent"
    source_note: "synthetic example field; replace with official or connector data in real analysis"
```

If replacing this with public values, use only small source-attributed values from official public pages and update `provider`, `source`, `retrieved_at`, `row_count`, `records`, and `limitations`.

- [ ] **Step 2: Create macro golden example**

The example must include:

```markdown
# Macro Social Financing Public Example

## Prompt
## Files The Agent Should Read
## Data Packet
## Expected Answer Shape
## Why This Is Good
## What Would Fail
```

Mandatory failure examples:

```text
- Calls "低于预期" without consensus data.
- Invents current 10Y CGB or DR007.
- Treats social financing aggregate as private endogenous demand without decomposition.
```

- [ ] **Step 3: Create missing-curve example**

The example must show that a good answer can be valuable even with no market data:

```markdown
# Yield Curve Missing Data Example

## Prompt
## Missing Fields
## Allowed Framework Analysis
## Forbidden Claims
## Expected Answer Shape
```

- [ ] **Step 4: Validate examples**

Create `scripts/validate_examples.py` with the same file-header style used by existing scripts:

```python
"""
文件路径: scripts/validate_examples.py
文件作用: 校验 FICC Researcher golden examples 和样例 data packet 的结构与敏感信息边界。
主要内容:
- validate_markdown_examples: 检查 golden-case Markdown 必需章节
- validate_data_packets: 检查 examples/data YAML 必需字段
- scan_secret_patterns: 扫描真实凭证赋值、API key 赋值、密码赋值和 OpenAI-style key
- main: 输出校验结果并用退出码表示是否通过
依赖关系:
- pathlib
- re
- sys
- yaml 可选，本仓库可使用 .tmp_pyyaml 作为本地校验依赖
使用场景:
- 新增或修改 examples/ 后运行，确认样例可被 agent 安全学习
注意事项:
- 本脚本只校验结构和敏感信息模式，不判断金融结论质量
"""
```

Responsibilities:

```text
- Ensure examples/golden-cases exists.
- Ensure every markdown example has Prompt, Expected Answer Shape, and What Would Fail or Forbidden Claims.
- Ensure examples/data YAML files include source, provider, retrieved_at, fields, row_count, limitations.
- Scan example files for forbidden secret patterns: concrete provider credential assignment, API key assignment, password assignment, or model/API key shapes with real-looking values.
```

- [ ] **Step 5: Validate**

Run:

```powershell
python .\scripts\validate_examples.py
python .\scripts\validate_skill_links.py
```

Expected:

```text
examples_validation_passed=true
validation_passed=true
```

## Task 4: 建立连接器映射层

**Files:**
- Modify: `references/12-data-connector-mapping.md`
- Modify: `references/02-data-source-policy.md`
- Modify: `references/04-mcp-connectors.md`
- Modify: `references/09-data-interface-catalog.md`
- Modify: `README.md`

- [ ] **Step 1: Expand connector mapping reference**

Replace the 04A stub in `references/12-data-connector-mapping.md` with sections:

```markdown
# Data Connector Mapping

## Purpose
## Compliance Boundary
## Data Packet Metadata
## Macro And Money
## Rates And Curves
## Funding And Money Market
## Credit Spreads
## Convertibles
## Institution Behavior
## Official Sources And WebSearch
## Provider Citation Notes
## Missing Data Downgrade Rules
```

- [ ] **Step 2: Add provider-neutral mapping rows**

Use this row shape:

```markdown
| Research field | Preferred official source | Optional structured sources | Tushare candidate | iFinD/Wind/local candidate | Required metadata | Missing-data downgrade |
| --- | --- | --- | --- | --- | --- | --- |
| Social financing aggregate | PBOC | Tushare, iFinD, Wind | `sf_month` if licensed | macro indicator panel | period, value, unit, source, retrieved_at | no expectation or decomposition claim without supporting data |
```

Important:

- Mention Tushare as an optional candidate where useful.
- State that provider docs and service terms govern exact availability.
- Do not include token, API URL with token, private host, account name, or paid raw export.

- [ ] **Step 3: Move provider-specific detail out of 09 if needed**

If `references/09-data-interface-catalog.md` becomes too provider-specific, keep only:

```text
Research needs, required fields, preferred source families, important limits, missing-data behavior.
```

Move exact optional candidates such as `sf_month`, `cn_m`, `cn_cpi`, `yc_cb` into 12.

- [ ] **Step 4: Add citation guidance**

Add this policy:

```markdown
When an answer uses Tushare, iFinD, Wind, WebSearch, official pages, or a user file, it must cite provider/source name, interface or file, query parameters where safe, retrieved_at, fields, row_count, and limitations. Do not imply this repository redistributes provider data or represents the provider.
```

- [ ] **Step 5: Validate**

Run:

```powershell
python .\scripts\validate_skill_links.py
$secretPattern = ('(?i)(tok' + 'en|api[_-]?key|pass' + 'word|secret)\s*[:=]\s*["'']?[A-Za-z0-9_./+=-]{16,}|sk-[A-Za-z0-9]{20,}')
git ls-files | Select-String -NotMatch '^references/source-reports/' | ForEach-Object { Select-String -Path $_.Line -Pattern $secretPattern -ErrorAction SilentlyContinue }
```

Expected:

```text
validation_passed=true
No real secret assignment or OpenAI-style key in Git-tracked public files. Policy-only mentions are acceptable.
```

## Task 5: 固化 OpenClaw skill 发现和同步卫生

**Files:**
- Modify: `references/13-openclaw-skill-hygiene.md`
- Modify: `references/05-cross-platform-usage.md`
- Modify: `README.md`
- Create or update after execution: `docs/review/04-quality-implementation-results.md`

- [ ] **Step 1: Expand OpenClaw hygiene reference**

Replace the 04A stub in `references/13-openclaw-skill-hygiene.md` with sections:

```markdown
# OpenClaw Skill Hygiene

## Purpose
## Safe Sync Boundary
## Directory Layout
## Files To Exclude
## Backup Directory Rule
## MCP And Secret Boundary
## Smoke Test Sequence
## Eval Batch Sequence
## Troubleshooting
```

- [ ] **Step 2: Write safe sync boundary**

Required rules:

```markdown
- Sync only the public skill files needed by OpenClaw.
- Do not sync `references/source-reports/**` except `.gitkeep`.
- Do not sync `.env`, tokens, private logs, local outputs, or paid database exports.
- Keep backups outside active `skills/`, for example `skills-backups/`.
- Active skill discovery should see one `ficc-researcher/` directory, not `ficc-researcher.bak-*`.
```

Required safe sync command patterns:

```bash
# Preferred: create an archive from Git-tracked public files only.
git archive --format=tar HEAD | tar -xf - -C /tmp/ficc-researcher-public
rsync -a --delete /tmp/ficc-researcher-public/ ~/.openclaw/workspace/skills/ficc-researcher/
```

```powershell
# Windows-side audit before any manual copy.
git ls-files references/source-reports
git ls-files | Select-String -Pattern '^references/source-reports/' -NotMatch
```

Do not use a blind recursive copy from the working tree when `references/source-reports/` contains ignored private files.

- [ ] **Step 3: Add smoke-test sequence**

Use placeholders, not private hostnames:

```bash
cd ~/.openclaw/workspace/skills/ficc-researcher
python3 scripts/validate_skill_links.py
python3 scripts/validate_eval_cases.py
python3 scripts/validate_quality_rubrics.py
python3 scripts/validate_examples.py
```

Then run one anti-hallucination prompt and one data-assisted prompt in OpenClaw. Record results in `docs/review/04-quality-implementation-results.md`.

- [ ] **Step 4: Document common failures**

Include:

```markdown
- Agent reads `ficc-researcher.bak-*`: move backups outside active skills.
- Agent cannot see new references: resync public skill and rerun validation.
- Tushare MCP says token missing: fix local OpenClaw MCP config or use local Tushare Python output as a data packet; do not edit repository files with the real token.
- Agent fabricates current yields: rerun `current-market-data-anti-hallucination` and inspect whether 02/09/12 were read.
```

- [ ] **Step 5: Validate and record**

Run locally:

```powershell
python .\scripts\validate_skill_links.py
python .\scripts\validate_eval_cases.py
python .\scripts\validate_quality_rubrics.py
python .\scripts\validate_examples.py
python <local-skill-creator>\scripts\quick_validate.py .
git ls-files references/source-reports
```

Expected:

```text
validation_passed=true
eval_validation_passed=true
quality_rubrics_validation_passed=true
examples_validation_passed=true
Skill is valid!
references/source-reports/.gitkeep
```

## 执行顺序

1. 04A: Task 1, 创建 12/13 最小骨架，压缩入口和高频引用。
2. 04B: Task 2, 建立质量 rubric 和校验脚本。
3. 04C: Task 3, 建立 golden examples 和样例校验。
4. 04D: Task 4, 扩展连接器映射层。
5. 04E: Task 5, 扩展 OpenClaw 卫生和复测记录。

每个阶段都应能独立验证。若某阶段失败，不继续扩大修改范围。

## Git 和发布要求

提交前必须检查：

```powershell
git status --short --branch
git diff --stat
git ls-files references/source-reports
```

提交信息必须用中文，并说明：

```text
改动原因：
改动内容：
验证情况：
注意事项：
后续方向：
```

未经用户明确要求，不自动 `git commit` 或 `git push`。

## 当前状态

- 状态: 已执行本地 04A-04E。
- 本文件状态: 04 号执行计划已创建并用于本地实施。
- 已完成: 12/13 references、quality rubrics、golden examples、example/rubric validators、README/SKILL/policy routing updates。
- 待完成: 同步到 OpenClaw 后运行 04 号 smoke set，并把结果追加到 `docs/review/04-quality-implementation-results.md`。
