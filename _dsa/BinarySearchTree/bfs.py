import collections


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BfsGrid:
    grid = [[]]

    visited = set()
    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def bfs(self, r, c):
        q = collections.deque()

        q.append((r, c))
        self.visited.add((r, c))
        # Iterate through the q

        while q:
            row, col = q.popleft()

            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dc, dr in directions:
                r = row + dr
                c = col + dc

                if (
                    r in range(self.rows)
                    and c in range(self.cols)
                    and self.grid[r][c] == "1"
                    and (r, c) not in self.visited
                ):

                    q.append((r, c))
                    self.visited.add((r, c))


class BfsTree:
    queue = collections.deque()
    results = []
    root = Node(3)
    while