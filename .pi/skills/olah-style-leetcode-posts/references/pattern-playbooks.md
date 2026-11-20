# Pattern playbooks: recognition, invariant and proof

Use this as a reasoning aid, not a pattern-matching shortcut. First verify the preconditions on the actual problem.

## Binary search on a sorted or rotated range

Recognition: an ordered range allows half the candidates to be discarded after one comparison. For a rotated array with distinct values, at least one half around mid is sorted.

State: if the target exists, it remains inside the inclusive interval [left, right].

Proof template:
1. Initialization: the full array contains every possible target index.
2. Maintenance: identify a sorted half; retain it only if target lies between its endpoints, otherwise discard it.
3. Termination: the interval becomes empty (absent) or mid matches (present).
Pitfalls: inconsistent inclusive/exclusive boundaries, forgetting equality at an endpoint, assuming duplicate values when the problem guarantees distinct values, or claiming logarithmic time after a linear pivot scan.

## Dynamic programming / unbounded knapsack

Recognition: multiple paths reach the same subproblem and the best answer depends on smaller states.

State must say exactly what dp[x] means. For minimum coin count, dp[x] is the minimum number of coins needed to form amount x. Base dp[0]=0; unreachable states use a sentinel. Transition considers every legal final coin c: dp[x]=min(dp[x], dp[x-c]+1).

Proof template:
- Every nonzero valid combination has some final coin c.
- Removing c leaves a valid smaller subproblem x-c.
- By optimal substructure, replacing that remainder with its optimum cannot worsen the solution.
- Enumerating all available c therefore considers an optimal final choice.
- Increasing x ensures all dependencies are already computed.
Pitfalls: wrong base case, using zero for unreachable states, off-by-one sentinel, confusing unlimited coins with 0/1 use, or changing loop order without explaining the semantics.

## Monotonic stack / next greater element

Recognition: elements wait for a future element that permanently resolves or discards them; a new element can resolve several pending elements at once.

State: store indices, not only values, when the answer needs a distance or position. For next strictly warmer day, stack temperatures are non-increasing from bottom to top; only a strictly warmer current value resolves the top.

Proof: when current i pops j, every index between j and i was already processed and failed to be warmer than j. Thus i is the first future warmer day for j. Every index is pushed once and popped once, giving O(n) total stack operations.

Pitfalls: use > versus >= correctly; equal values are not strictly warmer. Store indices to compute i-j. Do not pop unresolved items at end; their answer remains zero.

## Breadth-first search / level order

Recognition: process nodes by distance/depth in an unweighted graph or by tree level.

State: a FIFO queue contains the frontier in nondecreasing depth order. For level grouping, capture level_size before consuming the current level; children enqueued during this loop belong to the next level.

Proof: FIFO order ensures all depth-d nodes leave the queue before depth-(d+1) nodes. The fixed level_size identifies exactly the current layer.

Pitfalls: using list.pop(0) and silently adding O(n²) shifting cost; iterating while queue length changes and merging adjacent levels; failing to handle an empty root; adding children in an order inconsistent with the requested left-to-right order.

## LRU cache / hash map plus doubly linked list

Recognition: operations require both key lookup and recency-order updates in average O(1).

Invariants:
- every real linked-list node appears exactly once in the map;
- every map value appears exactly once between head and tail sentinels;
- head.next is most-recent and tail.prev is least-recent;
- prev/next pointers are reciprocal;
- no real node is linked twice or left detached while still in the map.

Operation proof:
- get hit: map finds the node, unlink/link-front updates recency, return its value;
- get miss: state is unchanged and return -1;
- put existing: update value and move to front;
- put new: add to map/front; if over capacity, remove tail.prev and its map entry.
Pitfalls: evict before adding when capacity logic is unclear, delete from list but not map, forget to detach both pointers, or fail to move an updated key to most-recent.

## Sliding window

State the exact validity predicate for the current interval. Explain why extending the right edge and moving the left edge restores validity without needing to move left backwards. Do not assume every window predicate is monotone; prove that it is.

## Two pointers

State which candidates are being eliminated. Use sorted monotonicity or an area bound to prove a pointer move cannot discard a better answer. A diagram showing two moving pointers is not itself a proof.

## Backtracking

State path, choices and remaining candidates. Prove every solution maps to a search-tree path, and that pruning excludes only paths that cannot lead to a valid solution. Restore every mutable state and copy emitted results.

## Graph traversal / connected components

Define vertices, edges and adjacency precisely. Mark visited at enqueue/push time to prevent duplicate frontier entries. Distinguish directed/undirected edges, four/eight-neighbor grids and weighted/unweighted paths.

## Pattern comparison

When a problem admits multiple methods, add a short comparison:
- correctness preconditions;
- time and space;
- implementation complexity;
- why the chosen method best teaches the core constraint.
Do not force a single universal template onto structurally different problems.
