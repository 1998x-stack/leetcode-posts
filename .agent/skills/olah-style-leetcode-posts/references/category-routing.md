# Category and topic routing

Use one primary category for browsing and one primary topic for learning paths. Secondary tags can connect across categories.

| Primary category | Use when the central proof is about | Example topics |
|---|---|---|
| two-pointer | safely eliminating one or more ordered candidates | opposite-direction, sorted enumeration |
| sliding-window | maintaining a contiguous interval | variable window, frequency window |
| backtracking | exploring and restoring a choice path | permutations, pruning |
| graphs | reachability, connectivity or graph traversal | grid traversal, shortest path |
| binary-search | monotone ordered search space | rotated sorted array |
| dynamic-programming | optimal substructure over smaller states | unbounded knapsack |
| monotonic-stack | resolving pending elements by a later element | next greater, next warmer |
| trees | parent/child traversal and depth/level order | level-order BFS |
| data-structures | coordinating lookup with an explicit mutable structure | LRU cache |

Do not classify by one incidental data structure. For example, a BFS tree traversal belongs to trees because the output is grouped by tree level; a grid flood-fill belongs to graphs. An LRU cache belongs to data-structures because the main lesson is maintaining a lookup/order invariant across operations.
