import collections


class Solution:
    def snakesAndLadders(self, board) -> int:
        dice = 6
        goal = len(board) * len(board[0])
        board.reverse()

        def convert(square):
            row = (square - 1) // len(board)
            col = (square - 1) % len(board)
            if row % 2:
                col = len(board) - 1 - col
            return [row, col]

        q = collections.deque([[1, 0]])
        visited = set()

        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                next_square = square + i
                r, c = convert(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square == goal:
                    return moves + 1

                if next_square not in visited:
                    q.append([next_square, moves + 1])
                    visited.add(next_square)

        return -1


Solution().snakesAndLadders(
    [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
)
