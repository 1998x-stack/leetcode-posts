from __future__ import annotations

from itertools import combinations, permutations, product
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def solution(category: str, slug: str):
    path = ROOT / "posts" / category / slug / "solution.py"
    spec = importlib.util.spec_from_file_location("lc_" + slug.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module.Solution()

def test_sliding_window_examples():
    fn = solution("sliding-window", "longest-substring-without-repeating-characters").lengthOfLongestSubstring
    for text, expected in [("", 0), ("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3), ("abba", 2), ("dvdf", 3), ("anviaj", 5)]:
        assert fn(text) == expected

def test_sliding_window_against_bruteforce():
    fn = solution("sliding-window", "longest-substring-without-repeating-characters").lengthOfLongestSubstring
    for n in range(7):
        for seq in product("abc", repeat=n):
            s = "".join(seq)
            expected = max((j - i for i in range(n + 1) for j in range(i, n + 1)
                            if len(set(s[i:j])) == j - i), default=0)
            assert fn(s) == expected

def test_container_examples():
    fn = solution("two-pointer", "container-with-most-water").maxArea
    assert fn([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert fn([1, 1]) == 1
    assert fn([4, 3, 2, 1, 4]) == 16

def test_container_against_bruteforce():
    fn = solution("two-pointer", "container-with-most-water").maxArea
    for n in range(2, 6):
        for heights in product([0, 1, 2, 4], repeat=n):
            assert fn(list(heights)) == max((j - i) * min(heights[i], heights[j])
                                            for i in range(n) for j in range(i+1, n))

def canonical_triples(triples):
    return sorted(set(tuple(sorted(triple)) for triple in triples))

def test_three_sum_examples_and_input_unchanged():
    fn = solution("two-pointer", "three-sum").threeSum
    arr = [-1, 0, 1, 2, -1, -4]
    snapshot = arr[:]
    assert canonical_triples(fn(arr)) == [(-1, -1, 2), (-1, 0, 1)]
    assert arr == snapshot
    assert fn([0, 0, 0, 0]) == [[0, 0, 0]]
    assert fn([]) == []
    assert fn([0, 1, 1]) == []

def test_three_sum_against_bruteforce():
    fn = solution("two-pointer", "three-sum").threeSum
    for n in range(6):
        for seq in product([-2, -1, 0, 1, 2], repeat=n):
            arr = list(seq)
            expected = canonical_triples(triple for triple in combinations(arr, 3) if sum(triple) == 0)
            actual = fn(arr)
            assert canonical_triples(actual) == expected
            assert len(actual) == len(expected)

def test_permutations_matches_itertools():
    fn = solution("backtracking", "permutations").permute
    assert fn([]) == [[]]
    for n in range(1, 6):
        arr = list(range(n))
        actual = fn(arr)
        expected = list(permutations(arr))
        assert sorted(map(tuple, actual)) == sorted(expected)
        assert len({id(row) for row in actual}) == len(actual)  # leaf copies, no aliasing

def islands_reference(grid):
    rows, cols = len(grid), len(grid[0]) if grid else 0
    seen = set()
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1" or (r, c) in seen:
                continue
            count += 1
            stack = [(r, c)]
            seen.add((r, c))
            while stack:
                x, y = stack.pop()
                for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1" and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        stack.append((nx, ny))
    return count

def test_islands_examples_and_mutation():
    fn = solution("graphs", "number-of-islands").numIslands
    grid = [list(row) for row in ["11000", "11000", "00100", "00011"]]
    assert fn(grid) == 3
    assert all(x == "0" for row in grid for x in row)
    assert fn([]) == 0
    assert fn([["0"]]) == 0
    assert fn([["1"]]) == 1
    assert fn([["1", "0"], ["0", "1"]]) == 2  # diagonals are disconnected

def test_islands_against_reference():
    fn = solution("graphs", "number-of-islands").numIslands
    for rows, cols in ((1, 4), (2, 3), (3, 3)):
        for seq in product("01", repeat=rows * cols):
            grid = [list(seq[r*cols:(r+1)*cols]) for r in range(rows)]
            expected = islands_reference(grid)
            copied = [row[:] for row in grid]
            assert fn(copied) == expected

def test_registry_and_original_svg_covers():
    cats = json.loads((ROOT / "content/categories.json").read_text())
    posts = json.loads((ROOT / "content/posts.json").read_text())
    registered = {c["slug"]: {t["slug"] for t in c["topics"]} for c in cats}
    assert len(posts) == 5
    assert sorted(p["status"] for p in posts) == ["published"] * 5
    assert len({p["cover"]["caption"] for p in posts}) == 5
    for post in posts:
        assert post["topic"] in registered[post["category"]]
        folder = ROOT / "posts" / post["category"] / post["slug"]
        assert (folder / post["cover"]["src"]).is_file()
        assert len(list((folder / "assets").glob("*.svg"))) >= 3
        assert (folder / "evidence.json").is_file()
        assert post["problem_url"].startswith("https://leetcode.com/problems/")


# Second batch: binary search, dynamic programming, monotonic stack, tree BFS and LRU design.
def test_rotated_search_exhaustive_rotations():
    fn = solution("binary-search", "search-in-rotated-sorted-array").search
    assert fn([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert fn([4, 5, 6, 7, 0, 1, 2], 3) == -1
    for n in range(1, 9):
        base = list(range(-3, -3 + n))
        for pivot in range(n):
            rotated = base[pivot:] + base[:pivot]
            for target in range(-4, n - 2):
                assert fn(rotated, target) == (rotated.index(target) if target in rotated else -1)

def _coin_change_bfs(coins, amount):
    from collections import deque
    dist = [-1] * (amount + 1)
    dist[0] = 0
    q = deque([0])
    while q:
        x = q.popleft()
        for coin in coins:
            nxt = x + coin
            if nxt <= amount and dist[nxt] == -1:
                dist[nxt] = dist[x] + 1
                q.append(nxt)
    return dist[amount]

def test_coin_change_differential():
    from itertools import combinations
    fn = solution("dynamic-programming", "coin-change").coinChange
    assert fn([1, 2, 5], 11) == 3
    assert fn([2], 3) == -1
    assert fn([1], 0) == 0
    for size in range(1, 4):
        for coins in combinations(range(1, 6), size):
            for amount in range(16):
                assert fn(list(coins), amount) == _coin_change_bfs(coins, amount)

def _daily_temperatures_reference(values):
    out = [0] * len(values)
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[j] > values[i]:
                out[i] = j - i
                break
    return out

def test_daily_temperatures_exhaustive_small_inputs():
    from itertools import product
    fn = solution("monotonic-stack", "daily-temperatures").dailyTemperatures
    assert fn([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert fn([70, 70, 71]) == [2, 1, 0]
    for n in range(1, 7):
        for values in product((70, 71, 72), repeat=n):
            assert fn(list(values)) == _daily_temperatures_reference(values)

class _TestTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right

def _build_test_tree(values):
    from collections import deque
    if not values or values[0] is None:
        return None
    root = _TestTreeNode(values[0])
    q, i = deque([root]), 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = _TestTreeNode(values[i]); q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = _TestTreeNode(values[i]); q.append(node.right)
        i += 1
    return root

def _tree_levels_reference(root):
    levels = []
    def visit(node, depth):
        if node is None: return
        if depth == len(levels): levels.append([])
        levels[depth].append(node.val)
        visit(node.left, depth + 1)
        visit(node.right, depth + 1)
    visit(root, 0)
    return levels

def test_level_order_examples_and_reference():
    fn = solution("trees", "binary-tree-level-order-traversal").levelOrder
    for values in ([], [1], [3, 9, 20, None, None, 15, 7],
                   [1, 2, 3, 4, None, None, 5], [1, None, 2, None, 3],
                   [1, 2, 3, 4, 5, 6, 7]):
        root = _build_test_tree(values)
        assert fn(root) == _tree_levels_reference(root)
    assert fn(None) == []

def _load_lru_class():
    import importlib.util
    path = ROOT / "posts" / "data-structures" / "lru-cache" / "solution.py"
    spec = importlib.util.spec_from_file_location("lc_lru_cache", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module.LRUCache

def _assert_lru_invariants(cache):
    assert cache.head.prev is None and cache.tail.next is None
    assert cache.head.next.prev is cache.head
    assert cache.tail.prev.next is cache.tail
    keys, node = [], cache.head
    while node.next is not cache.tail:
        node = node.next
        assert node.prev.next is node
        keys.append(node.key)
        assert len(keys) <= cache.capacity
    assert len(keys) == len(set(keys)) == len(cache.nodes)
    assert set(keys) == set(cache.nodes)

def test_lru_examples_and_differential():
    from collections import OrderedDict
    import random
    LRUCache = _load_lru_class()
    cache = LRUCache(2)
    cache.put(1, 1); cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3 and cache.get(4) == 4
    _assert_lru_invariants(cache)
    for seed in range(12):
        rng = random.Random(seed)
        capacity = 1 + seed % 4
        cache, reference = LRUCache(capacity), OrderedDict()
        for _ in range(120):
            key = rng.randrange(6)
            if rng.random() < 0.55:
                actual = cache.get(key)
                expected = reference.pop(key, -1)
                if expected != -1: reference[key] = expected
                assert actual == expected
            else:
                value = rng.randrange(100)
                cache.put(key, value)
                reference.pop(key, None); reference[key] = value
                if len(reference) > capacity: reference.popitem(last=False)
            linked, node = [], cache.head.next
            while node is not cache.tail:
                linked.append(node.key); node = node.next
            assert linked == list(reversed(reference.keys()))
            _assert_lru_invariants(cache)

def test_second_batch_manifest_and_assets():
    import json
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "content/posts.json").read_text(encoding="utf-8"))
    slugs = {"search-in-rotated-sorted-array", "coin-change", "daily-temperatures",
             "binary-tree-level-order-traversal", "lru-cache"}
    entries = [p for p in manifest if p["slug"] in slugs]
    assert len(entries) == 5
    for post in entries:
        folder = root / "posts" / post["category"] / post["slug"]
        assert (folder / "index.html").is_file() and (folder / "solution.py").is_file()
        assert (folder / "evidence.json").is_file()
        assert len(list((folder / "assets").glob("*.svg"))) == 3
