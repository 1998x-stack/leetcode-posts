class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        one_step_before = 1
        two_steps_before = 2
        for _ in range(3, n + 1):
            one_step_before, two_steps_before = (
                two_steps_before,
                one_step_before + two_steps_before,
            )
        return two_steps_before
