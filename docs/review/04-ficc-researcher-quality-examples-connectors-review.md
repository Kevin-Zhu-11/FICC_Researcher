# 04 FICC Researcher Quality Examples And Connector Mapping Review

## 审查结论

- 结论: 通过，可以执行。
- 建议执行方式: 分 04A 到 04E 五段小步推进，每段完成后运行本地校验；04A 必须先创建 12/13 最小骨架，再从 `SKILL.md` 链接它们。
- 必要条件: 不提交源研报、token、账号、私有端点、付费数据库导出或 OpenClaw 本地敏感日志。

## 目标一致性

04 号方案与项目目标一致：

- 继续把 FICC Researcher 定位为研究框架、数据需求、输出纪律和验证标准，而不是数据接口实现本身。
- 继续支持 Codex、OpenClaw、Claude-style agents 和个人项目 agent 复用。
- 继续沿用 `skill-creator` 的渐进披露结构，避免 `SKILL.md` 膨胀。
- 继续借鉴 Anthropic financial-services 的 connectors / workflows / file-based checks 思路，但不照搬其插件目录。

## 1-5 步审查

### Step 1: 压缩入口和高频引用

必要性:

- 03B 后 `SKILL.md` 已能导航，但后续继续增加 Tushare、样例和 OpenClaw 说明会有上下文膨胀风险。

可执行性:

- 需要先创建 `references/12-data-connector-mapping.md` 和 `references/13-openclaw-skill-hygiene.md` 的最小骨架，再调整 `SKILL.md` 导航和少量重复说明，不影响 playbook 语义。

风险:

- 如果删得过多，agent 可能不知道 12/13 存在。

控制:

- `SKILL.md` 保留一行式导航；详细内容放 `references/12-data-connector-mapping.md` 和 `references/13-openclaw-skill-hygiene.md`。若 12/13 未创建，不允许先改 `SKILL.md` 链接。

### Step 2: 质量评分 rubric

必要性:

- 03B eval 证明 agent 能成功运行和满足块结构，但还没有评估来源纪律、推理深度、风险反例和反幻觉质量。

可执行性:

- `quality-rubrics.yml` 可以先作为人工评分和结构校验标准，不需要复杂自动评分。

风险:

- LLM 自动评分容易给出虚假的精确感。

控制:

- 脚本只检查 rubric 结构、workflow 覆盖和字段合法性；金融质量保留人工抽样或盲评。

### Step 3: Golden examples

必要性:

- Codex/OpenClaw/Claude 需要能模仿的合格输出，尤其是“数据缺失时仍然有价值”的答案。

可执行性:

- 先做 1 个宏观数据点评样例和 1 个缺失曲线数据样例即可，不需要铺开所有 playbook。

风险:

- 公共宏观样例如果粘贴过多来源内容或使用付费导出，会带来版权和数据许可风险。

控制:

- 使用很小的公开或脱敏 data packet；记录 source、retrieved_at、fields、row_count、records、limitations；不放空壳 `YYYY-MM`、`row_count: 0` 和 `records: []` 作为最终 golden example；不放券商研报大段原文和付费数据库导出。

### Step 4: 连接器映射层

必要性:

- 用户已经明确希望 FICC skill 负责研究框架和数据需求，Tushare/iFinD/Wind/WebSearch 负责取数；需要把这个边界写成 agent 可执行规则。

可执行性:

- `references/12-data-connector-mapping.md` 只做字段到 provider 候选的映射，不要求实际接口可用。

风险:

- 显式写 Tushare 接口可能被误解为仓库内置服务、官方授权或必须依赖。

控制:

- 写清 optional candidate、用户自行配置、遵守服务条款、仓库不分发数据、不写 token、不保证覆盖。

### Step 5: OpenClaw 卫生

必要性:

- 03B 测试中出现过旧 `ficc-researcher.bak-*` 被读取的问题；OpenClaw skill discovery 和同步范围需要制度化。

可执行性:

- 写成 `references/13-openclaw-skill-hygiene.md` 和 README 简述即可，不改变 OpenClaw 配置。

