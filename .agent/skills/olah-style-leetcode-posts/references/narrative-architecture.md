# Narrative architecture: teach the reasoning, not the trick

## The article's learning arc

### 1. Orient
State the problem in original language, the input/output shape, the relevant constraints and a small concrete example. Link the official problem.

### 2. Establish the baseline
Show the most direct approach in one paragraph or a small trace. Quantify repeated work or state explosion. Do not ridicule the baseline: it explains the optimization target.

### 3. Reveal the hidden structure
Introduce the property that makes the faster method possible: sorted order, overlapping subproblems, monotone waiting states, FIFO depth order, or coupled lookup/order invariants.

### 4. Name the state
Define every pointer, DP entry, stack item, queue layer, node link or cache order. A reader should be able to inspect a diagram and say what each item means.

### 5. Walk through a difficult transition
For each step explain what changed, why it is legal, what candidates are discarded or retained, how the invariant remains true, and what the current answer/state means.

### 6. Prove correctness
Use initialization/maintenance/termination or a pattern-specific proof. Include completeness and soundness. Do not substitute "the loop eventually finds it" for a proof.

### 7. Implement
Provide the complete platform-compatible code. Explain the two or three lines where the invariant is maintained. Avoid narrating every obvious syntax token.

### 8. Audit complexity and edge cases
Separate time, auxiliary space and output space. Show at least one bug-shaped counterexample and its correction.

### 9. Transfer
Name one nearby pattern and one condition under which the current approach would stop working. Avoid a generic "practice more" conclusion.

## Style rules

- Write for a technical reader who may be new to this pattern.
- Define terms such as invariant, frontier, monotonicity, optimal substructure and amortized analysis at first use.
- Use small numbers and realistic state snapshots.
- Avoid long unbroken prose, fake urgency, excessive emojis, interview hype and decorative slogans.
- Do not repeat the same point in title, subtitle, hero, figure caption and body.
- Use equations only when they clarify a recurrence or bound; explain each symbol in words.
