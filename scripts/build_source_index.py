"""
文件路径: scripts/build_source_index.py
文件作用: 校验 FICC Researcher 源报告索引与可选本地 Markdown 源报告是否一致。
主要内容:
- scan_source_reports: 递归扫描 references/source-reports 下的 Markdown 文件
- parse_index_source_files: 从 references/01-source-index.yml 提取 source_file 字段
- main: 输出数量、缺失文件和未索引文件，并用退出码标记校验结果
依赖关系:
- pathlib
- re
使用场景:
- 新增或移动研报 Markdown 后运行，确认 source index 没有漂移
注意事项:
- 本脚本不依赖 PyYAML，避免为了校验索引引入额外依赖
- 公开仓库不跟踪研报原文；缺少 source-reports 原文时只校验索引条目数量
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from validation_config import EXPECTED_SOURCE_COUNT

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "references" / "source-reports"
INDEX_FILE = ROOT / "references" / "01-source-index.yml"


def to_repo_path(path: Path) -> str:
    """Return a forward-slash path relative to the skill root."""
    return path.relative_to(ROOT).as_posix()


def scan_source_reports() -> set[str]:
    return {to_repo_path(path) for path in SOURCE_DIR.rglob("*.md")}


def parse_index_source_files() -> list[str]:
    text = INDEX_FILE.read_text(encoding="utf-8")
    files: list[str] = []
    for match in re.finditer(r"^\s*source_file:\s*(.+?)\s*$", text, re.MULTILINE):
        value = match.group(1).strip().strip('"').strip("'")
        files.append(value)
    return files


def count_index_entries() -> int:
    text = INDEX_FILE.read_text(encoding="utf-8")
    return len(re.findall(r"^- id:\s+", text, re.MULTILINE))


def validate_index_only(entry_count: int) -> int:
    print("source_reports_present=no")
    print(f"indexed_reports_count={entry_count}")
    if entry_count != EXPECTED_SOURCE_COUNT:
        print(f"error: expected indexed_reports_count={EXPECTED_SOURCE_COUNT}")
        return 1
    print("info: source report originals are optional and ignored for public GitHub pushes")
    return 0


def main() -> int:
    if not INDEX_FILE.exists():
        print(f"missing_index_file={INDEX_FILE}")
        return 1

    entry_count = count_index_entries()
    indexed_files = set(parse_index_source_files())
    if not SOURCE_DIR.exists():
        return validate_index_only(entry_count)

    source_reports = scan_source_reports()
    if not source_reports:
        return validate_index_only(entry_count)

    missing_files = sorted(indexed_files - source_reports)
    unindexed_files = sorted(source_reports - indexed_files)

    print("source_reports_present=yes")
    print(f"source_reports_count={len(source_reports)}")
    print(f"indexed_reports_count={entry_count}")
    print(f"missing_files={len(missing_files)}")
    print(f"unindexed_files={len(unindexed_files)}")

    for path in missing_files:
        print(f"missing: {path}")
    for path in unindexed_files:
        print(f"unindexed: {path}")

    if len(source_reports) != EXPECTED_SOURCE_COUNT:
        print(f"error: expected source_reports_count={EXPECTED_SOURCE_COUNT}")
        return 1
    if entry_count != EXPECTED_SOURCE_COUNT:
        print(f"error: expected indexed_reports_count={EXPECTED_SOURCE_COUNT}")
        return 1
    if missing_files or unindexed_files:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
