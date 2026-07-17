---
name: technical-seo-audit
description: Technical and on-page SEO audit of any website — a client site, your own site, a competitor, or a staging build before a CMS migration. Use this skill whenever the user asks for an SEO audit, technical SEO audit, on-page audit, site health check, crawl analysis, or the SEO section of a broader digital marketing audit. Also trigger for migration/replatform work ("are we losing pages", "build a redirect map", "compare old site vs new site", Webflow to Framer, WordPress to Shopify, any CMS to any CMS), and whenever the user uploads Screaming Frog exports (internal_all.csv, image_details.csv, All Inlinks), a GSC Pages export, or a sitemap and wants them analysed. Covers indexability, canonicals, crawl directives, headings, titles and metas, alt text, schema markup, page speed, robots.txt, llms.txt, internal linking, page-inventory diffing and redirect mapping.
---

# Technical SEO Audit

Two modes. Pick one at the start — they share Phases A–D but differ either side.

| Mode | When | Extra phases |
|---|---|---|
| **Site audit** | A live site: client, own, or competitor. Often one section of a wider digital marketing audit. | Phase 0 (scoping) + Phase E (prioritise) |
| **Migration audit** | A site is moving to a new CMS/builder. | Phase M (inventory diff + redirect map) + launch-day checklist |

If unsure, ask. "Audit this client's site" = site mode. "We're moving to Framer" = migration mode. A migration audit is a site audit *plus* Phase M — never skip A–D just because there's a redirect map to build.

---

## Read this first: the crawler lies

**The biggest failure mode in this work is trusting a crawl.** Before reporting any finding, classify the evidence:

| Evidence type | Trust |
|---|---|
| `view-source:` on a real page | **Highest** — this is what Google sees |
| HTTP status codes | High — rendering-independent |
| Sitemap contents | Medium — a *claim* a URL exists, not proof it works |
| Link-discovery crawl (Spider mode) | **Low** — misses anything behind load-more/JS pagination |
| On-page data from a large crawl | **Low until verified** — see Trap 2 |

In a real audit, three findings were reported as catastrophic and were **all false**: "0 of 408 pages migrated", "342 posts have no titles", "344 pages missing canonicals". All three were crawl artifacts. **Never report a catastrophic finding from crawl data alone** — verify against raw HTML first.

`scripts/onpage_audit.py` runs an artifact check before anything else and refuses to report on-page findings if the crawl is poisoned.

### Trap 1 — Spider crawls miss CMS collections
Spider mode follows `<a href>`. Galleries and blog listings often use load-more buttons or JS pagination, so the crawler dead-ends.
**Symptom:** the crawl returns far fewer pages than GSC shows earning clicks.
**Fix:** crawl in **List mode** from the XML sitemap.
**But log it as a finding, not just a nuisance:** if your crawler can't reach those pages by following links, they're orphaned from the internal link graph and Google is working harder than it should to find them.

### Trap 2 — Rate limiting produces fake empty pages
Edge-hosted builders (Framer, Vercel, Webflow) serve a generic SPA shell once a crawl exceeds their throughput limit. Pages look broken-but-present.
**Symptom:** many pages return an **identical byte size**, the same default title, ~15 words, no H1 — while a *subset* comes back with full correct data. **A genuine problem affects all pages of a type equally. Asymmetry means artifact.**
**Test:** crawl 10 of the "broken" URLs alone. If they come back correct, it was rate limiting.
**Fix:** 1 thread (paid licence), or batches of ~50 (works on free).

### Trap 3 — "0 results" can mean "not measured"
An empty "Missing Alt Text" export can mean zero missing, *or* that images were never crawled. Always check the denominator. Use **All Image Inlinks**, which shows every image *and* its alt value — catching both missing alt and useless alt (`alt="Frame-2847.png"`).

See `references/screaming-frog-config.md` for correct setup and which exports to request.

---

