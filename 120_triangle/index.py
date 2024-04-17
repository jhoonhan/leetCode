class Solution:
    def minimumTotal2(self, triangle: list) -> int:
        dp = []
        for i in range(len(triangle)):
            dp.append([])
            for _ in range(len(triangle[i])):
                dp[i].append(float("inf"))

        def dfs(i, level):
            if len(triangle) == 1:
                dp[0][0] = triangle[0][0]
                return

            if level > len(triangle) - 1:
                return 0

            if dp[level][i] != float("inf"):
                print("dp fired")
                return dp[level][i]

            left = dfs(i, level + 1)
            right = dfs(i + 1, level + 1)
            min_val = min(left, right)

            dp[level][i] = triangle[level][i] + min_val

            return dp[level][i]

        dfs(0, 0)
        print(dp[0][0])

        return dp[0][0]

    def minimumTotal(self, triangle: list) -> int:
        dp = [0] * len(triangle) + 1

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])
        return dp[0]


Solution().minimumTotal2([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
