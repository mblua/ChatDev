# LM-Readiness Validation Checklist

## Overview

This checklist validates technical documentation assets against the LLM-ready documentation framework established in the repository. Use this checklist during document creation, review, and maintenance to ensure compliance with all framework requirements.

**Note:** Files of type `AGENTS.md` are exempt from metadata and change log requirements as they are internal agent context.

## Quick Reference

**Scoring System:**
- ✅ **Pass**: Meets requirement
- ❌ **Fail**: Does not meet requirement
- ⚠️ **Warning**: Partial compliance or recommendation

**Validation Categories:**
1. [Metadata Standards](#1-metadata-standards)
2. [Content Structure](#2-content-structure)
3. [Diagram Compliance](#3-diagram-compliance)
4. [Document Size Compliance](#4-document-size-compliance)
5. [Best Practices](#5-best-practices)
6. [Directory Compliance](#6-directory-compliance)

---

## 1. Metadata Standards

### YAML Frontmatter Completeness
- [ ] **Document has YAML frontmatter** (starts with `---`)
- [ ] **Title field present and descriptive**
- [ ] **Purpose field present** (1-2 sentences explaining document value)
- [ ] **Audience field present** (array with valid roles: architect, developer, presales, executive, operator, analyst)
- [ ] **Scope field present** (defines document boundaries)
- [ ] **Last_updated field present** (YYYY-MM-DD format)
- [ ] **Version field present** (semantic versioning: major.minor.patch)
- [ ] **Keywords field present** (array of 3+ searchable terms)
- [ ] **Related_docs field present** (array of relative paths, can be empty)

### Metadata Quality
- [ ] **Title accurately reflects content**
- [ ] **Purpose statement is clear and actionable**
- [ ] **Audience roles are appropriate for content**
- [ ] **Scope definition matches actual document coverage**
- [ ] **Keywords are relevant and comprehensive**
- [ ] **Related document links are valid paths**

---

## 2. Content Structure

### Heading Hierarchy
- [ ] **Uses proper heading levels** (# ## ### #### - no skips)
- [ ] **Consistent heading structure throughout**
- [ ] **Logical information hierarchy** (most important info highest)
- [ ] **No orphaned headings** (every subheading has parent context)

### Document Organization
- [ ] **Clear introduction or objective section**
- [ ] **Logical flow of information**
- [ ] **Appropriate section breaks**
- [ ] **Conclusion or summary section** (for longer documents)

### Readability
- [ ] **Short, declarative sentences** (< 25 words average)
- [ ] **Active voice preferred over passive**
- [ ] **Consistent terminology and naming**
- [ ] **Clear transitions between sections**

---

## 3. Diagram Compliance

### Mermaid-Only Rule
- [ ] **No image files referenced** (*.png, *.jpg, *.svg external files)
- [ ] **All diagrams use Mermaid syntax**
- [ ] **Diagrams are inline** (not referenced as separate files)
- [ ] **Mermaid syntax is valid** (can render without errors)

### Diagram Quality
- [ ] **Diagrams enhance understanding** (not decorative)
- [ ] **Appropriate diagram types** (flowchart, sequence, mindmap, etc.)
- [ ] **Clear labeling and descriptions**
- [ ] **Diagrams support content** (contextually placed)

### Diagram Accessibility
- [ ] **Text-based descriptions provided** (for screen readers)
- [ ] **Color-independent understanding** (works in black/white)
- [ ] **Logical flow direction** (left-to-right, top-to-bottom)

---

## 4. Document Size Compliance

### Size Limits (Critical)
- [ ] **Document does not exceed 12,000 tokens** (~800 lines)
- [ ] **No single section exceeds 3,000 tokens** (~200 lines)
- [ ] **If over limit, document has been split** into focused sub-documents

### Split Indicators
- [ ] **No unrelated topics** combined in single document
- [ ] **Sections could not stand alone** as independent guides
- [ ] **Document has single clear purpose** (not multiple guides merged)

### Token Estimation Reference

| Lines | Estimated Tokens | Status |
|-------|------------------|--------|
| < 500 | ~7,500 | ✅ Optimal |
| 500-800 | 7,500-12,000 | ✅ Acceptable |
| 800-1000 | 12,000-15,000 | ⚠️ Consider splitting |
| > 1000 | > 15,000 | ❌ Must split |

### Why This Matters
- **RAG Performance**: Smaller documents create more coherent chunks
- **LLM Context**: Fits better in context windows
- **Maintainability**: Easier to update focused documents
- **Navigation**: Humans find information faster

---

## 5. Best Practices

### Content Quality
- [ ] **Examples provided** (code, configuration, or scenarios)
- [ ] **Practical focus** (actionable information)
- [ ] **Current and accurate information**
- [ ] **No customer-specific data**

### Structure and Navigation
- [ ] **Table of contents** (for documents > 5 sections)
- [ ] **Clear section navigation**
- [ ] **Internal cross-references** (link to related sections)
- [ ] **External cross-references** (link to other documents)

### Language and Style
- [ ] **Professional, technical tone**
- [ ] **Consistent formatting** (code blocks, lists, emphasis)
- [ ] **Spelling and grammar correct**
- [ ] **Industry-standard terminology**

---

## 6. Directory Compliance

### Correct Placement
- [ ] **Document in appropriate directory** (/docs/compendiums, /platforms, etc.)
- [ ] **Follows directory naming conventions**
- [ ] **File naming follows kebab-case** (word-word-word.md)

### Directory-Specific Requirements

#### For `/docs/compendiums/`:
- [ ] **Comprehensive coverage** (technical depth appropriate)
- [ ] **Multi-audience support** (appendices for different roles)
- [ ] **Business context included** (ROI, benefits)
- [ ] **Citation system present**

#### For `/docs/platforms/`:
- [ ] **Step-by-step instructions**
- [ ] **Verification checklists**
- [ ] **Configuration focus**
- [ ] **Security considerations**

#### For `/docs/patterns/`:
- [ ] **Problem-solution format**
- [ ] **Code examples included**
- [ ] **Trade-offs documented**
- [ ] **When to use/not use clearly stated**

#### For `/docs/tools/`:
- [ ] **Installation instructions**
- [ ] **Configuration examples**
- [ ] **Usage workflows**
- [ ] **Integration guidance**

---

## Automated Validation

### Syntax Checks
- [ ] **Markdown syntax valid** (no broken links, formatting)
- [ ] **YAML frontmatter parseable**
- [ ] **Code blocks have language tags**
- [ ] **No broken internal links**

### Consistency Checks
- [ ] **Terminology consistent throughout**
- [ ] **Formatting consistent** (headings, lists, emphasis)
- [ ] **Cross-references accurate**
- [ ] **Version information current**

---

## Review Process

### Pre-Commit Validation
- [ ] **Self-review completed** using this checklist
- [ ] **Peer review requested** for complex changes
- [ ] **Automated checks passed** (if available)

### Post-Commit Validation
- [ ] **Document renders correctly** in repository viewer
- [ ] **Links functional** in rendered output
- [ ] **Diagrams display properly**
- [ ] **Mobile-friendly formatting**

---

## Scoring and Compliance

### Compliance Levels
- **100% Compliant**: All requirements met, no warnings
- **90-99% Compliant**: All critical requirements met, minor issues
- **80-89% Compliant**: Major requirements met, some gaps
- **<80% Compliant**: Requires revision before acceptance

### Critical Requirements (Must Pass)
- YAML frontmatter complete and valid
- Mermaid-only diagrams (no image files)
- Customer-agnostic content
- Correct directory placement
- Basic readability and structure
- **Document size under 12,000 tokens (~800 lines)**

### Recommended Improvements
- Enhanced examples and code samples
- More comprehensive cross-references
- Additional audience-specific content
- Performance and testing guidance

---

## Validation Tools

### Manual Tools
- **Markdown linters** (markdownlint, remark)
- **YAML validators** (yamllint)
- **Spell checkers** (aspell, codespell)

### Automated Scripts (Future)
- **Frontmatter validator** (checks required fields)
- **Mermaid syntax checker** (validates diagram code)
- **Link checker** (validates internal/external references)
- **Structure analyzer** (heading hierarchy, content flow)

---

*This checklist ensures all documentation maintains the highest standards of LLM-readiness and human usability.*