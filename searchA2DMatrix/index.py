class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1

        # Find row
        while t <= b:
            mid = (t + b) // 2

            if matrix[mid][0] == target:
                return True

            if target > matrix[mid][0]:
                t = mid + 1
            else:
                b = mid - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[b][mid] == target:
                return True

            if target > matrix[b][mid]:
                l = mid + 1
            else:
                r = mid - 1

        return False


Solution().searchMatrix([[1]], 11)
