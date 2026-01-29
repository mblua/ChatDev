# Agent Context: /docs/compendiums

## Purpose

Contains deep technical guides and comprehensive domain knowledge. These are the most dense and authoritative documents in the repository.

## Document Characteristics

| Aspect | Requirement |
|--------|-------------|
| Length | 1000+ lines minimum |
| Audience | Multi-role support (Architect, Developer, Presales, Exec) |
| Diagrams | Extensive Mermaid for complex architectures |
| Structure | Hierarchical section numbering (1., 1.1, etc.) |
| Depth | Comprehensive - do not over-summarize |

## Agent Responsibilities

1. **Depth Validation**: Ensure documents meet 1000+ line threshold
2. **Completeness**: Verify all template sections are present
3. **Audience Coverage**: Check for role-specific appendices
4. **Diagrams**: Require architecture diagrams (Mermaid)
5. **Version Control**: Increment version metadata on updates

## Required Sections

Every compendium must include:

```
1. Executive Summary (business value + technical overview)
2. Table of Contents
3. Core Concepts
4. Architecture and Design (with diagrams)
5. Implementation Guide
6. Best Practices
7. Reference Materials
8. Appendices (by audience role)
9. Change Log
```

## Change Log Conventions

The Change Log section must follow this format:

| Column | Description |
|--------|-------------|
| Version | Semantic version (e.g., 1.0.0, 1.1.0) |
| Date | ISO 8601 date (YYYY-MM-DD) |
| **Human Author** | Name of the human author responsible for the change (not "AI Assistant" or similar) |
| Description | Brief summary of changes |

**Important**: The author column must always contain the name of the human who requested or supervised the change. AI assistants are tools, not authors.

## Technology Organization

Compendiums should be organized by technology when volume warrants:

```
/compendiums/
  /mulesoft/
    agent-fabric-compendium.md
    anypoint-platform-compendium.md
  /aws/
    lambda-compendium.md
```

## When Creating New Compendiums

1. Use `templates/compendium-template.md`
2. Estimate if content will exceed 1000 lines
3. If not, consider `/patterns` or `/concepts` instead
4. Ensure multi-audience appendices are planned

## Key Examples

- `agent-fabric-compendium.md`: The flagship example of a high-quality compendium

## Compendium vs Other Types

| Aspect | Compendium | Pattern | Concept |
|--------|------------|---------|---------|
| Focus | Complete guide | Solution | Theory |
| Length | 1000+ lines | Medium | Short-medium |
| Code | Included | Required | Minimal |
| Audience | All roles | Implementing | Learning |

