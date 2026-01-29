# Configuration Template

**Purpose:** This template provides a standardized structure for configuration-focused documents in `/docs/platforms/`. Use this template for step-by-step setup guides, governance configurations, and platform-specific settings.

---

```yaml
---
title: [Document Title]
purpose: [Brief purpose statement explaining the configuration objective]
audience: [[architect, developer]]  # Select appropriate roles
scope: [Specific scope of what this configuration covers]
last_updated: YYYY-MM-DD
version: 1.0.0
keywords: [[keyword1, keyword2, keyword3]]
related_docs: [[path/to/related.md]]
---
```

# [Document Title]

## Objective

[Brief statement of what this configuration achieves. Include success criteria.]

This document is intended to be followed **step by step** by both humans and LLMs to reproduce the exact same configuration.

---

## How to Use This Document

[Explain how to use this document - as a checklist, verification guide, or implementation reference. Mention any prerequisites or assumptions.]

---

## Prerequisites and Assumptions

[List any prerequisites, system requirements, or assumptions:]

* [Prerequisite 1]
* [Prerequisite 2]
* [Assumption 1]
* [Assumption 2]

---

## 1. [Configuration Section Name]

### Navigation

[Provide navigation path or UI location]
`[Path/Location → Submenu → Settings]`

### Required Settings (ENABLE)

* **[Setting Name]**
  * [Detailed configuration instructions]
  * [Additional parameters or options]

* **[Another Setting]**
  * [Configuration details]

### Optional Settings (RECOMMENDED)

* **[Optional Setting]**
  * [Why this is recommended]
  * [Configuration details]

---

## 2. [Next Configuration Section]

### Navigation

[Navigation details]

### [Settings Category]

* **[Setting Name]**
  * [Configuration instructions]

---

## Verification Steps

After completing all configuration steps, verify the setup:

### [Verification Method 1]

1. [Step-by-step verification instructions]
2. **Expected Result:** [What should happen if configured correctly]

### [Verification Method 2]

1. [Verification steps]
2. **Expected Result:** [Expected outcome]

---

## Troubleshooting

### Common Issues

**Issue: [Common Problem]**
- **Symptoms:** [What indicates this problem]
- **Solution:** [Step-by-step resolution]

**Issue: [Another Problem]**
- **Symptoms:** [Symptoms]
- **Solution:** [Solution steps]

---

## Security Considerations

[Document any security implications or best practices related to this configuration.]

---

## Related Documentation

* [Link to related documents]
* [Additional resources]

---

## Change Log

### Version 1.0.0 - YYYY-MM-DD - Initial version
**Sources:**
- [Your Name]
- [AI Assistant Name, if applicable]

---

*This configuration ensures [brief statement of compliance or governance objective].*