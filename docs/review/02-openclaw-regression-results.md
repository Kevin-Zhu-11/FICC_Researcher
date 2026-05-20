# FICC Researcher 02 OpenClaw Regression Results

## Environment

- Host: `<vm-ssh-target>`
- OpenClaw: `2026.5.12`
- Skill path: `~/.openclaw/workspace/skills/ficc-researcher`
- Gateway: reachable on local loopback.
- Skill permissions after sync: read-only directory.

## Skill Visibility

OpenClaw reported:

```text
ficc-researcher ✓ Ready
Source: openclaw-workspace
Visible to model: yes
Available as command: yes
```

## Validation Commands

Remote commands passed:

```bash
python3 scripts/build_source_index.py
python3 scripts/validate_source_refs.py
python3 scripts/validate_skill_links.py
```

Key outputs:

```text
source_reports_count=23
indexed_reports_count=23
unknown_source_ids=0
required_playbooks=12
evidence_cards_count>=6
templates_count>=3
validation_passed=true
```

## Prompt Results

| Prompt | Result |
| --- | --- |
| 当前低利率环境下，10 年国债收益率上行需要哪些条件？ | Passed. Routed to `rates-macro.md` and `bond-strategy.md`; included data-needed block, source evidence, risks, and follow-up indicators. |
| 信用利差处于低位时，信用债还能怎么做收益？ | Passed. Routed to `credit-strategy.md`, `institution-behavior.md`, and `bond-strategy.md`; avoided current-market conclusions. |
| 银行理财赎回为什么会影响信用债和短端利率？ | Passed. Routed to `wealth-management-funds`, `institution-behavior`, `credit-strategy`, and `rates-macro`; explained redemption feedback and missing data. |
| 转债估值应该看平价溢价率还是债底？ | Passed. Routed to `convertible-hybrid`; separated parity zone, bond floor, clauses, and data gaps. |
| 城投化债背景下，区域利差该如何分析？ | Passed. Routed to `city-investment-bonds.md` and `credit-strategy.md`; included city-investment source evidence and policy-risk caveats. |
| 如果没有实时数据，你能给出哪些数据清单和分析路径？ | Passed. Returned data checklist, analysis path, source evidence, risks, and follow-up indicators without fabricating market data. |
| 用户提供信用利差/DR007 模拟数据 | Passed. Identified user data, computed limited static relationships, stated what the data can and cannot support, and listed missing fields. |
| 用户提供转债模拟数据 | Passed. Used `convertible-hybrid`, computed implied price and bond-floor gap, and stated missing terms/valuation data. |

## Failures Or Deviations

- No blocking failures.
- OpenClaw prints a non-blocking warning that `plugins.allow` is empty. This is an OpenClaw hardening item outside this skill's repository.
- WebSearch is available in OpenClaw, but previous web-fetch testing showed some fetches may be blocked by network safety rules. FICC should treat WebSearch as source discovery, not market-data retrieval.

## Conclusion

- OpenClaw regression passed for the 95% no-credential completion target.
- The skill can route framework questions, use new playbooks, handle user-provided data, and avoid fabricated current market data.
- 100% completion remains conditional on a real data connector such as Tushare MCP, iFinD, Wind, or a local bond database.
