# FICC Researcher 02 号完成度提升实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将 `ficc-researcher` 从 v0.1 可用骨架推进到 95%-100% 完成度，使其可以稳定服务 Codex、Claude、OpenClaw 和个人 agent 的固收研究工作流。

**Architecture:** 采用“轻量入口 + 完整 playbook 族 + 源报告 evidence cards + 集中 MCP/数据连接模板 + 跨平台使用协议 + 自动化验证”的结构。95% 完成度不依赖真实密钥；100% 完成度需要至少一个真实结构化数据连接器完成取数闭环。

**Tech Stack:** Markdown, YAML, Python, Git, Codex skill conventions, OpenClaw workspace skills, optional MCP connectors for Tushare/iFinD/Wind/local bond database, WebSearch.

---

## 设计判断

### 完成度定义

当前状态约为 60%-65%:

- 已有 `SKILL.md`、routing、source index、data source policy、data integration policy。
- 已有 5 个主干 playbook。
- 已通过本地和 OpenClaw 基础验证。
- 已能处理无实时数据的框架问题和用户提供的模拟数据。

95% 完成标准:

- 12 个核心 playbook 全部存在并符合统一模板。
- 每个 playbook 都引用 source index 中的源报告 id，并明确数据字段、缺失数据输出、风险与反例。
- 23 篇源报告被萃取为可复用 evidence cards 或主题证据索引。
- MCP/WebSearch/用户上传数据接入边界有明确模板和验证规则。
- 验证脚本能检查必需 playbook、source id、引用路径、source reports 数量、核心数据协议文件。
- OpenClaw 只读测试副本通过 6 个验收问题和至少 1 个用户数据问题。
- Git 首提交准备清单完整，但不自动提交。

100% 完成标准:

- 在 95% 基础上，至少接通一个真实结构化数据源，例如 Tushare MCP、Tushare Python workflow、iFinD MCP、Wind 本地桥或本地债券数据库。
- 至少完成 1 个“真实数据 + FICC playbook”的端到端分析样例。
- 数据样例中必须包含 source、as_of、retrieved_at、fields、limitations。
- 若没有 token、账号或本地数据库权限，则 100% 项只能保持待执行，不得伪造。

### 方案比较

推荐方案 B。

| 方案 | 内容 | 优点 | 缺点 | 完成度 |
| --- | --- | --- | --- | --- |
| A. 轻量补文档 | 只补 7 个 playbook 和 MCP 说明 | 快，风险低 | 验证弱，跨平台复用不稳 | 80%-85% |
| B. 完整 skill 化 | 补 playbook、evidence cards、连接模板、验证脚本、OpenClaw 测试 | 不依赖密钥即可到 95%，结构稳定 | 工作量中等 | 95% |
| C. 生产级数据闭环 | 在 B 上接真实 Tushare/iFinD/Wind/MCP | 最接近生产可用 | 需要密钥、权限和环境配置 | 100% |

本计划采用 B，并把 C 作为条件任务。

## 文件职责

- `SKILL.md`: 继续保持轻量入口，只新增必要导航，不塞专题细节。
- `agents/openai.yaml`: 跟随 skill 能力更新默认提示。
- `references/00-routing.md`: 从“可路由到 future playbook”升级为“可路由到真实 playbook”。
- `references/01-source-index.yml`: 保持 23 篇源报告索引，必要时补 `source_role` 细分。
- `references/02-data-source-policy.md`: 保持数据源优先级和禁止伪造纪律。
- `references/03-data-integration-policy.md`: 保持用户数据、MCP 数据、WebSearch 数据协作协议。
- `references/04-mcp-connectors.md`: 新增无密钥 MCP/数据连接器说明。
- `.mcp.example.json`: 新增无密钥连接器模板。
- `references/05-cross-platform-usage.md`: 新增 Codex、Claude、OpenClaw、个人 agent 使用协议。
- `references/evidence-cards/*.md`: 新增源报告主题证据卡。
- `references/playbooks/*.md`: 补齐 12 个核心 playbook。
- `references/chart-notes/key-framework-charts.md`: 补充原始图片 URL 和更多图表文字重构。
- `assets/templates/*.md`: 新增可复用分析输出模板。
- `scripts/validate_skill_links.py`: 扩展结构校验。
- `scripts/validate_source_refs.py`: 新增 source id 引用校验。
- `scripts/extract_image_urls.py`: 新增图片 URL 抽取辅助脚本。
- `docs/review/02-ficc-researcher-completion-review.md`: 执行前计划审查和完成后复盘。

