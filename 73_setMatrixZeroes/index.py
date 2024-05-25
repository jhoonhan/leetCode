class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # First pass, convert to #
        row_len = len(matrix)
        col_len = len(matrix[0])

        for r in range(row_len):
            for c in range(col_len):
                val = matrix[r][c]
                if val == 0:
                    for i in range(row_len):
                        if matrix[i][c] != 0:
                            matrix[i][c] = "#"
                    for j in range(col_len):
                        if matrix[r][j] != 0:
                            matrix[r][j] = "#"

        # Second pass, convert all # to 0
        for r in range(row_len):
            for c in range(col_len):
                if matrix[r][c] == "#":
                    matrix[r][c] = 0

        print(matrix)


Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
