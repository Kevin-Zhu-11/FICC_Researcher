# Macro Social Financing Public Example

## Prompt

请使用 ficc-researcher 分析一组社融和货币数据对债市的影响。数据包位于 `examples/data/macro-social-financing-public-sample.yml`。如果缺少收益率、利差、资金利率或市场预期，只能给框架判断和缺口清单。

## Files The Agent Should Read

- `SKILL.md`
- `references/00-routing.md`
- `references/02-data-source-policy.md`
- `references/03-data-integration-policy.md`
- `references/07-macro-indicator-glossary.md`
- `references/08-policy-reaction-function.md`
- `references/09-data-interface-catalog.md`
- `references/10-workflow-entrypoints.md`
- `references/11-research-decision-chains.md`
- `references/12-data-connector-mapping.md`
- `references/playbooks/rates-macro.md`
- `references/playbooks/bond-strategy.md`
- `assets/templates/macro-data-commentary-template.md`

## Data Packet

Use `examples/data/macro-social-financing-public-sample.yml`.

The packet is synthetic and desensitized. A good answer must label it as example data and must not treat it as an official market fact.

## Expected Answer Shape

```text
问题归类:
使用 playbook:
数据来源与时间:
数据质量检查:
数据事实:
预期差:
政策反应函数:
债市传导:
曲线含义:
信用与机构行为:
不能确认的部分:
风险与反例:
后续跟踪:
```

## Why This Is Good

- It separates synthetic data facts from stable framework facts.
- It refuses to call the release above or below expectation without consensus data.
- It treats social financing aggregate as an entry point, not as proof of private endogenous demand.
- It asks for current yield curve, funding, credit-spread, and institution-flow data before drawing current market conclusions.

## What Would Fail

- Calls the release "低于预期" without consensus, survey, or market-pricing evidence.
- Invents current 10Y CGB, 10Y CDB, DR007, NCD, or credit-spread levels.
- Treats aggregate social financing as private demand without decomposition.
- Presents synthetic example records as official PBOC or provider-returned data.
- Gives personalized portfolio advice or guaranteed return language.
