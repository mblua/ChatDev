# Agent Context: _validations Directory

## Purpose

This directory contains the validation system for the doc-llm-ready repository. It centralizes:

- PR validation role prompt
- Validation registry
- PR validation reports

## Directory Structure

| Path | Purpose | Protection |
|------|---------|------------|
| `README.md` | System documentation | @mblua-phi |
| `AGENTS.md` | This file - agent context | @mblua-phi |
| `role-pr-reviewer.md` | Role prompt for PR validation | @mblua-phi |
| `VALIDATION_REGISTRY.md` | Historical validation log | @mblua-phi |
| `pr-validations/` | PR validation reports | Open |

## Agent Instructions

### When Working in This Directory

1. **Read `role-pr-reviewer.md`** before performing any PR validation
2. **Never modify protected files** without explicit user request
3. **Always use isolated workspace** for PR checkout (see role prompt)
4. **Write reports to `pr-validations/`** using the naming convention

### Naming Convention for Validation Reports

```
PR<NUMBER>_validation_<YYYYMMDD_hhmmss>_<MODEL>.md
```

Example:
```
PR42_validation_20250113_153045_claude-opus-4-5.md
```

### Model Self-Identification

When generating validation reports, include in frontmatter:

```yaml
reviewer_model: claude-opus-4-5-20251101
reviewer_model_short: claude-opus-4-5
```

### Prohibited Actions

| Action | Reason |
|--------|--------|
| Checkout PR in main repo | Breaks session context |
| Modify `role-pr-reviewer.md` | Protected file |
| Delete validation reports | Audit trail required |
| Skip user notification | User must be informed of workspace creation |

### Validation Report Requirements

Each PR validation report MUST include:

1. **Frontmatter** with PR metadata and model identification
2. **Summary** of what the PR does
3. **Changed files table** with status
4. **Detailed analysis** per file
5. **Quality metrics** with scores
6. **Recommendation** (APPROVE/REQUEST_CHANGES)

### Integration with VALIDATION_REGISTRY.md

After generating a PR validation report:

1. If verdict is APPROVE, add entry to `VALIDATION_REGISTRY.md`
2. If verdict is REQUEST_CHANGES, do NOT add entry
3. Entry format must match existing registry structure

## Language Standard

All content in this directory MUST be written in English.
