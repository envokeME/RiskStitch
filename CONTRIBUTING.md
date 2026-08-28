# Contributing to RiskStitch

RiskStitch accepts patterns, evaluation cases, documentation, schemas, and corrections that improve defensibility of GRC work.

## Contribution requirements

A pattern contribution must:

1. solve one bounded GRC task;
2. define required inputs and explicitly tolerate missing information;
3. distinguish facts, source-derived statements, inferences, assumptions, and unknowns;
4. require evidence locators for consequential conclusions;
5. prohibit fabricated evidence, citations, owners, dates, scores, and compliance claims;
6. define a deterministic output structure;
7. end with a human-review gate;
8. include at least one evaluation case;
9. avoid proprietary standards text and confidential material;
10. pass `make validate`.

## Workflow

1. Edit `specs/patterns.json`.
2. Run `python3 tools/render_patterns.py`.
3. Add or update an evaluation case.
4. Run `make validate`.
5. Open a pull request describing the task boundary, evidence model, known failure modes, and testing performed.

Do not hand-edit generated files under `patterns/`. The renderer will overwrite them.

## Content boundaries

Never contribute:

- secrets, tokens, credentials, internal URLs, or personal data;
- real client assessments, audit evidence, contracts, reports, or findings;
- proprietary control or regulatory text without documented permission;
- claims that a pattern guarantees compliance, eliminates professional review, or produces an audit opinion;
- instructions that let a model approve its own output.

## Status labels

- `experimental`: structurally valid; model behavior has not been broadly evaluated.
- `candidate`: evaluation cases exist across at least two model families and identified failures are documented.
- `validated`: requires maintainer approval, a published evaluation record, and defined version scope.

No contribution may self-promote to `validated`.
