class Solution:
    def lengthOfLIS2(self, nums: list) -> int:
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

    def lengthOfLIS(self, nums: list) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


Solution().lengthOfLIS([1, 2, 4, 3])
