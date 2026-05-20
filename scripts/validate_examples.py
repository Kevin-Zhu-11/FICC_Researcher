"""
文件路径: scripts/validate_examples.py
文件作用: 校验 FICC Researcher golden examples 和样例 data packet 的结构与敏感信息边界。
主要内容:
- validate_markdown_examples: 检查 golden-case Markdown 必需章节
- validate_data_packets: 检查 examples/data YAML 必需字段
- scan_secret_patterns: 扫描真实凭证赋值、API key 赋值、密码赋值和 OpenAI-style key
- main: 输出校验结果并用退出码表示是否通过
依赖关系:
- pathlib
- re
- sys
- yaml 可选，本仓库可使用 .tmp_pyyaml 作为本地校验依赖
使用场景:
- 新增或修改 examples/ 后运行，确认样例可被 agent 安全学习
注意事项:
- 本脚本只校验结构和敏感信息模式，不判断金融结论质量
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
TMP_PYYAML = ROOT / ".tmp_pyyaml"
if TMP_PYYAML.is_dir():
    sys.path.insert(0, str(TMP_PYYAML))


try:
    import yaml
except ImportError:  # pragma: no cover - depends on local environment
    print("missing_dependency: pyyaml")
    sys.exit(1)


GOLDEN_DIR = ROOT / "examples" / "golden-cases"
DATA_DIR = ROOT / "examples" / "data"
REQUIRED_MARKDOWN_HEADINGS = ["## Prompt", "## Expected Answer Shape"]
REQUIRED_DATA_FIELDS = [
    "source",
    "provider",
    "interface_or_file",
    "query",
    "as_of",
    "retrieved_at",
    "fields",
    "row_count",
    "limitations",
]
SECRET_PATTERN = re.compile(
    r"(?i)(token|api[_-]?key|password|secret)\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{16,}|sk-[A-Za-z0-9]{20,}"
)


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data


def validate_markdown_examples() -> bool:
    passed = True
    if not GOLDEN_DIR.is_dir():
        print("error: examples/golden-cases missing")
        return False

    markdown_files = sorted(GOLDEN_DIR.glob("*.md"))
    if not markdown_files:
        print("error: no golden-case markdown files")
        return False

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT).as_posix()
        for heading in REQUIRED_MARKDOWN_HEADINGS:
            if heading not in text:
                print(f"error: {relative} missing_heading={heading}")
                passed = False
        if "## What Would Fail" not in text and "## Forbidden Claims" not in text:
            print(f"error: {relative} missing_failure_section")
            passed = False
        if "token" in text.lower() and SECRET_PATTERN.search(text):
            print(f"error: {relative} contains_secret_like_assignment")
            passed = False

    print(f"ok: golden_examples={len(markdown_files)}")
    return passed


def validate_data_packets() -> bool:
    passed = True
    if not DATA_DIR.is_dir():
        print("error: examples/data missing")
        return False

    data_files = sorted(DATA_DIR.glob("*.yml")) + sorted(DATA_DIR.glob("*.yaml"))
    if not data_files:
        print("error: no example data packet files")
        return False

    for path in data_files:
        relative = path.relative_to(ROOT).as_posix()
        try:
            data = load_yaml(path)
        except (ValueError, yaml.YAMLError) as exc:
            print(f"error: {relative} {exc}")
            passed = False
            continue

        for field in REQUIRED_DATA_FIELDS:
            if field not in data:
                print(f"error: {relative} missing_field={field}")
                passed = False

        fields = data.get("fields")
        row_count = data.get("row_count")
        limitations = data.get("limitations")
        if not isinstance(fields, list) or not fields:
            print(f"error: {relative} fields_empty")
            passed = False
        if not isinstance(row_count, int) or row_count < 0:
            print(f"error: {relative} invalid_row_count")
            passed = False
        if not isinstance(limitations, list) or not limitations:
            print(f"error: {relative} limitations_empty")
            passed = False

    print(f"ok: example_data_packets={len(data_files)}")
    return passed


def scan_secret_patterns() -> bool:
    passed = True
    files = list(GOLDEN_DIR.glob("*.md")) + list(DATA_DIR.glob("*.yml")) + list(DATA_DIR.glob("*.yaml"))
    for path in files:
        text = path.read_text(encoding="utf-8")
        match = SECRET_PATTERN.search(text)
        if match:
            relative = path.relative_to(ROOT).as_posix()
            print(f"error: secret_like_pattern file={relative} match={match.group(0)}")
            passed = False
    if passed:
        print("ok: examples_secret_scan_clean")
    return passed


def main() -> int:
    passed = validate_markdown_examples()
    passed = validate_data_packets() and passed
    passed = scan_secret_patterns() and passed
    print(f"examples_validation_passed={str(passed).lower()}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
