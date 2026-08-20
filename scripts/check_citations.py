#!/usr/bin/env python3
"""Guard for the citation standard described in README.md.

The standard is only worth anything if the markers actually resolve. A
superscript "7" that points at a source list with six entries is worse than
no marker at all: it looks checked and isn't. This script fails the build on
the mechanical half of the standard so that review can spend its attention on
the editorial half.

What it checks, per article:

  1. Every <a class="cite" href="#src-N"> resolves to an <li id="src-N"> on
     the same page.
  2. Every <li id="src-N"> is pointed at by at least one marker. An orphaned
     entry means a claim was cut and its source was left behind, or a marker
     was never added.
  3. Source ids run 1..n with no gaps and no duplicates, and appear in the
     Sources block in that order — the standard numbers them in order of
     first appearance in the article.
  4. Markers appear in ascending order of first use down the page, which is
     the same rule seen from the other end.
  5. Every source entry contains a link, and every marker carries a title.
  6. No marker appears inside a heading, inside the .key-facts short answer,
     or inside a .faq-item — those restate claims already marked in the body,
     and the FAQ is mirrored into FAQPage JSON-LD where markup cannot follow.
  7. An article with a Sources block has at least one marker, and vice versa.

What it deliberately does NOT check: whether a number is right, whether the
source says what the article claims, or whether a claim that needs a marker
has one. No script can do those. See README.md.

Run from the repo root:

    python3 scripts/check_citations.py

Exit status is non-zero if anything failed, and every failure names the file
and the line.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Pages that predate the standard and are scheduled for the batch rewrites.
# These grew a Sources block out of links that were already in their prose,
# before there was a marker to tie a claim to an entry. Neither wrong nor
# conforming. Delete a name from here when its article has been through the
# standard — the point of the list is that it shrinks to nothing.
#
#   propagating-plants-from-cuttings.html -> issue #19 (voice/citation batch 2)
EXEMPT = {
    "propagating-plants-from-cuttings.html",
}

MARKER_RE = re.compile(r'<a\b[^>]*class="cite"[^>]*>', re.I)
HREF_RE = re.compile(r'href="#(src-[0-9]+)"', re.I)
TITLE_RE = re.compile(r'\btitle="[^"]+"', re.I)
ENTRY_RE = re.compile(r'<li\b[^>]*\bid="(src-[0-9]+)"', re.I)
SOURCES_RE = re.compile(r'class="article-sources"', re.I)


def html_files():
    for base, dirs, names in os.walk(ROOT):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in sorted(names):
            if name.endswith(".html"):
                yield os.path.join(base, name)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def enclosing_blocks(text):
    """Byte ranges a marker must not appear inside, with a label for each."""
    spans = []
    for m in re.finditer(r'<(h[1-6])\b[^>]*>.*?</\1>', text, re.I | re.S):
        spans.append((m.start(), m.end(), "a heading"))
    for cls, label in (("key-facts", "the .key-facts short answer"),
                       ("faq-item", "a .faq-item")):
        # Non-nesting blocks in this template, so a lazy match to the next
        # closing div of the same depth is good enough and cheap.
        for m in re.finditer(r'<(?:aside|div)\b[^>]*class="[^"]*\b%s\b[^"]*".*?</(?:aside|div)>'
                             % cls, text, re.I | re.S):
            spans.append((m.start(), m.end(), label))
    return spans


def check(path, text, fail):
    rel = os.path.relpath(path, ROOT)
    if os.path.basename(path) in EXEMPT:
        return

    markers = []           # (line, id, has_title, position)
    for m in MARKER_RE.finditer(text):
        tag = m.group(0)
        href = HREF_RE.search(tag)
        line = line_of(text, m.start())
        if not href:
            fail(rel, line, 'citation marker has no href="#src-N"')
            continue
        markers.append((line, href.group(1), bool(TITLE_RE.search(tag)), m.start()))
        if not TITLE_RE.search(tag):
            fail(rel, line, 'citation marker %s has no title="" — a hover '
                            'should answer "says who?" without a page jump'
                            % href.group(1))

    entries = [(line_of(text, m.start()), m.group(1), m.start())
               for m in ENTRY_RE.finditer(text)]
    has_block = bool(SOURCES_RE.search(text))

    if not markers and not entries and not has_block:
        return

    if markers and not has_block:
        fail(rel, markers[0][0], "article has citation markers but no "
                                 ".article-sources block")
    if has_block and not markers:
        line = line_of(text, SOURCES_RE.search(text).start())
        fail(rel, line, "article has a .article-sources block but no citation "
                        "markers pointing into it")

    entry_ids = [e[1] for e in entries]
    seen = set()
    for line, sid, _ in entries:
        if sid in seen:
            fail(rel, line, "duplicate source id %s" % sid)
        seen.add(sid)

    expected = ["src-%d" % (i + 1) for i in range(len(entries))]
    if entry_ids != expected:
        line = entries[0][0] if entries else 1
        fail(rel, line, "source ids must run %s in document order, found %s"
             % (" ".join(expected) or "(none)", " ".join(entry_ids) or "(none)"))

    for line, sid, start in entries:
        end = text.find("</li>", start)
        body = text[start:end if end != -1 else start + 400]
        if "<a " not in body.lower():
            fail(rel, line, "source entry %s has no link — a citation the "
                            "reader cannot follow is not a citation" % sid)

    # 1 and 2: markers and entries must agree.
    used = set()
    for line, sid, _, _ in markers:
        if sid not in seen:
            fail(rel, line, "citation marker points at %s, which is not in the "
                            "Sources block" % sid)
        used.add(sid)
    for line, sid, _ in entries:
        if sid not in used:
            fail(rel, line, "source %s is never cited — either a claim was cut "
                            "and left its source behind, or a marker is missing"
                 % sid)

    # 4: first use of each source runs down the page in order.
    first_use = []
    for line, sid, _, _ in markers:
        if sid not in [s for s, _ in first_use]:
            first_use.append((sid, line))
    order = [int(s.split("-")[1]) for s, _ in first_use]
    if order != sorted(order):
        bad = next(line for (sid, line), n, prev
                   in zip(first_use, order, [0] + order) if n < prev)
        fail(rel, bad, "sources are numbered in order of first appearance; "
                       "first uses run %s" % " ".join(str(n) for n in order))

    # 6: markers stay out of headings, the short answer, and the FAQ.
    for lo, hi, label in enclosing_blocks(text):
        for line, sid, _, pos in markers:
            if lo <= pos < hi:
                fail(rel, line, "citation marker %s is inside %s — markers "
                                "belong in the body prose only" % (sid, label))


def main():
    failures = []

    def fail(rel, line, msg):
        failures.append("%s:%s: %s" % (rel, line, msg))

    pages = 0
    markers = 0
    for path in html_files():
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        n = len(MARKER_RE.findall(text))
        if n or SOURCES_RE.search(text):
            pages += 1
            markers += n
        check(path, text, fail)

    if failures:
        for line in failures:
            print("FAIL: %s" % line)
        print("\n%d citation problem(s)." % len(failures))
        return 1

    print("OK: %d citation marker(s) across %d page(s); every marker resolves, "
          "every source is cited." % (markers, pages))
    return 0


if __name__ == "__main__":
    sys.exit(main())