## Task 1: 建立 02 号基线和完成度仪表盘

**Files:**
- Create: `<repo-root>\docs\review\02-ficc-researcher-completion-review.md`
- Modify: `<repo-root>\scripts\validate_skill_links.py`

- [ ] **Step 1: 检查 Git 状态**

Run:

```powershell
git status --short --branch --ignored
```

Expected:

```text
## No commits yet on master
?? .gitignore
?? SKILL.md
?? agents/
?? assets/
?? docs/
?? references/
?? scripts/
!! .tmp_pyyaml/
```

If additional unexpected files appear, inspect them before editing.

- [ ] **Step 2: 创建计划审查文件**

Create `docs/review/02-ficc-researcher-completion-review.md` with:

```markdown
# FICC Researcher 02 号计划审查

## 审查结论

- 初始结论: 通过，可以执行 95% 完成度计划。
- 100% 完成度依赖真实数据连接器和凭据，未获得凭据前不得伪造数据闭环。

## 目标一致性

- 计划与 00 号设计思想一致: 单 skill、多 playbook、集中数据源政策、可审计输出。
- 计划与 01 号执行结果一致: 在已有入口、路由、索引和 5 个主干 playbook 上扩展。

## 范围边界

- 本阶段做: 补齐 playbook、证据卡、MCP 模板、跨平台协议、验证脚本、OpenClaw 回归测试。
- 本阶段不做: 写入真实 token、替代投资建议、自动交易、生产级数据库迁移。

## 过度设计检查

- 不拆多个 skill，仍使用单 `ficc-researcher` 入口。
- 不把 Tushare/iFinD/Wind 调用写死进 playbook。
- 不把 23 篇源报告全文塞进 `SKILL.md`。

## 验证要求

- 本地脚本全部通过。
- `skill-creator` quick validate 通过。
- OpenClaw workspace skill 显示 ready。
- 6 个验收问题和 1 个用户数据问题通过。

## 风险

- 数据连接器无凭据时只能到 95%，不能宣称 100%。
- 图表 URL 可能失效，必须保留文字重构。
- Future playbook 补齐后需要同步更新 routing 和验证脚本。
```

- [ ] **Step 3: 扩展结构校验脚本的目标清单**

Modify `scripts/validate_skill_links.py` so required files include:

```python
"references/04-mcp-connectors.md",
"references/05-cross-platform-usage.md",
```

And add exact required playbook names:

```python
REQUIRED_PLAYBOOKS = [
    "rates-macro.md",
    "bond-strategy.md",
    "institution-behavior.md",
    "credit-strategy.md",
    "convertible-hybrid.md",
    "city-investment-bonds.md",
    "financial-credit.md",
    "wealth-management-funds.md",
    "derivatives.md",
    "offshore-global-rates.md",
    "abs-reits.md",
    "quant-ai-research.md",
]
```

Expected output after all tasks:

```text
ok: required_playbooks=12
```

- [ ] **Step 4: Run baseline validation**

Run:

```powershell
python .\scripts\build_source_index.py
python .\scripts\validate_skill_links.py
```

Expected at this early step:

```text
build_source_index.py passes
validate_skill_links.py may fail until required new files/playbooks are created
```

## Task 2: 补齐 7 个缺失 playbook

