class Solution:
    def numIslands(self, grid) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and is not in visited:
                    



sol = Solution()
sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])