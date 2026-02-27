# The Omega System (Public)

Welcome to the public-facing hub of the **Omega Ecosystem**. This repository represents a fully decoupled, self-governing collection of tools designed to orchestrate and execute AI-driven software development.

## 🧱 The Architecture

The ecosystem is split into three standalone but highly interconnected layers:

### 1. 📜 Constitution V10 (The Engine)
The law. This folder contains the absolute set of instructions, blueprints, and guardrails (`INSTRUCTOR.xml`, `SECURITY.xml`, `PROMPTING.xml`) that govern how autonomous agents plan, build, test, and act. 
- Houses the **Hive Orchestration** directories where agents collaborate securely without stepping on each other's toes.

### 2. 🦀 Omega Claw v1 (The Remote Control)
A dynamic, Python-based dispatcher that bridges the gap between your mobile device (Telegram) and the Constitution's Hive.
- Secured by **SQLCipher / Fernet** data-at-rest encryption.
- Powered by a stateless `IntentAgent` and dynamic `OrchestratorAgent`.
- Send natural language commands like `"build a saas"` or `"install postgres skill"`, and it translates them into `[FOUNDER_JOB]` files for agents to pick up.

### 3. 📦 Constitution Store v1 (The Marketplace)
The asset repository. A massive collection of plug-and-play capabilities.
- **Kits/Seeds:** Pre-configured project scaffolds (e.g. `website`, `automation`).
- **Skills:** Modular Python files that extend Omega Claw's intent system.
- **MCPs:** Configurations to dynamically connect agents to external services like GitHub or Supabase.

---

*This repository is continually evolving. Always check individual sub-directories for detailed module-level instructions.*
