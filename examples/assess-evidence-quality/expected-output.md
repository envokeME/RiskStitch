# Illustrative expected structure

## Claim under test

The claim has four assertions: population completeness, identity reconciliation, disablement occurrence, and disablement within 24 hours for April 1–June 30, 2026.

## Quality assessment

| Dimension | Rating | Basis |
|---|---|---|
| Relevance | Medium | Screenshot relates to disabled accounts but does not show timing |
| Reliability | Low | Provenance, tenant, query, and system-of-record details are absent |
| Completeness | Low | The 12-row screenshot cannot be reconciled to the HR population |
| Timeliness | Medium | Captured soon after quarter end but historical state is not established |
| Traceability | Low | No immutable identifier or source query |
| Corroboration | Low | Two emails are assertions; no HR export or identity audit log |

## Coverage matrix

The screenshot partially supports that 12 displayed accounts had a `Disabled` status at an unknown observation context. It does not establish the complete termination population or the 24-hour timing assertion.

## Contradictions and limitations

- “All terminations” is a `SOURCE-DERIVED` HR assertion without population evidence.
- “Every account” is a `SOURCE-DERIVED` administrator assertion without reconciliation evidence.
- No direct contradiction is supplied, but independent corroboration is absent.

## Support conclusion

`insufficient_information`. The artifact does not support the full claim across population, period, or timing.

## Evidence request

Request the HR population and identity audit log for the same period, joined by immutable worker identifier, with effective termination and disablement timestamps, query lineage, exclusions, and exceptions.

## Human review required

The control owner must validate the population definition. The tester or audit authority retains the operating-effectiveness conclusion.
