# TASK: Import Brand Assets
**Kit:** Website
**Phase:** Pre-Production
**Portable:** Yes

---

## FOR THE USER

Drop your brand assets into `user-input/plug-and-play/`:
- Brand guidelines PDF
- Logo files (SVG, PNG)
- Color palette
- Font files or names
- Tone of voice document

Then tell your AI: **"Execute BRAND_IMPORT.task.md"**

---

## FOR THE AI

### CONTEXT
The user has brand assets in plug-and-play. Your job is to:
1. Scan what's there
2. Extract brand information
3. Generate or update BRAND.md seed file

### STEPS

1. **Scan plug-and-play**
   - List all files in `user-input/plug-and-play/`
   - Identify brand-related files (PDFs, images, docs)

2. **Extract brand information**
   - Primary colors (hex codes)
   - Secondary colors
   - Typography (font names, weights)
   - Logo variations
   - Tone of voice keywords
   - Any brand rules or don'ts

3. **Generate BRAND.md**
   - Create or update `user-input/seed/BRAND.md`
   - Use the standard seed format
   - Include all extracted information

4. **Report findings**
   - What was imported
   - What's missing or unclear
   - Recommendations

### OUTPUT

Present a summary:
```
BRAND IMPORT COMPLETE

Imported:
- [List of what was extracted]

Updated:
- user-input/seed/BRAND.md

Missing (consider adding):
- [List of gaps]

Recommendations:
- [Any suggestions]
```

### SUCCESS CRITERIA
- [ ] All brand files in plug-and-play were scanned
- [ ] BRAND.md was created or updated
- [ ] User can see what was imported
