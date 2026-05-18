# FICC Researcher 01 号执行复盘

## 审查结论

- 通过，可以作为第一版 `ficc-researcher` skill 骨架继续扩展。
- 当前版本完成入口、路由、数据源纪律、源报告索引、首批主干 playbook、关键图表文字重构和结构校验脚本。
- 本阶段不包含真实 MCP 连接配置、不包含密钥、不包含投资建议自动化执行。

## 完成范围

- 新增 `SKILL.md` 和 `agents/openai.yaml`。
- 新增 `references/00-routing.md`、`references/01-source-index.yml`、`references/02-data-source-policy.md`。
- 新增首批 5 个 playbook:
  - `rates-macro.md`
  - `bond-strategy.md`
  - `institution-behavior.md`
  - `credit-strategy.md`
  - `convertible-hybrid.md`
- 新增 `references/chart-notes/key-framework-charts.md`，首批转写 5 张关键框架图。
- 新增 `scripts/build_source_index.py` 和 `scripts/validate_skill_links.py`。

## 验证记录

已运行:

```powershell
python .\scripts\build_source_index.py
```

结果:

```text
source_reports_count=23
indexed_reports_count=23
missing_files=0
unindexed_files=0
```

已运行:

```powershell
python .\scripts\validate_skill_links.py
```

结果:

```text
ok: SKILL.md
ok: agents/openai.yaml
ok: references/00-routing.md
ok: references/01-source-index.yml
ok: references/02-data-source-policy.md
ok: references/chart-notes/key-framework-charts.md
ok: playbooks_count>=5
ok: source_reports_count=23
validation_passed=true
```

已运行:

```powershell
$env:PYTHONPATH='D:\000AAA_Datas\Python\Skills\FICC_Researcher\.tmp_pyyaml'
python C:\Users\kevin\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\000AAA_Datas\Python\Skills\FICC_Researcher
```

结果:

```text
Skill is valid!
```

## 依赖说明

- 官方 `quick_validate.py` 依赖 `PyYAML`。
- 当前系统 Python 和 Codex bundled Python 默认未安装 `PyYAML`。
- 本次为运行官方验证，将 `PyYAML` 临时安装到 `.tmp_pyyaml/`，该目录受 `.gitignore` 的 `.tmp*/` 规则忽略，不进入版本跟踪。

## 影响面

- 只影响 `D:\000AAA_Datas\Python\Skills\FICC_Researcher` 独立 Git 仓库。
- 未修改 `D:\000AAA_Datas\Python\Skills` 下其他 skill。
- 未创建真实 `.mcp.json`，未写入任何 token、API key、账号或私有连接信息。

## 风险和后续

- `source_role` 当前统一为 `framework`，后续可细分为 `core_framework`、`supporting_framework`、`future`。
- 城投、大金融、理财、衍生品、海外债、ABS/REITs、量化 AI 仍是 future playbook，需要 02 号计划扩展。
- 图表 URL 目前只做文字重构，未逐个固化原始 URL；后续可从源 Markdown 中抽取并建立图片索引。
- 当前 skill 是研究辅助框架，不替代实时行情、信用尽调或投资决策。
