"""
文件路径: scripts/validate_claim_map.py
文件作用: 校验 FICC Researcher 的 playbook claim 到 evidence/source 的映射是否完整一致。
主要内容:
- load_yaml: 读取 references/16-source-claim-map.yml
- parse_source_ids: 从 references/01-source-index.yml 提取 source id
- validate_claims: 检查 claim_id、playbook、evidence_card、source_ids、decision_chain
依赖关系:
- pathlib
- re
- yaml，可使用仓库本地 .tmp_pyyaml
使用场景:
- 新增或修改 playbook 框架 claim、evidence card 或 source report id 后运行
注意事项:
- 本脚本只校验结构和引用一致性，不判断金融研究结论正确性
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

from validation_config import REQUIRED_PLAYBOOKS


ROOT = Path(__file__).resolve().parents[1]
TMP_PYYAML = ROOT / ".tmp_pyyaml"
if TMP_PYYAML.is_dir():
    sys.path.insert(0, str(TMP_PYYAML))

try:
    import yaml
except ImportError:  # pragma: no cover - depends on local environment
    print("missing_dependency: pyyaml")
    sys.exit(1)


CLAIM_MAP_PATH = ROOT / "references" / "16-source-claim-map.yml"
SOURCE_INDEX_PATH = ROOT / "references" / "01-source-index.yml"
EVIDENCE_DIR = ROOT / "references" / "evidence-cards"
CLAIM_ID_PATTERN = re.compile(r"^[A-Z]{2,4}-\d{2}$")


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping")
    return data


def parse_source_ids() -> set[str]:
    text = SOURCE_INDEX_PATH.read_text(encoding="utf-8")
    return set(re.findall(r"^- id:\s*([a-z0-9-]+)\s*$", text, re.MULTILINE))


def validate_claims(data: dict[str, Any], source_ids: set[str]) -> bool:
    passed = True
    claims = data.get("claims")
    if not isinstance(claims, list) or not claims:
        print("error: claims must be a non-empty list")
        return False

    seen_claim_ids: set[str] = set()
    covered_playbooks: set[str] = set()
    required_playbook_stems = {Path(name).stem for name in REQUIRED_PLAYBOOKS}

    for index, claim in enumerate(claims, start=1):
        if not isinstance(claim, dict):
            print(f"error: claim[{index}] must be a mapping")
            passed = False
            continue

        claim_id = claim.get("claim_id")
        playbook = claim.get("playbook")
        evidence_card = claim.get("evidence_card")
        evidence_section = claim.get("evidence_section")
        claim_text = claim.get("claim")
        mapped_source_ids = claim.get("source_ids")
        decision_chain = claim.get("decision_chain")

        if not isinstance(claim_id, str) or not CLAIM_ID_PATTERN.match(claim_id):
            print(f"error: claim[{index}] invalid_claim_id={claim_id}")
            passed = False
        elif claim_id in seen_claim_ids:
            print(f"error: duplicate_claim_id={claim_id}")
            passed = False
        else:
            seen_claim_ids.add(claim_id)

        if not isinstance(playbook, str) or playbook not in required_playbook_stems:
            print(f"error: claim={claim_id} invalid_playbook={playbook}")
            passed = False
        else:
            covered_playbooks.add(playbook)

        if not isinstance(claim_text, str) or len(claim_text.strip()) < 20:
            print(f"error: claim={claim_id} claim_text_too_short")
            passed = False

        if not isinstance(evidence_card, str) or not (EVIDENCE_DIR / evidence_card).is_file():
            print(f"error: claim={claim_id} missing_evidence_card={evidence_card}")
            passed = False

        if not isinstance(evidence_section, str) or len(evidence_section.strip()) < 3:
            print(f"error: claim={claim_id} invalid_evidence_section")
            passed = False

        if not isinstance(mapped_source_ids, list) or not mapped_source_ids:
            print(f"error: claim={claim_id} source_ids_empty")
            passed = False
        else:
            for source_id in mapped_source_ids:
                if not isinstance(source_id, str) or source_id not in source_ids:
                    print(f"error: claim={claim_id} unknown_source_id={source_id}")
                    passed = False

        if not isinstance(decision_chain, str) or len(decision_chain.strip()) < 3:
            print(f"error: claim={claim_id} invalid_decision_chain")
            passed = False

    missing_playbooks = sorted(required_playbook_stems - covered_playbooks)
    for playbook in missing_playbooks:
        print(f"error: playbook_without_claim={playbook}")
        passed = False

    print(f"ok: claims={len(claims)}")
    print(f"ok: covered_playbooks={len(covered_playbooks)}")
    return passed


def main() -> int:
    try:
        data = load_yaml(CLAIM_MAP_PATH)
        source_ids = parse_source_ids()
    except (FileNotFoundError, ValueError, yaml.YAMLError) as exc:
        print(f"error: {exc}")
        return 1

    passed = validate_claims(data, source_ids)
    print(f"claim_map_validation_passed={str(passed).lower()}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
