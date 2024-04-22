class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [
            [float("inf") for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)
        ]
        for r in range(len(word1) + 1):
            dp[r][-1] = len(word1) - r
        for c in range(len(word2) + 1):
            dp[-1][c] = len(word2) - c

        for r in range(len(word1) - 1, -1, -1):
            for c in range(len(word2) - 1, -1, -1):
                w1 = word1[r]
                w2 = word2[c]

                right = dp[r][c + 1]
                left = dp[r + 1][c]
                diag = dp[r + 1][c + 1]

                if w1 == w2:
                    dp[r][c] = diag
                else:
                    dp[r][c] = 1 + min(right, left, diag)

        return dp[0][0]


Solution().minDistance("horse", "ros")
