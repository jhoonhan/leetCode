class Solution:
    def minPathSum2(self, grid: list) -> int:
        # dp = [None] * (len(grid) + 2)
        # mid = len(dp) // 2
        # dp[mid] = grid[-1][-1]
        # r = len(grid) - 1
        # c = len(grid[0]) - 1
        # dp = [[None] * (c + 1)] * (r + 1)
        dp = [
            [0, 0, 0],
            [0, 0, 0],
        ]
        dp[1][2] = 1

        def dfs(r, c, acc):

            if (
                r < 0
                or r > len(grid) - 1
                or c < 0
                or c > len(grid[0]) - 1
                # or grid[r][c] == 0
            ):
                return acc

            acc += grid[r][c]

            left = dfs(r, c - 1, acc)
            top = dfs(r - 1, c, acc)

            acc = min(left, top)
            # print(f"@ r:{r}, c:{c} val: {acc}")
            if r == 0 and c == 0:
                print(acc)

            return acc

        res = dfs(len(grid) - 1, len(grid[0]) - 1, 0)
        print(res)

    def minPathSum(self, grid: list) -> int:
        dp = [[float("inf")] * (len(grid[0]) + 1) for r in range(len(grid) + 1)]

        for r in range(len(grid) - 1, -1, -1):
            for c in range(len(grid[0]) - 1, -1, -1):

                right = dp[r][c + 1]
                bottom = dp[r + 1][c]

                min_val = min(right, bottom)
                if min_val == float("inf"):
                    min_val = 0

                dp[r][c] = grid[r][c] + min_val

        print(dp[0][0])

        return dp[0][0]


Solution().minPathSum2([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
