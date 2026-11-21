from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]

def solution(category: str, slug: str):
    path = ROOT / "posts" / category / slug / "solution.py"
    spec = importlib.util.spec_from_file_location("new_" + slug.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module.Solution()

def test_valid_anagram_examples_and_exhaustive():
    fn = solution("arrays-hashing", "valid-anagram").isAnagram
    assert fn("anagram", "nagaram") is True
    assert fn("rat", "car") is False
    assert fn("a", "a") is True
    assert fn("ab", "a") is False
    assert fn("aab", "abb") is False
    words = ["".join(chars) for n in range(5) for chars in product("abc", repeat=n)]
    for left in words:
        for right in words:
            assert fn(left, right) == (sorted(left) == sorted(right))

def test_group_anagrams_examples_and_partition():
    fn = solution("arrays-hashing", "group-anagrams").groupAnagrams
    result = fn(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = {frozenset(group) for group in result}
    assert normalized == {frozenset({"eat", "tea", "ate"}), frozenset({"tan", "nat"}), frozenset({"bat"})}
    assert fn([]) == []
    assert fn([""]) == [[""]]
    words = ["".join(chars) for n in range(4) for chars in product("ab", repeat=n)]
    result = fn(words)
    flattened = [word for group in result for word in group]
    assert Counter(flattened) == Counter(words)
    for group in result:
        assert len({tuple(sorted(word)) for word in group}) == 1

def test_top_k_frequent_examples_and_reference():
    fn = solution("data-structures", "top-k-frequent-elements").topKFrequent
    assert set(fn([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert set(fn([1], 1)) == {1}
    for n in range(1, 7):
        for values in product([-1, 0, 1], repeat=n):
            nums = list(values)
            counts = Counter(nums)
            # Skip ties at the k boundary: the problem promises a unique answer.
            ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
            for k in range(1, len(counts) + 1):
                if k < len(ranked) and ranked[k - 1][1] == ranked[k][1]:
                    continue
                assert set(fn(nums, k)) == {value for value, _ in ranked[:k]}

def reference_valid_parentheses(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif not stack or stack[-1] != pairs[char]:
            return False
        else:
            stack.pop()
    return not stack

def test_valid_parentheses_examples_and_exhaustive():
    fn = solution("data-structures", "valid-parentheses").isValid
    for text, expected in [("()", True),("()[]{}", True),("(]", False),("([)]", False),("{[]}", True),("", True),("(((", False)]:
        assert fn(text) is expected
    alphabet = "()[]{}"
    for n in range(7):
        for chars in product(alphabet, repeat=n):
            text = "".join(chars)
            assert fn(text) == reference_valid_parentheses(text)

class ListNode:
    def __init__(self, val, next=None):
        self.val, self.next = val, next

def test_reverse_linked_list_identity_and_boundaries():
    fn = solution("data-structures", "reverse-linked-list").reverseList
    assert fn(None) is None
    single = ListNode(7)
    assert fn(single) is single and single.next is None
    nodes = [ListNode(value) for value in [1, 2, 3, 4, 5]]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    result = fn(nodes[0])
    seen, values = set(), []
    current = result
    while current:
        assert id(current) not in seen, "cycle introduced"
        seen.add(id(current))
        values.append(current.val)
        current = current.next
    assert values == [5, 4, 3, 2, 1]
    assert seen == {id(node) for node in nodes}, "must reuse every original node exactly once"
