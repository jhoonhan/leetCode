class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                comp = s[i : len(w) + i]
                if (i + len(w)) <= len(s) and comp == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        print(dp[0])


Solution().wordBreak("leetcode", ["leet", "code"])
