class Solution:
    def spiralOrder(self, matrix: list) -> list:
        row_start = 0
        row_end = len(matrix)
        col_start = 0
        col_end = len(matrix[0])

        res = []
        while row_start <= row_end and col_start <= col_end:
            # Row-Top
            res += matrix[row_start][col_start:col_end]
            row_start += 1
            if row_start >= row_end or col_start >= col_end:
                break

            # Col-Right
            for i in range(row_start, row_end):
                res.append(matrix[i][col_end - 1])
            col_end -= 1
            if row_start >= row_end or col_start >= col_end:
                break

            # Row-Bottom REVERSE
            temp = matrix[row_end - 1][col_start:col_end]
            temp.reverse()
            res += temp
            row_end -= 1
            if row_start >= row_end or col_start >= col_end:
                break

            # Col-Left REVERSE
            for i in range(row_end - 1, row_start - 1, -1):
                res.append(matrix[i][col_start])
            col_start += 1

        return res

    def spiralOrder_neet(self, matrix: list) -> list:
        res = []
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        while left < right and top < bottom:
            # Top
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Right
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # Bottom
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        print(res)


Solution().spiralOrder_neet([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
