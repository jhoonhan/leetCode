class Solution:
    def combine(self, n: int, k: int) -> list:
        res = []

        def backtrack(i, acc):
            if len(acc) == k:
                res.append(acc[:])
                return

            for i in range(i, n):
                backtrack(i + 1, acc + [i + 1])

        backtrack(0, [])
        return res
