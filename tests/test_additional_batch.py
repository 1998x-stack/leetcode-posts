from __future__ import annotations
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def solution(category: str, slug: str):
    path = ROOT / "posts" / category / slug / "solution.py"
    spec = importlib.util.spec_from_file_location("lc_" + slug.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module.Solution()

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
