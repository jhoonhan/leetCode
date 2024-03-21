class Solution:
    def minSubArrayLen(self, target: int, nums: list) -> int:
        l = 0
        r = 0
        total = 0
        res = len(nums) + 1
        while r < len(nums):
            total += nums[r]

            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1

            r += 1

        if res == len(nums) + 1:
            return 0
        else:
            return res


sol = Solution()
sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
