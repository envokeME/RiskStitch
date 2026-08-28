# Worked examples

These fixtures are fictional and sanitized. Expected outputs illustrate structure and evidence discipline; they are not golden answers and do not validate model behavior.

| Example | Pattern | Failure mode exercised |
|---|---|---|
| `normalize-risk-signal` | `grc_normalize_risk_signal` | Mixed sources, stale timestamps, missing owner, misleading severity, embedded instruction |
| `assess-evidence-quality` | `grc_assess_evidence_quality` | Screenshot evidence without population completeness or provenance |
| `quantify-risk-fair` | `grc_quantify_risk_fair` | Sparse ranges, unsupported correlation, false-precision pressure |

Run an example with Fabric:

```bash
cat examples/normalize-risk-signal/input.md \
  | fabric --pattern grc_normalize_risk_signal
```

Compare the result to the expected structure, then score it with `docs/model-testing.md`.
