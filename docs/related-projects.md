# Related public projects and scope

RiskStitch is not the first public collection of AI prompts for GRC. This page documents related work so users can choose the right tool and contributors can avoid reinventing useful ideas.

Checked: 2026-08-28. Repository contents can change after this date.

## Related projects

| Project | Public scope | Where it overlaps |
|---|---|---|
| [Fabric](https://github.com/danielmiessler/Fabric) | General-purpose framework and library of reusable AI patterns | RiskStitch follows Fabric's `system.md` pattern convention and can be installed into a Fabric custom-pattern directory. |
| [GRC-Prompts-Library](https://github.com/KunalCyber/GRC-Prompts-Library) | 45 prompts across 13 GRC, security, career, and implementation domains, with an Excel workbook | Broad GRC task coverage, structured prompt instructions, decision guidance, and copy-and-paste use across multiple models. |
| [prompts-sec-comp](https://github.com/RiskResponse/prompts-sec-comp) | Focused security-compliance materials for SOC 2 system descriptions and incident reports, including YAML input and checklists | Structured inputs, guardrails, examples, and detailed practitioner guidance for a small number of deep use cases. |
| [Internal Audit AI Prompt Library](https://github.com/Jules04711/internal_audit_ai_prompt_library) | 44 prompts organized around the internal-audit lifecycle, distributed through a workbook and training manual | Planning, fieldwork, reporting, follow-up, and standards-aware audit assistance. |
| [Audit-and-compliance-prompt-library](https://github.com/kathrynmcgilvrayeles/Audit-and-compliance-prompt-library) | Audit and compliance prompt collection | Audit and compliance task assistance. |

Inclusion here is descriptive, not an endorsement, certification, quality ranking, or claim of compatibility.

## RiskStitch's intended contribution

The project is deliberately narrower in claim and stronger in engineering discipline:

1. **Fabric-compatible execution.** Each runnable pattern is a standalone `system.md` file.
2. **One shared evidence contract.** Patterns label facts, source-derived claims, inferences, assumptions, and unknowns.
3. **Human decision boundaries.** Protected decisions remain with named, accountable human roles.
4. **Specifications before generated files.** Structured pattern definitions are the source of truth; a deterministic renderer creates the runnable library and catalog.
5. **Testable repository behavior.** Validation checks structure, safety language, paths, schemas, and generated-file drift.
6. **Evaluation transparency.** Worked examples and a model-testing protocol distinguish repository consistency from actual model quality.
7. **Workflow-oriented outputs.** Patterns produce evidence ledgers, missing-data gates, and reviewable sections rather than only polished narrative.

These features do not prove that RiskStitch is better for every use case. A focused prompt, workbook, or training manual may be more useful for a particular practitioner. RiskStitch is aimed at teams that want GRC prompts to behave more like versioned control artifacts than informal snippets.

## Positioning boundary

Use this description:

> RiskStitch is an open, evidence-disciplined, Fabric-compatible GRC pattern system for producing traceable drafts that humans review and approve.

Do not describe RiskStitch as the first GRC prompt library, the only comprehensive GRC AI project, a compliance engine, an automated auditor, or a certified implementation of any framework.

## Suggest a related project

Open an issue or pull request with:

- the public repository URL;
- a factual one-sentence scope description;
- the specific overlap with RiskStitch;
- any relationship or conflict of interest.

Keep comparisons respectful, verifiable, and limited to public project artifacts.
