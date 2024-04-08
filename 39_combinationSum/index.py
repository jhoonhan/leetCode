class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, acc):
            # Base cases
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
        return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
