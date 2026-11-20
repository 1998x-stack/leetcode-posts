class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        stack = [(root, 1)]
        best = 0
        while stack:
            node, depth = stack.pop()
            best = max(best, depth)
            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))
        return best
