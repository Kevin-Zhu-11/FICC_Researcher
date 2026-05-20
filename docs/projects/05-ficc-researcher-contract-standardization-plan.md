# 05 FICC Researcher Contract Standardization Plan

## 阶段目标

吸收设计审查反馈，先解决会直接影响 Agent 稳定执行的契约不一致、验证不可移植、magic number 分散、source id 校验过窄、smoke 覆盖缺口和 Tushare 接口清单分散问题。

## 背景说明

04 阶段已经补齐质量 rubric、golden examples、connector mapping 和 OpenClaw smoke 流程。新的设计审查指出：skill 的零件已经较完整，但统一输出契约、数据包契约、路由冲突处理和验证维护性仍存在摩擦。

## 范围边界

本阶段做：

- 建立 canonical 输出契约、缺失数据块、data packet contract、置信度、时间尺度、组合动作边界和语言规则。
- 将 `SKILL.md`、routing、data policy、integration policy、connector mapping、workflow entrypoints 和 templates 指向同一契约。
- 修复 public repo 文档中的用户绝对路径硬编码。
- 将验证脚本 magic number 和精确文件清单集中管理。
- 扩展 source id 校验，支持未来新增机构前缀。
- 补充 daily-bond-brief、derivatives、financial-credit、quant-ai-research 的 smoke 覆盖。
- 汇总 Tushare 候选接口，保持 provider-neutral，不把具体 MCP 写死进 playbook。

本阶段不做：

- 不重写 12 个 playbook 的完整分析框架。
- 不拆分已有 evidence card。
- 不逐段标注每个 framework claim 的 source report section。
- 不接入真实 Wind/iFinD/local database。
- 不提交或推送，除非用户明确要求。

## 任务拆分

1. 新增 `references/14-contracts-and-analysis-standards.md` 作为唯一契约来源。
2. 更新 `SKILL.md` 和 `references/00-routing.md`，让 workflow 顺序先路由、再契约、再字段、再数据源。
3. 更新 `references/02-data-source-policy.md`、`03-data-integration-policy.md`、`04-mcp-connectors.md`、`09-data-interface-catalog.md`、`12-data-connector-mapping.md`。
4. 更新 `references/10-workflow-entrypoints.md`、`assets/templates/*.md`、`evals/expected-output-contracts.yml`。
5. 新增 `scripts/validation_config.py`，并改造 `build_source_index.py`、`validate_source_refs.py`、`validate_skill_links.py`、`extract_image_urls.py`。
6. 扩展 `evals/smoke-prompts.yml`。
7. 运行完整验证链，记录结果。

## 涉及文件

- `SKILL.md`
- `README.md`
- `references/00-routing.md`
- `references/02-data-source-policy.md`
- `references/03-data-integration-policy.md`
- `references/04-mcp-connectors.md`
- `references/06-portfolio-action-policy.md`
- `references/09-data-interface-catalog.md`
- `references/10-workflow-entrypoints.md`
- `references/12-data-connector-mapping.md`
- `references/14-contracts-and-analysis-standards.md`
- `assets/templates/*.md`
- `evals/expected-output-contracts.yml`
- `evals/smoke-prompts.yml`
- `scripts/*.py`

## 数据或接口变化

无真实数据接口变更。Tushare 仍作为可选结构化数据源说明，不作为硬依赖。仓库不保存 token、账号、私有 endpoint 或授权数据。

## 验证方式

从仓库根目录运行：

```powershell
python .\scripts\build_source_index.py
python .\scripts\validate_source_refs.py
python .\scripts\validate_skill_links.py
python .\scripts\validate_eval_cases.py
python .\scripts\validate_quality_rubrics.py
python .\scripts\validate_examples.py
```

如本机安装了 Codex `skill-creator`，再用本机路径运行 `quick_validate.py`。

## 风险和回滚

- 输出契约统一后，旧 prompt 或旧 golden example 中的 `当前缺少数据` 可能仍可读但不再是推荐标签。
- smoke case 数量增加后，OpenClaw eval 执行时间会变长。
- 深层 playbook 表达规范和 section-level source mapping 尚未在本阶段完成，需要 05B 继续推进。

回滚方式：恢复本阶段涉及文件到 04 阶段版本，并移除 `references/14-contracts-and-analysis-standards.md` 与 `scripts/validation_config.py`。

## 当前状态

已完成本阶段实现，等待完整验证和用户确认是否继续 05B。
