# 05B FICC Researcher Framework Deep Unification Plan

## 阶段目标

把 FICC Researcher 从“多个可用 playbook 的集合”推进到“统一框架语言 + 可追溯 claim map + 对称 evidence cards”的结构。重点解决 playbook 框架表达不一致、跨框架冲突缺少元规则、claim 与 source evidence 脱节、合并 evidence card 不对称、quant-ai 过于泛化的问题。

## 背景说明

05A 已统一输出契约、data packet、缺失数据块、置信度和时间尺度。剩余问题集中在框架层：12 个 playbook 的 Framework 有因果链、组件加法、泛化流水线等多种写法；`11-research-decision-chains.md` 质量较高但没有成为 playbook 标准；`offshore-derivatives-abs-reits-evidence.md` 把 4 个领域合并；`quant-ai-research.md` 对 FICC 领域特征描述不足。

## 范围边界

本阶段做：

- 新增 playbook framework expression standard。
- 新增 source claim map，将每个 playbook 的核心 claim 映射到 evidence card section 和 source report id。
- 更新 `SKILL.md`、routing 和 workflow entrypoints，让 15/16 成为框架解释与溯源层。
- 把合并 evidence card 拆成 offshore、derivatives、ABS/REITs 三张卡。
- 强化 `quant-ai-research.md` 的 FICC factor families、PIT、频率错配、回测泄漏、估值口径和人工复核边界。
- 新增 claim map 校验脚本并纳入 validation chain。
- 记录重复/冲突清单和合并决策。

本阶段不做：

- 不复制或发布 source report 原文。
- 不给每篇 source report 做逐段摘要。
- 不引入真实数据接口或供应商 SDK。
- 不提交或推送，除非用户明确要求。

## 主要冲突与处理原则

| 冲突/重复 | 处理 |
| --- | --- |
| `Framework` 写法不统一 | 15 号文件定义统一的 claim table、mechanism、fails when、required data、decision chain 表达 |
| `rates-macro` 与 `institution-behavior` 对财政供给方向可能相反 | 统一为 competing channels，不互相覆盖，交给 `11` 的 fiscal supply chain 决定主导通道 |
| `credit-strategy` 与 `city/financial/ABS` 重叠 | credit-strategy 作为 generic spread layer，专业主体/结构交给专门 playbook |
| `bond-strategy` 与 `06-portfolio-action-policy` 重复 | bond-strategy 只给 portfolio reasoning，06 负责 action translation gate |
| `07` 和 `08` 都给宏观政策传导 | 07 负责 indicator glossary，08 负责 policy reaction filter |
| 合并 evidence card 不对称 | 拆分为 offshore、derivatives、abs-reits 三张卡 |
| quant-ai 泛化 | 增加 FICC factor families、PIT/time semantics、release lag、curve/spread panel、transaction cost 和 human review |

## 涉及文件

- `SKILL.md`
- `README.md`
- `references/00-routing.md`
- `references/10-workflow-entrypoints.md`
- `references/11-research-decision-chains.md`
- `references/14-contracts-and-analysis-standards.md`
- `references/15-playbook-framework-standard.md`
- `references/16-source-claim-map.yml`
- `references/playbooks/*.md`
- `references/evidence-cards/*.md`
- `scripts/validation_config.py`
- `scripts/validate_claim_map.py`
- `scripts/validate_skill_links.py`
- `evals/smoke-prompts.yml`
- `evals/quality-rubrics.yml`

## 验证方式

```powershell
python .\scripts\build_source_index.py
python .\scripts\validate_source_refs.py
python .\scripts\validate_claim_map.py
python .\scripts\validate_skill_links.py
python .\scripts\validate_eval_cases.py
python .\scripts\validate_quality_rubrics.py
python .\scripts\validate_examples.py
```

本机可再运行 `skill-creator quick_validate.py`。

## 风险和回滚

- 风险：claim map 如果过细，会增加维护成本；如果过粗，又不能解决溯源问题。本阶段用 playbook-level claim，而不是 source-report paragraph-level claim，保持可维护。
- 风险：拆分 evidence card 可能破坏旧引用。本阶段同时更新 validation config 和相关引用。
- 回滚：恢复 05B 涉及文件，删除 `15`、`16` 和 `validate_claim_map.py`。

## 当前状态

进行中。
