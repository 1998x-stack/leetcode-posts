# Complexity analysis worksheet

Define variables explicitly: n elements/nodes, m rows, w maximum frontier width, A target amount, C coin types, k cache capacity, h tree height.

## Time

- Bound each loop and each nested loop.
- Check whether inner work restarts or advances monotonically.
- For stack/queue algorithms, count total pushes and pops; a nested while loop can still be O(n) when each item is removed once.
- Include sorting and copied inputs.
- For hash tables, distinguish average-case O(1) from worst-case guarantees.
- For graph traversal, use O(V+E); for DP, count states times transitions.

## Space

Report auxiliary working memory, recursion stack, queue/monotonic stack, returned output and input copies separately.

Reference examples:
- rotated binary search: O(1) auxiliary;
- coin change: O(A) DP array;
- daily temperatures: O(n) stack and O(n) output;
- level-order traversal: O(w) queue and O(n) returned levels;
- LRU: O(k) map entries and O(k) linked nodes.

Never call output memory free. Do not omit a BFS queue, recursion stack or copied/sorted input. State expected dictionary behavior.
