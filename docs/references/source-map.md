# Source map — claim-by-claim

Produced before the rewrite so that sourcing gates the writing rather than trailing it. This repo has already shipped and publicly corrected several fabricated numbers (PR #11, PR #22), every one of them written first and checked afterwards.

## Corrections from the citation reference implementation (issue #17)

Six findings from actually loading the sources this document recommends. **Read these before using §5 or §6**, because three of them would have shipped a bad citation.

1. **The Thiram 24(c) label in §5.7 must not be cited.** It carries the prohibition sentence, but its header reads "FOR DISTRIBUTION AND USE ONLY WITHIN THE STATE OF OREGON", "THIS LABEL IS VALID UNTIL DECEMBER 31, 2021", "For Treatment of Cereal Grain Seeds… FOR EXPORT ONLY", and "Seed treated under SLN No. OR-160012 may not be planted in the U.S." Expired, single-state, cereal grains, export only. Use instead: **USDA AMS, "Labeling Requirements for Chemically Treated Seed"** (`ams.usda.gov/sites/default/files/media/LabelingRequirementsforChemicallyTreatedSeed.pdf`, 200/55 KB) for the label wording and the thiram/captan names, and **LSU AgCenter, "Seed Treatments for Vegetables"** (`lsuagcenter.com/NR/rdonlyres/26772246-4C4A-4028-992D-95BF6DD51C6D/96988/43SeedTreatmentsVegetables2014FINAL.pdf`, 200/627 KB) for "Most commercially available vegetable seeds come treated with at least one fungicide and/or insecticide." Illinois RPD 915 is dated March 1992 and supports the fungicide list but *not* the "routinely sold treated" half.

2. **The Handreck 1993 coir CEC figures are unverifiable and have been cut from the site.** The reference is real (Comm. Soil Sci. Plant Anal. 24(3-4):349-363, doi 10.1080/00103629309368804) but paywalled behind a Cloudflare 403, and no reachable source reproduces "21-30 vs 78 mmol(+)/L". Two accessible sources give the *direction* only: Carlile et al. 2015 (`woodsubstrates.cals.ncsu.edu/.../constituents-and-properties.pdf`, 200/2.1 MB) — "Coir has a lower CEC than peat, with values ranging from 35 to 95 cmolc kg−1" — and Native Plants Journal 1(2). Note that **Purdue HO-255-W puts coir in its *high*-CEC list**, so the site should not build any argument on coir's exchange capacity at all. The compositional argument is the one that survives: HO-255-W, "coir-based substrates require more Ca, sulfur (S), Cu, and Fe; they also require less K."

3. **"Lower leaf interveinal chlorosis is the most commonly observed initial magnesium deficiency symptom" is not an NC State Extension sentence.** It is a *figure caption* in e-GRO Alerts 14(20) (April 2025) and 13(12) (March 2024), by Veazie & Whipker. It appears on none of the 3,067 pages in `content.ces.ncsu.edu/sitemap.xml`. Attribute it to the alert, and cite it as a caption.

4. **e-GRO PDFs need `pdftotext -raw`, not `-layout`.** Figure captions are line-broken in the text layer, so `-layout` and plain grep both return confident false negatives on strings that are genuinely present. This is the same class of failure as the HTML-entity trap in §9.1.

5. **"Purple stems means phosphorus" is much weaker than §6 assumed, and now has a source.** e-GRO Alert 13(2), "Phosphorus Has 2 Ps" (`e-gro.org/pdf/2024-13-02.pdf`, 200/981 KB): "in most cases with our warmer growing temperatures, we failed to induce lower leaf purpling… Instead, lower leaves developed an overall pale yellow coloration and an olive-green spotting pattern… We have observed this on over 40 species," and a caption reading "Lower leaf purpling in pentas caused by a low substrate pH (<5.0) and not a phosphorus deficiency." **This independently matches Cockson's olive-green spotting description for this crop**, which is the strongest convergence between the two source families anywhere in this document. The deficiency chart has been rebuilt on it; `/tools/deficiency-diagnosis/` still leads on purpling and needs the same fix.

6. **HPS lamp life has no single number, and the extension figures omit the fixture class.** Cornell's course page (25,000 h) and the University of Arkansas (24,000 h) both state a bare figure. Manufacturer data, which is the correct tier for an equipment spec, splits it: Ushio's catalogue rates single-ended lamps 19,000-24,000 h — on pages it marks "Discontinued — For Reference Only" — and **double-ended lamps at 10,000 h**; Osram recommends replacement "after 10 000 hours… in order to ensure optimal and continuous growth", footnoted as a 95% survival rate; Philips publishes 10,000-12,000 h service lifetimes at stated maintenance levels. Converted at a 16 h photoperiod, 10,000 h is about 21 months, which **partially rehabilitates the "12-18 months" folklore §4.4 dismisses** — it is a photoperiod, not a bulb property. §4.4's other half stands: carbon filter life is a separate claim and 6-12 months is still the sourced figure.

Two smaller notes. Virginia Tech SPES-817NP says CO2 in enclosed facilities has "been reported to be as low as 200 ppm" and gives no citation for it — write "reported", not "measured". And the storage-life source §5.7 lists as "Kou et al." is actually **Dayarathna et al. (2023), *Life* 13(2):393**, and it studied *mustard* microgreens specifically: 14 days at 5 °C, 4 days at 10 °C, 2 days at 15 °C, under a day at 20-25 °C.

## Two corrections to this document's own research

Both were caught by re-checking the collated findings against the repo and the live web. Read the rest of this file knowing that agent-reported access results and agent-reported absences are both fallible.

1. **The VPD paragraph DOES exist.** The collation claimed "75°F at 80% humidity is a sluggish 0.59 kPa" appears nowhere in the repo and was residue from an old retraction. It is live, in `articles/common-indoor-gardening-mistakes.html` around line 184. The grep missed it because the markup uses HTML entities — `75&deg;F` and `0.59&thinsp;kPa` — so a plain-text search for the rendered string finds nothing. **Any absence check on this repo must account for entities**, or it will keep producing confident false negatives.

2. **Missouri Extension direct PDF paths still work.** The collation reported `extension.missouri.edu` 403ing on all routes including direct `.pdf`. Re-tested afterwards: `.../agguides/hort/g06984.pdf` returns 200 with correct content. The 403s were most likely rate limiting during a burst of automated requests, not a permanent block. Re-test before treating any host as blocked, and space out requests.

## Access reality

Status codes alone are not a fetchability test. Three traps observed:

- `canr.msu.edu` returns **200 with a 948-byte Incapsula challenge body**. A status check passes; there is no article behind it.
- `journals.ashs.org` returns **200 with a 1,444-byte JavaScript shell**. Same failure shape.
- `extension.psu.edu` returns a straight 403 to every path tested.

So: check the body length and content, not just the code.

Known good, verified: NC State Extension Gardener Handbook, Purdue HO-255-W, UF/IFAS EDIS, ASPCA toxic plant database, OkState `pods.okstate.edu` fact sheets, Denver Cannabis Environmental BMP Guide, CSU GardenNotes, USU Extension, EIA data files, Missouri direct `.pdf` paths.

Known blocked: MDPI (all routes including DOI resolver — Cockson 2019 was hand-pulled, see the sibling digest), `pubs.acs.org`, `extension.psu.edu`, plus the two 200-but-empty hosts above.

## Nothing is gated on a manual download

The two sources previously called the highest-value hand-pulls both turned out to be fetchable: OkState HLA-6722 carries the per-crop EC/pH table in full, and the Hydrofarm heat-mat spec serves verbatim. The manual-pull batch is **0 essential, 4 useful, 6 optional** — the rewrite can proceed without any of them.

# Source Map — growingmj.com

**Status:** collated from seven subject-area source maps, with conflicts between them independently re-tested.
**Purpose:** this file gates the rewrite. Writing is sourced first, then written — not sourced afterward.
**Last verified:** 2026-08-19. All HTTP statuses below were observed with
`curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)" -o /dev/null -w '%{http_code}' --max-time 25 "<url>"`
plus, where noted, a body-content check.

---

## 0. How to use this document

1. **Never cite a source that is not listed here as fetchable**, or that is not in `docs/references/` as a hand-pulled digest.
2. **A 200 is not proof of content.** Four hosts in this subject area return 200 and serve nothing usable (§3.2). Always check the body, not the status code.
3. **Every number needs its condition attached.** The site's characteristic failure mode is not invention — it is a real number with its premise deleted (a fixture class, a temperature, a season, a crop). See §4.
4. **If a claim is in §7, do not source it. Cut it or convert it to a range.** "No source found" is a finished answer, not an unfinished one.
5. **Where §8 says the literature disagrees, present the disagreement.** Do not pick a winner and state it flatly.
6. **The audit that produced this work is partly stale and partly wrong.** Read §9 before budgeting against its counts.

---

## 1. Source hierarchy

In strict order. A lower tier is used only when no higher tier covers the claim.

| Tier | Class | Notes |
|---|---|---|
| 1 | **University cooperative extension** | The workhorse. Written for exactly this audience. Land-grant, reviewed, and free. |
| 2 | **USDA / federal agency** (EIA, EPA, FDA, USPTO, USDA-ARS/AMS) | For economic and regulatory facts extension does not carry. |
| 3 | **Peer-reviewed horticulture and controlled-environment agriculture** | For mechanism and for anything extension states without a number. |
| 4 | **EPA-registered pesticide labels** | The **only** legitimate authority for a dose, rate or interval on a named product. |
| 5 | **Manufacturer technical documentation** | Equipment specifications **only** — CFM, µmol/J, wattage, flow rate, handling procedure. Never for a horticultural claim. |
| — | **Commercial grow blogs** | **Not sources.** This is where the site's existing errors came from. |

**Two standing rules.**
- A manufacturer may be cited for what its own product does, attributed in the text ("Grodan says…"), never for a claim about plants. Where a vendor's horticultural claim conflicts with extension, extension wins — Grodan calls stone wool "pH-neutral" while the trade calls it high-pH, which is precisely why that number needs a real source or none.
- **Manufacturer datasheets rot.** The Gavita Pro 600e SE spec sheet now 301s to a homepage; the whole `ctahr.hawaii.edu/oc/freepubs/` tree is 404. Prefer measured peer-reviewed values over a spec-sheet URL, and never build an argument on a link you have not just loaded.

---

## 2. Global constants — set once, reference everywhere

### 2.1 Electricity rate — **17.8 ¢/kWh**

Live in **exactly three articles** (verified by grep): `led-vs-hps-grow-lights`, `understanding-grow-light-schedules`, `choosing-a-grow-tent-for-beginners`. All three say `$0.15/kWh`, which was last roughly accurate in 2022. Every dollar figure derived from it is **~19% low**.

Source: **U.S. EIA, Electric Power Monthly, Table 5.3.** Machine-readable: `https://www.eia.gov/electricity/monthly/xls/table_5_03.xlsx` (200). The HTML table page renders via JS and gives curl only boilerplate — **cite the HTML page, parse the xlsx.**

Values parsed directly from the xlsx (US residential, ¢/kWh):

| Series | Value |
|---|---|
| Annual 2024 (final) | 16.48 |
| Annual 2025 (preliminary) | 17.30 |
| **Rolling 12 months ending May 2026** | **17.82** |
| Year-to-date 2026 (Jan–May) | 18.11 |
| May 2026 alone | 18.44 |

**Use 17.82 ¢ (round to ~18 ¢).** The seven maps each grabbed a different row and three of them recommended the single-month 18.44, which is seasonally peaked and will read as wrong for most of the year. The rolling 12-month average is the correct statistic for evergreen copy. Note the rate has risen every year since 2020 (13.66 in 2021), so it will be stale again by next summer.

**Implementation:** put it in `data/` with the retrieval date and reference it, rather than hardcoding it in three files. The next correction should be a one-file edit. Show the as-of date in visible copy so staleness is self-evident.

Recomputed figures for the live articles: 72 kWh/mo → **$12.83** (page says ~$11); 216 kWh/mo → **$38.49** (says ~$32); 288 kWh/mo → **$51.32** (says ~$43); 144 kWh/mo → **$25.66** (says ~$22).

### 2.2 Isopropyl alcohol — **70%**

Two independent extension sources agree, and it now appears in two articles (mealybug dabbing, blade sanitation). Consolidate into one shared block: UC IPM gives 70%-or-less dabbed with a swab for houseplant mealybugs (10–25% in a spray bottle for extensive infestations, repeated weekly); Iowa State gives 70% isopropyl wiped or dipped, no soak needed, for pruning blades.

### 2.3 Insecticidal soap and horticultural oil — **1–2% (2½–5 tbsp/gal)**

One Clemson page covers both, plus the shared safety limit: do not apply above 90°F or in full sun; injury symptoms can take 48 hours to appear, so a leaf test needs a 48-hour wait. Both are usable on vegetables up to harvest. Consolidating this into one linked block removes the largest single category of unsourced numbers on the site.

### 2.4 DLI conversion — `PPFD × hours × 0.0036 = DLI`

Publish DLI targets, not bare PPFD. The literature speaks in DLI because photoperiod is a free variable, and publishing DLI plus the conversion makes the "dim and long vs bright and short" argument fall out for free. Canonical crop table in §5.1.

---

## 3. Access rules

### 3.1 Confirmed open — fetch freely

`e-gro.org` (PDFs, no gate at all — **the single best-value host in this subject area**; its alerts are co-published by NC State, Cornell, Iowa State, Arkansas, OSU and MSU, which lets you route *around* the MSU block) · `content.ces.ncsu.edu` · `extension.purdue.edu/extmedia` + `purdue.edu/hla` · `hgic.clemson.edu` · `ipm.ucanr.edu` · `pubs.ext.vt.edu` · `extension.usu.edu` · `yardandgarden.extension.iastate.edu` + `hortnews.extension.iastate.edu` · `extension.illinois.edu` + `ipm.illinois.edu` · `extension.unh.edu` · `extension.umass.edu` / `ag.umass.edu` · `cmg.extension.colostate.edu` + `planttalk.colostate.edu` + `extension.colostate.edu/resource/*` · `edis.ifas.ufl.edu` / `ask.ifas.ufl.edu` · `fieldreport.caes.uga.edu` · `bookstore.ksre.ksu.edu` · `njaes.rutgers.edu` + `rucore.libraries.rutgers.edu` · `cfaes.osu.edu` · `blogs.cornell.edu` + `greenhouse.cornell.edu` · `wpcdn.web.wsu.edu` · `beaufort.ces.ncsu.edu` · `aces.edu` · `lsuagcenter.com` · `hort.extension.wisc.edu` + `pddc.wisc.edu` · `pnwhandbooks.org` · `eia.gov` · `ars.usda.gov` · `epa.gov` + `www3.epa.gov` · `fda.gov` · `uspto.gov` · `ams.usda.gov` · `aspca.org` · `pmc.ncbi.nlm.nih.gov` · `journals.plos.org` · `frontiersin.org` · `actahort.org` · `designlights.org` · `farm-energy.extension.org` · **`pods.okstate.edu`**

**Three host-specific notes that will save a cycle:**
- **`pods.okstate.edu` is the working mirror for Oklahoma State.** `extension.okstate.edu` 403s site-wide, but the same fact sheets serve at `pods.okstate.edu/fact-sheets/<ID>pod.pdf` (verified: HLA-6722 200/529KB, HLA-6708 200/1.4MB). One map recorded HLA-6722 as its highest-value manual pull; it is not blocked at all.
- **`farm-energy.extension.org` 403s to WebFetch but 200s to plain curl.** It is the most load-bearing single source in the ventilation subject area. Same fingerprinting behaviour on `pnwhandbooks.org`. **A 403 from a fetcher is worth one curl retry before declaring a source unreachable.**
- **`pubmed.ncbi.nlm.nih.gov` returns 203, not 200.** The page renders. Do not treat 203 as a failure.

### 3.2 The dangerous ones — **200 but no content**

These pass a status-code check and fail a content check. Any agent "verifying" by status code alone gets a false pass.

| Host | Behaviour | Route around it |
|---|---|---|
| `canr.msu.edu` (MSU Extension) | 200, **948-byte Incapsula challenge page** | Use e-GRO alerts (MSU co-publishes) or CSU GardenNotes |
| `journals.ashs.org` (HortScience/HortTechnology) | 200, **1,444-byte JS shell** | Indexed abstract, or PMC if mirrored |
| `extension.umd.edu` | 200, JS-gated, nav chrome only | Clemson / e-GRO. *UMD's blossom-end-rot page is fine at 200.* |
| `extension.colostate.edu/topic-areas/...` (7.221) | 200/152KB, table is client-rendered | Illinois PDF reproduces it with attribution |
| `ec.europa.eu` EU Pesticides Database | 200/146KB, JS application | Cut the claim (§7) |
| `eia.gov` HTML table grapher | 200, JS-rendered | **Use the `.xlsx` path** |
| `handbook.ashrae.org` | 200 — **prose IS served**; equations are images | Derive from Greenheck fan laws (open) |

### 3.3 Confirmed hard blocks (403)

`extension.psu.edu` (site-wide) · `extension.okstate.edu` (use `pods.` mirror) · **`extension.missouri.edu` (see below)** · `extension.oregonstate.edu/gardening/*` (but `/sites/extd8/files/documents/*.pdf` and `/catalog/pub/*` are **200**) · `extension.umn.edu/preserving-and-preparing/*` (**partial** — `/vegetables/` and `/planting-and-growing-guides/` are **200**) · `postharvest.ucdavis.edu` · `sciencedirect.com` · `pubs.acs.org` (every route incl. DOI resolver) · `mdpi.com` (every route incl. DOI resolver) · `pnas.org` (**use the PMC mirror**) · `oaktrust.library.tamu.edu` · `nature.com` (303s for WebFetch, 200s for curl — prefer PMC) · Oxford Academic · CSIRO Publishing · `omri.org/about` (but `/omri-lists` is 200)

> **⚠ Correction to the brief's known-good list.** The brief recorded "Missouri extension landing pages 403 but their direct `.pdf` paths 200." **That rule is stale.** I tested four paths — `publications/g6470`, and direct PDFs `g06470`, `g06515`, `g06970` under `/media/wysiwyg/Extensiondata/Pub/pdf/agguides/hort/` — and **all four returned 403**. Two of the seven sub-agents independently hit the same wall. Treat Missouri as fully blocked.

### 3.4 Dead, not blocked (404 — stop linking these)

The entire `ctahr.hawaii.edu/oc/freepubs/` tree, including **VC-1** (the Kratky non-circulating hydroponics publication) and SA-5. Cite Kratky to ISHS *Acta Horticulturae* instead — 648:83-89 (2004) and 843:65-72 (2009), `actahort.org` resolves 200 at abstract level — or to the Wayback capture (200). **Anything on this site still linking to `ctahr.hawaii.edu` is linking to a dead host.**

Also stale-URL traps, not blocks: `secure.caes.uga.edu/.../B%201318_6.PDF` returns 200 with a *pecan production bulletin*, not B1318 — use the `fieldreport.caes.uga.edu` HTML. Several `extension.umn.edu` crop paths 404 but have working equivalents at different paths.

### 3.5 Manual-pull batch

**Nothing here blocks the rewrite.** Every load-bearing claim on the site has an agent-fetchable source. Ranked honestly for one sitting:

| Source | Rank | Settles |
|---|---|---|
| MSU "Selecting which iron chelate to use" | useful | Per-chelate pH numbers; CSU GardenNotes #223 already carries the actionable rule |
| ACS *ES&T* cannabis facility air quality (+ VOC/RH adsorption) | useful | ~65% RH adsorption threshold; general site value. Denver BMP carries the load-bearing claims |
| Konduru/Evans/Stamps 1999, coir chemistry (HortScience) | useful | Honest mechanism for the coco cal-mag claim |
| Penn State microgreens guides | useful | Seed food-safety guidance; USU already supplies the full per-variety table |
| ScienceDirect basil-N / pepper topping | optional | **Recommended fix is to cut the mechanism, not source it** |
| CSU 7.221 seed storage | optional | Illinois PDF reproduces it with attribution |
| UMD nutrient deficiency | optional | One uncontroversial sentence |
| UMN preserving herbs | optional | NC State + OSU cover it |
| EU Pesticides DB / UK HSE azadirachtin | optional | **Recommend cutting the claim instead** |
| NFPA 70 NEC 210.20(A) verbatim | optional | UpCodes paraphrase is usable |

**Two items previously called "essential" are resolved, not pulled:** OkState HLA-6722 (fetchable at `pods.okstate.edu`, full Table 2 extracted below) and the Hydrofarm heat-mat spec (fetchable, verbatim). ASHRAE Ch.49 serves its prose; ASTM D1907's landing page carries no scope text and a $72 paywall — **do not buy it**, the fix is to stop claiming denier measures strength.

---

## 4. Cross-cutting corrections — fix as a class, in one pass

Fixing these article-by-article will produce inconsistent copy. Each is one pass across the whole site.

**4.1 Body / table / FAQPage triples that disagree.** Several articles state a number three times — in prose, in a table, and in FAQPage schema — with different values. Google can surface whichever it likes, so the schema copy is the highest-exposure text on the page. Known triples: leafy-green photoperiod (table 12-14 h vs FAQ 14-16 h); the 16→24 h energy increase (body 50%, FAQ 40% — **the body is right, 24/16 = 1.5, this is arithmetic, not sourcing**); carbon filter life (three places, all 12-18 months); passive-watering "impossible to overwater" (FAQ contradicts body two sections earlier); DWC "fewest moving parts". **Reconcile internal contradictions BEFORE sourcing.** A rewrite that sources one number and leaves its contradicting twin in the schema has fixed nothing.

**4.2 "LEDs run cool" — the single most repeated internet error in this subject, and it is doing real harm here.** Five articles use "clip fan" language and hold incompatible positions. The physics: fixtures of equal efficacy generate the same thermal energy per photon; LEDs merely dissipate more of it *away* from the plant plane, worth about **1.3 °C** of leaf temperature (Nelson & Bugbee 2015). Essentially all wall draw ends up as heat in a closed tent. Separately, **airflow is not air exchange** — sealed CEA spaces measure as low as **200 ppm CO2** against ~430 ambient (Virginia Tech SPES-817NP), and a clip fan addresses neither heat removal nor CO2 replenishment. An exhaust path sized to the space is required regardless of light type.

**4.3 Fixed intervals are the site's signature failure mode.** At least a dozen calendar numbers across the site have no source: water every 3-7 days, feed every 2-3 days, change the reservoir every 1-2 weeks, refill every 1-2 weeks, flush every few weeks, repot every 1-2 years, prune sessions a week apart, "recovery in a week or two". Every extension source on container watering says the same thing in different words: **check the medium, don't follow the calendar.** Fix as a class: replace each schedule with a trigger and a diagnostic.

**4.4 "12-18 months" is a default value, not a measurement.** It appears as *both* the HPS bulb life (`led-vs-hps`, 3 places) *and* the carbon filter life (`grow-tent-odor-control`, 3 places). Two unrelated components sharing an oddly specific interval is a fingerprint. Filter life is **6-12 months** (Denver BMP). Fix both.

**4.5 L70 is a decay endpoint, not a warranty of flat output.** "Tens of thousands of hours before any noticeable drop" inverts the rating. L70 = the hour at which output has *already* fallen to 70%; the published figure is usually L70-B50, the hour at which *half a sample* is expected to have reached that point. Output declines from hour one.

**4.6 The Miracle-Gro fungus-gnat mechanism is wrong and appears in three articles.** `houseplant-care-fundamentals`, `choosing-a-grow-medium`, and `starting-an-indoor-herb-garden` all claim a bark/compost-free mix is "less inviting to fungus gnats". Backwards: **peat-heavy, consistently moist mixes are the most attractive substrate to egg-laying females** (CSU). Gnats are a moisture problem, not an ingredient problem. (`common-indoor-gardening-mistakes` carries the same affiliate link for a different, acceptable reason — refreshing spent mix — and does not need this fix.)

**4.7 All 51 affiliate links are Amazon *search* URLs.** `grep -c 'amazon.com/s?k='` returns hits in 12 of 18 articles. A factual product claim cannot hang on a query whose referent changes daily — this affects "the seeds are heirloom and open-pollinated", the moisture-meter specs, and every price. **Not fixable by sourcing:** link specific ASINs and verify against them, or drop the claims.

**4.8 EC targets are stated ABOVE source-water EC in the primary literature.** Cornell is explicit; popular charts including this site's omit the qualifier entirely. A reader on well water at 0.6 mS/cm who mixes to a raw reading of 1.0 is feeding at 0.4. This qualifier is more actionable than the numbers themselves and is missing site-wide.

**4.9 Alkalinity is the missing concept under at least four claims** — the pH-check interval, "there's no buffer in hydro", the 0.5/day drift rule, and erratic tip burn. All four try to describe a phenomenon whose driver (source-water carbonate/bicarbonate) the site never names. Introducing alkalinity once fixes all four and lets the invented numbers go away.

---

## 5. Sources by subject area

### 5.1 Lighting

| Source | URL | Status | Carries |
|---|---|---|---|
| Nelson & Bugbee 2014, PLoS ONE 9(6):e99010 | `journals.plos.org/plosone/article?id=10.1371/journal.pone.0099010` (PMC: `pmc.ncbi.nlm.nih.gov/articles/PMC4048233/`) | 200 | Measured fixture efficacy + **input** power |
| Nelson & Bugbee 2015, PLoS ONE 10(10):e0138930 | `journals.plos.org/plosone/article?id=10.1371/journal.pone.0138930` | 200 | Leaf temperature under HPS vs LED; the 1.3 °C figure |
| Kusuma, Pattison & Bugbee 2020, *Hort. Research* 7:56 | `pmc.ncbi.nlm.nih.gov/articles/PMC7105460/` | 200 | LED efficacy ceilings; L70 = 50,000 h |
| DLC Horticultural Technical Requirements V4.0 | `designlights.org/our-work/horticultural-lighting/technical-requirements/hort-v4-0/` | 200 | 2.5 µmol/J QPL floor, eff. 18 Apr 2025 |
| DOE SSL "Lifetime and Reliability" | `betterbuildingssolutioncenter.energy.gov/sites/default/files/attachments/life-reliability_fact-sheet.pdf` | 200 | L70 / L70-B50 definitions |
| Virginia Coop. Ext. SPES-720NP (DLI intro guide) | `pubs.ext.vt.edu/SPES/spes-720/spes-720.html` | 200 | **Crop DLI table + conversion formula** |
| Purdue HO-238-B-W | `extension.purdue.edu/extmedia/ho/ho-238-b-w.pdf` | 200 | DLI chart, ~40 species; sensor placement |
| Purdue Veg Crops Hotline (transplant DLI) | `vegcropshotline.org/article/managing-daily-light-integral-to-improve-vegetable-transplant-quality/` | 200 | Transplant DLI 10-15 / 15-20 |
| UMN Extension, Lighting for indoor plants | `extension.umn.edu/planting-and-growing-guides/lighting-indoor-plants` | 200 | PPF bands (50-150 / 150-250 / 250-450); photoperiod by use |
| Cornell CEA Hydroponic Lettuce Handbook | `cpb-us-e1.wpmucdn.com/blogs.cornell.edu/dist/8/8824/files/2019/06/Cornell-CEA-Lettuce-Handbook-.pdf` | 200 | Full set-point table; 17 mol/m²/d; tipburn is an **airflow** ceiling |
| Jeong, Zhen, Zhang & Niu 2025, *Front. Plant Sci.* | `pmc.ncbi.nlm.nih.gov/articles/PMC11803448/` | 200 | Photoperiod/DLI trade in lettuce; 24 h highest yield |
| Marie et al. 2024, *Front. Plant Sci.* | `pmc.ncbi.nlm.nih.gov/articles/PMC11150841/` | 200 | Tomato photoperiodic injury >17 h; CAB-13 |
| e-GRO Veg Alert 2(1) (Mattson, bolting) | `e-gro.org/pdf/E201.pdf` | 200 | Spinach 13-14 h critical daylength; **temperature dominates** |
| Iowa State, supplemental light | `yardandgarden.extension.iastate.edu/how-to/how-determine-how-much-supplemental-light-provide-indoor-plants` | 200 | 14 h/day default; LED 18 in |
| Clemson, indoor light requirements | `hgic.clemson.edu/factsheet/indoor-plants-cleaning-fertilizing-containers-light-requirements/` | 200 | Foot-candle bands + window mapping |

**Canonical crop DLI table (VT SPES-720NP), mol·m⁻²·d⁻¹:** seedlings/cuttings 5-10 · microgreens 9-12 · parsley 10-15 · lettuce 12-17 · spinach 14-20 · cilantro 15-20 · basil 15-25 · impatiens 8-12 · begonia/geranium 12-19 · petunia 20-25 · tomato/cucumber/zucchini 20-30. VT also states: **do not use candela, lumen, foot-candles, lux, watts or joules** for plant light; phone apps are typically the most cost-effective PPFD meter.

**Measured efficacy, with fixture class attached (Nelson & Bugbee 2014).** Never quote µmol/J without the class.

| Fixture | Rated | **Measured input** | µmol/s | µmol/J |
|---|---|---|---|---|
| Gavita Pro 1000 **DE** | 1000 W | 1,033 W | 1,751 | **1.70** |
| ePapillon 1000 W DE | 1000 W | 1,041 W | 1,767 | 1.70 |
| Mogul-base **SE** HPS | 1000 W | 1,067 W | 1,090 | **1.02** |
| Mogul-base **SE** HPS | 400 W | 443 W | 416 | **0.94** |
| Cycloptics CMH 3100K | 315 W | 337 W | 491 | **1.46** |
| iGrow induction fluorescent | 400 W | 394 W | 374 | 0.95 |

### 5.2 Tent, ventilation, odour, airflow

| Source | URL | Status | Carries |
|---|---|---|---|
| Bartok, "Greenhouse Ventilation," eXtension/UConn | `farm-energy.extension.org/greenhouse-ventilation/` | **200 via curl** (403 to WebFetch) | 1 ACH/min summer max = 8-10 °F rise; **1.25× intake rule**; intake field test; 10-20 °F over ambient in extreme heat |
| Rutgers E277 (Wheeler & Both) | `rucore.libraries.rutgers.edu/rutgers-lib/47188/PDF/1/` | 200 | 8-10 cfm/ft²; static pressure 0.05 in w.g. (range 0.03-0.13); inlet/screen derates |
| Purdue HO-327-W (Nemali) | `extension.purdue.edu/extmedia/HO/HO-327-W.pdf` | 200 | **68-78 °F optimum; 78-85 °F = excess growth; damage >90 °F**; 8-10 cfm/ft² |
| UMass, Horizontal Air Flow | `umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/horizontal-air-flow-is-best-for-greenhouse-air-circulation` | 200 | **2 cfm/ft² circulation; 50-100 fpm at canopy**; disease mechanism |
| Denver DPHE Cannabis BMP — Air Quality | `denvergov.org/content/dam/denvergov/Portals/771/documents/EQ/MJ%20Sustainability/6_Cannabis_BestPracticesManagementGuide_AirQuality.pdf` | 200 | **Filter life 6-12 months**; contact time; humidity; pre-filter 6-8 months |
| Can-Filters filter calculator | `canfilters.com/help/filter-calculator/` | 200 | **10-25%** filter derate (manufacturer's own figure) |
| LBNL, Compression Effects in Flexible Ducts | `osti.gov/servlets/purl/836654` | 200 | **Slack duct = 4× pressure drop, up to ~10×** |
| ATCO acoustic data (ADC FD-72R1) | `atcoflex.com/wp-content/uploads/2024/08/Acoustic-Data.pdf` | 200 | Insulated-duct insertion loss per 10 ft by octave band |
| Greenheck Fan Fundamentals | `content.greenheck.com/public/DAMProd/Original/10002/FanFundamentals.pdf` | 200 | **Fan laws** — BHp varies with cube of rpm |
| Aerovent FE-300, Fan Sound | `aerovent.com/wp-content/uploads/sites/2/2021/12/Fan-Sound-and-Sound-Ratings-FE-300.pdf` | 200 | Sound ∝ static pressure; <3000 rpm advice |
| UMass, Reducing Humidity in the Greenhouse | `umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/reducing-humidity-in-greenhouse` | 200 | Condensation-onset RH by temperature |
| Fundamentals of Industrial Hygiene ch.19 (LEV) | `faculty.uml.edu/swoskie/recognition/fihchap19.pdf` | 200 | **Negative upstream / positive downstream of the fan** |
| Chandra et al. 2008, *Physiol Mol Biol Plants* 14:299 | `pmc.ncbi.nlm.nih.gov/articles/PMC3550641/` | 200 | Crop photosynthesis optimum 25-30 °C at ~1500 PPFD |
| IRC 2021 R311.2 | `codes.iccsafe.org/s/IRC2021P2/chapter-3-building-planning/IRC2021P2-Pt03-Ch03-SecR311.2` | 200 | 32 in egress clear width; interior doors exempt |

**The equation the ventilation article is missing:** `CFM = BTU/hr ÷ (1.08 × ΔT)`. A 480 W LED = 1,638 BTU/hr, so 101 CFM holds a 15 °F rise, 152 CFM holds 10 °F, 303 CFM holds 5 °F. This single line reconciles the whole article — the 4-in vs 6-in contradiction, the "oversized wastes power" vs "run a 6-in at 40%" contradiction, and the 200-400 CFM figure — without new argument. **Always carry the ΔT with the CFM.**

### 5.3 Hydroponics, growing media, watering automation

| Source | URL | Status | Carries |
|---|---|---|---|
| **OkState HLA-6722, EC & pH Guide for Hydroponics** | **`pods.okstate.edu/fact-sheets/HLA-6722pod.pdf`** | **200** | **Per-crop EC/pH table — see below** |
| OkState HLA-6708, Mist Propagation | `pods.okstate.edu/fact-sheets/HLA-6708pod.pdf` | 200 | Rooting medium 75 °F optimum |
| UF/IFAS HS1422, Lettuce in Small Hydroponic Systems | `ask.ifas.ufl.edu/publication/HS1422` | 200 | Lettuce EC 1.2-1.8; pH 6.0-7.0; 65-80 °F; DO 5 mg/L |
| Cornell CEA Lettuce Handbook | (see §5.1) | 200 | EC 1150-1250 µS **above source water**; DO 7 ppm, failure <3 |
| OSU/Ohioline HYG-1437 | `cfaes.osu.edu/fact-sheet/hydroponic-nutrient-solution-optimized-greenhouse-tomato-production` | 200 | Tomato EC 2.0→2.4 dS/m by stage; pH 5.5-6.5 |
| UNH, Hydroponics at Home | `extension.unh.edu/resource/hydroponics-home` | 200 | Solution change by system type; pH 5.5-7.0 at home |
| e-GRO Edible Alert 3(1) (Mattson, Pythium) | `e-gro.org/pdf/E301.pdf` | 200 | **Root zone 68-75 °F; both cold and warm favour a Pythium sp.** |
| UMass, Water Quality: pH and Alkalinity | `umass.edu/agriculture-food-environment/greenhouse-floriculture/fact-sheets/water-quality-ph-alkalinity` | 200 | **Alkalinity is the buffer**; 0-100 ppm acceptable, 30-60 optimum |
| UF/IFAS FA171, Chlorine—Friend or Foe? | `ask.ifas.ufl.edu/publication/FA171` | 200 | **24 h vigorous aeration; chloramine does NOT off-gas** |
| VT SPES-128P, Leaching Fraction | `pubs.ext.vt.edu/SPES/SPES-128/SPES-128.html` | 200 | LF is **EC-dependent**: 10% / 20% / 30% |
| Clemson HGIC 1459, Indoor Plants – Watering | `hgic.clemson.edu/factsheet/indoor-plants-watering/` | 200 | Finger test to first joint; water till it runs out; **meters affected by fertiliser and soil type** |
| UC IPM Pest Notes 7448, Fungus Gnats | `ipm.ucanr.edu/home-and-landscape/fungus-gnats/` | 200 | Larval diet; Bti at ~5-day intervals; dry the surface |
| CSU 5.584, Fungus Gnats | `extension.colostate.edu/resource/fungus-gnats-as-houseplant-and-indoor-pests/` | 200 | **Peat-heavy moist media are most attractive**; dry top 1-2 in |
| LSU AgCenter, Growing Media Part 4 | `lsuagcenter.com/~/media/system/d/6/0/f/.../growing%20media%20for%20containers%20part%204%20-%20the%20recipespdf.pdf` | 200 | Perlite ≈ 1 part in 4-5 |
| Grodan Grow Guide (V2) | `grodan.com/siteassets/downloads/downloads-na-101/grow-guide-2023/growing-in-grodan-products.pdf` | 200 | Conditioning pH 5.5-6.5, EC ≥1.5; runoff 5-15% veg / 15-25% gen |
| CANNA, Characteristics of rock wool | `cannagardening.com/articles/characteristics-rock-wool` | 200 | 80% solution / 15% air after drainage; **vertical moisture gradient** |
| ROCKWOOL Safe Use Instruction Sheet | `rockwool.com/siteassets/rw-na-ranson/operations/rockwool-safe_use_instruction_sheet.pdf` | 200 | Mechanical irritation; gloves + pre-wet |
| IARC Monographs Vol. 81 | `ncbi.nlm.nih.gov/books/NBK396448/` | 200 | Stone wool = **Group 3**, not classifiable |
| Perlite Institute, Safe and Natural | `perlite.org/wp-content/uploads/2021/06/Perlite-SafeNatural.pdf` | 200 | **Amorphous** silica; OSHA PNOR nuisance dust — *not* a silicosis risk |
| Blumat Classic user manual | `blumat.com/storage/app/media/classic/manual/Blumat_Classic_online_user_manual_EN.pdf` | 200 | **Head-height rule + flow rates**; annual clean (no vinegar) |
| Illinois Extension, Container Drainage Options | `extension.illinois.edu/container-gardens/container-drainage-options` | 200 | Self-watering = capillary wicking, not demand sensing |
| Woznicki et al. 2023, *Front. Plant Sci.* | `frontiersin.org/journals/plant-science/articles/10.3389/fpls.2023.1307240/full` | 200 | Coir transport footprint + deforestation (**not** water use or labour) |

**OkState HLA-6722 Table 2 — optimum EC and pH for hydroponic crops** (Singh & Dunn, Oct 2016). This is a drop-in replacement for the site's unsourced feed chart.

| Crop | EC (mS/cm) | pH | | Crop | EC (mS/cm) | pH |
|---|---|---|---|---|---|---|
| Asparagus | 1.4-1.8 | 6.0-6.8 | | Lettuce | 1.2-1.8 | 6.0-7.0 |
| African Violet | 1.2-1.5 | 6.0-7.0 | | Marrow | 1.8-2.4 | 6.0 |
| **Basil** | **1.0-1.6** | **5.5-6.0** | | Okra | 2.0-2.4 | 6.5 |
| Bean | 2.0-4.0 | 6.0 | | Pak Choi | 1.5-2.0 | 7.0 |
| Banana | 1.8-2.2 | 5.5-6.5 | | **Peppers** | **0.8-1.8** | **5.5-6.0** |
| Broccoli | 2.8-3.5 | 6.0-6.8 | | Parsley | 1.8-2.2 | 6.0-6.5 |
| Cabbage | 2.5-3.0 | 6.5-7.0 | | Rhubarb | 1.6-2.0 | 5.5-6.0 |
| Celery | 1.8-2.4 | 6.5 | | **Sage** | **1.0-1.6** | **5.5-6.5** |
| Carnation | 2.0-3.5 | 6.0 | | Spinach | 1.8-2.3 | 6.0-7.0 |
| Courgettes | 1.8-2.4 | 6.0 | | Strawberry | 1.8-2.2 | 6.0 |
| Cucumber | 1.7-2.0 | 5.0-5.5 | | **Tomato** | **2.0-4.0** | **6.0-6.5** |
| Eggplant | 2.5-3.5 | 6.0 | | Leek | 1.4-1.8 | 6.5-7.0 |
| Ficus | 1.6-2.4 | 5.5-6.0 | | | | |

Also from HLA-6722, and directly relevant: alkalinity **>75 ppm** drives pH up and demands more frequent checks · **"The pH and EC should be checked daily"** and at the same time of day · **"Water temperature of 72 to 75 °F is optimal"** · **"It is advisable to replace the nutrient solution completely every two weeks"** · **"In soil culture, soil acts as a buffer… This buffer is absent in soilless culture."** The last three each *partially rehabilitate* claims other maps marked contradicted — see §8.

### 5.4 Nutrients and deficiency diagnosis

| Source | URL | Status | Carries |
|---|---|---|---|
| e-GRO Alert 9(8), Nutrient Disorder Primer | `e-gro.org/pdf/2020_908.pdf` | 200 | **The best single symptom reference.** Soilless pH 5.8-6.2; low-pH Fe/Mn toxicity; per-nutrient symptoms |
| e-GRO Research Update 2016.04 (Mattson & Merrill) | `e-gro.org/pdf/2016-4.pdf` | 200 | Controlled single-element omission in basil; **onset ~2 wk macros, 4 wk Fe** |
| e-GRO Alert 13(13), Petunia Purpling | `e-gro.org/pdf/2024-13-13.pdf` | 200 | **Anthocyanin has many drivers**; LED root-zone cold; Mg purpling |
| Purdue HO-237-W, pH and EC in Soilless Substrates | `extension.purdue.edu/extmedia/ho/ho-237-w.pdf` | 200 | **Substrate pH 5.4-6.2; PourThru EC target table** |
| Altland & Buamscha 2008 (USDA-ARS copy) | `ars.usda.gov/ARSUserFiles/50820500/Publications/Altland215699_2007_pHDFB.pdf` | 200 | **The 1-1.5 pH-unit soil/soilless offset**, documented since 1961 |
| CSU GardenNotes #223, Iron Chlorosis | `cmg.extension.colostate.edu/Gardennotes/223.pdf` | 200 | **Above pH 7.5 only EDDHA/EDDHMA work** |
| NC State Ext. Gardener Handbook ch.16 | `content.ces.ncsu.edu/extension-gardener-handbook/16-vegetable-gardening` | 200 | Vegetable soil pH 6.0-6.5 |
| UMass SPTTL-3, Adjusting Soil pH | `umass.edu/agriculture-food-environment/sites/ag.umass.edu/files/fact-sheets/pdf/spttl_3_adjusting_soil_ph_0.pdf` | 200 | **Sulfur is a months-long amendment; re-test at 4-6 months** |
| UGA B1318, Growing Indoor Plants with Success | `fieldreport.caes.uga.edu/publications/B1318/growing-indoor-plants-with-success/` | 200 | **¼ label rate monthly + feedback rule**; 58-86 °F; low-light symptom list |
| Cornell SoilNOW, diagnosing by leaf symptom | `blogs.cornell.edu/soilnow/ph/how-to-diagnose-plant-nutrient-deficiencies-using-leaf-symptoms/` | 200 | Mobile/immobile lists (**note: their page lists Mg twice — do not copy verbatim**) |
| UF/IFAS BUL343/AE266, Soil Water Content Devices | `edis.ifas.ufl.edu/publication/AE266` | 200 | **Resistance probes are salinity-sensitive**; gypsum buffers, cheap probes don't |
| UMD, Blossom End Rot on Vegetables | `extension.umd.edu/resource/blossom-end-rot-vegetables` | 200 | **Water movement, not soil calcium** |
| Purdue, Match Plant to Proper Container | `purdue.edu/hla/sites/yardandgarden/match-plant-to-proper-container/` | 200 | "Next size larger" + pull-the-rootball rule |
| NC State, Botrytis Blight | `content.ces.ncsu.edu/botrytis-blight-of-greenhouse-ornamentals` | 200 | Air circulation; <3 h/day high humidity |
| CSU PlantTalk 1317 | `planttalk.colostate.edu/topics/houseplants/1317-houseplants-temperature-humidity/` | 200 | Cool/intermediate/warm categories |

**Three pH targets, not two** — the site currently merges soil and soilless into one chart, which is a documented ~1 to 1.5 unit error: **garden soil 6.0-6.5 · soilless container mix 5.4-6.2 · recirculating solution 5.6-6.0.**

### 5.5 Pests and IPM

| Source | URL | Status | Carries |
|---|---|---|---|
| UC IPM Mealybugs | `ipm.ucanr.edu/home-and-landscape/mealybugs/` | 200 | **70% isopropyl** dab; weekly repeat |
| UC IPM Fungus Gnats | `ipm.ucanr.edu/home-and-landscape/fungus-gnats/` | 200 | Bti ~5-day intervals; ~17-day cycle at 75 °F; traps catch **adults only** |
| UC IPM Aphids | `ipm.ucanr.edu/home-and-landscape/aphids/` | 200 | 7-8 days nymph→reproducing adult |
| KSU MF3001, Mealybug Management | `bookstore.ksre.ksu.edu/pubs/mealybug-management-in-greenhouses-and-interiorscapes_MF3001.pdf` | 200 | **Egg to adult ≈ 60 days** |
| KSU MF2997, Twospotted Spider Mite | `bookstore.ksre.ksu.edu/pubs/twospotted-spider-mite-management-in-greenhouses-and-nurseries_MF2997.pdf` | 200 | **14 d at 70 °F, 7 d at 84 °F**; optimum 30-50% RH |
| Clemson, Common Houseplant Insects | `hgic.clemson.edu/factsheet/common-houseplant-insects-related-pests/` | 200 | Weekly forceful rinse |
| Clemson, Insecticidal Soaps | `hgic.clemson.edu/factsheet/insecticidal-soaps-for-garden-pest-control/` | 200 | **1-2% rate; not above 90 °F; 48 h to see injury** |
| Bonide Captain Jack's Neem **Max** label | `files.plytix.com/.../l020.pdf` | 200 | **0.8-1.5 fl oz/gal, 10-14 day interval** |
| Bonide Neem Oil Concentrate label | `files.plytix.com/.../l024.pdf` | 200 | 2 tbsp/gal, 7-14 days; **up to day of harvest** |
| Summit Mosquito Bits label | `summitchemical.com/wp-content/uploads/2021/01/119-1-SPECIMEN-Mos-BITS.pdf` | 200 | **4 tbsp/gal, soak 30 min, skim, weekly ×3** |
| Iowa State, sanitizing pruning shears | `yardandgarden.extension.iastate.edu/faq/how-do-i-sanitize-my-pruning-shears` | 200 | 70% isopropyl; 10% bleach alternative |
| PNW Handbooks, Fluorine Toxicity | `pnwhandbooks.org/plantdisease/pathogen-articles/nonpathogenic-phenomena/fluorine-toxicity-plants` | **200 via curl** (403 to some fetchers) | Fluoride tip necrosis; Dracaena and spider plant |
| ASPCA toxic plant database | `aspca.org/pet-care/animal-poison-control/toxic-and-non-toxic-plants/<plant>` | 200 | Per-plant toxicity records |
| UMN, Preventing seedling damping off | `extension.umn.edu/solve-problem/how-prevent-seedling-damping` | 200 | Pathogens; 10% bleach sanitation; airflow |

### 5.6 Seed starting and propagation

| Source | URL | Status | Carries |
|---|---|---|---|
| Harrington (UC Davis), Soil Temperature for Germination — WSU copy | `wpcdn.web.wsu.edu/extension/uploads/sites/43/2024/04/Soil-Temperature-Conditions-for-Vegetable-Seed-Germination.pdf` | 200 | **Per-crop min/optimum/max + days-to-emergence** |
| NC State Handbook ch.13, Propagation | `content.ces.ncsu.edu/extension-gardener-handbook/13-propagation` | 200 | Cutting length; **light/dark germination Table 13-1**; hardening ≥2 weeks; auxin effects |
| UMN, Starting seeds indoors | `extension.umn.edu/planting-and-growing-guides/starting-seeds-indoors` | 200 | Depth rule; 12-16 h; **mix runs 5 °F below air**; 2-week hardening |
| Illinois, Seed Viability and Germination | `extension.illinois.edu/sites/default/files/seed_viability.pdf` | 200 | Viability table; **10-seed test decision rule with no gaps** |
| Iowa State, Storing Seeds / Germination Rates | `hortnews.extension.iastate.edu/1999/4-2-1999/veggielife.html` | 200 | **20 seeds min, 50 better**; % thresholds; 70-80 °F |
| Yang et al., lettuce thermoinhibition | `pmc.ncbi.nlm.nih.gov/articles/PMC11314492/` | 200 | Lettuce fails above ~25-30 °C; **reversible** |
| Velez-Ramirez et al., phyA and continuous light | `pmc.ncbi.nlm.nih.gov/articles/PMC6363712/` | 200 | CL injury is a species exception, not a rule |
| Mason et al. 2014, PNAS (apical dominance) | `pmc.ncbi.nlm.nih.gov/articles/PMC4000805/` | 200 | **Sugar demand, not auxin, is the initial regulator** |
| Santos, Fisher & Argo, Nutrient Supply in Propagation | `gpnmag.com/article/nutrient-supply-propagation/` | 200 | **50-100 ppm N from root initiation** |
| Hydrofarm seedling heat mat | `hydrofarm.com/p/seedling-heat-mat/mt10004` | **200** | **"warming the root area 10-20 °F over ambient"** — manufacturer spec, verbatim |
| Clonex (Hydrodynamics Intl.) | `hydrodynamicsintl.com/clonex-rooting-gel/` | 200 | Storage **conditions**, deliberately **no shelf life** |
| USPTO, Plant Patents (35 U.S.C. 161) | `uspto.gov/patents/basics/apply/plant-patent` | 200 | Asexual reproduction excluded, 20 yr, no gift carve-out |

### 5.7 Microgreens, herbs, vegetables

| Source | URL | Status | Carries |
|---|---|---|---|
| **USU, Grow Your Own Microgreens** | `extension.usu.edu/yardandgarden/research/grow-your-own-microgreens` | 200 | **Per-variety table: seed g/1020, presoak, blackout, days to harvest, dated seed cost.** The whole article rebuilds from this one page |
| Iowa State, Growing Herbs Indoors | `yardandgarden.extension.iastate.edu/how-to/growing-herbs-indoors` | 200 | **~8 h direct light**; easy vs hard herb split; feeding at ½–¼ strength, not in winter |
| Utah State, Basil in the Garden | `extension.usu.edu/yardandgarden/research/basil-in-the-garden` | 200 | **Pinching flowers does NOT stimulate foliage** — contradicts near-universal advice |
| OSU SP 50-921, Drying Herbs | `extension.oregonstate.edu/sites/extd8/files/documents/8836/sp50921dryingherbs.pdf` | 200 | Bursting-bud harvest; **air dry 5-10 d; dehydrator 90-100 °F, 1-3 h; microwave protocol + fire warning** |
| OSU SP 50-701, Herbs and Vegetables in Oil | `extension.oregonstate.edu/catalog/pub/sp-50-701-herbs-vegetables-oil` | 200 | ***C. botulinum*** — refrigerate or freeze; no home acidification |
| NC State, Harvesting and Preserving Herbs | `content.ces.ncsu.edu/harvesting-and-preserving-herbs-for-the-home-gardener` | 200 | **Up to 75% of season's growth**; early morning after dew; water ice-cube freezing |
| Illinois, Herbs: Harvesting | `extension.illinois.edu/herbs/harvesting` | 200 | **Annual 50-75% vs perennial ⅓**; basil pruning protocol |
| Rutgers FS1283, Basil Postharvest | `njaes.rutgers.edu/fs1283/` | 200 | Chilling injury below 50-54 °F; afternoon harvest reduces it |
| Illinois, Growing Vegetables in Containers | `extension.illinois.edu/container-gardens/growing-vegetables-containers` | 200 | **Container size table — cherry/patio tomato = 1 gallon** |
| Clemson, Container Vegetable Gardening | `hgic.clemson.edu/factsheet/container-vegetable-gardening/` | 200 | 6-8 in minimum depth; 8-10 h light for fruiting |
| UMN, Growing peppers | `extension.umn.edu/vegetables/growing-peppers` | 200 | **Nights <60 °F or >70 °F, days >90 °F → flower drop**; start seed 8 wk before transplant |
| Clemson, Why Did My Tomatoes Stop Producing Fruit? | `hgic.clemson.edu/why-did-my-tomatoes-stop-producing-fruit/` | 200 | Optimal set 70-84 °F day / 64-70 °F night |
| UMN, Growing radishes / carrots / lettuce | `extension.umn.edu/vegetables/...` | 200 | 3-5 weeks; bitterness from moisture stress |
| Iowa State, Pollination in the Vegetable Garden | `hortnews.extension.iastate.edu/1996/3-22-1996/pollen.html` | 200 | **Pollen vibrator = electric toothbrush** — greenhouse practice |
| UNL G2205, Guide to Growing Houseplants | `extensionpubs.unl.edu/publication/g2205/na/html/view` | 200 | **RH 40-60%; injury under 20%**; leach 4-5 times |
| UNH, increasing humidity for houseplants | `extension.unh.edu/blog/2025/01/how-can-i-increase-humidity-indoors-my-houseplants` | 200 | **Ranks the fixes**: humidifier > grouping > pebble tray |
| Thiram 480 DP label (24(c)) | `s3-us-west-1.amazonaws.com/agrian-cg-fs1-production/pdfs/Thiram_480_DP_Section_24c.pdf` | 200 | **"Do not use treated seed for food, feed, or oil purposes"** |
| Illinois RPD 915, Vegetable Seed Treatment | `ipm.illinois.edu/diseases/rpds/915.pdf` | 200 | Garden seed is routinely treated |
| FDA microgreens recall notice | `fda.gov/safety/recalls-market-withdrawals-safety-alerts/greenbelt-greenhouse-ltd-recalls-greenbelt-microgreens-brand-microgreens-because-possible-health` | 200 | Concrete counterexample to "risk-free" |
| Kou et al., microgreen storage (PMC9966302) | `ncbi.nlm.nih.gov/pmc/articles/PMC9966302/` | 200 | 14 d at 5 °C; 1-2 d at ambient |

**USU microgreens table, per 1020 tray** — seed g / presoak / blackout d / harvest d / seed cost (as of 1/8/2026, 5 lb+ rate):
arugula 10 g / – / 1-2 / 6-8 / $0.17 · basil 28 / – / 4-7 / 12-16 / $1.84 · broccoli 28 / – / 2-4 / 8-12 / $1.12 · cilantro 28 / – / 7-14 / 21-28 / – · kale 28 / – / 1-2 / 8-12 / $0.37 · mesclun 28 / – / 3-5 / 12-14 / $1.45 · **pea 150 / 6 h / 3 / 8-10 / $1.16** · radish (champion) 42 / – / 1-2 / 8-12 / $0.88 · radish (purple) 42 / – / 1-2 / 8-12 / $1.95 · rutabaga 28 / – / 1-2 / 8-12 / $0.35 · **sunflower 48 / 12 h / 3 / 9-10 / $0.45**.
Environment: 74 °F germination, 72 °F lights-on, 68 °F lights-off; **18 h on / 6 h dark**; 2-5 lb flat weight on **every** variety for the first half of the blackout, then invert the tray as a non-contact cover; harvest **at first true leaves**, not by height.

---

## 6. Claim-by-claim map

Verdicts: **C** = contradicted (must change) · **S** = sourced (keep, usually tighten) · **U** = unsourceable (see §7).

### led-vs-hps-grow-lights
| Claim | | Correction / source |
|---|---|---|
| "450W LED and 600W HPS deliver roughly comparable usable light" | **C** | Not comparable. 450 W LED at 2.5-2.8 µmol/J = 1,125-1,260 µmol/s; a 600 W SE HPS (~645 W wall) ≈ 600-870 µmol/s. LED matches or beats it on photons and wins decisively on watts. *Nelson & Bugbee 2014* |
| "$0.15/kWh" | **C** | §2.1 |
| "seedlings 100-300, greens 200-400, fruiting 400-700+" PPFD | **C** | Fruiting ceiling overshoots ~30%. Publish DLI + conversion instead. *Purdue / UMN / Cornell* |
| "LEDs 2.5-2.8 µmol/J, HPS ~1.7" | **S** | 1.7 is **1000 W DE only**; the modelled SE fixture is ~1.0. Attach the fixture class. *DLC V4.0 + Kusuma 2020* |
| "tens of thousands of hours before any noticeable drop" | **C** | §4.5. Rewrite to "rated L70 at 50,000 h — putting out ~70% of original by then." *DOE SSL* |
| "CMH… better efficiency than HPS" | **C** | Backwards: CMH 1.46 vs DE HPS 1.70. *Nelson & Bugbee 2014* |
| Ballast losses ignored | **S** | Measured input exceeds rating by 3-11%; a "600 W" SE draws ~640-665 W. LED ratings are already input power |
| "LEDs run cool… a basic clip fan is genuinely enough" | **C** | §4.2. **Cut outright.** Highest-harm claim in the set |
| "1000W equivalent pulls 100-150W" · T5 $40 / HPS kit $50-80 / bulb $20-30 · "broader spectrum is why growers switch" | **U** | §7 |

### understanding-grow-light-schedules
| Claim | | Correction / source |
|---|---|---|
| Schedules-by-crop table | **C** | Houseplants 12-14 h (not 10-12); tomato/pepper 14-16 h is well supported, never above 17 h. *UMN + Arkansas* |
| "$0.15/kWh" → $14-15, $22, $90 | **C** | §2.1 |
| Table 12-14 h vs FAQ 14-16 h for greens | **C** | §4.1. Correct the **table** to match the FAQ, not the reverse |
| Body 50% vs FAQ 40% for 16→24 h | **C** | **Arithmetic**: 24/16 = 1.5. Fix the FAQ (rich-result eligible) |
| "tomatoes… mottled damaged leaves under continuous light" | **S** | Best-supported claim on the page. Add the >17 h threshold and genotype dependence. *Marie et al. 2024* |
| "14 hours. Nothing common resents 14 hours." | **C** | Spinach's critical daylength is 13-14 h. Even there, temperature dominates bolting. *e-GRO E201 + Iowa State* |
| "Lettuce, spinach, greens 12-14 h" | **C** | Split spinach out; greens 14-18 h at DLI 12-17. Bolting is a **temperature** problem first. *Cornell + e-GRO* |
| "Photosynthesis is roughly cumulative" | **S** | True; state the two bounds (compensation point below, photoperiod tolerance above). *Jeong et al. 2025* |
| "overnight rates cut cost by a third" · "$12 timer" · wandering-onset 14 h is worse than steady 12 h | **U** | §7 |

### choosing-a-grow-tent-for-beginners
| Claim | | Correction / source |
|---|---|---|
| "$0.15/kWh" → $11, $32 | **C** | §2.1 |
| "70-82 °F… fix exhaust past 85 °F" | **C** | **68-78 °F optimum; 78-85 °F = stretch; damage >90 °F.** *Purdue HO-327-W* |
| Crop-specific temperature ceiling | **S** | Peer-reviewed optimum is 25-30 °C (77-86 °F) at 1500 PPFD. If keeping ~82 °F, say it's about VPD/equipment margin, not photosynthesis. *Chandra 2008* |
| "assembled 4x4 doesn't fit a standard door" | **S** | **The audit is wrong here — keep it.** 48 in exceeds any interior door in every orientation; IRC sets 32 in for the *egress* door and exempts others |
| "sturdy 600D fabric" | **C** | Denier is linear density (yarn mass), not strength. Say "600D entry / 1680D heavy; a thickness proxy, not a durability rating." **Do not buy ASTM D1907** |
| No electrical guidance | **S** | Add NEC 210.20(A): continuous load ≤80% of circuit → **1,440 W on 15 A, 1,920 W on 20 A**. Extension cords are temporary |
| "12 in headroom" · full cost table · "most tents include…" | **U** | §7 |

### grow-tent-odor-control-and-ventilation
| Claim | | Correction / source |
|---|---|---|
| "filter costs 25-30% of rated airflow" | **C** | Manufacturer's own figure is **10-25%**, and it is a curve intersection, not a constant. *Can-Filters* |
| "one air change every 1-3 minutes" | **C** | 1 ACH/min is a **summer maximum** tied to an 8-10 °F rise; ¼/min is the winter rate. *Bartok* |
| "200-400 CFM for a 4x4" | **C** | Three extension anchors give 104-160 CFM. Show `CFM = BTU/hr ÷ (1.08 × ΔT)` and state the ΔT you're buying |
| "filters last 12-18 months" (×3) | **C** | **6-12 months.** §4.4. *Denver BMP* |
| "filter after the fan cuts filtration effectiveness" | **C** | Effectiveness is contact time, identical either side. The real reason is **pressure sign** — everything downstream of the fan is pressurised and leaks outward. Delete the fabricated half |
| Hot tent ← "filter placed after the fan" | **C** | Filter position is not a heat variable. Replace with wattage/ΔT, exhaust-into-same-room, restricted intake, ambient |
| 4-in vs 6-in contradiction | **S** | 4-in = 205 CFM free air → ~154-185 CFM after derate: below the article's own 200+ but above the extension 104-160. Resolve as "enough, but no headroom" |
| "oversized fan wastes power" | **C** | Backwards — power varies with the **cube** of speed; 40% speed ≈ 6% of power. Delete or narrow to the drying point |
| "half speed is dramatically quieter" | **S** | ≈**15 dB** per halving. If anything an understatement |
| "insulated ducting muffles noticeably" | **S** | Per 10 ft of 6-in: 8/19/35/41/46/31 dB at 125-4000 Hz. Weakest at low frequency; **don't extrapolate past 10 ft** |
| "every 90° bend costs more" | **S** | Bends ≈ Co 0.82-0.87 — but **slack matters far more: 4× pressure drop, up to ~10×.** New, actionable, currently missing |
| "walls bow gently inward" | **C** | Half right. Walls **sucked hard** against the frame = inadequate intake (Bartok's field test) |
| Intake fan mentioned, never sized | **S** | **Intake area ≥1.25× fan area**; intake fan must always be the weaker one; target ~0.05 in w.g. |
| Clip fan "gently sways" | **S** | **2 cfm/ft² total; 50-100 fpm at canopy.** A 4x4 wants ~32 CFM — a clip fan is genuinely right-sized |

### setting-up-a-basic-hydroponic-system
| Claim | | Correction / source |
|---|---|---|
| "sit uncovered a few hours to off-gas chlorine" | **C** | **24 h vigorous aeration**, and **chloramine does not off-gas at all**. Tell readers to ask their utility which is used |
| Lettuce EC 0.8-1.2 | **C** | 1.2-1.8 (UF, OkState); Cornell 1.15-1.25 **above source water**. §4.8 |
| Tomato EC 2.0-3.0 | **C** | ~2.0→2.4 dS/m by stage. *OSU HYG-1437* (OkState's 2.0-4.0 is the outlier — see §8) |
| Herb / pepper / seedling EC rows | **C** | **Now sourceable.** Basil and sage **1.0-1.6** (article's herb row is right); **peppers 0.8-1.8** — the article's 1.8-2.4 is contradicted. *OkState HLA-6722* |
| Reservoir 65-72 °F, "above 75 °F = pythium" | **C** | **68-75 °F** (e-GRO) or 72-75 °F (OkState). No cold-side safety: *P. dissotocum* favours cool, *P. aphanidermatum* warm |
| "full change every 1-2 weeks" | **C→hedge** | UNH: months to years by system type. **OkState: "replace completely every two weeks."** §8 |
| "check pH every 2-3 days" | **C→hedge** | UNH implies no fixed interval; **OkState says daily**. Lead with alkalinity as the driver. §8 |
| "in a hydroponic reservoir there's no buffer" | **C→hedge** | UMass: alkalinity **is** the buffer. **OkState says the buffer "is absent in soilless culture."** Best synthesis: the buffer is whatever alkalinity the fill water carried in — RO swings hard, hard tap water resists then climbs |
| "roots suffocate within a day or two" | **C** | Replace with DO numbers: ≥6 ppm target, 8-9 ideal, inhibition <4, failure <3. Drop the absolute — Kratky runs unaerated by design |
| DWC "fewest moving parts of any method" | **C** | False — Kratky has none. Add a Kratky section or say "simplest **powered** method" |
| Cost breakdown "meters are two-thirds" | **C** | **Arithmetic**: $50-100 of $135-195 is 37-51%. "A third to a half" |
| "swings exceed ~0.5/day" | **U** | §7 |

### choosing-a-grow-medium-soil-vs-coco-vs-rockwool
| Claim | | Correction / source |
|---|---|---|
| "10-20% runoff" | **S** | Present as **EC-dependent**: 10% / 20% / 30% by irrigation EC. *VT SPES-128P* |
| "water every 3-7 days" | **C** | Keep the trigger, drop the interval. §4.3 |
| "perlite 20-30% by volume" | **S→adjust** | Extension recipes cluster at 1 part in 4-5. Say "about one part perlite to four or five" |
| "rockwool has naturally high starting pH" | **S** | Give the **conditioning** target (pH 5.5-6.5, EC ≥1.5) — that's the actionable number. Do **not** publish a numeric dry-substrate pH (§7) |
| "Grodan since 1969" | **S** | Attribute in text ("Grodan says…") — it's a company self-claim next to an affiliate link |
| Fungus gnats drawn to bark/compost | **C** | §4.6. Peat-heavy moist mixes are *most* attractive. Cut the product justification |
| OMRI "matters if you plan to eat it" | **C** | OMRI is an organic-compliance determination, not a safety one. Cut the clause |
| FAQ "coir more sustainable? Generally yes" | **C** | Hedge — in FAQPage schema. Transport footprint + deforestation are real. *Woznicki 2023* (**not** water use or labour — needs its own source or drop) |
| Missing: rockwool fibre irritation | **S** | Gloves + pre-wet. **IARC Group 3** — mechanical irritation, not cancer. Don't overstate |
| Missing: perlite dust | **C** | Add the warning but **not** as "silica hazard" — the audit's framing would be a new error. Amorphous silica, OSHA nuisance dust |
| Coco brick expansion ratio · four price claims | **U** | §7 |

### automating-your-indoor-garden-watering
| Claim | | Correction / source |
|---|---|---|
| "1:1 vinegar soak overnight" | **C** | Manufacturer says: annually, warm water 5 min, brush/scrape, flush by pressing the cap underwater, sand the cone. **No vinegar anywhere.** *Blumat manual* |
| "soak the cone 15 min" | **S** | That's the **US distributor**; the manufacturer says fill the cone to the brim and cap it full |
| Missing: head-height rule | **S** | Level just below the cap = ideal (~75 ml/24 h); well below = ~50 ml; **above the cap = continuous siphon, up to 150 ml — the flood mode** |
| FAQ "nearly impossible to overwater" | **C** | False for both named systems, and it's in FAQPage schema. Blumat's own manual warns of overwatering; self-watering pots wick regardless of demand |
| "a stake + big jar carries a thirsty pot two weeks" | **C** | At 50-75 ml/24 h that's 0.7-1.05 L. Manufacturer says water with a can every 4-6 weeks regardless |
| Decision row: hydro "already automated" | **C** | Wrong on the sibling article's own terms. "Self-feeding, but still needs EC/pH monitoring and periodic changes" |
| "refill every 1-2 weeks is the entire maintenance schedule" | **U/incomplete** | No interval is defensible; **and** sub-irrigated pots accumulate salts and need periodic top-watering to flush |
| Drip flush "every few weeks" · cost table · setup-time estimate | **U** | §7 |

### nutrient-deficiency-identification-chart
| Claim | | Correction / source |
|---|---|---|
| "soil 6.0-7.0, hydro 5.5-6.5" | **C** | **Three targets**: soil 6.0-6.5 · soilless 5.4-6.2 · solution 5.6-6.0 |
| Merged pH-lockout table | **C** | The merge **is** the error — a documented 1-1.5 unit offset. *Altland & Buamscha 2008* |
| Direction of Fe/Mn/Zn lockout | **S** | Correct. Add the omitted low-pH risk in soilless: **Fe/Mn toxicity**, not Ca/Mg lockout |
| Mg given a separate "pale, faded" row | **C** | **Mg deficiency IS interveinal chlorosis.** Collapse into one symptom split by leaf position. Note K is the common confusion, not Fe |
| "iron at pH 7.5 does approximately nothing" | **C** | **Name the chelate.** Fe-EDDHA/EDDHMA work above 7.5; EDTA and DTPA don't. **Highest-value single fix in this article** |
| "fix the pH and the deficiency cures itself" | **C** | True for a reservoir, false for soil. Sulfur is a 4-6 month amendment; use a chelate or foliar feed this season |
| "purple stems → phosphorus" | **C** | Anthocyanin has many drivers. Indoors it's usually **cold or saturated root zone**, not a P-poor feed. Mg can also purple in cold |
| Mobile/immobile binary | **C** | Add the two that fool people: **sulfur** (uniform chlorosis, looks like N — position is the only tell) and **zinc** (Cornell's own list omits it) |
| Rest of the 7-row chart | **S** | 5 of 7 hold. Tighten Zn to "rosette-like clustering of small new leaves" |
| "half label strength" | **C** | **¼ label rate monthly**, with UGA's feedback rule up or down |
| "cut fertilizer strength in half" with no EC anchor | **S** | Give the **PourThru** column — the only method a home grower can perform. *Purdue HO-237-W Table 2* |
| Cal-mag: "coco binds Ca and Mg" | **C** | Vendor mechanism. Real: coir is inherently high K/Na, near-zero Ca/Mg, and excess K competes at uptake. Add the sulfur caveat — a no-S cal-mag can induce S deficiency |
| "normal within a week or two" | **U** | §7 |

### common-indoor-gardening-mistakes
| Claim | | Correction / source |
|---|---|---|
| **VPD paragraph ("0.59 kPa")** | **PHANTOM** | **Does not exist in the repo.** Verified: zero site-wide hits for VPD, kPa, "vapor pressure", "0.59". §9 |
| "65-80 °F" | **C** | UGA: **58-86 °F** tolerance vs 72-82 °F human comfort — a better and more reassuring sentence |
| "top inch or two dry" | **S** | UGA says "an inch or so" — dropping "or two" fixes the small-pot problem. Add UGA's modifier list |
| "go up two inches in pot diameter" | **U→rewrite** | Purdue says "the next size larger" with an **observable** rule: pull the root ball and look |
| XLUX meter "removes the guesswork" | **C** | Resistance probes track conductivity — fertiliser salts bias them wet. Collides with the article's own item 7. Demote to a coarse cross-check |
| Item 2: airflow fixes mold **and** legginess | **C** | Split. Mold → NC State/Botrytis + fan. Legginess → item 3 and UGA's low-light symptom list. Keep the thigmomorphogenesis point for stem strength |
| Item 3: no numbers at all | **S** | Give DLI targets + measure at canopy. **Drop foot-candle/lux framing** — VT says don't use it |
| "a week / two-to-three weeks" waiting periods · "five-dollar option" | **U** | §7 |

### dealing-with-indoor-plant-pests-naturally
| Claim | | Correction / source |
|---|---|---|
| Neem "every 5-7 days", no rate | **C** | **Label**: 0.8-1.5 fl oz/gal, **10-14 day** interval. 5-7 days is the miticide interval |
| Neem safe on edibles | **S** | Label says "up to day of harvest" — a citable fact. Add the omitted precautions (no stressed/wilted plants; early morning/late evening) |
| Azadirachtin "not approved for amateur use in parts of the EU" | **U** | **Cut.** §7 |
| Alcohol swab, no concentration | **S** | **70% or less**; 10-25% for spray; test 1-2 days ahead; repeat weekly |
| BTI "steep overnight, weekly for a month" | **C** | **Label**: 4 tbsp/gal, soak **30 minutes**, **skim and discard floating granules**, weekly ×**3** |
| BTI cadence | **C** | Label weekly×3, or UC IPM's ~5-day intervals. Bti does not persist indoors |
| "¼-inch coarse sand" | **U** | Practice is citable, **depth is not**. Lead with drying + Bti |
| Mealybugs "1-2 weeks egg to adult" | **C** | **≈60 days.** The 6-14 day figure is the **egg stage only**. Every derived instruction changes — plan on two months |
| Spider mites "5-7 days at room temp" | **C** | **14 d at 70 °F, 7 d at 84 °F.** 5-7 d is the >85 °F case. The 5-7 day *spray* interval survives for a different reason |
| Fungus gnats "3-4 weeks" | **S→range** | 17 d at 75 °F (UC IPM) to ~5 weeks (CSU). Give the range with temperature |
| Aphids "about a week" | **S** | 7-8 days — technically nymph→reproducing adult |
| Rinse cadences | **S** | Weekly during active infestation; wash in the morning so leaves dry |
| "humidity slows mites" | **S** | Mites optimal at **30-50% RH** → target 50-60% with air movement. Real danger is night condensation, not an RH number |
| Insecticidal soap "gentle" | **S** | §2.3 + the sensitive-species list |
| Fungus gnat plan = "dry soil + traps" | **C** | Traps catch **adults**; they are monitoring. Control = dry surface + Bti drench |

### houseplant-care-fundamentals
| Claim | | Correction / source |
|---|---|---|
| "heated air drops humidity to 25-35%" | **U→rewrite** | Target **40-60%**; injury under 20%. Iowa State says homes run 10-20% in winter — the article *understates* it |
| "repot every 1-2 years" | **C** | Fast growers annually, slow every 2-3 years; the trigger is roots, not the calendar |
| "half strength monthly" | **S** | Clemson states exactly this regime; pair with the general schedule and "no fertilizer in winter" |
| "run a few times the pot's volume" | **U** | No source. Use UNL's procedure: **repeat the leach 4-5 times**, draining between; UNH's cadence ~every 4 months |
| "finger two inches in" (×3) | **C** | **One knuckle, about one inch** |
| Pebble tray listed as equivalent to a humidifier | **C** | Extension **ranks** them: humidifier > grouping > tray ("a small benefit") |
| XLUX "no calibration involved" | **C** | That's the defect. Clemson: readings are affected by fertilizer and soil type |
| Miracle-Gro "less inviting to fungus gnats" | **C** | §4.6 |
| FAQ "crispy tips = low humidity, not overwatering" | **C** | Overstated. List four causes incl. **salts and fluoride/chloride** — spider plant and Dracaena are the classic fluoride indicators. Note standing water off-gasses chlorine but **not** fluoride |
| Light categories with no anchor | **S** | Clemson's foot-candle bands + window mapping; "a well-lighted home is often under 100 ft-c" |
| Missing: pet toxicity | **S** | Pothos, ZZ, heartleaf philodendron = toxic (insoluble calcium oxalates); spider plant non-toxic. **Name which, don't blanket-warn** |
| "$40 at a grocery store" | **U** | §7 |

### pruning-and-training-indoor-plants
| Claim | | Correction / source |
|---|---|---|
| "top at 5-7 nodes" | **C** | Extension is by **height**: at 12 in, prune to the second set of leaves; *C. annuum* only, establishment only |
| "peppers need topping once, early" | **S→hedge** | Illinois recommends it; trial literature is split on yield. Frame as an architecture decision, not a yield guarantee |
| "no more than a third of foliage" (×3) | **C** | No controlled basis. The two real rules: **ANSI A300 25% of live canopy/season** (trees) and renewal pruning **⅓ of the oldest stems/year** (shrubs). Keep as a rule of thumb, not a finding |
| "suckers under two inches" | **C** | **2-4 inches** is the citable window. Add: prune in the morning after plants dry |
| "basil/mint at 3-4 leaf pairs" | **S** | USU confirms (6-8 leaves), and adds how much to take. **⚠ USU also says pinching basil flowers does NOT stimulate foliage and reduces yield** — the cheapest "we checked and the internet is wrong" moment available |
| "leaves in deep shade aren't paying rent" | **C** | Criterion is the **light compensation point**, not appearance. Leaving lower leaves cost no yield in trial |
| "auxin suppresses buds below" | **C** | Add one clause: the **initial** trigger is sugar demand; auxin/strigolactones decide which released buds grow out. Practical upshot unchanged |
| "flowering stem has hormones pointed the wrong way" | **C** | It's **carbohydrate allocation**. Advice survives, explanation doesn't. Free additions: prefer lateral shoots; avoid N-pushed stock |
| Blade sanitation | **S** | §2.2. Reframe the edible-residue note as **disease hygiene** — both products are labelled up to harvest |
| "stub dies back a few mm" · "reasserts a top within a week" · "folds under four or five fruits" · sessions a week apart | **U** | §7 |

### seed-starting-guide-for-beginners
| Claim | | Correction / source |
|---|---|---|
| "70-80 °F suits most seeds" | **C** | No single band exists. Warm-season 75-85 °F vs cool-season 60-75 °F; NC State's single number is **65-75 °F** |
| Lettuce inside that band | **C** | Lettuce is 60-75 °F and **thermoinhibits above ~77-86 °F**. Name it as the heat-mat exception. (Use "thermoinhibition" — the block is reversible; "thermodormant" is wrong) |
| "twice the seed's width" | **S** | Cite UMN; note NC State's 2-4× **minimum diameter**, and UMN's usable check: deep enough that one more seed could sit on top |
| "12-16 h, not 24" | **S/C** | Keep 12-16 h (UMN). **Drop "not 24" as species-blind** — tomato is the documented exception, many species take 18-24 h fine |
| Seed shelf-life table | **C** | Two outright errors: **spinach is 3-5 years, not 1-2**; **parsley is 1 year, not 2-3**. Rebuild from **one** named source, stated in the caption |
| 10-seed test rule | **C** | Gaps at 2, 5, 6. Illinois: 10/10 normal, 7-9 sow thicker, **≤6 buy new**. Iowa State: 20 min (50 better), express as % |
| "harden off 7-10 days" | **C** | **At least two weeks** (NC State **and** UMN). Add the 45 °F floor, the no-wind rule, and the over-hardening warning |
| Germination timeline "days 1-6 nothing visible" | **C** | Tomato emerges in 6-8 d at 70-77 °F — the article says "nothing" right up to the day it sprouts. Index by temperature |
| "seed mix is free of pathogens and gnat eggs" | **C** | The property is **pasteurized**, not sterile, and gnats are a moisture problem. Note the article's own dome advice creates the breeding condition |
| "fine seeds like lettuce or basil need light" | **C** | Lettuce yes (NC State Table 13-1); **basil is buried ⅛-¼ in**. Split them, and don't conflate "too fine to cover" with "needs light" |
| Missing: post-emergence temperature drop | **S** | 65-70 °F day / 55-60 °F night prevents legginess — the second half of the fix, and it resolves the heat-mat question cleanly |
| Heat mat "10-20 °F bump" | **S** | **Manufacturer spec, now verified.** Attribute as such. Better still, give UMN's absolute: mix runs up to 5 °F **below** air, so target a soil temperature. Don't run the mat on the light timer |

### propagating-plants-from-cuttings
| Claim | | Correction / source |
|---|---|---|
| "70-75 °F sweet spot" | **S** | OkState: **75 °F optimum**. Add: keep air cooler than medium |
| "4-6 in, 2-3 nodes" | **S** | Confirmed for woody; **3-5 in** for herbaceous. Free addition: sterilize the blade between cuttings |
| "auxin suppresses buds" | **C** | See pruning row |
| "don't fertilize a cutting at all" | **C** | Wrong as an absolute. Very low while callusing, then **50-100 ppm N from root initiation**. NC State's safe home phrasing: medium should be "low in fertility," not zero |
| "rockwool holds the perfect ratio with no judgment calls" | **C** | **Reverse it.** Manufacturer documents a steep vertical gradient and names over-watering as the classic error. It requires free drainage, a level surface, and no standing water — three judgment calls the article's dome tray violates |
| Clonex "keeps a couple of years" | **U** | Manufacturer publishes storage **conditions** and deliberately no duration |
| Missing: pet toxicity | **S** | A pothos cutting in an open glass at counter height. **Highest-harm gap in either article** — one sentence + ASPCA link |
| Missing: patented cultivars | **S** | Taking cuttings **is** the excluded act, 20 years, no gift carve-out. Directly load-bearing on the closing call to action |
| Rooting-time table · "change water every 2-3 days" · "half die off in soil" · "water roots are hairless" · rosemary 20%→50% | **U** | §7. **Extension essentially does not cover water rooting** — that's why this half of the article sources at ~20% |

### growing-microgreens-indoors
| Claim | | Correction / source |
|---|---|---|
| "10-30 g per tray" | **C** | Use USU's per-variety rates. **⚠ The audit's own correction (200-400 g for sunflower) is itself wrong — USU says 48 g** |
| "dark 3-4 days" | **C** | Variety-specific, 1-2 d to 7-14 d. Give the table |
| "uncover at about an inch tall" | **U→rewrite** | USU's trigger is procedural: remove the weight when roots are pushing into the medium (~half the covered time), then invert the tray |
| Days-to-harvest rows | **C** | Radish 8-12 (not 7-10), pea 8-10 (not 10-14), sunflower 9-10, **split cilantro (21-28) from basil (12-16)**. Cut the beet/chard row |
| "harvest at 1-3 in" / "1-2 in" | **C** | Extension uses **first true leaves**, not height. Also fixes the internal contradiction |
| "keeps about a week" | **S** | Up to 14 d at 5 °C; store unwashed |
| "$1-2 of seed per tray" | **S** | **The only price on the site with a real citation** — USU publishes dated per-tray costs; radish $0.88 matches "maybe a dollar" |
| "no pest pressure worth mentioning" | **C** | Damping-off is the defining risk of a dense wet tray. Say so, then keep the fan advice |
| "the soil wicks up what it needs" | **C** | Add the pour-off: fill, wait 30 min, **discard what wasn't absorbed** |
| "a brick" | **S** | **The audit is wrong — universal weighting is correct.** Quantify: 2-5 lb, first half of blackout only, then invert |
| Implied food-safety | **C** | Add a short block; cite the real FDA recall rather than asserting safety |
| "soak peas and sunflower overnight" + economic reason for microgreen seed | **C** | Presoak is **pea 6 h, sunflower 12 h**. And the real reason is **fungicide-treated garden seed is labelled not for food or feed** |
| Startup equipment prices | **U** | §7 |

### starting-an-indoor-herb-garden
| Claim | | Correction / source |
|---|---|---|
| "6+ hours of strong sun" | **S→raise** | Iowa State: **about eight hours** of direct light indoors |
| "PPFD 200-400 for 14-16 h" | **C** | 200 × 14 = 10.1 mol/day; basil needs 15-25. Tighten to ~300-400 for 16 h |
| Two units never reconciled | **C** | Reconcile through DLI and link the site's own DLI calculator |
| Table's "Moderate / Low / High" undefined | **S** | Adopt UMN's numeric bands |
| "overwatering is the second most common killer" | **U** | No source ranks causes. Keep the sourceable half |
| "top inch dry" | **S** | Top **1-2 in** (CSU, ties to gnat suppression). **Basil is the exception** — never fully dry |
| "no feeding for the first couple of months" | **U** | Cut the window. Herbs need less fertilizer; feed spring-summer, not winter |
| "half strength every 2-4 weeks" | **S** | Broaden to "half or quarter"; add the seasonal restriction |
| Heat mat "10-20 °F" | **S** | Manufacturer spec, verified. **Must be fixed in the same pass as seed-starting** or the site ships a third version |
| "radiators dry the air to 30%" | **C** | Iowa State: **10-20%** in winter — the article understates it |
| "basil sulks below 55 °F" | **S** | Chilling-sensitive below ~50-54 °F; 55 °F is a defensible round number |
| Rosemary "easy, tolerates dry spells" | **C** | Iowa State puts it in the **harder** group (light + spider mites), and it wants to dry only *slightly*. **Contradicts the site's own propagation article, which rates it Hard** |
| "mint nearly impossible to kill" | **U→soften** | Cut the superlative — but **do not import the audit's spider-mite counter-claim**; Iowa State puts mint in the easy group |
| Miracle-Gro gnat claim | **C** | §4.6 |
| "overfed herbs… oils get diluted" | **C** | **Cut the mechanism.** §7 / §8 — this is the PR #11 shape |
| "$60-80 all-in" · AeroGarden · search-URL product claims | **U** | §7 |

### harvesting-and-drying-herbs
| Claim | | Correction / source |
|---|---|---|
| "oil peaks just before flowering" | **S/C** | Keep the **harvest recommendation** (two extension sources). **Cut "it peaks"** — peppermint and oregano peak at full bloom |
| "cut mid-morning" | **S→shift** | "Early morning, once the dew has dried." Cut the lighter-oils mechanism. Note basil specifically does better cut in the afternoon |
| "60-70 °F and 45-55% RH" for air drying | **C** | **Cut the spec.** No herb-drying publication states one, and 45-55% for two weeks works against the article's own mould warnings. Reads as an imported cannabis dry-room number |
| "one to two weeks" | **C** | **5-10 days**; tender-leaf herbs must dry fast or they mould |
| "dehydrator 95-105 °F, 2-6 h" | **C** | **90-100 °F, 1-3 h**, until leaves crumble |
| "ovens don't go below 170 °F" | **S→rewrite** | Conclusion right, appliance figure unsourceable. Extension: oven drying is **not recommended** |
| Microwave in 20-second bursts | **C** | Use the published protocol: ≤1-2 cups, single layer, **plain white — not recycled — paper towels (metal scraps can arc and catch fire)**, wattage-indexed times, stir every 30 s |
| Cilantro in olive oil, no keep-frozen note | **C** | ***C. botulinum*.** Switch to **water** ice cubes (NC State's own method), or state unmissably: keep frozen, never room temperature |
| "never take more than a third" | **C** | Wrong for annuals. **Annuals 50-75%, perennials ⅓**; NC State allows **75%** of the season's growth. Basil harder still |
| "past their best after about a year" | **S** | 6 months to 1 year; store **whole**, crush at use |
| "five to eight stems per bundle" | **U** | Sources say "small, loose bundles" — the requirement is airflow, not a count |
| "air drying preserves more than any heated method" | **C** | Not supportable, and the article contradicts itself later. Present as a **trade-off**: air for hardy, low-heat dehydrator for tender |

### best-vegetables-to-grow-indoors-year-round
| Claim | | Correction / source |
|---|---|---|
| "radishes in 25-30 days" | **S** | State as **3-5 weeks** from direct sowing |
| "peppers/tomatoes 2-3 months to first fruit" | **C** | Catalogue days are from **transplant**; pepper seed starts 8 weeks earlier. Give two columns or convert to from-seed and say so |
| Container table | **C** | Illinois: cherry/patio tomato **1 gallon**, standard 3 gallons, peppers 2 gal for 2 plants. Minimum depth 6-8 in |
| "dwarf tomatoes — 5 gallons, not negotiable" | **C** | Directly contradicted. 5 gal is the full-size figure. **Drop "not negotiable."** Note: no extension source names micro-dwarf cultivars — correct via Illinois' cherry/patio row, don't invent a micro-dwarf pot size |
| SF-4000 at 14-16 h | **C** | A 4x4 flowering fixture badly overshoots leafy-green DLI. Specify a DLI and a modest fixture; recompute cost at §2.1 |
| "Leafy greens — windowsill — 3-6 weeks" | **C** | A windowsill is not a lettuce light budget. Change the column to grow light, or drop the harvest promise |
| "pollen goes sterile above 90 °F" | **S** | Thresholds right, mechanism overstated — it's **flower drop**. Add the missing upper night bound (>70 °F) |
| "long carrots need 12+ in" | **S** | Better advice: grow **short types** in a 12-in-deep container |
| Electric toothbrush pollination | **S** | Real greenhouse practice (pollen vibrator). Attribute it; drop the anecdote as evidence |
| "inconsistent watering causes bitter lettuce" | **S** | Lettuce bitterness is **heat/bolting first**. Carrots and tomato splitting hold |
| **Missing: blossom end rot** | **S** | Total content gap on a page recommending container tomatoes. Get the causation right: it's **water movement, not soil calcium** — the fix is consistent deep watering and a big enough pot, **not** a calcium supplement |
| Microgreens row "no grow light needed" | **C** | Contradicts the site's own microgreens page and USU. ~1 in of medium + 18 h on a timer |
| "zucchini yields less than $2" · "scallions regrow indefinitely" · "seeds are heirloom" | **U** | §7 |

---

## 7. Claims that cannot be sourced — cut, or rewrite as honest ranges

I looked for each of these. Nothing authoritative exists. **Do not keep hunting; do not swap in a blog number.**

### 7.1 Every retail price on the site — **date-stamp or cut**
T5 fixtures, used HPS kits, replacement bulbs, timers ($12), the full tent cost table (7 rows), grow media (4 prices), DWC build ($135-195 itemised), meters, drip kits, ceramic stakes, herb startup ($60-80), microgreen equipment, five grocery houseplants ($40), "a good five-dollar option". No BLS series, no extension budget sheet, no USDA figure prices hobby growing equipment. Two acceptable treatments: **(a)** a visible "prices checked <month year>" line so they age visibly rather than silently, or **(b)** convert to ratios that don't decay ("the light is the single largest line; the tent is roughly a third"). **The one exception:** USU publishes dated per-tray microgreen seed costs — cite it and keep the date.

### 7.2 Market-share and motivation claims — **cut**
"Most tents include a removable floor tray" · "most decent tents include 2-3 duct ports" · "broader spectrum is the main reason growers switch to quantum boards" · "1000W-equivalent LEDs pull 100-150 W". Nobody surveys this category. Rewrite the tent ones as **shopping instructions** ("check the listing for a separate removable tray; count the duct ports — you need one high, one low, one for cables"). Replace the LED equivalence with **photon arithmetic**: 150 W at 2.5-2.8 µmol/J = 375-420 µmol/s against 1,751 µmol/s measured from a 1000 W DE HPS — about a quarter.

### 7.3 Invented intervals and thresholds — **replace with a trigger**
"Overnight rates cut cost by a third" (EIA publishes no TOU differential — rewrite as a conditional with no number) · pH drift ">0.5/day" · "change the water every 2-3 days" · "flush drip lines every few weeks" · "refill every 1-2 weeks" · "a week minimum for feeding changes, 2-3 weeks for light" (the only published timings argue this is too **short** — deficiency takes 2 weeks to appear, 4 for iron) · "recovery within a week or two" (keep the sound half: judge by the next flush of new growth; already-yellowed leaves will not re-green) · "self-watering stretches watering to a couple of weeks" · "12 inches of headroom above the tent" (derive it: fixture depth + ratchet hangers + duct elbow radius).

### 7.4 Fabricated percentages and quantities — **cut outright**
These are the exact shape of the failure the site has already publicly corrected:
- **"Half of a six-inch water root system dies off in soil."**
- **"My rosemary strike rate went from one in five to better than half"** — an anecdote positioned as product evidence next to an affiliate link.
- **"A zucchini plant fills a 4x4 tent to produce less than a $2 haul"** — rebuild the (correct) conclusion on footprint and DLI, both sourceable.
- **"A loaded pepper branch folds under four or five fruits."**
- **"Scallions can be regrown indefinitely"** — false, but no source quantifies the decline either; rewrite without a number.
- **"Water roots are hairless"** — the article refutes itself two sections later.
- **"Full sun is 100,000 lux; a windowsill gives 5,000-10,000"** — extension never works in lux. Use foot-candles or DLI.
- **"Coco brick expands several times"** — vendor sheets disagree by nearly 3×. Tell the reader to read the expanded volume printed on their brick.
- **"Rockwool starts at pH 7-8.5"** — only non-blog statement is behind MDPI's 403, and the manufacturer's own site says "pH-neutral". **Omit the number**; the conditioning target is already sourced.
- **"A ¼-inch sand layer"** — the practice is citable, the depth is not.
- **"Five to eight stems per bundle"** — the requirement is airflow.
- **"Go up two inches in pot diameter"** — nurseries and retailers only.
- **"Herbs in fresh mix don't need feeding for two months."**
- **"Overwatering is the second most common herb-killer"** — nobody ranks causes.
- **"Heated air drops humidity to 25-35%"** — publish the **target** (40-60%, injury under 20%) instead.
- **"The stub dies back a few millimetres"** / **"an untied plant reasserts a top within a week"** — keep as observation, never as measurement.

### 7.5 Mechanisms invented to explain a contested result — **delete the "because" clause**
The highest-risk category on the site, and the direct analogue of the VPD offset and the zinc description.
- **"Overfed herbs lose flavour because the aromatic oils get diluted."** The basil-N literature genuinely splits (N variously raises leaf oil concentration, lowers it at high rates, or changes nothing). Write the practice note with **no mechanism**: herbs need less fertilizer than other container plants, and fertilizing too often may dull aroma and taste.
- **"Coco binds calcium and magnesium."** Vendor mechanism; the real one is a supply-and-competition story.
- **"Getting the filter order backwards cuts filtration effectiveness."** The pressure-sign reason is real; the effectiveness claim is fabricated.
- **"A flowering stem has its hormones pointed the wrong way."** It's carbohydrate allocation.
- **"Auxin from the tip suppresses the buds below."** Needs one hedging clause.
- **"Fungus gnats breed in bark and compost."** It's moisture.

### 7.6 Legal and regulatory claims the site cannot cite — **cut**
"Azadirachtin is not approved for amateur use in parts of the EU." Product authorisation is a member-state decision that varies and changes. Replace with: "check your national pesticide regulator — neem/azadirachtin approvals differ outside the US."

### 7.7 Not a sourcing problem — a linking problem
**All 51 affiliate links are Amazon search URLs** (`/s?k=`, in 12 of 18 articles). "The seeds are heirloom and open-pollinated", "no batteries and a colour-coded reading", and every attached price describe whatever the query returns today. Either link a specific ASIN and verify the claim against that listing, or state the claim generically about the instrument category and drop the specifics. No amount of sourcing fixes this.

---

## 8. Where the literature genuinely disagrees — hedge, don't pick a winner

1. **Lettuce photoperiod.** Home/extension guidance (UMN) says 12-14 h; CEA research and commercial practice run 16-24 h — Cornell uses 24 h for seedlings, and Jeong et al. found 24 h highest-yielding with no disorders at constant DLI. **This is the one place in this subject where popular internet consensus (16-18 h) is closer to the research than the extension fact sheet.** The extension number is a conservative home-scale convention, not a physiological ceiling.
2. **Bolting causation.** Blogs blame long days. Extension is explicit that **temperature dominates** (>80 °F for multiple days, day-count mattering more than severity). Spinach is a genuine obligate long-day bolter at 13-14 h — but even there, moderate temperature prevents it. **Do not bundle lettuce and spinach in one table row.**
3. **Reservoir temperature and change frequency.** e-GRO says 68-75 °F; OkState says 72-75 °F; Cornell actively **heats** to 75 °F; UF allows 65-80 °F. On change frequency, UNH says months-to-years by system type while **OkState says replace completely every two weeks** — which partially rehabilitates the article's current claim. Present both with their system context.
4. **The "no buffer in hydro" question.** UMass says alkalinity **is** the buffer; **OkState says the buffer "is absent in soilless culture."** Both are extension. Best synthesis: the buffer is whatever alkalinity the fill water carried in — RO swings hard, hard tap water resists your pH-down and then climbs back.
5. **Hydroponic pH.** OSU 5.5-6.5 · Cornell 5.6-6.0 (lettuce) · UF 6.0-7.0 (lettuce) · OkState 5.5-6.0 solution / 6.0-6.5 root zone · UNH 5.5-7.0 at home. Four bands from five sources. Don't present one as settled.
6. **Soilless optimum pH.** Lucas & Davis 5.0-5.8 · Peterson 5.2-5.5 · Purdue 5.4-6.2 · e-GRO 5.8-6.2. A real spread that varies by substrate and crop — and Altland's own data did **not** reproduce the classic P-availability drop below 5.5 in bark. Publish a range with the source named.
7. **Modern single-ended HPS efficacy.** The audit asserts 1.2-1.5 µmol/J for a 600 W SE. **Unsourceable.** The only measured SE figures are ~1.0 (magnetic mogul-base). Cite the measured 1.0 and 1.7 with their fixture classes and **do not invent a 600 W SE number** — that is exactly the fabrication shape the site already has.
8. **Fungus gnat life cycle.** UC IPM ~17 days at 75 °F vs CSU "about five weeks." Both current extension. Give the range with temperature.
9. **Seed viability.** Illinois vs Iowa State differ materially on spinach (3 vs 5) and broccoli (3 vs 5). Build the table from **one** named source and put it in the caption.
10. **Germination-test threshold.** Illinois discards at ≤6/10; Iowa State at ≤50%. Both far stricter than the article.
11. **Topping peppers.** Illinois Extension recommends it at 12 in; trial results on total yield are mixed by cultivar and season.
12. **Coir sustainability.** Genuinely contested; neither peat nor coir is cleanly ahead. The available source supports only the **transport and deforestation** halves — not water use in salt-washing, and not labour.
13. **Houseplant temperature.** UGA 58-86 °F tolerance vs CSU's three-category scheme. Differently framed rather than contradictory — pick one and attribute it.

**One place extension flatly contradicts near-universal internet advice, and extension is right:** Utah State on basil — *"Pinching off the flowers as they form does not stimulate new foliage; in fact it encourages flowers to form in the axils of the leaves thus reducing the yield of the plant."* If the site wants a demonstrable "we checked and the internet is wrong" moment, this is the cheapest one available.

---

## 9. Audit hygiene — read before budgeting

**9.1 One audit entry is a phantom.** The VPD paragraph ("75 °F at 80% humidity is a sluggish 0.59 kPa while 85 °F at the same 80% is a working 0.82 kPa") **does not exist in the repo.** Independently verified: zero hits site-wide for `vpd`, `kpa`, `vapor pressure`, or `0.59` across all 18 articles. Item 4 of `common-indoor-gardening-mistakes` contains only the 65-80 °F band and a hygrometer recommendation. Either the audit ran against an uncommitted draft, or this is residue from the PR #11 leaf-offset retraction that was never cleared. **Check whether other audit entries are similarly stale before budgeting rewrite time against the 136/102 counts.**

**9.2 The audit's own corrections contain at least two new fabrications.** In microgreens it proposes 200-400 g of sunflower seed per 1020 tray (USU publishes **48 g**) and states that blackout weighting is normally skipped for radish and brassicas (USU prescribes 2-5 lb for **every** variety). An agent rewriting from the audit alone would ship two fresh errors into an article being corrected for exactly that. **Gate the rewrite on §5-§6 of this document, not on the audit's proposed corrections.**

**9.3 The audit is wrong in at least one place where the article is right.** It flags "an assembled 4x4 does not fit through a standard door" as an overstated absolute. It isn't — a 48-inch rigid frame cannot pass a 32-inch opening in any orientation, and IRC R311.2 sets 32 in as the minimum for the *egress* door while exempting interior doors from even that. **Do not soften that sentence.**

**9.4 Two problems are arithmetic, not sourcing, and should be fixed first** because they cost nothing and block nothing: the 40%-vs-50% FAQ/body split on 16→24 h (24/16 = 1.5), and "the meters are two-thirds of that" when the article's own list makes them 37-51%.

**9.5 If a fix touches a number that appears in more than one article, do all of them in the same pass.** Known multi-article numbers: the electricity rate (3 articles), the heat-mat temperature rise (2, currently inconsistent), "12-18 months" (2, different components), the Miracle-Gro gnat mechanism (3), "clip fan" positions (5), rosemary's difficulty rating (2, currently contradictory), and 70% isopropyl (2, consistent — consolidate rather than fix).