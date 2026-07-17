# Screaming Frog: correct configuration for a migration audit

The free licence caps at 500 URLs and blocks JS rendering and speed config.
**Both limits are workable.** Most "we need a paid licence" conclusions are wrong —
the real blocker is usually rate limiting, not licensing.

## Modes

**Never use Spider mode for inventory.** Spider mode follows `<a href>` from a seed
URL. Template galleries and blog listings commonly use load-more buttons or JS
pagination, so the crawler dead-ends and silently returns a fraction of the site.

Real example: a Spider crawl of a Webflow site returned 88 pages — zero blog posts —
while GSC showed 614 blog URLs earning clicks. The blog wasn't broken; it was
undiscoverable by link-following.

**Always use List mode:**
`Mode → List → Upload → Download XML Sitemap → paste https://site.com/sitemap.xml`

This bypasses link discovery entirely. If the CMS puts it in the sitemap, you get it.

## Rate limiting (the big one)

Edge-hosted builders (Framer especially) throttle aggressively. Past their limit,
they return a **generic SPA shell** instead of the real page — same byte size, default
title, no H1, ~15 words. It looks exactly like "the CMS import failed."

**Diagnostic:** if a *subset* of pages returns full correct data in the same crawl
while the rest are identical empty shells, it is rate limiting. A genuine import
failure affects all pages of a type equally. **Asymmetry means artifact.**

**Fixes, in order of preference:**
1. Paid: `Config → Speed → Max Threads = 1`, `Max URI/s = 1`
2. Free: crawl in batches of ~50 URLs. Slow, but the data comes back clean.
3. Free: audit the non-CMS pages first (usually 30–60 URLs) — under any limit,
   and it covers the highest-traffic pages.

## JS rendering — usually NOT needed

Framer, Webflow and most builders **server-render metadata**. Title, meta description,
canonical, and OG tags are in the raw HTML before any JS runs.

**Verify before assuming you need JS:** open a page, `Ctrl+U` (View Source, *not*
Inspect Element), `Ctrl+F` for `<title>`. If the real title is there, a plain HTML
crawl can read it, and the free licence is sufficient.

If the raw source genuinely lacks metadata, you need JS rendering (paid) — or use
Ahrefs/Semrush Site Audit, which render JS and have no URL cap.

## Exports to request

| Export | Path | What it answers |
|---|---|---|
| Internal HTML | `Internal → HTML → Export` | Titles, metas, H1/H2, canonicals, indexability, word count, size |
| All Image Inlinks | `Bulk Export → Images → All Image Inlinks` | Alt text — **use this, not the "missing alt" filter** |
| All Inlinks | `Bulk Export → Links → All Inlinks` | Broken link sources, path-relative links, true orphans |
| Missing Alt Attribute **& Text** | `Bulk Export → Images → ...` | Superset of no-alt and empty-alt (the other two filters each catch half) |

**Never trust an empty "missing alt" export.** Zero rows can mean "nothing missing"
*or* "images were never crawled." Check the denominator in the Images tab. Use
All Image Inlinks so you see every image and its actual alt value — that also catches
filename-junk alt (`alt="Frame-2847.png"`), which passes a missing-alt check but is
worse than useless.

## Reading 404s

A crawler cannot invent URLs. **Every 404 in a crawl means something links to it.**
Click the URL → **Inlinks** tab (bottom pane) → see the source page and anchor text.

Check the **Link Path** column for `Path-Relative`. A relative href (no leading slash)
resolves differently on every page it appears on. In component-based builders, one
bad component generates a *different* broken URL on each page it's placed. Fix the
component, not the individual URLs — then re-crawl to see how far it spread.

## Config for image/alt data

`Config → Spider → Crawl → Images` must be ticked, or image exports come back empty
and you'll misread that as "no problems."
