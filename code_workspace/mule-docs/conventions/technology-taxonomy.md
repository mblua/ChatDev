---
title: Technology Taxonomy
purpose: Define supported technology categories and classification standards for multi-technology documentation
audience: [architect, developer, operator]
scope: Technology categorization, naming conventions, and metadata standards for technology-specific content
last_updated: 2026-01-02
version: 1.0.0
keywords: [taxonomy, technology-stack, categorization, multi-technology, classification]
related_docs: [conventions/metadata-standard.md, conventions/directory-guidelines.md]
---

# Technology Taxonomy

## Overview

This document defines the supported technology categories and provides standards for classifying documentation across multiple technology stacks. It enables consistent organization and discovery of content regardless of the underlying technology.

## Technology Categories

### Integration

Technologies focused on connecting systems and data flows.

| Technology | Identifier | Documentation Focus |
|------------|------------|---------------------|
| MuleSoft | `mulesoft` | Anypoint Platform, DataWeave, Agent Fabric |
| Apache Camel | `apache-camel` | Integration patterns, routes |
| Apache Kafka | `kafka` | Event streaming, topics, consumers |
| RabbitMQ | `rabbitmq` | Message queuing, exchanges |
| IBM MQ | `ibm-mq` | Enterprise messaging |

### AI and Agents

Technologies for artificial intelligence and autonomous agents.

| Technology | Identifier | Documentation Focus |
|------------|------------|---------------------|
| Agent Fabric | `agent-fabric` | MuleSoft agent orchestration |
| LangChain | `langchain` | LLM application framework |
| AutoGen | `autogen` | Multi-agent conversations |
| CrewAI | `crewai` | Agent collaboration |
| Semantic Kernel | `semantic-kernel` | AI orchestration |

### Cloud Platforms

Major cloud providers and their services.

| Technology | Identifier | Documentation Focus |
|------------|------------|---------------------|
| AWS | `aws` | Amazon Web Services |
| Azure | `azure` | Microsoft Azure |
| GCP | `gcp` | Google Cloud Platform |
| Salesforce | `salesforce` | Salesforce platform and APIs |

### DevOps and CI/CD

Tools for development operations and continuous integration.

| Technology | Identifier | Documentation Focus |
|------------|------------|---------------------|
| GitHub | `github` | Repositories, Actions, workflows |
| GitLab | `gitlab` | CI/CD, repositories |
| Jenkins | `jenkins` | Build automation |
| Terraform | `terraform` | Infrastructure as code |
| Ansible | `ansible` | Configuration management |

### Containers and Orchestration

Container technologies and orchestration platforms.

| Technology | Identifier | Documentation Focus |
|------------|------------|---------------------|
| Docker | `docker` | Containerization |
| Kubernetes | `kubernetes` | Container orchestration |
| OpenShift | `openshift` | Enterprise Kubernetes |
| Helm | `helm` | Kubernetes package manager |

### Databases

Data storage and management technologies.

| Technology | Identifier | Documentation Focus |
|------------|------------|---------------------|
| PostgreSQL | `postgresql` | Relational database |
| MongoDB | `mongodb` | Document database |
| Redis | `redis` | In-memory data store |
| Elasticsearch | `elasticsearch` | Search and analytics |
| DynamoDB | `dynamodb` | AWS NoSQL database |

### API Management

API gateway and management platforms.

| Technology | Identifier | Documentation Focus |
|------------|------------|---------------------|
| Anypoint Platform | `anypoint` | MuleSoft API management |
| Kong | `kong` | API gateway |
| Apigee | `apigee` | Google API platform |
| AWS API Gateway | `aws-apigw` | AWS API management |

### Observability

Monitoring, logging, and tracing tools.

| Technology | Identifier | Documentation Focus |
|------------|------------|---------------------|
| Datadog | `datadog` | Monitoring platform |
| Splunk | `splunk` | Log management |
| Grafana | `grafana` | Visualization |
| Prometheus | `prometheus` | Metrics collection |
| Dynatrace | `dynatrace` | APM platform |

### Programming Languages

Languages used in examples and implementations.

| Technology | Identifier | Documentation Focus |
|------------|------------|---------------------|
| Java | `java` | Enterprise applications |
| Python | `python` | Scripts, AI/ML, automation |
| JavaScript | `javascript` | Web, Node.js applications |
| TypeScript | `typescript` | Typed JavaScript |
| DataWeave | `dataweave` | MuleSoft transformations |
| Go | `go` | Cloud-native applications |

## Metadata Extension

### Extended Frontmatter Fields

Documents should include technology classification in their frontmatter:

```yaml
---
# ... standard fields ...
technology_stack:
  primary: mulesoft          # Main technology covered
  secondary: [aws, kafka]    # Related technologies
  version: "4.6"             # Specific version if applicable
integration_points:
  - salesforce               # Technologies this integrates with
  - postgresql
---
```

### Field Definitions

#### technology_stack

| Subfield | Type | Required | Description |
|----------|------|----------|-------------|
| `primary` | string | Yes | Main technology identifier from taxonomy |
| `secondary` | array | No | Related technology identifiers |
| `version` | string | No | Specific version documented |

#### integration_points

| Type | Required | Description |
|------|----------|-------------|
| array | No | Technologies that integrate with the primary |

## Directory Organization

### By Technology

For directories with many documents, organize by technology:

```
/docs/compendiums/
  /mulesoft/
    agent-fabric-compendium.md
    anypoint-platform-compendium.md
  /aws/
    lambda-compendium.md
  /kubernetes/
    deployment-patterns-compendium.md
```

### Cross-Technology Documents

Documents covering multiple technologies equally should:

1. Use the most relevant directory
2. List all technologies in `technology_stack.secondary`
3. Be indexed in all relevant technology sections

## Naming Conventions

### File Names

```
[technology]-[topic]-[type].md

Examples:
- mulesoft-agent-fabric-compendium.md
- aws-lambda-configuration.md
- kafka-consumer-pattern.md
```

### Technology Identifiers

- Use lowercase
- Use hyphens for multi-word names
- Match identifiers in this taxonomy exactly

## Validation Rules

When validating technology metadata:

1. `primary` technology must exist in this taxonomy
2. `secondary` technologies must exist in this taxonomy
3. `integration_points` should exist in this taxonomy
4. Version format should match technology conventions

## Adding New Technologies

To add a new technology to the taxonomy:

1. Identify the appropriate category
2. Add entry with identifier and documentation focus
3. Update this document with the new entry
4. Update `last_updated` and increment version

---

## Change Log

### Version 1.0.0 - 2026-01-02 - Initial technology taxonomy
**Sources:**
- Repository analysis
- Industry standard technology categorization
- Claude Code Assistant
