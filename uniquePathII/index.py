class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
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

        res = dp[0][0]
        print(res)
        return res


Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
