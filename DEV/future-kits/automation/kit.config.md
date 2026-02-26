# KIT CONFIG — Automation

**Kit:** Automation
**Version:** 1.0
**Activates when:** PROJECT.md → Project Type = Agentic Workflow / Automation

---

## Authority Hierarchy

```
1. constitution/SECURITY.xml     ← Supreme (never override)
2. constitution/QUALITY.xml      ← Quality standards
3. constitution/PROMPTING.xml    ← Communication methods
4. constitution/*.xml            ← Other laws
5. This Kit's PROMPTER.md        ← Discovery + requirements
6. This Kit's kit.config.md      ← Activation rules (this file)
7. This Kit's AUTOMATION_KIT.md  ← Patterns + checklists
8. user-input/seed/*.md          ← User's project context
```

**Rule:** Higher number never overrides lower number.

---

## Kit Contents

| File | Purpose |
|:-----|:--------|
| `PROMPTER.md` | How to discover requirements, what questions to ask |
| `AUTOMATION_KIT.md` | Workflow architecture, triggers, error handling, retry patterns |
| `kit.config.md` | This file — activation rules |
| `TRACKER.md` | Progress tracking for this kit |

---

## Activation Flow

```
1. User runs RUN.md or ignition prompt
2. AI loads constitution (mandatory)
3. AI reads user-input/seed/PROJECT.md
4. AI detects: Project Type = Agentic Workflow / Automation
5. AI loads this kit:
   └── First: PROMPTER.md (discovery)
   └── Then: AUTOMATION_KIT.md (patterns)
6. PROMPTER.md drives the conversation
7. Build begins only when requirements table is complete
```

---

## Override Rules

| If this says... | But this says... | Winner |
|:----------------|:-----------------|:-------|
| AUTOMATION_KIT.md: use n8n | TECH_STACK.md: use Make | TECH_STACK.md |
| AUTOMATION_KIT.md: 3 retry attempts | AGENTS.md: 5 retries | AGENTS.md |
| Anything in this kit | SECURITY.xml | SECURITY.xml (always) |
| PROMPTER.md: ask trigger questions | User: "Skip that" | PROMPTER.md (requirements must be filled) |

---

## What This Kit Provides

The agent uses these patterns as starting points for:
- Workflow architecture (trigger → validate → process → output → log)
- Platform-specific patterns (n8n, Make, Zapier, custom agents)
- Error handling and retry strategies
- Dead letter queue design
- Circuit breaker for workflows
- Data flow security from SECURITY.xml
- Scheduling best practices with jitter
- Monitoring and alerting requirements

---

## When NOT to Use This Kit

- Project type = Web Application → Use `saas/` kit
- Project type = Static Website → Use `website/` kit
- Project type = API only → Use `api/` kit

---

*This config is read-only during build. Modify only between projects.*
