class Solution:
    def lengthOfLIS(self, nums: list) -> int:

        def dfs(i, acc):

            res = []
            if i == len(nums) - 1:
                res.append(acc)
                return res

            for j in range(i + 1, len(nums)):
                if nums[j] <= acc[-1]:
                    res.append(acc)
                    continue
                else:
                    temp = acc + [nums[j]]
                    perms = dfs(j, temp)
                    res.extend(perms)

            return res

        traversed = []
        for i in range(len(nums)):
            traversed.extend(dfs(i, [nums[i]]))
        print(traversed)

        max_c = 0
        for a in traversed:
            max_c = max(max_c, len(a))
        return max_c


Solution().lengthOfLIS([1, 2, 4, 3])
