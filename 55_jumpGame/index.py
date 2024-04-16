class Solution:
    # def canJump(self, nums) -> bool:
    #     dp = [0] * len(nums)
    #     dp[-1] = nums[-1]

    #     for i in range(len(nums) - 1, -1, -1):
    #         # if dp[i]:
    #         #     continue

    #         max_val = 0
    #         for j in range(nums[i] + 1):
    #             index = i + j
    #             if index in range(len(nums)):
    #                 # print(f"max:{max_val}, {dp[index]}, {i}")
    #                 max_val = max(max_val, dp[index], i)
    #         dp[i] = max_val

    #     res = dp[0] >= len(nums) - 1
    #     print(res)

    #     return res

    def canJump(self, nums) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0


Solution().canJump([3, 2, 1, 0, 4])