## Phase 0 — Scoping (site mode)

Before crawling, establish what "good" means for *this* site.

1. **What is the site for?** Lead gen, ecommerce, content/ad revenue, SaaS trials. This decides which pages matter.
2. **Get GSC access** (Performance → Pages, 12 months). Without it you can't prioritise, and every finding looks equally important — which means none are.
3. **Get GA4** if the goal is conversion rather than traffic.
4. **Ask what changed recently.** Replatform, redesign, content pruning, a migration nobody mentioned. Half of "our traffic dropped" is answered here.
5. **Check for bot traffic** before trusting any conversion-rate figure.

**Output of this phase:** one line stating what the audit is trying to protect or grow.

---

## Phase A — Indexability & crawl directives

The first question is never "is the title good." It's **can Google reach and index this at all.**

- **robots.txt** — anything blocking real content? Does the `Sitemap:` line point at the right domain? Before accepting any parameter `Disallow`, confirm what the parameter does — blocking a **pagination** parameter can orphan hundreds of pages.
- **`noindex`** — sitewide, and especially on **hub/index pages**. A `noindex` on a blog index cuts the discovery path to every post behind it.
- **Canonicals** — self-referencing? Pointing at a staging domain? Missing? Cross-domain?
- **sitemap.xml** — junk in it (`/search`, param URLs)? Hub pages *missing* from it? Does it match reality?
- **Status codes** — every 404 in a crawl means **something links to it**. A crawler cannot invent URLs. Find the source (Inlinks tab). Check the `Link Path` column for `Path-Relative` hrefs — in component-based builders one bad component generates a *different* broken URL on every page it appears on.
- **HTTPS**, redirect chains, `http→https` resolved in one hop.

---

## Phase B — On-page

Run `scripts/onpage_audit.py` on the Internal HTML export.

- **Missing H1** — usually template-level, so one fix cascades across every page of that type. Check whether headings start at H2/H3 (broken hierarchy).
- **Duplicate H1** — common in responsive builders rendering a desktop *and* mobile H1 into the DOM.
- **Titles** — >60 chars / 600px, missing, duplicated. A ` | Brand` suffix appended to already-full titles is the usual culprit.
- **Meta descriptions** — >155 chars, missing, duplicated.
- **Thin content** (<300 words) — critical if the page is a category hub or a redirect target.
- **Internal linking** — orphan pages, crawl depth, pages reachable only via sitemap.
- **URL structure** — IDs, params, underscores, excessive depth.
- **Page weight & text ratio** — text ratio under 10% means the page is almost all code. Compare to a competitor or the previous platform.

---

## Phase C — Alt text

Export **All Image Inlinks**, not the missing-alt filter (Trap 3).

Split by `Link Position` — nav/footer are usually fine; **Content** is where the gap lives.

**Fix CMS collections first.** Gallery and hub pages pull thumbnails from a CMS collection: add **one** alt field, bind it, and every gallery inherits it. This is typically 60–90% of the volume for a fraction of the effort. Hand-written pages come after.

Three buckets: **missing entirely** → fix. **Filename junk** (`alt="Frame-2847.png"`) → fix; it passes a missing-alt check but is worse than useless. **Present and descriptive** → leave alone, *regardless of keywords*. Alt text describes the image; keyword-stuffed alt is worse than none. Decorative images get `alt=""`.

---

## Phase D — Schema, speed, AI discoverability

**Schema** — test in Google's Rich Results Test (`search.google.com/test/rich-results`). **Also test 2–3 competitors.** If they emit `SoftwareApplication` with ratings and the client doesn't, that's a visible SERP gap on every head term. In migration mode, test the *old* site too — dropped schema is a regression and jumps the queue.
Bind schema to CMS fields in the page template; never ask editors to paste JSON-LD per post. Never fabricate `aggregateRating`. See `references/schema-templates.md`.

