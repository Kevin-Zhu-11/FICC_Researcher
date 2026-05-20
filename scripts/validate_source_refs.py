"""
文件路径: scripts/validate_source_refs.py
文件作用: 校验 references Markdown 中引用的 source id 是否存在于源报告索引。
主要内容:
- parse_source_ids: 从 references/01-source-index.yml 提取所有 id
- iter_scan_files: 扫描 references/**/*.md，排除未入库的 source-reports 原始资料
- find_referenced_ids: 扫描 Markdown 中反引号包裹的 source-like id，支持未来新增机构前缀
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

from validation_config import EXPECTED_SOURCE_COUNT

ROOT = Path(__file__).resolve().parents[1]
INDEX_FILE = ROOT / "references" / "01-source-index.yml"
REFERENCES_DIR = ROOT / "references"
BACKTICK_TOKEN_PATTERN = re.compile(r"`([a-z][a-z0-9]*(?:-[a-z0-9]+){2,})`")
YEAR_SUFFIX_PATTERN = re.compile(r"-20\d{2}$")


def parse_source_ids() -> set[str]:
    text = INDEX_FILE.read_text(encoding="utf-8")
    return set(re.findall(r"^- id:\s*([a-z0-9-]+)\s*$", text, re.MULTILINE))


def iter_scan_files() -> list[Path]:
    if not REFERENCES_DIR.exists():
        return []
    return [
        path
        for path in REFERENCES_DIR.rglob("*.md")
        if "source-reports" not in path.relative_to(REFERENCES_DIR).parts
    ]


def find_referenced_ids(source_ids: set[str], scan_files: list[Path]) -> set[str]:
    refs: set[str] = set()
    for path in scan_files:
        text = path.read_text(encoding="utf-8")
        for token in BACKTICK_TOKEN_PATTERN.findall(text):
            if token in source_ids or YEAR_SUFFIX_PATTERN.search(token):
                refs.add(token)
    return refs


def main() -> int:
    source_ids = parse_source_ids()
    scan_files = iter_scan_files()
    referenced_ids = find_referenced_ids(source_ids, scan_files)
    unknown_ids = sorted(referenced_ids - source_ids)

    print(f"source_ids_count={len(source_ids)}")
    print(f"scanned_markdown_files={len(scan_files)}")
    print(f"referenced_source_ids_count={len(referenced_ids)}")
    print(f"unknown_source_ids={len(unknown_ids)}")
    for source_id in unknown_ids:
        print(f"unknown: {source_id}")

    passed = len(source_ids) == EXPECTED_SOURCE_COUNT and not unknown_ids
    print(f"validation_passed={str(passed).lower()}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
