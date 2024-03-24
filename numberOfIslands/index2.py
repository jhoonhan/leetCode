import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def __bfs(r, c):
            q = collections.deque()

            q.append((r, c))

            while q:
                row, col = q.popleft()

                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == "1":
                        q.append((r, c))
                        grid[r][c] = "#"

        def __dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            __dfs(r + 1, c)
            __dfs(r - 1, c)
            __dfs(r, c + 1)
            __dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    __dfs(r, c)
                    count += 1

        return count