**Speed** — PageSpeed Insights, mobile. **Record LCP / CLS / INP as numbers.** A linked report with no figures carries no weight with engineering.

**llms.txt / llm.txt** — usually blank by default. See `references/llms-txt-guide.md`.

---

## Phase E — Prioritise (site mode)

An audit listing 40 equally-weighted problems is useless. Sort by **clicks and impressions at risk**, not by count.

| Tier | Definition |
|---|---|
| **Blocker** | Prevents indexing or destroys existing rankings (noindex, staging canonical, blocked robots.txt) |
| **Regression** | The site is *worse* than it was, or than a competitor (dropped schema, lost pages) |
| **Opportunity** | Upside not currently held (new schema, alt text, thin content) |
| **Hygiene** | Real but low-impact (meta length, decorative alt) |

**Lead with clicks at risk, not page counts.** "439 pages missing" panics people; "9 pages carry 78% of the risk" gets action.

**Never chase an audit score of 100.** Tools score what they can measure. They will happily give 95 while a locale page is deleted and canonicals point at staging, and they'll ding you for meta lengths Google rewrites anyway. The metric that matters is clicks and impressions over time.

---

## Phase M — Migration only: inventory diff & redirect map

**Goal:** every old URL classified as OK / MISSING / URL-CHANGED, weighted by traffic.

**Inputs:** old sitemap, new sitemap, GSC Pages (12mo), and Ahrefs/Semrush "Best by links" if available — pages with backlinks need redirects even at zero traffic.

Run `scripts/migration_diff.py`. It normalises URLs (trailing slash, case, encoding — platforms differ, and a naive string match reports 100% of pages as missing), joins GSC clicks, and fuzzy-matches renamed paths by slug.

**Filter GSC to the production host.** Domain properties include `help.`/`affiliate.` subdomains that aren't part of the migration and will pollute the numbers.

**301 = permanent. 302 = temporary.** Migrations use 301s. 302s do not pass link equity and rankings never transfer. Spot-check after launch.

### Migration-specific traps
- **Category paths often gain a folder level** (`/case-study-templates` → `/template-categories/case-study-templates`). The content exists, so it looks fine — but the old URL 404s. **The most-missed finding in any migration.** Diff paths, not page titles.
- **Locale roots (`/ar`, `/pt`) cannot be saved by a redirect.** If the new builder has no localization configured, the traffic is gone. 301-ing a position-6 Arabic page to an English page destroys it. Escalate separately and loudly — never bury it in a spreadsheet row.
- **Author/tag pages look worthless** (near-zero clicks) but every post links to them. Dropping them breaks N internal links and the author-entity/E-E-A-T structure.
- **Massive low-value tails** — keep the top ~25 by clicks, 301 the rest to the category hub. Consolidation is legitimate; doing it to pages that matter is not.
- **Dependency ordering:** if you're 301-ing traffic *into* a page, fix that page **first**. Redirecting 880 clicks into an H1-less, 15-word category page is worse than a 404.

### Launch-day checklist
- [ ] Canonicals resolve to the production domain (view-source, one CMS page)
- [ ] `og:url` resolves to the production domain
- [ ] No `noindex` on anything that should rank
- [ ] robots.txt `Sitemap:` line → production domain
- [ ] Submit new sitemap in GSC
- [ ] Spot-check 5 redirects return **301**, not 302
- [ ] Monitor GSC Coverage + Performance daily for 2 weeks

---

## Reporting standards

- **Separate CONFIRMED from NEEDS VERIFICATION.** State the sample size. "10 of 370 posts checked" is honest; implying full coverage is not.
- **Retract loudly when wrong.** If a finding turns out to be an artifact, say so plainly before continuing.
- **Every finding needs an owner and an action**, not just a description.
- **Say what wasn't checked.** Off-page/backlinks, unaudited CMS pages, missing CWV numbers. An audit that hides its gaps is worse than one that admits them.
