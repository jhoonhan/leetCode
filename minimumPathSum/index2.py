class Solution:
    def minPathSum2(self, grid: list) -> int:
        row = len(grid)
        col = len(grid[0])

        res = []

        def dfs(r, c, acc):
            if r < 0 or r >= row or c < 0 or c >= col:
                return

            if r == row - 1 and c == col - 1:
                res.append(acc + grid[r][c])

            acc += grid[r][c]

            dfs(r + 1, c, acc)
            dfs(r, c + 1, acc)

        dfs(0, 0, 0)
        print(min(res))
        return min(res)

    def minPathSum(self, grid: list) -> int:
        row = len(grid)
        col = len(grid[0])

        dp = [[float("inf")] * (col + 1) for _ in range(row + 1)]

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                bottom = dp[r + 1][c]
                right = dp[r][c + 1]
                min_val = min(bottom, right)

                if min_val == float("inf"):
                    dp[r][c] = grid[r][c]
                    continue

                dp[r][c] = grid[r][c] + min_val

        res = dp[0][0]
        print(res)
        return res


Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
