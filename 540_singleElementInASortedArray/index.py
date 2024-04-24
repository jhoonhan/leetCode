class Solution:
    def singleNonDuplicate(self, nums: list) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if m - r <= 3:
                res = 0
                for n in nums[l : r + 1]:
                    res = n ^ res
                return res

            if nums[m] != nums[m - 1] and nums[m] != nums[m + 1]:
                return nums[m]

            # if index is even
            if m % 2 == 0:
                if nums[m - 1] == nums[m]:
                    r = m
                else:
                    l = m
            else:
                if nums[m - 1] == nums[m]:
                    l = m
                else:
                    r = m


Solution().singleNonDuplicate([1, 1, 2])
