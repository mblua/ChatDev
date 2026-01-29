---
title: llm-ready-docs
purpose: Framework for creating and maintaining human-readable and LLM-optimized technical documentation
audience: [architect, developer, presales, executive, operator, analyst]
scope: Documentation structure, standards, conventions, and knowledge assets for LLM-ready ecosystems
last_updated: 2026-01-02
version: 1.1.0
keywords: [llm-ready, documentation-framework, technical-writing, devagents, mermaid]
related_docs: [conventions/metadata-standard.md, conventions/lm-readiness-checklist.md]
---

# llm-ready-docs

## Overview

**llm-ready-docs** is a documentation framework designed to centralize technical knowledge in a format that is both human-readable and fully optimized for Large Language Models (LLMs). This project establishes a clear, scalable structure for creating, maintaining and evolving documentation used across architecture, design, integration, agentic workflows and technical enablement.

The approach is based entirely on Markdown and textual diagram definitions, allowing documentation to be version-controlled, collaboratively improved and easily ingested by LLMs or DevAgents. This enables automated reasoning, summarization, validation and code or design assistance based on the knowledge contained in the repository.

This repository was inspired by and initially seeded with the **MuleSoft Agent Fabric Compendium**, a deeply structured, LM-ready technical asset that demonstrated the benefits of this documentation pattern.

---

## Table of Contents

