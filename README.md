# OMEGA CONSTITUTION

**Build anything with AI, the right way.**

A framework that makes AI build software properly — safe, complete, and flexible.

---

## Repository Structure

```
Omega Constitution Pack/
│
├── omega-constitution-v9/     ◄── THE FRAMEWORK
│   ├── START HERE/               Training manual + startup prompts
│   ├── CONSTITUTION/             AI rules (XML files)
│   ├── USER SPACE/               Your project files
│   │   ├── dev-work/             Framework files (seeds, context)
│   │   └── project/              Clean deliverable (share this)
│   └── STORE/                    → Links to omega-store
│
├── omega-store/               ◄── KITS & TOOLS
│   ├── kits/                     Project templates (website, saas, api)
│   ├── skills/                   Agent templates
│   └── mcps/                     MCP configurations
│
├── DEV/                       ◄── META-DEVELOPMENT
│   ├── CONTEXT_DEV.md            Our working memory
│   ├── CHANGES_DEV.md            Constitution changelog
│   └── IMPLEMENTATION_DEV.md     Roadmap & ideas
│
└── README.md                  ◄── YOU ARE HERE
```

---

## Quick Start

### 1. Clone

```bash
git clone https://github.com/edsworld27/omega-constitution.git
cd omega-constitution
```

### 2. Open in Your AI

Open `omega-constitution-v9/` in Claude, GPT, Cursor, or any AI tool.

### 3. Paste This Prompt

```
You are the OMEGA CONSTRUCTOR.

Read constitution/SECURITY.xml, FRAMEWORK.xml, INSTRUCTOR.xml.
Read USER SPACE/dev-work/SESSION_CONTEXT.md.

Ask me what I want to build. Guide me through it.
```

### 4. Talk

The AI interviews you, fills in requirements, and builds.

---

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│                      YOU (Human)                        │
│                                                         │
│   1. Pick a mode (Full / Quick / Lite / Just Build)     │
│   2. Answer questions (or fill seeds yourself)          │
│   3. Say "build" when ready                             │
│   4. Review what AI builds                              │
│   5. Say "continue" or "fix X"                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                      AI (Agent)                         │
│                                                         │
│   • Reads constitution (XML files)                      │
│   • Asks questions to fill gaps                         │
│   • Validates requirements before building              │
│   • Builds in USER SPACE/project/                       │
│   • Waits for your approval at each step                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Modes

| Mode | Best For | Context |
|:-----|:---------|:--------|
| **Full Discovery** | New projects, exploring | ~40k tokens |
| **Quick Start** | Pre-planned, seeds filled | ~40k tokens |
| **Lite** | Small models (<32k) | ~8k tokens |
| **Just Build** | Know exactly what you want | ~3k tokens |

All prompts are in [omega-constitution-v9/START HERE/RUN.md](omega-constitution-v9/START%20HERE/RUN.md)

---

## The Build Flow

```
DISCOVER ──► PLAN ──► BUILD ──► TEST ──► SHIP

    │          │         │         │
    ▼          ▼         ▼         ▼
 You answer  You approve  You review  You approve
 questions   the plan     the code    results
```

At every step: AI stops and waits for you. **You are the pilot.**

---

## Project Handoff

When your project is complete:

```
USER SPACE/
├── dev-work/     ← Framework files (don't share)
└── project/      ← Clean deliverable (share this!)
```

The `project/` folder is always clean and ready to hand off. No compilation needed.

Or use the compiler for a Desktop export:
```bash
python3 CONSTITUTION/python/omega_compiler.py
```

---

## Kits (Project Templates)

Kits auto-activate based on project type:

| Kit | For |
|:----|:----|
| **website** | Marketing sites, landing pages |
| **saas** | SaaS apps with auth, billing |
| **api** | API-first backends |
| **automation** | n8n, workflows, integrations |

Kits live in [omega-store/kits/](omega-store/kits/)

### Create Your Own Kit

Use the template: [omega-store/kits/_template/](omega-store/kits/_template/)

Guide: [KIT_CREATION_GUIDE.md](omega-store/kits/KIT_CREATION_GUIDE.md)

---

## The Golden Rules

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   1. SECURITY IS SUPREME                                │
│      AI never exposes secrets or bypasses safety        │
│                                                         │
│   2. YOU ARE THE PILOT                                  │
│      AI executes, you decide                            │
│                                                         │
│   3. FUNCTION BEFORE FORM                               │
│      Make it work, then make it pretty                  │
│                                                         │
│   4. ASK, DON'T ASSUME                                  │
│      AI asks when unclear, never guesses                │
│                                                         │
│   5. SHOW, DON'T TELL                                   │
│      AI provides evidence, not just claims              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Files You Need

| File | What It Does |
|:-----|:-------------|
| [START_HERE.md](omega-constitution-v9/START%20HERE/START_HERE.md) | Full training manual |
| [RUN.md](omega-constitution-v9/START%20HERE/RUN.md) | All startup prompts |
| [OMEGA_LITE.md](omega-constitution-v9/START%20HERE/OMEGA_LITE.md) | Condensed rules (small models) |

---

## Contributing

### To the Framework
- Fork omega-constitution
- Make changes
- PR with description

### To the Store
- Fork omega-store
- Add your kit/skill
- PR with description

See [DEV/](DEV/) for how we develop the framework itself.

---

## Links

| Resource | URL |
|:---------|:----|
| Constitution Repo | [github.com/edsworld27/omega-constitution](https://github.com/edsworld27/omega-constitution) |
| Store Repo | [github.com/edsworld27/omega-store](https://github.com/edsworld27/omega-store) |

---

## License

MIT

---

*Built by Ed. Powered by the Omega Formula Stack.*
