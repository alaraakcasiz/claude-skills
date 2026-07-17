# Claude Skills

Reusable skill files for Claude AI — built for SEO, marketing analytics, content operations, and qualitative research workflows.

Each skill is a structured prompt + reference bundle that turns Claude into a domain-specific operator. Drop any of these into your Claude environment and they work out of the box.

## Skills

| Skill | What it does |
|---|---|
| **[technical-seo-audit](./technical-seo-audit/)** | Full technical and on-page SEO audit — indexability, crawl directives, schema, alt text, internal linking, CMS migration diffing and redirect mapping. Works with Screaming Frog exports, GSC data, and sitemaps. |
| **[saas-ga4-marketing-audit](./saas-ga4-marketing-audit/)** | Standardized SaaS marketing audit from GA4 + GSC exports. Channel performance, funnel analysis, device/geo breakdown, SEO health — produces a full report or presentation. |
| **[market-research-plan](./market-research-plan/)** | Design and plan qualitative, quantitative, or mixed-methods research studies. Interview guides, survey design, thematic analysis frameworks. |
| **[linkedin-post](./linkedin-post/)** | LinkedIn post writing system with hook patterns, formatting rules, and performance-tested constraints. Built from 30-day posting challenge data. |
| **[seo-blog-deepener](./seo-blog-deepener/)** | Deep optimization of existing blog posts for search — keyword enrichment, internal linking, schema markup, meta optimization. |
| **[reddit-date-fetcher](./reddit-date-fetcher/)** | Fetch real Reddit post/comment dates via Arctic Shift archive API. Bypasses Reddit's 403 anti-bot wall entirely. |

## How to use

1. Copy the skill folder into your Claude skills directory
2. Each skill has a `SKILL.md` file (the main prompt) and optionally a `references/` folder with supporting data
3. Claude will automatically trigger the skill based on your request

## About

Built by [Alara Akcasiz](https://www.linkedin.com/in/alaraakcasiz/) — CMO at Decktopus AI, MSc student at NOVA IMS Lisbon. These skills were developed through real production work across SEO, paid media, content ops, and marketing analytics.

## License

MIT
