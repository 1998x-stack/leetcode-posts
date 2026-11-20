class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        used = [False] * len(nums)
        path: list[int] = []

        def dfs() -> None:
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i, value in enumerate(nums):
                if used[i]:
                    continue
                used[i] = True
                path.append(value)
                dfs()
                path.pop()
                used[i] = False

        dfs()
        return result
