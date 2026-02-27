# TASK: Import Wireframes & Mockups
**Kit:** Website
**Phase:** Pre-Production
**Portable:** Yes

---

## FOR THE USER

Drop your wireframes/mockups into `user-input/plug-and-play/`:
- Figma exports (PNG, PDF)
- Lovable/v0/AI Studio exports
- Sketch files
- Hand-drawn scans
- Screenshot references

Then tell your AI: **"Execute WIREFRAME_IMPORT.task.md"**

---

## FOR THE AI

### CONTEXT
The user has wireframes or mockups in plug-and-play. Your job is to:
1. Analyze the visual structure
2. Extract page layouts and components
3. Generate a sitemap and component inventory

### STEPS

1. **Scan plug-and-play**
   - List all visual files (PNG, PDF, JPG, etc.)
   - If there are code exports (HTML, React), note those too

2. **Analyze structure**
   - Identify distinct pages/screens
   - Identify repeated components (nav, footer, cards, etc.)
   - Note layout patterns (grid, hero sections, etc.)

3. **Generate sitemap**
   - List all pages with hierarchy
   - Note which pages share layouts

4. **Generate component inventory**
   - List all unique components
   - Note variations (e.g., "Card - with image", "Card - text only")

5. **If code exists**
   - Analyze the exported code
   - Note framework used
   - Identify what's reusable vs. needs rebuilding

### OUTPUT

Present a summary:
```
WIREFRAME IMPORT COMPLETE

Pages identified:
- Homepage
- About
- [etc.]

Components identified:
- Navigation (sticky, with dropdown)
- Hero (full-width, with CTA)
- [etc.]

Layout patterns:
- [Describe common patterns]

Code export (if any):
- Framework: [e.g., React, HTML]
- Reusable: [what can be kept]
- Needs work: [what needs rebuilding]

Recommendations:
- [Suggestions for build order]
```

### SUCCESS CRITERIA
- [ ] All visual files analyzed
- [ ] Sitemap generated
- [ ] Component inventory created
- [ ] User understands what was imported
