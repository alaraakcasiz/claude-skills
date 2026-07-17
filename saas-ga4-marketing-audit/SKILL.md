---
name: saas-ga4-marketing-audit
description: Run a standardized SaaS digital marketing audit from Google Analytics 4 (and optionally Google Search Console) exports. Use this skill whenever the user asks for a "digital marketing audit," "GA4 audit," "marketing performance review," or wants a periodic (monthly/quarterly) deep-dive into a SaaS client's channel performance, funnel, SEO, device/geo behavior, and social/creator programs — for Decktopus or any other client/consulting engagement. Trigger this any time the user uploads GA4 CSV exports (Traffic Acquisition, User Acquisition, Landing Page, Device, Country/Demographics, Pages and Screens, Audiences, Events) and/or GSC exports (Queries, Pages, Countries, Devices, Search Appearance) and wants them analyzed, synthesized, or turned into an audit report/presentation. Also trigger on requests like "analyze this GA4 data," "build me a marketing audit for [client]," or "do our quarterly audit."
---

# SaaS GA4 Digital Marketing Audit

A repeatable framework for turning raw GA4 + GSC exports into a structured, client-ready digital
marketing audit — channel performance, funnel, SEO, device/geo behavior, social/creator programs,
and a prioritized action plan. Built from a full audit engagement (Decktopus AI, Q2 2026) and
generalized for reuse across clients.

## When to use this

Use this skill any time the person is running (or wants to run) a periodic marketing audit off
GA4/GSC exports for a SaaS product — their own company or a consulting client. It applies whether
they have all the data ready or want to build it up conversationally over multiple uploads across
a session.

## Core operating principles

These came directly out of client feedback and should not be skipped:

1. **Standalone-period first, YoY second.** Default to analyzing the requested period on its own
   terms (efficient channels, funnel leaks, growth areas). Only bring in YoY comparisons if asked,
   and even then, flag confounding factors (budget changes, paused campaigns, bot-filter changes)
   before drawing conclusions from the delta.
2. **Volume-gate every "fix this" recommendation.** Before recommending effort on any page/channel/
   keyword, check its absolute impression/session/revenue volume. A page ranking #1 with 300
   impressions is a quick-win at best, not a priority investment. State the volume explicitly next
   to any CTR/ranking observation.
3. **Don't transplant practices across markets/languages uncritically.** If one locale (e.g. /ar)
   outperforms another (e.g. /en) for the same intent, resist recommending "copy what worked
   there." Different markets have different competitive intensity — note the gap, recommend the
   underperforming locale get its own independent optimization, not a copy-paste.
4. **Distinguish "channel is broken" from "channel is under-resourced."** Before calling a channel
   or program underperforming, check whether it was fully staffed/funded for the whole period
   (e.g. a creator program paused mid-quarter). Read partial-period activity as partial-period,
   not as a verdict on the channel.
5. **Flag data quality before drawing conclusions from it.** Always check for: outdated/stale
   audience definitions, bot traffic signatures (see below), and known unfilterable traffic
   sources the client has already told you about. State these as caveats near the findings they
   affect, not just in a footnote.
6. **Distinguish "cost of fixing" from "value of fixing."** For CTR/title-tag issues, compute the
   realistic upside (impressions × plausible CTR delta) before recommending a project around it.
7. **Attribution has structural blind spots — say so.** Last-click models cannot see "saw it on
   LinkedIn, then searched brand name on Google" — that shows up as Direct or brand Organic
   Search. Note this explicitly wherever a channel's true influence is likely underrepresented,
   rather than treating the reported number as ground truth.
8. **When the client corrects an interpretation, propagate the correction everywhere,** including
   already-written report sections, executive summary bullets, and the action plan — not just the
   sentence where it was raised.

## Workflow

### 1. Scope the engagement

Ask (or infer from context) before diving into data:
- Client name and product category
- Period to analyze (and whether YoY/prior-period comparison is wanted — default: no, standalone)
- Data format available: CSV export vs screenshot (CSV strongly preferred for clean parsing)
- Whether GSC data is available in addition to GA4 (recommended but optional)
- Any known context that should shape interpretation: paused campaigns, budget changes, known bot/
  spam sources, recent product changes (e.g. new mobile app), ongoing programs (creators,
  affiliates) and their active windows

### 2. Collect the right exports

See `references/export_checklist.md` for the full list of GA4 and GSC reports this framework is
built around, what each is used for, and what to do if a report is missing. Work incrementally —
don't block on having every report before starting; analyze what's available and note gaps.

### 3. Analyze incrementally, in conversation

