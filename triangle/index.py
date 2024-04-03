class Solution:
    def minimumTotal(self, triangle: list) -> int:
        dp = []
        for i in range(len(triangle)):
            dp.append([])
            for j in range(len(triangle[i])):
                dp[i].append(float("inf"))

        def dfs(i, level, acc):
            if len(triangle) == 1:
                dp[0][0] = triangle[0][0]
                return

            if level > len(triangle) - 1:
                return acc

            acc += triangle[level][i]
            dp[level][i] = min(acc, dp[level][i])

            for j in range(i, i + 2):
                dfs(j, level + 1, acc)

            return acc

        dfs(0, 0, 0)
        res = min(dp[-1])
        print(res)

        return res


Solution().minimumTotal([[-10]])
