class Solution:
    def uniquePathsWithObstacles2(self, obstacleGrid: list) -> int:
        grid = obstacleGrid
        row = len(grid)
        col = len(grid[0])
        dp = {(row - 1, col - 1): 1}

        def dfs(r, c):
            if r == row or c == col or grid[r][c]:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            bottom = dfs(r + 1, c)
            right = dfs(r, c + 1)
            dp[(r, c)] = bottom + right

            return dp[(r, c)]

        print(dfs(0, 0))
        return dfs(0, 0)

    def uniquePathsWithObstacles3(self, obstacleGrid: list) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp = [[0] * (col + 1) for _ in range(row + 1)]
        dp[row - 1][col] = 1

        # for r in range(row):
        #     for c in range(col):
        #         if obstacleGrid[r][c] == 1:
        #             dp[r][c] = None

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if dp[r][c] == 1:
                    dp[r][c] = 0
                    continue

                dp[r][c] = dp[r][c + 1] + dp[r + 1][c]

        print(dp[0][0])
        return dp[0][0]

    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [0] * col
        dp[-1] = 1

        for r in reversed(range(row)):
            for c in reversed(range(col)):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                elif c + 1 < col:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]


Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
