---
title: GitHub Repository Configuration
purpose: Step-by-step governance guide for configuring secure GitHub repositories
audience: [architect, developer]
scope: Branch protection rules, merge strategies, and collaborator permissions for documentation and code repositories
last_updated: 2025-12-18
version: 1.0.0
keywords: [github, governance, security, repository-config, devops]
related_docs: []
---

# GitHub Repository Configuration

## Objective

Configure a GitHub repository (documentation-only) so that:

* All changes reach `main` **only via Pull Requests**
* Each PR is merged as **a single commit (Squash-only)**
* Direct pushes to `main` are blocked
* Reviews are required for non-admin users
* Repository admins may optionally bypass review requirements

This document is intended to be followed **step by step** by both humans and LLMs to reproduce the exact same configuration.

---

## How to Use This Document

This document serves as a standardized checklist for repository owners. When creating a new repository or auditing an existing one, follow each section sequentially. For LLMs/DevAgents, this document can be used as a reference to verify if a repository's settings (fetched via GitHub API) align with the organization's governance standards.

---

## Repository Assumptions

* Repository is hosted on **GitHub**
* Default branch name: `main`
* Repository type: **documentation-only** (no CI / no status checks)
* Repository owner wants to remain **admin**
* Other collaborators should be **non-admin contributors**

---

## 1. Branch Protection Rule (`main`)

### Navigation

`Repository → Settings → Branches → Branch protection rules`

Create or edit a rule with:

* **Branch name pattern**: `main`

### Required Settings (ENABLE)

* **Require a pull request before merging**
  * Required approvals: **1**
* **Require conversation resolution before merging**
* **Dismiss stale pull request approvals when new commits are pushed** (recommended)
* **Require approval of the most recent reviewable push** (optional, recommended)

### Admin Bypass Policy

* **Do not allow bypassing the above settings**: **DISABLED**

This allows repository admins to merge without a reviewer, while non-admin users must still comply with all PR requirements.

### Explicitly Disabled Settings

* **Require status checks to pass before merging** (no CI in docs repo)
* **Require linear history**
* **Require signed commits**
* **Require deployments to succeed before merging**
* **Lock branch**

### Force & Deletion Rules

* **Allow force pushes**: DISABLED
* **Allow deletions**: DISABLED

---

## 2. Pull Request Merge Strategy (Squash-only)

### Navigation

`Repository → Settings → Pull requests`

### Merge Options Configuration

Set exactly as follows:

* **Allow merge commits**: DISABLED
* **Allow squash merging**: ENABLED
* **Allow rebase merging**: DISABLED

### Squash Commit Message

* **Default squash commit message**: `Pull request title and description`

### Resulting Behavior

* Every PR is merged as **one single commit**
* No traditional merge commits are possible
* No rebase merges are possible
* Merge button in PRs shows **only**: `Squash and merge`

---

## 3. Collaborators & Permissions

### Navigation

`Repository → Settings → Collaborators`

### Repository Owner

* The repository owner is implicitly **Admin**
* Owner does not appear in the collaborators list
* Owner cannot accidentally lose admin rights

### Inviting Collaborators

1. Click **Add people**
2. Invite user by GitHub username
3. Wait until invitation is **accepted**

### After Invitation Is Accepted

* Set collaborator **Type** to:
  * **Write** (recommended)

### Role Guarantees

| Role          | Capabilities                                         |
| ------------- | ---------------------------------------------------- |
| Admin (Owner) | Can bypass PR approvals, manage rules, merge at will |
| Write         | Can push branches, open PRs, cannot bypass rules     |

---

## 4. Code Repositories (CI/CD Extension)

If this repository contained **source code** (not just documentation), the following additional configuration would be mandatory:

### Navigation
`Repository → Settings → Branches → Branch protection rules → [main rule]`

### Required Settings (ENABLE)
* **Require status checks to pass before merging**
  * Search and select the relevant CI workflows (e.g., `build`, `test`, `lint`).
  * **Require branches to be up to date before merging**: ENABLED (Ensures tests run against the latest `main`).

---

## 5. Expected End-State (Verification Checklist)

After configuration, all of the following must be true:

* ❌ `git push origin main` is rejected
* ✅ All changes reach `main` via Pull Requests only
* ✅ Non-admin users must obtain at least 1 approval
* ✅ Admin users can merge without requesting review
* ✅ Merge button only shows `Squash and merge`
* ✅ Each merged PR produces exactly **one commit** in `main`

---

## 6. Intent Summary (for LLM consumption)

> Configure a GitHub repository so that `main` is fully protected, accepts changes only through Pull Requests, enforces squash-only merges, blocks direct pushes, requires reviews for non-admins, and allows admins to bypass review requirements. The repository is documentation-only and does not use CI or status checks.

---

## Change Log

### Version 1.0.0 - 2025-12-18 - Initial version with comprehensive repository configuration guide
**Sources:**
- Mariano Blua
- Grok (xAI)

---

## End of Configuration

This setup represents a clean, minimal, and enforceable workflow suitable for documentation repositories and small teams.

