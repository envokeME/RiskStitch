# Safety model

RiskStitch is a prompt library. It does not run models, transmit data, create decisions, or enforce controls. Safety depends on the pattern, source data, model, client, provider, configuration, reviewer, and downstream workflow.

## Protected decisions

Patterns must not make these final decisions:

- legal or regulatory applicability;
- compliance certification or attestation;
- audit opinion or formal audit conclusion;
- risk acceptance or exception approval;
- vendor approval;
- finding closure;
- production AI deployment approval;
- privacy lawful-basis determination;
- financial, personnel, safety, or emergency action.

The output names the authorized human role and unresolved items.

## Evidence-state model

| Label | Meaning | Permitted basis |
|---|---|---|
| `FACT` | Directly observed in supplied input | Exact source field, record, date, or quoted fragment |
| `SOURCE-DERIVED` | Explicitly asserted by a named supplied source | Document statement or respondent claim with locator |
| `INFERENCE` | Reasoned interpretation from supplied evidence | Stated reasoning and evidence chain |
| `ASSUMPTION` | Unverified input used provisionally | Explicit rationale and effect if wrong |
| `UNKNOWN` | Required information is absent or unusable | Gap, conflict, or inaccessible evidence |

The labels describe epistemic state. They do not rate importance or truth. A vendor's statement can be `SOURCE-DERIVED` and still require verification.

## Threats and controls

| Threat | Pattern control | Residual limitation |
|---|---|---|
| Fabricated evidence | Requires supplied evidence locators and `UNKNOWN` for gaps | Models may fabricate locators |
| Prompt injection inside evidence | Declares inputs untrusted and unable to override the pattern | Models may follow malicious embedded instructions |
| False precision | Requires ranges, units, basis, and uncertainty | Models may perform arithmetic incorrectly |
| Stale framework interpretation | Requires source version, jurisdiction, and date | Model knowledge may still contaminate output |
| Compliance overclaim | Prohibits certification and legal conclusions | Users may remove warnings or misuse output |
| Sensitive-data exposure | Requires minimization and redaction | Provider and client controls determine actual handling |
| Automation bias | Separates recommendation from decision and requires review | Reviewers may rubber-stamp polished output |
| Proprietary text leakage | Prohibits unnecessary reproduction | Users control source permissions and retention |

## Operational gate

Before using a pattern operationally:

1. confirm the task boundary and authorized reviewer;
2. classify and minimize input data;
3. use an approved model, provider, tenant, and retention configuration;
4. run a prompt-injection and secret check on source material;
5. verify citations and evidence locators against original sources;
6. independently recalculate scores, ranges, and percentages;
7. record model, pattern version, input date, reviewer, and decision;
8. retain or delete inputs and outputs under policy;
9. test high-impact patterns against adversarial and incomplete cases;
10. prevent the model from approving its own output.

## Status meaning

All release 0.1.0 patterns are `experimental`. Structural tests prove repository consistency only. They do not establish accuracy, reliability, legal sufficiency, framework conformance, or fitness for a particular organization.
