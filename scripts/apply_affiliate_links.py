#!/usr/bin/env python3
"""
apply_affiliate_links.py
-------------------------
Stamps real Amazon Associates tracking links across every HTML file in the
site, replacing the [[AFFILIATE:<id>]] placeholder hrefs with real product/
search URLs (optionally with your Associates tag appended).

This is the ONLY script you need to run once your Amazon Associates
application is approved.

Usage:
    python3 scripts/apply_affiliate_links.py YOUR-AMAZON-TAG-20

    # or, to use the tag already stored in data/affiliate-links.json
    # (set "amazon_tag" there first), just run with no argument:
    python3 scripts/apply_affiliate_links.py

What it does:
    1. Reads data/affiliate-links.json for the id -> url mapping.
    2. Walks every *.html file in the repo.
    3. Replaces href="[[AFFILIATE:some-id]]" with the real URL from the
       JSON file, appending "?tag=YOUR-TAG" (or "&tag=YOUR-TAG" if the URL
       already has a query string).
    4. Prints a summary of how many placeholders were replaced, and warns
       about any placeholder ids it could not find in the JSON file.

Safe to re-run: if you update data/affiliate-links.json later (new
products, new tag), just run it again -- it always re-derives links from
[[AFFILIATE:id]] tokens, so keep a backup or use git to track changes
(running against already-stamped files will simply find no more
placeholders left to replace).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "affiliate-links.json"
PLACEHOLDER_RE = re.compile(r'href="\[\[AFFILIATE:([a-zA-Z0-9\-_]+)\]\]"')


def build_url(base_url: str, tag: str) -> str:
    if not tag:
        return base_url
    separator = "&" if "?" in base_url else "?"
    return f"{base_url}{separator}tag={tag}"


def main():
    if not DATA_FILE.exists():
        print(f"ERROR: could not find {DATA_FILE}")
        sys.exit(1)

    data = json.loads(DATA_FILE.read_text())
    links = data.get("links", {})
    tag = sys.argv[1] if len(sys.argv) > 1 else data.get("amazon_tag", "")

    if not tag:
        print("WARNING: no Amazon tag supplied and none set in affiliate-links.json.")
        print("Links will be stamped WITHOUT a tracking tag (plain URLs only).")
        print("Pass your tag as an argument, e.g.:")
        print("    python3 scripts/apply_affiliate_links.py yourtag-20\n")

    total_replacements = 0
    missing_ids = set()
    html_files = sorted(ROOT.rglob("*.html"))

    for path in html_files:
        text = path.read_text()

        def replace(match):
            nonlocal total_replacements
            aff_id = match.group(1)
            entry = links.get(aff_id)
            if not entry:
                missing_ids.add(aff_id)
                return match.group(0)
            total_replacements += 1
            url = build_url(entry["url"], tag)
            return f'href="{url}"'

        new_text = PLACEHOLDER_RE.sub(replace, text)
        if new_text != text:
            path.write_text(new_text)
            print(f"Updated {path.relative_to(ROOT)}")

    print(f"\nDone. Replaced {total_replacements} placeholder link(s).")
    if missing_ids:
        print("WARNING: these affiliate IDs appear in HTML but have no entry")
        print("in data/affiliate-links.json:", ", ".join(sorted(missing_ids)))


if __name__ == "__main__":
    main()
