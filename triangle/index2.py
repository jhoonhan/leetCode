class Solution:
    def minimumTotal(self, triangle: list) -> int:
        dp = [0] * (len(triangle[-1]) + 1)
        print(dp)

        for row in reversed(triangle):
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])


Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
