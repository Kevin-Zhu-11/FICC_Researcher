# FICC Researcher

[English](README.md) | [简体中文](README.zh-CN.md)

FICC Researcher 是一个面向 Agent 的固定收益研究 skill。它把固收研究拆成路由、playbook、证据卡、数据契约和输出模板，让 Codex、OpenClaw、Claude 风格 Agent 或个人研究 Agent 能按同一套框架处理中国债券市场问题。

这个仓库不提供实时行情，也不分发券商研报原文。它负责告诉 Agent 需要哪些数据、如何检查数据、如何把框架和事实分开，以及在缺数据时应该怎样降级输出。

## 它解决什么问题

FICC Researcher 要求 Agent 在回答固收问题时区分三层内容：

- 框架事实：来自 playbook、证据卡和研究框架的稳定机制。
- 数据事实：来自用户文件、MCP、数据库、官方来源或可验证网页的当前数据。
- 推断判断：在数据和框架基础上形成的条件性结论，必须写清置信度、缺失数据和风险。

当前覆盖的主题包括：

- 利率和宏观
- 债券组合策略和曲线分析
- 信用策略、城投债、大金融信用债
- 银行理财、基金和机构行为
- 可转债、可交债和混合资产
- 利率衍生品
- 美债、中资美元债、点心债和离岸人民币债
- ABS 和公募 REITs
- 固收量化和 AI 投研流程

## 仓库结构

```text
FICC_Researcher/
├── SKILL.md                         # Agent 入口
├── agents/
│   └── openai.yaml                  # Agent 展示元数据
├── assets/templates/                # 输出模板
├── docs/projects/                   # 设计和阶段计划
├── docs/review/                     # 验证和审查记录
├── examples/
│   ├── data/                        # 脱敏或公开样例数据包
│   └── golden-cases/                # 标准输出示例
├── references/
│   ├── 00-routing.md                # 问题路由
│   ├── 01-source-index.yml          # 来源索引，不包含研报原文
│   ├── 02-data-source-policy.md     # 数据源优先级和缺失数据规则
│   ├── 09-data-interface-catalog.md # 字段级数据需求
│   ├── 10-workflow-entrypoints.md   # 可复用研究工作流
│   ├── 14-contracts-and-analysis-standards.md # 统一输出和数据契约
│   ├── 16-source-claim-map.yml      # claim 到证据和来源的映射
│   ├── playbooks/                   # 核心研究 playbook
│   ├── evidence-cards/              # 压缩后的证据卡
│   └── chart-notes/                 # 图表和图片链接说明
├── evals/                           # smoke prompts 和输出契约
└── scripts/                         # 校验和索引脚本
```

## 快速开始

可以直接使用 GitHub Release：

- Release 页面：<https://github.com/Kevin-Zhu-11/FICC_Researcher/releases/tag/v0.1.0-public-preview>
- Release 包：`ficc-researcher-v0.1.0-public-preview.zip`

也可以克隆仓库：

```bash
git clone https://github.com/Kevin-Zhu-11/FICC_Researcher.git ficc-researcher
cd ficc-researcher
python scripts/validate_skill_links.py
python scripts/validate_eval_cases.py
```

测试 prompt：

```text
Use the ficc-researcher skill to analyze how China social financing data for April 2026 affects the rates-bond curve.
If current yields, credit spreads, funding rates, or expectation data are missing, list the missing fields and do not invent market levels.
```

一个合格回答应该读取 `SKILL.md`、`references/00-routing.md` 和相关 playbook，并按 `references/14-contracts-and-analysis-standards.md` 区分 framework facts、data facts、inferred judgments、confidence、missing data 和 risks。

## 安装到 Codex

把仓库克隆或解压到 Codex 的 skills 目录。默认位置通常是 `$CODEX_HOME/skills` 或 `~/.codex/skills`。

Windows PowerShell 示例：

```powershell
$skillsRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills" } else { Join-Path $HOME ".codex\skills" }
New-Item -ItemType Directory -Force $skillsRoot | Out-Null
git clone https://github.com/Kevin-Zhu-11/FICC_Researcher.git (Join-Path $skillsRoot "ficc-researcher")
```

最终目录应为：

```text
<codex-skills-root>/ficc-researcher/SKILL.md
```

## 安装到 OpenClaw

推荐只同步 Git 跟踪的公开文件：

```bash
mkdir -p ~/.openclaw/workspace/skills/ficc-researcher
git clone https://github.com/Kevin-Zhu-11/FICC_Researcher.git /tmp/ficc-researcher
cd /tmp/ficc-researcher
git archive --format=tar HEAD | tar -xf - -C ~/.openclaw/workspace/skills/ficc-researcher
cd ~/.openclaw/workspace/skills/ficc-researcher
python3 scripts/validate_skill_links.py
python3 scripts/validate_eval_cases.py
```

`~/.openclaw/workspace/skills/` 下只保留一个活跃的 `ficc-researcher/`。备份目录建议放到 `~/.openclaw/workspace/skills-backups/`，不要放在 active skills 目录里，避免 Agent 误读旧版本。

## 数据连接器

FICC Researcher 不绑定某一个数据商。它可以和用户表格、Tushare MCP、iFinD、Wind、本地债券数据库、官方网页或 WebSearch 配合使用。

所有连接器返回的数据都应先整理成统一数据包：

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

真实 token、私有 endpoint、账号名和付费数据导出不要写进仓库。OpenClaw 中的 MCP 建议用运行时配置或环境变量管理，例如：

```bash
openclaw mcp list
openclaw mcp set <provider-name> '<json-config-with-env-placeholders>'
openclaw mcp show <provider-name>
```

## 源研报边界

`references/source-reports/*.md` 不进入 Git，因为源研报可能有版权和分发限制。公开仓库只保留抽取后的框架层：

- playbooks
- evidence cards
- source id index
- chart notes
- data policies
- templates

公开仓库中 `references/source-reports/` 只应跟踪 `.gitkeep`。

## 校验

在仓库根目录运行：

```powershell
python .\scripts\build_source_index.py
python .\scripts\validate_source_refs.py
python .\scripts\validate_claim_map.py
python .\scripts\validate_skill_links.py
python .\scripts\validate_eval_cases.py
python .\scripts\validate_quality_rubrics.py
python .\scripts\validate_examples.py
```

如果本机安装了 Codex 的 `skill-creator`，还可以用本地路径运行 `quick_validate.py`。

## 当前状态

当前版本约完成 98%。路由、playbooks、证据卡、模板、质量 rubrics、golden examples、连接器映射和 OpenClaw 回归检查都已就位。后续主要补充真实数据连接器的联调，以及 iFinD、Wind 和本地数据库的字段扩展。

## 许可证

本仓库使用 MIT License。许可证适用于仓库中的代码、抽取后的 playbooks、模板和公开材料，不授予任何第三方券商研报或私有源文档的再分发权利。
