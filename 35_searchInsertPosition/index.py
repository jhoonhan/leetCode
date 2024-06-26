class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l


Solution().searchInsert([1, 2, 3, 4, 5, 6, 7], 6)
