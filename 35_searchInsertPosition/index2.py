class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            mid = nums[m]
            if target == mid:
                return m
            elif target > mid:
                l = m + 1
            else:
                r = m - 1

        return l
