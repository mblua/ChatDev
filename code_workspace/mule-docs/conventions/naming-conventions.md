# Naming Conventions for GitHub Repositories and Branches

This document establishes the official naming standards for PhiDimensions' GitHub organization to ensure consistency, discoverability, and automated governance.

---

## 1. Repository Naming

All repository names must be in **lowercase** and use **kebab-case** (words separated by hyphens).

### Base Pattern
`[scope]-[project-name]-[component]`

### Scope Prefixes
Use the following prefixes to categorize repositories:

| Prefix | Description | Example |
| :--- | :--- | :--- |
| `pro-` | **Projects/Clients**: Specific client work or initiatives. | `pro-hmbay-order-api` |
| `doc-` | **Documentation**: Non-executable content, guides, or blueprints. | `doc-architecture-standards` |
| `mule-` | **MuleSoft**: Reusable MuleSoft assets, common frameworks, or APIs. | `mule-common-error-handler` |
| `poc-` | **Proof of Concept**: Experimental projects or sandbox tests. | `poc-agentforce-integration` |
| `infra-` | **Infrastructure**: DevOps scripts, Terraform, or CI/CD templates. | `infra-mule-runtime-setup` |
| `tool-` | **Tools**: Internal scripts, utilities, or automation tools. | `tool-github-migrator` |

### Key Rules
*   **No Company Name**: Do not include "phi" or "phidimensions" in the repo name; it is already part of the organization.
*   **No Versioning**: Avoid `v1` or `v2` in the name. Use Git tags or branches for version management.
*   **Be Descriptive**: Ensure the name clearly reflects the content without being overly long.

---

## 2. Branch Naming

All branch names must be in **lowercase**, use **kebab-case**, and follow a hierarchical structure using forward slashes.

### Pattern
`[category]/[ID]-[short-description]`

### Categories
Categorizing branches allows for better visual organization and easier automation via Branch Rulesets.

| Category | Description | Example |
| :--- | :--- | :--- |
| `feature/` | New functionality or enhancements. | `feature/phi-123-oauth-support` |
| `bugfix/` | Fixes for bugs found in development or QA. | `bugfix/gh-45-validation-error` |
| `hotfix/` | Urgent fixes intended for production (`main`). | `hotfix/security-patch-v1` |
| `refactor/` | Code changes that neither fix a bug nor add a feature. | `refactor/api-response-format` |
| `docs/` | Documentation-only changes. | `docs/update-naming-guide` |
| `experiment/` | Temporary branches for testing ideas. | `experiment/new-mule-connector` |
| `[username]/` | Personal workspace for testing, organizing, or WIP. | `mblua/testing`, `mblua/organizing` |

### Key Rules
*   **Personal Names for Workspaces**: Use your username as a prefix for personal, non-collaborative work (e.g., `mblua/my-test`). For collaborative tasks or PRs, use the standard categories (`feature/`, `bugfix/`, etc.).
*   **Ticket Integration**: Always include the Ticket ID (Jira, GitHub Issues, etc.) if applicable for collaborative branches.
*   **Keep it Short**: Focus on the *intent* of the branch.
*   **Clean Up**: Delete branches immediately after they are merged to keep the repository clean.

---

## 3. Benefits for Governance

By following these conventions, we can implement **Branch Rulesets** at the Organization level:
*   Enforce that all PRs targeting `main` must come from `feature/`, `bugfix/`, or `hotfix/` branches.
*   Automatically require specific reviewers for branches categorized as `infra/` or `hotfix/`.
*   Filter repositories by name to apply security policies across all `pro-` repositories at once.

