# GA4 / GSC Export Checklist

Work with whatever subset arrives first; this is a checklist to request against, not a blocker.

## Google Analytics 4 (required for the core audit)

| Report | GA4 location | Used for |
|---|---|---|
| Traffic Acquisition (Session default channel group) | Reports > Acquisition > Traffic acquisition | Channel-level sessions, engagement rate, key-event rate, revenue |
| User Acquisition (First user primary channel group) | Reports > Acquisition > User acquisition | New users, ARPU, avg. purchase revenue per channel; also pull a **campaign-dimension** version (not just source/medium) to catch creator/influencer/UTM-tagged traffic hiding in a generic bucket |
| User Acquisition cohorts | Explore > Cohort or the acquisition report's cohort view | Retention-flavored view of acquisition, useful for creator/campaign attribution cross-checks |
| Landing Page | Reports > Engagement > Landing page (or Explore) | Sessions/conversion by entry page — where the funnel actually starts |
| Device category | Reports > Tech > Device category (or Explore) | On-site behavior (engagement, revenue) by device — compare against GSC device data |
| Demographic details: Country | Reports > User > Demographics > Country | Active users, bounce rate, engagement rate, revenue, ARPU by country |
| Pages and screens | Reports > Engagement > Pages and screens | Page-level views, bounce/engagement rate, key events; watch for 404/"not found" volume and off-product content verticals |
| Audiences | Advertising > Audiences (or the Audiences report) | Segment-level revenue/ARPU — **confirm definitions are current before relying on specific numbers** |
| Events | Reports > Engagement > Events | Find the actual key/conversion events (sign_up, purchase, etc.) and their unique-user counts — this is how you compute true funnel rates, not just "key events" totals |

## Google Search Console (optional but strongly recommended for the SEO section)

| Report | Used for |
|---|---|
| Queries | Brand vs non-brand split; identify core product-intent keywords and their position/CTR |
| Pages | Per-page clicks/impressions/position/CTR — this is where the "ranks well but nobody clicks" pattern shows up |
| Countries | Position/CTR by country — cross-check against GA4 country revenue for anomalies |
| Devices | Position/CTR by device — compare against GA4 device behavior |
| Search Appearance | Rich result / snippet type performance (review snippets, translated results, etc.) |

## If a report is missing

- **No GSC data**: skip the SEO deep-dive section or mark it "pending GSC export" in the report;
  don't guess at query-level findings from GA4 alone.
- **No campaign-dimension User Acquisition**: flag that creator/influencer/UTM attribution can't be
  fully verified yet, rather than assuming a source/medium-only view means UTMs aren't working —
  the campaign dimension is where UTM-tagged traffic actually surfaces.
- **No Events report**: fall back to the "Key events" total in Traffic Acquisition, but note that
  this is usually a single event type (often "purchase") and won't show a full multi-stage funnel.
- **CSV unavailable, screenshots only**: work from screenshots but flag that exact figures should
  be double-checked against a CSV export before finalizing the report.
