class Solution:
    def combine(self, n: int, k: int) -> list:
        res = []

        def backtracK(i, acc):
            if len(acc) == k:
                res.append(acc)
                return

            for j in range(i, n):
                backtracK(j + 1, acc + [j + 1])

        backtracK(0, [])

        print(res)
        return res


Solution().combine(4, 2)
