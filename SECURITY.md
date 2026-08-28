# Security Policy

## Supported versions

Only the latest release and the default branch receive security fixes.

## Report a vulnerability

Do not include exploit details, secrets, confidential evidence, or personal data in a public issue. Use GitHub's private vulnerability reporting feature when it is enabled for this repository.

## Data-handling boundary

RiskStitch patterns operate on user-supplied material. The repository does not transmit data, call a model, or store user input. The selected AI client and model provider determine runtime data handling.

Before use:

- classify the source material;
- remove secrets and unnecessary personal information;
- use an approved model and tenant;
- apply least privilege to local files and integrations;
- retain outputs according to organizational policy;
- verify model output before operational use.

Prompt injection is an expected threat. Patterns treat supplied documents as untrusted evidence, not instructions. A model may still fail to follow that boundary.
