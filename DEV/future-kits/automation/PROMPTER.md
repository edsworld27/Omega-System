# AUTOMATION KIT — PROMPTER

**Purpose:** This file tells the AI how to gather requirements and ensure nothing is missed when building an Automation / Workflow project.

**Authority:** Constitution > This Prompter > kit.config.md > AUTOMATION_KIT.md patterns

---

## 1. ACTIVATION GATE

Before using this kit, verify:
- [ ] Constitution loaded (SECURITY.xml, QUALITY.xml, PROMPTING.xml, etc.)
- [ ] PROJECT.md read (user-input/seed/)
- [ ] Project type = Automation confirmed
- [ ] plug-and-play/ scanned for existing assets

If any constitution file is missing → HALT. Load constitution first.

---

## 2. REQUIREMENTS TABLE

**Every row must have a value before build begins. If blank, AI must ask.**

| Requirement | Source | Status | Notes |
|:------------|:-------|:-------|:------|
| Project name | PROJECT.md | [ ] | |
| North star (singular goal) | PROJECT.md | [ ] | |
| Automation platform | TECH_STACK.md or ask | [ ] | n8n / Make / Zapier / Custom |
| Trigger type | Ask | [ ] | Webhook / Schedule / Event |
| Data sources | Ask | [ ] | |
| Data destinations | Ask | [ ] | |
| Error handling | Ask | [ ] | Retry / Alert / Fail |
| Frequency | Ask | [ ] | Real-time / Hourly / Daily |
| Volume expected | Ask | [ ] | |
| Credentials needed | Ask | [ ] | List services |
| Monitoring | Ask | [ ] | |
| Launch deadline | CONSTRAINTS.md or ask | [ ] | |
| Budget tier | CONSTRAINTS.md or ask | [ ] | |

---

## 3. DISCOVERY SEQUENCE

*To be completed — use PROMPTING.xml methods, ask in batches of 2-4 questions.*

### Batch 1: Workflow Purpose
```
[Questions about what gets automated, trigger events]
```

### Batch 2: Data Flow
```
[Questions about sources, transformations, destinations]
```

### Batch 3: Reliability
```
[Questions about error handling, retries, monitoring]
```

### Batch 4: Launch Context
```
[Questions about timeline, testing, credentials]
```

---

## 4. EVALUATION MATRIX

*To be completed — score project against AUTOMATION_KIT.md requirements.*

| Category | Required Items | Status |
|:---------|:---------------|:-------|
| **Triggers** | | [ ] |
| **Data flow** | | [ ] |
| **Error handling** | | [ ] |
| **Logging** | | [ ] |
| **Credentials** | | [ ] |
| **Testing** | | [ ] |

---

## 5. BUILD HANDOFF

Once requirements table is complete:

1. **Generate workflow diagram**
2. **List all credentials needed**
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

*To be completed — Automation-specific prompting guidance.*

---

*This prompter auto-activates when kit.config.md conditions are met.*
