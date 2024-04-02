class Solution:
    def rob(self, nums: list) -> int:
        persis = 0
        increase = 0

        for n in nums:
            new_val = persis + n
            max_val = max(increase, new_val)

            persis = increase
            increase = max_val
            print(f"DP[{n}]: {increase}")

        print(increase)
        return increase


Solution().rob([2, 7, 9, 3, 1])
