# Omega Constitution Index

> [!IMPORTANT]
> The full Omega Constitution is now stored in an external repository to keep this workspace lightweight and improve Agent context limits.
> 
> **Repository:** [https://github.com/edsworld27/omega-constitution](https://github.com/edsworld27/omega-constitution)

When you need to reference specific rules, methodologies, or blueprints, execute a tool command to fetch the relevant Markdown or XML file from the `omega-constitution` repository.

## Map of Core Files

*   **Security Policies:** `SECURITY.xml`
*   **Prompting & Interaction Rules:** `PROMPTING.xml`, `INSTRUCTOR.xml`
*   **Architectural Framework:** `FRAMEWORK.xml`, `STRUCTURE.xml`
*   **Quality & Best Practices:** `QUALITY.xml`, `PRACTICES.xml`
*   **Agent Blueprints:** `blueprints/AGENT_MD.md`, `blueprints/AGENT_WORKFLOW.md`
*   **Project Documents:** `blueprints/PRD.md`, `blueprints/SOP.md`, `blueprints/TEST_PLAN.md`
*   **Python Tooling:** `/python/` (Contains helper scripts like compiler and watcher)
*   **Testing:** `/tests/COMPLIANCE_TESTS.md`

### How to use this index:

1. Identify the file you need based on the map above.
2. Fetch the Raw content from GitHub. For example, to read the Security rules:
   `curl -s https://raw.githubusercontent.com/edsworld27/omega-constitution/main/SECURITY.xml`
3. Ingest only the specific file needed for your current task.
