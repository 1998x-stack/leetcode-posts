# Browser QA protocol

Use real Chromium/Playwright. Static HTML parsing is necessary but not sufficient. Save machine-readable reports and screenshots.

## Required viewports

| View | Required checks |
|---|---|
| 1440 × 900 | Article/sidebar proportions, legible SVG, no unexpected overflow |
| 768 × 1024 | TOC and article stack correctly, no overlap |
| 390 × 844 | Text, code, figures and controls fit; no page-level horizontal scroll |
| 360 × 800 | Narrow labels and long identifiers remain readable |

Also test print emulation and local/offline behavior.

## Semantic and asset checks

- Exactly one H1; main landmark, named navigation and logical heading hierarchy.
- Every figure has an image/SVG and nonempty figcaption.
- Every image has an intentional alt value (empty alt only for truly decorative images).
- Local images decode and have nonzero geometry; SVGs have title/desc/viewBox and no clipped labels.
- Internal anchors resolve; official problem links are visible and open safely.
- No missing local scripts/styles, remote font dependency or unexpected network request.

## Interaction checks

- Tab through all controls and confirm visible focus.
- Check previous/next boundary disabled state and keyboard navigation.
- Click at least two states and assert meaningful content changes.
- Confirm aria-live text changes and no pageerror/console error is emitted.
- Check reduced-motion behavior and ensure there is no autoplay.

## Layout and print checks

- document.documentElement.scrollWidth must not exceed innerWidth (within 1px).
- Horizontal scrolling belongs only inside a named code/math region.
- Emulate print: hide controls and sticky navigation, keep key figures/captions and code readable, avoid blank figure pages.
- Check images after decode; lazy images must be forced to load before declaring them broken.

## Evidence and failure policy

Capture desktop/tablet/mobile/narrow-mobile screenshots and a JSON report. A failed or skipped check is not a pass. Fix the article or report a genuine infrastructure issue. Never weaken the check globally to suppress one article's failure.

Command:
python skills/olah-style-leetcode-posts/scripts/browser_check.py posts/category/slug/index.html --output reports/slug

The final task report must distinguish static validation, Python tests, browser checks, PDF validation and actual Pages deployment.
