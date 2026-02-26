# KIT CONFIG — API

**Kit:** API
**Version:** 1.0
**Activates when:** PROJECT.md → Project Type = API / Backend Service

---

## Authority Hierarchy

```
1. constitution/SECURITY.xml     ← Supreme (never override)
2. constitution/QUALITY.xml      ← Quality standards
3. constitution/PROMPTING.xml    ← Communication methods
4. constitution/*.xml            ← Other laws
5. This Kit's PROMPTER.md        ← Discovery + requirements
6. This Kit's kit.config.md      ← Activation rules (this file)
7. This Kit's API_KIT.md         ← Patterns + checklists
8. user-input/seed/*.md          ← User's project context
```

**Rule:** Higher number never overrides lower number.

---

## Kit Contents

| File | Purpose |
|:-----|:--------|
| `PROMPTER.md` | How to discover requirements, what questions to ask |
| `API_KIT.md` | RESTful structure, auth, rate limiting, versioning, errors, pagination patterns |
| `kit.config.md` | This file — activation rules |
| `TRACKER.md` | Progress tracking for this kit |

---

## Activation Flow

```
1. User runs RUN.md or ignition prompt
2. AI loads constitution (mandatory)
3. AI reads user-input/seed/PROJECT.md
4. AI detects: Project Type = API / Backend Service
5. AI loads this kit:
   └── First: PROMPTER.md (discovery)
   └── Then: API_KIT.md (patterns)
6. PROMPTER.md drives the conversation
7. Build begins only when requirements table is complete
```

---

## Override Rules

| If this says... | But this says... | Winner |
|:----------------|:-----------------|:-------|
| API_KIT.md: REST endpoints | TECH_STACK.md: GraphQL | TECH_STACK.md |
| API_KIT.md: standard error format | INTERFACES.md: custom format | INTERFACES.md |
| Anything in this kit | SECURITY.xml | SECURITY.xml (always) |
| PROMPTER.md: ask versioning questions | User: "Skip that" | PROMPTER.md (requirements must be filled) |

---

## What This Kit Provides

The agent uses these patterns as starting points for:
- RESTful endpoint structure and naming
- Authentication pattern selection
- Rate limiting tier definitions
- API versioning strategy
- Error response format standardisation
- Pagination patterns
- HTTP status code usage
- Health check endpoint design
- Webhook signature and retry patterns
- Idempotency key implementation
- CORS configuration
- Monitoring and alerting requirements

---

## When NOT to Use This Kit

- Project type = Full-stack Web App → Use `saas/` kit
- Project type = Static Website → Use `website/` kit
- Project type = Automation workflow → Use `automation/` kit

---

*This config is read-only during build. Modify only between projects.*
