class Solution:
    def threeSum(self, nums: list) -> list:
        print("aang")
        s_arr = sorted(nums)
        print(s_arr)
        for i in range(len(s_arr)):
            target = 0 - s_arr[i]
            arr = s_arr[i + 1 :]
            l = 0
            r = len(arr) - 1


Solution().threeSum([-1, 0, 1, 2, -1, -4])
