class Solution:
    def findPeakElement2(self, nums: list) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            left = float("-inf") if mid <= 0 else nums[mid - 1]
            center = nums[mid]
            right = float("-inf") if mid >= len(nums) - 1 else nums[mid + 1]

            if center > left and center > right:
                return mid

            if center < left:
                r = mid - 1
            elif center < right:
                l = mid + 1

        return 0

    def findPeakElement(self, nums: list) -> int:
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


Solution().findPeakElement([-2147483648, -2147483647])
