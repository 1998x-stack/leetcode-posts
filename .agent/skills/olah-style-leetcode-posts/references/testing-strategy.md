# Testing strategy: make incorrect reasoning fail

## Test layers

1. Contract tests: expected signature, return type, ordering, mutation and empty/missing behavior.
2. Canonical examples: assert exact outputs from the official contract, using independently written fixtures.
3. Boundary tests: smallest valid input, one element, endpoints, amount zero, no solution, equal values, uneven final tree level and capacity one.
4. Adversarial tests: repeated binary-search rotations, duplicate coin denominations, equal temperatures, decreasing temperature runs, sparse trees, update-existing-key and LRU eviction after a touch.
5. Differential tests: compare optimized code with a simple, obviously correct reference on small domains.
6. Invariant tests: inspect map/list links and capacity after each LRU operation; assert monotonic stack results against direct scans.
7. Regression tests: every discovered bug becomes a permanent deterministic fixture.

## Differential recipes

- Rotated search: enumerate strictly increasing arrays, rotate at every pivot and compare with linear search.
- Coin change: enumerate small coin sets and amounts; compare with breadth-first search over reachable totals.
- Daily temperatures: enumerate short sequences over a small temperature alphabet and compare with a nested scan.
- Tree BFS: build small trees with missing children and compare level output with depth-first grouping by depth.
- LRU: compare deterministic operations against collections.OrderedDict and validate list/map bijection after each operation.
- Existing problems: brute-force substring/area/triple enumeration, itertools permutations and independent grid flood-fill.

## Metamorphic checks

- Permuting coin denominations cannot change the minimum count.
- A target absent from a rotated array must remain absent regardless of rotation.
- Equal temperatures do not resolve each other under a strict-warmer contract.
- Adding a leaf only changes the corresponding tree level.
- A successful LRU get changes recency, not key/value membership.

Use exhaustive finite domains where feasible. Otherwise use a fixed seed and state the domain. Do not use flaky time thresholds as correctness tests. A local benchmark is not a claim about LeetCode's infrastructure. Never report tests that were not executed as passed.
