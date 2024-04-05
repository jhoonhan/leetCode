class Solution:
    def spiralOrder(self, matrix: list) -> list:
        rs = 0
        re = len(matrix)
        cs = 0
        ce = len(matrix[0])

        res = []
        while rs < re and cs < ce:
            # top right to left
            for num in matrix[rs][cs:ce]:
                res.append(num)
            rs += 1

            # right top to bottom
            for i in range(rs, re):
                res.append(matrix[i][ce - 1])
            ce -= 1

            if not (cs < ce and rs < re):
                break

            # bottom right to left
            for num in reversed(matrix[re - 1][cs:ce]):
                res.append(num)
            re -= 1

            # left bottom to top
            for i in reversed(range(rs, re)):
                res.append(matrix[i][cs])
            cs += 1

        return res


Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
