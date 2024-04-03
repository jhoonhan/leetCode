class Solution:
    def uniquePathsWithObstacles2(self, obstacleGrid: list) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp = [[0] * (col + 1) for _ in range(row + 1)]
        for r in range(row):
            for c in range(col):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = None
        # Sets the right value to 1 so that the very last element adds up to 1
        dp[row - 1][col] = 1

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                # If its a block
                if dp[r][c] == None:
                    dp[r][c] = 0
                    continue

                dp[r][c] = dp[r][c + 1] + dp[r + 1][c]

        return dp[0][0]

    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = [0] * col
        dp[-1] = 1

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                if obstacleGrid[r][c]:
                    dp[c] = 0
                elif c + 1 < col:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]

    # DFS with cache
    def uniquePathsWithObstacles3(self, obstacleGrid: list) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        dp = {(row - 1, col - 1): 1}

        def dfs(r, c):

            if r == row or c == col or obstacleGrid[r][c]:
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            bottom = dfs(r + 1, c)
            right = dfs(r, c + 1)
            dp[(r, c)] = bottom + right

            return dp[(r, c)]

        return dfs(0, 0)


Solution().uniquePathsWithObstacles([[0, 1], [0, 0]])
