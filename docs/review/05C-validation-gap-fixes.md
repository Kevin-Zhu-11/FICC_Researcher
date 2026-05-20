# 05C Validation Gap Fixes

## Purpose

Close the remaining cross-file validation gaps found after the 05A and 05B refactors.

## Fixed Issues

### 1. Workflow entrypoint eval case links

`references/10-workflow-entrypoints.md` now references existing smoke cases:

- `portfolio-action-review` -> `funding-leverage`
- `policy-event-commentary` -> `overseas-rates-linkage`
- `data-assisted-analysis` -> `user-data-minimal-table`

The third item was found during live verification: the entrypoint already named `user-data-minimal-table`, but the smoke file did not define it. A focused smoke case was added instead of pointing the workflow to a less representative ABS or anti-hallucination case.

### 2. Cross-file eval validation

`scripts/validate_eval_cases.py` now checks:

- every workflow in `evals/expected-output-contracts.yml` has an `Eval case:` entry in `references/10-workflow-entrypoints.md`;
- every entrypoint `Eval case:` id exists in `evals/smoke-prompts.yml`;
- every entrypoint case belongs to the same workflow declared by the entrypoint.

This closes the gap where each file could validate independently while the cross-file ID link was broken.

### 3. Portfolio policy source report references

`scripts/validate_source_refs.py` already scans reference Markdown files, including policy files. The script now prints the scanned Markdown file count, and `references/06-portfolio-action-policy.md` explicitly states that its source ids are covered by this validator.

## Validation Snapshot

```text
build_source_index.py:
source_reports_present=yes
source_reports_count=25
indexed_reports_count=25
missing_files=0
unindexed_files=0

validate_eval_cases.py:
ok: canonical_required_blocks=11
ok: output_contracts=9
ok: eval_cases=15
ok: workflow_entrypoint_eval_links=9
eval_validation_passed=true

validate_source_refs.py:
source_ids_count=25
scanned_markdown_files=37
referenced_source_ids_count=25
unknown_source_ids=0
validation_passed=true

validate_claim_map.py:
ok: claims=17
ok: covered_playbooks=12
claim_map_validation_passed=true

validate_skill_links.py:
validation_passed=true

validate_quality_rubrics.py:
ok: quality_rubrics=9
ok: rubric_case_links=15
quality_rubrics_validation_passed=true

validate_examples.py:
ok: golden_examples=2
ok: example_data_packets=1
ok: examples_secret_scan_clean
examples_validation_passed=true

skill-creator quick_validate.py:
Skill is valid!
```

## Status

审查结论：
- 通过，7 个项目验证脚本全部通过，skill-creator quick validation 通过。
