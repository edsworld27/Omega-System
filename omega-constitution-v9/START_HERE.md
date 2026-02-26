# START HERE — User Guide

**Omega Constitution Pack v9** — Build anything with AI, the right way.

---

## What This Does

1. **Security** — Rules the AI can't bypass (secrets, injection, validation)
2. **Quality** — Function before form, test what you build
3. **Completeness** — Nothing gets missed, requirements validated before building
4. **Flexibility** — Full guidance or skip to code, your choice

---

## Choose How You Work

### Decision Tree

```
Know exactly what to build?
├── YES → Want AI guidance anyway?
│         ├── YES → Full Discovery
│         └── NO  → Just Build
└── NO  → Small model (<32k context)?
          ├── YES → Lite Mode
          └── NO  → Full Discovery
```

### Mode Comparison

| Mode | Context | Discovery | Best For |
|:-----|:--------|:----------|:---------|
| **Full Discovery** | ~40k | AI guides you | Complex projects, first-timers |
| **Quick Start** | ~40k | You filled seeds | Pre-planned projects |
| **Lite Mode** | ~8k | Minimal | Small models, simple builds |
| **Just Build** | ~3k | None | You know exactly what you want |

---

## Full Discovery Mode

**The AI guides you through everything.**

### How to Start
1. Open this folder in your AI tool (Claude, GPT, etc.)
2. Copy the "Full Discovery" prompt from [RUN.md](RUN.md)
3. Paste and start talking

### What Happens
1. AI loads the constitution (security, framework, instructor)
2. AI scans your seeds and asks what's missing
3. AI suggests a kit based on your project type
4. Kit PROMPTER validates all requirements
5. Build begins only when everything is filled

### Best For
- New projects where you're still figuring things out
- First time using the pack
- Complex multi-phase builds

---

## Quick Start Mode

**You fill the seeds first, AI validates and builds.**

### How to Start
1. Fill `user-input/seed/PROJECT.md` (minimum: name, type, north star)
2. Fill other seeds you have info for (BRAND.md, TECH_STACK.md, etc.)
3. Copy the "Quick Start" prompt from [RUN.md](RUN.md)
4. Paste and go

### What Happens
1. AI reads your seeds
2. AI checks against the kit PROMPTER requirements
3. AI only asks about blank fields or [PLACEHOLDER] markers
4. Build begins faster

### Best For
- You planned externally (ChatGPT, docs, whiteboard)
- Migrating an existing project
- You know what you want, just need it built

---

## Lite Mode

**Single-file rules for smaller models.**

### How to Start
1. Copy the prompt from [OMEGA_LITE.md](OMEGA_LITE.md)
2. Paste into your AI
3. Answer the simple questions

### What You Get
- ~8k tokens instead of ~85k
- Core security, workflow, and rules
- Works on models with <32k context
- Still maintains safety and quality

### What You Give Up
- Full kit patterns and checklists
- Detailed blueprints
- Multi-phase tracking

### Best For
- Smaller AI models
- Simple projects
- Quick prototypes

---

## Just Build Mode

**Skip discovery, straight to code.**

### How to Start
1. Open [ignition/JUST_BUILD.md](ignition/JUST_BUILD.md)
2. Fill in the template:
   - Project: What you're building
   - Tech Stack: What tools
   - Start With: First thing to build
3. Paste into AI and go

### What Happens
1. AI respects security rules (always)
2. AI builds what you asked
3. AI shows you results
4. You iterate

### What You Give Up
- Discovery questions
- Requirement validation
- Kit checklists
- PRD/SOP generation

### Best For
- You know EXACTLY what you want
- Small, focused tasks
- Prototyping and experiments
- Time-sensitive builds

---

## How the AI Works (Smart Reader)

The AI doesn't load everything at once. It's a **smart reader with a notepad**.

```
Full Constitution (95 files)
         ↓
    AI reads Tier 1 (always loaded)
         ↓
    AI scans other files as needed
         ↓
    AI writes findings to SESSION_CONTEXT.md
         ↓
    AI works from its notes
         ↓
    AI loads more files only when needed
```

