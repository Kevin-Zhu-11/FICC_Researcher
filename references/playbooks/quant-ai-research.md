# Quant AI Research

## Scope

Use this playbook for fixed-income quant research, AI research workflows, factor extraction, monitoring, report automation, agent design, and data-to-framework research systems.

## When To Use

- The question mentions 固收量化, AI投研, 因子, 监控, 智能体, 自动化报告, LLM, prompt, or 数据驱动研究.
- The user wants to turn research reports or market data into repeatable signals or monitoring workflows.
- The answer needs model validation and human review boundaries.

## Required Inputs

- Research question, universe, data dictionary, source, timestamp, frequency, and field definitions.
- Factor or rule definition, expected sign, economic intuition, sample period, and rebalance frequency.
- Labels or outcomes: returns, spread changes, default events, drawdowns, redemptions, or policy events.
- Validation: train/test split, out-of-sample period, turnover, transaction cost, robustness, false positives.
- Monitoring: alert threshold, update cycle, dashboard/report format, responsible reviewer.

## Framework

```text
research question
-> data contract and quality checks
-> factor / rule / prompt workflow
-> validation and robustness
-> monitoring and human review
-> report or action recommendation with audit trail
```

AI can accelerate parsing, routing, summarization, and candidate generation. It should not be treated as a source of data facts unless connected to verified data.

## Analysis Steps

1. Define the research problem and decision target.
2. Specify data contract: universe, fields, timestamp, frequency, and source.
3. Define factor, rule, prompt workflow, or agent pipeline.
4. Establish validation: sample split, metrics, costs, turnover, and failure cases.
5. Define monitoring and human review.
6. Produce a reproducible output contract.
7. If data or labels are missing, return required data and validation design instead of a performance claim.

## Output Template

```text
使用 playbook: quant-ai-research
研究问题:
数据契约:
因子/规则/智能体流程:
验证设计:
监控方案:
缺失数据:
风险与反例:
```

## Risk Checks

- Do not treat LLM summaries as data facts.
- Do not accept factor performance without out-of-sample validation.
- Check look-ahead bias, survivorship bias, point-in-time availability, and transaction costs.
- Check whether labels are observable at decision time.
- Keep human review for investment and risk decisions.

## Source Reports

- `huatai-quant-ai-ficc-2025`
- `cicc-ficc-ai-agent-path-2025`

## Search Keywords

固收量化, AI投研, 因子, 智能体, 监控, Prompt, LLM, 数据契约, 回测, 样本外, 自动化报告
