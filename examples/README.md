# Worked examples

These fixtures are fictional and sanitized. Expected outputs illustrate structure and evidence discipline; they are not golden answers and do not validate model behavior.

| Example | Pattern | Failure mode exercised |
|---|---|---|
| [`normalize-risk-signal`](normalize-risk-signal/) | `grc_normalize_risk_signal` | Mixed sources, stale timestamps, missing owner, misleading severity, embedded instruction |
| [`assess-evidence-quality`](assess-evidence-quality/) | `grc_assess_evidence_quality` | Screenshot evidence without population completeness or provenance |
| [`quantify-risk-fair`](quantify-risk-fair/) | `grc_quantify_risk_fair` | Sparse ranges, unsupported correlation, false-precision pressure |

Read the [end-to-end walkthrough](end-to-end-walkthrough.md) for the complete path:

`User objective → source input → selected pattern → execution prompt → expected output → human review → next bounded task`

Run an example with Fabric:

```bash
cat examples/normalize-risk-signal/input.md \
  | fabric --pattern grc_normalize_risk_signal
```

Without Fabric, use the selected pattern's `system.md` as the governing instruction in ChatGPT, Claude, Codex, or another supported interface, then provide the example `input.md` separately. See the [AI interface guide](../docs/using-with-ai-tools.md).

Compare the result to the illustrative expected output, then score model behavior with [`docs/model-testing.md`](../docs/model-testing.md).
