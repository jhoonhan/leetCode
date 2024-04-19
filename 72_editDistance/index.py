class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        print("awesome God")
        dp = [
            [float("inf") for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)
        ]
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for r in range(len(word1) - 1, -1, -1):
            for c in range(len(word2) - 1, -1, -1):
                w1 = word1[r]
                w2 = word2[c]
                if w1 == w2:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1])

        return dp[0][0]


Solution().minDistance("intention", "execution")
