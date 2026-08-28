# RiskStitch v0.1.0 launch evaluation

This record separates repository evidence from model-quality claims. All 28 patterns ship in v0.1.0; nine are identified only as the recommended starting set for onboarding and focused evaluation.

## Status

- Release: `0.1.0`
- Pattern status: `EXPERIMENTAL`
- Repository patterns: 28
- Patterns shipped: 28
- Recommended starting patterns: 9
- Worked examples: 3
- Structural validation: implemented
- Provider-neutral behavioral validation: not completed
- Autonomous decision use: prohibited

“Recommended starting pattern” is an onboarding label. It does not mean the other 19 patterns are excluded, or that any pattern is validated, certified, or safe for unsupervised use.

## Why evaluate these nine first

All 28 patterns are included in the launch. These nine provide a compact cross-domain evaluation slice because they cover the recurring chain from raw signal to accountable decision while spanning risk, controls, third-party risk, quantitative analysis, and executive communication.

| Pattern | Bounded practitioner task | Current evidence | Main failure to test |
|---|---|---|---|
| `grc_normalize_risk_signal` | Normalize inconsistent findings without losing provenance | Specification, structural tests, worked example | Severity substituted for risk; embedded source instructions followed |
| `grc_write_risk_statement` | Draft a cause-event-impact scenario | Specification and structural tests | Vague threat language; unsupported impact |
| `grc_assess_evidence_quality` | Judge evidence for a defined purpose | Specification, structural tests, worked example | Screenshot or assertion treated as sufficient operation evidence |
| `grc_test_control_design` | Assess whether a control is designed to meet its objective | Specification and structural tests | Design confused with implementation or effectiveness |
| `grc_test_control_effectiveness` | Evaluate control operation across a period and population | Specification and structural tests | Sample overgeneralized to full population |
| `grc_review_soc_report` | Evaluate a report for a defined vendor use | Specification and structural tests | Scope, period, CUECs, or subservice dependencies ignored |
| `grc_assess_vendor_security` | Evaluate vendor claims, evidence, contradictions, and scenarios | Specification and structural tests | Vendor assertion repeated as verified fact |
| `grc_quantify_risk_fair` | Build supported frequency and magnitude ranges | Specification, structural tests, worked example | False precision; unsupported independence or correlation |
| `grc_translate_risk_to_business` | Produce a decision brief from technical risk | Specification and structural tests | Technical severity presented as business impact or risk acceptance |

## Evidence available at launch

### Repository-level evidence

`make validate` checks:

- specifications and generated patterns remain synchronized;
- the catalog contains 28 unique, valid pattern names;
- every pattern contains the common evidence contract and human-review gate;
- all patterns remain experimental unless an approved evaluation changes status;
- JSON schemas parse;
- example input and expected-output files remain paired;
- required local README assets exist;
- prohibited compliance and autonomous-review claims are absent from generated patterns.

These checks establish repository consistency. They do not establish that a model follows the pattern reliably.

### Worked-example evidence

| Example | Complete-input behavior | Incomplete-input behavior | Adversarial behavior |
|---|---|---|---|
| `normalize-risk-signal` | Mixed records and enrichment fields are represented | Owner and present exposure remain unknown | Embedded instruction is treated as source text |
| `assess-evidence-quality` | Evidence is assessed against a stated purpose | Population completeness and provenance gaps block sufficiency | Unsupported assertion is not promoted to fact |
| `quantify-risk-fair` | Frequency and magnitude ranges retain their basis | Missing dependency data remains an uncertainty | Pressure for a single precise number is rejected |

Expected outputs are illustrative structures, not golden answers. They show intended behavior and allow reviewers to identify obvious failure. They do not establish cross-model reliability.

## Minimum behavioral evaluation before status promotion

Each recommended starting pattern must be run against at least:

1. complete and internally consistent evidence;
2. incomplete evidence that blocks a conclusion;
3. conflicting or stale evidence;
4. embedded prompt-injection text;
5. plausible but unsupported claims;
6. a request for a protected decision;
7. sensitive data requiring minimization;
8. a domain-specific calculation, population, scope, or category trap.

Each record must identify the pattern commit, provider, model and version, configuration, date, sanitized case, dimension scores, automatic-fail conditions, failure mode, two reviewers, disposition, and change reference. Use [`model-testing.md`](model-testing.md).

## Launch claims allowed

- RiskStitch provides 28 experimental, Fabric-compatible GRC patterns.
- All 28 patterns are included in v0.1.0; nine provide a documented starting path for new users.
- Three sanitized worked examples show the intended evidence and output structure.
- Repository tests validate deterministic generation and structural safety invariants.
- Every pattern requires evidence-state separation and accountable human review.

## Launch claims prohibited

- The patterns are validated across ChatGPT, Claude, Codex, Fabric providers, or model families.
- The patterns produce correct, complete, legally sufficient, audit-ready, or compliant results.
- The patterns can autonomously approve vendors, accept risk, close findings, issue audit opinions, or determine legal applicability.
- Structural tests prove model quality.
- The recommended-starting label means production-ready or excludes the other 19 patterns.

## Promotion rule

A pattern remains `experimental` until documented behavioral evaluation exists. `candidate` requires cases across at least two model families with identified failures recorded. `validated` requires maintainer approval, a published evaluation record, defined version scope, and no unresolved automatic-fail behavior in the approved test set.
