class Solution:
    def hIndex2(self, citations: list) -> int:
        citations.sort()
        length = len(citations)

        res = 0
        for i, n in enumerate(citations):
            res = max(res, min(n, length - i))

        return res

    def hIndex(self, citations: list) -> int:

        citations.sort()
        citations.reverse()

        l = 0
        r = len(citations) - 1
        while l <= r:
            mid = l + ((r - l) // 2)

            if citations[mid] == mid + 1:
                return mid + 1
            elif mid < citations[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l


Solution().hIndex([3, 0, 6, 1, 5])
