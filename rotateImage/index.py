class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r - l):
                t = l
                b = r

                temp = matrix[t][l + i]
                # BL to TL
                matrix[t][l + i] = matrix[b - i][l]
                # BR to BL
                matrix[b - i][l] = matrix[b][r - i]
                # TR to BR
                matrix[b][r - i] = matrix[t + i][r]
                # TL to TR
                matrix[t + i][r] = temp

            l += 1
            r -= 1


Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
