class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2):
            index = -1 + (i * -1)
            dp[index] = 1

        for i in range(n - 1, -1, -1):
            if dp[i]:
                continue
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]

    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp


Solution().climbStairs(5)
