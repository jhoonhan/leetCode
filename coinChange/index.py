class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        print(dp[amount])
        return dp[amount] if dp[amount] != amount + 1 else -1


Solution().coinChange([1, 2, 5], 11)
