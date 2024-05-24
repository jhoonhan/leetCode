class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
        return []


Solution().twoSum([3, 2, 4], 6)
