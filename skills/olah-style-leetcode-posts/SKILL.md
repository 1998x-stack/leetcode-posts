---
name: olah-style-leetcode-posts
description: Produce rigorous, approachable, visual LeetCode explainers with verified problem facts, explicit algorithm proofs, tested Python solutions, original SVG storyboards, accessible interactions and reliable publication.
---

# LeetCode Algorithm Explainer Skill · v2

## Mission and audience

Teach the reader to derive an algorithm, defend why it works, recognize when the pattern transfers, and implement it safely. The primary audience is university and graduate students and interview learners. Explain unfamiliar terms before using them; prefer a small concrete example over dense jargon. Do not dilute technical truth to make an explanation feel simple.

This Skill adapts the visual publishing system of xm-posts. It does not copy LeetCode's full statement, editorials, code, diagrams or community explanations. Every article is independently authored.

## Non-negotiable editorial contract

A publishable article must answer all seven questions:
1. What exactly is the input, output, and constraint that makes the problem interesting?
2. Why is the obvious approach too slow, too wasteful, or too difficult to reason about?
3. What state does the optimized algorithm maintain?
4. Which invariant or recurrence makes every update safe?
5. Why does the algorithm neither miss a valid answer nor create an invalid one?
6. What are the true time and space costs, including output, recursion, queues, hash tables and mutation?
7. Which adversarial or boundary examples would expose a plausible bug?

A code listing without these answers is not a complete post.

## Phase 0 — Repository preflight

Before editing:
- Read AGENTS.md, README.md, docs/taxonomy.md, docs/editorial.md, this Skill and its relevant references.
- Inspect content/categories.json, content/posts.json, content/reading_paths.json, the target category README, related articles, article CSS, site builder, validator, test conventions and publishing workflow.
- Search the manifest by problem number, canonical slug, English title and key pattern. Do not create duplicate coverage under a different slug.
- Confirm the current branch and base SHA. Never overwrite main directly or silently replace a published article.
- Preserve existing URLs, stable slugs, IDs and asset names unless a deliberate migration is approved.

## Phase 1 — Verify and scope the problem

Use the canonical LeetCode page as the primary authority. Confirm problem number, exact title, difficulty, method/class interface, input semantics, constraints, examples and whether input mutation is permitted. Secondary explanations can help identify pitfalls, but cannot override the official statement.

Record the facts actually used in evidence.json. Separate:
- source facts: stated by the official problem;
- derived claims: recurrence, invariant, correctness and complexity derived by the author;
- local evidence: deterministic tests and browser checks;
- unverified observations: omit them or label them explicitly.

Write a short original Chinese paraphrase. Never reproduce the complete prompt, sample explanation, premium content, editorial prose or screenshots. Link the official problem page prominently.

## Phase 2 — Classify before writing

Choose one primary category and one stable topic. Use tags for secondary patterns. Do not create a new category merely to accommodate one article if an existing category is conceptually correct. Add a category only when it forms a reusable family with a clear description and at least one useful topic.

Current primary families include two pointers, sliding windows, backtracking, graphs/grids, binary search, dynamic programming, monotonic stacks, trees and data-structure design. New patterns should extend the taxonomy deliberately, not fragment it.

State the recognition signal, preconditions and failure boundary. Example: a monotonic stack applies when unresolved elements can be permanently answered or discarded by a later element; it is not a generic replacement for every stack.

## Phase 3 — Build the reasoning before the page

Write a one-page problem brief before creating HTML:
- input/output and the constraint that matters;
- smallest illustrative example and a counterexample;
- brute-force baseline and its complexity;
- candidate pattern and why its preconditions hold;
- state definition, invariant or DP recurrence;
- transition and termination;
- correctness proof outline;
- time, auxiliary-space and output-space bounds;
- expected mutation and API contract;
- tests that could falsify the reasoning.

Use the pattern playbooks in references/pattern-playbooks.md. If two algorithms are plausible, compare them and explain why the chosen one is clearer or more appropriate. Do not present an optimization as optimal without a stated complexity argument.

## Phase 4 — Prove the algorithm

The proof must correspond line-for-line to the submitted implementation.

Use the appropriate proof structure:
- loop invariant: initialization, maintenance, termination;
- binary search: target-preserving interval and a justified half-discard;
- dynamic programming: state meaning, base cases, transition completeness, optimal substructure and evaluation order;
- monotonic stack: stack order, exact pop condition, first qualifying element and amortized push/pop count;
- BFS: queue ordering by depth, level boundary and visited policy;
- linked data structure: map/list bijection, pointer invariants and recency semantics;
- backtracking: complete choices, unique path, undo and output-copy semantics;
- greedy/two pointers: exchange argument or upper bound proving a discarded candidate cannot win.

A proof that only restates the code is not a proof. Include one concrete trace and one adversarial case.

## Phase 5 — Implement and audit complexity

Provide a LeetCode-compatible Python Solution interface and standard-library-only implementation. Keep helper classes local to the article solution where appropriate. Do not rely on unavailable packages, network access, random seeds, platform-specific behavior or notebook state.

Audit:
- every loop and nested loop;
- every item pushed/popped or visited;
- recursive depth and number of states;
- hash-table average-case assumptions;
- sorting and copied input;
- queue width, stack depth and auxiliary structures;
- returned result size separately from working memory;
- whether the implementation mutates its arguments.

Use worst-case bounds where required; call expected/average hash operations what they are. Do not claim O(1) space while allocating a list, set, queue or recursion stack that grows with input.

