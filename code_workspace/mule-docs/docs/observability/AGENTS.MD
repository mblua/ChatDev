# Agent Context: /docs/observability

## Purpose

Monitoring, metrics, logging, and system health documentation. Documents here define what to measure and how to respond.

## Document Characteristics

| Aspect | Requirement |
|--------|-------------|
| Metrics | Defined with units and thresholds |
| Alerts | Include response procedures |
| Dashboards | Specify layouts and queries |
| SLOs | Clear service level objectives |

## Agent Responsibilities

1. **Metrics**: Define units and collection methods
2. **Thresholds**: Justify alert boundaries
3. **Runbooks**: Link to incident response procedures
4. **SLOs**: Define service level objectives clearly

## Required Sections

Every observability document must include:

```
1. Observability Strategy
2. Key Metrics
3. Logging Standards
4. Alerting Rules
5. Dashboard Specifications
6. SLO Definitions
7. Runbook References
8. Change Log
```

## Metric Documentation Format

For each metric:

```markdown
### Metric: [metric_name]

| Property | Value |
|----------|-------|
| **Description** | What this metric measures |
| **Unit** | requests/second, milliseconds, percentage |
| **Collection** | How/where collected |
| **Normal Range** | Expected values under normal operation |
| **Warning Threshold** | When to investigate |
| **Critical Threshold** | When to alert |
| **Response** | Link to runbook |
```

## Alert Definition Format

```markdown
### Alert: [Alert Name]

**Condition:** `metric > threshold for duration`

**Severity:** Critical | Warning | Info

**Response:**
1. [Immediate action]
2. [Investigation steps]
3. [Escalation path]

**Runbook:** [Link to detailed procedure]
```

## SLO Definition Format

```markdown
### SLO: [Service Level Objective Name]

| Property | Value |
|----------|-------|
| **Indicator (SLI)** | What is measured |
| **Target** | 99.9% availability |
| **Window** | Rolling 30 days |
| **Error Budget** | 43.2 minutes/month |
```

## Dashboard Specification

```markdown
### Dashboard: [Dashboard Name]

**Purpose:** [What questions this dashboard answers]

**Panels:**
1. [Panel name] - [Metric/query] - [Visualization type]
2. [Panel name] - [Metric/query] - [Visualization type]

**Refresh Rate:** [How often to update]
```

