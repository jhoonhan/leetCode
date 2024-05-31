class Solution:
    def numIslands(self, grid) -> int:
        res = 0
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if r not in range(row) or c not in range(col) or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1

        return res
