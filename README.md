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
scripts/apply_affiliate_links.py   One-command script to stamp your real Amazon tag site-wide
scripts/check_affiliate_links.py   Guard: fails if a placeholder or dead affiliate link is live
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
