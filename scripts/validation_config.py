"""
文件路径: scripts/validation_config.py
文件作用: 集中管理 FICC Researcher 结构校验脚本共用的数量和文件清单。
主要内容:
- EXPECTED_SOURCE_COUNT: 源报告索引期望数量
- REQUIRED_*: 必需文件、playbook、证据卡、模板和示例清单
依赖关系:
- 无第三方依赖
使用场景:
- build_source_index.py、validate_source_refs.py、validate_skill_links.py 复用同一套校验常量
注意事项:
- 新增正式 playbook、证据卡、模板或源报告后，应优先更新本文件，再运行验证脚本
"""

from __future__ import annotations


EXPECTED_SOURCE_COUNT = 25

REQUIRED_FILES = [
    ".mcp.example.json",
    "SKILL.md",
    "agents/openai.yaml",
    "references/00-routing.md",
    "references/01-source-index.yml",
    "references/02-data-source-policy.md",
    "references/03-data-integration-policy.md",
    "references/04-mcp-connectors.md",
    "references/05-cross-platform-usage.md",
    "references/06-portfolio-action-policy.md",
    "references/07-macro-indicator-glossary.md",
    "references/08-policy-reaction-function.md",
    "references/09-data-interface-catalog.md",
    "references/10-workflow-entrypoints.md",
    "references/11-research-decision-chains.md",
    "references/12-data-connector-mapping.md",
    "references/13-openclaw-skill-hygiene.md",
    "references/14-contracts-and-analysis-standards.md",
    "references/15-playbook-framework-standard.md",
    "references/16-source-claim-map.yml",
    "references/chart-notes/key-framework-charts.md",
    "references/chart-notes/image-url-index.yml",
    "evals/smoke-prompts.yml",
    "evals/expected-output-contracts.yml",
    "evals/quality-rubrics.yml",
    "examples/data/macro-social-financing-public-sample.yml",
    "examples/golden-cases/macro-social-financing-public-example.md",
    "examples/golden-cases/yield-curve-missing-data-example.md",
    "scripts/validation_config.py",
    "scripts/validate_eval_cases.py",
    "scripts/validate_claim_map.py",
    "scripts/validate_source_refs.py",
    "scripts/validate_quality_rubrics.py",
    "scripts/validate_examples.py",
]

REQUIRED_PLAYBOOKS = [
    "rates-macro.md",
    "bond-strategy.md",
    "institution-behavior.md",
    "credit-strategy.md",
    "convertible-hybrid.md",
    "city-investment-bonds.md",
    "financial-credit.md",
    "wealth-management-funds.md",
    "derivatives.md",
    "offshore-global-rates.md",
    "abs-reits.md",
    "quant-ai-research.md",
]

REQUIRED_EVIDENCE_CARDS = [
    "abs-reits-evidence.md",
    "convertible-hybrid-evidence.md",
    "credit-evidence.md",
    "derivatives-evidence.md",
    "institution-wealth-evidence.md",
    "macro-policy-evidence.md",
    "offshore-global-rates-evidence.md",
    "quant-ai-evidence.md",
    "rates-macro-evidence.md",
]

REQUIRED_TEMPLATES = [
    "credit-spread-review-template.md",
    "daily-bond-brief-template.md",
    "data-assisted-analysis-template.md",
    "framework-analysis-template.md",
    "macro-data-commentary-template.md",
    "missing-data-template.md",
    "policy-event-commentary-template.md",
    "portfolio-action-template.md",
    "yield-curve-review-template.md",
]

REQUIRED_GOLDEN_EXAMPLES = [
    "macro-social-financing-public-example.md",
    "yield-curve-missing-data-example.md",
]
