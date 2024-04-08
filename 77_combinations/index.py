class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, acc):
            if len(acc) == k:
                res.append(acc.copy())
                return
            for j in range(i, n):
                backtrack(j + 1, acc + [j + 1])

        backtrack(0, [])
        return res

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def bracktrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start, n + 1):
                comb.append(i)
                bracktrack(i + 1, comb)
                comb.pop()

        bracktrack(1, [])

        return res
