class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        res = []

        def backtrack(i, acc):

            if sum(acc) > target:
                return

            if sum(acc) == target:
                res.append(acc)
                return

            for j in range(i, len(candidates)):
                if sum(acc) + candidates[j] > target:
                    break
                backtrack(j, acc + [candidates[j]])

        backtrack(0, [])
        print(res)

    def combinationSum(self, candidates: list, target: int) -> list:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return

            # with
            dfs(i, cur + [candidates[i]], total + candidates[i])
            # without
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


Solution().combinationSum([2, 3, 6, 7], 7)
