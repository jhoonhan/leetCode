class Solution:
    def permute(self, nums: list) -> list:
        res = []

        if len(nums) == 1:
            return [nums[:]]

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            nums.append(n)
            res.extend(perms)

        return res


Solution().permute([1, 2, 3])
