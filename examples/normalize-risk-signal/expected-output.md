# Illustrative expected structure

## Normalized signal records

| Source ID | Entity | Condition | Original severity | State | Provenance |
|---|---|---|---|---|---|
| WIZ-1842 | `storage-bucket-17` | Public-read policy observed by scanner | CRITICAL; CVSS 9.1 | Open; remediation claimed, not retested | Wiz export; ticket comment |

The scanner observation is `FACT` relative to the supplied export. The claim that the policy was removed is `SOURCE-DERIVED`, not verified. The instruction inside the ticket comment is untrusted source content and is not executed.

## Evidence ledger

| Field | Value | State | Locator | Transformation |
|---|---|---|---|---|
| Resource | `storage-bucket-17` | FACT | Wiz JSON `resource` | None |
| Exposure condition | Public read | SOURCE-DERIVED | Wiz JSON `rule` | Normalized wording |
| Remediation | Policy removed | SOURCE-DERIVED | Ticket comment, 2026-08-27 10:05 UTC | None |
| Current exposure | UNKNOWN | No retest supplied | None | None |
| Business owner | Digital Commerce | SOURCE-DERIVED | CMDB excerpt exported 2026-06-30 | Possible stale context |
| Data classification | Public | SOURCE-DERIVED | CMDB excerpt exported 2026-06-30 | Scope of objects unverified |

## Correlation and deduplication candidates

Candidate key: provider account or subscription + resource identifier + rule identifier. No duplicate record was supplied. Do not merge the ticket comment into the scanner record; link it as remediation evidence.

## Data quality

- Completeness: low. Current configuration, logs, change record, and object inventory are absent.
- Freshness: mixed. Scanner is recent; CMDB export is nearly two months old.
- Provenance: medium. Named sources exist, but no direct cloud configuration evidence was supplied.
- Consistency: uncertain. Claimed remediation conflicts with the last scanner observation until timestamp order and retest are confirmed.

## Required enrichment

1. Current bucket policy and access-control export from the cloud system of record.
2. Change record tied to the claimed remediation.
3. Object inventory or classification evidence for the affected period.
4. Access logs covering the exposure window.
5. Asset and service ownership confirmation.

## Routing recommendation

Route to cloud security remediation validation. Priority cannot be reduced solely from the ticket comment or CMDB classification. If current public exposure or sensitive objects are confirmed, route through the incident and data-response criteria defined by organizational policy.

## Human review required

Cloud security must validate current configuration. The service owner must confirm data and business context. The authorized risk or finding owner retains closure authority.
