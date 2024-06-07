class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        res = []

        def dfs(i, acc, total):
            if total == target:
                res.append(acc[:])
                return
            if i >= len(candidates) or total > target:
                return

            # with
            dfs(i, acc + [candidates[i]], total + candidates[i])

            # without
            dfs(i + 1, acc, total)

        dfs(0, [], 0)

        return res


Solution().combinationSum([2, 3, 6, 7], 3)
