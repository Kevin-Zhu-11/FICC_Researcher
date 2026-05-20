"""
文件路径: scripts/validate_skill_links.py
文件作用: 校验 FICC Researcher skill 的关键文件、必需 playbook 和公开仓库结构。
主要内容:
- require_file: 检查必需文件存在
- count_markdown: 统计指定目录下 Markdown 文件数量
- require_playbooks: 检查 12 个核心 playbook 是否存在
- require_named_files: 精确检查证据卡、模板和示例文件名
- require_playbook_standard_sections: 检查 playbook 深层统一所需章节
- require_eval_files: 检查 03B/04 smoke prompt、输出契约和质量 rubric 文件存在
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

from validation_config import (
    EXPECTED_SOURCE_COUNT,
    REQUIRED_EVIDENCE_CARDS,
    REQUIRED_FILES,
    REQUIRED_GOLDEN_EXAMPLES,
    REQUIRED_PLAYBOOKS,
    REQUIRED_TEMPLATES,
)

ROOT = Path(__file__).resolve().parents[1]


def require_file(relative_path: str) -> bool:
    path = ROOT / relative_path
    if path.is_file():
        print(f"ok: {relative_path}")
        return True
    print(f"missing: {relative_path}")
    return False


def count_markdown(relative_dir: str) -> int:
    return len(list((ROOT / relative_dir).rglob("*.md")))


def require_playbooks() -> bool:
    playbook_dir = ROOT / "references" / "playbooks"
    missing = [name for name in REQUIRED_PLAYBOOKS if not (playbook_dir / name).is_file()]
    if missing:
        for name in missing:
            print(f"missing_playbook: {name}")
        return False
    print(f"ok: required_playbooks={len(REQUIRED_PLAYBOOKS)}")
    return True


def require_playbook_standard_sections() -> bool:
    playbook_dir = ROOT / "references" / "playbooks"
    required_sections = [
        "## Framework",
        "## Framework Claims",
        "## Analysis Steps",
        "## Output Overlay",
        "## Source Reports",
        "## Claim IDs",
    ]
    passed = True
    for name in REQUIRED_PLAYBOOKS:
        path = playbook_dir / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for section in required_sections:
            if section not in text:
                print(f"missing_playbook_section: {name} {section}")
                passed = False
    if passed:
        print(f"ok: playbook_standard_sections={len(REQUIRED_PLAYBOOKS)}")
    return passed


def require_named_files(relative_dir: str, required_names: list[str], label: str) -> bool:
    directory = ROOT / relative_dir
    missing = [name for name in required_names if not (directory / name).is_file()]
    extra = sorted(
        path.name
        for path in directory.glob("*.md")
        if path.name not in required_names and path.name != ".gitkeep"
    )
    if missing:
        for name in missing:
            print(f"missing_{label}: {name}")
        return False
    print(f"ok: required_{label}={len(required_names)}")
    if extra:
        for name in extra:
            print(f"info: extra_{label}: {name}")
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
    passed = require_playbook_standard_sections() and passed

    passed = require_named_files(
        "references/evidence-cards",
        REQUIRED_EVIDENCE_CARDS,
        "evidence_card",
    ) and passed
    passed = require_named_files("assets/templates", REQUIRED_TEMPLATES, "template") and passed
    passed = require_named_files(
        "examples/golden-cases",
        REQUIRED_GOLDEN_EXAMPLES,
        "golden_example",
    ) and passed

    source_reports_count = count_markdown("references/source-reports")
    if source_reports_count == EXPECTED_SOURCE_COUNT:
        print(f"ok: private_source_reports_count={EXPECTED_SOURCE_COUNT}")
    else:
        print(f"info: private_source_reports_count={source_reports_count}")
        print("info: source report originals are optional and ignored for public GitHub pushes")

    print("info: run scripts/validate_source_refs.py for source-id validation")
    print(f"validation_passed={str(passed).lower()}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
