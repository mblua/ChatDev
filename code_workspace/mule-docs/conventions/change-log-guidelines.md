# Change Log Guidelines

## Overview

All technical documentation assets in this repository must include a **Change Log** section at the end (before the final summary) to track version history and attribution. This ensures transparency, accountability, and proper credit for all contributions (both human and AI-assisted).

**Exception:** Files of type `AGENTS.md` are exempt from this requirement as they serve as internal context for AI agents rather than public technical documentation.

## Required Format

Each version entry in the Change Log must follow this exact format:

```markdown
## Change Log

### Version X.X.X - YYYY-MM-DD - Description of changes
**Sources:**
- Contributor Name
- AI Assistant Name (if applicable)
```

## Format Requirements

### Version Entry Structure
- **Version:** Semantic versioning (major.minor.patch) - must match the version in frontmatter
- **Date:** YYYY-MM-DD format - must match the last_updated date for that version
- **Description:** Clear, concise summary of what changed in this version
- **Sources:** Bullet list of contributors who worked on that version

### Ordering
- **Reverse chronological order:** Most recent versions must appear first
- **Complete history:** All versions from 1.0.0 onward must be documented

### Source Attribution
- **Human contributors:** Include full names of team members who contributed
- **AI contributors:** Include AI assistant names (e.g., "Grok (xAI)", "Claude", "GPT-4")
- **Multiple contributors:** List each contributor on a separate line
- **Lead contributor:** Place primary author first when applicable

## Semantic Versioning Guidelines

Follow semantic versioning principles for version increments:

- **MAJOR (X.0.0):** Breaking changes to structure or core concepts
- **MINOR (X.Y.0):** New sections, significant content additions, or clarifications
- **PATCH (X.Y.Z):** Typos, formatting fixes, or minor updates

## Implementation Rules

### Placement
- **Location:** Change Log section must be the last section before the final document summary
- **Separator:** Use `---` (three dashes) before and after the Change Log section

### When to Update
- **New versions:** Always add a new entry when incrementing version number
- **Version changes:** Update both the frontmatter version and add Change Log entry
- **Date updates:** Ensure the date in Change Log matches last_updated in frontmatter

### Content Guidelines
- **Descriptive:** Use clear, actionable descriptions of changes
- **Concise:** Keep descriptions under 100 characters when possible
- **Action-oriented:** Start with verbs (Added, Updated, Fixed, Removed)
- **Specific:** Reference section names or feature names when relevant

## Examples

### Single Contributor
```markdown
### Version 1.1.0 - 2025-12-19 - Added troubleshooting section with common Git issues
**Sources:**
- Mariano Blua
```

### Multiple Contributors (Human + AI)
```markdown
### Version 1.0.0 - 2025-12-18 - Initial version with GitHub Desktop and CLI methods
**Sources:**
- Mariano Blua
- Grok (xAI)
```

### Complex Update
```markdown
### Version 2.1.0 - 2025-12-20 - Major refactoring of branching workflows and added CI/CD integration examples
**Sources:**
- Lead Developer Name
- Assistant Developer Name
- Grok (xAI)
- Claude (Anthropic)
```

## Validation Checklist

Before submitting a document update, verify:

- [ ] Change Log follows the exact format specified
- [ ] Version number matches frontmatter version
- [ ] Date matches last_updated in frontmatter
- [ ] Sources include all contributors (human and AI)
- [ ] Description is clear and concise
- [ ] Entries are in reverse chronological order
- [ ] No duplicate or missing version entries

## Migration for Existing Documents

For documents created before this guideline:

1. **Add Change Log section** at the end (before final summary)
2. **Create Version 1.0.0 entry** with original creation date
3. **Include all known contributors** (human and AI)
4. **Future updates** follow normal versioning process

## Related Standards

- **[Metadata Standard](metadata-standard.md)**: Frontmatter requirements and field definitions
- **[LM-Readiness Checklist](lm-readiness-checklist.md)**: Overall document compliance validation

---

*These guidelines ensure consistent, transparent, and accountable documentation versioning across the repository.*