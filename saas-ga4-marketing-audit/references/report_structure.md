# Audit Report / Deck Structure

Use this as the section order for both the Word doc and the slide deck (deck = one slide per
bullet below, roughly; doc = one H1 section per bullet).

1. **Title** — Client name, "Q_ 20__ Digital Marketing Audit," period covered, prepared-by line.
2. **Executive Summary** — 5-7 bullets, each a complete finding (not a teaser): what was found,
   why it matters, and enough nuance to not be misread (e.g. "X, but Y confounding factor applies"
   rather than a bare stat).
3. **Scope & Methodology** — period, standalone vs YoY, data sources used, and a data-quality
   callout box (stale audiences, known bot sources, filters applied) up front so the reader carries
   it through the rest of the doc.
4. **Channel Performance** — table: channel, sessions, engagement rate, conversion/key-event rate,
   revenue. Prose: most-balanced channel, highest-volume-weakest-quality channel, any channel whose
   efficiency needs a causal explanation (e.g. "PMax residual effect" rather than a mystery),
   any channel that's deliberately low-conversion by design (don't flag as broken).
5. **Funnel** — stage-by-stage table with rates. Call out the single biggest drop-off. Mark any
   audience-based figures as provisional if audiences are stale.
6. **SEO Deep-Dive** (if GSC available) — brand vs non-brand split; the single highest-value
   keyword-gap finding with a volume-gated, market-aware recommendation (not a copy-paste-across-
   locales recommendation); any off-product content vertical driving non-brand volume, framed as a
   strategic question; page-level CTR issues with impression volume stated next to every one, and a
   note on whether the fix is worth dedicated effort or is a quick win.
7. **Device** — GSC search-side table + GA4 behavior-side table side by side; name the contrast
   explicitly if search performance and on-site conversion tell different stories.
8. **Geography** — country table (active users, engagement/bounce, revenue, ARPU); call out
   highest-ARPU markets, high-volume-low-ARPU markets, and any anomalies (implausible $0 revenue in
   a market with working payment rails, implausible CTR-position combinations).
9. **Social / Creator / Affiliate** — source/medium breakdown by platform; campaign-dimension
   breakdown of any tagged program; explicitly separate "tagged campaign" value from "organic/
   untagged" value; note any program's active window if it wasn't running the full period; name a
   standout performer if the data supports it (e.g. one creator or one content format worth
   replicating elsewhere, including in the client's own organic strategy).
10. **Pages/Content** — top pages, notable engagement/bounce outliers, any off-product content
    finding already surfaced in SEO.
11. **Action Plan** — three tiers (High / Medium / Low-or-Monitor). Each item is a single, concrete
    sentence — no vague "improve X." High priority = high confidence + meaningful volume/impact.
    Medium = clear but lower-cost or lower-certainty. Monitor = things worth watching but not
    acting on yet (e.g. "see how a recent product change shifts this next period").
12. **Data Quality Notes** — every caveat raised earlier in the doc, collected in one place: stale
    audiences, anomalous traffic clusters, unfilterable known bot sources, minor cross-report
    reconciliation gaps.

## Tone conventions

- State findings, then the nuance that prevents misreading them — don't bury the caveat in a
  separate section only.
- Never recommend heavy investment without stating the volume/impact ceiling next to it.
- When a client corrects an interpretation mid-engagement, that correction must propagate to every
  section it touches — exec summary, the detailed section, and the action plan — not just the
  place it was raised.
- Prefer concrete numbers over adjectives ("conversion rate 0.475%, a third of Paid Search's,"
  not "conversion is somewhat weaker").
- Distinguish observations you're confident in from ones that need one more data pull to confirm —
  say so explicitly ("this would need a landing-page-by-source cut to confirm") rather than
  presenting a hypothesis as settled.
