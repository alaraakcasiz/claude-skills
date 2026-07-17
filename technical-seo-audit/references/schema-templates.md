# Schema markup templates (JSON-LD)

## Before you write anything

1. **Test the OLD site first** at https://search.google.com/test/rich-results
   Migration frequently drops schema. If the old site had `Article` and the new one
   has nothing, that is a **regression** — the only class of finding that makes the
   new site worse than what you already have. It jumps the queue.
2. **Steal your own markup.** If the old site validates, view-source, find the
   `<script type="application/ld+json">` block, and port it. It's already written
   and already passing.
3. **Check competitors.** Run 2–3 competitors through the Rich Results Test. If they
   emit `SoftwareApplication` with ratings and you don't, that's a visible SERP gap
   on every head term.

## Implementation rule

**Bind schema to CMS fields in the page template.** Add a code/embed block to the
collection page layout and reference the fields you already have (title, meta
description, featured image, publish date, author).

Do **not** create a per-post custom-code field for editors to paste JSON-LD into.
It won't be applied retroactively to existing posts, and every post becomes a chance
for a malformed block. Reserve manual fields only for post-specific extras (HowTo,
FAQ).

Validate one page per type before rolling out. A broken JSON-LD block on 370 pages
is worse than none.

---

## Article — blog posts

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{Post Title}",
  "description": "{Meta Description}",
  "image": "{Featured Image URL}",
  "datePublished": "{Publish Date}",
  "dateModified": "{Updated Date}",
  "author": {
    "@type": "Person",
    "name": "{Author Name}",
    "url": "https://www.example.com/author/{author-slug}"
  },
  "publisher": {
    "@type": "Organization",
    "name": "{Brand}",
    "logo": {"@type": "ImageObject", "url": "https://www.example.com/logo.png"}
  },
  "mainEntityOfPage": "https://www.example.com/blog/{slug}"
}
```

`author.url` must resolve. Author schema pointing at a 404 is a validation warning and
kills the E-E-A-T signal — this is a second reason not to drop author pages in a
migration.

While in this template, also fix `og:type` → `article` (builders default it to
`website`).

## SoftwareApplication — SaaS product pages

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "{Product}",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web",
  "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.6",
    "reviewCount": "REAL_NUMBER"
  }
}
```

**Never fabricate `aggregateRating`.** Pull verifiable numbers from G2/Capterra or
**omit the property entirely** — the rest of the markup still works. Invented review
data is a manual-action risk.

## FAQPage

Only mark up FAQs **visible on the page**. Marking up hidden content is a violation.

Google restricted FAQ rich results in 2023 to government and health sites, so you
likely won't get the SERP accordion. It still helps LLMs and AI Overviews parse your
Q&A — which is the real reason to do it if GEO/AEO matters to you.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "{Question}",
    "acceptedAnswer": {"@type": "Answer", "text": "{Answer}"}
  }]
}
```

## BreadcrumbList

Worth it wherever you have a real hierarchy (`/templates` → `/category/x` →
`/templates/y`). Replaces the URL in the SERP with a clickable path.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Templates", "item": "https://www.example.com/templates"},
    {"@type": "ListItem", "position": 2, "name": "{Category}", "item": "https://www.example.com/category/{slug}"},
    {"@type": "ListItem", "position": 3, "name": "{Page}"}
  ]
}
```

Pairs with adding **visible** breadcrumb navigation.

## Organization — sitewide, once

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{Brand}",
  "url": "https://www.example.com",
  "logo": "https://www.example.com/logo.png",
  "sameAs": ["{LinkedIn}", "{X}", "{G2}"]
}
```

## Validate

- **Rich Results Test** — what Google will actually show
- **validator.schema.org** — catches syntax errors Google's tool silently ignores
