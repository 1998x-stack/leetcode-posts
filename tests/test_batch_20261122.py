from __future__ import annotations

from itertools import permutations, product
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def solution(category: str, slug: str):
    path = ROOT / "posts" / category / slug / "solution.py"
    spec = importlib.util.spec_from_file_location("batch_" + slug.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module.Solution()


def test_reverse_polish_examples_and_truncation_toward_zero():
    fn = solution("data-structures", "evaluate-reverse-polish-notation").evalRPN
    assert fn(["2", "1", "+", "3", "*"]) == 9
    assert fn(["4", "13", "5", "/", "+"]) == 6
    assert fn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert fn(["-7", "2", "/"]) == -3
    assert fn(["7", "-2", "/"]) == -3
    assert fn(["-7", "-2", "/"]) == 3
    assert fn(["2", "5", "-"]) == -3


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def make_list(values):
    nodes = [Node(value) for value in values]
    for left, right in zip(nodes, nodes[1:]):
        left.next = right
    return (nodes[0] if nodes else None), nodes


def read_list(head):
    values, nodes, seen = [], [], set()
    while head is not None:
        assert id(head) not in seen, "merged list contains a cycle"
        seen.add(id(head))
        values.append(head.val)
        nodes.append(head)
        head = head.next
    return values, nodes


def test_merge_two_sorted_lists_reuses_nodes_and_handles_empty_inputs():
    fn = solution("data-structures", "merge-two-sorted-lists").mergeTwoLists
    left, left_nodes = make_list([1, 2, 4])
    right, right_nodes = make_list([1, 3, 4])
    merged = fn(left, right)
    values, nodes = read_list(merged)
    assert values == [1, 1, 2, 3, 4, 4]
    assert {id(node) for node in nodes} == {id(node) for node in left_nodes + right_nodes}
    assert len(nodes) == len(left_nodes) + len(right_nodes)
    assert fn(None, None) is None
    only, only_nodes = make_list([0])
    assert fn(None, only) is only_nodes[0]


def test_merge_two_sorted_lists_exhaustive_small_inputs():
    fn = solution("data-structures", "merge-two-sorted-lists").mergeTwoLists
    sequences = [[]]
    for length in range(1, 4):
        sequences.extend(
            [list(values) for values in product(range(3), repeat=length) if list(values) == sorted(values)]
        )
    for left_values in sequences:
        for right_values in sequences:
            left, left_nodes = make_list(left_values)
            right, right_nodes = make_list(right_values)
            merged = fn(left, right)
            values, nodes = read_list(merged)
            assert values == sorted(left_values + right_values)
            assert len(nodes) == len(left_nodes) + len(right_nodes)
            assert {id(node) for node in nodes} == {id(node) for node in left_nodes + right_nodes}


def test_climbing_stairs_examples_and_recurrence():
    fn = solution("dynamic-programming", "climbing-stairs").climbStairs
    expected = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    for n, answer in enumerate(expected, start=1):
        assert fn(n) == answer
    assert fn(45) == 1836311903


def brute_rob(nums):
    best = 0
    for mask in range(1 << len(nums)):
        if mask & (mask << 1):
            continue
        total = sum(value for i, value in enumerate(nums) if mask & (1 << i))
        best = max(best, total)
    return best


def test_house_robber_examples_and_exhaustive_small_arrays():
    fn = solution("dynamic-programming", "house-robber").rob
    assert fn([1, 2, 3, 1]) == 4
    assert fn([2, 7, 9, 3, 1]) == 12
    assert fn([1, 4, 5, 4, 1]) == 8
    assert fn([0, 0, 0]) == 0
    assert fn([]) == 0
    for length in range(8):
        for nums in product(range(4), repeat=length):
            assert fn(list(nums)) == brute_rob(list(nums))


def has_topological_order(num_courses, edges):
    for order in permutations(range(num_courses)):
        position = {course: index for index, course in enumerate(order)}
        if all(position[source] < position[target] for source, target in edges):
            return True
    return False


def test_course_schedule_examples_and_edge_cases():
    fn = solution("graphs", "course-schedule").canFinish
    assert fn(2, [[1, 0]]) is True
    assert fn(2, [[1, 0], [0, 1]]) is False
    assert fn(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) is True
    assert fn(3, [[1, 0], [2, 1], [0, 2]]) is False
    assert fn(3, []) is True
    assert fn(1, [[0, 0]]) is False


def test_course_schedule_exhaustive_three_vertex_graphs():
    fn = solution("graphs", "course-schedule").canFinish
    vertices = range(3)
    possible_edges = [(source, target) for source in vertices for target in vertices]
    for flags in product((0, 1), repeat=len(possible_edges)):
        edges = [edge for edge, include in zip(possible_edges, flags) if include]
        prerequisites = [[target, source] for source, target in edges]
        assert fn(3, prerequisites) == has_topological_order(3, edges)
