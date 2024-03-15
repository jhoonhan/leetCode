class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # l = 0
        # r = len(s) - 1
        # while l < r:
        #     s[l], s[r] = s[r], s[l]
        #     l, r = l + 1, r - 1

        stack = []
        for char in s:
            stack.append(char)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1


aang = Solution()

aang.reverseString(["a", "b", "c"])
