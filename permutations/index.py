class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = []

        def backtrack(index, acc):
            visited.append(nums[index])

            if len(acc) == len(nums) - 1:
                res.append(acc.copy() + [nums[index]])
                visited.pop()
                return

            for i in range(len(nums)):
                if nums[i] not in visited:
                    backtrack(i, acc + [nums[index]])
            visited.pop()

        if nums:
            for i in range(len(nums)):
                backtrack(i, [])
        return res
