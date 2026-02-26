# OMEGA CONSTITUTION PACK — v9

**Build anything with AI, the right way.**

A framework that makes AI build things properly — safe, complete, and flexible.

---

## The Core 4 Structure

The Omega Constitution v9 is organized into 4 simple pillars:

```text
omega-constitution-v9/
├── START HERE/        ◄── Readmes, training manuals, and startup prompts
├── CONSTITUTION/      ◄── The AI rules and framework (XML, AI reads this)
├── USER SPACE/        ◄── Your actual project files go here
└── STORE/             ◄── Link to the external Omega Store repo (kits, skills, MCPs)
```

**[START HERE/START_HERE.md](START_HERE/START_HERE.md)** is your training manual. It has everything you need.

---

## Quick Start

1. Open `omega-constitution-v9/` in your AI (Claude, GPT, Cursor, etc.)
2. Paste this prompt:

```
You are the OMEGA CONSTRUCTOR.

Read constitution/SECURITY.xml, FRAMEWORK.xml, INSTRUCTOR.xml.
Read user-input/SESSION_CONTEXT.md.

Ask me what I want to build.
```

3. Talk. The AI guides you.

---

## The Master Daemon

Omega comes with self-healing background scripts (auto-updating project maps, security scanners, and changelogs).
To turn them on, run this command from the `omega-constitution-v9` folder:

```bash
python3 CONSTITUTION/python/omega_daemon.py
```

---

## Modes

| Mode | For | Tokens |
|:-----|:----|:-------|
| Full Discovery | AI guides you through everything | ~40k |
| Quick Start | You filled requirements, AI validates | ~40k |
| Lite | Small models, simple projects | ~8k |
| Just Build | Skip to code | ~3k |

Details in [START_HERE.md](omega-constitution-v9/START_HERE.md)

---

## What's Inside v9

```
omega-constitution-v9/
├── START_HERE.md        ◄── Training manual (read this)
├── RUN.md               ◄── All startup prompts
├── OMEGA_LITE.md        ◄── Condensed rules for small models
├── constitution/        ◄── AI rules (XML, you don't need to read)
├── user-input/          ◄── Your project files go here
└── store/               ◄── Kits, skills, patterns
```

---

## Previous Versions

- `omega-v3/` — Earlier version, preserved for reference

---

*Built by Ed. Powered by the Omega Formula Stack.*
