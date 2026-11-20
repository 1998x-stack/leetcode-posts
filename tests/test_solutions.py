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
