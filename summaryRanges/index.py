class Solution:
    def summaryRanges(self, nums: list) -> list:
        if len(nums) < 1:
            return nums
        res = []
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > end + 1:
                if start != end:
                    res.append(str(start) + "->" + str(end))
                else:
                    res.append(str(end))
                start, end = nums[i], nums[i]
            else:
                end = nums[i]

        if start != end:
            res.append(str(start) + "->" + str(end))
        else:
            res.append(str(end))
        return res


Solution().summaryRanges([0, 1, 2, 4, 5, 7])
