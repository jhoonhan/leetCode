class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        l = 0
        r = len(nums) - 1
        res = [-1, -1]

        # Find smallest
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                res[0] = m
                r = m - 1

        l = 0
        r = len(nums) - 1

        # Find smallest
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                res[1] = m
                l = m + 1

        return res


Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