## Phase 6 — Create a visual storyboard

Every article has at least three distinct original SVG assets:
1. cover.svg — the key mechanism or invariant, recognizable as this article's thumbnail;
2. trace.svg — a concrete state transition with values and labels from the worked example;
3. pitfall.svg — a counterexample, incorrect transition or boundary condition contrasted with the correct rule.

These are three different teaching jobs, not three recolors of one picture. Draft a storyboard and validate its values against the code trace before drawing. Every arrow, region, node, highlight and color must encode a stated fact. Do not use generic cards, decorative network graphs, fake equations or reused covers.

Each SVG is standalone and contains xmlns, viewBox, title, desc, unique IDs, sufficient contrast, legible labels and no remote asset. Aim for 14px or larger labels at nominal desktop width; if the figure is dense, split it into stages instead of shrinking the text. Color must not be the only way to distinguish states.

## Phase 7 — Write the article as a learning sequence

Recommended sequence:
1. Title, one-sentence intuition, difficulty, official problem link and estimated reading time.
2. Original problem summary, example and relevant constraints.
3. Naive idea and why it fails or scales poorly.
4. Visual model and exact state definition.
5. Invariant/recurrence with a plain-language interpretation.
6. Interactive trace with an explanation for each transition.
7. Correctness argument.
8. Complete Python implementation.
9. Time, auxiliary-space and output-space analysis.
10. Pitfalls, boundary cases and related patterns.

Each section must move the reader's understanding forward. Avoid repeating the same explanation in the hero, caption, body and conclusion. Define notation before using it. Use short paragraphs, worked tables and annotated code where they genuinely help.

## Phase 8 — Add interaction without hiding the lesson

The initial state must be meaningful without JavaScript. Controls must be native buttons, keyboard operable, visibly focused and have accessible names. Announce changed step descriptions with aria-live. Provide previous/next and boundary disabled states. Do not autoplay or require pointer dragging.

A trace is a deterministic, explicitly labelled subset of the execution. Never imply that five selected frames are the full run if intermediate operations are omitted. The displayed state, metric, explanation, code and SVG must agree. Interactions must change meaningful algorithm state, not just color or decoration.

## Phase 9 — Verify at multiple layers

Follow references/testing-strategy.md and references/browser-qa.md.

Required checks:
- mirror parity: python scripts/sync_skills.py --check;
- deterministic solution tests: python -m pytest -q;
- brute-force/differential tests for small input domains when feasible;
- static SVG/XML audit: python scripts/audit_svg.py;
- reproducible site build: python scripts/build_site.py;
- article/site validation: python scripts/validate_site.py;
- real Chromium checks for all published articles: python scripts/browser_check_all.py --workers 2;
- PDF render and validation when the publishing workflow requires PDFs.

Inspect 1440, 768, 390 and 360 pixel layouts. Check links, image decoding, SVG geometry, focus order, keyboard interaction, console/page errors, external requests, print output and horizontal overflow. A skipped check is not a pass. Do not weaken a validator merely to make a failing article green; repair the article or explain a genuine false positive with a narrowly scoped fix.

## Phase 10 — Publish responsibly

New content starts as draft while being authored. Only mark it published after the source, code, proof, assets, tests, static build and browser checks agree. Confirm all related-reading routes reference published slugs only. Synchronize the canonical Skill to Claude, Pi, Agent and OpenCode mirrors.

Create a feature branch and PR. Review the complete diff and CI results. Merge only when all required checks pass and the intended workflow permits it. After merge, verify the Pages deployment and public article URL independently. A merged commit, uploaded artifact or successful build is not proof that Pages is live.

## Artifact contract

For every published post:
- posts/<category>/<slug>/index.html
- posts/<category>/<slug>/assets/cover.svg
- posts/<category>/<slug>/assets/trace.svg
- posts/<category>/<slug>/assets/pitfall.svg
- posts/<category>/<slug>/solution.py
- posts/<category>/<slug>/evidence.json
- a deterministic test in tests/test_solutions.py or a focused test module
- one unique manifest entry in content/posts.json
- a registered category/topic and useful reading-path links

Manifest metadata must include slug, title, subtitle, category, topic, status, published, updated, reading_minutes, tags, summary, problem_url and a cover object with a local SVG source and a unique explanatory caption.

## Hard stops

Do not publish when any of these remain:
- wrong title, difficulty, constraints or method signature;
- code and proof describe different algorithms;
- missing edge-case or differential tests where feasible;
- incorrect complexity or omitted mutation/output costs;
- copied statement/editorial or unlicensed diagrams;
- misleading, repeated or semantically wrong SVG;
- broken links, missing image, console error or mobile overflow;
- inaccessible controls or a trace that disagrees with the implementation;
- missing evidence, missing skill mirrors or unverified deployment claims.

## Reference map

- Problem verification and planning: references/problem-analysis.md
- Pattern recognition and proof templates: references/pattern-playbooks.md
- Narrative and visual teaching: references/narrative-architecture.md
- Source/proof/test evidence: references/evidence-and-citation.md
- Test design: references/testing-strategy.md
- Complexity accounting: references/complexity-analysis.md
- HTML/CSS: references/html-design-system.md
- SVG storyboard and verification: references/svg-production.md
- Interactions and Python: references/implementation-and-interactivity.md
- Browser and print QA: references/browser-qa.md
- Release score: references/scorecard.md
- PR, PDF and Pages: references/publishing.md