**Files:**
- Create: `<repo-root>\references\playbooks\city-investment-bonds.md`
- Create: `<repo-root>\references\playbooks\financial-credit.md`
- Create: `<repo-root>\references\playbooks\wealth-management-funds.md`
- Create: `<repo-root>\references\playbooks\derivatives.md`
- Create: `<repo-root>\references\playbooks\offshore-global-rates.md`
- Create: `<repo-root>\references\playbooks\abs-reits.md`
- Create: `<repo-root>\references\playbooks\quant-ai-research.md`
- Modify: `<repo-root>\references\00-routing.md`

- [ ] **Step 1: 使用统一 playbook 模板**

Each new playbook must include exactly these sections:

```markdown
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

- [ ] **Step 2: Create `city-investment-bonds.md`**

Required coverage:

```text
Scope: 城投债、化债、区域利差、平台转型、隐性债务、再融资。
Required Inputs: 区域财政、债务率、土地出让、城投平台现金流、银行授信、债券到期、区域利差、特殊再融资债。
Framework: 区域财政实力 + 债务压力 + 政策支持 + 再融资能力 + 市场估值。
Risk Checks: 不用行政级别替代信用判断；不把化债政策等同于所有主体刚兑。
Source Reports: `cicc-city-investment-bonds-2025`, `huatai-credit-bond-framework-2025`.
```

- [ ] **Step 3: Create `financial-credit.md`**

Required coverage:

```text
Scope: 银行二永债、TLAC、券商债、保险资本补充债、大金融信用债。
Required Inputs: 资本充足率、核心一级资本、TLAC、盈利、资产质量、流动性、监管规则、品种条款、利差。
Framework: 主体资质 + 资本工具条款 + 监管资本需求 + 机构配置需求 + 流动性溢价。
Risk Checks: 不把系统重要性等同于债项无风险；区分主体信用和次级条款风险。
Source Reports: `cicc-financial-credit-bonds-2025`, `huatai-credit-bond-framework-2025`.
```

- [ ] **Step 4: Create `wealth-management-funds.md`**

Required coverage:

```text
Scope: 银行理财净值化、赎回、固收+基金、公募基金行为、产品负债端。
Required Inputs: 产品 NAV、回撤、份额、申赎、久期、杠杆、持仓评级、资产配置、产品类型。
Framework: 负债稳定性 + 估值波动 + 流动性管理 + 持仓结构 + 赎回反馈。
Risk Checks: 不把产品收益率当作全部持仓表现；赎回压力下流动性好资产可能先被卖出。
Source Reports: `cicc-wealth-management-net-value-2025`, `cicc-fixed-income-plus-fund-framework-2025`, `huatai-institution-behavior-2025`.
```

- [ ] **Step 5: Create `derivatives.md`**

Required coverage:

```text
Scope: 国债期货、利率互换、基差、套保、IRS、期权。
Required Inputs: CTD、转换因子、IRR、基差、回购利率、期货价格、现券曲线、swap curve、DV01、套保目标。
Framework: 现券曲线 + 融资成本 + 期货定价 + 基差/IRR + 风险敞口。
Risk Checks: 不把期货方向交易和套保混在一起；检查保证金、展期和流动性风险。
Source Reports: `cicc-interest-rate-derivatives-2025`.
```

- [ ] **Step 6: Create `offshore-global-rates.md`**

Required coverage:

```text
Scope: 美债、中资美元债、点心债、离岸人民币债、全球利率和汇率约束。
Required Inputs: UST curve、Fed path、DXY、USD/CNH、hedge cost、issuer spread、评级、境内外利差、跨境政策。
Framework: 全球利率锚 + 汇率/套保成本 + 主体信用 + 境内外融资替代 + 流动性。
Risk Checks: 不把境内信用框架直接套到离岸债；区分美元利率风险和发行人信用风险。
Source Reports: `cicc-us-treasuries-framework-2025`, `cicc-offshore-credit-usd-dim-sum-2025`, `cicc-offshore-rmb-bonds-2025`.
```

- [ ] **Step 7: Create `abs-reits.md`**

Required coverage:

```text
Scope: ABS、公募 REITs、底层资产现金流、交易结构、估值和流动性。
Required Inputs: 底层资产池、现金流、分层结构、增信、违约/提前偿还、REITs NOI、分派率、估值、成交流动性。
Framework: 底层资产质量 + 结构增信 + 现金流稳定性 + 利率/信用定价 + 流动性折价。
Risk Checks: 不把优先级结构等同于无风险；REITs 要区分资产经营波动和利率估值波动。
Source Reports: `cicc-abs-framework-2025`, `cicc-public-reits-strategy-2025`.
```

- [ ] **Step 8: Create `quant-ai-research.md`**

Required coverage:

```text
Scope: 固收量化、AI 投研、因子、监控、报告自动化、智能体。
Required Inputs: 数据字典、因子定义、样本区间、标签、回测假设、评价指标、监控频率。
Framework: 研究问题 -> 数据契约 -> 因子/规则 -> 验证 -> 监控 -> 人类复核。
Risk Checks: 不把 LLM 摘要当成数据事实；不接受无样本外验证的因子结论。
Source Reports: `huatai-quant-ai-ficc-2025`, `cicc-ficc-ai-agent-path-2025`.
```

- [ ] **Step 9: Update routing from future routes to actual playbooks**

Modify `references/00-routing.md`:

```text
Replace wording that says target playbooks are future work.
Keep a fallback rule: if a playbook exists but current data is unavailable, return missing-data block.
```

- [ ] **Step 10: Validate playbook count**

Run:

```powershell
Get-ChildItem .\references\playbooks -Filter *.md | Select-Object -ExpandProperty Name
python .\scripts\validate_skill_links.py
```

Expected:

```text
12 playbook names are listed
validation_passed=true
```

## Task 3: 建立源报告 evidence cards

**Files:**
- Create directory: `<repo-root>\references\evidence-cards`
- Create: `<repo-root>\references\evidence-cards\rates-macro-evidence.md`
- Create: `<repo-root>\references\evidence-cards\credit-evidence.md`
- Create: `<repo-root>\references\evidence-cards\institution-wealth-evidence.md`
- Create: `<repo-root>\references\evidence-cards\convertible-hybrid-evidence.md`
- Create: `<repo-root>\references\evidence-cards\offshore-derivatives-abs-reits-evidence.md`
- Create: `<repo-root>\references\evidence-cards\quant-ai-evidence.md`
- Modify: `<repo-root>\SKILL.md`

- [ ] **Step 1: Create evidence-card template**

Each evidence card should use:

```markdown
# [Topic] Evidence

