"""
文件路径: scripts/validate_quality_rubrics.py
文件作用: 校验 FICC Researcher 质量评分 rubric 的结构完整性。
主要内容:
- load_yaml: 读取 YAML，并在本地 .tmp_pyyaml 存在时自动加入路径
- validate_rubrics: 检查 hard_gates、scoring、minimum_total_score
- validate_case_links: 检查 smoke case 的 rubric 引用
- main: 输出校验结果并用退出码表示是否通过
依赖关系:
- pathlib
- sys
- yaml 可选，本仓库可使用 .tmp_pyyaml 作为本地校验依赖
使用场景:
- 修改 evals/quality-rubrics.yml 或 evals/*.yml 后运行
注意事项:
- 本脚本只校验 rubric 结构，不判断金融结论质量
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


RUBRICS_PATH = ROOT / "evals" / "quality-rubrics.yml"
CONTRACTS_PATH = ROOT / "evals" / "expected-output-contracts.yml"
CASES_PATH = ROOT / "evals" / "smoke-prompts.yml"


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data


def validate_rubrics(rubrics_data: dict[str, Any], contracts_data: dict[str, Any]) -> bool:
    passed = True
    rubrics = rubrics_data.get("rubrics")
    contracts = contracts_data.get("contracts")
    if not isinstance(rubrics, dict) or not rubrics:
        print("error: rubrics must be a non-empty mapping")
        return False
    if not isinstance(contracts, dict) or not contracts:
        print("error: contracts must be a non-empty mapping")
        return False

    missing_rubrics = sorted(set(contracts) - set(rubrics))
    extra_rubrics = sorted(set(rubrics) - set(contracts))
    for workflow in missing_rubrics:
        print(f"missing_rubric_for_contract={workflow}")
        passed = False
    for workflow in extra_rubrics:
        print(f"warning: rubric_without_contract={workflow}")

    for workflow, rubric in rubrics.items():
        if not isinstance(workflow, str) or not workflow:
            print("error: empty_rubric_workflow")
            passed = False
            continue
        if not isinstance(rubric, dict):
            print(f"error: rubric_not_mapping={workflow}")
            passed = False
            continue

        hard_gates = rubric.get("hard_gates")
        scoring = rubric.get("scoring")
        minimum_total_score = rubric.get("minimum_total_score")

        if not isinstance(hard_gates, list) or len(hard_gates) < 2:
            print(f"error: workflow={workflow} hard_gates_too_short")
            passed = False
        elif any(not isinstance(gate, str) or not gate for gate in hard_gates):
            print(f"error: workflow={workflow} invalid_hard_gate")
            passed = False

        if not isinstance(scoring, dict) or not scoring:
            print(f"error: workflow={workflow} scoring_empty")
            passed = False
        else:
            total_score = 0
            for dimension, config in scoring.items():
                if not isinstance(dimension, str) or not dimension:
                    print(f"error: workflow={workflow} empty_scoring_dimension")
                    passed = False
                    continue
                if not isinstance(config, dict):
                    print(f"error: workflow={workflow} dimension={dimension} config_not_mapping")
                    passed = False
                    continue
                max_score = config.get("max_score")
                pass_threshold = config.get("pass_threshold")
                if not isinstance(max_score, int) or max_score <= 0:
                    print(f"error: workflow={workflow} dimension={dimension} invalid_max_score")
                    passed = False
                    continue
                if not isinstance(pass_threshold, int) or pass_threshold < 0:
                    print(f"error: workflow={workflow} dimension={dimension} invalid_pass_threshold")
                    passed = False
                    continue
                if pass_threshold > max_score:
                    print(f"error: workflow={workflow} dimension={dimension} threshold_gt_max")
                    passed = False
                total_score += max_score

            if isinstance(minimum_total_score, int) and minimum_total_score > total_score:
                print(f"error: workflow={workflow} minimum_total_score_gt_total")
                passed = False

        if not isinstance(minimum_total_score, int) or minimum_total_score <= 0:
            print(f"error: workflow={workflow} invalid_minimum_total_score")
            passed = False

    print(f"ok: quality_rubrics={len(rubrics)}")
    return passed


def validate_case_links(cases_data: dict[str, Any], rubrics_data: dict[str, Any]) -> bool:
    passed = True
    cases = cases_data.get("cases")
    rubrics = rubrics_data.get("rubrics", {})
    if not isinstance(cases, list) or not cases:
        print("error: cases must be a non-empty list")
        return False
    if not isinstance(rubrics, dict):
        print("error: rubrics must be a mapping")
        return False

    for case in cases:
        if not isinstance(case, dict):
            print("error: case_not_mapping")
            passed = False
            continue
        case_id = case.get("id", "unknown")
        rubric = case.get("rubric")
        if not isinstance(rubric, str) or not rubric:
            print(f"error: case={case_id} missing_rubric")
            passed = False
        elif rubric not in rubrics:
            print(f"error: case={case_id} unknown_rubric={rubric}")
            passed = False

    print(f"ok: rubric_case_links={len(cases)}")
    return passed


def main() -> int:
    try:
        rubrics_data = load_yaml(RUBRICS_PATH)
        contracts_data = load_yaml(CONTRACTS_PATH)
        cases_data = load_yaml(CASES_PATH)
    except (FileNotFoundError, ValueError, yaml.YAMLError) as exc:
        print(f"error: {exc}")
        return 1

    passed = validate_rubrics(rubrics_data, contracts_data)
    passed = validate_case_links(cases_data, rubrics_data) and passed
    print(f"quality_rubrics_validation_passed={str(passed).lower()}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
