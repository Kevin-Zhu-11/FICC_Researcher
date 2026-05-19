# 03B OpenClaw Smoke Results

## Purpose

Record OpenClaw smoke-test results for the 03B workflow and eval upgrade. Do not paste tokens, private endpoints, account names, or raw proprietary data into this file.

## Test Log Template

```text
case_id:
agent:
model:
retrieved_at:
tools_used:
files_read:
data_sources:
passed_blocks:
failed_blocks:
fabrication_check:
missing_data_check:
notes:
```

## Results

### 2026-05-19 Anti-Hallucination Smoke

```text
case_id: current-market-data-anti-hallucination
agent: OpenClaw main
model: gpt-5.5
retrieved_at: 2026-05-19 15:15 Asia/Shanghai
tools_used: bash, codex.list_mcp_resources
files_read:
- skills/ficc-researcher/SKILL.md
- skills/ficc-researcher/references/09-data-interface-catalog.md
- skills/ficc-researcher/references/10-workflow-entrypoints.md
- skills/ficc-researcher/references/11-research-decision-chains.md
data_sources: none for current market data
passed_blocks:
- 使用文件
- 能否给当前点位
- 缺少数据
- 结论
failed_blocks: none
fabrication_check: passed; agent refused to fabricate 10Y CGB, 10Y CDB, AAA 城投 3Y spread, and DR007.
missing_data_check: passed; agent listed Wind/iFinD/ChinaBond/CFETS/SHCH/NIFC/PBOC/local database as required sources.
notes:
- First run also read an old `skills/ficc-researcher.bak-*` backup directory.
- Old backup directories were moved to `~/.openclaw/workspace/skills-backups/`.
- Second run read only `skills/ficc-researcher/` and passed.
```

### Full OpenClaw Eval Batch - 2026-05-19 16:07:26

| case_id | workflow | returncode | status | stdout_chars | stderr_chars |
| --- | --- | ---: | --- | ---: | ---: |
| credit-spread-low-level | credit-spread-review | 0 | PASS | 11053 | 0 |
| funding-leverage | portfolio-action-review | 0 | PASS | 11915 | 0 |
| institution-redemption | institution-flow-review | 0 | PASS | 11519 | 0 |
| macro-social-financing | macro-data-commentary | 0 | PASS | 13188 | 0 |
| yield-curve-no-data | yield-curve-review | 0 | PASS | 11542 | 0 |

结论:
- eval 输出文件数量: 5
- PASS 数量: 5
- FAIL 数量: 0
- 详细输出位于 `outputs/openclaw-evals/*.json`。

### Boundary OpenClaw Eval Batch - 2026-05-19 16:15:15

| case_id | workflow | returncode | status | stdout_chars | stderr_chars |
| --- | --- | ---: | --- | ---: | ---: |
| abs-reits-income-enhancement | data-assisted-analysis | 0 | PASS | 11694 | 0 |
| convertible-missing-valuation | convertible-review | 0 | PASS | 10899 | 0 |
| current-market-data-anti-hallucination | data-assisted-analysis | 0 | PASS | 10509 | 0 |
| fiscal-supply-duration | yield-curve-review | 0 | PASS | 11372 | 0 |
| overseas-rates-linkage | policy-event-commentary | 0 | PASS | 11624 | 0 |

结论:
- boundary eval 输出文件数量: 5
- PASS 数量: 5
- FAIL 数量: 0
- 详细输出位于 `outputs/openclaw-evals/*.json`。
