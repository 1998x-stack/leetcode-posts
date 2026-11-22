from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adjacency = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            adjacency[prerequisite].append(course)
            indegree[course] += 1

        ready = deque(course for course, degree in enumerate(indegree) if degree == 0)
        completed = 0

        while ready:
            course = ready.popleft()
            completed += 1
            for dependent in adjacency[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    ready.append(dependent)

        return completed == numCourses
