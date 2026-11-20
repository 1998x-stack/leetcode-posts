---
name: olah-style-leetcode-posts
description: Convert LeetCode problems into rigorous, readable Chinese HTML explainers with original SVG diagrams, interactive state traces, correctness invariants, runnable Python tests and GitHub Pages publication.
---
# LeetCode Algorithm Explainer Skill

Adapted from xm-posts' editorial and visual production system. Audience: undergraduate/graduate students and interview learners. Outputs are independently written; no wholesale copying of LeetCode statements or third-party diagrams.

## Mandatory workflow
1. Read AGENTS.md, README.md, docs/taxonomy.md, docs/foundations.md, content/domains.json, content/categories.json, content/facets.json, publishing manifest, existing posts and design assets.
2. Verify the official LeetCode title, number, difficulty, I/O and relevant constraints; summarize without copying the full prompt. Put provenance in evidence.json. Do not invent metrics.
3. Design the progression: concrete example → naive baseline → invariant → state transitions → correctness argument → complexity with output/stack assumptions → Python code → edge-case tests.
4. Draw at least three original, accessible, self-standing SVG figures: mechanism cover, trace and counterexample. Use viewBox, title/description, unique IDs, clear labels, accurate colors, and 360px legibility.
5. Add a keyboard-accessible step-through demonstration with meaningful static default. No-JS reading remains useful.
6. Write LeetCode-compatible Python solution.py with no external dependencies. Tests cover standard, duplicate, edge, no-solution and invariant cases. Be clear whether input mutates.
7. Use semantic standalone HTML: exactly one H1, main, nav, figure captions, focus-visible, reduced-motion, mobile and print. MathML is optional; if used, follow math-typesetting.md.
8. Validate: sync skill mirrors; run pytest, build, site validation, SVG audit and browser_check_all.py. Inspect actual 1440/768/390/360px rendering, overflow and interaction. Never claim skipped tests passed.
9. Publish by PR, check CI, merge to main, then verify GitHub Pages and public URL.

## Artifact contract
posts/<category>/<slug>/index.html; assets/cover.svg, assets/trace.svg, assets/pitfall.svg; solution.py; evidence.json; deterministic tests. Register an official problem_url in content/posts.json with a unique explained cover.caption and published or draft status.

## Taxonomy and knowledge links
- Give every published post exactly one primary category and one L3 topic. Preserve existing slugs and article URLs.
- Populate all six controlled facet fields using only content/facets.json values.
- Treat domains as knowledge navigation, categories as algorithm families, topics as reusable problem patterns, and learning paths as ordered prerequisite journeys. Never create a category solely for one problem.

## Foundational algorithm coverage
- Arrays & hashing: distinguish set membership from key-to-index maps; explain scanned-prefix invariants, check-before-insert for Two Sum, expected hash complexity, prefix/suffix decomposition, zero handling, input mutation and output-space accounting.
- Binary search: declare closed [left, right] or half-open [lo, hi) intervals before code; align loop condition and updates; state the invariant and prove each discarded half; distinguish exact search, lower bound, upper bound and rotated-array uniqueness assumptions.
- Binary trees: define recursive return semantics and the empty-tree base case; explain preorder/inorder/postorder roles; snapshot BFS queue length per level; distinguish node-count height from edge-count path diameter; include recursion stack O(h).
- Every new category should have a three-step learning route, topic README, explicit L3 patterns and a mastery checklist in docs/foundations.md.

## Critical correctness
- Sliding window: define valid state and monotone left bound.
- Two pointers: justify why removing the chosen candidate cannot miss optimum.
- Sorted 3Sum: justify both deduplication loops.
- Backtracking: choice, recursion, undo, and why results require a copy.
- Grid traversal: adjacency, visited marking, connected components, mutation behavior.

## Reference routing
problem-analysis.md, narrative-architecture.md, evidence-and-citation.md, html-design-system.md, svg-production.md, implementation-and-interactivity.md, browser-qa.md, publishing.md, math-typesetting.md.
