# MuleSoft Application Generator Workflow

This workflow generates a complete MuleSoft application using a multi-agent approach.

## Workflow Structure

```
User Prompt → SpecArchitect → MuleDeveloper → QAVerifier → [APPROVED → FINAL | NEEDS_REVISION → Loop]
```

## Agents

| Agent | Role | Max Iterations |
|-------|------|----------------|
| SpecArchitect | Creates API specification and architecture | 1 |
| MuleDeveloper | Implements the Mule application | 1 + revisions |
| QAVerifier | Reviews and approves/rejects code | max 2 revisions |

## Execution Steps

### Step 1: Specification
Spawn SpecArchitect agent with the user's task prompt. Save output to `logs/01_specification.md`.

### Step 2: Development
Spawn MuleDeveloper agent with the specification. Save output to `logs/02_implementation.md`.

### Step 3: QA Review
Spawn QAVerifier agent with the implementation. Save output to `logs/03_qa_review.md`.

### Step 4: Decision
- If QA response starts with "APPROVED": Workflow complete. Save final code to `generated_code/`.
- If QA response starts with "NEEDS_REVISION":
  - If revision count < 2: Go to Step 2 with QA feedback
  - Else: Complete with current implementation and warning

## Output Structure

```
output/{timestamp}/
├── logs/
│   ├── 01_specification.md
│   ├── 02_implementation.md
│   ├── 02_implementation_rev1.md (if revision)
│   ├── 03_qa_review.md
│   └── 03_qa_review_rev1.md (if revision)
└── generated_code/
    ├── src/main/mule/
    │   ├── global.xml
    │   ├── interface.xml
    │   └── implementation.xml
    ├── src/main/resources/
    │   └── config.yaml
    └── pom.xml
```

## Usage

To run this workflow, provide a task prompt describing the MuleSoft application you want to create.

Example:
```
Create a Recipe Storage System API with POST /api/recipes endpoint that saves recipes to the filesystem.
```
