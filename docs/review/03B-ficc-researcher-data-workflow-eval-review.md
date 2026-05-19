# 03B FICC Researcher Data Workflow And Eval Review

## 审查结论

- 结论: 通过，可以执行。
- 条件: 执行时必须继续保持 `references/source-reports/**` 不入 Git，不写入任何 token、账号、私有端点或付费数据。
- 性质: 这是 03 号方案的深化补充，不覆盖已有 `03-ficc-researcher-vm-framework-upgrade.md` 的 VM 同步记录。

## 目标一致性

03B 与项目目标一致：

- 继续保持单一 `ficc-researcher` skill，而不是拆成多个难维护 skill。
- 将 FICC skill 定位为研究框架、数据需求和输出纪律，而不是数据连接器本身。
- 让 Codex、OpenClaw、Claude 和个人 agent 可以共享同一套 Markdown/YAML 规则。
- 继续保护源研报版权边界，只提交抽象框架层。

## 参考资料吸收检查

### skill-creator

已吸收：

- `SKILL.md` 保持轻量。
- 详细接口、workflow、决策链放入 `references/`。
- 可重复验证放入 `scripts/` 和 `evals/`。
- 避免重复内容在 `SKILL.md`、README 和 playbook 中多处散落。

### Anthropic financial-services

已吸收：

- agents / skills / commands / connectors 分层思想。
- centralized connectors 思想。
- file-based Markdown/YAML 管理。
- check script 和 cross-file reference validation 思路。

未照搬：

- 不引入 Claude Cowork plugin 目录。
- 不创建真实 slash commands。
- 不复制 partner plugin 内容或连接器配置。

### Anthropic LSEG 插件

已吸收：

- 固收任务可拆成 bond RV、portfolio、macro-rates、swap curve、basis 等 workflow。
- 命令入口与 skill 知识分离。
- 连接器提供数据，skill 负责解释数据。

### 华泰/中金研报框架

已吸收：

- 华泰基本面分析: 经济温度、经济循环、领先/同步/滞后指标、预期差、政策到市场。
- 华泰固收框架: 基本面、政策、情绪/定价三角，需求/供给/价格/政策/市场定价共同解释。
- 中金固收系列: 利率、信用、机构行为、城投、二永、理财、转债、衍生品、ABS/REITs、离岸债等 playbook 底座。

## 范围审查

范围清楚：

- 新增 09 数据接口目录。
- 新增 10 workflow 入口目录。
- 新增 11 决策链文件。
- 新增 eval prompt 与输出契约。
- 更新验证脚本和 README。

范围没有越界：

- 不做真实数据抓取实现。
- 不绑定具体 MCP 工具名。
- 不新增数据库。
- 不做自动交易或个人投资建议。
- 不把版权敏感源资料推送到 GitHub。

## 过度设计检查

风险点：

- `09-data-interface-catalog.md` 如果写得太细，可能变成第二份 Tushare/Wind 文档。
- `10-workflow-entrypoints.md` 如果扩得太多，可能变成命令系统。
- `evals/` 如果做 LLM 自动评分，容易假装验证质量。

控制方式：

- 09 只写研究需要、字段、来源优先级和限制，不复制接口文档。
- 10 只覆盖高频固收研究产品。
- eval 脚本只做结构校验；金融质量由人工或后续单独评审。

## 安全与合规审查

必须遵守：

- 不提交 token、API key、账户、私有路径或生产端点。
- Tushare、iFinD、Wind 只作为 optional connector，不作为仓库内置依赖。
- 公开仓库只保留抽象框架、模板、验证脚本和引用链接。
- 源报告全文、图片和私有 md 继续本地 ignored。

潜在风险：

- README 或 09 中写 provider 名称时，可能被误解为官方合作或授权。

缓解：

- 明确写 optional connector、用户自行配置、遵守服务条款、不再分发数据。

## 兼容性审查

兼容 Codex：

- 仍从 `SKILL.md` 触发。
- references 按需读取，避免主入口过长。

兼容 OpenClaw：

- 不要求 OpenClaw 修改全局配置。
- 工具返回数据后按 data packet contract 进入 FICC。

兼容 Claude-style agents：

- Workflow entrypoints 用 Markdown 表达，不依赖平台专有 command。

兼容公开 GitHub：

- 不包含源报告原文。
- `.mcp.example.json` 只保留占位符。

## 验证方式是否足够

计划要求：

- `build_source_index.py`
- `validate_source_refs.py`
- `validate_skill_links.py`
- `validate_eval_cases.py`
- `skill-creator` quick validate
- `git ls-files references/source-reports`
- OpenClaw 3 到 5 个 smoke prompt

审查判断：

- 对结构完整性足够。
- 对金融分析质量仍需要人工抽样评估。
- 对真实数据连接质量，需要后续在 OpenClaw/Tushare/iFinD/Wind 环境中记录结果。

## 是否需要拆分阶段

建议按三段执行：

1. 03B-A: 09/10/11 文档与 README/SKILL 路由。
2. 03B-B: eval prompt、输出契约和验证脚本。
3. 03B-C: OpenClaw smoke 测试与结果记录。

每段都可以独立验证和提交。

## 可以开始执行吗

可以。建议先执行 03B-A，因为它直接解决当前最大问题：agent 已经能取数和分析，但还缺“字段级数据需求目录”和“高频 workflow 入口”。

## 执行后复核

本地执行结果：

- 03B-A: 已完成。09 数据接口目录、10 workflow 入口、11 决策链均已新增并从 `SKILL.md`、routing 和相关 policy 文件接入。
- 03B-B: 已完成。eval prompt、输出契约和 `validate_eval_cases.py` 已新增，结构校验通过。
- 03B-C: 已完整执行。公开 skill 副本已同步到 OpenClaw VM，完成 current-market-data anti-hallucination 测试，并跑完 `evals/smoke-prompts.yml` 中全部 10 个 OpenClaw eval case。

已运行验证：

```text
python .\scripts\build_source_index.py
python .\scripts\validate_source_refs.py
python .\scripts\validate_skill_links.py
python .\scripts\validate_eval_cases.py
skill-creator quick_validate.py
```

验证结论：

- source report 本地索引数量为 25，缺失和未索引均为 0。
- source id 引用未知数量为 0。
- skill 结构校验通过。
- eval case 数量为 10，output contract 数量为 9，校验通过。
- `Skill is valid!`

OpenClaw 补充验证：

- VM 上 `validate_skill_links.py` 通过，公开副本 `private_source_reports_count=0`。
- VM 上 `validate_eval_cases.py` 通过，`eval_cases=10`。
- OpenClaw main agent 能读取 `skills/ficc-researcher/SKILL.md`、09、10、11。
- 对“今天 10Y 国债、10Y 国开、AAA 城投 3Y 利差和 DR007”问题，agent 明确拒绝编造当前点位，并列出所需数据来源。
- OpenClaw eval 10/10 PASS，0 FAIL，所有结果 `returncode=0` 且 `stderr_chars=0`。
- 已将 VM 上旧 `ficc-researcher.bak-*` 目录移到 `~/.openclaw/workspace/skills-backups/`，避免被当作 skill 误读。
