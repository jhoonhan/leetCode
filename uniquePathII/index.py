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
                res = 0
                # If its a block
                if dp[r][c] == None:
                    dp[r][c] = 0
                    continue

                dp[r][c] = dp[r][c + 1] + dp[r + 1][c]

        return dp[0][0]

    # DFS brute force
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        def dfs(r, c):

            if r < 0 or r > row - 1 or c < 0 or c > col - 1 or obstacleGrid[r][c] == 1:
                return 0

            if r == row - 1 and c == col - 1 and obstacleGrid[r][c] != 1:
                return 1

            bottom = dfs(r + 1, c)
            right = dfs(r, c + 1)

            return bottom + right

        return dfs(0, 0)


Solution().uniquePathsWithObstacles([[0, 1], [0, 0]])
