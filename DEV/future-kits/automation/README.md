# Automation Kit

Build workflows with n8n, Make, Zapier, or custom agents.

**Status:** Patterns only (task files coming soon)

---

## What's Inside

```
automation/
├── README.md              ← You're here
├── AUTOMATION_KIT.md      ← Patterns & best practices
└── kit.config.md          ← Auto-activation rules
```

---

## Key Patterns (in AUTOMATION_KIT.md)

- **Workflow Architecture** — Trigger → Validate → Process → Output → Log
- **Trigger Types** — Webhook, cron, event, manual, agent handoff
- **Platform Patterns** — n8n, Make, Zapier specifics
- **Error Handling** — Retry strategy, dead letter queues
- **Circuit Breaker** — Auto-disable failing workflows
- **Security** — Webhook validation, credential management
- **Scheduling** — UTC cron, jitter, execution limits
- **Agent Workflows** — Multi-agent pipelines

---

## How to Use

1. **Copy** this folder to `user-input/plug-and-play/kits/automation/`
2. **Run** the ignition prompt — AI will detect the kit
3. **Reference** `AUTOMATION_KIT.md` for patterns and checklists

---

## Best For

- n8n workflows
- Make (Integromat) scenarios
- Zapier automations
- Custom agent pipelines
- Scheduled jobs
- Event-driven processing

---

## Combine With

- **API Kit** — For webhook endpoints
- **SaaS Kit** — For user-triggered automations
