class Solution:
    def jump(self, nums: list) -> int:
        if len(nums) <= 1:
            return 0

        count = 0

        i = 0
        while i < len(nums):
            if nums[i] + i >= len(nums) - 1:
                count += 1
                break

            max_val = (0, 0)

            for j in range(1, nums[i] + 1):
                comp_i = i + j
                if comp_i in range(len(nums)):
                    comp_v = (nums[comp_i] + comp_i, comp_i)
                    max_val = max(max_val, comp_v)

            i = max_val[1]
            count += 1
            if i >= len(nums) - 1:
                break

        return count


Solution().jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3])
