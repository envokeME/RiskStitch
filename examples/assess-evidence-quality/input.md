# Fictional input

Claim under test:

> All terminated workforce accounts are disabled in the identity provider within 24 hours of the effective termination time for the period April 1–June 30, 2026.

Supplied evidence:

1. `termination-review.png`: screenshot captured July 2, 2026. It shows 12 rows with employee email, termination date, and account status `Disabled`. The browser address bar, tenant, query, export time, filters, total row count, and page count are not visible.
2. HR analyst email dated July 2, 2026: “These are all terminations for Q2.”
3. Identity administrator email dated July 3, 2026: “I disabled every account the HR team sent.”

Not supplied:

- HR termination population export;
- identity-provider audit log;
- effective termination timestamps;
- account disable timestamps;
- reconciliation by immutable worker identifier;
- exceptions or service-account handling;
- evidence of the report query and filters.
