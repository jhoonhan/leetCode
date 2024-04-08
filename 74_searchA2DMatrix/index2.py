class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        # find row
        t = 0
        b = row - 1
        while t <= b:
            m = t + ((b - t) // 2)
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                t = m + 1
            else:
                b = m - 1

        # search within row
        l = 0
        r = col - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[b][m] == target:
                print("true")
                return True
            elif matrix[b][m] < target:
                l = m + 1
            else:
                r = m - 1

        print("false")
        return False


Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11)
