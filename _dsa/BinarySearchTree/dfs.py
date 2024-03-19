grid = [[]]
rows = len(grid)
cols = len(grid[0])


def dfs(r: int, c: int):
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
        return
    grid[r][c] = "#"
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)
