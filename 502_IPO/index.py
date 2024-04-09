import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list, capital: list) -> int:
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1 * p)

            if not maxProfit:
                break
            w += -1 * heapq.heappop(maxProfit)
        return w


Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1])
