import collections


class Solution:
    def numIslands(self, grid) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()

            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dc, dr in directions:
                    r = row + dr
                    c = col + dc

                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                coord = (r, c)
                if grid[r][c] == "1" and coord not in visited:
                    bfs(r, c)
                    islands += 1

        return islands


class Solution2:
    def numIslands(self, grid) -> int:
        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "#"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        rows = len(grid)
        cols = len(grid[0])

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        print(grid)
        print(count)

        return count


sol = Solution2()
sol.numIslands(
    [
        ["1", "1", "1", "0"],
        ["1", "1", "0", "1"],
        ["1", "1", "0", "0"],
        ["0", "0", "0", "0"],
    ]
)
