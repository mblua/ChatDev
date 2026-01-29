# Agent Context: /docs/governance

## Purpose

Organizational policies, compliance standards, and decision-making frameworks. Documents here define rules and processes for how work should be done.

## Document Characteristics

| Aspect | Requirement |
|--------|-------------|
| Authority | Cite authoritative sources |
| Scope | Clear applicability boundaries |
| Enforcement | Define consequences |
| Review | Include review schedules |

## Agent Responsibilities

1. **Authority**: Cite regulatory or organizational sources
2. **Compliance**: Reference specific requirements
3. **Enforcement**: Define what happens on non-compliance
4. **Review Cycles**: Document when policies are reviewed

## Required Sections

Every governance document must include:

```
1. Policy Statement
2. Scope and Applicability
3. Definitions
4. Requirements
5. Compliance Criteria
6. Exceptions Process
7. Enforcement
8. Review Schedule
9. Related Policies
10. Change Log
```

## Sensitive Content Warning

Governance documents must be:

- **Customer-agnostic**: No customer-specific policies
- **Generic**: Generalizable frameworks only
- **Sanitized**: No internal org charts or proprietary details
- **Compliant**: No confidential compliance specifics

## Policy Categories

```
/governance/
  /security/
    access-control-policy.md
    data-classification-policy.md
  /development/
    code-review-policy.md
    release-management-policy.md
  /compliance/
    audit-requirements.md
    regulatory-mapping.md
```

## Policy Document Pattern

```markdown
## Policy Statement

[Clear, concise statement of what is required]

## Scope

**Applies to:** [Who/what this covers]
**Does not apply to:** [Explicit exclusions]

## Requirements

1. [Specific, measurable requirement]
2. [Another requirement]

## Compliance

| Requirement | Evidence | Verification |
|-------------|----------|--------------|
| Req 1 | What proves compliance | How to check |
```

## Review Schedule Format

```markdown
## Review Schedule

| Aspect | Frequency | Last Review | Next Review |
|--------|-----------|-------------|-------------|
| Full policy | Annual | YYYY-MM-DD | YYYY-MM-DD |
| Technical details | Quarterly | YYYY-MM-DD | YYYY-MM-DD |
```

