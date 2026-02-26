# CHANGES — Omega Constitution v9

> Complete changelog from v9.0 to present.
> For repo links see [LINKS.md](../DEV/LINKS.md) | For structure see [TREEMAP.md](TREEMAP.md)

---

## v9.9.6 — 2026-02-26
**Scenarios folder + multi-repo awareness**
- Added `CONSTITUTION/scenarios/` — standard operating procedures for agents
- Created `git-push-all-repos.md` — when user says "push to git", agents check ALL ecosystem repos
- Hardened `.gitignore` per SECURITY.xml §1.1 (`.pem`, `.key`, `.p12` patterns)
- Removed root `.env.example` — env config belongs only in omega-claw repo

## v9.9.5 — 2026-02-26
**Environment cleanup**
- Removed misplaced `.env.example` from Constitution root
- Each repo is self-contained: env files live only in the repo that needs them

## v9.9.4 — 2026-02-26
**Environment system**
- Added `.env.example` with comprehensive placeholder config (Telegram, paths, future API keys)
- Hardened `.gitignore` in both Constitution and Omega Claw repos

## v9.9.3 — 2026-02-26
**omega.py Install Omega Claw**
- `omega.py` wizard now offers "Install Omega Claw?" after project setup
- If yes: clones the repo, asks for Telegram token, creates `.env`
- If no: skips silently — zero friction
- Detects if already installed

## v9.9.2 — 2026-02-26
**Evaluation + cross-agent sync**
- Full McKinsey-grade evaluation (7.8/10 overall score)
- `SESSION_CONTEXT.md` updated with full ecosystem state + repo URLs
- `CHANGES_DEV.md` updated with omega-claw GitHub link
- `DEV/LINKS.md` — central reference for all repo URLs + versions

## v9.9.1 — 2026-02-26
**Omega Claw standalone repo**
- Created https://github.com/edsworld27/omega-claw (separate from Constitution)
- Referenced in Constitution docs so agents can discover it
- Updated `DEV/LINKS.md` with live URL

## v9.9 — 2026-02-26
**🦀 Omega Claw MVP**
Built a complete Telegram → Constitution orchestration engine as a standalone project:
- `main.py` — entry point (logging → SQLite → Telegram boot)
- `core/telegram_bot.py` — auth whitelist, message splitting, error handling
- `core/orchestrator.py` — message router with SQLite command logging
- `core/intent_agent.py` — keyword classifier (no LLM, no API costs)
- `core/logging_setup.py` — redacted logging (hides tokens in output)
- `agents/base_agent.py` — clean ABC for all agents
- `agents/orchestrator_agent/` — 4-step onboarding wizard + FOUNDER_JOB generation
- `agents/reporter_agent/` — Hive status + SQLite job history
- `agents/__init__.py` — lean AgentRegistry
- `db/database.py` — SQLite with `jobs` + `command_log` tables
- `skills/` scaffold — plug-and-play directory with `_template/`
- `mcps/` scaffold — future MCP connections
- Only 2 dependencies: `python-telegram-bot` + `python-dotenv`

## v9.8.1 — 2026-02-26
**Session changelog sync**
- Full session changelog written covering v9.6–v9.8
- All cross-agent context files updated

## v9.8 — 2026-02-26
**End-to-end Telegram → Hive loop**
- `omega-bot` MVP: stripped 30+ file mac-commander down to 9 lean files
- `omega_job_watcher.py` daemon: watches `telegram_inbox/` for new FOUNDER_JOBs
- Writes `PICKUP_ALERT.md` when jobs detected
- `INSTRUCTOR.xml` Step 1: "Check for PICKUP_ALERT.md on session start"
- Wired into `omega_daemon.py` as a background task

## v9.7 — 2026-02-26
**Recursive Rule of 3 hierarchy**
- Replaced Rule of 5 with mathematically cleaner Rule of 3
- Infinite recursion: Founder → Mega-Manager → Manager → Worker
- For every 1-3 subordinates, spawn 1 manager tier above
- Updated `MASTER_ORCHESTRATOR.md` with full scaling formula
- Updated `ConstitutionAgent` onboarding to include Rule of 3

## v9.6.1 — 2026-02-26
**Telegram Bot documentation**
- `DEV/ideation/CONSTITUTION_BOT.md` — full design doc for bot integration
- Architecture decisions documented

## v9.6 — 2026-02-26
**🤖 Constitution Telegram Bot**
- `ConstitutionAgent` — 4-step structured onboarding via Telegram
- Generates `FOUNDER_JOB-XXX.md` files in `telegram_inbox/`
- Jobs are Constitution-compliant with Kit, Mode, and Rule of 3 instructions
- SQLite logging via `create_job()`

## v9.5.1 — 2026-02-25
**Management hierarchy**
- Rule of 5 management hierarchy for the Agent Hive
- (Later replaced by Rule of 3 in v9.7)

## v9.5 — 2026-02-25
**Infinite scale + mode autonomy**
- Infinite Agent Hive scaling
- Mode-based checkpoint autonomy (Full Discovery = strict, Just Build = autonomous)
- Context offloading to prevent AI context window limits
- IDE routing rules
- Constitution Bot ideation begun

---

## Omega Claw Changelog

### v1.4 — 2026-02-26
- Comprehensive `.env.example` with all config sections
- Hardened `.gitignore` per SECURITY.xml §1.1

### v1.3 — 2026-02-26
**All SECURITY.XML findings fixed**
- Capability matrix on `BaseAgent` + all agents (§3.3)
- `fcntl.flock()` on state file reads/writes (§3.7)
- `_escape_md()` on all user-supplied output (§2.2)
- Forbidden import scan + SHA-256 hash trust on skills (§3.4)

### v1.2 — 2026-02-26
**Critical security fixes**
- Deny-by-default auth — rejects ALL if no users configured (§5.4)
- Generic error messages — never leak exceptions to Telegram (§0.8)
- Input allowlist — alpha + spaces, max 50 chars (§2.1)
- DB file permissions `chmod 600` (§4.5)

### v1.1 — 2026-02-26
**Skills auto-loader**
- `core/skill_loader.py` — scans `skills/` on boot
- Reads `skill.json` → imports `handler.py` → registers intents
- Dynamic keyword injection into IntentAgent
- `SkillAgent` wrapper in AgentRegistry
- Verified with test `hello-skill` — plug-and-play works

### v1.0 — 2026-02-26
**Initial release** — full Omega Claw MVP pushed to GitHub
- **[2026-02-26 18:44:53]** Modified file: `USER SPACE/logging/compliance_report.md`
- **[2026-02-26 18:45:05]** Modified file: `USER SPACE/logging/compliance_report.md`
- **[2026-02-26 18:45:14]** Modified file: `USER SPACE/logging/compliance_report.md`
- **[2026-02-26 18:45:23]** Modified file: `USER SPACE/logging/compliance_report.md`
