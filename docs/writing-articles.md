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
lang: en                     # en or si; required for language-specific lists
translation_key: ai-engineering-what-is-an-llm  # same key on both translations
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

3. Commit and push. The article appears on its language's hub home page, series page and "All articles" list, and in the shared RSS feed. The portfolio's "Latest" section lists the original Sinhala articles once.

## Add an English translation

Keep the Sinhala article at its existing path. Add its translation under `_articles/en/<series>/<slug>.md` with `lang: en`, `locale: en_US` and an explicit `permalink: /learn/en/<series>/<slug>/`. Use the same `translation_key`, `series`, `part` and original publication date in both versions. Use a different `title`, `description`, body, `cover` and social-preview `image` for each language as needed. Existing Sinhala URLs and images stay unchanged.

The language control matches `translation_key`; it only appears when a counterpart exists. Lists and previous/next links filter on `lang`, so translations do not double the series part count. Hub pages live at `/learn/` (Sinhala) and `/learn/en/` (English). Links determine the selected language, without browser-storage preferences or automatic redirects.

For translated hub or series pages, also share a `translation_key` across their front matter. Keep page titles/descriptions localized for search and social metadata. UI strings live in `_data/learn_ui.yml`; Sinhala series titles, descriptions and levels live under each series's `translations.si` in `_data/series.yml`.

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
3. Add the English page under `learn/en/series/` with its English permalink, `lang: en`, `locale: en_US` and matching `translation_key`.
4. Optionally set `cover` and `cover_alt` in the series data to show artwork on the series card and section page. Add its 1200×630 preview to both series pages' `image` front matter.

## Preview locally (optional)

```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000/learn/
```

Use a current Ruby (3.2 or later) for the local preview dependencies. To check language links, five-part navigation and image paths after changes:

```bash
bundle exec jekyll build
python3 tools/test_bilingual.py
```

## Rename the hub

Change `learn.name` and `learn.tagline` in `_config.yml`.
