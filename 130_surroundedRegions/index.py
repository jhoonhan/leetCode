import collections


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        # DFS
        def __dfs(r, c):
            if r in range(rows) and c in range(cols) and board[r][c] == "O":
                board[r][c] = "N"
                __dfs(r - 1, c)
                __dfs(r, c + 1)
                __dfs(r + 1, c)
                __dfs(r, c - 1)

        for r in range(rows):
            __dfs(r, 0)
            __dfs(r, cols - 1)
        for c in range(cols):
            __dfs(0, c)
            __dfs(rows - 1, c)
        # DFS

        # BFS
        def __bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            while q:
                r, c = q.popleft()
                if r in range(rows) and c in range(cols) and board[r][c] == "O":
                    board[r][c] = "N"
                    q.append((r - 1, c))
                    q.append((r, c + 1))
                    q.append((r + 1, c))
                    q.append((r, c - 1))

        for r in range(rows):
            __bfs(r, 0)
            __bfs(r, cols - 1)
        for c in range(cols):
            __bfs(0, c)
            __bfs(rows - 1, c)
        # BFS

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "N":
                    board[r][c] = "O"
