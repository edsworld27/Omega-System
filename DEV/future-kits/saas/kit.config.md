# KIT CONFIG — SaaS

**Kit:** SaaS
**Version:** 1.0
**Activates when:** PROJECT.md → Project Type = Web Application / SaaS

---

## Authority Hierarchy

```
1. constitution/SECURITY.xml     ← Supreme (never override)
2. constitution/QUALITY.xml      ← Quality standards
3. constitution/PROMPTING.xml    ← Communication methods
4. constitution/*.xml            ← Other laws
5. This Kit's PROMPTER.md        ← Discovery + requirements
6. This Kit's kit.config.md      ← Activation rules (this file)
7. This Kit's SAAS_KIT.md        ← Patterns + checklists
8. user-input/seed/*.md          ← User's project context
```

**Rule:** Higher number never overrides lower number.

---

## Kit Contents

| File | Purpose |
|:-----|:--------|
| `PROMPTER.md` | How to discover requirements, what questions to ask |
| `SAAS_KIT.md` | Auth, billing, onboarding, dashboard, emails, multi-tenancy patterns |
| `kit.config.md` | This file — activation rules |
| `TRACKER.md` | Progress tracking for this kit |

---

## Activation Flow

```
1. User runs RUN.md or ignition prompt
2. AI loads constitution (mandatory)
3. AI reads user-input/seed/PROJECT.md
4. AI detects: Project Type = Web Application / SaaS
5. AI loads this kit:
   └── First: PROMPTER.md (discovery)
   └── Then: SAAS_KIT.md (patterns)
6. PROMPTER.md drives the conversation
7. Build begins only when requirements table is complete
```

---

## Override Rules

| If this says... | But this says... | Winner |
|:----------------|:-----------------|:-------|
| SAAS_KIT.md: use NextAuth | TECH_STACK.md: use Clerk | TECH_STACK.md |
| SAAS_KIT.md: 3 pricing tiers | PROJECT.md: 2 tiers | PROJECT.md |
| Anything in this kit | SECURITY.xml | SECURITY.xml (always) |
| PROMPTER.md: ask auth questions | User: "Skip auth setup" | PROMPTER.md (requirements must be filled) |

---

## What This Kit Provides

The agent uses these patterns as starting points for:
- Authentication and session management flow
- Auth security requirements (from SECURITY.xml)
- Billing and subscription tier structure
- Onboarding wizard design
- Dashboard layout patterns
- Transactional email templates
- Multi-tenancy data isolation
- Usage tracking and limit enforcement
- Settings page structure

---

## When NOT to Use This Kit

- Project type = Static Website → Use `website/` kit
- Project type = API only → Use `api/` kit
- Project type = Automation workflow → Use `automation/` kit

---

*This config is read-only during build. Modify only between projects.*
