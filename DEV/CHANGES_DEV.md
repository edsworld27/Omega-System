# CHANGES_DEV — Constitution Changelog

**Purpose:** Track all changes to the Omega Constitution framework.

---

## v9.4 — 2026-02-26

### Structured Onboarding Flow
- Created ONBOARDING.md with mandatory interview sequence
- Added CP-ONBOARD checkpoint (before CP-0)
- Rewrote RUN.md with single master prompt
- Enforces: Mode → Project Type → Existing Work → Purpose
- One question at a time, no deviation

### DEV Workspace
- Created DEV/ folder for meta-development
- CONTEXT_DEV.md — working memory
- CHANGES_DEV.md — this changelog
- IMPLEMENTATION_DEV.md — roadmap
- Using constitution to build constitution

### README as Navigation Hub
- Simplified to links only
- Points to all other docs

---

## v9.3 — 2026-02-26

### Path Structure Update
- Updated all `user-input/` references to `USER SPACE/dev-work/`
- Files updated:
  - FRAMEWORK.xml, PRACTICES.xml, INSTRUCTOR.xml
  - All ignition prompts (FRESH_BUILD, IMPORT, RESUME, etc.)
  - START_HERE.md, RUN.md
  - TECH_STACK.md seed template

---

## v9.2 — 2026-02-26

### Kit Creation Framework
- Created `omega-store/kits/_template/` skeleton
- Added KIT_EXPORT_GUIDE.md (320 lines)
- Updated KIT_CREATION_GUIDE.md with quick start
- Moved incomplete kits to DEV/future-kits/

### USER SPACE Restructure
- Split into `dev-work/` and `project/`
- dev-work/ = framework files
- project/ = clean deliverable
- Updated omega_compiler.py to use new paths

### Repository Split
- Created omega-store repo (https://github.com/edsworld27/omega-store)
- omega-constitution = framework only
- omega-store = kits, skills, mcps

---

## v9.1 — Earlier

### Initial v9 Setup
- Plug-and-play kit architecture
- Kit auto-discovery via kit.config.md
- Python daemon system (watchers)
- Constitution compliance test suite
- Training manual with ASCII diagrams

---

## Format

```
## vX.X — YYYY-MM-DD

### Category
- Change description
- Files affected
```

---

*This is our changelog for the constitution itself, not user projects.*
