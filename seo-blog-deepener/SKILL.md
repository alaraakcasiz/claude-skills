---
name: seo-blog-deepener
description: >
  Deeply optimize and enrich an existing blog post or web page for SEO. Use this skill whenever the user wants to:
  improve, deepen, rewrite, or optimize a blog post or article for search engines; make a blog post a pillar page;
  enrich content with keywords, statistics, internal links, or schema markup; improve meta descriptions or titles;
  or asks to "SEO optimize", "deepen", "enrich", or "make this rank better". Trigger even if the user just pastes
  a URL and says "optimize this" or "improve this for SEO". This skill covers the full end-to-end workflow from
  fetching the page to delivering a production-ready optimized HTML/Markdown file with schema markup suggestions.
---

# SEO Blog Deepener Skill

A full end-to-end workflow for deeply optimizing an existing blog post into a high-ranking, pillar-page-quality article.

---

## Workflow

### Step 1 — Fetch & Audit the Source Page
- `web_fetch` the target URL
- Extract: title, meta description, H1/H2/H3 structure, word count, existing images (note alt text), internal links already present, CTAs
- Note what's missing: stats, examples, depth, keyword density, schema

### Step 2 — Keyword Research
- Identify the **primary keyword** from the URL slug and page title
- `web_search` for: `"{primary keyword}" site:google.com` or `"{primary keyword}" SEO search volume`
- Also search: `"{primary keyword}" competition content` to see what top-ranking pages cover
- Identify: primary keyword, 3–5 secondary/LSI keywords, featured snippet opportunities

### Step 3 — Fetch the Sitemap for Internal Links
- Try `web_fetch` on `{root-domain}/sitemap.xml` or `{root-domain}/sitemap_index.xml`
- Extract all URLs relevant to the blog's topic
- Select 3–6 strong internal link candidates (prefer pillar pages, related posts, product pages)

### Step 4 — Research Statistics & Authoritative Sources
- Search for recent stats (last 2–3 years) from: HubSpot, Content Marketing Institute, Nielsen, Statista, Google, SEMrush, Ahrefs, Moz, Forrester, McKinsey, or niche-specific authority sites
- Find 5–10 data points to embed in the content
- Note sources for inline attribution (e.g. "According to HubSpot's 2024 State of Marketing report...")

### Step 5 — Determine Search Intent
Classify the query intent:
- **Informational**: user wants to learn (→ comprehensive guide format, FAQs, definitions)
- **Commercial**: user is comparing options (→ comparisons, pros/cons, use cases)
- **Transactional**: user wants to act (→ strong CTAs, product mentions)
- **Navigational**: user wants a specific page (→ brand clarity)

Match content depth, format, and CTAs to intent.

### Step 6 — Optimize & Rewrite the Blog Post

**Structure rules:**
- One H1 only (primary keyword + intent match)
- H2s = main topic sections (include secondary keywords naturally)
- H3s = subtopics and supporting details
- Keep original image placements; do NOT change or remove images
- Add/optimize image alt text with keywords

**Content rules:**
- Short paragraphs (2–4 lines max)
- Use bullet points and numbered lists for scannable content
- Bold key terms and phrases
- Embed statistics with source attribution
- Include at least 2 real-world examples or case studies
- Write for E-E-A-T: show experience, cite expertise, link to authoritative sources
- Mention the brand/tool naturally where it adds value — not as spam
- Cover the topic more comprehensively than competitor pages
- Target 2,500–5,000+ words for pillar pages

**Meta optimization:**
- Title tag: 50–60 chars, primary keyword near the front
- Meta description: 150–160 chars, includes keyword + clear value proposition + soft CTA

**Internal linking:**
- Add 3–6 contextual internal links from sitemap research
- Use descriptive anchor text (not "click here")

### Step 7 — Schema Markup Suggestions

Always suggest at least:
- **Article schema** (always — for blog posts)
- **FAQ schema** (if there's a Q&A or FAQ section)
- **HowTo schema** (if there's a step-by-step process)
- **BreadcrumbList schema** (if site has breadcrumbs)

Provide copy-pasteable JSON-LD for each schema type.

### Step 8 — Deliver the Output

Output a complete, production-ready blog post as a `.md` or `.html` file including:
1. Optimized meta title + description (at top as comments or frontmatter)
2. Full rewritten article body
3. Schema markup JSON-LD blocks at the bottom
4. A brief **SEO Summary** section listing: primary keyword, secondary keywords, word count, internal links added, schema types included

---

## Quality Checklist (run before output)

- [ ] Primary keyword in H1, first 100 words, at least 2 H2s, meta title, meta description
- [ ] Secondary keywords distributed naturally
- [ ] 5+ statistics with source attribution
- [ ] 2+ real-world examples
- [ ] 3–6 internal links with descriptive anchors
- [ ] Short paragraphs + bullet points throughout
- [ ] All original images preserved (do not change)
- [ ] Brand mentions feel natural, not spammy
- [ ] Article schema + FAQ or HowTo schema included
- [ ] Word count 2,500+ (pillar page target: 3,500+)
- [ ] Meta description 150–160 chars

---

## Output Format

```
<!-- SEO META -->
<!-- Title: [optimized title, 50-60 chars] -->
<!-- Meta Description: [150-160 chars] -->

# [H1]

[Full article body in Markdown]

---

## Schema Markup

### Article Schema (JSON-LD)
\`\`\`json
{ ... }
\`\`\`

### FAQ Schema (JSON-LD)
\`\`\`json
{ ... }
\`\`\`

---

## SEO Summary
- Primary keyword: ...
- Secondary keywords: ...
- Word count: ~X
- Internal links added: X
- Schema types: Article, FAQ, [HowTo]
```
