# Article sharing implementation

User approved the previously proposed sharing controls by asking to implement them on 2026-10-30. This change adds the controls; social preview artwork remains a separate task.

Use one shared Liquid include after the article body. Both instances share the canonical public URL of the current language, independent of localhost, query strings or heading fragments. Add Copy link, WhatsApp, Facebook, LinkedIn, X and the native device Share action where available. Localize all interface text. Social links work without JavaScript; JavaScript enables copy/native actions. When clipboard access fails, show a selectable link with clear instructions. Dismissing the native share dialog is silent. No automatic posting, third-party scripts or tracking.

- [x] Add failing generated-HTML tests for all ten articles' bottom sharing controls and language-specific destinations.
- [x] Implement the include, labels, responsive styles and isolated share script.
- [x] Build and run all tests. Verify mobile layout, copy feedback, fallback and native-share behavior; review the diff.
Delivery: commit and push `feat/article-sharing`, then create a PR against master.

Verification: Jekyll build, nine generated-HTML tests and six Node behavior tests pass. Mobile browser checks confirmed Sinhala/English copy URLs, localized success messages, and no horizontal overflow at 320px and 393px. Independent review found no actionable issues.

User refinement: keep sharing controls only at the bottom of each article.
