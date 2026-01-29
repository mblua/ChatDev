# Validation Registry

Central log of all documentation validations performed against AGENTS.md rules.

## Purpose

This registry tracks compliance validation for all documents in the repository. Each entry records:
- Which document was validated
- The specific version validated
- When the validation occurred
- Which AGENTS.md rules were applied
- The validation result
- Which orchestrator performed the validation (e.g., Claude Code, Cursor, Windsurf)
- Which model was used (e.g., claude-opus-4.5, claude-sonnet-4)

## Registry

| Document | Version | Date | Applied Rules | Result | Orchestrator | Model |
|----------|---------|------|---------------|--------|--------------|-------|
| docs/compendiums/muleapps.md | 1.0.0 | 2026-01-05 | root, docs, compendiums | PASS | Cursor | gemini-3-flash-preview |
| docs/compendiums/idp-compendium.md | 1.0.0 | 2026-01-05 | root, docs, compendiums | PASS | Cursor | gemini-3-flash-preview |
| docs/compendiums/mulesoft/agent-fabric-compendium.md | 1.2.0 | 2026-01-14 | root, docs, compendiums | PASS | Cursor | gemini-3-flash-preview |
| docs/compendiums/mulesoft/idp-compendium.md | 1.1.0 | 2026-01-14 | root, docs, compendiums | PASS | Cursor | gemini-3-flash-preview |
| docs/compendiums/mulesoft/api-best-practices.md | 1.0.0 | 2026-01-14 | root, docs, compendiums | PASS | Cursor | gemini-3-flash-preview |
| docs/compendiums/mulesoft/design-patterns.md | 1.0.0 | 2026-01-15 | root, docs, compendiums | PASS | Cursor | gemini-3-flash-preview |
| docs/compendiums/mulesoft/testing-guide.md | 1.0.0 | 2026-01-15 | root, docs, compendiums | PASS | Cursor | gemini-3-flash-preview |
| templates/mulesoft-api-led-app-template.md | 1.0.0 | 2026-01-15 | root, templates | PASS | Cursor | gemini-3-flash-preview |
| docs/roles/role-mulesoft-expert-developer.md | 1.0.0 | 2026-01-15 | root, docs | PASS | Cursor | gemini-3-flash-preview |

## Notes

- Entries are appended chronologically
- Historical entries are never deleted (audit trail)
- A document requires re-validation when its version changes
- `Applied Rules` column uses shorthand: `root` for root AGENTS.md, directory name for directory-specific rules (e.g., `docs`, `conventions`)
- `Orchestrator` identifies the tool/IDE used (Claude Code, Cursor, Windsurf, etc.)
- `Model` identifies the LLM model used (claude-opus-4.5, claude-sonnet-4, gpt-4, etc.)

## PR Validations

For PR-specific validation reports, see the `pr-validations/` subdirectory. Each PR validation generates a detailed report file with:

- Full analysis of changed files
- Compliance scores per criterion
- Overall recommendation (APPROVE/REQUEST_CHANGES)
- Model identification for traceability

PR validation reports follow this naming convention:
```
PR<NUMBER>_validation_<YYYYMMDD_hhmmss>_<MODEL>.md
```
