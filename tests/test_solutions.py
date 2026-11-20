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


def test_two_sum_examples_and_no_input_mutation():
    fn = solution("arrays-hashing", "two-sum").twoSum
    for nums, target in [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]:
        snapshot = nums[:]
        result = fn(nums, target)
        assert len(result) == 2 and result[0] != result[1]
        assert nums[result[0]] + nums[result[1]] == target
        assert nums == snapshot
    assert fn([1, 2, 3], 20) == []


def test_two_sum_exhaustive_small_inputs():
    fn = solution("arrays-hashing", "two-sum").twoSum
    for n in range(2, 6):
        for values in product([-2, -1, 0, 1, 2], repeat=n):
            nums = list(values)
            for target in range(-3, 4):
                result = fn(nums, target)
                valid = [(i, j) for i in range(n) for j in range(i + 1, n)
                         if nums[i] + nums[j] == target]
                if valid:
                    assert len(result) == 2 and result[0] != result[1]
                    assert nums[result[0]] + nums[result[1]] == target
                else:
                    assert result == []


def test_contains_duplicate_examples_and_exhaustive():
    fn = solution("arrays-hashing", "contains-duplicate").containsDuplicate
    assert fn([1, 2, 3, 1]) is True
    assert fn([1, 2, 3, 4]) is False
    assert fn([1, 1, 1]) is True
    for n in range(1, 7):
        for values in product([0, 1, 2], repeat=n):
            assert fn(list(values)) == (len(set(values)) != n)


def test_product_except_self_examples_and_exhaustive():
    from math import prod
    fn = solution("arrays-hashing", "product-of-array-except-self").productExceptSelf
    assert fn([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert fn([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert fn([0, 0]) == [0, 0]
    assert fn([2, 3]) == [3, 2]
    for n in range(2, 6):
        for values in product([-2, 0, 3], repeat=n):
            nums = list(values)
            expected = [prod(nums[:i] + nums[i + 1:]) for i in range(n)]
            assert fn(nums) == expected


def test_binary_search_exhaustive_sorted_arrays():
    from itertools import combinations
    fn = solution("binary-search", "binary-search").search
    for n in range(0, 7):
        for values in combinations(range(-3, 4), n):
            nums = list(values)
            for target in range(-4, 5):
                expected = nums.index(target) if target in nums else -1
                assert fn(nums, target) == expected


def test_find_first_and_last_position_exhaustive():
    from itertools import combinations_with_replacement
    fn = solution("binary-search", "find-first-and-last-position").searchRange
    for n in range(0, 7):
        for values in combinations_with_replacement(range(-2, 3), n):
            nums = list(values)
            for target in range(-3, 4):
                matches = [i for i, value in enumerate(nums) if value == target]
                expected = [matches[0], matches[-1]] if matches else [-1, -1]
                assert fn(nums, target) == expected


def test_rotated_binary_search_exhaustive():
    from itertools import combinations
    fn = solution("binary-search", "search-in-rotated-sorted-array").search
    for n in range(1, 7):
        for values in combinations(range(-3, 4), n):
            for pivot in range(n):
                nums = list(values[pivot:]) + list(values[:pivot])
                for target in range(-4, 5):
                    expected = nums.index(target) if target in nums else -1
                    assert fn(nums, target) == expected


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def test_maximum_depth_of_binary_tree():
    fn = solution("binary-tree", "maximum-depth-of-binary-tree").maxDepth
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert fn(root) == 3
    assert fn(TreeNode(1, None, TreeNode(2))) == 2
    assert fn(TreeNode(1)) == 1
    assert fn(None) == 0


def test_binary_tree_level_order_traversal():
    fn = solution("binary-tree", "binary-tree-level-order-traversal").levelOrder
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert fn(root) == [[3], [9, 20], [15, 7]]
    assert fn(TreeNode(1)) == [[1]]
    assert fn(None) == []


def test_diameter_of_binary_tree():
    fn = solution("binary-tree", "diameter-of-binary-tree").diameterOfBinaryTree
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert fn(root) == 3
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert fn(root) == 3
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(5)), TreeNode(4, None, TreeNode(6))), TreeNode(9))
    assert fn(root) == 4
    assert fn(TreeNode(1)) == 0


def test_registry_and_original_svg_covers():
    cats = json.loads((ROOT / "content/categories.json").read_text())
    posts = json.loads((ROOT / "content/posts.json").read_text())
    domains = json.loads((ROOT / "content/domains.json").read_text())
    facets = json.loads((ROOT / "content/facets.json").read_text())
    domain_ids = {domain["slug"] for domain in domains}
    registered = {c["slug"]: {t["slug"] for t in c["topics"]} for c in cats}
    assert len({p["slug"] for p in posts}) == len(posts)
    published = [p for p in posts if p["status"] == "published"]
    assert published, "At least one article must be published"
    assert all(p["status"] in {"draft", "published"} for p in posts)
    assert len({p["cover"]["caption"] for p in published}) == len(published), "Published covers must be distinct"
    allowed = {field: {item["slug"] for item in facets[field]}
               for field in ("structures", "techniques", "problem_shapes", "reasoning", "prerequisites")}
    stages = {item["slug"] for item in facets["learning_stages"]}
    for category in cats:
        assert category["domain"] in domain_ids
    for post in posts:
        assert post["topic"] in registered[post["category"]]
        assert set(post["facets"]) == set(allowed) | {"learning_stage"}
        for field, values in allowed.items():
            assert set(post["facets"][field]) <= values
        assert post["facets"]["learning_stage"] in stages
        folder = ROOT / "posts" / post["category"] / post["slug"]
        assert (folder / post["cover"]["src"]).is_file()
        assert len(list((folder / "assets").glob("*.svg"))) >= 3
        assert (folder / "evidence.json").is_file()
        assert post["problem_url"].startswith("https://leetcode.com/problems/")
