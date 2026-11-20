from collections import deque


class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level_values)
        return result
