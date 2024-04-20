class Solution:
    def maximalSquare(self, matrix: list) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        res = 0

        for r in range(len(matrix) - 1, -1, -1):
            for c in range(len(matrix[0]) - 1, -1, -1):
                curr = matrix[r][c] == "1"
                right = (
                    matrix[r][c + 1] == "1" if c + 1 in range(len(matrix[0])) else False
                )
                bottom = (
                    matrix[r + 1][c] == "1" if r + 1 in range(len(matrix)) else False
                )
                diagonal = (
                    matrix[r + 1][c + 1] == "1"
                    if c + 1 in range(len(matrix[0])) and r + 1 in range(len(matrix))
                    else False
                )

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

        if res == 1:
            return 1
        elif res > 1:
            return res**2
        else:
            return res


Solution().maximalSquare(
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
)
