# 05B Framework Deep Unification Review

## 审查结论

通过，可以执行。当前 05B 计划与 FICC Researcher 的单 skill、分层 references、数据源中立、版权边界和 OpenClaw 可移植目标一致。

## 计划是否和项目目标一致

一致。05A 已解决输出契约和数据接口契约；05B 继续处理框架层统一，属于让 Agent 更稳定使用 skill 的必要工作。

## 范围是否清楚

清楚。本阶段只处理框架表达、claim map、evidence card 对称性、quant-ai FICC 特化和验证脚本，不做真实数据接入、供应商 SDK、研报原文发布或 GitHub 推送。

## 是否存在过度设计

有一个潜在风险：claim map 如果做到 source report 段落级，会变成版权与维护负担。本阶段采用 playbook claim -> evidence card section -> source id 的层级，粒度足够让 Agent 溯源，又不会复制研报内容。

## 遗漏边界条件

需要特别覆盖：

- source id 必须全部存在于 `01-source-index.yml`。
- evidence card 文件名必须被 `validate_skill_links.py` 精确检查。
- 旧合并 evidence card 拆分后，不能留下 routing 指向旧文件。
- quant-ai smoke/rubric 必须显式禁止 generic quant pipeline only。

## 是否影响现有功能

影响 skill 内部指令和验证，不影响外部数据接口。新增的 `15`、`16` 会被 `SKILL.md` 和 routing 引入，但不会改变 05A 的 canonical output contract。

## 安全、版权、兼容性

- 安全：不写 token、账号、私有 URL。
- 版权：不复制 source reports 原文，只引用 source id。
- 兼容性：旧 playbook 文件名保持不变；evidence card 拆分后旧合并卡可删除，前提是验证和引用全部更新。

## 验证方式是否足够

足够。新增 `validate_claim_map.py` 后，完整验证链能够覆盖 source id、evidence card、claim id、eval prompt 和 skill-creator 基础格式。

## 是否可以开始执行

可以执行。
