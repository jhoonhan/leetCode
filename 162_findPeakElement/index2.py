class Solution:
    def findPeakElement(self, nums) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if m > 0 and nums[m] < nums[m - 1]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m


Solution().findPeakElement([1, 2, 1, 3, 5, 5, 6])
