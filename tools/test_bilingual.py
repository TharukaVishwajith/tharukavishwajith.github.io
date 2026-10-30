"""Check the reader-visible contract after `bundle exec jekyll build`.

Run from the repository root: python3 tools/test_bilingual.py
"""
import unittest
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

SITE = Path("_site")
SLUGS = ["meat-proxy", "disposable-software", "ai-harness-engineering", "doom-loop", "review-tax"]


class Page(HTMLParser):
    def __init__(self, url):
        super().__init__()
        self.tags = []
        path = SITE / url.strip("/") / "index.html"
        self.source = path.read_text()
        self.feed(self.source)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def attrs(self, tag, **match):
        return [attrs for name, attrs in self.tags if name == tag and all(attrs.get(k) == v for k, v in match.items())]


class BilingualPages(unittest.TestCase):
    def test_stylesheet_urls_expire_with_each_build(self):
        for url in ["/", "/learn/", "/learn/series/ai-native-development/", "/learn/en/ai-native-development/doom-loop/"]:
            with self.subTest(url=url):
                styles = Page(url).attrs("link", rel="stylesheet")
                local = [urlsplit(s["href"]) for s in styles if s["href"].startswith("/assets/css/")]
                self.assertTrue(local)
                for style in local:
                    self.assertTrue(parse_qs(style.query).get("v"), f"{url}: {style.path} can reuse stale CSS")

    def test_all_five_articles_have_reciprocal_language_links(self):
        for slug in SLUGS:
            for lang, prefix, other_lang, other_prefix in [("si", "/learn/", "en", "/learn/en/"), ("en", "/learn/en/", "si", "/learn/")]:
                with self.subTest(slug=slug, lang=lang):
                    page = Page(prefix + "ai-native-development/" + slug + "/")
                    self.assertTrue(page.attrs("html", lang=lang))
                    target = other_prefix + "ai-native-development/" + slug + "/"
                    self.assertTrue(page.attrs("a", hreflang=other_lang, href=target))
                    self.assertTrue(page.attrs("a", hreflang=lang, **{"aria-current": "page"}))
                    self.assertTrue(page.attrs("link", rel="alternate", hreflang=other_lang, href="https://tharuka.xyz" + target))
                    self.assertTrue(page.attrs("link", rel="canonical", href="https://tharuka.xyz" + prefix + "ai-native-development/" + slug + "/"))

    def test_lists_show_five_parts_in_the_selected_language(self):
        for lang, prefix in [("si", "/learn/"), ("en", "/learn/en/")]:
            for suffix in ["", "articles/", "series/ai-native-development/"]:
                with self.subTest(lang=lang, suffix=suffix):
                    page = Page(prefix + suffix)
                    articles = [a["href"] for a in page.attrs("a") if re.match(r"^/learn/(?:en/)?ai-native-development/", a.get("href", ""))]
                    self.assertEqual(len(articles), 5)
                    self.assertEqual(len(set(articles)), 5)
                    self.assertTrue(all(url.startswith(prefix + "ai-native-development/") for url in articles))
                    self.assertNotIn("Part 6", page.source)

    def test_pagers_stay_in_language_and_do_not_count_translations(self):
        for prefix in ["/learn/", "/learn/en/"]:
            for i, slug in enumerate(SLUGS):
                with self.subTest(prefix=prefix, slug=slug):
                    page = Page(prefix + "ai-native-development/" + slug + "/")
                    if prefix == "/learn/en/":
                        self.assertIn(f"Part {i + 1} of 5", page.source)
                    prev = page.attrs("a", **{"class": "pager-prev"})
                    next_ = page.attrs("a", **{"class": "pager-next"})
                    self.assertEqual([a["href"] for a in prev], [prefix + "ai-native-development/" + SLUGS[i - 1] + "/"] if i else [])
                    self.assertEqual([a["href"] for a in next_], [prefix + "ai-native-development/" + SLUGS[i + 1] + "/"] if i < 4 else [])

    def test_local_learning_links_and_images_resolve(self):
        for path in (SITE / "learn").rglob("*.html"):
            page = Page("/" + str(path.parent.relative_to(SITE)) + "/")
            for tag, attrs in page.tags:
                url = attrs.get("src") if tag == "img" else attrs.get("href") if tag == "a" else None
                if not url or not url.startswith("/") or url.startswith("//"):
                    continue
                target = SITE / url.split("#")[0].lstrip("/")
                if url.split("#")[0].endswith("/"):
                    target /= "index.html"
                self.assertTrue(target.exists(), f"{path}: missing {url}")

    def test_english_covers_and_series_artwork(self):
        for slug, cover in [("disposable-software", "disposable-software-en.png"), ("ai-harness-engineering", "ai-harness-en.png"), ("doom-loop", "doom-loop-en.png"), ("review-tax", "review-tax-en.png")]:
            page = Page("/learn/en/ai-native-development/" + slug + "/")
            self.assertTrue(page.attrs("img", src="/images/learn/" + cover))
        for prefix in ["/learn/", "/learn/en/"]:
            for suffix in ["", "series/ai-native-development/"]:
                self.assertTrue(Page(prefix + suffix).attrs("img", src="/images/learn/ai-native-development.jpg"))

    def test_hub_library_and_series_language_links_are_reciprocal(self):
        for suffix in ["", "articles/", "series/ai-native-development/", "series/ai-engineering/", "series/data-engineering/"]:
            for prefix, other_prefix, other_lang in [("/learn/", "/learn/en/", "en"), ("/learn/en/", "/learn/", "si")]:
                with self.subTest(prefix=prefix, suffix=suffix):
                    self.assertTrue(Page(prefix + suffix).attrs("a", hreflang=other_lang, href=other_prefix + suffix))

    def test_portfolio_latest_does_not_duplicate_translations(self):
        page = Page("/")
        articles = [a["href"] for a in page.attrs("a") if re.match(r"^/learn/(?:en/)?ai-native-development/", a.get("href", ""))]
        self.assertEqual(len(articles), 3)
        self.assertTrue(all(url.startswith("/learn/ai-native-development/") for url in articles))


if __name__ == "__main__":
    unittest.main()
