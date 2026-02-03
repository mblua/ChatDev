# MuleSoft Workflow Workspace

This workspace contains a multi-agent workflow for generating MuleSoft applications.

## Mule Workflow Command

When the user asks to "run the mule workflow" or "generate a mule app" or similar:

### Execution Steps

1. **Create Session Directory**
   ```
   output/{YYYYMMDD_HHMMSS}/
   ├── logs/
   └── generated_code/
   ```

2. **Phase 1: SpecArchitect**
   - Read `agents/spec_architect.md` for the agent prompt
   - Use Task tool with subagent_type="general-purpose"
   - Input: User's task prompt + agent instructions + reference to mule docs
   - Save output to `logs/01_specification.md`

3. **Phase 2: MuleDeveloper**
   - Read `agents/mule_developer.md` for the agent prompt
   - Use Task tool with subagent_type="general-purpose"
   - Input: Specification from Phase 1 + agent instructions + reference to mule docs
   - Save output to `logs/02_implementation.md`

4. **Phase 3: QAVerifier**
   - Read `agents/qa_verifier.md` for the agent prompt
   - Use Task tool with subagent_type="general-purpose"
   - Input: Specification + Implementation + agent instructions
   - Save output to `logs/03_qa_review.md`

5. **Phase 4: Decision**
   - If QA output starts with "APPROVED":
     - Extract code blocks from implementation
     - Save to `generated_code/` with proper file structure
     - Report success to user
   - If QA output starts with "NEEDS_REVISION":
     - If revision_count < 2:
       - Go back to Phase 2 with QA feedback
       - Save as `logs/02_implementation_rev{n}.md`
     - Else:
       - Save current implementation as final with warning
       - Report completion with caveat

### Agent Prompts Location

- `agents/spec_architect.md` - API specification architect
- `agents/mule_developer.md` - Mule 4 developer
- `agents/qa_verifier.md` - QA and code reviewer

### MuleSoft Documentation

Reference documentation is available at:
- `E:\0_mmb\0_repos_phi\phi_doc-llm-ready\templates\mulesoft-api-led-app-template.md`
- `E:\0_mmb\0_repos_phi\phi_doc-llm-ready\conventions\naming-conventions.md`

Agents should read these files to follow organizational standards.

### Output Structure

```
output/{timestamp}/
├── logs/
│   ├── 01_specification.md
│   ├── 02_implementation.md
│   └── 03_qa_review.md
└── generated_code/
    ├── src/main/mule/
    │   ├── global.xml
    │   ├── interface.xml
    │   └── implementation.xml
    ├── src/main/resources/
    │   └── config.yaml
    └── pom.xml
```

## Example Usage

User: "Run the mule workflow for a Recipe Storage API"

Claude Code should then:
1. Create session directory
2. Run SpecArchitect with the prompt
3. Run MuleDeveloper with the spec
4. Run QAVerifier with spec + implementation
5. Handle approval/revision loop
6. Save final output and report to user
