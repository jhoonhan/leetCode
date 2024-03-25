class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def __yeweon_babo(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        __yeweon_babo(nums, 0, len(nums) - 1)
        __yeweon_babo(nums, 0, k - 1)
        __yeweon_babo(nums, k, len(nums) - 1)


# Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)
