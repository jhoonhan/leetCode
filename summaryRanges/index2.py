class Solution:
    def summaryRanges(self, nums: list) -> list:
        s = 0
        e = 0
        res = []

        if not nums:
            return res

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            curr = nums[i]

            if curr == prev + 1:
                e += 1
            else:
                # res.append(nums[s : e + 1])
                if s != e:
                    res.append(f"{nums[s]}->{nums[e]}")
                else:
                    res.append(f"{nums[s]}")
                s = i
                e = i
        if s != e:
            res.append(f"{nums[s]}->{nums[-1]}")

        else:
            res.append(f"{nums[-1]}")

        return res


Solution().summaryRanges([])
