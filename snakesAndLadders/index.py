class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def __convert(square):
            row = (square - 1) // length
            col = (square - 1) % length
            if row % 2:
                col = length - 1 - col
            return [row, col]

        q = collections.deque()
        q.append([1, 0])  # square number, moves it took
        visited = set()
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                next_square = square + i
                r, c = __convert(next_square)

                # if there is ladder or snake, the value is not -1
                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square == length * length:
                    # When it reaches, return move with one more since it is dealing with next move
                    return moves + 1

                if next_square not in visited:
                    q.append([next_square, moves + 1])
                    visited.add(next_square)
        return -1
