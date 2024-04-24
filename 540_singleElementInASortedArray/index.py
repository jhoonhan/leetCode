class Solution:
    def singleNonDuplicate(self, nums: list) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        print(res)

        return res


Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
