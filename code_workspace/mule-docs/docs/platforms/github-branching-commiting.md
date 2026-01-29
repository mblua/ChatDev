---
title: GitHub Branching and Committing
purpose: Step-by-step guide for branching and committing changes using GitHub Desktop and command-line Git
audience: [architect, developer]
scope: Branch creation, committing changes, and basic Git workflows for GitHub repositories
last_updated: 2025-12-18
version: 1.0.0
keywords: [github, git, branching, committing, version-control, workflow]
related_docs: [docs/platforms/github-repo-config.md]
---

# GitHub Branching and Committing

## Objective

This guide explains how to create branches and commit changes to GitHub repositories using two methods:

* **GitHub Desktop**: A user-friendly graphical interface for Git operations
* **Command-line Git**: Direct terminal commands for advanced users and automation

Both methods ensure changes follow the repository's configured workflow (branches → Pull Requests → squash merge to main).

This document is intended to be followed **step by step** by both humans and LLMs to perform version control operations consistently.

---

## How to Use This Document

This guide serves as a practical reference for developers working with GitHub repositories. Choose the method that matches your workflow preference. The GitHub Desktop section is recommended for beginners, while the Git CLI section provides more control for experienced developers.

---

## Prerequisites and Assumptions

* Repository is configured following [GitHub Repository Configuration](docs/platforms/github-repo-config.md)
* You have write access to the repository
* GitHub Desktop is installed (for GUI method)
* Git is installed and configured (for CLI method)
* Repository is cloned locally

---

## Method 1: Using GitHub Desktop

GitHub Desktop provides a visual interface for Git operations. Download from: https://desktop.github.com/

### 1. Launch GitHub Desktop

1. Open GitHub Desktop application
2. Ensure your repository is selected from the repository list
3. Verify you're on the `main` branch (shown in the top toolbar)

### 2. Create a New Branch

1. Click **Branch** menu → **New branch**
2. Enter a descriptive branch name (e.g., `add-user-authentication`)
3. Ensure **Create branch based on 'main'** is selected
4. Click **Create branch**

### 3. Make Changes to Files

1. Open your code editor or IDE
2. Edit the necessary files in your local repository folder
3. Save all changes
4. Return to GitHub Desktop

### 4. Review and Stage Changes

1. GitHub Desktop will show changed files in the **Changes** tab
2. Review each changed file by clicking on it
3. Check the diff to ensure changes are correct
4. Select files to commit by checking the boxes next to filenames
5. **Optional**: Uncheck any files you don't want to commit

### 5. Commit Changes

1. Enter a clear, concise commit message in the summary field
   * Example: "Add user authentication endpoint"
   * Keep first line under 50 characters
2. Add detailed description if needed in the description field
3. Click **Commit to [branch-name]**

### 6. Publish and Create Pull Request

1. Click **Publish branch** (or **Push origin** if already published)
2. Click **Create Pull Request** button
3. GitHub will open in your browser with the PR form pre-filled
4. Add PR title and description
5. Click **Create pull request**

---

## Method 2: Using Command-Line Git

Command-line Git provides full control over version control operations. Official documentation: https://git-scm.com/

### 1. Verify Repository State

```bash
# Navigate to your repository
cd /path/to/your/repository

# Check current status
git status

# Ensure you're on main and up to date
git checkout main
git pull origin main
```

### 2. Create a New Branch

```bash
# Create and switch to new branch
git checkout -b feature/add-user-authentication

# Alternative: create branch then switch
git branch feature/add-user-authentication
git checkout feature/add-user-authentication
```

**Branch Naming Convention:**
* Use `feature/` prefix for new features
* Use `fix/` prefix for bug fixes
* Use `docs/` prefix for documentation changes
* Use lowercase with hyphens: `feature/user-login-validation`

### 3. Make Changes to Files

1. Open your code editor or IDE
2. Edit the necessary files
3. Save all changes

### 4. Check Changes

```bash
# See what files have changed
git status

# Review specific changes
git diff

# Review changes for specific file
git diff path/to/file.md
```

### 5. Stage Changes

```bash
# Stage all changes
git add .

# Stage specific files
git add path/to/file1.md path/to/file2.md

# Interactive staging
git add -p
```

### 6. Commit Changes

```bash
# Commit with message
git commit -m "Add user authentication endpoint

- Implement login validation
- Add password hashing
- Update API documentation"

# Alternative: commit with editor
git commit
```

**Commit Message Guidelines:**
* First line: Brief summary (under 50 characters)
* Blank line after summary
* Detailed description explaining what and why
* Use present tense: "Add feature" not "Added feature"

### 7. Push Branch and Create Pull Request

```bash
# Push branch to GitHub
git push -u origin feature/add-user-authentication

# Create Pull Request via GitHub web interface
# Or use GitHub CLI if installed:
gh pr create --title "Add user authentication" --body "Implementation details..."
```

---

## Verification Steps

After completing the branching and committing process, verify success:

### Branch Creation Verification

1. **GitHub Desktop**: Check that branch name appears in top toolbar
2. **Git CLI**: Run `git branch` and verify your branch is listed with asterisk
3. **GitHub Web**: Navigate to repository → Branches tab → Confirm new branch exists

### Commit Verification

1. **GitHub Desktop**: Check **History** tab shows your commit
2. **Git CLI**: Run `git log --oneline -5` and verify your commit appears
3. **GitHub Web**: Branch page shows commit history

### Pull Request Verification

1. Navigate to repository → Pull Requests tab
2. Confirm PR exists with correct title and branch
3. **Expected Result:** PR shows your commits and changes

---

## Troubleshooting

### Common Issues

**Issue: Cannot push to repository**
- **Symptoms:** Push fails with permission denied
- **Solution:** Verify you have write access; check if repository requires SSH keys

**Issue: Branch not appearing on GitHub**
- **Symptoms:** Branch exists locally but not remotely
- **Solution:** Push with `git push -u origin branch-name` or publish in GitHub Desktop

**Issue: Merge conflicts**
- **Symptoms:** Pull request shows conflicts
- **Solution:** Pull latest main changes and resolve conflicts before pushing

**Issue: Commit message not following convention**
- **Symptoms:** PR reviews request message changes
- **Solution:** Amend commit with `git commit --amend` and force push

---

## Best Practices

* **Branch frequently**: Create branches for each feature or fix
* **Commit regularly**: Make small, focused commits
* **Write clear messages**: Explain what and why, not just what
* **Review before committing**: Always check your changes with `git diff`
* **Pull before pushing**: Update your branch with latest main changes
* **Delete merged branches**: Clean up after PRs are merged

---

## Related Documentation

* [GitHub Repository Configuration](docs/platforms/github-repo-config.md) - Repository setup and governance
* [Official Git Documentation](https://git-scm.com/doc) - Complete Git reference
* [GitHub Desktop Documentation](https://docs.github.com/en/desktop) - GUI tool documentation

---

## Change Log

### Version 1.0.0 - 2025-12-18 - Initial version with GitHub Desktop and CLI methods
**Sources:**
- Mariano Blua
- Grok (xAI)

---

*This guide ensures consistent branching and committing practices across the development team.*