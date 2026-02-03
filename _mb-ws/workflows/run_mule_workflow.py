#!/usr/bin/env python3
"""
MuleSoft Application Generator Workflow Orchestrator

This script is meant to be executed by Claude Code to orchestrate the multi-agent workflow.
It provides the structure and prompts for each agent phase.

Usage: When the user asks to run the mule workflow, Claude Code should:
1. Read this file to understand the workflow
2. Create the output directory structure
3. Execute each phase using Task tool with the appropriate agent prompts
4. Handle the QA loop logic
5. Save all outputs to the logs directory
"""

import os
from datetime import datetime
from pathlib import Path

# Configuration
WORKSPACE = Path("E:/0_mmb/0_repos/ChatDev/_mb-ws")
AGENTS_DIR = WORKSPACE / "agents"
OUTPUT_DIR = WORKSPACE / "output"
MULE_DOCS = Path("E:/0_mmb/0_repos_phi/phi_doc-llm-ready")

MAX_REVISIONS = 2


def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def create_session_dir():
    """Create a new session directory for this workflow run."""
    timestamp = get_timestamp()
    session_dir = OUTPUT_DIR / timestamp
    (session_dir / "logs").mkdir(parents=True, exist_ok=True)
    (session_dir / "generated_code" / "src" / "main" / "mule").mkdir(parents=True, exist_ok=True)
    (session_dir / "generated_code" / "src" / "main" / "resources").mkdir(parents=True, exist_ok=True)
    return session_dir


def load_agent_prompt(agent_name: str) -> str:
    """Load an agent's prompt from the agents directory."""
    prompt_file = AGENTS_DIR / f"{agent_name}.md"
    return prompt_file.read_text(encoding="utf-8")


# Agent prompts for Claude Code Task tool
SPEC_ARCHITECT_TASK = """
You are the SpecArchitect agent in a MuleSoft application generator workflow.

{agent_prompt}

## User's Request:
{task_prompt}

## Instructions:
1. Read the MuleSoft documentation if needed:
   - E:/0_mmb/0_repos_phi/phi_doc-llm-ready/templates/mulesoft-api-led-app-template.md
   - E:/0_mmb/0_repos_phi/phi_doc-llm-ready/conventions/naming-conventions.md
2. Create a complete technical specification for this MuleSoft application
3. Output the specification in markdown format with all required sections

Do NOT implement the code - only create the specification.
"""

MULE_DEVELOPER_TASK = """
You are the MuleDeveloper agent in a MuleSoft application generator workflow.

{agent_prompt}

## Specification to Implement:
{specification}

{revision_feedback}

## Instructions:
1. Read the MuleSoft documentation if needed:
   - E:/0_mmb/0_repos_phi/phi_doc-llm-ready/templates/mulesoft-api-led-app-template.md
   - E:/0_mmb/0_repos_phi/phi_doc-llm-ready/conventions/naming-conventions.md
2. Implement ALL required files for the Mule application
3. Each file must be in a separate code block with the filename as a comment

Output ALL files needed for a complete, working Mule 4 application.
"""

QA_VERIFIER_TASK = """
You are the QAVerifier agent in a MuleSoft application generator workflow.

{agent_prompt}

## Original Specification:
{specification}

## Implementation to Review:
{implementation}

## Instructions:
1. Review the implementation against the specification
2. Check all items in your verification checklist
3. Your response MUST start with either "APPROVED" or "NEEDS_REVISION"

Be thorough but fair. Only reject for real issues.
"""


if __name__ == "__main__":
    print("MuleSoft Workflow Orchestrator")
    print("=" * 40)
    print(f"Workspace: {WORKSPACE}")
    print(f"Agents: {AGENTS_DIR}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Max Revisions: {MAX_REVISIONS}")
    print()
    print("This script provides the structure for Claude Code to orchestrate the workflow.")
    print("Run it by asking Claude Code to 'run the mule workflow' with your task prompt.")
