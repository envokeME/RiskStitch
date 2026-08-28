# Illustrative expected structure

## Model specification

- Unit: annual loss exposure for one credential-compromise scenario.
- Time horizon: 12 months.
- Supplied loss-event frequency range: 0.2–2.0 per year; most likely 0.7.
- Supplied per-event magnitude components are added, assuming no overlap. That independence and overlap assumption is unverified.
- Fines are excluded. Customer-loss estimates are a low-confidence hypothesis.

## Input estimates

All workshop values are `SOURCE-DERIVED`. Internal incident records, vendor quote, counsel range, and finance model were not supplied directly, so their quality cannot be verified.

## Calculation

Simple aligned-point arithmetic, not a probability distribution or Monte Carlo result:

- Low per-event magnitude: $25,000 + $10,000 + $5,000 + $5,000 = $45,000.
- Most-likely per-event magnitude: $75,000 + $40,000 + $30,000 + $35,000 = $180,000.
- High per-event magnitude: $250,000 + $200,000 + $250,000 + $200,000 = $900,000.
- Low aligned annual value: 0.2 × $45,000 = $9,000.
- Most-likely aligned annual value: 0.7 × $180,000 = $126,000.
- High aligned annual value: 2.0 × $900,000 = $1,800,000.

These aligned points are not percentiles and should not be described as a loss distribution.

## Loss magnitude components

Investigation is the strongest-supported component. Customer loss has the weakest basis. Legal response excludes fines but may overlap with investigation; the overlap is `UNKNOWN`.

## Sensitivity and uncertainty

The high result is driven by loss-event frequency and the legal, notification, and customer-loss high estimates. The most valuable next data are administrator population and MFA coverage, credential-compromise attempts, verified detection coverage, incident loss records, record counts, and a validated churn relationship.

## Decision comparison

The supplied high aligned value exceeds the $250,000 committee review threshold. This supports escalation for review, not a claim that annual loss will be $1.8 million.

## Human review required

The risk analyst must validate the model and prevent double counting. Finance and counsel must validate magnitude components. The risk committee retains treatment and acceptance authority.
