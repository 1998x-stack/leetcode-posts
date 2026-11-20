# Problem analysis and authoring brief

## 1. Establish the exact contract

Read the canonical problem page, not a copied problem list. Record:
- problem number, exact English title and stated difficulty;
- required class and method signature;
- input/output shape and ordering requirements;
- whether values are unique, sorted, positive, bounded or mutable;
- maximum input sizes and any explicit time-complexity requirement;
- whether repeated use, empty input, missing target or impossible output is allowed.

Do not infer a constraint from a sample. A sample demonstrates behavior; it does not define the full domain.

## 2. Write an original summary

Explain the task in two to four sentences. Keep the semantic contract intact: continuous substring versus subsequence, strict versus non-strict comparison, four-direction versus diagonal adjacency, one-use versus unlimited items, average versus worst-case complexity. Link to the official page for the complete statement.

## 3. Identify the algorithmic pressure

Ask what makes brute force expensive:
- repeated scans of the same range;
- recomputing the same subproblem;
- enumerating permutations or combinations;
- revisiting already solved next-greater queries;
- repeatedly sorting or searching;
- updating both lookup and order without a shared invariant.

Write a real baseline and its upper bound. Avoid vague phrases such as "too slow" without explaining why.

## 4. Select a pattern using its preconditions

Name the recognition signal, the required property and the failure boundary. Examples:
- binary search requires a monotone decision or a sorted region;
- sliding window needs a condition that can be restored by moving a boundary;
- DP needs a valid state and recurrence over smaller states;
- monotonic stack needs a one-way resolution/discard rule;
- BFS relies on FIFO order and equal-cost edges for shortest unweighted distance;
- LRU needs constant-time lookup plus constant-time order updates.

If the property is absent, the pattern is not justified.

## 5. Build a falsifiable trace

Choose an example that triggers the important branch, not just a happy path. Add a counterexample for a common bug:
- binary search: target exactly at left/right or absent;
- DP: unreachable amount and zero amount;
- monotonic stack: equal values and a decreasing suffix;
- BFS: empty tree and uneven final level;
- LRU: update existing key, touch an old key, then evict.

Record exact states after each operation. These states become the stepper, SVG labels and test expectations.

## 6. Plan the proof

Before writing HTML, state:
- invariant/state meaning;
- initialization/base case;
- transition/maintenance;
- why the transition preserves correctness;
- termination and answer extraction;
- completeness: why every possible valid answer is represented;
- uniqueness/no-duplication when relevant.

For dynamic programming, explain the optimal substructure and why the recurrence considers every legal final choice. For amortized algorithms, explain total operations rather than claiming each loop iteration is constant.

## 7. Audit the implementation contract

Use the platform's expected signature. Mention imported helpers. If TreeNode or another platform type is supplied by LeetCode, do not pretend the article's code defines it. If a custom helper class is required (e.g. LRU node), include it in the complete solution. State whether the algorithm mutates its arguments.

## 8. Complexity worksheet

Use variables that match the problem:
- n: number of elements/nodes;
- A: target amount;
- C: number of coin denominations;
- w: maximum tree width;
- k: cache capacity.

Count time, working memory, recursion/queue/stack and output separately. State expected hash-table behavior and whether sorting allocates a copy.

## 9. Editorial review

Ask a peer to explain the algorithm from the article alone. If they cannot state the invariant, simulate one difficult branch, and explain the complexity without reading the code comments, the article is not ready.
