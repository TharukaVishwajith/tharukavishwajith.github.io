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

## Add a new series

1. Add an entry to `_data/series.yml` (id, title, short, level, colour, description, topics).
2. Copy `learn/series/ai-engineering.md` to `learn/series/<new-id>.md` and change `series_id`, `permalink` and `title`.

## Preview locally (optional)

```bash
gem install jekyll kramdown-parser-gfm jekyll-seo-tag jekyll-feed
jekyll serve
# open http://localhost:4000/learn/
```

## Rename the hub

Change `learn.name` and `learn.tagline` in `_config.yml`.
