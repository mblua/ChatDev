# Agent Context: /indexes

## Purpose

Navigation indexes for discovering documentation by various dimensions. These files help users and LLMs find relevant content quickly.

## Agent Responsibilities

1. **Accuracy**: Indexes must reflect actual content in the repository
2. **Freshness**: Update indexes when documents are added, moved, or removed
3. **Links**: All links must be valid relative paths
4. **Automation**: Consider automating index generation when possible

## Index Types

| Index | Purpose | Update Trigger |
|-------|---------|----------------|
| `by-technology.md` | Find docs by technology stack | New technology documented |
| `by-audience.md` | Find docs by target role | Document audience changes |
| `by-topic.md` | Hierarchical topic navigation | New topic or structure change |

## Index Format

All indexes should follow this format:

```markdown
## [Category]

### [Subcategory]

- [Document Title](../relative/path.md) - Brief description
```

## Maintenance Rules

### When to Update Indexes

| Event | Action |
|-------|--------|
| New document added | Add entry to relevant indexes |
| Document moved | Update path in all indexes |
| Document deleted | Remove from all indexes |
| Metadata changed | Update if affects categorization |

### Validation Checklist

Before committing index changes:

- [ ] All links are valid relative paths
- [ ] All links point to existing files
- [ ] Descriptions match document purpose
- [ ] No duplicate entries
- [ ] Alphabetical ordering within sections

## Automation Opportunities

Consider scripts to auto-generate indexes from:

- Frontmatter metadata extraction
- Directory structure scanning
- `technology_stack` field aggregation
- `audience` field grouping

## Cross-Index Consistency

A document may appear in multiple indexes:

- `by-technology.md`: Listed under its primary technology
- `by-audience.md`: Listed under each audience in its metadata
- `by-topic.md`: Listed under its topic category

Ensure all index entries for the same document have consistent:
- File path
- Brief description (can be tailored to index context)

