# Contributing to doc-llm-ready

Thank you for contributing to the doc-llm-ready documentation framework.

## Before You Start

1. Read the [README.md](README.md) to understand the project mission
2. Review [conventions/lm-readiness-checklist.md](conventions/lm-readiness-checklist.md) for quality standards
3. Check [conventions/directory-guidelines.md](conventions/directory-guidelines.md) for file placement

## Contribution Workflow

### 1. Create Your Branch

```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

Follow these standards:

| Requirement | Description |
|-------------|-------------|
| Mermaid diagrams | Use Mermaid syntax, never binary images |
| YAML frontmatter | Required for all docs (except AGENTS.md) |
| English content | All documentation must be in English |
| Max document size | 12,000 tokens (~800 lines) per file |

### 3. Self-Validate

Before creating a PR, check your changes against:

- [ ] `conventions/metadata-standard.md` - Frontmatter requirements
- [ ] `conventions/lm-readiness-checklist.md` - Quality checklist
- [ ] `conventions/naming-conventions.md` - File naming rules

### 4. Create Pull Request

```bash
git add .
git commit -m "docs: add your descriptive message"
git push origin feature/your-feature-name
```

Then create a PR on GitHub.

## Mandatory PR Validation

**All documentation PRs MUST be validated before merge.**

### How It Works

1. A reviewer runs the PR validation role prompt
2. The validation generates a detailed report
3. PRs with score >= 75 can be merged
4. PRs with score < 75 require changes

### Validation Process

The reviewer uses the role prompt at `_validations/role-pr-reviewer.md`:

```
@_validations/role-pr-reviewer.md Review PR #<NUMBER>
```

This generates a validation report at:
```
_validations/pr-validations/PR<NUM>_validation_<TIMESTAMP>_<MODEL>.md
```

### Validation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Metadata Compliance | 20% | YAML frontmatter complete and valid |
| Structural Quality | 25% | Proper headings, logical organization |
| LLM-Readiness | 25% | Short sentences, clear structure |
| Directory Compliance | 15% | Correct file placement |
| Content Value | 15% | Meaningful contribution |

### Score Interpretation

| Score | Verdict | Action |
|-------|---------|--------|
| 90-100 | APPROVE | Merge ready |
| 75-89 | APPROVE with comments | Minor suggestions |
| 60-74 | REQUEST_CHANGES | Must fix issues |
| < 60 | REQUEST_CHANGES | Significant rework |

## Protected Files

Some files require specific approvals:

| Path | Approver | Reason |
|------|----------|--------|
| `/_validations/*` | @mblua-phi | Validation system |
| `/conventions/*` | @mblua-phi | Standards |
| `/templates/*` | @mblua-phi | Document templates |
| `AGENTS.md` (any) | @mblua-phi | Agent instructions |

Exception: `/_validations/pr-validations/*` is open for all contributors.

## Questions?

- Check existing documentation in `/docs`
- Review the `AGENTS.md` files for context
- Open an issue for clarification
