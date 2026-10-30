# Bilingual Wizard Lab Implementation Plan

> Execute inline using executing-plans, with tests against generated Jekyll pages.

**Goal:** Read all five AI Native Development articles in Sinhala or English and switch languages without losing the article.

**Architecture:** Shared Jekyll layouts render language-specific pages and collections. Translation keys pair equivalent pages; `lang` filters lists and pagers. Explicit English routes preserve current Sinhala URLs.

**Tech Stack:** GitHub Pages compatible Jekyll, Liquid, YAML, Markdown, existing CSS, Python unittest for generated HTML checks.

## Global constraints

- Preserve existing Sinhala bodies, covers and URLs.
- Use all four supplied English covers, reuse the Meat Proxy cover, add one new series image.
- No JavaScript requirement for language selection; no new runtime dependency on the deployed site.

## Tasks

- [x] Establish a real local Jekyll build and add failing generated-HTML tests for paired language links, five-part lists, same-language pagers and alternate metadata (`tools/test_bilingual.py`).
- [x] Add `_data/learn_ui.yml`, `_includes/language-switch.html`, `_includes/language-alternates.html` and shared learning-home/library includes. Update learning layouts to filter by language and use localized labels. Add English hub, library and series routes with matching translation keys.
- [x] Translate all five Markdown articles into `_articles/en/ai-native-development/`, preserving meaning and examples. Add translation keys to originals. Copy English covers without altering supplied assets and build preview derivatives. Add series artwork and metadata to `_data/series.yml`.
- [x] Prevent duplicate translations in the portfolio's latest section. Document translation keys, language routes and the section-image prompt.
- [x] Build with Jekyll and run `python3 tools/test_bilingual.py`. Inspect desktop/mobile pages, language links and library search in a browser, then review the complete diff and report the local result.

## Verification

Jekyll 3.10 build passes. Seven generated-HTML tests pass, covering all five translation pairs, reciprocal hub/library/series links, list counts, same-language pagers, local assets, English covers, series artwork and portfolio deduplication. Browser checks at 375px and 1440px verified layout, same-article language switching, library search and its empty state. Independent review found English metadata on Sinhala series pages; titles and descriptions were localized before final verification.
