# 03 FICC Researcher Upgrade Review

## 背景

本轮根据桌面文件 `ficc_researcher_upgrade.md` 的改进建议，结合新增本地源资料：

- `references/source-reports/【华泰固收】固收分析框架（2025版）/content.md`
- `references/source-reports/【华泰固收】基本面分析的道与术（2025版）/content.md`

对 FICC Researcher 的可借鉴项进行吸收。

## 改进意见拆解

### 基金经理视角

核心问题：

- 现有 skill 已能解释宏观、利率、信用和机构行为，但组合动作语言不足。
- 缺少久期、曲线、杠杆、信用仓位、止盈止损和持有期收益拆解。

已解决：

- 新增 `references/06-portfolio-action-policy.md`。
- 新增 `assets/templates/portfolio-action-template.md`。
- 在 `bond-strategy.md` 中加入组合动作、情景触发、止损和亏损路径要求。

待后续：

- 真实组合持仓、久期和基点价值计算。
- 持有期收益自动拆解脚本。

### 经济学家视角

核心问题：

- 缺少宏观指标口径、频率、领先/同步/滞后属性。
- 缺少政策反应函数。
- 缺少预期差分析。

已解决：

- 新增 `references/07-macro-indicator-glossary.md`。
- 新增 `references/08-policy-reaction-function.md`。
- 新增 `references/evidence-cards/macro-policy-evidence.md`。
- 新增 `assets/templates/macro-data-commentary-template.md` 和 `assets/templates/policy-event-commentary-template.md`。
- 在 `rates-macro.md` 中加入数据发布背景、预期差和政策反应函数检查。

待后续：

- 指标历史分位、领先滞后检验和相关性稳定性脚本。
- 社融、通胀、PMI 等指标的真实数据接口联调。

### 固收研究员视角

核心问题：

- 研究框架有了，但日报、数据快评、曲线复盘、信用利差复盘等产品形态还薄。

已解决：

- 新增 `assets/templates/daily-bond-brief-template.md`。
- 新增 `assets/templates/yield-curve-review-template.md`。
- 新增 `assets/templates/credit-spread-review-template.md`。

待后续：

- 图表生成脚本。
- 日报/周报自动填充样例。
- OpenClaw 上基于 WebSearch/Tushare MCP 的真实运行样例。

## 新增华泰资料吸收结果

### 华泰固收分析框架 2025版

可吸收重点：

- 市场交易的是预期差，而不是数据本身。
- 基本面分析需要同时看需求、供给、价格、政策和市场定价。
- 政策组合需要看财政、货币、产业、地产、消费和市场稳定。
- 供给端政策和需求端政策对债市影响不同。

落地文件：

- `references/07-macro-indicator-glossary.md`
- `references/08-policy-reaction-function.md`
- `references/evidence-cards/macro-policy-evidence.md`

### 华泰基本面分析的道与术 2025版

可吸收重点：

- 宏观研究是感知经济温度、推断周期季节。
- 中国经济分析不能只套三驾马车，需要关注供需平衡、经济循环和价格信号。
- 指标需区分领先、同步、滞后，并注意口径差异。
- 社融、PMI、CPI、PPI、投资、消费、出口等指标需要结合政策反应解读。

落地文件：

- `references/07-macro-indicator-glossary.md`
- `references/08-policy-reaction-function.md`
- `assets/templates/macro-data-commentary-template.md`

## Source Index 更新

新增 source id：

- `huatai-fixed-income-framework-2025`
- `huatai-fundamental-analysis-method-2025`

本地私有源资料数量从 23 增加到 25。

## Git 与版权边界

本轮同步更新 `.gitignore`：

- `references/source-reports/**` 被忽略。
- `references/source-reports/.gitkeep` 保留。

新增源资料原文和图片仍只保留本地，不进入 GitHub。

## 验证结果

已运行：

```powershell
python .\scripts\extract_image_urls.py
python .\scripts\build_source_index.py
python .\scripts\validate_source_refs.py
python .\scripts\validate_skill_links.py
```

结果：

- `source_reports_count=25`
- `indexed_reports_count=25`
- `unknown_source_ids=0`
- `validation_passed=true`

## 结论

本轮已经解决改进意见中的三类高价值短板：

- 组合动作语言
- 宏观指标口径
- 政策反应函数和预期差分析

尚未解决的部分主要依赖下一阶段真实数据和计算能力：

- Tushare MCP / iFinD / Wind 联调
- 图表生成
- 组合持仓收益和风险计算
- 日报/周报真实样例回归测试

## VM 与 OpenClaw 状态补充

2026-05-19 检查结果：

- OpenClaw 版本：`2026.5.12`。
- Gateway：运行正常，Feishu 通道 OK。
- VM 上 `~/.openclaw/workspace/skills/ficc-researcher` 仍是旧副本。
- 旧副本缺少 06/07/08、`macro-policy-evidence.md` 和新增宏观模板。
- VM 上 `openclaw mcp list` 显示未注册 MCP server。
- VM 上 Tushare Python 环境可用，`tushare=1.4.29`，token 长度为 56，`trade_cal` 最小接口测试通过。

修正原则：

- 先同步公开 skill 文件到 VM。
- 不同步 `references/source-reports/**`。
- 不直接修改 `~/.openclaw/openclaw.json` 的顶层结构。
- 后续 Tushare MCP 必须通过 `openclaw mcp set` 注册。
