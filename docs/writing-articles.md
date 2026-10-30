# Writing articles for Wizard Lab

Articles are plain Markdown files in `_articles/`. GitHub Pages builds them automatically when you push to `master`; there is no server and nothing to deploy.

## Add an article

1. Create a file under the folder for its series, for example `_articles/ai-engineering/01-what-is-an-llm.md`.
   The file path becomes the URL: `tharuka.xyz/learn/ai-engineering/01-what-is-an-llm/`.
2. Start it with this front matter:

```markdown
---
title: "What is an LLM, really?"
description: One or two sentences shown on cards and in search results.
series: ai-engineering        # an id from _data/series.yml
part: 1                       # order inside the series
date: 2026-11-05
level: Beginner               # optional
tags: [llm, fundamentals]     # optional
cover: /images/learn/what-is-an-llm.jpg   # optional cover shown on the page
cover_alt: Short description of the cover
image:                        # link preview for WhatsApp, LinkedIn, X... (see below)
  path: /images/og/what-is-an-llm.jpg
  width: 1200
  height: 630
  alt: Short description of the cover
locale: si_LK                 # only for Sinhala articles (with lang: si)
---

Intro paragraph...

## First section

Body text, code, images...
```

3. Commit and push. The article appears on the hub home page, its series page, the "All articles" list, the RSS feed, and in "Latest" on tharuka.xyz.

## What you can use in an article

- `##` and `###` headings. They build the "On this page" sidebar automatically.
- Fenced code blocks with a language (```` ```python ````). They get syntax highlighting and a copy button.
- `> **Tip:** ...` blockquotes render as callouts.
- Tables, lists, links and images (GitHub-flavoured Markdown).
- Images: put them in `images/learn/<series>/` and reference them as `![Alt text](/images/learn/ai-engineering/diagram.png)`.

## Link previews and SEO

Titles, descriptions, canonical URLs, the sitemap and structured data are generated for you from the front matter, so a good `title` and `description` is all an article needs for search.

When a link is shared (WhatsApp, LinkedIn, X, Facebook), the preview uses the article's `image`. Make it from the cover so it is 1200x630 and small enough for WhatsApp:

```bash
python3 tools/make_og_covers.py images/learn/what-is-an-llm.jpg   # writes images/og/what-is-an-llm.jpg
```

Without an `image`, the article falls back to the Wizard Lab preview. After publishing, you can check a link with [opengraph.xyz](https://www.opengraph.xyz/) or LinkedIn's [Post Inspector](https://www.linkedin.com/post-inspector/). WhatsApp caches previews, so an old preview can stick for a while.

## Add a new series

1. Add an entry to `_data/series.yml` (id, title, short, level, colour, description, topics).
2. Copy `learn/series/ai-engineering.md` to `learn/series/<new-id>.md` and change `series_id`, `permalink`, `title` and `description` (the description is what search results and link previews show).

## Preview locally (optional)

```bash
gem install jekyll kramdown-parser-gfm jekyll-seo-tag jekyll-feed jekyll-sitemap
jekyll serve
# open http://localhost:4000/learn/
```

## Rename the hub

Change `learn.name` and `learn.tagline` in `_config.yml`.
