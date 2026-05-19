# FICC Researcher 03 号 VM 同步与框架增强计划

## 阶段目标

把本地新版 `ficc-researcher` 同步为 GitHub 与 OpenClaw VM 可用版本，并将华泰新增两篇框架资料中的宏观分析方法进一步标准化到 skill 文件中。

## 背景说明

OpenClaw 测试显示，VM 上的 `~/.openclaw/workspace/skills/ficc-researcher` 仍是旧副本：

- 缺少 `references/06-portfolio-action-policy.md`
- 缺少 `references/07-macro-indicator-glossary.md`
- 缺少 `references/08-policy-reaction-function.md`
- 缺少 `references/evidence-cards/macro-policy-evidence.md`
- 缺少 `assets/templates/macro-data-commentary-template.md`

因此，OpenClaw 在宏观数据点评中提示部分文件不存在。这个问题来自 VM 同步滞后，而不是本地 skill 缺失。

## 范围边界

本阶段做：

- 强化宏观指标、政策反应函数、预期差和债市传导文件。
- 更新 MCP/OpenClaw 连接器说明，避免再次把顶层 `mcpServers` 写入 `openclaw.json`。
- 保持 `references/source-reports/**` 不进入 GitHub。
- 将公开 skill 文件同步到 OpenClaw VM。
- 完成本地与 VM 验证。

本阶段不做：

- 不提交源研报原文、图片或目录版 content.md。
- 不把 Tushare/iFinD/Wind 账号、token 或私有端点写入仓库。
- 不把数据接口调用写死进 FICC playbook。
- 不绕过 OpenClaw URL 安全策略。

## 任务拆分

### Task 1: 框架文件增强

涉及文件：

- `references/07-macro-indicator-glossary.md`
- `references/08-policy-reaction-function.md`
- `references/evidence-cards/macro-policy-evidence.md`
- `references/playbooks/rates-macro.md`
- `assets/templates/macro-data-commentary-template.md`

验收：

- 宏观数据点评必须区分领先、同步、滞后指标。
- 必须包含预期差、政策目标、政策工具、约束、资金面和曲线传导。
- 必须要求差分推算给出公式或基数。

### Task 2: MCP 与 OpenClaw 接口说明修正

涉及文件：

- `.mcp.example.json`
- `references/04-mcp-connectors.md`
- `references/02-data-source-policy.md`

验收：

- 文档明确：OpenClaw 使用 `openclaw mcp set <name> '<json>'` 注册 MCP。
- 文档明确：不要直接在 `openclaw.json` 顶层写入 `mcpServers`。
- Tushare 可作为 Python workflow 或 MCP server，但 FICC skill 只消费数据包。

### Task 3: 本地验证

运行：

```powershell
python .\scripts\extract_image_urls.py
python .\scripts\build_source_index.py
python .\scripts\validate_source_refs.py
python .\scripts\validate_skill_links.py
python C:\Users\kevin\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\000AAA_Datas\Python\Skills\FICC_Researcher
```

验收：

- 25 份本地源资料索引通过。
- 7 张 evidence cards、9 个模板、12 个 playbook 通过。
- quick validate 通过。

### Task 4: GitHub 推送

提交前检查：

- `git ls-files references/source-reports` 只能出现 `.gitkeep`。
- `git status --short --ignored` 中 source reports 应保持 ignored。

提交信息使用中文，说明：

- 改动原因
- 改动内容
- 验证情况
- 注意事项
- 后续方向

### Task 5: OpenClaw VM 同步

同步目标：

- `~/.openclaw/workspace/skills/ficc-researcher`

同步范围：

- `SKILL.md`
- `.gitignore`
- `.mcp.example.json`
- `README.md`
- `LICENSE`
- `agents/`
- `assets/`
- `docs/`
- `references/`
- `scripts/`

排除：

- `.git/`
- `.tmp*/`
- `references/source-reports/**`
- `outputs/`
- `tmp/`

验收：

- VM 上新版文件存在。
- VM 上 `source-reports` 只保留 `.gitkeep`。
- OpenClaw gateway 和 Feishu 仍正常。

## 数据或接口变化

- GitHub 仓库新增公开框架文件和模板。
- OpenClaw VM 的 skill 副本更新。
- OpenClaw MCP 配置不在本阶段新增，避免影响 gateway 稳定性。

## 风险和回滚

- 风险：同步误带源研报原文。控制方式：打包前排除 `references/source-reports/**`，同步后检查。
- 风险：OpenClaw 配置被错误 MCP 示例污染。控制方式：只更新 skill 文件，不写 `openclaw.json`。
- 回滚：OpenClaw 同步前备份旧目录为 `ficc-researcher.bak-YYYYMMDD-HHMMSS`。

## 当前状态

进行中。
