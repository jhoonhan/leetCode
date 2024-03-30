class Solution:
    def singleNumber(self, nums: list) -> int:
        res = 0
        for n in nums:
            res = n ^ res

        return res


Solution().singleNumber([2, 2, 1])
