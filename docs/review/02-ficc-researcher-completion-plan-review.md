# FICC Researcher 02 号计划审查报告

## 审查结论

- 通过，可以执行 02 号计划。
- 95% 完成度目标不依赖真实密钥或外部账号，适合立即推进。
- 100% 完成度必须以至少一个真实结构化数据连接器完成取数闭环为条件；没有凭据时不得宣称完成。

## 目标一致性

- 与 00 号设计思想一致: 单 skill、多 playbook、集中数据政策、可审计输出。
- 与 01 号执行成果一致: 在已有入口、路由、源报告索引、5 个主干 playbook、OpenClaw 测试基础上扩展。
- 与当前长期目标一致: 支持 Codex、Claude、OpenClaw 和个人 agent 复用。

## 范围清晰度

- 范围内:
  - 补齐 12 个核心 playbook。
  - 建立 evidence cards。
  - 增加 MCP/数据连接器模板。
  - 增加跨平台使用协议。
  - 增强验证脚本。
  - 完成 OpenClaw 回归测试。
- 范围外:
  - 写入真实 token、API key、账号密码。
  - 直接交易、组合调仓或投资建议执行。
  - 把 Tushare/iFinD/Wind 调用逻辑硬编码进 playbook。

## 过度设计检查

- 计划没有把 skill 拆成多个独立 skill，仍保持一个 `ficc-researcher` 入口。
- MCP 只做模板和边界，不强制绑定某个供应商。
- evidence cards 是源报告摘要层，不复制 23 篇全文。
- 输出模板放在 `assets/templates/`，不塞进 `SKILL.md`。

## 边界条件

- 如果 source reports 数量仍为 23，则验证脚本应继续要求 `source_reports_count=23`。
- 如果新增源报告，必须同步更新 `01-source-index.yml` 和验证脚本期望。
- 如果 OpenClaw 测试副本更新，应恢复只读权限。
- 如果接入真实 Tushare/iFinD/Wind，凭据必须留在环境变量、MCP 配置或本地 secret 管理中，不进入 Git。

## 验证充分性

计划要求:

- 本地 source index 校验。
- 本地 link 校验。
- source id 引用校验。
- `skill-creator` quick validate。
- OpenClaw skill ready 检查。
- 6 个核心验收问题。
- 1-2 个用户数据问题。
- 密钥扫描。

验证覆盖足够支撑 95% 完成度。

## 风险

- 7 个新 playbook 可能质量不均，需要执行时保持统一模板和 source id 校验。
- evidence cards 若写得像读书笔记，会降低可操作性；必须保留“用在什么问题、需要什么数据、常见误读”。
- WebSearch 可用但 web_fetch 之前出现过安全拦截，不能把 WebSearch 当作行情/估值主数据源。
- 100% 目标依赖外部数据权限，可能需要单独计划。

## 是否可以开始执行

可以开始执行。

建议先执行:

```text
Task 1 -> Task 2 -> Task 7
```

即先建立完成度基线、补齐 7 个 playbook，再马上增强验证脚本，避免后续内容漂移。
