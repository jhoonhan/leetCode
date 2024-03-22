class Solution:
    def isValid(self, s: str) -> bool:
        map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for char in s:
            print(char)


Solution().isValid("()[]{}")
