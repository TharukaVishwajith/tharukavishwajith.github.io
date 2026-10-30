# Putting the learning hub on learn.tharuka.xyz

## How GitHub Pages handles domains

A GitHub Pages site gets exactly one custom domain per repository. This repository already owns `tharuka.xyz` (see `CNAME`), so `learn.tharuka.xyz` has to be served by a **second repository**. Both stay free and static; no server is needed.

## Recommended path

**Phase 1 (this PR): ship at `tharuka.xyz/learn/`.** It works the moment this PR merges, with no DNS changes, and you can start publishing articles straight away.

**Phase 2: move to `learn.tharuka.xyz` when you're ready.** About 15 minutes of work:

1. **Create the repository.** On GitHub, create a new public repository, e.g. `TharukaVishwajith/learn`. Leave it empty.
2. **Move the hub into it.** Copy these from this repo: `_articles/`, `_data/series.yml`, `_includes/`, `_layouts/learn.html`, `_layouts/series.html`, `_layouts/article.html`, `assets/`, `learn/` (its contents become the site root), `images/profile.jpg`, `images/favicon.ico`, `_config.yml`, `404.html`.
   In the new repo's `_config.yml` set `url: "https://learn.tharuka.xyz"`, and change the article permalink from `/learn/:path/` to `/:path/` (and the `/learn/...` links in the layouts to `/...`).
   Claude can do this move for you once the empty repo exists.
3. **Add a CNAME file** in the new repo containing exactly one line: `learn.tharuka.xyz`.
4. **Turn on Pages.** In the new repo: Settings → Pages → Build and deployment → Source: "Deploy from a branch", branch `main`, folder `/ (root)`. Under "Custom domain" enter `learn.tharuka.xyz` and save.
5. **Add the DNS record** at your domain registrar / DNS provider for `tharuka.xyz`:

   | Type  | Name / Host | Value / Target                 | TTL  |
   |-------|-------------|--------------------------------|------|
   | CNAME | `learn`     | `tharukavishwajith.github.io.` | Auto / 3600 |

   Point it at `tharukavishwajith.github.io` (your user Pages host), **not** at the repository name. Do not touch the existing apex (`@`) records for `tharuka.xyz`.
6. **Wait and enable HTTPS.** DNS usually propagates in minutes, sometimes up to 24 hours. Once GitHub's DNS check passes, tick "Enforce HTTPS" on the Pages settings page (the certificate can take up to an hour to issue).
   Check from a terminal: `dig learn.tharuka.xyz +short` should print `tharukavishwajith.github.io.` followed by GitHub IPs.
7. **Point the main site at it.** In this repo's `_config.yml`, set `learn.url: "https://learn.tharuka.xyz/"`. Every "Wizard Lab" link on tharuka.xyz updates.
8. **Keep old links working.** Replace this repo's `learn/index.html` with a small redirect page (`<meta http-equiv="refresh" content="0; url=https://learn.tharuka.xyz/">`), then delete the hub files from this repo.

## Recommended: verify the domain with GitHub

GitHub account Settings → Pages → "Add a domain" → `tharuka.xyz`. Add the TXT record it shows. This stops anyone else from claiming `*.tharuka.xyz` on GitHub Pages, which matters once you add subdomains.

## Later: moving to a server

Because articles are plain Markdown with front matter, they move as-is to Astro, Next.js, Hugo, or a headless CMS if you outgrow GitHub Pages.
