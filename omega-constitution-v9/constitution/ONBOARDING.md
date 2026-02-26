# ONBOARDING — Structured Interview Flow

**This is the MANDATORY first interaction when a user starts.**

The AI MUST follow this exact sequence. No skipping. No deviation.

---

## STEP 1: Mode Selection (ALWAYS FIRST)

```
═══════════════════════════════════════════════════════════
  OMEGA CONSTRUCTOR — SELECT MODE
═══════════════════════════════════════════════════════════

  How would you like to work?

  1. FULL DISCOVERY — I'll guide you through everything
     (Best for: new projects, exploring ideas)

  2. QUICK START — You already filled the seed files
     (Best for: pre-planned projects)

  3. LITE MODE — Minimal questions, simple build
     (Best for: small models, quick prototypes)

  4. JUST BUILD — Skip to code, you know what you want
     (Best for: experienced users, clear specs)

  Reply with: 1, 2, 3, or 4
═══════════════════════════════════════════════════════════
```

**WAIT for answer before proceeding.**

---

## STEP 2: Project Type (After mode selected)

```
═══════════════════════════════════════════════════════════
  WHAT ARE YOU BUILDING?
═══════════════════════════════════════════════════════════

  A. WEBSITE — Marketing site, landing page, portfolio
  B. WEB APP — SaaS, dashboard, user accounts
  C. API — Backend service, REST/GraphQL
  D. AUTOMATION — Workflows, integrations, scripts
  E. OTHER — Tell me what

  Reply with: A, B, C, D, or E
═══════════════════════════════════════════════════════════
```

**This triggers kit activation.** A=website kit, B=saas kit, C=api kit, D=automation kit.

**WAIT for answer before proceeding.**

---

## STEP 3: Existing Work Detection (Critical)

```
═══════════════════════════════════════════════════════════
  DO YOU HAVE EXISTING WORK?
═══════════════════════════════════════════════════════════

  1. STARTING FRESH — Nothing built yet

  2. HAVE FRONTEND — UI/designs exist, need backend

  3. HAVE BACKEND — API exists, need frontend

  4. HAVE BOTH — Existing project, need help continuing

  5. HAVE DESIGNS — Wireframes/mockups, no code yet

  Reply with: 1, 2, 3, 4, or 5
═══════════════════════════════════════════════════════════
```

**Based on answer:**
- 1 → Fresh build flow
- 2 → Load FRONTEND_ONLY.md context
- 3 → Load BACKEND_ONLY.md context
- 4 → Load IMPORT_PROJECT.md context
- 5 → Fresh build with design assets

**WAIT for answer before proceeding.**

---

## STEP 4: Quick Context Gather

```
═══════════════════════════════════════════════════════════
  QUICK CONTEXT
═══════════════════════════════════════════════════════════

  In 1-2 sentences, what's the core purpose?

  Example: "A landing page for my SaaS that captures emails"
  Example: "An API that processes payments for my app"
  Example: "A dashboard where users manage their projects"

═══════════════════════════════════════════════════════════
```

**WAIT for answer before proceeding.**

---

## STEP 5: Handoff to Kit PROMPTER

After Steps 1-4, the activated kit's PROMPTER.md takes over with domain-specific questions.

```
═══════════════════════════════════════════════════════════
  GOT IT. HERE'S WHAT I KNOW:
═══════════════════════════════════════════════════════════

  Mode: [Full Discovery / Quick Start / Lite / Just Build]
  Type: [Website / Web App / API / Automation / Other]
  Starting Point: [Fresh / Have Frontend / Have Backend / etc.]
  Purpose: [Their 1-2 sentence description]

  Kit Activated: [website / saas / api / automation / none]

  Now I'll ask specific questions for your project type.
═══════════════════════════════════════════════════════════
```

Then proceed to kit's PROMPTER.md questions.

---

## Mode-Specific Behavior

### If FULL DISCOVERY (Mode 1)
- Ask all questions from kit PROMPTER
- Fill seeds as user answers
- Validate completeness before building

### If QUICK START (Mode 2)
- Read existing seeds
- Only ask about blanks/placeholders
- Validate and confirm understanding

### If LITE MODE (Mode 3)
- Ask only: What? Tech stack? First feature?
- Skip detailed discovery
- Build incrementally

### If JUST BUILD (Mode 4)
- Skip to: "What do you want me to build first?"
- Minimal questions, maximum action
- Still follow security rules

---

## Rules

1. **Never skip Step 1** — Mode selection is mandatory
2. **Never skip Step 3** — Existing work detection prevents wasted effort
3. **Always confirm understanding** — Show summary before building
4. **One question at a time** — Don't overwhelm with multiple questions
5. **Wait for answers** — Don't assume or proceed without response

---

## Anti-Patterns

- ❌ Asking 5 questions at once
- ❌ Assuming they're starting fresh
- ❌ Skipping to code without knowing context
- ❌ Ignoring that they have existing work
- ❌ Using the wrong kit for their project type

---

*This flow ensures every user gets the right experience from the first message.*
