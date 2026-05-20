# 05 FICC Researcher Design Review Triage

## 审查结论

通过，可以执行并已按 05A 范围落地。审查中最影响 Agent 行为稳定性的部分已经修复；框架表达深度和 source section 级溯源属于 05B 深层重构。

## 已修复

1. 输出契约不一致：新增 `references/14-contracts-and-analysis-standards.md`，统一 canonical answer contract、minimum no-data contract 和 workflow overlay 关系。
2. 缺失数据块格式不一致：统一为 `缺失数据`，保留 `当前缺少数据` 为 legacy alias。
3. Data Packet Contract 多版本：统一为 `source/provider/interface_or_file/query/as_of/retrieved_at/time_range/frequency/universe/fields/row_count/units/schema_notes/missing_fields/limitations`。
4. SKILL workflow 顺序：改为先路由和契约，再读 playbook，再定义字段，再选数据源。
5. 数据横切步骤分散：`14` 号契约承接 output/data/confidence/time/portfolio/cross-framework glue，其他文件只补充具体规则。
6. Validation 列表不一致：`SKILL.md` 和 `README.md` 均加入 `validate_source_refs.py`，并移除 public docs 中用户绝对路径命令。
7. Magic number 分散：新增 `scripts/validation_config.py`，验证脚本复用集中配置。
8. Source ID 正则过窄：`validate_source_refs.py` 改为扫描 source-like 反引号 id，支持未来新增机构前缀。
9. daily-bond-brief 无 smoke：新增 `daily-brief-no-live-data`。
10. playbook smoke 覆盖缺口：新增 `derivatives-basis-no-data`、`financial-credit-bank-capital`、`quant-ai-research-factor-monitor`。
11. Tushare 接口散落：在 `references/12-data-connector-mapping.md` 新增候选接口汇总。
12. 禁止行为抽象：`SKILL.md` 和 `14` 号契约补入具体推理陷阱。
13. 语言混用无政策：`14` 号契约增加默认中文标签、英文术语括注规则。
14. source-traceability 未定义：`14` 号契约定义触发条件。
15. 组合动作与投资建议边界：`14` 号契约定义 allowed/not allowed。
16. 置信度和时间维度缺失：`14` 号契约定义高/中/低和常见 horizon。

## 部分缓解

- `05-cross-platform-usage.md` 和 `13-openclaw-skill-hygiene.md` 仍有少量主题重叠，但当前职责已经更清楚：05 处理跨平台使用，13 处理 OpenClaw 同步卫生。后续可进一步压缩。
- `offshore-derivatives-abs-reits-evidence.md` 仍为合并证据卡。本阶段新增 smoke 覆盖 derivatives，但 evidence card 拆分留到 05B。
- Playbook 的 required inputs 粒度仍不完全一致。本阶段用 `09-data-interface-catalog.md` 和 `14` 号契约兜住字段定义，未逐个重写 playbook。

## 暂缓到 05B

- 12 个 playbook 统一成同一种 framework 表达规范。
- 将每个 playbook 的 framework claim 映射到 source report 或 evidence card section。
- 拆分 `offshore-derivatives-abs-reits-evidence.md` 为更对称的证据卡。
- 增强 `quant-ai-research.md` 的 FICC-specific 因子、频率错配、PIT、回测泄漏和过拟合规则。
- 将 `08-policy-reaction-function.md` 和 `11-research-decision-chains.md` 更强制地接入每个相关 playbook。
- 统一所有 workflow template 与 `expected-output-contracts.yml` 的块名到更严格的一对一关系。

## 风险检查

- 安全：未写入 token、账号、私有 endpoint 或授权数据。
- 版权：未加入 `references/source-reports/*.md` 原文。
- 兼容性：`当前缺少数据` 仍作为 legacy alias 被说明，避免旧 agent 完全失效。
- 可移植性：README 和 SKILL 不再硬编码用户 Windows 绝对路径验证命令。

## 是否可以开始执行

已执行 05A。下一步是运行完整验证链，并按用户要求决定是否同步 OpenClaw、提交、推送，或进入 05B。
