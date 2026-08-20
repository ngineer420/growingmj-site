#!/usr/bin/env python3
"""
check_electricity_rate.py
-------------------------
Guards the one electricity rate the whole site quotes.

Running-cost figures used to be hardcoded as $0.15/kWh in three separate
articles. When the EIA figure moved, nobody moved the articles, and every
dollar amount derived from it was about 19% low for years. This script makes
that failure loud instead of silent.

The rate lives in data/electricity-rate.json. This script walks every HTML
file and fails if:

  1. an article quotes a per-kWh rate that is not the one in the JSON, or
  2. an article quotes the rate without the as-of period next to it, so a
     reader cannot tell how old the number is, or
  3. a derived dollar figure listed in the JSON's "derived_figures" no longer
     matches kwh_per_month * dollars_per_kwh.

Usage:
    python3 scripts/check_electricity_rate.py

To update the rate:
    1. Pull the current value from the EIA .xlsx named in the JSON.
    2. Edit cents_per_kwh, dollars_per_kwh, display, as_of and retrieved.
    3. Recompute "derived_figures" (kwh_per_month * dollars_per_kwh).
    4. Run this script. It names every article still carrying the old value.
    5. Fix those articles. That is the whole procedure.

Exit code 0 if everything agrees, 1 otherwise.
"""

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "electricity-rate.json")

# Any per-kWh rate written as dollars ($0.1782) or cents (17.8&cent;/kWh,
# 17.8 cents/kWh). Entity-aware on purpose: this repo writes &cent; and
# &nbsp;, so a naive search for "17.8¢/kWh" finds nothing while the text is
# right there on the page.
RATE_PATTERNS = [
    re.compile(r"\$0\.\d+\s*(?:&nbsp;|&thinsp;|\s)*/?\s*kWh", re.I),
    re.compile(r"\d+(?:\.\d+)?\s*(?:&cent;|¢|\s*cents?)\s*(?:&nbsp;|&thinsp;|\s)*/?\s*kWh", re.I),
]


def load():
    with open(DATA, encoding="utf-8") as fh:
        return json.load(fh)


def html_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in (".git", ".worktrees", "node_modules")]
        for name in sorted(filenames):
            if name.endswith(".html"):
                yield os.path.join(dirpath, name)


def main():
    cfg = load()
    expected_display = cfg["display"]
    expected_dollars = cfg["dollars_per_kwh"]
    as_of = cfg["as_of"]
    problems = []
    seen = 0

    for path in html_files():
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()

        hits = []
        for pat in RATE_PATTERNS:
            hits.extend(m.group(0) for m in pat.finditer(text))
        if not hits:
            continue

        seen += len(hits)
        for hit in hits:
            normalised = hit.replace("&nbsp;", "").replace("&thinsp;", "").replace(" ", "")
            wanted = expected_display.replace("&nbsp;", "").replace("&thinsp;", "").replace(" ", "")
            if normalised.lower() != wanted.lower():
                problems.append(
                    "%s: quotes %r but data/electricity-rate.json says %s"
                    % (rel, hit, expected_display)
                )

        # The markup wraps, so the as-of phrase can be split across lines.
        # Compare on collapsed whitespace, not raw text.
        flat = re.sub(r"\s+", " ", text)
        if as_of not in flat:
            problems.append(
                "%s: quotes a per-kWh rate but does not show the as-of period "
                "(%r), so a stale number would not be visible to the reader"
                % (rel, as_of)
            )

    for fig in cfg.get("derived_figures", []):
        computed = round(fig["kwh_per_month"] * expected_dollars, 2)
        if abs(computed - fig["dollars_per_month"]) > 0.01:
            problems.append(
                "data/electricity-rate.json: %s (%s) says $%.2f/month but "
                "%s kWh x $%s = $%.2f"
                % (fig["article"], fig["basis"], fig["dollars_per_month"],
                   fig["kwh_per_month"], expected_dollars, computed)
            )

    if problems:
        print("Electricity rate is out of sync (%d problem(s)):\n" % len(problems))
        for p in problems:
            print("  - " + p)
        print("\nThe rate of record is %s (%s), from %s."
              % (expected_display, as_of, cfg["source"]["title"]))
        return 1

    print("OK: %d per-kWh mention(s) across the site, all at %s (%s)."
          % (seen, expected_display, as_of))
    return 0


if __name__ == "__main__":
    sys.exit(main())
