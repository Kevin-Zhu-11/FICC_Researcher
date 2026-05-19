# Research Decision Chains

Use this file when a question spans multiple playbooks or when an agent needs a repeatable reasoning path rather than a free-form essay.

## Macro Release To Rates

```text
指标事实
-> 口径、频率、公布机构
-> 相对预期、相对前值、季节性、基数
-> 经济循环: 消费 / 制造业 / 地产 / 外需 / 财政金融
-> 政策目标: 增长就业 / 价格 / 金融稳定 / 汇率
-> 政策工具与约束
-> 资金面、财政供给、风险偏好
-> 收益率曲线分段
-> 信用和机构行为
-> 组合动作和风险触发
```

Common errors:

- 社融高不等于私人需求强。
- M2 高不等于交易活化。
- PPI 反弹不等于全面需求过热。
- 单月弱数据不等于趋势性信用收缩。
- 未看到当前收益率和利差前，不要给点位判断。

Required data:

- Actual value, previous value, expectation if available, decomposition, release source, curve, funding, credit spread, policy context.

## Funding To Curve

```text
央行操作与财政缴款
-> DR007/R007/NCD/Shibor
-> 银行负债和非银杠杆成本
-> 短端利率锚
-> 中端 carry/rolldown
-> 长端期限溢价和配置需求
-> 曲线形态
-> 杠杆和久期风险
```

Common errors:

- 宽资金不等于杠杆无风险。
- 短端低位不等于长端一定下行。
- 资金价格稳定不等于产品负债稳定。

Required data:

- Repo rates, repo volume, NCD yield and issuance, OMO/MLF, fiscal payment, product flow, curve points.

## Fiscal Supply To Duration

```text
预算与发行计划
-> 发行节奏、缴款、净融资
-> 配置盘吸收能力
-> 银行表内、保险、基金和理财需求
-> 期限溢价
-> 10Y/30Y 波动
-> 久期仓位和止盈纪律
```

Common errors:

- 财政加力既支持增长，也增加债券供给。
- 政府债单月高位不等于财政支出已经形成实物工作量。
- 超长债基本面利多可能被供给和拥挤交易抵消。

Required data:

- Issuance calendar, net financing, maturity, payment date, fiscal expenditure, curve supply by tenor, investor absorption.

## Credit Spread To Allocation

```text
利差水平和分位
-> 主体基本面
-> 再融资环境
-> 供给和净融资
-> 机构需求和负债稳定性
-> 流动性补偿
-> 下沉、拉久期或高等级 carry
-> 退出条件和风险触发
```

Common errors:

- 信用利差低不等于信用风险消失。
- 资产荒不等于所有低资质主体安全。
- 票息不是无风险收益。
- 宽资金不能替代主体现金流和再融资验证。

Required data:

- Spread by rating/sector/tenor, issuer cash flow, maturity wall, issuance, cancellation, default/extension, fund and wealth demand.

## Institution Behavior To Market

```text
负债稳定性
-> 久期偏好
-> 杠杆能力
-> 净值波动
-> 申赎或配置反馈
-> 利率债需求
-> 信用利差
-> 曲线和流动性
```

Common errors:

- 只看收益率变化，不看产品净值和负债端。
- 把银行、理财、基金、保险视为同一类买盘。
- 忽略赎回反馈对信用债流动性的放大。

Required data:

- AUM, flows, NAV drawdown, holdings, duration, leverage, insurance premium, bank deposit and bond allocation.

## Policy Event To Portfolio

```text
政策事实
-> 政策目标
-> 工具类型
-> 约束条件
-> 是否超预期
-> 资金、供给、风险偏好、信用风险
-> 可交易部分
-> 组合动作
-> 反例与止损
```

Common errors:

- 把政策表述当成已经发生的流动性投放或财政支出。
- 只看增长利多，忽略供给压力。
- 忽略汇率、银行净息差、债市杠杆和金融稳定约束。

Required data:

- Official policy text, release time, tool details, expected/actual gap, market pricing before and after, implementation calendar.

## Convertible To Hybrid Allocation

```text
正股趋势和波动
-> 平价和转股溢价率
-> 债底和信用保护
-> 条款状态
-> 流动性
-> 股债性分类
-> 组合角色
-> 风险触发
```

Common errors:

- 只看正股弹性，忽略债底、溢价率和条款。
- 把低价转债自动视为安全。
- 忽略评级、流动性和赎回/下修约束。

Required data:

- Convertible price, stock price, conversion price, parity, premium, bond floor, YTM, clause status, rating, volume.

## Offshore Rates And Credit To Domestic FICC

```text
海外政策和 UST 曲线
-> 美元指数和 CNH
-> 套保成本
-> 离岸融资和中资美元债利差
-> 点心债/离岸人民币债供需
-> 境内利率和信用相对价值
```

Common errors:

- 不看汇率和套保成本就比较境内外收益。
- 把 UST 下行直接等同于境内长端下行。
- 忽略离岸流动性和发行人信用差异。

Required data:

- UST curve, Fed path, DXY/CNH, hedge cost, issuer spread, offshore issuance, rating, liquidity.
