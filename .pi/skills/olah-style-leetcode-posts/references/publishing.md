# Publishing and release workflow

## Before opening a PR

1. Update category/topic registry and category README if needed.
2. Add article HTML, three unique SVGs, solution.py, evidence.json and deterministic tests.
3. Register one manifest entry per problem; use draft while content is incomplete.
4. Update reading paths only with existing, published slugs.
5. Synchronize all Skill mirrors and run the mirror check.
6. Run tests, SVG audit, build, source/site validation and full Chromium QA.
7. Render and validate PDFs when the repository workflow requires them.
8. Review all generated metadata, RSS, sitemap, archive pagination, related cards and local links.

## Pull request

- Use a focused feature branch and a descriptive PR title/body.
- Summarize new problems, category decisions, algorithm patterns and important proof/test details.
- Include CI evidence and known limitations. Never state that a test passed unless it ran.
- Inspect the diff for duplicated diagrams, copied statements, broken links, accidental _site output and unrelated formatting churn.

## Merge and deployment

Merge only after all required checks pass and the task's release policy allows it. Verify the merge commit on main. Check the Pages workflow and environment status. A successful build artifact is not a deployed site. Confirm the public home, archive, topic page and each new article URL. If Pages is not configured or permissions block deployment, state the exact user-side action needed and leave no false success claim.
