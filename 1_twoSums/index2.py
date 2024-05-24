class Solution:
    def twoSum(self, nums, target: int):
        hmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hmap:
                return [hmap[diff], i]
            hmap[n] = i
        return []


Solution().twoSum([2, 7, 11, 15], 9)
