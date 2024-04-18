class Solution:
    def search(self, nums: list, target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if target == nums[m]:
                print(m)
                return m

            if nums[l] <= nums[m]:
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] > target or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
