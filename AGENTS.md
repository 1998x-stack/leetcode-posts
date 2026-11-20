# AGENTS.md — leetcode-posts

算法正确性、可复现性与教学清晰度优先于视觉效果。所有新增或修改必须遵循 Skill v2：skills/olah-style-leetcode-posts/SKILL.md。

## Canonical architecture
- Category/topic registry: content/categories.json
- Published/draft manifest: content/posts.json
- Curated learning routes: content/reading_paths.json
- Article source: posts/<category>/<slug>/index.html
- Three unique SVGs: posts/<category>/<slug>/assets/{cover,trace,pitfall}.svg
- Python implementation: solution.py; provenance/proof ledger: evidence.json
- Skill canonical: skills/olah-style-leetcode-posts; mirrors: .claude, .pi, .agent, .opencode
- Static site builder: scripts/build_site.py; do not commit _site or .pdf-cache.

## Required article contract
1. Verify exact problem number/title/difficulty/API/constraints on canonical LeetCode. Paraphrase; never copy the complete statement or editorial.
2. Write a problem brief before HTML: baseline, pattern preconditions, state/invariant or recurrence, initialization, transition, termination, correctness proof and counterexample.
3. The proof must match the implementation. Explain completeness/soundness and why each candidate can be discarded or retained.
4. Audit time, auxiliary space, queue/stack/recursion, output space, input copy and mutation separately. Distinguish expected hash-table operations.
5. Provide three distinct original SVGs: mechanism cover, worked trace and pitfall/counterexample. All labels and arrows must match code/test states.
6. Provide a meaningful static default plus keyboard-accessible stepper; no autoplay; aria-live; visible focus; no-JS remains readable.
7. Python solution uses standard library and the expected LeetCode interface. Add boundary, adversarial and differential tests where feasible.
8. Evidence ledger separates official facts, derived proofs and locally executed checks. Do not invent acceptance rate, ranking or benchmark claims.
9. Mobile/desktop/print/offline QA must cover 1440, 768, 390 and 360 widths. Skips are not passes.
10. Keep taxonomy, unique cover captions, related reading paths and all five Skill mirrors in sync.

## Release commands
```bash
python scripts/sync_skills.py --check
python -m pytest -q
python scripts/audit_svg.py
python scripts/build_site.py
python scripts/validate_site.py
python scripts/browser_check_all.py --workers 2
python scripts/render_pdfs.py
python scripts/validate_site.py --require-pdfs
```

New articles start as draft. Publish only after code, proof, tests, visuals and browser QA agree. PR first; merge only after required CI passes. Verify actual Pages deployment separately from a successful build.
