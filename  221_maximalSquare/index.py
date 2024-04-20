class Solution:
    def maximalSquare(self, matrix: list) -> int:
        res = 0
        row = len(matrix)
        col = len(matrix[0])

        if row == 1 and col == 1:
            return int(matrix[0][0])
        elif row == 1:
            res = int(max(matrix[0]))
            return res
        elif col == 1:
            for r in range(row):
                res = max(res, int(matrix[r][0]))
            return res

        dp = [[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            dp[r][-1] = int(matrix[r][-1])
        for c in range(col):
            dp[-1][c] = int(matrix[-1][c])

        for r in range(row - 2, -1, -1):
            for c in range(col - 2, -1, -1):
                curr = matrix[r][c] == "1"
                right = matrix[r][c + 1] == "1"
                bottom = matrix[r + 1][c] == "1"
                diagonal = matrix[r + 1][c + 1] == "1"

                dpr = dp[r][c + 1]
                dpb = dp[r + 1][c]
                dpd = dp[r + 1][c + 1]

                if curr and right and bottom and diagonal:
                    val = 1 + min(dpr, dpb, dpd)
                    dp[r][c] = val
                    res = max(res, val)
                elif not (curr or right or bottom or diagonal):
                    dp[r][c] = 0
                else:
                    dp[r][c] = 1
                    res = max(res, 1)

        return res**2
