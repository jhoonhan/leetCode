class Solution:
    def maxProfit(self, prices: list) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1
        return max_profit


Solution().maxProfit([7, 1, 5, 3, 6, 4])
