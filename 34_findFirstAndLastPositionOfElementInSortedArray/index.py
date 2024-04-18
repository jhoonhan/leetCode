class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        l = 0
        r = len(nums) - 1
        res = [-1, -1]

        # find smallest
        while l <= r:
            m = l + ((r - l) // 2)
            # reg BS
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                # When position is met
                if nums[l] == target:
                    res[0] = l
                    break
                if l < m:
                    r = m

        # Find largest
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            # reg BS
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                # When position is met
                if nums[r] == target:
                    res[1] = r
                    break
                if r > m:
                    l = m
                    r -= 1
        print(res)
        return res


Solution().searchRange([5, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 9, 10], 8)
