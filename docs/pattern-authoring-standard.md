# Pattern authoring standard

## Design rule

One pattern performs one bounded transformation for one accountable workflow. Split patterns when inputs, evidence standards, decision rights, or outputs differ materially.

## Required specification fields

Each object in `specs/patterns.json` contains:

- `name`: stable `grc_`-prefixed slug;
- `title`: practitioner-readable task;
- `version`: semantic version for the pattern contract;
- `status`: `experimental`, `candidate`, or `validated`;
- `domain`: primary GRC domain;
- `summary`: bounded outcome;
- `role`: expertise and scope;
- `inputs`: minimum source material and context;
- `method`: ordered analysis method;
- `output_sections`: exact reviewable output contract;
- `special_rules`: task-specific failure boundaries;
- `tags`: discovery terms.

The renderer injects the shared evidence contract and human-review gate.

## Quality tests

A strong pattern must answer:

1. What exact decision or work product does this support?
2. Which facts must come from input rather than model memory?
3. What evidence locator can a reviewer verify?
4. Which missing input could reverse the result?
5. Which human retains authority?
6. What common category error must be blocked?
7. How will a reviewer know that the output is complete?
8. What adversarial or incomplete case should make the pattern refuse a conclusion?

## Writing constraints

- Use observable verbs: identify, map, compare, calculate, trace, test, classify.
- Avoid vague verbs without criteria: improve, enhance, ensure, consider, manage.
- Do not ask the model to be infallible, unbiased, legally authoritative, or certified.
- Do not request hidden chain-of-thought. Require concise rationale and evidence instead.
- Do not encode proprietary framework text.
- Do not require a score when inputs are insufficient.
- Preserve raw values when normalization changes a field.
- Define denominators for percentages and populations for tests.

## Rendering

```bash
python3 tools/render_patterns.py
python3 tools/render_patterns.py --check
```

Generated files under `patterns/` are review artifacts. Change the structured specification, render, and review the resulting diff.
