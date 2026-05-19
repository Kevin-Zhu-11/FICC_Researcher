"""
文件路径: scripts/validate_eval_cases.py
文件作用: 校验 FICC Researcher eval prompt 与输出契约文件的结构完整性。
主要内容:
- load_yaml: 读取 YAML，并在本地 .tmp_pyyaml 存在时自动加入路径
- validate_cases: 检查 case id、workflow、prompt、required_files、forbidden
- validate_contracts: 检查 workflow 输出契约
依赖关系:
- pathlib
- sys
- yaml 可选，本仓库可使用 .tmp_pyyaml 作为本地校验依赖
使用场景:
- 修改 evals/*.yml 后运行，确认 smoke prompt 引用文件存在且 workflow 有输出契约
注意事项:
- 本脚本只校验结构，不评判金融分析质量
"""

from __future__ import annotations

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


CASES_PATH = ROOT / "evals" / "smoke-prompts.yml"
CONTRACTS_PATH = ROOT / "evals" / "expected-output-contracts.yml"


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data


def validate_cases(cases_data: dict[str, Any], contracts: dict[str, Any]) -> bool:
    passed = True
    cases = cases_data.get("cases")
    if not isinstance(cases, list) or not cases:
        print("error: cases must be a non-empty list")
        return False

    seen_ids: set[str] = set()
    contract_map = contracts.get("contracts", {})
    if not isinstance(contract_map, dict):
        print("error: contracts must be a mapping")
        return False

    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            print(f"error: case[{index}] must be a mapping")
            passed = False
            continue

        case_id = case.get("id")
        workflow = case.get("workflow")
        prompt = case.get("prompt")
        required_files = case.get("required_files")
        forbidden = case.get("forbidden")

        if not isinstance(case_id, str) or not case_id:
            print(f"error: case[{index}] missing id")
            passed = False
        elif case_id in seen_ids:
            print(f"error: duplicate_case_id={case_id}")
            passed = False
        else:
            seen_ids.add(case_id)

        if not isinstance(workflow, str) or not workflow:
            print(f"error: case[{index}] missing workflow")
            passed = False
        elif workflow not in contract_map:
            print(f"error: case={case_id} workflow_has_no_contract={workflow}")
            passed = False

        if not isinstance(prompt, str) or len(prompt.strip()) < 10:
            print(f"error: case={case_id} prompt_too_short")
            passed = False

        if not isinstance(required_files, list) or not required_files:
            print(f"error: case={case_id} required_files_empty")
            passed = False
        else:
            for relative_path in required_files:
                if not isinstance(relative_path, str):
                    print(f"error: case={case_id} required_file_not_string")
                    passed = False
                    continue
                if not (ROOT / relative_path).is_file():
                    print(f"missing_required_file: case={case_id} path={relative_path}")
                    passed = False

        if not isinstance(forbidden, list) or not forbidden:
            print(f"error: case={case_id} forbidden_empty")
            passed = False

    print(f"ok: eval_cases={len(cases)}")
    return passed


def validate_contracts(contracts_data: dict[str, Any]) -> bool:
    passed = True
    contracts = contracts_data.get("contracts")
    if not isinstance(contracts, dict) or not contracts:
        print("error: contracts must be a non-empty mapping")
        return False

    for workflow, contract in contracts.items():
        if not isinstance(workflow, str) or not workflow:
            print("error: empty_workflow_name")
            passed = False
            continue
        if not isinstance(contract, dict):
            print(f"error: contract_not_mapping={workflow}")
            passed = False
            continue
        required_blocks = contract.get("required_blocks")
        if not isinstance(required_blocks, list) or len(required_blocks) < 3:
            print(f"error: workflow={workflow} required_blocks_too_short")
            passed = False
        elif any(not isinstance(block, str) or not block for block in required_blocks):
            print(f"error: workflow={workflow} invalid_required_block")
            passed = False

    print(f"ok: output_contracts={len(contracts)}")
    return passed


def main() -> int:
    try:
        cases_data = load_yaml(CASES_PATH)
        contracts_data = load_yaml(CONTRACTS_PATH)
    except (FileNotFoundError, ValueError, yaml.YAMLError) as exc:
        print(f"error: {exc}")
        return 1

    passed = validate_contracts(contracts_data)
    passed = validate_cases(cases_data, contracts_data) and passed
    print(f"eval_validation_passed={str(passed).lower()}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
