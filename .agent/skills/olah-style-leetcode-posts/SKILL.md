---
name: olah-style-leetcode-posts
description: Convert LeetCode problems into rigorous, readable Chinese HTML explainers with original SVG diagrams, interactive state traces, correctness invariants, runnable Python tests and GitHub Pages publication.
---
# LeetCode Algorithm Explainer Skill

Adapted from xm-posts' editorial and visual production system. Audience: undergraduate/graduate students and interview learners. Outputs are independently written; no wholesale copying of LeetCode statements or third-party diagrams.

## Mandatory workflow
1. Read AGENTS.md, README.md, the taxonomy, publishing manifest, existing posts and design assets.
2. Verify the official LeetCode title, number, difficulty, I/O and relevant constraints; summarize the prompt in original words. Put provenance in evidence.json. Do not invent metrics or reproduce full copyrighted statement.
3. Design the progression: concrete example → naive baseline → invariant → state transitions → correctness argument → complexity with output/stack assumptions → Python code → edge-case tests.
4. Draw at least three original, accessible, self-standing SVG figures: mechanism cover, trace and counterexample. Use viewBox, title/description, clear labels, accurate colors, and 360px legibility. Avoid generic/shared thumbnails.
5. Add a keyboard-accessible step-through demonstration with meaningful static default. No-JS reading remains useful.
6. Write LeetCode-compatible class Solution Python method in solution.py with no external dependencies. Tests cover standard, duplicate, edge, no-solution and invariant cases. Be clear whether input mutates.
7. Use a semantic standalone HTML article: exactly one H1, main, nav, figure captions, focus-visible, reduced-motion, mobile and print. Use math semantics when needed, not decorative symbols.
8. Validate: python scripts/sync_skills.py --check; python -m pytest -q; python scripts/build_site.py; python scripts/validate_site.py; python scripts/browser_check_all.py. Inspect actual 1440/768/390/360px rendering, overflow and interaction. Never claim skipped tests passed.
9. Publish by PR, check CI, merge to main, then verify GitHub Pages and public URL. Drafts never go live.

## Artifact contract
posts/<category>/<slug>/index.html; assets/cover.svg, assets/trace.svg, assets/pitfall.svg; solution.py; evidence.json; tests/test_<slug>.py. Register a real LeetCode problem_url in content/posts.json with a unique explained cover.caption and published or draft status.

## Critical correctness
- Sliding window: define valid state and monotone left bound.
- Two pointers: justify why removing the chosen candidate cannot miss optimum.
- Sorted 3Sum: justify both deduplication loops.
- Backtracking: choice, recursion, undo, and why results require a copy.
- Grid traversal: adjacency, visited marking, connected components, mutation behavior.
- State worst-case time/extra space/output space separately; distinguish an illustrative trace from complete execution.

## Reference routing
problem-analysis.md, narrative-architecture.md, evidence-and-citation.md, html-design-system.md, svg-production.md, implementation-and-interactivity.md, browser-qa.md, publishing.md, math-typesetting.md.
