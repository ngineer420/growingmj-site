# Deploying growingmj.com

This repo is served by GitHub Pages. Pages has already been enabled for
this repo (source: `main` branch, root `/`), and a `CNAME` file in the
repo root already tells GitHub Pages the custom domain is `growingmj.com`.
The only remaining step is pointing your domain's DNS at GitHub.

## 1. DNS records to add at your domain registrar

Log into wherever `growingmj.com` is registered (GoDaddy, Namecheap,
Cloudflare, Google Domains, etc.) and open its DNS management page. Add
the following records:

### Apex domain (`growingmj.com`, no `www`) — required

Add four **A** records, all on the root/apex (`@`), pointing to GitHub
Pages' IP addresses:

| Type | Host | Value |
|------|------|-------|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

Optional but recommended — IPv6 (**AAAA**) records for the same apex:

| Type | Host | Value |
|------|------|-------|
| AAAA | @ | 2606:50c0:8000::153 |
| AAAA | @ | 2606:50c0:8001::153 |
| AAAA | @ | 2606:50c0:8002::153 |
| AAAA | @ | 2606:50c0:8003::153 |

### `www` subdomain — optional, recommended

If you also want `www.growingmj.com` to work (it will automatically
redirect to the apex domain once GitHub verifies the custom domain), add:

| Type | Host | Value |
|------|------|-------|
| CNAME | www | ngineer420.github.io |

### Notes

- Some registrars use `@` to mean "the root domain" in the host/name
  field; others want it left blank. Use whichever convention your
  registrar's UI expects for a root-domain record.
- DNS changes can take anywhere from a few minutes to 24-48 hours to
  propagate fully, depending on your registrar and previous TTL settings.
- Do not also add a CNAME record on the apex (`@`) — apex domains must use
  A/AAAA records, not CNAME. Only the `www` subdomain (or another
  subdomain) can use a CNAME.

## 2. Verify Pages picks up the domain

Once DNS has propagated:

1. Go to the repo on GitHub → **Settings → Pages**.
2. Confirm **Custom domain** shows `growingmj.com` with a green checkmark
   (not a DNS warning).
3. Once verified, GitHub Pages will offer a checkbox for **Enforce
   HTTPS** — enable it. It may take a little while to become available
   right after DNS verifies while GitHub provisions the TLS certificate.
4. Visit `https://growingmj.com` and confirm the homepage loads over
   HTTPS with a valid certificate.

## 3. Applying for Amazon Associates

Amazon requires a site to already have real, live content before
approving an Associates application — this repo is built specifically to
satisfy that (six full articles, About/Privacy/Disclosure pages, a real
domain). Once `https://growingmj.com` is live and working end to end:

1. Go to [affiliate-program.amazon.com](https://affiliate-program.amazon.com/)
   and apply, using `growingmj.com` as your website.
2. Fill out the application with your real name/tax/payment details (this
   step has to be done by you personally — it's not something that can be
   automated or done on your behalf).
3. Amazon typically asks you to make a small number of qualifying sales
   within 180 days of approval to keep the account active, so it can help
   to share a couple of article links once you're approved.
4. Once approved, Amazon gives you a **tracking ID** (looks like
   `growingmj-20`).
5. Follow the "Once you're approved for Amazon Associates" section in
   `README.md`: set that tracking ID in `data/affiliate-links.json` (or
   pass it as an argument), then run:
   ```bash
   python3 scripts/apply_affiliate_links.py growingmj-20
   ```
   This rewrites every `[[AFFILIATE:id]]` placeholder across every article
   into a real, tagged Amazon link in a single pass. Commit and push the
   result.

## 4. Ongoing maintenance

- Add new articles as plain `.html` files under `articles/`, following the
  existing header/footer/disclosure-banner structure in any current
  article for consistency.
- Add new product links to `data/affiliate-links.json` first, then
  reference them from articles with `href="[[AFFILIATE:your-id]]"`.
- Update `sitemap.xml` when you add new pages.
- Remember: no cannabis-specific content — this site is scoped to general
  indoor/home gardening (see the "Content policy" section in `README.md`).
