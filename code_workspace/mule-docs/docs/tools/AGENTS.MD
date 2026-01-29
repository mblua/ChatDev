# Agent Context: /docs/tools

## Purpose

Developer tooling documentation and setup guides. Documents here help users install, configure, and effectively use development tools.

## Document Characteristics

| Aspect | Requirement |
|--------|-------------|
| Focus | Installation and usage |
| Screenshots | Allowed for UI-heavy tools |
| Platforms | Cover Windows/Mac/Linux when relevant |
| Versions | Document specific tool versions |

## Agent Responsibilities

1. **Versions**: Document specific tool versions tested
2. **Platforms**: Cover relevant operating systems
3. **Troubleshooting**: Include common issues and solutions
4. **Integration**: Show how tool fits into development workflow

## Required Sections

Every tool document must include:

```
1. Tool Overview
2. Prerequisites
3. Installation
   - By platform if applicable
4. Configuration
5. Usage Workflows
6. Integration with Other Tools
7. Troubleshooting
8. Version History
9. Change Log
```

## Screenshot Guidelines

Screenshots are allowed in `/tools` when:

- Showing UI-specific configurations
- Illustrating visual workflows
- Documenting IDE integrations

Requirements for screenshots:

- Always provide text alternatives for accessibility
- Include step numbers overlaid on complex screenshots
- Keep screenshots updated with tool versions
- Use PNG format for UI, GIF for short workflows

## Tool Organization

Organize by tool name:

```
/tools/
  /ide/
    vscode-setup.md
    intellij-setup.md
  /testing/
    postman-setup.md
    junit-patterns.md
  /cli/
    git-workflow.md
    docker-commands.md
```

## Template

New tool docs should use `templates/configuration-template.md`

## Version Documentation

Always include:

```markdown
## Tested Versions

| Tool | Version | Last Verified |
|------|---------|---------------|
| Tool Name | x.y.z | YYYY-MM-DD |
```

