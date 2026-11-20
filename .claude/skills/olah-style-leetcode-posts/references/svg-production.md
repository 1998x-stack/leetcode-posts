# SVG production: storyboard, draw, export, verify

## Three different teaching assets

1. Cover: the algorithm's central structure at a glance. It must remain legible as a small archive thumbnail.
2. Trace: a real state snapshot or transition from the worked example, using the same values and indices as the article and tests.
3. Pitfall: a tempting incorrect rule, boundary failure or counterexample paired with the correct rule.

Never create three nearly identical SVGs by changing only their title or accent color. Each should answer a different learning question.

## Storyboard before markup

For each figure write: question answered, entities, relationships, direction, state colors, labels, source/example values and expected caption. Cross-check the storyboard against the code and trace fixtures.

Examples:
- rotated binary search: one pivot break, sorted half, retained interval;
- coin change: amount states, base value, candidate transitions and minimum;
- monotonic stack: unresolved indices, decreasing order and pop-on-warmer event;
- tree BFS: parent/child edges, queue frontier and level boundary;
- LRU: hash lookup, doubly linked recency order, head/tail sentinels and eviction end.

## SVG technical contract

- Standalone XML with xmlns and viewBox; include title and desc.
- IDs are unique within the SVG; avoid reusing page IDs.
- Prefer explicit fill/stroke/font attributes so the exported asset renders independently.
- Use a consistent color grammar within the article, with labels, shapes or line styles as redundant cues.
- Minimum label size is approximately 14px at nominal desktop width; split a dense figure into stages rather than shrinking labels.
- Ensure all text remains inside viewBox; test long Chinese labels and small screens.
- No external images, CSS URLs, scripts, event attributes or remote fonts.
- Figure captions state the algorithmic fact shown, not "algorithm overview".
- Keep alt text concise and complementary to the caption.

## Visual correctness review

Check arrow direction, edge endpoints, index labels, comparison operators, stack order, queue order, DP values and cache recency. A beautiful incorrect diagram is a correctness defect. Confirm that the trace image and HTML stepper do not disagree.
