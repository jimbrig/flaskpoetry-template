# "Use Log4brains to manage the ADRs"

- Status: Accepted
- Deciders: Jimmy Briggs
- Date: 2023-03-14
- Tags: Documentation, Architecture, Descisions, Logs, Techinical, Tool

Technical Story: Architecture Descision Record Logging Tool (ACR): `Log4brains`

## Context and Problem Statement

Need a mechanism to document decisions made related to infrastructure,
technical design, tooling, and design patterns.

## Decision Drivers

- Easy to Use
- Runs in CI/CD Pipeline
- Automated Deployments
- Automated ADR CLI Tool

## Considered Options

- Manual

## Decision Outcome

Chosen option: `log4brains` (`npm` CLI package) with GitHub Actions.

### Positive Consequences

- [e.g., improvement of quality attribute satisfaction, follow-up decisions required, …]
- …

### Negative Consequences <!-- optional -->

- [e.g., compromising quality attribute, follow-up decisions required, …]
- …

## Pros and Cons of the Options <!-- optional -->

### [option 1]

[example | description | pointer to more information | …] <!-- optional -->

- Good, because [argument a]
- Good, because [argument b]
- Bad, because [argument c]
- … <!-- numbers of pros and cons can vary -->

### [option 2]

[example | description | pointer to more information | …] <!-- optional -->

- Good, because [argument a]
- Good, because [argument b]
- Bad, because [argument c]
- … <!-- numbers of pros and cons can vary -->

### [option 3]

[example | description | pointer to more information | …] <!-- optional -->

- Good, because [argument a]
- Good, because [argument b]
- Bad, because [argument c]
- … <!-- numbers of pros and cons can vary -->

## Links <!-- optional -->

- [Link type](link to adr) <!-- example: Refined by [xxx](yyyymmdd-xxx.md) -->
- … <!-- numbers of links can vary -->
