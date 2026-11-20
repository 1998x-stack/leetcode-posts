from __future__ import annotations
from collections import Counter
from itertools import product
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

def load(category, slug):
    path = ROOT / "posts" / category / slug / "solution.py"
    spec = importlib.util.spec_from_file_location("next_" + slug.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module.Solution()

def test_linked_list_cycle_identity_and_boundaries():
    fn = load("data-structures", "linked-list-cycle").hasCycle
    class Node:
        def __init__(self, val):
            self.val, self.next = val, None
    assert fn(None) is False
    one = Node(1)
    assert fn(one) is False
    one.next = one
    assert fn(one) is True
    nodes = [Node(x) for x in [3, 2, 0, -4]]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    nodes[-1].next = nodes[1]
    assert fn(nodes[0]) is True
    nodes[-1].next = None
    assert fn(nodes[0]) is False
    a, b, c = Node(7), Node(7), Node(7)
    a.next, b.next = b, c
    assert fn(a) is False

def test_valid_palindrome_examples_and_exhaustive():
    fn = load("two-pointer", "valid-palindrome").isPalindrome
    assert fn("A man, a plan, a canal: Panama") is True
    assert fn("race a car") is False
    assert fn(" ") is True
    for n in range(7):
        for chars in product("aA! 0", repeat=n):
            s = "".join(chars)
            filtered = "".join(ch.lower() for ch in s if ch.isalnum())
            assert fn(s) == (filtered == filtered[::-1])

def brute_trap(height):
    return sum(min(max(height[:i+1]), max(height[i:])) - h for i, h in enumerate(height))

def test_trapping_rain_water_examples_and_exhaustive():
    fn = load("two-pointer", "trapping-rain-water").trap
    assert fn([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert fn([4,2,0,3,2,5]) == 9
    assert fn([1]) == 0
    for n in range(1, 7):
        for values in product(range(4), repeat=n):
            assert fn(list(values)) == brute_trap(list(values))

def brute_replacement(s, k):
    best = 0
    for left in range(len(s)):
        counts = Counter()
        for right in range(left, len(s)):
            counts[s[right]] += 1
            if right-left+1-max(counts.values()) <= k:
                best = max(best, right-left+1)
    return best

def test_character_replacement_examples_and_exhaustive():
    fn = load("sliding-window", "longest-repeating-character-replacement").characterReplacement
    assert fn("ABAB", 2) == 4
    assert fn("AABABBA", 1) == 4
    for n in range(1, 7):
        for chars in product("ABC", repeat=n):
            s = "".join(chars)
            for k in range(n+1):
                assert fn(s, k) == brute_replacement(s, k)

def brute_min_window(s, t):
    if not t:
        return ""
    need = Counter(t)
    best = ""
    for left in range(len(s)):
        counts = Counter()
        for right in range(left, len(s)):
            counts[s[right]] += 1
            if all(counts[ch] >= amount for ch, amount in need.items()):
                candidate = s[left:right+1]
                if not best or len(candidate) < len(best):
                    best = candidate
                break
    return best

def test_minimum_window_examples_and_exhaustive():
    fn = load("sliding-window", "minimum-window-substring").minWindow
    assert fn("ADOBECODEBANC", "ABC") == "BANC"
    assert fn("a", "a") == "a"
    assert fn("a", "aa") == ""
    assert fn("aa", "aa") == "aa"
    for m in range(1, 6):
        for chars in product("ABC", repeat=m):
            s = "".join(chars)
            for n in range(1, min(4, m+1)):
                for target in product("ABC", repeat=n):
                    t = "".join(target)
                    assert fn(s, t) == brute_min_window(s, t)
