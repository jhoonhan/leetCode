class Solution:
    def permute2(self, nums: List[int]) -> List[List[int]]:
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

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            res.extend(perms)
            nums.append(n)

        return res