* [Overview](#overview)
* [Why LM-Ready Documentation?](#why-lm-ready-documentation)
* [Advantages of This Documentation Model](#advantages-of-this-documentation-model)
* [Supported Technologies](#supported-technologies)
* [Repository Structure](#repository-structure)
    * [Directory Descriptions](#directory-descriptions)
* [Agent Instructions (AGENTS.md)](#agent-instructions-agentsmd)
* [Documentation Standards](#documentation-standards)
    * [Metadata Standards](#metadata-standards)
    * [Document Templates](#document-templates)
    * [Validation Checklist](#validation-checklist)
* [Knowledge Assets](#knowledge-assets)
* [Navigation Indexes](#navigation-indexes)
* [Key Principles](#key-principles)
* [How to Contribute](#how-to-contribute)
* [Best Practices for LM-Ready Docs](#best-practices-for-lm-ready-docs)
* [Validating Documentation](#validating-documentation)
* [Future Enhancements](#future-enhancements)
* [License](#license)
* [Acknowledgments](#acknowledgments)

---

## Why LM-Ready Documentation?

Traditional documentation formats are not suited for modern agentic workflows. PDFs, screenshots and graphical diagram files are difficult for LLMs to interpret, impossible to diff properly and slow to update.

This repository adopts a set of principles that ensure long-term usability, precision and alignment with intelligent development frameworks.

## Advantages of This Documentation Model

| Benefit                          | Description                                                        |
| -------------------------------- | ------------------------------------------------------------------ |
| **Versionability**               | Markdown + Git enables full history tracking and rollback          |
| **Collaboration**                | Pull request workflows enable peer review and quality control      |
| **LLM Interpretability**         | Structured text is ideal for DevAgents, bots, and RAG systems      |
| **Portability**                  | Renders consistently across editors, IDEs, and platforms           |
| **Agentic Automation**           | Docs can be auto-generated or auto-updated using AI tools          |
| **Reduced Staleness**            | Single source of truth eliminates wiki drift and duplication       |
| **Content/Rendering Separation** | No binary diagram files; all content is human and machine readable |

---

## Supported Technologies

This repository contains documentation for multiple technology stacks. The complete taxonomy is defined in [`conventions/technology-taxonomy.md`](conventions/technology-taxonomy.md).

| Category | Technologies |
|----------|--------------|
| **Integration** | MuleSoft, Apache Camel, Kafka, RabbitMQ |
| **AI/Agents** | Agent Fabric, LangChain, AutoGen, CrewAI |
| **Cloud Platforms** | AWS, Azure, GCP, Salesforce |
| **DevOps** | GitHub, GitLab, Terraform, Jenkins |
| **Containers** | Kubernetes, Docker, OpenShift, Helm |
| **Observability** | Datadog, Splunk, Grafana, Prometheus |
| **Databases** | PostgreSQL, MongoDB, Redis, Elasticsearch |

Documents use the `technology_stack` field in frontmatter to enable discovery by technology. See:
- [Index by Technology](indexes/by-technology.md)
- [Index by Audience](indexes/by-audience.md)
- [Index by Topic](indexes/by-topic.md)

---

## Repository Structure

The following structure is recommended for organizing LM-ready assets:

```
/docs
  /compendiums      # Deep technical guides (1000+ lines)
    AGENTS.MD
  /concepts         # Theoretical foundations
    AGENTS.MD
  /architectures    # System designs and blueprints
    AGENTS.MD
  /patterns         # Reusable solution templates
    AGENTS.MD
  /platforms        # Configuration and governance
    AGENTS.MD
  /tools            # Developer tooling documentation
    AGENTS.MD
  /governance       # Policies and compliance
    AGENTS.MD
  /observability    # Monitoring and metrics
    AGENTS.MD
  AGENTS.MD         # Knowledge base routing

/indexes
  AGENTS.MD
  by-technology.md  # Index by technology stack
  by-audience.md    # Index by target audience
  by-topic.md       # Index by subject matter

/templates
  AGENTS.MD
  compendium-template.md
  configuration-template.md
  pattern-template.md
  concept-template.md
  architecture-template.md

/conventions
  AGENTS.MD
  metadata-standard.md
  lm-readiness-checklist.md
  directory-guidelines.md
  naming-conventions.md
  change-log-guidelines.md
  technology-taxonomy.md    # Multi-technology categorization

AGENTS.MD           # Root agent context
CLAUDE.md           # Redirects to AGENTS.md
README.md           # This file
```

This structure ensures clarity, modularity and ease of automated consumption.

### Directory Descriptions

*   **`/compendiums`**: Comprehensive technical guides (1000+ lines OK, but consider splitting). Include appendices for multiple audiences (architect, developer, presales, executive) with business value propositions and citation systems.
*   **`/concepts`**: Core theoretical principles and fundamental ideas that underpin technical domains. Focus on understanding over implementation with conceptual diagrams.
*   **`/architectures`**: High-level designs, system diagrams, and structural blueprints. Emphasize architectural decision rationale and Mermaid-based architecture diagrams.
*   **`/patterns`**: Reusable solution templates with code examples, trade-off analysis, and decision frameworks for when to use each pattern.
*   **`/platforms`**: Configuration-focused documentation with step-by-step instructions, verification checklists, and governance standards for service-side environments (GitHub, Cloud providers, CI/CD).
*   **`/tools`**: Developer tooling documentation with installation guides, configuration examples, and integration patterns. Screenshots allowed for UI-heavy tools (exception to Mermaid-only rule).
*   **`/governance`**: Organizational policies, compliance standards, and decision-making frameworks with clear approval processes and escalation paths.
*   **`/observability`**: Standards for monitoring, logging, and system health tracking with defined metrics, alerting standards, and troubleshooting playbooks.

---

## Agent Instructions (AGENTS.md)

This repository uses `AGENTS.md` files to provide context for LLM agents and AI assistants. These files are exempt from the standard metadata requirements.

### Structure

- **Root `AGENTS.md`**: Global rules, principles, and repository-wide context
- **Directory `AGENTS.md`**: Context-specific instructions for each major directory
- **`CLAUDE.md`**: Redirects to `AGENTS.md` for Claude-specific tooling

### Available Agent Context Files

| Location | Purpose |
|----------|---------|
| [`AGENTS.md`](AGENTS.md) | Global agent instructions and multi-technology context |
| [`conventions/AGENTS.md`](conventions/AGENTS.MD) | Standards enforcement context |
| [`docs/AGENTS.md`](docs/AGENTS.MD) | Knowledge base routing and quality gates |
| [`templates/AGENTS.md`](templates/AGENTS.MD) | Template selection guidance |
| [`indexes/AGENTS.md`](indexes/AGENTS.MD) | Index maintenance rules |

Each `/docs` subdirectory also contains its own `AGENTS.md` with domain-specific instructions.

### Usage

When working with AI assistants, point them to the relevant `AGENTS.md` for optimal results. Agents should:

1. Read the root `AGENTS.md` first for global context
2. Read the directory-specific `AGENTS.md` before operating in that directory
3. Follow validation rules defined in the agent context files

---

## Documentation Standards

### Metadata Standards

All technical documentation assets must include standardized YAML frontmatter for consistent metadata across all assets. The complete metadata standard is documented in [`conventions/metadata-standard.md`](conventions/metadata-standard.md). (Note: `AGENTS.md` files are exempt).

**Required Frontmatter Fields:**
- `title`: Document title
- `purpose`: Brief purpose statement (1-2 sentences)
- `audience`: Target roles (architect, developer, presales, executive, operator, analyst)
- `scope`: Document boundaries and coverage
- `last_updated`: Update date (YYYY-MM-DD)
- `version`: Semantic version (major.minor.patch)
- `keywords`: Searchable terms for discovery
- `related_docs`: Paths to related documents

### Document Templates

Standardized templates ensure consistency and quality across document types:

* **[Configuration Template](templates/configuration-template.md)**: For `/docs/platforms/` documents with step-by-step setup guides
* **[Compendium Template](templates/compendium-template.md)**: For `/docs/compendiums/` with comprehensive technical coverage
* **[Pattern Template](templates/pattern-template.md)**: For `/docs/patterns/` with reusable solution frameworks

**Usage:** Copy the appropriate template and customize it for your specific documentation needs.

### Validation Checklist

Use the [LM-Readiness Validation Checklist](conventions/lm-readiness-checklist.md) to ensure all technical documentation assets meet framework standards before committing changes.

**Quick Validation Areas:**
- ✅ YAML frontmatter completeness (excluding `AGENTS.md`)
- ✅ Mermaid-only diagrams
- ✅ Customer-agnostic content
- ✅ Proper directory placement
- ✅ Readability and structure

---

## Directory Guidelines

Detailed guidelines for each directory type are available in [`conventions/directory-guidelines.md`](conventions/directory-guidelines.md), including:

- Specific content characteristics for each directory
- Best practices and formatting requirements
- Examples of appropriate content
- When to use each directory type

---

## Knowledge Assets

This repository contains deeply structured assets that expand on specific technical domains:

*   **[MuleSoft Agent Fabric Compendium](docs/compendiums/mulesoft/agent-fabric-compendium.md)**: A comprehensive technical guide covering the four pillars of Agent Fabric (Discover, Orchestrate, Govern, Observe). It includes architecture diagrams, A2A/MCP protocol specifications, and strategic implementation priorities for enterprise agent management.
*   **[GitHub Repository Configuration](docs/platforms/github-repo-config.md)**: A step-by-step governance guide for configuring secure GitHub repositories. It defines branch protection rules, squash-merge strategies, and collaborator permissions suitable for both documentation and code-centric projects.

---

## Navigation Indexes

The repository provides multiple navigation indexes to help discover documentation:

| Index | Description | Use When |
|-------|-------------|----------|
| [By Technology](indexes/by-technology.md) | Documents grouped by technology stack | Looking for docs about a specific technology |
| [By Audience](indexes/by-audience.md) | Documents grouped by target role | Finding content for a specific audience |
| [By Topic](indexes/by-topic.md) | Hierarchical topic-based navigation | Exploring related concepts |

These indexes are maintained alongside the documentation and should be updated when new documents are added.

---

## Key Principles

### LM-Ready by Design

All documentation must follow consistent structural patterns:

* **Clear metadata**: Frontmatter or header sections identifying purpose, scope, and audience
* **Predictable structure**: Standardized heading hierarchy and section ordering
* **Diagram support**: Visual representations using text-based formats

### Mermaid-First Diagrams

All diagrams must be written using [Mermaid](https://mermaid.js.org/) syntax to ensure:

* Version control friendliness (diff-able text)
* Portability across rendering platforms
* LLM interpretability without image processing
* Easy maintenance and updates

### Customer-Agnostic Content

Documents must be:

* Free of sensitive or proprietary customer information
* Suitable for internal automation and DevAgent consumption
* Generalizable patterns rather than implementation-specific details

---

## How to Contribute

Contributions are welcome and encouraged. This repository is intended to evolve collaboratively.

### Contribution Workflow

1. **Create a feature branch** for your update.
2. Follow all LM-ready conventions described in `/conventions`.
3. Ensure all diagrams are in Mermaid.
4. Verify that no customer-specific details are included.
5. Submit a **Pull Request** with a clear description of:

   * what was changed,
   * why it was changed,
   * and any implications for existing docs.
6. At least one reviewer must validate:

   * clarity,
   * LM-readiness,
   * alignment with style guide,
   * and correctness of technical content.
7. Once approved, the PR can be merged.

### Submitting Corrections

If you detect an error:

* Open an Issue describing the problem, or
* Submit a PR directly with the fix.

Both small corrections and large enhancements are equally welcome.

---

## Best Practices for LM-Ready Docs

To maximize LLM performance and output consistency, apply the following guidelines:

### Do:

* Use short, declarative sentences.
* Prioritize structure over prose.
* Include examples whenever possible.
* Keep diagrams simple and descriptive.
* Use headings to break down concepts.
* Keep related files close in the folder hierarchy.

### Avoid:

* Screenshots of diagrams.
* Embedding unstructured large text blocks.
* Mixing customer-specific and general technical content.
* Using ambiguous terminology.

---

## Validating Documentation

Before merging new or updated documentation, validate compliance with LM-readiness standards using the comprehensive [LM-Readiness Validation Checklist](conventions/lm-readiness-checklist.md).

### Validation Process

1. **Self-Review**: Use the checklist to validate your document before submission
2. **Peer Review**: Have another contributor validate using the same checklist
3. **Automated Checks**: Run any available automated validation scripts

### LLM-Based Validation

For automated verification, use an LLM with the following prompt:

```
Verify the document [DOCUMENT_PATH] against the LM-readiness guidelines defined in README.md and conventions/lm-readiness-checklist.md.

Evaluate compliance across these criteria:
1. LM-Ready by Design: Clear metadata, predictable structure, diagram support
2. Mermaid-First Diagrams: All diagrams in Mermaid syntax, no image files
3. Customer-Agnostic Content: No sensitive data, generalizable patterns
4. Best Practices: Short sentences, structured content, examples, proper headings
5. Directory Compliance: Proper placement and structure for document type

Provide a compliance summary table with status (✅/❌) and evidence for each criterion.
```

### Compliance Scoring

- **100% Compliant**: All requirements met, no warnings
- **90-99% Compliant**: All critical requirements met, minor issues
- **80-89% Compliant**: Major requirements met, some gaps
- **<80% Compliant**: Requires revision before acceptance

This validation can be performed manually by reviewers or integrated into CI/CD pipelines using LLM-based tooling.

---

## Change Log

### Version 1.1.0 - 2026-01-02 - Multi-technology support and distributed AGENTS.md
**Sources:**
- Claude Code Assistant

**Changes:**
- Added multi-technology documentation support with technology taxonomy
- Created AGENTS.md files for all major directories
- Added CLAUDE.md redirect file
- Created navigation indexes (by-technology, by-audience, by-topic)
- Added concept-template.md and architecture-template.md
- Extended metadata-standard.md with technology_stack and integration_points fields
- Created new directories: concepts, architectures, patterns, tools, governance, observability

### Version 1.0.1 - 2025-12-19 - Added standardized YAML frontmatter for LLM-readiness compliance
**Sources:**
- Cursor Agent

### Version 1.0.0 - 2025-12-18 - Initial repository setup with LM-ready documentation framework
**Sources:**
- Mariano Blua
- Grok (xAI)

---

## Future Enhancements

Planned expansions for this repository include:

* Automated generation of documentation from source assets.
* Creation of an internal **DevAgent** preloaded with this repository.
* Enhanced automation scripts for LM-readiness validation (beyond current checklist).
* Interactive applications for pre-sales demonstrations.
* Integration with internal wikis, referencing the repository as the single source of truth.

### Recently Implemented

* ✅ **Standardized YAML frontmatter** for consistent metadata across all documents
* ✅ **Document templates** for Configuration, Compendium, and Pattern types
* ✅ **Comprehensive validation checklist** for LM-readiness compliance
* ✅ **Detailed directory guidelines** with specific requirements for each content type
* ✅ **Metadata standards documentation** with field definitions and examples

---

## License

Documentation in this repository is intended for internal enablement and technical acceleration. Distribution must follow organizational guidelines.

---

## Acknowledgments

This repository grows from the initial effort of consolidating deep technical material into LM-ready structures, starting with the **MuleSoft Agent Fabric Compendium**, which validated the value of this approach.
