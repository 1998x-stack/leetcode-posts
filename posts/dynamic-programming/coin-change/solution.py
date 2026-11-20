class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        unreachable = amount + 1
        dp = [unreachable] * (amount + 1)
        dp[0] = 0
        for current in range(1, amount + 1):
            for coin in coins:
                if coin <= current:
                    dp[current] = min(dp[current], dp[current - coin] + 1)
        return -1 if dp[amount] == unreachable else dp[amount]
