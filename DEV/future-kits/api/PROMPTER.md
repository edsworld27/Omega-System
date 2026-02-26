# API KIT — PROMPTER

**Purpose:** This file tells the AI how to gather requirements and ensure nothing is missed when building an API / Backend Service project.

**Authority:** Constitution > This Prompter > kit.config.md > API_KIT.md patterns

---

## 1. ACTIVATION GATE

Before using this kit, verify:
- [ ] Constitution loaded (SECURITY.xml, QUALITY.xml, PROMPTING.xml, etc.)
- [ ] PROJECT.md read (user-input/seed/)
- [ ] Project type = API / Backend Service confirmed
- [ ] plug-and-play/ scanned for existing assets

If any constitution file is missing → HALT. Load constitution first.

---

## 2. REQUIREMENTS TABLE

**Every row must have a value before build begins. If blank, AI must ask.**

| Requirement | Source | Status | Notes |
|:------------|:-------|:-------|:------|
| Project name | PROJECT.md | [ ] | |
| North star (singular goal) | PROJECT.md | [ ] | |
| API consumers | PROJECT.md or ask | [ ] | Internal / Public / Both |
| API style | Ask | [ ] | REST / GraphQL / gRPC |
| Auth method | TECH_STACK.md or ask | [ ] | API Key / OAuth / JWT |
| Database | TECH_STACK.md or ask | [ ] | |
| Rate limiting requirements | Ask | [ ] | |
| Versioning strategy | Ask | [ ] | URL / Header / None |
| Documentation format | Ask | [ ] | OpenAPI / GraphQL SDL |
| Tech stack | TECH_STACK.md or ask | [ ] | |
| Hosting | PROJECT.md or ask | [ ] | |
| Launch deadline | CONSTRAINTS.md or ask | [ ] | |
| Budget tier | CONSTRAINTS.md or ask | [ ] | |

---

## 3. DISCOVERY SEQUENCE

*To be completed — use PROMPTING.xml methods, ask in batches of 2-4 questions.*

### Batch 1: API Purpose
```
[Questions about what the API does, who consumes it]
```

### Batch 2: Technical Design
```
[Questions about endpoints, data models, auth]
```

### Batch 3: Operations
```
[Questions about rate limits, monitoring, versioning]
```

### Batch 4: Launch Context
```
[Questions about timeline, documentation, testing]
```

---

## 4. EVALUATION MATRIX

*To be completed — score project against API_KIT.md requirements.*

| Category | Required Items | Status |
|:---------|:---------------|:-------|
| **Endpoints** | | [ ] |
| **Auth** | | [ ] |
| **Validation** | | [ ] |
| **Error handling** | | [ ] |
| **Documentation** | | [ ] |
| **Testing** | | [ ] |

---

## 5. BUILD HANDOFF

Once requirements table is complete:

1. **Generate INTERFACES.md** (API contract)
2. **Create endpoint list**
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

*To be completed — API-specific prompting guidance.*

---

*This prompter auto-activates when kit.config.md conditions are met.*
