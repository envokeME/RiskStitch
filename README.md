# RiskStitch

![RiskStitch — open GRC pattern library](assets/riskstitch-social.png)

[![validate](https://github.com/envokeME/riskstitch/actions/workflows/validate.yml/badge.svg)](https://github.com/envokeME/riskstitch/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-2f855a.svg)](LICENSE)
[![Patterns: 28](https://img.shields.io/badge/patterns-28-2563eb.svg)](catalog.json)
[![Status: Experimental](https://img.shields.io/badge/status-experimental-f59e0b.svg)](docs/safety-model.md)

**Open, evidence-disciplined AI patterns for governance, risk, and compliance work.**

RiskStitch converts raw GRC inputs—scanner findings, policies, evidence, audit notes, risk narratives, vendor documents, regulatory changes, and AI use cases—into structured drafts that a practitioner can inspect, challenge, and approve.

It is inspired by [Fabric](https://github.com/danielmiessler/Fabric) and uses Fabric's `system.md` pattern format. RiskStitch is an independent project and is not affiliated with or endorsed by Fabric.

> Status: **EXPERIMENTAL.** The patterns are operational drafts with structural tests. They are not certified by NIST, ISO, AICPA, The Open Group, FIRST, CISA, regulators, or standards bodies.

## Start here

You do not need to be a GRC specialist or a Fabric user to understand the project.

- **New to GRC?** Read the [plain-English GRC field guide](docs/grc-primer.md). It explains risk, controls, evidence, compliance, and audit through one worked example.
- **Ready to try one pattern?** Start with [`grc_normalize_risk_signal`](patterns/grc_normalize_risk_signal/system.md) and its [worked example](examples/normalize-risk-signal/).
- **Already use Fabric?** Go directly to [Quick start with Fabric](#quick-start-with-fabric).
- **Reviewing the engineering?** Read the [architecture](docs/architecture.md), [safety model](docs/safety-model.md), and [model-testing protocol](docs/model-testing.md).

## Why this exists

Generic prompts produce polished text without a defensible chain from evidence to conclusion. GRC work requires the opposite:

`Signal → Context → Measure → Treat → Validate`

Every RiskStitch pattern applies the same evidence contract:

- distinguish facts, source-derived statements, inferences, assumptions, and unknowns;
- cite evidence locations from the supplied input;
- refuse to invent controls, citations, scores, owners, dates, or legal conclusions;
- expose missing information and decision dependencies;
- reserve risk acceptance, audit opinions, compliance claims, and legal judgments for authorized humans.

## More than a list of prompts

GRC prompt libraries already exist, and some contain more prompts than RiskStitch. RiskStitch focuses on a different unit of value: a governed pattern that can be installed, inspected, generated, tested, versioned, and reviewed.

| Typical prompt collection | RiskStitch |
|---|---|
| Copy-and-paste text | Standalone prompts plus Fabric-compatible `system.md` patterns |
| Instructions authored independently | Shared evidence contract generated into every pattern |
| Output quality judged by appearance | Evidence states, source locators, unknowns, and human-review gates |
| Files are the source of truth | Structured specifications generate runnable files deterministically |
| Informal examples | Sanitized inputs, expected outputs, schemas, and repository tests |
| Model produces a deliverable | Model produces a reviewable draft; accountable humans retain decisions |

This does not make model output correct. It makes the expected behavior, evidence boundary, and review responsibility easier to see and test.

See [related public projects and scope](docs/related-projects.md) for an honest view of adjacent work and RiskStitch's intended contribution.

## What is included

| Domain | Patterns | Representative work |
|---|---:|---|
| Risk | 8 | Normalize signals, write risk statements, build scenarios, prioritize findings, FAIR-style quantification, closure validation, KRIs, challenge narratives |
| Controls | 5 | Design controls, test design and operating effectiveness, evaluate evidence, map controls to evidence |
| Third-party risk | 4 | Vendor tiering, SOC report review, vendor security assessment, TPRM risk drafting |
| Audit and compliance | 5 | Requirement mapping, gap assessment, audit findings, management responses, regulatory change analysis |
| AI governance and privacy | 3 | AI inventory, AI risk assessment, privacy impact screening |
| Resilience | 2 | Business impact analysis, incident lessons |
| Executive communication | 1 | Translate technical risk into business decision language |

The complete machine-readable inventory is in [`catalog.json`](catalog.json).

## Quick start with Fabric

Install [Fabric](https://github.com/danielmiessler/Fabric), configure a custom patterns directory with `fabric --setup`, then copy RiskStitch patterns into that directory:

```bash
git clone https://github.com/envokeME/riskstitch.git
cd riskstitch
./scripts/install.sh /path/to/your/fabric-custom-patterns
```

Run a pattern against a file or piped input:

```bash
cat examples/normalize-risk-signal/input.md \
  | fabric --pattern grc_normalize_risk_signal
```

```bash
cat vendor-soc-notes.txt \
  | fabric --pattern grc_review_soc_report
```

The installer does not create accounts, configure providers, request API keys, or overwrite an existing pattern unless `--force` is supplied.

## Use without Fabric

Each folder under [`patterns/`](patterns/) contains a standalone `system.md`. Paste that system prompt into an AI tool, then provide the source material as the user input. Model behavior and data handling depend on the selected tool and provider.

## Three useful starting points

### 1. Normalize mixed security findings

`grc_normalize_risk_signal` separates observed facts from enrichment and decision data. It produces a stable record suitable for downstream deduplication and prioritization.

Input:

```text
Wiz reports a public storage bucket. Asset owner unknown. CVSS 9.1.
The issue was seen last month, but no current exposure test is attached.
```

Output structure:

```text
Signal record → Evidence ledger → Data quality → Correlation keys → Required enrichment → Routing recommendation
```

### 2. Test evidence instead of summarizing it

`grc_assess_evidence_quality` evaluates relevance, reliability, period coverage, population completeness, provenance, and contradictions. Missing evidence remains missing.

### 3. Quantify risk without false precision

`grc_quantify_risk_fair` creates frequency and magnitude ranges, records the basis for every estimate, runs arithmetic only when inputs support it, and separates model output from the final business decision.

Worked inputs and illustrative outputs are in [`examples/`](examples/).

## The core idea in one example

Suppose a scanner reports a public cloud storage bucket with a severity score of 9.1.

A generic prompt may jump to: “Critical risk. Remediate immediately.” RiskStitch first separates what is known from what is merely suggested:

| Question | Example treatment |
|---|---|
| What was observed? | The scanner reported a public bucket and a 9.1 score. |
| What is only source-derived? | The scanner's classification and score are claims from that source until verified. |
| What is unknown? | Current exposure, data sensitivity, business owner, exploit path, and compensating controls. |
| What can be inferred? | Public exposure may increase likelihood, but organizational risk cannot be established from the score alone. |
| Who decides? | An authorized risk owner decides treatment or acceptance after evidence review. |

That separation is the difference between polished text and a defensible draft. The [GRC field guide](docs/grc-primer.md) walks through the full chain.

## Pattern anatomy

Every generated pattern contains:

1. identity and bounded purpose;
2. non-negotiable GRC evidence rules;
3. required input fields;
4. a domain-specific method;
5. an explicit output contract;
6. special safety and quality rules;
7. a human-review gate.

Pattern specifications live in [`specs/patterns.json`](specs/patterns.json). The runnable `system.md` files are deterministically generated by [`tools/render_patterns.py`](tools/render_patterns.py), so changes are reviewable and drift is testable.

## Validate the repository

RiskStitch uses only the Python standard library for validation.

```bash
make validate
```

Validation checks:

- catalog and pattern count;
- deterministic rendering;
- required evidence and review sections;
- unique names and valid slugs;
- JSON schema syntax;
- example coverage;
- unsafe or unsubstantiated compliance claims.

Structural validation does not prove prompt quality. See [`docs/model-testing.md`](docs/model-testing.md) for the human evaluation protocol.

## Safety model

Do not submit secrets, credentials, regulated data, confidential client material, or unnecessary personal information to a model. Use approved enterprise tooling and data-handling rules.

RiskStitch does not:

- determine legal or regulatory applicability;
- certify compliance;
- issue an audit opinion;
- accept risk on behalf of an organization;
- replace qualified privacy, legal, security, audit, finance, or safety professionals;
- guarantee correctness, completeness, or current framework interpretation.

Read [`docs/safety-model.md`](docs/safety-model.md) before operational use.

## Reference foundations

Patterns use general concepts drawn from public primary sources without reproducing copyrighted standards text:

- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework)
- [NIST risk management publications](https://csrc.nist.gov/projects/risk-management)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [NIST Privacy Framework](https://www.nist.gov/privacy-framework)
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [FIRST CVSS v4.0](https://www.first.org/cvss/v4.0/)
- [FIRST EPSS](https://www.first.org/epss/)
- [Open FAIR](https://www.opengroup.org/openfair)

Framework and regulatory references must be verified against the authoritative current source for the relevant date and jurisdiction.

## Contributing

Contributions must include a bounded purpose, input contract, method, output contract, evidence rules, human-review gate, and at least one evaluation case. Do not submit proprietary framework text, client material, secrets, or content copied from private assessments.

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/pattern-authoring-standard.md`](docs/pattern-authoring-standard.md).

## License and attribution

RiskStitch is released under the [MIT License](LICENSE). Fabric is a separate MIT-licensed project. RiskStitch patterns are newly authored for this repository; no upstream Fabric patterns are vendored.
