"""
文件路径: scripts/validate_skill_links.py
文件作用: 校验 FICC Researcher skill 的关键文件、必需 playbook 和公开仓库结构。
主要内容:
- require_file: 检查必需文件存在
- count_markdown: 统计指定目录下 Markdown 文件数量
- require_playbooks: 检查 12 个核心 playbook 是否存在
- main: 输出校验结果并用退出码表示是否通过
依赖关系:
- pathlib
使用场景:
- 修改 skill 入口、references 或 playbooks 后运行，确认结构仍满足 02 号完成计划
注意事项:
- 本脚本只做结构校验，不判断 Markdown 内容质量
- source reports 原文属于本地私有参考材料，公开仓库只要求 source index 和 source id 可校验
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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
    "references/chart-notes/key-framework-charts.md",
    "references/chart-notes/image-url-index.yml",
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


def require_file(relative_path: str) -> bool:
    path = ROOT / relative_path
    if path.is_file():
        print(f"ok: {relative_path}")
        return True
    print(f"missing: {relative_path}")
    return False


def count_markdown(relative_dir: str) -> int:
    return len(list((ROOT / relative_dir).glob("*.md")))


def require_playbooks() -> bool:
    playbook_dir = ROOT / "references" / "playbooks"
    missing = [name for name in REQUIRED_PLAYBOOKS if not (playbook_dir / name).is_file()]
    if missing:
        for name in missing:
            print(f"missing_playbook: {name}")
        return False
    print(f"ok: required_playbooks={len(REQUIRED_PLAYBOOKS)}")
    return True


def main() -> int:
    passed = True

    for relative_path in REQUIRED_FILES:
        passed = require_file(relative_path) and passed

    playbooks_count = count_markdown("references/playbooks")
    if playbooks_count >= len(REQUIRED_PLAYBOOKS):
        print(f"ok: playbooks_count>={len(REQUIRED_PLAYBOOKS)}")
    else:
        print(f"error: playbooks_count={playbooks_count}")
        passed = False

    passed = require_playbooks() and passed

    evidence_cards_count = count_markdown("references/evidence-cards")
    if evidence_cards_count >= 6:
        print("ok: evidence_cards_count>=6")
    else:
        print(f"error: evidence_cards_count={evidence_cards_count}")
        passed = False

    templates_count = count_markdown("assets/templates")
    if templates_count >= 3:
        print("ok: templates_count>=3")
    else:
        print(f"error: templates_count={templates_count}")
        passed = False

    source_reports_count = count_markdown("references/source-reports")
    if source_reports_count == 23:
        print("ok: private_source_reports_count=23")
    else:
        print(f"info: private_source_reports_count={source_reports_count}")
        print("info: source report originals are optional and ignored for public GitHub pushes")

    print("info: run scripts/validate_source_refs.py for source-id validation")
    print(f"validation_passed={str(passed).lower()}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