## Use When

## Source Reports

## Core Framework Claims

## Data Fields Mentioned

## Common Misreadings

## Useful Search Terms
```

- [ ] **Step 2: Write `rates-macro-evidence.md`**

Include source ids:

```text
cicc-low-rate-macro-bond-pricing-2025
cicc-bond-principles-strategy-2025
huatai-bond-market-framework-2025
huatai-asset-allocation-framework-2025
```

Core claims:

```text
低利率环境下传统增长/通胀框架不够，财政、工业链条、机构负债和供需更重要。
利率分析要从宏观、资金、供给、需求和曲线结构共同入手。
```

- [ ] **Step 3: Write `credit-evidence.md`**

Include source ids:

```text
cicc-credit-strategy-low-spread-2025
huatai-credit-bond-framework-2025
cicc-city-investment-bonds-2025
cicc-financial-credit-bonds-2025
```

Core claims:

```text
信用利差由违约风险、流动性、投资者结构、供给和杠杆便利性共同决定。
低利差环境下收益增强依赖择券、择时、票息、曲线和有限下沉，不能只押利差压缩。
```

- [ ] **Step 4: Write remaining evidence cards**

Use the same template and cite only existing `id` values in `references/01-source-index.yml`.

- [ ] **Step 5: Update `SKILL.md` navigation**

Add one bullet under workflow:

```text
If the answer needs broker-evidence synthesis, read the relevant file under `references/evidence-cards/` before reading full source reports.
```

## Task 4: 建立 MCP 和数据连接器模板

**Files:**
- Create: `<repo-root>\references\04-mcp-connectors.md`
- Create: `<repo-root>\.mcp.example.json`
- Modify: `<repo-root>\references\02-data-source-policy.md`
- Modify: `<repo-root>\references\03-data-integration-policy.md`

- [ ] **Step 1: Create `04-mcp-connectors.md`**

Required sections:

```markdown
# MCP Connectors

