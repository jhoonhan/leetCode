class Solution:
    def minimumTotal(self, triangle: list) -> int:
        dp = [0] * (len(triangle) + 1)

        for i in range(len(triangle) - 1, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
