# llms.txt — authoring guide

A markdown file telling LLMs (ChatGPT, Perplexity, Claude, AI Overviews) what the site
is and which pages matter. Most site builders ship it **blank by default** — check
`/llms.txt` and `/llm.txt` (Framer uses the singular).

Not a traditional ranking factor, and there is no proof yet that it drives citations.
But it costs an hour and the downside is zero. Worth doing for any brand where "what's
the best X tool" is a question people ask an LLM.

## Structure (spec)

```
# Brand Name

> One-paragraph blockquote summary. This is the highest-value text in the file.

Prose context: who it's for, what problem it solves, key capabilities as a plain list.

## Section
- [Page Title](https://www.example.com/page): What this page covers.

## Optional
- [Terms](...)
```

Rules:
- H1 = brand name. One `>` blockquote summary. Then prose. Then `##` link sections.
- Every link needs a **description**, not just a title.
- `## Optional` is spec-defined — it signals content that can be skipped when context
  is tight. Put terms/privacy there. Everything above it is treated as core.

## What actually matters

**Use production URLs, never staging.** Same reasoning as canonicals — you don't want
LLMs citing a staging domain. And check every URL resolves *today*; a page that only
exists on the new build will 404 if llms.txt ships before launch.

**Lead with what the product IS and DOES, in citable facts.** When an LLM answers
"best tool for X," it pattern-matches capability descriptions.

- Good: "Applies your brand automatically from your website URL."
- Useless: "Revolutionize your presentations."

**Prioritize comparison content.** `/blog/x-vs-y` and "best tools for X" roundups are
the pages most likely to be pulled when someone asks an LLM to compare options. That's
the GEO play — put them in their own section.

**Keep it current.** The file is read as a whole. A stale product description is worse
than no file.

## Sections that usually earn their place

- Core product / primary pages
- Tools or feature pages (one line each)
- Who it's for (persona/use-case pages)
- Categories
- Guides and comparisons ← the GEO section
- Company (about, contact, press)
- Optional (legal)
