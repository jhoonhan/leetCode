class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        rl = len(s1)
        cl = len(s2)
        if rl + cl != len(s3):
            return False

        dp = [[False] * (cl + 1) for _ in range(rl + 1)]

        dp[rl][cl] = True

        for r in range(rl, -1, -1):
            for c in range(cl, -1, -1):
                if r < rl and s1[r] == s3[r + c] and dp[r + 1][c]:
                    dp[r][c] = True
                if c < cl and s2[c] == s3[r + c] and dp[r][c + 1]:
                    dp[r][c] = True

        return dp[0][0]


Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac")
