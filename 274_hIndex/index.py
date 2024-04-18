class Solution:
    def hIndex(self, citations: list) -> int:
        citations.sort()
        print(citations)
        length = len(citations)

        res = 0
        for i, n in enumerate(citations):
            v1 = n
            v2 = length - i
            v3 = min(v1, v2)
            res = max(res, v3)

        print(res)
        return res


Solution().hIndex([1, 3, 1])
