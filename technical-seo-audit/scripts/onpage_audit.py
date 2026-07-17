#!/usr/bin/env python3
"""
On-page + technical audit of a Screaming Frog "Internal > HTML" export.

CRITICAL: runs a crawl-artifact check FIRST. If the crawl was rate-limited,
the on-page data is garbage and must not be reported. See SKILL.md, Trap 2.

Usage:
  python onpage_audit.py internal_all.csv [--images image_details.csv]
"""
import argparse
import sys

import pandas as pd

pd.set_option("display.width", 250)
pd.set_option("display.max_colwidth", 80)


def artifact_check(d: pd.DataFrame) -> bool:
    """Detect rate-limited / SPA-shell crawls. Returns True if data looks poisoned."""
    print("=" * 70)
    print("STEP 0 — CRAWL ARTIFACT CHECK (do not skip)")
    print("=" * 70)

    poisoned = False

    # Signature 1: many pages sharing an identical byte size
    if "Size (bytes)" in d:
        top = d["Size (bytes)"].value_counts()
        if len(top) and top.iloc[0] >= 10 and top.iloc[0] / len(d) > 0.25:
            print(f"!! {top.iloc[0]} pages share an IDENTICAL byte size ({top.index[0]:,} bytes)")
            print("   -> Server served the same shell repeatedly. Classic rate-limit signature.")
            poisoned = True

    # Signature 2: one title dominating
    if "Title 1" in d:
        t = d["Title 1"].value_counts()
        if len(t) and t.iloc[0] / len(d) > 0.25:
            print(f'!! {t.iloc[0]} pages share the title "{t.index[0]}"')
            poisoned = True

    # Signature 3: asymmetry — a subset renders fully, the rest are empty
    if "Word Count" in d:
        empty = (d["Word Count"] < 50).sum()
        full = (d["Word Count"] > 300).sum()
        if empty > 10 and full > 0:
            print(f"!! {empty} near-empty pages AND {full} full pages in the SAME crawl.")
            print("   -> Asymmetry means ARTIFACT, not a real problem. A genuine issue")
            print("      affects all pages of a type equally.")
            poisoned = True

    if poisoned:
        print("\nVERDICT: DATA IS UNRELIABLE. Do not report on-page findings.")
        print("Retest: crawl 10 of the 'empty' URLs alone. If they come back correct,")
        print("it was rate limiting. Then crawl in batches of ~50.")
        print("Only STATUS CODES are trustworthy from this file.\n")
    else:
        print("No artifact signature detected. On-page data appears usable.\n")
    return poisoned


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--images")
    a = ap.parse_args()

    d = pd.read_csv(a.csv)
    if "Content Type" in d:
        d = d[d["Content Type"].astype(str).str.contains("html", na=False)]
    d = d.copy()
    print(f"Pages: {len(d)}\n")

    poisoned = artifact_check(d)

    # ---- Rendering-independent findings (always safe to report) ----
    print("=" * 70)
    print("HTTP-LEVEL FINDINGS (trustworthy regardless of rendering)")
    print("=" * 70)
    if "Status Code" in d:
        print("Status codes:", d["Status Code"].value_counts().to_dict())
        bad = d[~d["Status Code"].isin([200])]
        if len(bad):
            print("\nNon-200 URLs — NOTE: a crawler cannot invent URLs.")
            print("Every 404 here means SOMETHING LINKS TO IT. Find the source (Inlinks tab).")
            print(bad[["Address", "Status Code"]].to_string(index=False))

    # ---- The two silent killers ----
    print("\n" + "=" * 70)
    print("THE TWO SILENT KILLERS")
    print("=" * 70)
    if "Canonical Link Element 1" in d:
        c = d["Canonical Link Element 1"].astype(str)
        hosts = c[c != "nan"].str.extract(r"https?://([^/]+)")[0].value_counts()
        print("Canonical target hosts:", hosts.to_dict())
        print("  -> If ANY point at a staging domain, that MUST resolve to production")
        print("     on launch day. Re-check via view-source after DNS cutover.")
        print(f"  -> Pages with NO canonical: {(c == 'nan').sum()}"
              + ("  (unreliable — crawl is poisoned)" if poisoned else ""))

    for col in ("Meta Robots 1", "X-Robots-Tag 1"):
        if col in d:
            ni = d[d[col].astype(str).str.contains("noindex", case=False, na=False)]
            if len(ni):
                print(f"\n!! NOINDEX found in {col} on {len(ni)} page(s):")
                print(ni["Address"].to_string(index=False))
                print("   A noindex on a HUB page cuts the discovery path to everything it links to.")

    if poisoned:
        print("\nStopping here — on-page checks skipped because the crawl data is unreliable.")
        return

    # ---- On-page ----
    print("\n" + "=" * 70)
    print("ON-PAGE FINDINGS")
    print("=" * 70)

    if "H1-1" in d:
        m = d[d["H1-1"].isna()]
        print(f"\nMissing H1: {len(m)}")
        if len(m):
            print(m["Address"].to_string(index=False))
            print("  -> Usually TEMPLATE-level. One fix cascades to every page of that type.")
    if "H1-2" in d:
        dup = d[d["H1-2"].notna()]
        print(f"\nDuplicate H1 (2+ on one page): {len(dup)}")
        if len(dup):
            print("  -> Common in responsive builders rendering desktop + mobile H1 into the DOM.")
            print(dup["Address"].to_string(index=False))

    if "Title 1 Length" in d:
        lng = d[d["Title 1 Length"] > 60]
        print(f"\nTitles > 60 chars: {len(lng)} (Google truncates ~60ch / 600px)")
        if len(lng):
            print("  -> Usually an appended '| Brand' suffix on already-full titles. Trim it globally.")
            print(lng.nlargest(10, "Title 1 Length")[["Address", "Title 1 Length"]].to_string(index=False))
        print("Missing titles:", d["Title 1"].isna().sum())
        d_ = d[d["Title 1"].notna()]
        print("Duplicate titles:", d_["Title 1"].duplicated(keep=False).sum())

    if "Meta Description 1 Length" in d:
        print(f"\nMeta descriptions > 155 chars: {(d['Meta Description 1 Length'] > 155).sum()}")
        print("Missing meta descriptions:", d["Meta Description 1"].isna().sum())

    if "Word Count" in d:
        thin = d[d["Word Count"] < 300].sort_values("Word Count")
        print(f"\nThin pages (<300 words): {len(thin)}")
        if len(thin):
            print("  -> CRITICAL if any of these is a REDIRECT TARGET. Fix the page BEFORE")
            print("     shipping redirects into it.")
            print(thin[["Address", "Word Count"]].head(10).to_string(index=False))

    if "Size (bytes)" in d:
        mb = d["Size (bytes)"] / 1048576
        print(f"\nPage weight: median {mb.median():.2f} MB | >1MB: {(mb > 1).sum()}")
        print("  -> Compare to the OLD site. Modern builders often ship 4-16x heavier pages.")
        if "Text Ratio" in d:
            print(f"Text ratio: median {d['Text Ratio'].median():.1f}%  (<10% = almost all code)")

    # ---- Images ----
    if a.images:
        print("\n" + "=" * 70)
        print("ALT TEXT")
        print("=" * 70)
        im = pd.read_csv(a.images)
        im["alt"] = im.get("Alt Text", pd.Series(dtype=str)).fillna("").astype(str).str.strip()
        im["has"] = im["alt"] != ""
        print(f"Image instances: {len(im)} | unique: {im['To'].nunique()}")
        print(f"WITH alt: {im.has.sum()} ({100*im.has.mean():.0f}%) | "
              f"WITHOUT: {(~im.has).sum()} ({100*(~im.has).mean():.0f}%)")
        if "Link Position" in im:
            print("\nBy position (nav/footer are usually fine; Content is where the gap is):")
            print(im.groupby("Link Position")
                    .agg(total=("To", "size"), missing=("has", lambda s: (~s).sum()))
                    .to_string())
            c = im[im["Link Position"] == "Content"]
            if len(c):
                g = (c.groupby("From")
                       .agg(imgs=("To", "size"), missing=("has", lambda s: (~s).sum()))
                       .sort_values("missing", ascending=False))
                print("\nWorst pages (content images missing alt):")
                print(g.head(10).to_string())
                print("\n  -> Gallery/hub pages pulling CMS thumbnails are the big win:")
                print("     add ONE alt field to the CMS collection, bind it, and every")
                print("     gallery inherits it. Do CMS fields before hand-written pages.")
        # useless alt (filename junk)
        junk_re = (r"^(?:Frame|Group|image|IMG|Rectangle|Screenshot)[\s_-]*\d*$"
                   r"|\.(?:png|jpg|jpeg|webp|svg)$")
        junk = im[im.has & im["alt"].str.contains(junk_re, case=False, regex=True)]
        if len(junk):
            print(f"\n!! {len(junk)} images have FILENAME-JUNK alt (e.g. 'Frame-2847.png').")
            print("   These pass a 'missing alt' check but are worse than useless.")


if __name__ == "__main__":
    sys.exit(main())
