# Yield Curve Missing Data Example

## Prompt

请评价当前 1Y/3Y/5Y/10Y/30Y 国债和国开曲线。如果没有实时曲线、资金、供给和机构数据，只能给框架判断和需要补充的数据。

## Missing Fields

```text
当前缺少数据:
- 字段: 1Y/3Y/5Y/7Y/10Y/30Y 国债曲线、国开或政策金融债曲线、DR007/R007、NCD 利率、政府债发行和缴款、配置盘需求、国债期货基差。
- 推荐来源: ChinaBond, CFETS, SHCH, NIFC, Wind, iFinD, local bond database, user-provided exports.
- 时间范围: 当前交易日和至少一个比较日。
- 频率: 日频；资金面和交易拥挤度可使用更高频数据。
- 用途: 判断曲线分段、期限利差、资金锚、供给冲击、配置吸收和组合风险。
在缺少以上数据前，只能给出框架判断，不能给出当前市场结论。
```

## Allowed Framework Analysis

- Explain how short end depends on funding, central-bank operations, NCD pressure, and bank liability constraints.
- Explain how 3Y-7Y depends on carry, rolldown, allocation demand, and macro expectations.
- Explain how 10Y and 30Y depend on growth expectations, fiscal supply, insurer demand, term premium, and crowded positioning.
- State that weak macro data can be rates-friendly but may be offset by supply, policy expectations, or valuation.

## Forbidden Claims

- Do not give current curve levels without current source and timestamp.
- Do not say 10Y or 30Y must go down because data is weak.
- Do not recommend leverage without repo, NCD, product-liability, and liquidity data.
- Do not infer CDB or credit spreads from treasury levels alone.

## Expected Answer Shape

```text
曲线数据来源:
期限分段:
短端驱动:
中端驱动:
长端驱动:
供需与机构行为:
可用策略:
缺少数据:
风险触发:
```
