# Agent Context: /docs/platforms

## Purpose

Documentation focused on service-side environments, configuration, and governance standards. Step-by-step guides for platform setup and management.

## Document Characteristics

| Aspect | Requirement |
|--------|-------------|
| Focus | "How to configure" and "how to verify" |
| Structure | Numbered steps with verification checklists |
| Governance | Rules for platform usage |
| Precision | Exact field names and UI labels |

## Agent Responsibilities

1. **Actionability**: Ensure steps are executable
2. **Verification**: Each section needs success criteria
3. **Prerequisites**: List all requirements upfront
4. **Screenshots**: Allowed for UI-heavy platforms (exception to Mermaid-only rule)

## Required Sections

Every platform document must include:

```
1. Objective (with success criteria)
2. How to Use This Document
3. Prerequisites and Assumptions
4. Configuration Steps (numbered)
   - Navigation path
   - Required vs Optional settings
5. Verification Steps (with expected results)
6. Troubleshooting
7. Change Log
```

## Platform Organization

Organize by platform name when volume warrants:

```
/platforms/
  /github/
    repo-config.md
    branching-committing.md
    actions-setup.md
  /aws/
    iam-config.md
    vpc-setup.md
  /anypoint/
    environment-setup.md
```

## Special Considerations

- Include both GUI and CLI methods when available
- Mark required vs optional settings clearly
- Provide rollback instructions for critical configs
- Use exact UI labels in quotes: Click **"Save Changes"**

## Template

New platform docs should use `templates/configuration-template.md`

## Key Examples

- `github-repo-config.md`: Standard for repository governance
- `github-branching-commiting.md`: Workflow standards

## Verification Pattern

For each configuration step:

```markdown
### Step X: [Action Name]

**Navigation:** Settings → [Path] → [Submenu]

**Configuration:**
- Field 1: `value` (Required)
- Field 2: `value` (Optional)

**Expected Result:** [What user should see after saving]
```

