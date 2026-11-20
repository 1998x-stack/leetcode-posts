class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def lower_bound() -> int:
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def upper_bound() -> int:
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        left = lower_bound()
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        return [left, upper_bound() - 1]
