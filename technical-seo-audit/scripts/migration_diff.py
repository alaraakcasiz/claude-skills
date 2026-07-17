#!/usr/bin/env python3
"""
Migration gap diff: old site URLs vs new site URLs, weighted by GSC traffic.

Usage:
  python migration_diff.py --old old_urls.txt --new new_urls.txt \
      --gsc Pages.csv --host www.example.com --out gap_table.csv

Inputs:
  --old   Text file of old-site URLs or paths (one per line), OR a Screaming Frog
          list-mode Internal HTML export (.csv, uses the 'Address' column).
  --new   Same, for the new/staging site.
  --gsc   GSC Performance > Pages export (columns: Top pages, Clicks, Impressions).
  --host  Only keep GSC rows on this host (excludes help./affiliate. subdomains).

Output: CSV with one row per old-site URL, classified and click-weighted.
"""
import argparse
import sys
from urllib.parse import urlparse, unquote

import pandas as pd


def norm(u: str) -> str:
    """Normalize to a comparable path: lowercase, no trailing slash, decoded."""
    u = str(u).strip()
    if not u:
        return ""
    p = urlparse(u).path if "://" in u else u
    p = unquote(p).lower()
    if not p.startswith("/"):
        p = "/" + p
    return p.rstrip("/") if p != "/" else "/"


def load_urls(path: str) -> list:
    if path.endswith(".csv"):
        df = pd.read_csv(path)
        col = "Address" if "Address" in df.columns else df.columns[0]
        # keep only successful HTML pages if the columns are present
        if "Status Code" in df.columns:
            df = df[df["Status Code"] == 200]
        if "Content Type" in df.columns:
            df = df[df["Content Type"].astype(str).str.contains("html", na=False)]
        vals = df[col].tolist()
    else:
        vals = [l.strip() for l in open(path) if l.strip()]
    return [norm(v) for v in vals if norm(v)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--old", required=True)
    ap.add_argument("--new", required=True)
    ap.add_argument("--gsc")
    ap.add_argument("--host")
    ap.add_argument("--out", default="gap_table.csv")
    a = ap.parse_args()

    old = load_urls(a.old)
    new = set(load_urls(a.new))

    clicks, imps = {}, {}
    if a.gsc:
        g = pd.read_csv(a.gsc)
        url_col = "Top pages" if "Top pages" in g.columns else g.columns[0]
        if a.host:
            g = g[g[url_col].astype(str).str.contains(a.host, regex=False)]
        g["_p"] = g[url_col].map(norm)
        clicks = g.groupby("_p")["Clicks"].sum().to_dict()
        if "Impressions" in g.columns:
            imps = g.groupby("_p")["Impressions"].sum().to_dict()

    # Candidate matches for renamed paths: same final slug, different folder.
    by_slug = {}
    for p in new:
        by_slug.setdefault(p.rsplit("/", 1)[-1], []).append(p)

    rows = []
    for p in dict.fromkeys(old):  # dedupe, preserve order
        c = int(clicks.get(p, 0))
        i = int(imps.get(p, 0))
        if p in new:
            status, action, target = "OK", "KEEP", "Live at same URL"
        else:
            slug = p.rsplit("/", 1)[-1]
            cands = [x for x in by_slug.get(slug, []) if x != p]
            if cands:
                status = "MISSING (URL changed)"
                action = "REDIRECT"
                target = "301 -> " + cands[0]
            else:
                status = "MISSING"
                action = "REBUILD" if c > 0 else "REDIRECT / DROP"
                target = "No match in new site - decide"
        rows.append({
            "URL": p, "Clicks": c, "Impressions": i,
            "Status": status, "Action": action, "Target / Note": target,
        })

    df = pd.DataFrame(rows)
    order = {"REBUILD": 0, "REDIRECT": 1, "REDIRECT / DROP": 2, "KEEP": 3}
    df = df.sort_values(
        ["Action", "Clicks"],
        key=lambda s: s.map(order) if s.name == "Action" else -s,
    )
    df.to_csv(a.out, index=False)

    miss = df[df.Action != "KEEP"]
    tot = df.Clicks.sum() or 1
    print(f"Old URLs: {len(df)} | Missing: {len(miss)}")
    print(f"Clicks at risk: {miss.Clicks.sum():,} of {tot:,} ({100*miss.Clicks.sum()/tot:.1f}%)")
    print("\nTop 15 at risk:")
    print(miss.head(15).to_string(index=False))
    print(f"\nWrote {a.out}")

    # Concentration check — the headline is usually "N pages carry X% of risk"
    if len(miss):
        top = miss.head(10).Clicks.sum()
        if miss.Clicks.sum():
            print(f"\nTop 10 missing pages = {100*top/miss.Clicks.sum():.0f}% of all clicks at risk")


if __name__ == "__main__":
    sys.exit(main())
