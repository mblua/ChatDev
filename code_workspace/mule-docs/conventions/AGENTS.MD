# Agent Context: /conventions

## Purpose

This directory defines the rules and standards for ALL documentation in this repository. These conventions ensure consistency, quality, and LLM-readiness across all content.

## Agent Responsibilities

1. **Enforcement**: When reviewing documents, validate against these conventions
2. **Updates**: Propose updates to conventions when patterns emerge
3. **Consistency**: Ensure new conventions don't conflict with existing ones
4. **Education**: Help users understand why conventions exist

## Critical Files (Priority Order)

| Priority | File | Purpose |
|----------|------|---------|
| 1 | `lm-readiness-checklist.md` | Primary validation source |
| 2 | `metadata-standard.md` | Required YAML frontmatter for all documents |
| 3 | `directory-guidelines.md` | Placement rules for each folder |
| 4 | `technology-taxonomy.md` | Technology categorization and identifiers |
| 5 | `naming-conventions.md` | File and branch naming standards |
| 6 | `change-log-guidelines.md` | Version tracking and attribution |

## When Modifying Conventions

Follow semantic versioning for convention changes:

| Change Type | Version Impact | Example |
|-------------|----------------|---------|
| MAJOR | Affects all existing documents | New required field in metadata |
| MINOR | Adds new optional guidelines | New recommended practice |
| PATCH | Clarifications only | Typo fix, example update |

Always update examples when modifying rules.

## Validation Rules

When an agent validates a document against conventions:

1. Start with `metadata-standard.md` - check frontmatter completeness
2. Apply `directory-guidelines.md` - verify correct placement
3. Run through `lm-readiness-checklist.md` - comprehensive check
4. Verify `change-log-guidelines.md` compliance
5. Check `technology-taxonomy.md` for valid technology identifiers

## Convention Conflict Resolution

If conventions appear to conflict:

1. `lm-readiness-checklist.md` takes precedence
2. More specific guidelines override general ones
3. When in doubt, prioritize LLM interpretability
4. Document the conflict and propose resolution

## Adding New Conventions

Before adding a new convention file:

1. Verify it doesn't duplicate existing guidance
2. Ensure it aligns with core principles (Mermaid-first, metadata-standard, customer-agnostic)
3. Include clear examples
4. Update this AGENTS.md with the new file in the priority table

## Maintenance

Updates to these files have project-wide impact. Agents should be cautious and ensure backward compatibility or provide a clear migration path.

