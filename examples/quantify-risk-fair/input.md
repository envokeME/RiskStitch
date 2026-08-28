# Fictional input

Scenario:

During the next 12 months, an external actor uses a compromised support-administrator credential to export customer contact records, causing investigation, notification, support, legal, and customer-loss costs.

Supplied estimates from a workshop:

| Variable | Low | Most likely | High | Basis |
|---|---:|---:|---:|---|
| Successful loss events per year | 0.2 | 0.7 | 2.0 | Three-year internal incident history plus security-team judgment |
| Investigation and response per event | $25,000 | $75,000 | $250,000 | Two internal incidents and one vendor quote |
| Notification and support per event | $10,000 | $40,000 | $200,000 | Record-count scenarios; no jurisdictional determination |
| Legal and regulatory response per event | $5,000 | $30,000 | $250,000 | Counsel range; excludes fines |
| Customer loss per event | $5,000 | $35,000 | $200,000 | Finance hypothesis; no validated churn model |

Controls:

- phishing-resistant MFA is deployed to 70% of support administrators;
- privileged-session logging is enabled, but detection coverage has not been measured;
- quarterly access review found two stale administrators in the last test.

Decision threshold:

The risk committee requires review when modeled annual loss exposure could plausibly exceed $250,000. No risk appetite statement was supplied.

Do not use external benchmark data. Do not run a Monte Carlo simulation. Show only transparent range arithmetic and identify what would need simulation or better data.
