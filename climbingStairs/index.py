class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, c = 2, 1, 1
        for i in range(n - 2):
            temp_a = a
            temp_b = b
            a = a + b + c
            b = temp_a
            c = temp_b

        print(a)
        return a


Solution().climbStairs(5)
