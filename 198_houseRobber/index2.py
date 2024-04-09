class Solution:
    def rob(self, nums: list) -> int:
        prev = 0
        local_max = 0

        for num in nums:
            new_val = prev + num
            max_val = max(local_max, new_val)

            prev = local_max
            local_max = max_val
        return local_max


Solution().rob([1, 2, 3, 1])
