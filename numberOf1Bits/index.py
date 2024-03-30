class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 1:
            if n % 2:
                res += 1
            n = n // 2

        if n == 1:
            res += 1

        return res


Solution().hammingWeight(14)
