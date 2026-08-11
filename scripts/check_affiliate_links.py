#!/usr/bin/env python3
"""Assert no article ships a template placeholder or a dead affiliate link.

Affiliate links on this site are written into the HTML as a placeholder,
`href="[[AFFILIATE:<id>]]"`, and turned into real URLs by running
scripts/apply_affiliate_links.py. That stamping step is manual, so it is
possible to write an article, commit it, and publish it with the raw
placeholder still in the page.

That is exactly what happened: 22 placeholders across 8 articles went live,
rendering `[[AFFILIATE:self-watering-planter]]` as literal text to readers.
Every one of them was a monetised link that earned nothing, on pages whose
whole proposition is that a person who knows the subject wrote them.

Nothing was watching, so nothing caught it. This is the watcher. Run it
before publishing:

    python3 scripts/check_affiliate_links.py

It exits non-zero, naming the file and the gap, if any of the following is
true:

  1. A `[[...]]` template placeholder survives in a published .html page.
  2. An `affiliate-link` anchor has no href, or an empty one -- an anchor
     styled to promise a click that does not go anywhere.
  3. An affiliate href still points at an id rather than a URL.
  4. An affiliate href is missing the Associates tag set in
     data/affiliate-links.json -- an untagged link is a click that earns
     nothing, which is the same defect wearing a different hat.
  5. An id referenced by an article has no entry in
     data/affiliate-links.json, so stamping would silently skip it.
"""

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "affiliate-links.json"

PLACEHOLDER_RE = re.compile(r"\[\[[^\]\n]+\]\]")
ANCHOR_RE = re.compile(r"<a\b[^>]*\bclass=\"[^\"]*\baffiliate-link\b[^\"]*\"[^>]*>")
HREF_RE = re.compile(r"\bhref=\"([^\"]*)\"")
AFFILIATE_ID_RE = re.compile(r"\[\[AFFILIATE:([a-zA-Z0-9\-_]+)\]\]")


def pages():
    """Every published page, i.e. every .html file in the repo."""
    return sorted(p for p in ROOT.rglob("*.html") if ".git" not in p.parts)


def main():
    if not DATA_FILE.exists():
        print(f"ERROR: could not find {DATA_FILE}", file=sys.stderr)
        return 1

    data = json.loads(DATA_FILE.read_text())
    links = data.get("links", {})
    tag = data.get("amazon_tag", "")

    problems = []

    for path in pages():
        where = path.relative_to(ROOT)
        text = path.read_text()

        for match in PLACEHOLDER_RE.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            problems.append(
                f"{where}:{line}: unstamped placeholder {match.group(0)} is live "
                f"on the page. Run: python3 scripts/apply_affiliate_links.py"
            )

        for match in ANCHOR_RE.finditer(text):
            anchor = match.group(0)
            line = text.count("\n", 0, match.start()) + 1
            href = HREF_RE.search(anchor)

            if href is None or not href.group(1).strip():
                problems.append(
                    f"{where}:{line}: affiliate anchor has no href -- it is styled "
                    f"as a link but nothing happens when a reader clicks it: {anchor}"
                )
                continue

            url = href.group(1)
            if not url.startswith("http"):
                problems.append(
                    f"{where}:{line}: affiliate href is not a URL: {url}"
                )
            elif tag and f"tag={tag}" not in url:
                problems.append(
                    f"{where}:{line}: affiliate href is missing tag={tag}, so a "
                    f"click on it earns nothing: {url}"
                )

        for aff_id in AFFILIATE_ID_RE.findall(text):
            if aff_id not in links:
                problems.append(
                    f"{where}: id '{aff_id}' has no entry in "
                    f"data/affiliate-links.json, so stamping will skip it"
                )

    if problems:
        print(f"FAIL: {len(problems)} affiliate link problem(s) found.\n", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1

    checked = sum(len(ANCHOR_RE.findall(p.read_text())) for p in pages())
    print(f"OK: {checked} affiliate link(s) across {len(pages())} page(s); "
          f"no placeholders, no href-less anchors, all tagged {tag}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
