# Python implementation and interactive teaching

## Reference implementation

- Use the required LeetCode class/method interface.
- Include every helper class and import required by the solution.
- Avoid relying on platform-provided names beyond the documented problem interface (TreeNode is provided by the judge for tree problems).
- Keep the main implementation readable and deterministic.
- Explain input mutation and any expected/average hash-table behavior.
- If an alternative implementation is shorter but hides the algorithmic structure (e.g. OrderedDict for a custom LRU lesson), use the explicit data structure as the primary solution and mention the library alternative separately.

## Interaction data model

Treat a trace as a sequence of named, deterministic snapshots. Each snapshot must include visible items/nodes/indices, semantic role of each item (active, resolved, candidate, pivot, evicted, etc.), a concise explanation of the transition, a metric or state summary, and the exact example input and step number.

The stepper's visible state, metric and prose must be generated from the same snapshot object. Do not maintain separate hand-written values in the DOM.

## Accessible controls

- Use real button elements with type=button and explicit accessible names.
- Previous/next controls are disabled at the correct boundaries.
- Use aria-live=polite for the changing explanation or status.
- Provide visible keyboard focus and arrow-key navigation when the container owns focus.
- Respect prefers-reduced-motion; never autoplay.
- The first snapshot is useful before JavaScript runs.
- A no-JavaScript reader still sees the key concept, SVG, proof and full code.

## Honesty

An illustrative trace is not an execution engine unless it actually executes the submitted solution. Label selected states as a trace excerpt if intermediate operations are omitted. Never claim the visualization benchmarks, executes arbitrary user input or validates code unless it truly does.

## Test interaction meaning

Browser QA should click a control and assert a meaningful state change in text, values, order or status. A button changing only its own color is not an algorithm demonstration.
