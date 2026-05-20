# 05B Framework Conflict And Duplication Audit

## Purpose

Review the full FICC Researcher framework layer after 05A contract standardization, identify conflicts and repeated concepts, and record how 05B resolves or contains them.

## Conflict And Merge Decisions

| Area | Problem | Decision |
| --- | --- | --- |
| Playbook framework style | Some playbooks used causal chains, some additive component models, and `quant-ai` used a generic pipeline. | Add `references/15-playbook-framework-standard.md`; require every playbook to contain `Framework Claims`, `Output Overlay`, and `Claim IDs`. |
| Claim traceability | Playbook claims listed source reports but did not map individual claims to evidence sections. | Add `references/16-source-claim-map.yml` with 17 claims covering all 12 playbooks. |
| Rates vs institution behavior | Fiscal expansion can imply growth support and supply pressure; institution demand can absorb supply and weaken the rate-up implication. | Treat as competing channels. Use `11-research-decision-chains.md` and 15's conflict-resolution standard. |
| Bond strategy vs portfolio policy | `bond-strategy.md` and `06-portfolio-action-policy.md` both discussed actions. | `bond-strategy` owns portfolio reasoning; `06` owns action translation gate, scenario, trigger, loss path, and stop condition. |
| Credit generic vs specialized credit playbooks | `credit-strategy` overlapped with city investment, financial credit, ABS/REITs. | `credit-strategy` is now the generic spread/risk/liquidity layer; specialized instruments route to their own playbook first. |
| Macro indicator vs policy reaction | `07` explains indicator transmission and `08` filters policy response; both could produce direct bond conclusions. | `07` defines indicator meaning; `08` applies policy reaction filter before market transmission. |
| Evidence-card asymmetry | `offshore-derivatives-abs-reits-evidence.md` combined unrelated domains. | Split into `offshore-global-rates-evidence.md`, `derivatives-evidence.md`, and `abs-reits-evidence.md`. |
| Data fields across playbooks | Required inputs use different granularity. | Playbooks keep decision-level inputs; field-level source candidates live in `09` and provider mapping in `12`. |
| Quant/AI genericness | `quant-ai-research.md` could apply to any quant project. | Rewrite it around FICC factor families, PIT availability, release lag, frequency mismatch, entity mapping, stale valuation, liquidity, cost, and human review. |
| Output labels | Some templates and playbooks used custom output skeletons. | 05A established canonical output in `14`; 05B renames playbook templates to `Output Overlay` so they cannot override the canonical contract. |

## Repeated Concepts Kept Separate

- Funding appears in `rates-macro`, `bond-strategy`, `institution-behavior`, and `wealth-management-funds`. It is not merged because each file uses funding at a different layer: short-rate anchor, portfolio leverage, institution constraint, and redemption feedback.
- Policy support appears in `rates-macro`, `credit-strategy`, and `city-investment-bonds`. It is kept separate because macro policy support, credit refinancing support, and issuer guarantee assumptions are different.
- Liquidity appears in almost every playbook. It is kept as a cross-cutting risk concept; exact field requirements belong in `09-data-interface-catalog.md`.

## Fixed In 05B

- 12/12 playbooks now include `Framework Claims`.
- 12/12 playbooks now include `Claim IDs`.
- 12/12 playbooks use `Output Overlay` instead of defining competing output contracts.
- 17 claim ids map to source ids and evidence-card sections.
- Evidence card count becomes 9 with offshore, derivatives, and ABS/REITs split.
- `validate_claim_map.py` verifies claim-source consistency.
- `validate_skill_links.py` now checks required playbook standard sections.

## Remaining Design Limits

- Claim map is playbook-claim level, not source-report paragraph level. This is intentional to avoid copying or over-summarizing copyrighted source reports.
- Some `Required Inputs` sections still use domain-specific group labels rather than a perfectly identical heading set. This is acceptable because exact field requirements are centralized in `09` and provider candidates in `12`.
- 05B does not run full OpenClaw smoke unless requested after local verification.
