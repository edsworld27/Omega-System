# AUTOMATION KIT — Starter Pattern

## Workflow Architecture
Every automation follows this pattern:
```
[TRIGGER] → [VALIDATE INPUT] → [PROCESS] → [OUTPUT] → [LOG]
     │              │                │            │
     │         [REJECT + LOG]   [ERROR HANDLER]   │
     │                              │             │
     │                        [RETRY / ALERT]  [NOTIFY]
```

## Trigger Types
| Trigger | Use When | Platform Examples |
| :--- | :--- | :--- |
| **Webhook** | External event arrives | Stripe payment, GitHub PR, form submission |
| **Schedule (Cron)** | Time-based recurring task | Daily reports, weekly cleanup, monthly billing |
| **Event-driven** | Internal state change | User signs up, order completed, threshold reached |
| **Manual** | Human-initiated | Admin action, one-off migration, ad-hoc report |
| **Agent handoff** | Multi-agent pipeline | Agent A completes → Agent B starts |

## Workflow Template

### Workflow: [Name]
- **Purpose:** (One sentence — what does this workflow achieve?)
- **Trigger:** (What starts it?)
- **Frequency:** (How often? / On what event?)
- **Input schema:**
```json
{
  "field": "type — validation rule"
}
```
- **Processing steps:**
1. Validate input against schema
2. (Core logic step 1)
3. (Core logic step 2)
4. Generate output
5. Log result
- **Output:** (What is produced?)
- **Error handling:** (What happens on failure?)
- **Human review:** (When does a human need to approve?)

---

## Platform-Specific Patterns

### n8n
- Use **Webhook** node for external triggers
- Use **Set** node for data transformation (not Function node for simple transforms)
- Use **IF** node for branching, not embedded Javascript
- Store credentials using n8n's **Credentials Manager** — never hardcode
- Pin production workflows — use versioning via Git export
- Set workflow timeout: 5 minutes default, 30 minutes max for heavy processing
- Use **Error Trigger** node for global error handling

### Make (Integromat)
- Use **Instant triggers** (webhooks) over polling where possible
- Set **execution limits**: max 3 retries, 5-minute timeout
- Use **Routers** for parallel processing paths
- Enable **error handling** on every module (not just the first)
- Use **Data Stores** for state persistence between runs
- Tag scenarios with environment: `[PROD]`, `[DEV]`, `[TEST]`

### Zapier
- Use **Webhooks by Zapier** for custom triggers
- Use **Filter** steps to prevent unnecessary processing
- Use **Paths** for conditional logic (not multiple Zaps)
- Enable **autoreplay** for failed runs
- Use **Transfer by Zapier** for large data moves
- Monitor task usage to avoid unexpected billing

### Custom Agent Workflows
- Follow the **AGENT_MD_TEMPLATE** for agent definitions
- Follow the **AGENT_WORKFLOW_TEMPLATE** for flow design
- Every agent operates under SECURITY.xml — no exceptions
- Every agent has a defined **capability matrix** — actions outside it are rejected
- Handoffs between agents use structured JSON with validation at both ends

---

## Error Handling Patterns

### Retry Strategy
| Error Type | Retry? | Max Retries | Backoff |
| :--- | :--- | :--- | :--- |
| Network timeout | Yes | 3 | Exponential (1s, 5s, 30s) |
| Rate limit (429) | Yes | 3 | Respect `Retry-After` header |
| Auth failure (401) | No | 0 | Alert immediately — credential may be revoked |
| Validation error (400) | No | 0 | Log and reject — fix the input |
| Server error (500) | Yes | 2 | Fixed (30s, 60s) |

### Dead Letter Queue
When all retries fail:
1. Move the payload to a dead letter queue / log file
2. Alert the designated human via notification channel
3. Do NOT silently drop failed messages
4. Retain failed payloads for 30 days for replay

### Circuit Breaker for Workflows
If a workflow fails >5 times in 1 hour:
1. Disable the workflow automatically
2. Send alert to owner
3. Require manual re-enable after investigation
4. Log all failures with timestamps and error detail

---

## Data Flow Security
(From SECURITY.xml — applies to all automations)

- All webhook URLs use unique, unguessable paths
- All incoming webhooks validate signatures (HMAC-SHA256)
- Automation credentials stored in secrets manager — never in workflow definitions
- Production and development workflows use **separate credentials**
- PII is masked before logging
- External API calls use allowlisted destinations only

## Scheduling Best Practices
- Stagger schedules — don't run everything at midnight
- Use UTC for all cron expressions
- Add jitter (random delay 0–60s) to prevent thundering herd on APIs
- Log execution start + end + duration for every scheduled run
- Set maximum execution time per workflow — kill zombies

## Monitoring
- [ ] Execution count per workflow per day
- [ ] Success/failure rate per workflow
- [ ] Average execution time per workflow
- [ ] Queue depth (if using queues)
- [ ] Alert on: failure rate >5%, execution time >2x average, queue depth growing
