class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        l = 0
        r = len(matrix[0])
        t = 0
        b = len(matrix)
        while t <= b:
            mid = (t + b) // 2

            if matrix[mid][0] == target:
                return True

            if target > matrix[mid][0]:
                l = mid + 1
            else:
                r = mid - 1

        print(t)


Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
