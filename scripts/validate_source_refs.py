"""
文件路径: scripts/validate_source_refs.py
文件作用: 校验 playbook 和 evidence card 中引用的 source id 是否存在于源报告索引。
主要内容:
- parse_source_ids: 从 references/01-source-index.yml 提取所有 id
- find_referenced_ids: 扫描 Markdown 中反引号包裹的 cicc-* / huatai-* id
- main: 输出 source id 数量、引用数量、未知引用并返回校验退出码
依赖关系:
- pathlib
- re
使用场景:
- 新增 playbook 或 evidence card 后运行，确认 source report 引用没有拼写漂移
注意事项:
- 本脚本不依赖 PyYAML，只做 source id 引用一致性校验
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX_FILE = ROOT / "references" / "01-source-index.yml"
EXPECTED_SOURCE_COUNT = 25
SCAN_DIRS = [
    ROOT / "references" / "playbooks",
    ROOT / "references" / "evidence-cards",
]


def parse_source_ids() -> set[str]:
    text = INDEX_FILE.read_text(encoding="utf-8")
    return set(re.findall(r"^- id:\s*([a-z0-9-]+)\s*$", text, re.MULTILINE))


def find_referenced_ids() -> set[str]:
    refs: set[str] = set()
    pattern = re.compile(r"`((?:cicc|huatai)-[a-z0-9-]+)`")
    for directory in SCAN_DIRS:
        if not directory.exists():
            continue
        for path in directory.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            refs.update(pattern.findall(text))
    return refs


def main() -> int:
    source_ids = parse_source_ids()
    referenced_ids = find_referenced_ids()
    unknown_ids = sorted(referenced_ids - source_ids)

    print(f"source_ids_count={len(source_ids)}")
    print(f"referenced_source_ids_count={len(referenced_ids)}")
    print(f"unknown_source_ids={len(unknown_ids)}")
    for source_id in unknown_ids:
        print(f"unknown: {source_id}")

    passed = len(source_ids) == EXPECTED_SOURCE_COUNT and not unknown_ids
    print(f"validation_passed={str(passed).lower()}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
