# LLM-Ready Documentation Metadata Standard

## Overview

All technical documentation assets in this repository must include standardized YAML frontmatter to ensure consistent metadata across all assets. This standard enables better LLM ingestion, improved discoverability, and consistent document management.

**Exception:** Files of type `AGENTS.md` are exempt from this metadata standard as they serve as internal context for AI agents rather than public technical documentation.

## Required Frontmatter Format

All documentation assets (excluding `AGENTS.md`) must include the following YAML frontmatter at the beginning of the file:

```yaml
---
title: Document Title
purpose: Brief purpose statement (1-2 sentences)
audience: [architect, developer, presales, executive]
scope: Specific scope definition (what the document covers)
last_updated: YYYY-MM-DD
version: Semantic version (e.g., 1.0.0)
keywords: [keyword1, keyword2, keyword3]
related_docs: [path/to/related.md, another/path.md]
---
```

## Field Definitions

### title
- **Type:** String
- **Required:** Yes
- **Description:** The full title of the document
- **Example:** "MuleSoft Agent Fabric Compendium"

### purpose
- **Type:** String
- **Required:** Yes
- **Description:** Brief statement explaining why this document exists and what value it provides
- **Example:** "Comprehensive technical guide for implementing MuleSoft Agent Fabric across enterprise environments"

### audience
- **Type:** Array of strings
- **Required:** Yes
- **Allowed Values:** `architect`, `developer`, `presales`, `executive`, `operator`, `analyst`
- **Description:** Target audience roles for this document
- **Example:** `[architect, developer, presales]`

### scope
- **Type:** String
- **Required:** Yes
- **Description:** Specific boundaries of what the document covers
- **Example:** "Agent Fabric implementation patterns, A2A/MCP protocols, and governance frameworks"

### last_updated
- **Type:** Date string (YYYY-MM-DD)
- **Required:** Yes
- **Description:** Date when the document was last substantively updated
- **Example:** `2025-12-18`

### version
- **Type:** String (semantic versioning)
- **Required:** Yes
- **Description:** Current version of the document following semantic versioning
- **Example:** `1.2.0`

### keywords
- **Type:** Array of strings
- **Required:** Yes
- **Description:** Searchable keywords for discovery and categorization
- **Example:** `[agent-fabric, mulesoft, enterprise-integration, governance]`

### related_docs
- **Type:** Array of strings (relative paths)
- **Required:** No (but recommended)
- **Description:** Paths to related documents in the repository
- **Example:** `[docs/platforms/github-repo-config.md, docs/patterns/agent-patterns.md]`

### technology_stack (Optional - for multi-technology docs)
- **Type:** Object
- **Required:** No (recommended for technical documents)
- **Description:** Categorizes the document by technology for indexing and discovery
- **Structure:**
```yaml
technology_stack:
  primary: technology-identifier
  secondary: [tech1, tech2]
  version: "x.y.z"
```

#### technology_stack.primary
- **Type:** String
- **Required:** Yes (if technology_stack is used)
- **Description:** Main technology covered by the document
- **Valid Values:** See `conventions/technology-taxonomy.md`
- **Example:** `mulesoft`, `aws`, `kubernetes`

#### technology_stack.secondary
- **Type:** Array of strings
- **Required:** No
- **Description:** Related or secondary technologies covered
- **Example:** `[kafka, postgresql]`

#### technology_stack.version
- **Type:** String
- **Required:** No
- **Description:** Specific version of the primary technology documented
- **Example:** `"4.6"`, `"2024.1"`

### integration_points (Optional)
- **Type:** Array of strings
- **Required:** No
- **Description:** Technologies that integrate with the primary technology in this document
- **Example:** `[salesforce, aws-s3, mongodb]`

## Change Log Requirements

All documents must include a **Change Log** section following the standards defined in [`conventions/change-log-guidelines.md`](change-log-guidelines.md). This ensures proper version tracking and source attribution.

## Implementation Notes

1. **Placement:** Frontmatter must be the first content in the file, before any headings or text
2. **Validation:** Documents will be validated for frontmatter completeness during review
3. **Versioning:** Increment version numbers according to semantic versioning principles:
   - **MAJOR:** Breaking changes to structure or core concepts
   - **MINOR:** New sections, significant content additions, or clarifications
   - **PATCH:** Typos, formatting fixes, or minor updates
4. **Date Updates:** Update `last_updated` whenever substantive changes are made
5. **Change Log:** Follow the guidelines in [`conventions/change-log-guidelines.md`](change-log-guidelines.md)

## Examples

### Compendium Document
```yaml
---
title: MuleSoft Agent Fabric Compendium
purpose: Comprehensive technical guide covering the four pillars of Agent Fabric for enterprise implementation
audience: [architect, developer, presales]
scope: Agent Fabric architecture, A2A/MCP protocols, governance frameworks, and implementation patterns
last_updated: 2025-12-18
version: 1.0.0
keywords: [agent-fabric, mulesoft, enterprise-integration, governance, observability]
related_docs: [docs/platforms/github-repo-config.md]
---
```

### Configuration Document
```yaml
---
title: GitHub Repository Configuration
purpose: Step-by-step governance guide for configuring secure GitHub repositories
audience: [architect, developer]
scope: Branch protection rules, merge strategies, and collaborator permissions for documentation and code repositories
last_updated: 2025-12-18
version: 1.1.0
keywords: [github, governance, security, repository-config, devops]
related_docs: [docs/governance/security-policies.md]
technology_stack:
  primary: github
  secondary: []
---
```

### Multi-Technology Document
```yaml
---
title: Kafka Integration with MuleSoft
purpose: Guide for integrating Apache Kafka with MuleSoft applications
audience: [architect, developer]
scope: Kafka connector configuration, event processing patterns, and error handling
last_updated: 2026-01-02
version: 1.0.0
keywords: [kafka, mulesoft, integration, event-driven, messaging]
related_docs: [docs/patterns/event-driven-pattern.md]
technology_stack:
  primary: mulesoft
  secondary: [kafka]
  version: "4.6"
integration_points:
  - kafka
  - aws-msk
---
```

## Migration Timeline

Existing documents should be updated to include standardized frontmatter according to this schedule:
- **Phase 1 (Immediate):** Core documents in `/docs/compendiums/` and `/docs/platforms/`
- **Phase 2 (Week 2):** All remaining documents in established directories
- **Phase 3 (Ongoing):** New documents must include frontmatter from creation

---

*This standard ensures consistent, discoverable, and LLM-ready documentation across the repository.*