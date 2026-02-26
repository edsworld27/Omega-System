# SAAS KIT — PROMPTER

**Purpose:** This file tells the AI how to gather requirements and ensure nothing is missed when building a SaaS/Web Application project.

**Authority:** Constitution > This Prompter > kit.config.md > SAAS_KIT.md patterns

---

## 1. ACTIVATION GATE

Before using this kit, verify:
- [ ] Constitution loaded (SECURITY.xml, QUALITY.xml, PROMPTING.xml, etc.)
- [ ] PROJECT.md read (user-input/seed/)
- [ ] Project type = Web Application / SaaS confirmed
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
| Core user problem | PROJECT.md | [ ] | |
| Auth method | TECH_STACK.md or ask | [ ] | |
| Database choice | TECH_STACK.md or ask | [ ] | |
| Pricing model | Ask | [ ] | Free / Freemium / Paid |
| Multi-tenant? | Ask | [ ] | Yes / No |
| Tech stack | TECH_STACK.md or ask | [ ] | |
| Hosting | PROJECT.md or ask | [ ] | |
| Payment processor | Ask | [ ] | Stripe / None / Other |
| Launch deadline | CONSTRAINTS.md or ask | [ ] | |
| Budget tier | CONSTRAINTS.md or ask | [ ] | |

---

## 3. DISCOVERY SEQUENCE

*To be completed — use PROMPTING.xml methods, ask in batches of 2-4 questions.*

### Batch 1: Core Product
```
[Questions about what the product does, who it's for]
```

### Batch 2: Technical Architecture
```
[Questions about auth, database, API structure]
```

### Batch 3: Business Model
```
[Questions about pricing, billing, user tiers]
```

### Batch 4: Launch Context
```
[Questions about timeline, MVP scope, integrations]
```

---

## 4. EVALUATION MATRIX

*To be completed — score project against SAAS_KIT.md requirements.*

| Category | Required Items | Status |
|:---------|:---------------|:-------|
| **Auth** | | [ ] |
| **Database** | | [ ] |
| **API** | | [ ] |
| **Security** | | [ ] |
| **Billing** | | [ ] |
| **Monitoring** | | [ ] |

---

## 5. BUILD HANDOFF

Once requirements table is complete:

1. **Generate architecture diagram**
2. **Create API contract** (INTERFACES.md)
3. **Output PRD** using constitution/blueprints/PRD.md
4. **Begin phase tasks**

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

*To be completed — SaaS-specific prompting guidance.*

---

*This prompter auto-activates when kit.config.md conditions are met.*
