# Agent Context: /docs

## Purpose

Primary knowledge base containing all technical documentation. This directory houses the core content of the repository, organized by document type and purpose.

## Agent Responsibilities

1. **Classification**: Ensure documents are in the correct subdirectory
2. **Cross-References**: Maintain valid relative links between documents
3. **Technology Tags**: Verify `technology_stack` metadata accuracy
4. **Quality**: Enforce LM-readiness standards

## Directory Taxonomy

| Directory | Purpose | Characteristics |
|-----------|---------|-----------------|
| `/compendiums` | Comprehensive technical guides | Multi-audience, multi-section, authoritative reference |
| `/platforms` | Configuration and governance | Step-by-step, verification |
| `/patterns` | Reusable solutions | Problem-solution format |
| `/concepts` | Theoretical foundations | Educational, no implementation |
| `/architectures` | System designs | Diagrams, decisions |
| `/tools` | Developer tooling | Installation, workflows |
| `/governance` | Policies/compliance | Standards, approvals |
| `/observability` | Monitoring/metrics | Alerts, dashboards, SLOs |

## Document Size Policy

**Maximum size: 12,000 tokens (~800 lines)**

Documents exceeding this limit MUST be split into smaller, focused documents. This ensures:
- Optimal LLM context window usage
- Better RAG chunk coherence
- Easier maintenance and updates
- Improved human navigation

**Split indicators:**
- Document exceeds 800 lines
- Multiple unrelated topics in single document
- Sections that could stand alone as independent guides (e.g., Best Practices, implementation deep-dives)

## Decision Flowchart

```mermaid
flowchart TD
    A[New Document] --> B{Over 800 lines?}
    B -->|Yes| SPLIT[Split into focused docs]
    SPLIT --> A
    B -->|No| C{Multi-audience authoritative guide?}
    C -->|Yes| D[/compendiums]
    C -->|No| E{Is it step-by-step config?}
    E -->|Yes| F[/platforms]
    E -->|No| G{Is it a reusable solution?}
    G -->|Yes| H[/patterns]
    G -->|No| I{Is it theoretical?}
    I -->|Yes| J[/concepts]
    I -->|No| K{Is it system design?}
    K -->|Yes| L[/architectures]
    K -->|No| M{Is it tool-specific?}
    M -->|Yes| N[/tools]
    M -->|No| O{Is it policy/compliance?}
    O -->|Yes| P[/governance]
    O -->|No| Q[/observability]
```

## Quality Gates

Before approving any document in `/docs`:

- [ ] **Document size under 800 lines** (~12k tokens)
- [ ] Correct subdirectory placement per taxonomy
- [ ] Complete YAML frontmatter metadata
- [ ] At least one Mermaid diagram for complex topics
- [ ] Cross-references use relative paths
- [ ] Change Log entry present and current
- [ ] `technology_stack` field accurate (if multi-tech)
- [ ] No customer-specific or sensitive data

## Cross-Reference Standards

When linking between documents:

```markdown
<!-- Correct: Relative path from current location -->
See [GitHub Configuration](platforms/github-repo-config.md)

<!-- Incorrect: Absolute path -->
See [GitHub Configuration](/docs/platforms/github-repo-config.md)
```

## Technology Organization

Subdirectories may be further organized by technology when volume warrants:

```
/docs/compendiums/
  /mulesoft/
  /aws/
  /kubernetes/
```

Follow `conventions/technology-taxonomy.md` for valid technology identifiers.

## Navigation

Each sub-directory has its own `AGENTS.MD` for specific domain context.

