---
name: hook-repurposing
description: Repurpose proven short-form video hooks (TikTok, Reels, Shorts) from another app or brand into hooks native to your own product, written for a specific UGC creator persona, plus matching captions — delivered ready to paste into a spreadsheet. Use this skill whenever the user pastes a list of hooks that worked for a different product and wants them adapted, says "repurpose these hooks", "adapt these hooks to my app", "make these product-native", asks for captions for a hook list, or wants new on-screen hook text for a UGC or AI-creator account — even without a source list.
---

# Hook Repurposing

Turn hooks that already performed for another product into hooks for **your** product, written in the voice of a specific UGC persona, plus native captions — delivered ready to paste into Google Sheets (or any spreadsheet).

## The one rule that matters most

**Keep the proven hook's structure almost verbatim. Swap only the product-specific word(s).**

A hook works because of its rhythm, length, capitalization, punctuation and opening formula ("pov:", "don't panic but", "I have genuinely terrible news…", "rage bait question:"). The idea inside is the replaceable part. Rewriting a hook "to fit the product better" throws away the thing that was proven.

The most common failure: rewriting freely. For example, adapting a reading app's hook to an app blocker:

- Source: `non readers will never understand this feeling`
- ❌ Rewrite: `people with 7h screen time will never understand this feeling` — new shape, longer, lost the punch
- ✅ Surgery: `blue light zombies will never understand this feeling` — same shape, one slot swapped

Do surgery, not rewrites. More worked examples are in `references/worked-examples.md`.

| Source (reading app) | Adapted (app blocker, male persona) | What changed |
|---|---|---|
| non readers will never understand this feeling | blue light zombies will never understand this feeling | out-group noun only |
| romanticise your life by actually knowing things | romanticise your life by actually showing up | payoff phrase only |
| girl whatever | bro, whatever | persona register only |
| "you're literally just cheat reading" | "you're literally just cheating at discipline" | product verb only |
| they made scrolling educational | they made scrolling impossible | one word — now carries the product's mechanism |
| this thing OBLITERATED my tiktok addiction | (unchanged) | already fits — leave it |
| [famous university] built an app with the most intimidating ideas | an ivy league grad built an app with the most intimidating screen time rules | authority made true + payoff swapped |

If a hook already fits the product as-is, keep it word for word.

## Workflow

### 1. Identify product, persona, and source

Confirm (or infer from context) three things before writing:
- **Your product** — what it literally does, what's true and live. See `references/product-and-persona-template.md`.
- **The persona account** it will post from — gender, age, register, lifestyle.
- **The source product** the hooks came from — knowing it tells you what its payoff vocabulary is.

If any of these is unclear, ask one short question. Don't start writing on a guess. If the user works with recurring products/personas, suggest saving them into a filled-in copy of the template so future sessions start instantly.

### 2. Map the payoff vocabulary once

Every source app promises something. Work out its payoff words, then pick your equivalents and apply the mapping consistently across the whole set.

Example (reading/knowledge app → app blocker):
- smarter / educated / well-informed → disciplined / locked in / focused
- interesting → present / productive
- reading / knowledge / ideas → showing up / attention / side projects / runs
- "makes scrolling useful" → "makes scrolling impossible" / "won't let me in"

### 3. Find the slot in each hook and swap it

Usually one or two words per hook are tied to the source product. Change only those. Preserve:
- length (roughly the same word count)
- capitalization and ALL-CAPS emphasis (OBLITERATED, K*LLED, THE)
- punctuation, ellipses, quotation marks
- the opening formula and the "turn" of the sentence

### 4. Apply the persona filter

If a phrase is coded to the wrong persona, swap only the coded bit:
- female-coded → male persona: "girl whatever" → "bro, whatever", "rapunzel tower" → "monk era", "kisses for the CEO" → "props to the CEO", "the girl who…" → "the guy who…"
- and the reverse for a female persona

Pull persona-specific details for swaps from the persona's lifestyle (e.g. run clubs, morning runs, side project, 9-5 job, "1% better" for a self-improvement guy; presentations, carousels, client work for a marketer).

### 5. Truth-check every claim

- **Product and authority claims must be true.** These are checkable and get called out in comments. If the source says "[famous university] built…" and that isn't true for you, don't copy it. Use the real credential, phrased as the founder's background ("an ivy league founder built…", "a marketer who's worked with 10M-follower accounts…"), not as the institution building the product. Weaker-but-true beats inflated.
- **Only claim features that are live.** Planned or beta features don't go in hooks.
- **No medical or clinical claims** (ADHD, addiction cures, etc.) unless substantiated.
- **Persona life-story lines are fine** ("got promoted twice at 24", "LinkedIn messages went from 0 to 15") — these are the character's story, not product claims.

### 6. Flag weak fits instead of forcing them

Some hooks are welded to the source product's core (e.g. "Read enough books that…" or "psychology facts that explain…" for a reading app). Still produce a version, but mark it as **weak** so it goes to the end of the test queue.

### 7. Write captions (when asked)

Captions are a separate layer under the video. Rules:
- Native creator voice: lowercase, casual, mid-thought, like an inner aside — not ad copy.
- Never name the product or say "AI". The video does the reveal.
- Complement or slightly undercut the hook ("still a little annoyed it worked tbh").
- Exactly 3 hashtags, lowercase, unbranded (no product or brand tags, no #aitools). Pull from a topic pool that fits the persona's niche.
- If a caption promises something ("part 2", "ask in the comments", "screen time reveal if this gets 100 likes"), flag it as **debt** — it needs follow-up content ready before posting.

### 8. Deliver in Sheets-ready format

Default delivery is a single code block:
- one hook (or caption) per line, in the same order as the source list
- no header row, no numbering, no blank lines
- never start a line with a straight double quote `"` — Google Sheets parses it as a quoted field and breaks the cell. Use curly quotes “ ” instead.
- if both hooks and captions are requested, give two separate code blocks so each pastes into its own column

Only add a table with mechanism / b-roll / flag columns if the user asks for analysis. When they just want the hooks, give just the hooks.

## Format reminders for the video itself

These hooks are on-screen text over silent b-roll — the persona never speaks.
- Clips: 9:16, ~4 s (storytime parts ~10 s), with a sharp expression/energy shift at ~2 s that lands on the hook's "turn".
- No music in generation; trending sounds are added at posting.
- For AI-generated creators: keep the persona's look consistent (same character reference, explicit clothing per clip), mouth closed, no dialogue, and avoid complex physics (eating, crumbs, impacts).

## Hook bank

`references/worked-examples.md` holds a full source → adapted → caption set as a reference for voice and the minimal-edit rule. Read it:
- before writing new hooks, to match voice
- when the user asks for hook ideas without a source list
- to show worked examples of the minimal-edit rule

After a session where the user approves new hooks, offer to add them to their own hook bank so future sessions can check for duplicates.

## Quick self-check before sending

- Did I keep each hook's structure, or did I rewrite it? (If a hook is unrecognizable next to its source, redo it.)
- Is every product/authority claim true and every feature live?
- Is the voice right for this persona?
- Are weak fits and caption debts flagged?
- Is the output one-per-line, no header, no numbers, no straight quotes at line start?
