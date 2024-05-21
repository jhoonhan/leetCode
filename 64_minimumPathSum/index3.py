class Solution:
    def minPathSum(self, grid) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = [[float("inf")] * (col + 1) for _ in range(row + 1)]

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                right = dp[r][c + 1]
                bottom = dp[r + 1][c]
                value = min(right, bottom)

                if value == float("inf"):
                    dp[r][c] = grid[r][c]
                else:
                    dp[r][c] = value + grid[r][c]

        return dp[0][0]


Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