Work through data as it arrives rather than waiting for a complete bundle. Suggested order (skip
what's unavailable, adapt order to what the client uploads first):

1. **Channel performance** — sessions, engagement rate, conversion rate (key-event rate), revenue
   per channel. Identify most-efficient vs highest-volume-but-weak channels.
2. **Funnel** — new users → sign-up → purchase (or the client's equivalent stages). Compute rates
   at each stage; identify the biggest drop-off. Treat any audience-segment-based funnel detail
   (e.g. cart-abandonment audiences) as provisional if the client hasn't confirmed audience
   definitions are current.
3. **SEO deep-dive** (needs GSC) — brand vs non-brand click/impression split; identify high-
   impression, high-position, low-CTR pages (title/meta problem, volume-gated per principle #2);
   identify core product-intent non-brand keywords and check their ranking position, comparing
   across locales carefully (principle #3).
4. **Device** — compare GSC search-side device performance (position/CTR) against GA4 on-site
   behavior (engagement, revenue) by device. These often tell different stories — say both.
5. **Geography** — active users, bounce/engagement rate, revenue, and ARPU by country. Flag: (a)
   high-ARPU markets as investment signals, (b) high-volume/low-ARPU markets as scale-not-value
   markets, (c) any country with revenue that contradicts known payment-capability facts (real
   anomaly, not infra excuse), (d) any country with GSC CTR/position patterns that don't make
   statistical sense (see data-quality section below).
6. **Organic social & creator/affiliate programs** — break down by source/medium AND by campaign
   dimension separately (campaign-tagged influencer/creator traffic often hides inside a generic
   source/medium bucket like "referral" — check both). Compare creator-tagged campaigns against
   the residual untagged/organic bucket to see where real value concentrates. Always check whether
   any program was active for the full period before judging its performance.
7. **Pages/content** — top pages by volume, bounce/engagement outliers, any off-brand/off-product
   content verticals driving disproportionate traffic (flag as a strategic question: is this
   deliberate, and does the business have an equivalent product-relevant channel?).

### 4. Data quality checks (run these regardless of what else is analyzed)

- **Anomalous CTR-by-position clusters in GSC**: flag any country/segment where CTR is high (e.g.
  >5%) at a poor average position (e.g. >20) — this combination is close to statistically
  impossible for organic human behavior and usually signals bot/automated-click traffic or
  rank-tracking tools. Cross-reference against any known bot traffic sources the client has
  mentioned.
- **Stale audiences**: ask whether GA4 Audience definitions are current before leaning on them for
  specific claims.
- **Cross-report reconciliation**: minor session/user count mismatches between reports (e.g.
  Landing Page vs Traffic Acquisition totals) are normal (different attribution/dedup logic) —
  note once, don't treat as an error requiring resolution.
- **Known unfilterable traffic**: if the client mentions a specific bot/spam source they can't
  filter (e.g. a particular query parameter or affiliate), note it as a standing caveat rather than
  re-investigating it each time.

### 5. Build the deliverable(s)

Default to a conversational, incremental analysis in chat while data is coming in (no artifacts
needed unless requested — this keeps the working session light). Once the client says something
like "turn this into a report," produce:

- **A Word doc audit report** — use the `docx` skill. Structure: Executive Summary → Scope &
  Methodology → Channel Performance → Funnel → SEO Deep-Dive → Device → Geography → Social/Creator
  → Pages → Action Plan (High/Medium/Low or Monitor) → Data Quality Notes. See
  `references/report_structure.md` for the full section-by-section template and tone guidance.
- **A slide deck** (if requested) — use the `pptx` skill. Mirror the report's structure at
  presentation depth: one slide per major finding, stat callouts, native tables/charts, a
  three-column prioritized action plan slide, and a closing data-quality slide. Pick a palette
  that reads as "analytics/audit" (navy/teal/coral works well) rather than the client's own brand
  colors, unless asked to match brand.
- Always let the client review and correct the draft before finalizing — expect at least one
  revision pass, and when they correct something, check the *entire* document/deck for other
  places the same correction applies (principle #8).

## Adapting this for a new client

This framework is channel/funnel-agnostic but was built on a subscription SaaS with: sign-up →
purchase as the core funnel, a creator/influencer program, multilingual SEO pages, and a
Solutions/Use-Case page architecture. For a new client:
- Swap the funnel stages to match their actual product motion (e.g. trial → activation → paid).
- Swap "creator/influencer" for whatever their social/affiliate structure actually is.
- Keep the core analytical moves (channel efficiency, volume-gating, data quality checks,
  cross-locale caution, attribution blind-spot caveats) — these are product-agnostic.
- Ask the client for their brand keyword list up front so brand-vs-non-brand query
  classification can be done correctly from the start.

## Reference files

- `references/export_checklist.md` — full list of GA4/GSC reports this framework uses, what each
  is for, and fallback guidance when a report isn't available.
- `references/report_structure.md` — section-by-section template for the audit doc/deck, with the
  tone and framing conventions (direct, evidence-grounded, volume-gated recommendations, explicit
  caveats) that this skill's outputs should follow.
