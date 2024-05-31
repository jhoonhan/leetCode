class Solution:
    def solve(self, board: list) -> None:
        row_len = len(board)
        col_len = len(board[0])

        def dfs(r, c):
            if r not in range(row_len) or c not in range(col_len):
                return

            if board[r][c] == "O":
                board[r][c] = "#"
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        # for r in range(row_len):
        #     for c in range(col_len):
        #         if board[r][c] == "O":
        #             dfs(r, c)

        for r in range(row_len):
            dfs(r, 0)
            dfs(r, col_len - 1)
        for c in range(col_len):
            dfs(0, c)
            dfs(row_len - 1, c)

        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"

        print(board)

        return board


Solution().solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]])
