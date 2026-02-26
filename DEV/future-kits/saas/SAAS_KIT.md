# SAAS KIT — Starter Pattern

## Auth Flow
1. Sign Up (email/password or OAuth)
2. Email verification
3. Onboarding wizard (3–5 steps max)
4. Dashboard (first value in <60 seconds)
5. Login / Forgot password / Magic link

### Auth Security Requirements (from SECURITY.xml)
- Password hashing: Argon2id or bcrypt (work factor ≥12)
- Session tokens: HttpOnly, Secure, SameSite=Strict cookies
- JWT expiry: Access token ≤15 min, refresh token ≤7 days
- Account lockout: After 5 failed attempts, lock for 15 min
- Password reset: Single-use token, expires in 15 minutes
- MFA: Required for admin accounts, optional for users

## Billing Integration
- [ ] Subscription tiers defined
- [ ] Stripe/Paddle integration
- [ ] Free trial (duration: ___)
- [ ] Upgrade/downgrade flow
- [ ] Invoice generation
- [ ] Cancellation + retention flow

## Subscription Tiers
| Tier | Price | Features | Limits |
| :--- | :--- | :--- | :--- |
| Free | £0 | (core features) | (usage limits) |
| Pro | £/mo | (all features) | (higher limits) |
| Enterprise | Custom | (all + support) | (unlimited) |

## Dashboard Pattern
- Key metrics at top (cards)
- Recent activity feed
- Quick actions (primary CTA)
- Navigation: sidebar or top bar
- Settings accessible from avatar/menu

## Onboarding Checklist
- [ ] Welcome screen with value proposition
- [ ] Account setup (name, avatar, preferences)
- [ ] First action guided (wizard or tooltip tour)
- [ ] Empty states with helpful prompts
- [ ] Progress indicator ("2 of 4 steps complete")

## Transactional Email Templates
| Email | Trigger | Content |
| :--- | :--- | :--- |
| Welcome | Sign up confirmed | Value prop + first action CTA |
| Email verification | Sign up | Verify link (expires 24h) |
| Password reset | User request | Reset link (expires 15 min) |
| Invoice | Payment processed | Amount, date, receipt link |
| Trial expiring | 3 days before end | Upgrade CTA + features recap |
| Cancellation | User cancels | Retention offer + data export |
| Usage alert | Near limit | Upgrade CTA |

**Email Security:** SPF + DKIM + DMARC configured and verified (per SECURITY.xml §14).

## Multi-Tenancy Considerations
- **Data isolation:** Each tenant's data is logically or physically separated
- **URL strategy:** Subdomain (`tenant.app.com`) or path (`app.com/tenant`)
- **Configuration:** Per-tenant feature flags, branding, limits
- **Query safety:** Every database query filters by `tenant_id` — never rely on frontend to enforce this

## Usage Tracking
- [ ] Define usage units (API calls, storage, seats, records)
- [ ] Track usage per tenant in real-time
- [ ] Enforce limits at API level (not just UI)
- [ ] Alert users at 80% and 100% of limit
- [ ] Log all limit enforcement events

## Settings Page Structure
| Section | Fields |
| :--- | :--- |
| Profile | Name, email, avatar, password change |
| Team | Invite members, set roles, remove members |
| Billing | Current plan, payment method, invoices, upgrade |
| Notifications | Email preferences, in-app notification settings |
| API | API keys (generate, revoke, usage stats) |
| Data | Export data, delete account |
| Security | MFA setup, active sessions, login history |
