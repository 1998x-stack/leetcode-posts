class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = sorted(nums)  # 保留调用者的输入
        result: list[list[int]] = []
        n = len(arr)
        for i in range(n - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            if arr[i] > 0:
                break
            left, right = i + 1, n - 1
            while left < right:
                total = arr[i] + arr[left] + arr[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
        return result