### Why This Matters
- **Works on smaller models** — Not hoarding 85k tokens
- **Faster responses** — Less to process
- **Persistent memory** — SESSION_CONTEXT.md survives across sessions
- **Efficient** — Reads once, references notes

### The Tiers

| Tier | What | When |
|:-----|:-----|:-----|
| **Tier 1** | SECURITY, FRAMEWORK, INSTRUCTOR, SESSION_CONTEXT.md | Always loaded |
| **Tier 2** | Current kit PROMPTER, active blueprint | When actively working |
| **Tier 3** | Everything else | Read, summarise, release |

---

## Working Memory

`user-input/SESSION_CONTEXT.md` is the AI's notepad.

### What It Stores
- Project summary (name, type, north star)
- Requirements status (what's filled, what's blank)
- Key decisions (locked choices)
- Open questions (still to decide)
- Current checkpoint and blockers
- File summaries (what AI has scanned)
- Session log (what happened)

### When It Updates
- After completing a checkpoint
- After filling a seed
- After a key decision
- Before ending a session

### Why It Matters
- Resume sessions instantly
- AI remembers what it learned
- No re-reading the same files

---

## Have Existing Work?

### Drop Files
Put existing files in `user-input/plug-and-play/`:
- Wireframes
- Brand guidelines
- Existing code
- Documentation

The AI will detect them and ask what they are.

### Or Point to Them
Tell the AI: "My files are at /path/to/files"

Works the same way.

---

## Quick Commands

| Say | AI Does |
|:----|:--------|
| "What do you know?" | Summarizes current state |
| "What's next?" | Lists next actions |
| "Confirmed" / "Approved" | Proceed to next checkpoint |
| "Stop" | Halt and wait |
| "Continue" | Resume from where you left off |
| "Audit" | Check build against requirements |
| "Handoff" | Generate session summary |

---

## The 3 Zones

| Zone | Folder | Function | You Touch? |
|:-----|:-------|:---------|:-----------|
| **Constitution** | `constitution/` | Rules, security, workflow | No |
| **User Input** | `user-input/` | Seeds, files, project state | Yes |
| **Store** | `store/` | Kits, skills, tools | Copy what you need |

---

## Project Types & Kits

| Type | Kit | Focus |
|:-----|:----|:------|
| **Website** | `store/kits/website/` | Pages, SEO, performance, mobile |
| **SaaS** | `store/kits/saas/` | Auth, billing, dashboard, multi-tenancy |
| **API** | `store/kits/api/` | Endpoints, versioning, rate limits, errors |
| **Automation** | `store/kits/automation/` | Triggers, retries, error handling, logging |

Each kit has:
- **PROMPTER.md** — Requirements table, discovery questions
- **[KIT]_KIT.md** — Patterns and checklists
- **kit.config.md** — When it activates, override rules

---

## Files Reference

| File | What |
|:-----|:-----|
| [RUN.md](RUN.md) | All startup prompts (Full, Quick, Lite, Just Build) |
| [OMEGA_LITE.md](OMEGA_LITE.md) | Single-file condensed rules |
| [ignition/JUST_BUILD.md](ignition/JUST_BUILD.md) | Skip discovery, build now |
| [store/STORE_GUIDE.md](store/STORE_GUIDE.md) | How kits and skills work |
| [store/kits/KIT_GUIDE.md](store/kits/KIT_GUIDE.md) | Kit system details |

---

## Principles

1. **Function before Form** — Make it work, then make it pretty
2. **Security is Supreme** — Never compromise safety
3. **Human is the Pilot** — AI executes, you decide
4. **Ask, Don't Assume** — Questions over guessing
5. **Show, Don't Tell** — Evidence over claims
6. **Know, Don't Hoard** — Smart loading, not context bloat

---

## Getting Help

- **Switch modes:** Say "Switch to [mode name]"
- **More guidance:** Say "Switch to full mode"
- **Less ceremony:** Say "Just build this: [description]"
- **Stuck:** Say "Stop. What's blocking us?"

---

*Built by Ed. Powered by the Omega Formula Stack.*
