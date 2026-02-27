# TASK: Content Audit
**Kit:** Website
**Phase:** Pre-Production
**Portable:** Yes

---

## FOR THE USER

This task audits your existing content to understand what you have and what you need.

Options:
1. **Drop content files** into `preproduction/drop-zone/` (docs, spreadsheets, existing site export)
2. **Provide a URL** to your existing site
3. **Describe verbally** what content exists

Then tell your AI: **"Execute CONTENT_AUDIT.task.md"**

---

## FOR THE AI

### CONTEXT
The user needs a content audit before building. Your job is to:
1. Inventory existing content
2. Identify gaps
3. Create a content plan

### STEPS

1. **Gather content sources**
   - Check drop-zone for content files
   - Ask if there's an existing site URL to crawl
   - Ask what content exists in their head/notes

2. **Create content inventory**
   For each page, document:
   - Headline/title
   - Body copy (exists / needs writing / needs editing)
   - Images (exists / needs sourcing)
   - CTAs (defined / not defined)
   - Meta description (exists / needs writing)

3. **Identify content gaps**
   - Pages with no content
   - Pages with placeholder content
   - Missing images
   - Missing SEO elements

4. **Create content plan**
   - What needs to be written
   - What needs to be edited
   - What needs to be sourced (images, videos)
   - Priority order

### OUTPUT

Present a summary:
```
CONTENT AUDIT COMPLETE

Content inventory:
| Page | Headline | Body | Images | CTA | Meta |
|------|----------|------|--------|-----|------|
| Homepage | ✓ | Needs edit | 3/5 | ✓ | ✗ |
| About | ✓ | ✓ | 0/2 | ✗ | ✗ |
| [etc.] | | | | | |

Gaps identified:
- [List of missing content]

Content plan:
1. [Priority 1 - what to create first]
2. [Priority 2]
3. [etc.]

Estimated effort:
- Copy: [X pages need writing]
- Images: [X images need sourcing]
- SEO: [X meta descriptions needed]
```

### SUCCESS CRITERIA
- [ ] All existing content inventoried
- [ ] Gaps clearly identified
- [ ] Content plan created with priorities
- [ ] User knows what work remains