## Principle
## Connector Matrix
## Tushare
## iFinD
## Wind Local Bridge
## Local Bond Database
## WebSearch
## Data Packet Contract
## Security Rules
## Fallback Behavior
```

Connector matrix must include:

```text
Tushare: macro, equity, funds, convertibles where covered; not full bond microstructure.
iFinD: broad China macro, bonds, funds, announcements, market data.
Wind local bridge: curves, credit spreads, valuations, bond terms, holdings, issuer fundamentals.
Local bond database: curated point-in-time internal datasets.
WebSearch: policy/news/source discovery, not licensed market data replacement.
```

- [ ] **Step 2: Create `.mcp.example.json`**

Use this no-secret template:

```json
{
  "mcpServers": {
    "tushare": {
      "type": "stdio-or-http",
      "description": "Tushare connector. Store TUSHARE_TOKEN outside git and return source, as_of, retrieved_at, fields, and limitations."
    },
    "ifind": {
      "type": "stdio-or-http",
      "description": "iFinD finance data connector. Configure user credentials outside git."
    },
    "wind-local": {
      "type": "local",
      "description": "Local Wind bridge or exported Wind data reader. Do not store terminal credentials in this repository."
    },
    "bond-database": {
      "type": "local",
      "description": "Local bond database for curves, spreads, issuers, ratings, holdings, NAV, and transactions."
    }
  }
}
```

- [ ] **Step 3: Link connector policy from data-source files**

In `02-data-source-policy.md` and `03-data-integration-policy.md`, add:

```text
For connector setup templates and boundaries, read `references/04-mcp-connectors.md`.
```

- [ ] **Step 4: Verify no secrets**

Run:

```powershell
Select-String -Path .\.mcp.example.json,.\references\04-mcp-connectors.md -Pattern 'sk-','token=','password','secret','TUSHARE_TOKEN='
```

Expected:

```text
No real credential values; only explanatory placeholder text may appear.
```

## Task 5: 增强图表笔记和图片 URL 索引

**Files:**
- Modify: `<repo-root>\references\chart-notes\key-framework-charts.md`
- Create: `<repo-root>\references\chart-notes\image-url-index.yml`
- Create: `<repo-root>\scripts\extract_image_urls.py`

- [ ] **Step 1: Write `extract_image_urls.py`**

Script responsibilities:

```text
Scan references/source-reports/*.md
Extract Markdown image URLs and raw http(s) image links
Write references/chart-notes/image-url-index.yml
Include source_file, url, alt_text_or_context
Do not download images
```

- [ ] **Step 2: Run image extraction**

Run:

```powershell
python .\scripts\extract_image_urls.py
```

Expected:

```text
source_reports_count=23
image_urls_count=<positive number>
output=references/chart-notes/image-url-index.yml
```

- [ ] **Step 3: Expand key chart notes**

Add at least 5 more charts or framework reconstructions:

```text
城投债区域分析框架
大金融信用债资本工具框架
理财净值化赎回反馈链条
利率衍生品基差/IRR 框架
ABS/REITs 现金流与估值框架
```

Each entry must keep:

```text
Source report
Original image URL or image-url-index reference
Core message
Use when
Do not use when
Text reconstruction
```

## Task 6: 建立跨平台使用协议和输出模板

**Files:**
- Create: `<repo-root>\references\05-cross-platform-usage.md`
- Create: `<repo-root>\assets\templates\framework-analysis-template.md`
- Create: `<repo-root>\assets\templates\data-assisted-analysis-template.md`
- Create: `<repo-root>\assets\templates\missing-data-template.md`
- Modify: `<repo-root>\SKILL.md`

- [ ] **Step 1: Create `05-cross-platform-usage.md`**

Required sections:

```markdown
# Cross Platform Usage

## Codex
## Claude
## OpenClaw
## Personal Agents
## User-Provided Data
## Connector Data
## Required Safety Contract
## Smoke Tests
```

Include:

```text
Codex: Use SKILL.md + references as native skill folder.
Claude: Use SKILL.md body and references as project skill/context, preserving progressive disclosure.
OpenClaw: Place under ~/.openclaw/workspace/skills/ficc-researcher; keep credentials outside skill.
Personal agents: Load SKILL.md, routing, selected playbooks, data integration policy, and only necessary evidence cards.
```

- [ ] **Step 2: Create output templates**

`framework-analysis-template.md`:

```markdown
# Framework Analysis

## 问题归类
## 使用 Playbook
## 框架事实
## 当前缺少数据
## 推断判断
## 风险与反例
## 后续跟踪
```

`data-assisted-analysis-template.md`:

```markdown
# Data Assisted Analysis

## 问题归类
## 使用 Playbook
## 数据输入
## 数据质量检查
## 框架事实
## 数据事实
## 推断判断
## 缺失数据
## 风险与反例
## 后续跟踪
```

`missing-data-template.md`:

```markdown
当前缺少数据:
- 字段:
- 推荐来源:
- 时间范围:
- 频率:
- 用途:
在缺少以上数据前，只能给出框架判断，不能给出当前市场结论。
```

- [ ] **Step 3: Link templates from `SKILL.md`**

Add:

```text
For reusable output formats, use `assets/templates/` when producing reports or handoff drafts.
```

## Task 7: 增加 source id 引用校验

**Files:**
- Create: `<repo-root>\scripts\validate_source_refs.py`
- Modify: `<repo-root>\scripts\validate_skill_links.py`

- [ ] **Step 1: Write `validate_source_refs.py`**

Script requirements:

```text
Parse ids from references/01-source-index.yml
Scan references/playbooks/*.md and references/evidence-cards/*.md
Find backtick-wrapped source ids that look like cicc-* or huatai-*
Fail if any referenced source id is not in source index
Print source_ids_count, referenced_source_ids_count, unknown_source_ids
```

No PyYAML dependency. Use regex.

- [ ] **Step 2: Run source reference validation**

Run:

```powershell
python .\scripts\validate_source_refs.py
```

Expected:

```text
source_ids_count=23
unknown_source_ids=0
validation_passed=true
```

- [ ] **Step 3: Mention it in `validate_skill_links.py` output**

Do not import or execute the second script inside `validate_skill_links.py`. Print:

```text
info: run scripts/validate_source_refs.py for source-id validation
```

This keeps each validator focused.

## Task 8: 完成 OpenClaw 回归测试矩阵

**Files:**
- Create: `<repo-root>\docs\review\02-openclaw-regression-results.md`

- [ ] **Step 1: Sync test copy to OpenClaw**

Use the existing safe sync pattern:

```powershell
tar -C <repo-root> --exclude .git --exclude .tmp_pyyaml --exclude outputs --exclude tmp -cf ficc-researcher-openclaw-test.tar .
scp -i <ssh-key> <local-temp>\ficc-researcher-openclaw-test.tar <vm-ssh-target>:/tmp/ficc-researcher-openclaw-test.tar
ssh -i <ssh-key> <vm-ssh-target> "chmod -R u+w ~/.openclaw/workspace/skills/ficc-researcher; tar -C ~/.openclaw/workspace/skills/ficc-researcher -xf /tmp/ficc-researcher-openclaw-test.tar; chmod -R a-w ~/.openclaw/workspace/skills/ficc-researcher"
```

Expected:

```text
Remote skill remains ready and read-only.
```

- [ ] **Step 2: Run 6 core acceptance prompts**

Use `openclaw agent --agent main --session-id <unique-id> --thinking medium --timeout 300 --json --message "<prompt>"`.

Prompts:

```text
当前低利率环境下，10 年国债收益率上行需要哪些条件？
信用利差处于低位时，信用债还能怎么做收益？
银行理财赎回为什么会影响信用债和短端利率？
转债估值应该看平价溢价率还是债底？
城投化债背景下，区域利差该如何分析？
如果没有实时数据，你能给出哪些数据清单和分析路径？
```

Each output must contain:

```text
selected playbooks
data needed or data used
source report evidence
missing data block when required
risk and counterexample
follow-up indicators
no fabricated current market data
```

- [ ] **Step 3: Run 2 user-data prompts**

Prompt 1:

```text
用户提供模拟数据：日期=2026-05-17；AAA_3Y信用利差=32bp；AA+_3Y信用利差=58bp；DR007=1.72%；3Y信用债收益率=2.28%；理财赎回数据=缺失。请使用 ficc-researcher 分析这些数据能支持什么，不能支持什么。
```

Prompt 2:

```text
用户提供模拟转债数据：平价=96；转股溢价率=28%；债底=91；剩余期限=3.2年；赎回触发进度=未触发；正股近20日波动率=24%。请使用 ficc-researcher 分析估值框架和缺失数据。
```

- [ ] **Step 4: Write regression results**

Create `docs/review/02-openclaw-regression-results.md`:

```markdown
# FICC Researcher 02 OpenClaw Regression Results

## Environment

## Skill Visibility

## Validation Commands

## Prompt Results

## Failures Or Deviations

## Conclusion
```

## Task 9: 条件项：真实 Tushare 或 MCP 数据闭环

**Files:**
- Create if credentials are available: `<repo-root>\docs\review\02-data-connector-smoke-results.md`

- [ ] **Step 1: Check connector availability**

Run on target platform:

```bash
openclaw mcp list
python3 -c "import os; print(bool(os.environ.get('TUSHARE_TOKEN')))"
python3 -c "import tushare as ts; print(ts.__version__)"
```

Expected for 100% path:

```text
At least one connector or Tushare Python workflow is available.
Token is configured outside git.
```

- [ ] **Step 2: Run one safe data smoke test**

Use non-sensitive public macro or calendar data only, for example trading calendar or macro series supported by the configured connector.

Required result fields:

```text
source:
as_of:
retrieved_at:
fields:
row_count:
limitations:
```

- [ ] **Step 3: Combine data with FICC analysis**

Ask:

```text
请使用 ficc-researcher，将刚才获取的数据作为 data facts，回答该数据能支持哪些固收判断、不能支持哪些判断，并列出缺失字段。
```

Expected:

```text
The answer distinguishes framework facts, data facts, and inferred judgments.
No fabricated missing data.
```

- [ ] **Step 4: If credentials are unavailable, mark task skipped**

Write:

```text
100% data connector task skipped because no credentialed connector was available. Skill completion remains 95%, not 100%.
```

## Task 10: 最终验证和首提交准备

**Files:**
- Modify: `<repo-root>\docs\review\02-ficc-researcher-completion-review.md`

- [ ] **Step 1: Run local validators**

Run:

```powershell
python .\scripts\build_source_index.py
python .\scripts\validate_skill_links.py
python .\scripts\validate_source_refs.py
$env:PYTHONPATH='<repo-root>\.tmp_pyyaml'
python <local-skill-creator>\scripts\quick_validate.py <repo-root>
```

Expected:

```text
source_reports_count=23
indexed_reports_count=23
validation_passed=true
Skill is valid!
```

- [ ] **Step 2: Run security text scan**

Run:

```powershell
Select-String -Path .\SKILL.md,.\references\*.md,.\references\playbooks\*.md,.\references\evidence-cards\*.md,.\.mcp.example.json -Pattern 'sk-','password=','token=','api_key=','secret='
```

Expected:

```text
No real secrets. Placeholder terms only in policy text are acceptable.
```

- [ ] **Step 3: Run Git status**

Run:

```powershell
git status --short --branch --ignored
```

Expected:

```text
All intended files are untracked or modified.
.tmp_pyyaml/ remains ignored.
No unrelated files outside FICC_Researcher are touched.
```

- [ ] **Step 4: Update review conclusion**

In `docs/review/02-ficc-researcher-completion-review.md`, add:

```markdown
## Final Conclusion

- Completion level: 95% if all no-credential tasks pass.
- Completion level: 100% only if Task 9 completes with a real connector.
- Git commit: not performed unless user explicitly requests it.
```

- [ ] **Step 5: Prepare commit scope, but do not commit unless requested**

Recommended first commit scope:

```powershell
git add .gitignore SKILL.md agents references scripts assets docs .mcp.example.json
git status --short
```

Do not run `git commit` unless the user explicitly asks.

Recommended commit message when requested:

```text
文档：完善 FICC Researcher 固收分析技能到 95% 完成度

改动原因：
- 将 FICC Researcher 从可用骨架推进为完整固收研究 skill。

改动内容：
- 补齐 12 个核心 playbook。
- 新增源报告 evidence cards、MCP 连接器模板、跨平台使用协议和输出模板。
- 增强验证脚本，校验 playbook、source id、数据协议和图表索引。
- 完成 OpenClaw 回归测试记录。

验证情况：
- 已运行 source index、skill links、source refs 和 skill-creator quick validate。
- 已在 OpenClaw 测试副本完成验收问题测试。

注意事项：
- 不包含任何真实密钥、token 或私有连接信息。
- 100% 数据闭环依赖后续配置真实 Tushare/iFinD/Wind/MCP。

后续方向：
- 接入真实数据连接器并形成端到端数据分析样例。
```

## Acceptance Checklist

- [ ] 12 个 playbook 全部存在。
- [ ] `references/04-mcp-connectors.md` 存在。
- [ ] `.mcp.example.json` 存在且不含真实密钥。
- [ ] `references/05-cross-platform-usage.md` 存在。
- [ ] `references/evidence-cards/` 至少 6 个主题证据卡。
- [ ] `references/chart-notes/image-url-index.yml` 存在。
- [ ] `assets/templates/` 至少 3 个输出模板。
- [ ] `scripts/validate_source_refs.py` 存在并通过。
- [ ] `scripts/validate_skill_links.py` 检查 12 个必需 playbook。
- [ ] `quick_validate.py` 通过。
- [ ] OpenClaw 显示 `ficc-researcher ✓ Ready`。
- [ ] 6 个验收问题通过。
- [ ] 1-2 个用户数据问题通过。
- [ ] 无真实密钥入库。
- [ ] Git 首提交范围清楚。

## Execution Handoff

Plan complete and saved to `docs/projects/02-ficc-researcher-completion-plan.md`.

Execution options:

1. **Subagent-Driven (recommended)**: Dispatch one worker per bounded task group, with review between tasks. Best for the 7 playbooks and evidence cards.
2. **Inline Execution**: Execute tasks in this session using `superpowers:executing-plans`, with checkpoints after each major task.

Recommended first execution slice:

```text
Task 1 -> Task 2 -> Task 7
```

This makes the missing playbooks real first, then immediately strengthens validation.
