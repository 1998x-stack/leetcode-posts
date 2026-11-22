class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            right = stack.pop()
            left = stack.pop()
            if token == "+":
                value = left + right
            elif token == "-":
                value = left - right
            elif token == "*":
                value = left * right
            else:
                quotient = abs(left) // abs(right)
                value = quotient if (left >= 0) == (right >= 0) else -quotient
            stack.append(value)

        return stack[-1]
