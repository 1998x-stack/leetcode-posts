class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        if root is None:
            return 0

        stack = [(root, False)]
        heights: dict[int, int] = {}
        diameter = 0

        while stack:
            node, expanded = stack.pop()
            if not expanded:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue

            left_height = heights.pop(id(node.left), 0) if node.left else 0
            right_height = heights.pop(id(node.right), 0) if node.right else 0
            diameter = max(diameter, left_height + right_height)
            heights[id(node)] = 1 + max(left_height, right_height)

        return diameter
