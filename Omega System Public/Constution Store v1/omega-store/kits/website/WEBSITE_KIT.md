# WEBSITE KIT — Starter Pattern

## Sitemap Template
| Page | Path | Template | Priority |
| :--- | :--- | :--- | :--- |
| Home | / | Hero + Features + CTA | Critical |
| About | /about | Story + Team + Values | High |
| Services | /services | Service cards + CTAs | High |
| Contact | /contact | Form + Map + Details | Medium |
| Blog | /blog | Post list + Categories | Medium |
| Privacy | /privacy | Legal text | Required |
| Terms | /terms | Legal text | Required |

## SEO Checklist
- [ ] Unique title tag per page (<60 chars)
- [ ] Meta description per page (<155 chars)
- [ ] H1 on every page (one per page)
- [ ] Alt text on all images
- [ ] sitemap.xml generated
- [ ] robots.txt configured
- [ ] Schema markup (Organization, LocalBusiness, BreadcrumbList)
- [ ] Open Graph tags for social sharing
- [ ] Canonical URLs set

## Performance Budget
| Metric | Target | Tool |
| :--- | :--- | :--- |
| Largest Contentful Paint | <2.5s | Lighthouse |
| First Input Delay | <100ms | Lighthouse |
| Cumulative Layout Shift | <0.1 | Lighthouse |
| Total page weight | <500KB | DevTools |
| Image formats | WebP/AVIF | Build tool |

## Analytics Setup
- [ ] Google Analytics 4 (or privacy-friendly alternative)
- [ ] Google Search Console
- [ ] Event tracking for CTAs
- [ ] Conversion goals defined
- [ ] 404 error tracking

## Content Hierarchy Pattern
Each page should follow this hierarchy:
1. **Hero Section** — Primary message + CTA (above the fold)
2. **Social Proof** — Logos, testimonials, or stats
3. **Value Proposition** — 3–4 cards/columns explaining benefits
4. **Deep Content** — Detailed descriptions, case studies, features
5. **Secondary CTA** — Repeat the primary CTA or introduce a softer one
6. **FAQ** — Address objections before they leave
7. **Footer** — Navigation, legal links, contact, social

## Responsive Breakpoints
| Breakpoint | Width | Target |
| :--- | :--- | :--- |
| Mobile | <640px | Single column, stacked layout |
| Tablet | 640px–1024px | Two column, simplified nav |
| Desktop | 1024px–1440px | Full layout |
| Large Desktop | >1440px | Max-width container, centred |

**Mobile-first rule:** Start with mobile layout, progressively enhance for larger screens.

## Image Strategy
- **Hero images:** WebP, max 200KB, lazy-load below fold
- **Thumbnails:** WebP, max 30KB, eager-load if above fold
- **Icons:** SVG inline or sprite sheet
- **Responsive images:** Use `<picture>` element with `srcset` for 1x/2x/3x
- **No layout shift:** Always set `width` and `height` attributes

## Cookie Consent (GDPR/PECR)
- [ ] Cookie consent banner implemented (prior blocking)
- [ ] Analytics only fires after consent
- [ ] Categories: Necessary / Analytics / Marketing
- [ ] Consent stored and retrievable
- [ ] Reject button equally prominent as Accept
- [ ] Cookie policy page linked from banner

## Pre-Launch Checklist
- [ ] All pages render correctly on mobile, tablet, desktop
- [ ] All links work (no 404s)
- [ ] All forms submit correctly
- [ ] Favicon and touch icons set
- [ ] 404 page designed
- [ ] SSL certificate active
- [ ] Redirects configured (www → non-www or vice versa)
- [ ] Page speed ≥90 on Lighthouse
- [ ] Accessibility ≥90 on Lighthouse
- [ ] Social sharing preview (OG tags) tested
