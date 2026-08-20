# Growing MJ

A static, dependency-free site about indoor gardening, hydroponics, and
grow-tent equipment — hosted for free on GitHub Pages at
[growingmj.com](https://growingmj.com).

## What this is

Plain HTML/CSS, no build step, no framework, no JavaScript required. Every
page is a self-contained `.html` file that links to `/css/style.css`.
That's it — clone it, open `index.html` in a browser, or push to `main`
and GitHub Pages serves it as-is.

## Structure

```
index.html                     Homepage
about.html
privacy-policy.html
affiliate-disclosure.html
articles/
  choosing-a-grow-tent-for-beginners.html
  led-vs-hps-grow-lights.html
  setting-up-a-basic-hydroponic-system.html
  starting-an-indoor-herb-garden.html
  common-indoor-gardening-mistakes.html
  houseplant-care-fundamentals.html
  dealing-with-indoor-plant-pests-naturally.html
  nutrient-deficiency-identification-chart.html
  grow-tent-odor-control-and-ventilation.html
  best-vegetables-to-grow-indoors-year-round.html
  seed-starting-guide-for-beginners.html
  choosing-a-grow-medium-soil-vs-coco-vs-rockwool.html
  propagating-plants-from-cuttings.html
  pruning-and-training-indoor-plants.html
  harvesting-and-drying-herbs.html
  automating-your-indoor-garden-watering.html
  growing-microgreens-indoors.html
  understanding-grow-light-schedules.html
guides/
  index.html                   Guide hubs: the four control loops, plus the plant
  light/index.html             Light in (DLI)      — pairs with /tools/dli-calculator/
  water/index.html             Water through (VPD) — pairs with /tools/vpd-calculator/
  air/index.html               Air through (CFM)   — pairs with /tools/grow-tent-fan-calculator/
  feeding/index.html           Salt in solution (EC) — pairs with /tools/ppm-ec-converter/
  plants/index.html            The plant itself    — pairs with /tools/deficiency-diagnosis/
css/style.css                  All site styling
data/affiliate-links.json      Central affiliate link registry (see below)
data/electricity-rate.json     Canonical $/kWh for every running-cost figure — never inline a rate
docs/references/source-map.md  Claim-by-claim sourcing map for all 18 articles, fetchability tested
docs/references/*.md           Digests of sources that cannot be fetched by an agent
scripts/apply_affiliate_links.py   One-command script to stamp your real Amazon tag site-wide
scripts/check_affiliate_links.py   Guard: fails if a placeholder or dead affiliate link is live
scripts/check_electricity_rate.py  Guard: fails if any article carries a stale electricity rate
scripts/check_citations.py         Guard: fails if a citation marker does not resolve to a source
robots.txt
sitemap.xml
CNAME                           Custom domain for GitHub Pages (growingmj.com)
DEPLOY.md                       DNS + Amazon Associates setup instructions
```

## Content policy (important, read before adding new pages)

The domain name suggests cannabis, but this site is intentionally about
**general indoor/home gardening**: grow tents, LED grow lights, hydroponic
systems, indoor herb gardens, houseplants, and seed starting. This is a
deliberate choice — Amazon Associates and most mainstream ad networks
restrict or ban cannabis content, and legality varies by jurisdiction. Do
not add cannabis-specific content, strain reviews, or grow guides framed
around marijuana. The brand name "Growing MJ" stays as-is; the site simply
never explains what "MJ" stands for.

## Citation standard (read before writing or editing any article)

This site has already shipped fabricated numbers and corrected them
publicly. Every figure here is treated as unverified until a source is
found for it, and **sourcing gates the writing rather than trailing it** —
you find the source first and write from what it says, not the reverse.

Two goals pull against each other and this section is where that gets
resolved. The site has to be verifiable, and it has to read like a person
wrote it. Citation-stuffing is itself a machine-writing tell: a paragraph
broken by six parentheticals reads *more* generated, not less. So the
mechanism below is built to put the proof somewhere the eye does not have
to travel through.

Reference implementation, in this order of usefulness:
`articles/nutrient-deficiency-identification-chart.html` (a table-heavy
page), `articles/growing-microgreens-indoors.html` (dense procedural
numbers from one source), `articles/led-vs-hps-grow-lights.html` (mixed
equipment specs and derived arithmetic). Copy the shapes from those.

### The source hierarchy

Strict order. A lower tier is used only where no higher tier covers the
claim, and the tier is a ceiling on what the source may be cited *for*.

| Tier | Class | Notes |
|---|---|---|
| 1 | University cooperative extension | The workhorse. Written for exactly this audience, land-grant, reviewed, free. |
| 2 | USDA / federal agency (EIA, EPA, FDA, USDA-ARS) | Economic and regulatory facts extension does not carry. |
| 3 | Peer-reviewed horticulture and controlled-environment agriculture | Mechanism, and anything extension states without a number. |
| 4 | EPA-registered pesticide labels | The **only** legitimate authority for a dose, rate or interval on a named product. |
| 5 | Manufacturer technical documentation | Equipment specifications only — CFM, µmol/J, wattage, lamp life. **Never** for a claim about plants. |
| — | Commercial grow blogs | **Not sources.** This is where the site's existing errors came from. |

A manufacturer may be cited for what its own product does, attributed in
the text ("Grodan says…"). Where a vendor's horticultural claim conflicts
with extension, extension wins.

Two source documents live in the repo and should be read before starting
any article:

- `docs/references/source-map.md` — claim-by-claim mapping for all 18
  articles, with every source's fetchability already tested. Most of the
  sourcing work is already done there.
- `docs/references/cockson-2019-cannabis-nutrient-disorders.md` — a
  hand-pulled digest of the one study that induces and photographs each
  nutrient disorder in this crop rather than extrapolating from another.
  Where it disagrees with a general-crop extension source on a symptom
  description, it wins.

### The mechanism

**Prose stays clean. The marker is one character. The links live at the
foot of the article.**

1. **Inline marker.** A superscript numeral linking to the numbered entry
   in the article's `Sources` block:

   ```html
   Presoak peas for 6 hours and sunflower for 12.<a class="cite" href="#src-3" title="Utah State University Extension">3</a>
   ```

   One element, one class, styled as superscript by `.cite` in
   `css/style.css`. It is deliberately cheap to type and easy to grep —
   `grep -c 'class="cite"' articles/*.html` counts the citations on every
   page. The `title` carries the publisher so a hover answers "says who?"
   without a page jump.

   Two sources on one claim are two adjacent markers; CSS puts the comma
   in, so they render `2,5` rather than colliding into `25`.

2. **Sources block.** The `.article-sources` section already in the
   template, numbered in **order of first appearance in the article**:

   ```html
   <section class="article-sources" aria-labelledby="sources">
     <h2 id="sources">Sources</h2>
     <ol>
       <li id="src-3">Utah State University Extension, <a href="https://extension.usu.edu/yardandgarden/research/grow-your-own-microgreens">&ldquo;Grow Your Own Microgreens&rdquo;</a>, Table 1 (updated January 2026).</li>
     </ol>
     <p class="sources-note">Every source above was fetched and read on 20 August 2026&hellip;</p>
   </section>
   ```

   Entry format: **publisher, linked title, then the specific table,
   section or figure the number came from.** "NC State Extension" is not a
   citation; "NC State Extension, *Extension Gardener Handbook* ch. 16" is.
   The block sits after the body and before the FAQ.

3. **Numbers in a table cite in the table, not in the body.** Put a
   `<p class="table-source">` line directly under the `.table-scroll`
   wrapper — a sibling, not a `<caption>`, because a caption inherits the
   table's `min-width` and would sit inside the horizontal scroller.
   If the columns come from different sources, the marker can go in the
   column header instead. **Never in a data cell** — a marker in every cell
   is the citation-stuffing failure in its purest form.

   A **summary table** that only restates figures marked in the body below
   it carries no markers at all, on the same principle as the FAQ. The
   comparison table at the top of `led-vs-hps-grow-lights.html` is one;
   the variety table in `growing-microgreens-indoors.html` is not, because
   that table *is* where those numbers live.

### Where markers go, and where they do not

The placement rules are the half that keeps the prose readable. They are
not stylistic preferences; ignoring them is how the page turns into a
literature review.

- **At the end of the sentence, after the punctuation.** Never mid-sentence.
- **One marker per claim cluster, not per number.** Three figures from one
  source in one sentence get one marker at the end of it.
- **Consecutive sentences from the same source get one marker**, on the
  last of them.
- **Never more than two markers in one place**, and only ever two when the
  two sources back genuinely different halves of the claim.
- **A source named in the prose still gets a marker.** "Utah State
  Extension gives 6 hours for peas" is voice; the marker is the link. They
  are not duplicates and one does not excuse the other.
- **No markers in the FAQ, in the `.key-facts` short answer, or in a
  heading.** Those restate claims already marked in the body, and the FAQ
  is mirrored into `FAQPage` JSON-LD where markup cannot follow.

**What deliberately carries no marker — and this is the honest half:**

- **Arithmetic worked on the page** from a figure that *is* marked. 216
  kWh at the marked rate is $38.49; show the working, mark the rate, leave
  the result bare.
- **Observations and anecdotes told in the first person.** These are
  labelled by their voice. They are never presented as measurements.
- **Non-actionable numbers** — dates, the dimensions of a standard tray,
  how many items are in a list.

State that contract to the reader in the `.sources-note` line, because it
is what makes the marker mean something: **a number without a marker is
not a sourced claim.** That removes the incentive to sprinkle markers for
credibility — every one of them is a promise that someone checked.

### Rules about the numbers themselves

- **A number travels with its premise.** The site's characteristic failure
  is not invention, it is a real figure with its condition deleted — a
  fixture class, a crop, a temperature, a substrate. 1.7 µmol/J is true of
  a 1000 W *double-ended* HPS and false of the single-ended fixture most
  people own. 14 days of fridge life is true of *mustard* microgreens at
  5 °C. Carry the condition or drop the number.
- **A claim that cannot be sourced becomes an honest range, a trigger, or
  nothing.** "Check the medium" beats "water every 3-7 days". What it
  never becomes is a confident new number: substituting a fresh figure for
  an unsourced one is the exact failure this standard exists to stop.
- **Retail prices have no authority behind them.** Either cite a source
  that publishes a dated price and print that date, or drop the figure and
  give the ratio or the shopping instruction instead.
- **Where a number was cut or corrected and the wrong one is still
  circulating, say so in one sentence.** Telling the reader we looked for
  the "12-18 month HPS bulb" interval and could not source it is worth
  more than silently omitting it, and it is the single most human thing on
  a page full of figures.

### Verifying a source before you cite it

**A 200 is not a fetch.** `canr.msu.edu` returns 200 with a 948-byte
Incapsula challenge; `journals.ashs.org` returns 200 with a 1,444-byte
JavaScript shell. Check the body length and the body content, always:

```bash
curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)" \
     --max-time 40 -o /tmp/src.html -w '%{http_code}\n' "<url>"
wc -c /tmp/src.html && grep -i "<the claim>" /tmp/src.html
```

Never cite a URL you have not just loaded. `source-map.md` §3 lists the
hosts that are open, the ones that lie about it, and the ones that are
simply dead — read it before hunting.

If a source is authoritative but bot-blocked (MDPI 403s every automated
route, including the DOI resolver), **add a digest to `docs/references/`
and cite the paper normally with its DOI.** A reader with a browser can
reach what an agent cannot, so the reader still gets a working link.

### When a number changes, change all of its copies

Numbers on this site are duplicated by design and have contradicted
themselves in production more than once. Every changed figure has to be
chased through all of:

1. the body prose,
2. any table on the page,
3. the `.key-facts` "short answer" block at the top — **which is a verbatim
   copy of the first FAQ answer**, and carries an HTML comment saying so,
4. the matching `.faq-item`,
5. the `FAQPage` JSON-LD in `<head>`.

Then bump `Last updated` in the byline **and** `dateModified` in the
`Article` JSON-LD.

**Greps on this repo need to account for HTML entities.** The markup uses
`&deg;`, `&thinsp;`, `&nbsp;` and `&cent;`, so searching for `75°F` or
`0.59 kPa` finds nothing while the text is right there on the page. A
previous pass concluded an entire paragraph did not exist on that basis.
Search for the bare number.

Three guards exist and should be run before pushing:

```bash
python3 scripts/check_citations.py
python3 scripts/check_affiliate_links.py
python3 scripts/check_electricity_rate.py
```

`check_citations.py` covers the mechanical half of the standard only — that
every marker resolves to a source entry, that every entry is cited by at
least one marker, that the numbering runs in order of first appearance, and
that no marker has crept into a heading or the FAQ. It cannot tell you
whether a number is right or whether the source says what the article
claims. It carries a short exemption list of pages that predate the
standard; that list should shrink to nothing as the batch rewrites land.

The electricity rate lives in `data/electricity-rate.json` and is never
inlined in an article — it used to be hardcoded in three places and was
19% low in all of them.

## Affiliate links: how the placeholder system works

Every product mention in an article uses a placeholder link instead of a
real, tagged affiliate URL:

```html
<a href="[[AFFILIATE:grow-tent-4x4]]" class="affiliate-link">4x4 ft grow tent kit</a>
```

The `grow-tent-4x4` id maps to an entry in `data/affiliate-links.json`,
which is the single source of truth for every product link on the site:

```json
"grow-tent-4x4": {
  "label": "4x4 ft grow tent",
  "url": "https://www.amazon.com/s?k=4x4+grow+tent",
  "criteria": "Alloy steel poles and thick canvas rated to carry a light and a fan without sagging; check the port diameter against your fan's duct size."
}
```

### What the links point at, and what the copy may therefore say

Every `url` in the registry is an Amazon **category search**, not a product
page. That is a deliberate choice: search URLs survive a listing going out
of stock, where a hardcoded ASIN goes dead.

It has one consequence the copy has to respect. A search result set has no
fixed contents, so an article can never assert a fact about "the product"
behind one of these links — its composition, its specs, its price, its
brand history. All of those describe whatever the query returns today.

So the copy names no products. It gives shopping criteria instead: what to
look for, what a tool measures, what it cannot measure. That is what the
`criteria` field on each entry is for — it is the claim the article is
allowed to make.

If a specific ASIN is ever sourced for an entry, this is reversible: put
the product URL in `url`, add an `asin` field, and the product-specific
claims can come back — attached to a real product and verified against
that listing.

### Once you're approved for Amazon Associates

1. Get your Associates tracking ID (looks like `yourtag-20`).
2. Open `data/affiliate-links.json` and either:
   - set `"amazon_tag": "yourtag-20"` at the top of the file, **or**
   - pass it directly to the script (see below) without editing the file.
3. From the repo root, run:
   ```bash
   python3 scripts/apply_affiliate_links.py yourtag-20
   ```
   This walks every `.html` file in the site, finds every
   `href="[[AFFILIATE:id]]"` placeholder, looks up the matching entry in
   `data/affiliate-links.json`, and rewrites it to the real product URL
   with `?tag=yourtag-20` (or `&tag=yourtag-20` if the URL already has a
   query string) appended.
4. Review the diff (`git diff`), commit, and push. Every affiliate link
   across every article is now tagged in one pass — no manual find/replace
   through six articles.
5. To add a new product later, just add a new entry to
   `data/affiliate-links.json` and reference it in your article as
   `href="[[AFFILIATE:your-new-id]]"`, then re-run the script.

### Always run the check before publishing

Stamping is a manual step, so it is possible to write an article and
publish it with the raw `[[AFFILIATE:id]]` placeholder still in the page.
That has already happened once — 22 placeholders across 8 articles went
live as literal text where a product link should have been. Run this
before every push:

```bash
python3 scripts/check_affiliate_links.py
```

It exits non-zero and names the file and line if any page still contains a
`[[...]]` placeholder, if any `affiliate-link` anchor has no `href` (a link
that looks clickable and isn't), or if any affiliate URL is missing the
Associates tag. A clean run prints how many links it checked.

### Adding other affiliate programs later

If you join a non-Amazon affiliate program, add its links the same way:
create new entries in `data/affiliate-links.json` with that program's
plain URL, reference them with the same `[[AFFILIATE:id]]` pattern in
articles, and extend `scripts/apply_affiliate_links.py` if that program
needs a different tagging scheme than a simple `?tag=` query parameter.

## Legal/compliance pages

- `affiliate-disclosure.html` — required FTC-style disclosure, also linked
  from a banner at the top of every article that contains affiliate links.
- `privacy-policy.html` — covers GitHub Pages hosting, lack of first-party
  tracking, and how affiliate links/cookies work on the retailer's side.

Keep both of these current if you add new tracking, analytics, or
affiliate programs.

## Local preview

No build step needed — just open any `.html` file directly in a browser,
or run a tiny local server from the repo root if you want relative paths
to behave exactly like production:

```bash
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deployment

See [DEPLOY.md](./DEPLOY.md) for DNS setup and how to apply for Amazon
Associates once the site is live.
