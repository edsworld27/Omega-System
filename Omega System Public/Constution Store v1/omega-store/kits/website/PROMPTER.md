# WEBSITE KIT — PROMPTER

**Purpose:** This file tells the AI how to gather requirements and ensure nothing is missed when building a website project.

**Authority:** Constitution > This Prompter > kit.config.md > WEBSITE_KIT.md patterns

---

## 1. ACTIVATION GATE

Before using this kit, verify:
- [ ] Constitution loaded (SECURITY.xml, QUALITY.xml, PROMPTING.xml, etc.)
- [ ] PROJECT.md read (user-input/seed/)
- [ ] Project type = Website confirmed
- [ ] plug-and-play/ scanned for existing assets

If any constitution file is missing → HALT. Load constitution first.

---

## 2. REQUIREMENTS TABLE

**Every row must have a value before build begins. If blank, AI must ask.**

| Requirement | Source | Status | Notes |
|:------------|:-------|:-------|:------|
| Project name | PROJECT.md | [ ] | |
| North star (singular goal) | PROJECT.md | [ ] | |
| Target audience | PROJECT.md or PERSONAS.md | [ ] | |
| Site type (Marketing / Blog / E-commerce / Portfolio) | PROJECT.md | [ ] | |
| Page count estimate | CONTENT.md or ask | [ ] | |
| Content ready? | Ask or plug-and-play/ | [ ] | Yes/No/Partial |
| Brand guidelines exist? | BRAND.md or plug-and-play/ | [ ] | |
| Tech stack decision | TECH_STACK.md or ask | [ ] | |
| Hosting preference | PROJECT.md or ask | [ ] | |
| Domain name | Ask | [ ] | |
| Analytics tool | Ask (default: GA4) | [ ] | |
| Cookie consent needed? | Ask (default: Yes if EU) | [ ] | |
| Launch deadline | CONSTRAINTS.md or ask | [ ] | |
| Budget tier | CONSTRAINTS.md or ask | [ ] | £0 / £500 / £5k+ |

---

## 3. DISCOVERY SEQUENCE

Use PROMPTING.xml methods. Ask in batches of 2-4 questions max.

### Batch 1: Core Identity
```
I've loaded your project seeds. Let me confirm a few things:

1. **Site type:** Is this primarily:
   - Marketing/Landing page
   - Blog/Content site
   - E-commerce/Shop
   - Portfolio/Showcase
   - Other (describe)

2. **Scale:** How many pages do you expect?
   - Small (1-5 pages)
   - Medium (6-15 pages)
   - Large (15+ pages)
```

### Batch 2: Content Status
```
About your content:

1. **Do you have existing content** (copy, images, brand assets)?
   - Yes, it's ready → Drop into plug-and-play/ or tell me the path
   - Partial — I have some
   - No — starting from scratch

2. **Brand guidelines?**
   - Yes (colors, fonts, logo defined)
   - No — need to establish
```

### Batch 3: Technical Preferences
```
Technical setup:

1. **Framework preference?**
   - Next.js (Recommended for most)
   - Astro (best for content-heavy)
   - Plain HTML/CSS
   - Other: ___

2. **Hosting?**
   - Vercel (Recommended)
   - Netlify
   - Self-hosted
   - No preference
```

### Batch 4: Launch Context
```
Final context:

1. **Launch deadline?** (date or "no rush")

2. **Any specific integrations needed?**
   - Contact form → where do submissions go?
   - Newsletter signup → which provider?
   - E-commerce → Stripe? Shopify?
   - CMS for content editing?
```

---

## 4. EVALUATION MATRIX

After discovery, score the project against WEBSITE_KIT.md requirements:

| Category | Required Items | Status |
|:---------|:---------------|:-------|
| **Pages** | Home, About, Contact minimum | [ ] |
| **SEO** | Title, meta, H1, alt text, sitemap, robots.txt | [ ] |
| **Performance** | LCP <2.5s, FID <100ms, CLS <0.1 | [ ] |
| **Accessibility** | Lighthouse ≥90 | [ ] |
| **Mobile** | Responsive breakpoints defined | [ ] |
| **Legal** | Privacy policy, Terms, Cookie consent | [ ] |
| **Analytics** | Tracking code, events, goals | [ ] |
| **Security** | SSL, headers, form validation | [ ] |

---

## 5. BUILD HANDOFF

Once requirements table is complete:

1. **Generate sitemap** from WEBSITE_KIT.md template + user input
2. **Create component list** for tech stack
3. **Output PRD** using constitution/blueprints/PRD.md
4. **Begin phase tasks** from preproduction/ → production/ → testing/

---

## 6. NOTHING LEFT BEHIND

Before ANY code is written, this prompter ensures:
- Every seed gap is filled by asking
- Every kit requirement is evaluated
- Every constitution rule is respected
- Every deliverable is tracked

**If a requirement is unclear → ASK. Never assume.**

---

## 7. KIT-SPECIFIC PROMPTING RULES

From PROMPTING.xml, apply to website context:

1. **Visual proposals:** Describe layouts before building (Hero: full-width image, centered headline...)
2. **Chunked delivery:** Build page-by-page, not all at once
3. **Checkpoint after each page:** "Home page complete. Review before I continue?"
4. **No placeholder content:** Real copy or clear [PLACEHOLDER: describe what goes here]
5. **Mobile-first always:** Start with mobile layout in all component descriptions

---

*This prompter auto-activates when kit.config.md conditions are met.*
