class Solution:
    def search(self, nums: list, target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if target == nums[mid]:
                return mid

            # left sorted?
            if nums[l] <= nums[mid]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted?
            else:
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