风险:

- 如果文档里写入真实主机、私有路径或 token，会污染公开仓库。

控制:

- 使用占位符和本地路径模式，不写真实 token、账号、内网地址或私有服务配置。
- 同步命令必须优先使用 Git-tracked public files，例如 `git archive` 或 `git ls-files` 生成复制清单；禁止从 working tree 盲目递归复制，因为本地 ignored `references/source-reports/` 可能含有版权敏感资料。

## 过度设计检查

当前方案没有要求：

- 新建多个子 skill。
- 新增真实数据库。
- 生成平台专有 slash command。
- 自动抓取 Wind/iFinD/Tushare 数据。
- 自动给金融结论打分并替代人工判断。

因此过度设计风险可控。

## 安全与合规审查

必须继续遵守：

- `references/source-reports/**` 不进入公开仓库，除 `.gitkeep`。
- `.env`、token、API key、OpenClaw 私有配置不进入公开仓库。
- 连接器名称可以作为 optional source 出现，但不能写成授权、背书或再分发声明。
- 真实市场数据、收益率、利差、持仓、NAV、估值分位必须有来源、时间戳和字段说明。

新增检查建议：

```powershell
git ls-files references/source-reports
$secretPattern = ('(?i)(tok' + 'en|api[_-]?key|pass' + 'word|secret)\s*[:=]\s*["'']?[A-Za-z0-9_./+=-]{16,}|sk-[A-Za-z0-9]{20,}')
git ls-files | Select-String -NotMatch '^references/source-reports/' | ForEach-Object { Select-String -Path $_.Line -Pattern $secretPattern -ErrorAction SilentlyContinue }
```

## 与原始研报框架的关系

04 号不需要新增大量研报摘录。它应复用 03B 已抽象出的框架：

- 宏观到债市: 指标事实、口径、预期差、经济循环、政策反应、资金和供给、曲线分段。
- 信用到配置: 利差水平、主体基本面、再融资、机构需求、流动性补偿、下沉边界。
- 机构到市场: 负债稳定性、净值反馈、杠杆能力、久期偏好、赎回循环。
- 组合动作: 久期、曲线、杠杆、信用仓位、触发条件和反例。

04 号重点是让这些框架在真实 agent 执行时更稳定，而不是继续扩大知识库体量。

## 验证方式审查

修订后的验证足够作为 04 号第一阶段完成标准：

```powershell
python .\scripts\validate_skill_links.py
python .\scripts\validate_eval_cases.py
python .\scripts\validate_quality_rubrics.py
python .\scripts\validate_examples.py
python <local-skill-creator>\scripts\quick_validate.py .
git ls-files references/source-reports
$secretPattern = ('(?i)(tok' + 'en|api[_-]?key|pass' + 'word|secret)\s*[:=]\s*["'']?[A-Za-z0-9_./+=-]{16,}|sk-[A-Za-z0-9]{20,}')
git ls-files | Select-String -NotMatch '^references/source-reports/' | ForEach-Object { Select-String -Path $_.Line -Pattern $secretPattern -ErrorAction SilentlyContinue }
```

OpenClaw 侧建议复测：

```text
- 1 个 current-market-data anti-hallucination case
- 1 个 macro-social-financing data-assisted case
- 1 个 yield-curve missing-data case
```

## 可以开始执行吗

可以。建议下一步从 04A 开始：先做入口压缩和 12/13 导航，再做 rubric 和 examples。这样即使后续样例或脚本需要调整，也不会影响当前已经稳定的 03B 路由。

修订后执行顺序为：04A 先创建 12/13 最小骨架，再压缩入口和增加导航；04D/04E 再分别扩展 12/13 的完整内容。这样可以避免 `SKILL.md` 指向不存在文件导致校验失败。

## 当前状态

- 计划文件: `docs/projects/04-ficc-researcher-quality-examples-connectors-plan.md`
- 审查文件: `docs/review/04-ficc-researcher-quality-examples-connectors-review.md`
- 状态: 已按修订后的审查意见完成本地实施；OpenClaw 复测待同步后执行。
