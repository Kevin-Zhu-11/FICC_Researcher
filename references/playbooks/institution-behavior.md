# Institution Behavior

## Scope

Use this playbook for marginal demand and selling pressure from commercial banks, insurance companies, bank wealth management, mutual funds, broker proprietary books, foreign investors, pensions, and other liability-driven fixed-income investors.

## When To Use

- The question mentions 机构行为, 银行, 保险, 理财, 公募基金, 券商自营, 外资, 年金, 赎回, 配债, 欠配, 资产荒, or 负债端.
- The market move cannot be explained by macro data alone.
- The answer needs a demand-side explanation for rates, credit spreads, liquidity, or curve segments.

## Required Inputs

- Commercial banks: deposit growth, loan demand, LCR/NSFR pressure, NCD issuance, interbank assets, bond allocation.
- Insurance: premium growth, liability duration, accounting rules, solvency pressure, long-bond allocation.
- Wealth management: product NAV, redemption flow, asset duration, leverage, cash buffer, credit exposure.
- Mutual funds: fund shares, subscription/redemption, duration, leverage, credit exposure, ranking pressure.
- Brokers and proprietary books: repo leverage, VaR limits, trading inventory, funding access.
- Foreign investors: FX hedge cost, rate differential, custody flows, global risk appetite.
- Pensions and annuity: liability matching, allocation policy, long-duration demand.

## Framework

Institution behavior is the bridge between macro financing demand and bond-market pricing:

```text
financing demand and policy
-> bank balance sheets and deposits
-> wealth management, funds, insurance, brokers, foreign investors
-> marginal demand for rates, credit, short-end, long-end, and liquidity
-> feedback to yields, spreads, leverage, and market volatility
```

Analyze institutions by liability stability, regulatory/accounting constraints, tax treatment, leverage capacity, investment scope, and liquidity needs. The same yield move can have different meanings when the marginal buyer changes.

## Framework Claims

| Claim id | Claim | Mechanism | Fails when |
| --- | --- | --- | --- |
| `IH-01` | 机构行为通过负债稳定性、会计、监管、杠杆能力和流动性需求传导到边际买盘和卖盘。 | 不同机构的负债和约束决定其久期、信用、杠杆、现金和流动性偏好。 | 缺少申赎、持仓、久期、杠杆、保费、存款或托管流数据。 |

## Analysis Steps

1. Identify the likely marginal institution for the instrument and tenor.
2. Map its liability-side condition: stable inflow, redemption pressure, deposit pressure, premium inflow, or FX-driven flow.
3. Map its constraints: rating, tenor, accounting, liquidity, leverage, risk budget, tax, and regulation.
4. Infer likely behavior: buy duration, shorten duration, sell credit, increase liquidity, leverage carry, or de-risk.
5. Check feedback loops: redemption selling, spread widening, NAV pressure, and further redemptions.
6. Use `references/09-data-interface-catalog.md` for required flow, holding, NAV, duration, leverage, and liability data.
7. Use `references/11-research-decision-chains.md` for institution-behavior-to-market transmission.
8. Combine with rates or credit playbooks when pricing conclusions are needed.

## Output Overlay

```text
使用 playbook: institution-behavior
涉及机构:
负债端状态:
约束条件:
可能行为:
对利率/信用/流动性的影响:
缺失数据:
风险与反例:
```

## Risk Checks

- Do not treat all institutions as yield-chasing buyers.
- Check whether accounting rules reduce or amplify mark-to-market selling.
- Check whether redemption pressure forces liquid-asset selling before risky-asset selling.
- Check whether banks are constrained by deposits or capital rather than by yield preference.
- Distinguish structural allocation demand from short-term trading flow.
- Do not infer current institution positions from news or market moves alone.

## Source Reports

- `huatai-institution-behavior-2025`
- `cicc-low-rate-investor-behavior-2025`
- `cicc-bond-principles-strategy-2025`
- `cicc-wealth-management-net-value-2025`
- `cicc-credit-strategy-low-spread-2025`

## Claim IDs

- `IH-01`

## Search Keywords

机构行为, 商业银行, 保险, 银行理财, 公募基金, 券商自营, 外资, 年金, 负债端, 赎回, 配债, 欠配, 资产荒
