class Solution:
    def maxArea(self, height: list) -> int:
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
