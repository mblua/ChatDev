# Directory Structure Guidelines

## Overview

This document provides detailed guidelines for content organization within each directory in the `/docs` structure. Each directory serves a specific purpose and follows distinct conventions to ensure consistency and optimal LLM ingestion.

## Directory Guidelines

### `/docs/compendiums/`

**Purpose:** Deep technical knowledge, comprehensive guides, and **Best Practices** for complex domains.

**Content Characteristics:**
- Comprehensive coverage of technical domains (typically 1000+ lines)
- Specialized "Best Practices" sub-documents when volume warrants
- Multi-audience support (architect, developer, presales, executive)
- Extensive use of Mermaid diagrams for complex architectures
- Structured appendices for different audience types
- Business value propositions and ROI analysis
- Citation systems and source attribution

**Best Practices:**
- Use hierarchical section numbering (1., 1.1, 1.1.1)
- **Technology Subfolders**: Organize content into technology-specific subdirectories (e.g., `/compendiums/mulesoft/`) for better curation.
- Include executive summaries and technical deep-dives
- Consider splitting very long documents (>2000 lines) into focused sub-documents
- Provide appendices for implementation details and reference materials
- Include version metadata and change tracking

**Examples:**
- `agent-fabric-compendium.md` - Enterprise agent management guide
- `integration-platform-compendium.md` - Platform architecture overview

**When to Use:**
- Documenting complex technical domains requiring comprehensive coverage
- Creating reference materials for enterprise architecture decisions
- Providing multi-role guidance (technical + business)

---

### `/docs/platforms/`

**Purpose:** Configuration and governance documentation for service-side environments.

**Content Characteristics:**
- Step-by-step configuration instructions
- Platform-specific governance rules
- Security and compliance settings
- Environment setup procedures
- Verification checklists and validation steps

**Best Practices:**
- Use numbered steps for sequential processes
- Include verification sections with expected outcomes
- Provide both human-readable instructions and LLM-executable steps
- Focus on governance and security configurations
- Include troubleshooting sections for common issues

**Examples:**
- `github-repo-config.md` - Repository governance setup
- `aws-environment-config.md` - Cloud infrastructure configuration
- `kubernetes-cluster-setup.md` - Container orchestration setup

**When to Use:**
- Documenting platform configuration procedures
- Establishing governance standards for infrastructure
- Creating setup guides for development environments
- Defining security and compliance configurations

---

### `/docs/patterns/`

**Purpose:** Reusable solution templates and design patterns for common technical problems.

**Content Characteristics:**
- Problem-solution format with context
- Code examples and implementation templates
- Design pattern documentation
- Anti-patterns and common pitfalls
- Decision trees for pattern selection

**Best Practices:**
- Start with problem statement and context
- Include multiple implementation approaches when applicable
- Provide code examples in appropriate languages
- Document trade-offs and when to use/not use patterns
- Include testing and validation patterns

**Examples:**
- `microservice-communication-patterns.md` - Service interaction templates
- `error-handling-patterns.md` - Exception management strategies
- `caching-strategies.md` - Data caching implementation patterns

**When to Use:**
- Documenting reusable technical solutions
- Creating implementation templates for common problems
- Establishing design pattern libraries
- Providing decision frameworks for architectural choices

---

### `/docs/tools/`

**Purpose:** Documentation for developer-side tooling and productivity applications.

**Content Characteristics:**
- Tool installation and configuration
- Usage patterns and workflows
- Integration with development processes
- Troubleshooting and optimization tips
- Screenshots allowed for UI-heavy tools (exception to Mermaid-only rule)

**Best Practices:**
- Include installation prerequisites and system requirements
- Document common use cases and workflows
- Provide configuration examples and best practices
- Include performance tuning recommendations
- Document integration points with other tools

**Examples:**
- `cursor-ide-setup.md` - IDE configuration and extensions
- `git-workflow-tools.md` - Git productivity enhancements
- `testing-frameworks.md` - Testing tool configurations

**When to Use:**
- Documenting developer productivity tools
- Creating setup guides for development environments
- Establishing tool integration patterns
- Providing troubleshooting guides for development tools

---

### `/docs/concepts/`

**Purpose:** Core theoretical principles and fundamental ideas that underpin technical domains.

**Content Characteristics:**
- Theoretical foundations and principles
- Conceptual models and frameworks
- Terminology definitions and taxonomies
- Relationship mappings between concepts

**Best Practices:**
- Focus on understanding over implementation
- Use conceptual diagrams (mindmaps, relationship diagrams)
- Provide clear definitions and examples
- Establish consistent terminology across domains

**Examples:**
- `distributed-systems-concepts.md` - Core distributed computing principles
- `ai-agent-concepts.md` - Fundamental AI agent principles

---

### `/docs/architectures/`

**Purpose:** High-level designs, system diagrams, and structural blueprints.

**Content Characteristics:**
- System-level architecture diagrams
- Component interaction models
- Data flow architectures
- Deployment topologies

**Best Practices:**
- Use Mermaid architecture diagrams extensively
- Focus on high-level design decisions
- Document architectural principles and constraints
- Include rationale for architectural choices

**Examples:**
- `enterprise-integration-architecture.md` - System integration patterns
- `microservice-architecture.md` - Service-oriented design blueprints

---

### `/docs/governance/`

**Purpose:** Organizational policies, compliance standards, and decision-making frameworks.

**Content Characteristics:**
- Governance policies and procedures
- Compliance requirements and standards
- Decision frameworks and approval processes
- Risk management guidelines

**Best Practices:**
- Document clear decision-making processes
- Include compliance checklists and audit procedures
- Establish escalation paths and approval hierarchies
- Provide governance templates and examples

**Examples:**
- `security-governance.md` - Security policy frameworks
- `change-management.md` - Release and deployment governance

---

### `/docs/observability/`

**Purpose:** Standards for monitoring, logging, and system health tracking.

**Content Characteristics:**
- Monitoring and alerting standards
- Logging formats and aggregation patterns
- Performance metrics definitions
- Health check procedures

**Best Practices:**
- Define standard metrics and KPIs
- Establish logging standards and formats
- Document monitoring dashboards and alerts
- Include troubleshooting playbooks

**Examples:**
- `application-monitoring.md` - Application health tracking
- `infrastructure-observability.md` - System monitoring standards

---

## Content Migration Guidelines

When moving or restructuring content between directories:

1. **Review Purpose Alignment:** Ensure content fits the target directory's purpose
2. **Update Metadata:** Modify frontmatter to reflect new scope and audience
3. **Update Cross-References:** Fix any related document links
4. **Validate Structure:** Ensure content follows target directory conventions
5. **Update Navigation:** Modify table of contents and internal references

## Quality Assurance

All documents should be reviewed against these guidelines:

- **Purpose Alignment:** Content matches directory purpose and conventions
- **Structure Compliance:** Follows recommended formatting and organization
- **Metadata Completeness:** Includes required frontmatter fields
- **Cross-Reference Accuracy:** All related document links are valid
- **Audience Appropriateness:** Content suitable for declared audience roles

---

*These guidelines ensure consistent, discoverable, and purpose-aligned documentation across all repository directories.*